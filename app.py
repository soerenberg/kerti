"""Streamlit app."""
import pathlib
from typing import Any, Dict, Tuple

import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import yaml
import yfinance


@st.cache
def import_portfolio(path: pathlib.Path) -> Dict[str, Any]:
    """Read portfolio info from file."""
    with open(path, "r") as file_obj:
        return yaml.safe_load(file_obj)


@st.cache
def import_ticker_data(ticker: str,
                       period: str) -> Tuple[pd.DataFrame, Dict[str, Any]]:
    """Import data and info for a given ticker from yahoo finance.

    Args:
        ticker: ticker name, e.g. 'AAPL'.
        period: yfinance period, e.g. 'ytd' or '1mo'.

    Returns:
        pd.DataFrame: data for the given period
        dict: various information fields from yfinance
    """
    ticker = yfinance.Ticker(ticker)
    if ticker is None:
        raise ValueError(f"{ticker}!")
    return ticker.history(period=period), ticker.info


def candle_plot(data: pd.DataFrame) -> go.Figure:
    """Simple plotly candlestick plot.

    Args:
        data: needs columns Open, High, Low, Close and datetime index.

    Returns:
        plotly figure
    """
    fig = go.Figure(data=[
        go.Candlestick(x=data.index,
                       open=data['Open'],
                       high=data['High'],
                       low=data['Low'],
                       close=data['Close'])
    ])
    return fig


def run():
    """Run streamlit application"""
    portfolio = import_portfolio(pathlib.Path("portfolio.yaml"))

    periods = "1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max".split(",")

    period = st.sidebar.selectbox("period:", periods)

    for unit in portfolio:
        data, info = import_ticker_data(unit["ticker"], period)

        st.markdown(f"## {info['longName']}")
        with st.beta_expander("info"):
            for name, value in info.items():
                if value:
                    st.markdown(f"**{name}**: {value}")
        st.write(candle_plot(data))


if __name__ == "__main__":
    run()
