"""Class `CashRequestProcessor` to load, merge, and clean data.

Usage example:
    processor = CashRequestProcessor('File1.csv', 'File2.csv')
    processor.load_data()
    processor.merge_data()
    processor.clean_data()
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

from utils import find_timestamp_columns, timestamp_to_seconds


class TransactionProcessor:
    def __init__(self, bank_file, transaction_file, cash_request_file):
        self.cash_request_file = cash_request_file
        self.bank_file = bank_file
        self.transaction_file = transaction_file
        self.bank = None
        self.cash_request = None
        self.transaction = None

    def load_data(self):
        self.cash_request = pd.read_csv(self.cash_request_file)
        self.bank = pd.read_csv(self.bank_file)
        self.transaction = pd.read_csv(self.transaction_file)

    def merge_data(self):
        self.transaction = pd.merge(
            self.transaction, self.bank[["account_id", "user_id"]], on="account_id", how="left"
        )
        self.transaction = pd.merge(
            self.transaction, self.cash_request[["user_id", "status"]], on="user_id", how="left"
        )

    def clean_data(self):  # 'df.method({col: value} à tester pour pandas !!
        self.transaction.drop_duplicates(inplace=True)

        # self.cash_request = self.cash_request.drop(columns="device_version")

        timestamp_columns = find_timestamp_columns(self.transaction)
        for column_name in timestamp_columns:
            self.transaction[column_name] = self.transaction[column_name].apply(
                lambda x: timestamp_to_seconds(x) if pd.notna(x) else x
            )
            self.transaction[column_name].fillna("0", inplace=True)

        self.transaction["bridge_category"].fillna("0", inplace=True)
        self.transaction["recurrent_group_id"].fillna("0", inplace=True)
        self.transaction["status"].fillna("Inconnu", inplace=True)

        self.transaction.drop_duplicates(inplace=True)

        # Raise an error if there are still null values
        if self.transaction.isnull().sum().sum() > 0:
            raise ValueError(
                "Il y'a encore des valeurs null dans le dataset après nettoyage.",
                self.transaction.isnull().sum(),
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

        # transfer_type_mapping = {"instant": 0, "regular": 1}
        # self.cash_request["transfer_type"] = self.cash_request["transfer_type"].map(
        #     transfer_type_mapping
        # )

        # recovery_mapping = {
        #     "completed": 0,
        #     "pending": 1,
        #     "pending_direct_debit": 2,
        #     "No incident": 3,
        #     "cancelled": 4,
        # }
        # self.cash_request["recovery_status"] = self.cash_request["recovery_status"].map(
        #     recovery_mapping
        # )

        # label_encoder = LabelEncoder()
        # self.cash_request["card_description"] = label_encoder.fit_transform(
        #     self.cash_request["card_description"].astype(str)
        # )
        # self.cash_request["name"] = label_encoder.fit_transform(
        #     self.cash_request["name"]
        # )

    def save_cleaned_data(self, output_file="Data/transaction2.0.csv"):
        self.transaction.to_csv(output_file, index=False)
