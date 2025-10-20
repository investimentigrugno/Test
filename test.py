from tradingview_screener import Query
import streamlit as st

def test_fundamental_data():
    try:
        ticker = "NASDAQ:AAPL"
        columns = [
            'name', 'description', 'country', 'sector', 'close',
            'market_cap_basic', 'total_revenue_qoq_growth_fy', 'gross_profit_qoq_growth_fq',
            'net_income_qoq_growth_fq', 'earnings_per_share_diluted_qoq_growth_fq',
            'price_earnings_ttm', 'price_free_cash_flow_ttm', 'total_assets',
            'total_debt', 'shrhldr_s_equity_fq', 'operating_margin',
            'net_margin_ttm', 'free_cash_flow_qoq_growth_fq'
        ]

        query = Query().set_markets('america').set_tickers(ticker).select(*columns)
        total_count, df = query.get_scanner_data()

        st.write(f"Totale risultati: {total_count}")
        if df.empty:
            st.warning(f"Nessun dato trovato per {ticker}")
        else:
            st.success(f"Dati trovati per {ticker}:")
            st.dataframe(df.head())

    except Exception as e:
        st.error(f"Errore durante il test: {e}")

if __name__ == "__main__":
    test_fundamental_data()
