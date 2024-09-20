"""Class `CashRequestProcessor` to load, merge, and clean cash_request data.

Usage example:
    processor = CashRequestProcessor('File1.csv', 'File2.csv')
    processor.load_data()
    processor.merge_data()
    processor.clean_data()
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

from utils import find_timestamp_columns, timestamp_to_seconds


class CashRequestProcessor:
    def __init__(self, cash_request_file, bank_file):
        self.cash_request_file = cash_request_file
        self.bank_file = bank_file
        self.cash_request = None
        self.bank = None

    def load_data(self):
        self.cash_request = pd.read_csv(self.cash_request_file)
        self.bank = pd.read_csv(self.bank_file)

    def merge_data(self):
        self.cash_request = pd.merge(
            self.cash_request, self.bank["user_id", "name"], on="user_id", how="left"
        )

    def clean_data(self):  # 'df.method({col: value} à tester pour pandas !!
        self.cash_request.drop_duplicates(inplace=True)

        self.cash_request = self.cash_request.drop(columns="device_version")

        timestamp_columns = find_timestamp_columns(self.cash_request)
        for column_name in timestamp_columns:
            self.cash_request[column_name] = self.cash_request[column_name].apply(
                lambda x: timestamp_to_seconds(x) if pd.notna(x) else x
            )
            self.cash_request[column_name].fillna("0", inplace=True)

        self.cash_request["name"].fillna("Non connu", inplace=True)
        self.cash_request["deleted_account_id"].fillna("0", inplace=True)
        self.cash_request["user_id"].fillna("0", inplace=True)
        self.cash_request["allowed_amount"].fillna("0", inplace=True)
        self.cash_request["recovery_status"].fillna("No incident", inplace=True)
        self.cash_request["transfer_type"].fillna("Inconnu", inplace=True)
        self.cash_request["card_description"].fillna("Inconnu", inplace=True)

        self.cash_request["cash_request_debited_date"].fillna("0", inplace=True)
        self.cash_request["cash_request_received_date"].fillna("0", inplace=True)

        self.cash_request.drop_duplicates(inplace=True)

        # Raise an error if there are still null values
        if self.cash_request.isnull().sum().sum() > 0:
            raise ValueError(
                "Il y'a encore des valeurs null dans le dataset après nettoyage.",
                self.cash_request.isnull().sum(),
            )

    def preprocess_data(self):
        status_mapping = {
            "active": 0,
            "canceled": 1,
            "direct_debit_rejected": 2,
            "direct_debit_sent": 3,
            "expired": 4,
            "money_back": 5,
            "rejected": 6,
        }
        self.cash_request["status"] = self.cash_request["status"].map(status_mapping)

        transfer_type_mapping = {"instant": 0, "regular": 1}
        self.cash_request["transfer_type"] = self.cash_request["transfer_type"].map(
            transfer_type_mapping
        )

        recovery_mapping = {
            "completed": 0,
            "pending": 1,
            "pending_direct_debit": 2,
            "No incident": 3,
            "cancelled": 4,
        }
        self.cash_request["recovery_status"] = self.cash_request["recovery_status"].map(
            recovery_mapping
        )

        label_encoder = LabelEncoder()
        self.cash_request["card_description"] = label_encoder.fit_transform(
            self.cash_request["card_description"].astype(str)
        )
        self.cash_request["name"] = label_encoder.fit_transform(
            self.cash_request["name"]
        )

    def save_cleaned_data(self, output_file="Data/with_2.0.csv"):
        self.cash_request.to_csv(output_file, index=False)
