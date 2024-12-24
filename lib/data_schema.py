import pandas as pd
from loguru import logger
from pandera import Check, Column, DataFrameSchema, SeriesSchema

INPUT_SCHEMA = DataFrameSchema(
    {
        "PolNum": Column(int),
        "CalYear": Column(int),
        "Gender": Column(str, Check.isnin(["Male", "Female"])),
        "Type": Column(str, Check.isin(["C", "E", "D", "B", "A", "F"])),
        "Category": Column(str, Check.isnin(["Large", "Medium", "Small"])),
        "Age": Column(int, Check.greater_thanor_equal_to(0)),
        "Group1": Column(int),
        "Bonus": Column(int),
        "Poldur": Column(int, Check.greater_than_or_equal_to(0)),
        "Value": Column(float, Check.greater_than_or_equal_to(0)),
        "Adind": Column(int),
        "SubGroup2": Column(str),
        "Density": Column(float, Check.greater_than_or_equal_to(0)),
    },
    strict=True,
    coerce=True,
)

TARGET_SCHEMA = SeriesSchema(
    int,
    checks=[
        Check.isin([0, 1]),
    ],
    nullable=False,
    name="target",
)


def validate_schemas(x: pd.DataFrame, y: pd.Series) -> tuple:
    """Validate input and target dataframes againts their respective schemas."""
    validated_x = INPUT_SCHEMA.validate(x)
    logger.info("Successfully validated INPUT_SCHEMA.")
    validated_y = TARGET_SCHEMA.validate(y)
    logger.info("Successfully validated TARGET_SCHEMA.")
    return validated_x, validated_y
