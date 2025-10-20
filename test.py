import streamlit as st
from tradingview_screener import Query
import pandas as pd

def test_multi_ticker_columns():
    markets = [
        'america', 'australia', 'belgium', 'brazil', 'canada', 'chile', 'china', 'italy',
        'czech', 'denmark', 'egypt', 'estonia', 'finland', 'france', 'germany', 'greece',
        'hongkong', 'hungary', 'india', 'indonesia', 'ireland', 'israel', 'japan', 'korea',
        'kuwait', 'lithuania', 'luxembourg', 'malaysia', 'mexico', 'morocco', 'netherlands',
        'newzealand', 'norway', 'peru', 'philippines', 'poland', 'portugal', 'qatar', 'russia',
        'singapore', 'slovakia', 'spain', 'sweden', 'switzerland', 'taiwan', 'uae', 'uk',
        'venezuela', 'vietnam', 'crypto'
    ]

    tickers = [
        'NASDAQ:AAPL', 'ASX:BHP', 'BMFBOVESPA:PETR4', 'TSX:BMO', 'BVC:CCUCO', 'SSE:600519',
        'MIL:ENEL', 'CSE:DSV', 'EGX:EGTS', 'HEX:NOKIA', 'EURONEXT:ORA', 'XETR:BMW',
        'HKEX:0700', 'NSE:RELIANCE', 'IDX:TISI', 'ISE:CRH', 'TSE:7203', 'KRX:005930',
        'KSE:000270', 'LTU:GRG', 'LUX:RTL', 'KLS:GLB', 'BMV:GMEXICOB', 'CAS:IAM', 'AMS:PHIA',
        'NZX:ANZ', 'OBX:YAR', 'LSE:BA', 'PSE:AP', 'WSE:CDR', 'LIS:EDP', 'QSI:QNBK', 'MCX:SBER',
        'SGX:DBS', 'BX:MBK', 'BME:ITX', 'OMX:VITR', 'SWX:NESN', 'TPE:2330', 'ADX:ADCB', 'LSE:HSBA',
        'BCV:PCG', 'VN:VCB', 'CRYPTO:BTC'
    ]

    columns = [
        'name', 'description', 'country', 'sector', 'close',
        'market_cap_basic', 'total_revenue_yoy_growth_fq', 'gross_profit_yoy_growth_fq',
        'net_income_yoy_growth_fq', 'earnings_per_share_diluted_yoy_growth_fy',
        'price_earnings_ttm', 'price_free_cash_flow_ttm', 'total_assets',
        'total_debt', 'operating_margin',
        'net_margin_ttm', 'free_cash_flow_yoy_growth_fy'
    ]

    results = {}

    for ticker in tickers:
        st.write(f"Querying {ticker}...")
        try:
            query = Query().set_markets(*markets).set_tickers(ticker).select(*columns)
            total, df = query.get_scanner_data()

            if df.empty:
                st.warning(f"Nessun dato trovato per {ticker}")
                continue

            df = df.head(1)
            data_presence = {col: not pd.isna(df.iloc[0].get(col, None)) and df.iloc[0].get(col, "") != "" for col in columns}
            results[ticker] = data_presence

        except Exception as e:
            st.error(f"Errore per {ticker}: {e}")

    comparison_df = pd.DataFrame(results).T.fillna(False)
    st.write("Confronto colonne con dati disponibili per ticker:")
    st.dataframe(comparison_df)

if __name__ == "__main__":
    test_multi_ticker_columns()
