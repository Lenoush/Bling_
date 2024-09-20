"""Main module for processing cash request data and training models.

Usage:
    python main.py
"""

from data_cleanup import TransactionProcessor
from data_processor import CashRequestProcessor
from train_model import ModelTrainer

# Preprocess Data - cash_request
# processor = CashRequestProcessor("Data/cashrequest.csv", "Data/bank account.csv")
# processor.load_data()
# processor.merge_data()
# processor.clean_data()
# processor.preprocess_data()
# processor.save_cleaned_data()

# trainer = ModelTrainer(processor.cash_request)


# Preprocess Data - transaction
cleanup = TransactionProcessor("Data/bank account.csv", "Data/transactions.csv", "Data/cashrequest.csv")
cleanup.load_data()
cleanup.merge_data()
cleanup.clean_data()
# cleanup.preprocess_data()
cleanup.save_cleaned_data()

# # # Train Models
trainer = ModelTrainer(cleanup.transaction)
trainer.prepare_data()
trainer.train_logistic_regression()
trainer.train_decision_tree()
trainer.train_random_forest()