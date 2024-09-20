"""Utility functions for data processing."""

import re
import pandas as pd


def timestamp_to_seconds(timestamp_str):
    timestamp = pd.to_datetime(timestamp_str, utc=True)
    epoch = pd.Timestamp("1970-01-01", tz="UTC")
    time_diff = timestamp - epoch
    return time_diff.total_seconds()


def find_timestamp_columns(df):
    timestamp_columns = []

    pattern_time = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\+\d{2}"
    pattern_date = r"\d{4}-\d{2}-\d{2}"

    for col in df.columns:
        if (
            df[col].astype(str).apply(lambda x: bool(re.match(pattern_time, x))).any()
            or df[col]
            .astype(str)
            .apply(lambda x: bool(re.match(pattern_date, x)))
            .any()
        ):
            timestamp_columns.append(col)

    return timestamp_columns
