import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.graph_objects import Figure


def plot_numerical_distributions(df: pd.DataFrame, numerical_features: list) -> list[Figure]:
    """Plots the distribution of numerical features in the given DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing the numerical features to be plotted.
        numerical_features (list): A list of strings representing the names of the numerical features to be plotted.

    Returns:
        list[Figure]: A list of plotly Figure objects, each representing the distribution of a numerical feature.
    """
    figures = []
    for col in numerical_features:
        fig = px.histogram(df, x=col, title=f"Distribution of {col}")
        figures.append(fig)
    return figures


def plot_categorical_counts(df: pd.DataFrame, categorical_features: list) -> list[Figure]:
    """Plots the count distribution of categorical features in the given DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing the categorical features to be plotted.
        categorical_features (list): A list of strings representing the names of the categorical features to be plotted.

    Returns:
        list[Figure]: A list of plotly Figure objects, representing the count distribution of a categorical feature.
    """
    figures = []
    for col in categorical_features:
        fig = px.histogram(df, x=col, title=f"Count of {col}", color=col)
        figures.append(fig)
    return figures


def plot_scatter(df: pd.DataFrame, x_col: str, y_col: str, **kwargs: str) -> Figure:
    """Plots a scatter plot of two features in the given DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing the numerical features to be plotted.
        x_col (str): The name of the column representing the x-axis values.
        y_col (str): The name of the column representing the y-axis values.
        **kwargs (str): Additional keyword arguments to be passed to the px.scatter function for customization.

    Returns:
        Figure: A plotly Figure object representing the scatter plot of the two features.
    """
    fig = px.scatter(df, x=x_col, y=y_col, title=f"{x_col} vs. {y_col}", **kwargs)
    return fig


def plot_box_plot(df: pd.DataFrame, x_col: str, y_col: str) -> Figure:
    """Plots a box plot of the distribution of `y_col` by `x_col` in the given DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing the data to be plotted.
        x_col (str): The name of the column representing the x-axis values (categories).
        y_col (str): The name of the column representing the y-axis values (distribution).

    Returns:
        Figure: A plotly Figure object representing the box plot of the distribution of `y_col` by `x_col`.
    """
    fig = px.box(df, x=x_col, y=y_col, title=f"Distribution of {y_col} by {x_col}")
    return fig


def plot_correlation_heatmap(df: pd.DataFrame, numerical_features: list) -> Figure:
    """Plots a correlation heatmap for the given numerical features in the DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame containing the numerical features to be plotted.
        numerical_features (list): A list of strings representing the names of the numerical features to be plotted.

    Returns:
        Figure: A plotly Figure object representing the correlation heatmap of the numerical features.
    """
    corr = df[numerical_features].corr()
    fig = go.Figure(data=go.Heatmap(z=corr.values, x=corr.columns, y=corr.columns, colorscale="Viridis"))
    fig.update_layout(title="Correlation Heatmap for Numerical Features")
    return fig
