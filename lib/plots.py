import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def plot_numerical_distributions(df: pd.DataFrame, numerical_features: list) -> None:  # noqa: D103
    for col in numerical_features:
        fig = px.histogram(df, x=col, title=f"Distribution of {col}")
        fig.show()


def plot_categorical_counts(df: pd.DataFrame, categorical_features: list) -> None:  # noqa: D103
    for col in categorical_features:
        fig = px.histogram(df, x=col, title=f"Count of {col}", color=col)
        fig.show()


def plot_scatter(df: pd.DataFrame, x_col: str, y_col: str, **kwargs: str) -> None:  # noqa: D103
    fig = px.scatter(df, x=x_col, y=y_col, title=f"{x_col} vs. {y_col}", **kwargs)
    fig.show()


def plot_box_plot(df: pd.DataFrame, x_col: str, y_col: str) -> None:  # noqa: D103
    fig = px.box(df, x=x_col, y=y_col, title=f"Distribution of {y_col} by {x_col}")
    fig.show()


def plot_correlation_heatmap(df: pd.DataFrame, numerical_features: list) -> None:  # noqa: D103
    corr = df[numerical_features].corr()
    fig = go.Figure(data=go.Heatmap(z=corr.values, x=corr.columns, y=corr.columns, colorscale="Viridis"))
    fig.update_layout(title="Correlation Heatmap for Numerical Features")
    fig.show()
