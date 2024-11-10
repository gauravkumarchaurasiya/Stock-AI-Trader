import streamlit as st
from src.data.data_loader import load_data
from src.strategies.bollinger_band import BollingerBandStrategy
from src.backtest.backtester import Backtester
from src.utils.visualizations import plot_stock_data

st.title("Backtest Engine")

# Load and display data
file_path = st.file_uploader("Upload NSE Stock Data CSV", type=["csv"])
if file_path is not None:
    data = load_data(file_path)
    st.write("Stock Data", data)

    # Strategy selection
    strategy = st.selectbox("Select Strategy", ["Bollinger Band", "Moving Average"])
    initial_capital = st.number_input("Initial Capital", min_value=1000, step=1000)

    # Run backtest
    if st.button("Run Backtest"):
        if strategy == "Bollinger Band":
            backtester = Backtester(data, BollingerBandStrategy, initial_capital)
        # Add other strategies as needed

        backtester.run_backtest()
        final_value, positions = backtester.get_results()

        st.write(f"Final Portfolio Value: {final_value}")
        st.write("Positions", positions)

        # Visualize results
        plot_stock_data(data)