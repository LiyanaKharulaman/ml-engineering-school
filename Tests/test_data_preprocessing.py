import os
import sys

import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "../"))

import pandas as pd
import pandas.testing as pdt

from lib.data_preprocessing import create_target, drop_cols


@pytest.mark.parametrize(
    "df_input, df_expected, target_col_name",
    [
        (
            pd.DataFrame({"Date": [1, 2], "Numtppd": [2, 0]}),
            pd.DataFrame({"Date": [1, 2], "Numtppd": [2, 0], "target": [1, 0]}),
            "target",
        ),
        (
            pd.DataFrame({"Date": [2], "Numtppd": [2]}),
            pd.DataFrame({"Date": [2], "Numtppd": [2], "target": [1]}),
            "target",
        ),
    ],
)
def test_create_target(df_input: pd.DataFrame, df_expected: pd.DataFrame, target_col_name: str) -> None:  # noqa: D103
    df_output = create_target(df_input, target_col_name)
    pdt.assert_frame_equal(df_output, df_expected)


@pytest.mark.parametrize(
    "df_input, x_expected, y_expected, columns_to_drop, target_col_name",
    [
        (
            pd.DataFrame(
                {
                    "Date": [1, 2],
                    "Numtppd": [2, 0],
                    "Numtpbi": [1, 2],
                    "Indtppd": [1, 2],
                    "Indtpbi": [1, 2],
                    "target": [1, 0],
                }
            ),
            pd.DataFrame({"Date": [1, 2]}),
            pd.Series([1, 0], name="target"),
            ["Numtppd", "Numtpbi", "Indtppd", "Indtpbi"],
            "target",
        ),
        (
            pd.DataFrame({"Date": [1], "Numtppd": [2], "Numtpbi": [1], "Indtppd": [1], "Indtpbi": [1], "target": [1]}),
            pd.DataFrame({"Date": [1]}),
            pd.Series([1], name="target"),
            ["Numtppd", "Numtpbi", "Indtppd", "Indtpbi"],
            "target",
        ),
    ],
)
def test_drop_cols(  # noqa: D103
    df_input: pd.DataFrame, x_expected: pd.DataFrame, y_expected: pd.Series, columns_to_drop: list, target_col_name: str
) -> None:
    x_output, y_output = drop_cols(df_input, columns_to_drop, target_col_name)
    pdt.assert_frame_equal(x_output, x_expected)
    pdt.assert_series_equal(y_output, y_expected)


@pytest.mark.parametrize(
    "df_input, target_col_name",
    [
        (pd.DataFrame({"Date": [1, 2], "target": [1, 0]}), "target"),
        (pd.DataFrame({"Date": [1, 2]}), "target"),
    ],
)
def test_keyerror_create_target(df_input: pd.DataFrame, target_col_name: str) -> None:  # noqa: D103
    with pytest.raises(KeyError):
        create_target(df_input, target_col_name)


@pytest.mark.parametrize(
    "df_input, columns_to_drop, target_col_name",
    [
        (
            pd.DataFrame({"Date": [1, 2], "Numtppd": [2, 0], "Numtpbi": [1, 2], "Indtpbi": [1, 2], "target": [1, 0]}),
            ["Numtppd", "Numtpbi", "Indtppd", "Indtpbi"],
            "target",
        ),
        (
            pd.DataFrame({"Date": [1, 2], "Numtppd": [2, 0], "Numtpbi": [1, 2], "Indtppd": [1, 2], "Indtpbi": [1, 2]}),
            ["Numtppd", "Numtpbi", "Indtppd", "Indtpbi"],
            "target",
        ),
    ],
)
def test_keyerror_drop_cols(df_input: pd.DataFrame, columns_to_drop: list, target_col_name: str) -> None:  # noqa: D103
    with pytest.raises(KeyError):
        drop_cols(df_input, columns_to_drop, target_col_name)
