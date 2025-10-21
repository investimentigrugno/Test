import streamlit as st
from tradingview_screener import Query
import pandas as pd

def test_single_ticker():
    markets = [
        'america', 'australia', 'belgium', 'brazil', 'canada', 'chile', 'china', 'italy',
        'czech', 'denmark', 'egypt', 'estonia', 'finland', 'france', 'germany', 'greece',
        'hongkong', 'hungary', 'india', 'indonesia', 'ireland', 'israel', 'japan', 'korea',
        'kuwait', 'lithuania', 'luxembourg', 'malaysia', 'mexico', 'morocco', 'netherlands',
        'newzealand', 'norway', 'peru', 'philippines', 'poland', 'portugal', 'qatar', 'russia',
        'singapore', 'slovakia', 'spain', 'sweden', 'switzerland', 'taiwan', 'uae', 'uk',
        'venezuela', 'vietnam', 'crypto'
    ]

    columns = [
        'name', 'description', 'country', 'sector', 'close',
        'market_cap_basic', 'total_revenue_yoy_growth_fy', 'gross_profit_yoy_growth_fy',
        'net_income_yoy_growth_fy', 'earnings_per_share_diluted_yoy_growth_fy',
        'price_earnings_ttm', 'price_free_cash_flow_ttm', 'total_assets',
        'total_debt', 'operating_margin', 'ebitda_yoy_growth_fy',
        'net_margin_ttm', 'free_cash_flow_yoy_growth_fy', 'price_sales_ratio',
        'capex_per_share_ttm', 'capital_expenditures_yoy_growth_ttm', 'enterprise_value_to_free_cash_flow_ttm',
        'free_cash_flow_cagr_5y', 'invent_turnover_current', 'price_target_low', 'price_target_high', 'price_target_median',
        'revenue_forecast_fq', 'earnings_per_share_forecast_fq'
    ]

    # Barra di ricerca per il ticker
    st.title("🔍 Analisi Dati Fondamentali Ticker")
    ticker = st.text_input("Inserisci il ticker (es. NASDAQ:AAPL):", "NASDAQ:AAPL")

    if st.button("🔍 Cerca Dati"):
        if ticker:
            st.write(f"Querying {ticker}...")
            try:
                query = Query().set_markets(*markets).set_tickers(ticker).select(*columns)
                total, df = query.get_scanner_data()

                if df.empty:
                    st.warning(f"❌ Nessun dato trovato per {ticker}")
                else:
                    st.success(f"✅ Dati trovati per {ticker}")
                    df = df.head(1)
                    
                    # Mostra i dati completi
                    st.subheader("📊 Dati Completi")
                    st.dataframe(df)
                    
                    # Analisi presenza dati per colonna CON VALORI
                    st.subheader("📋 Presenza Dati per Colonna")
                    data_info = []
                    for col in columns:
                        value = df.iloc[0].get(col, None)
                        is_present = not pd.isna(value) and value != ""
                        stato = "✅ Presente" if is_present else "❌ Assente"
                        valore = value if is_present else "N/A"
                        data_info.append({
                            'Colonna': col,
                            'Stato': stato,
                            'Valore': valore
                        })
                    
                    presence_df = pd.DataFrame(data_info)
                    st.dataframe(presence_df, use_container_width=True)

            except Exception as e:
                st.error(f"❌ Errore per {ticker}: {e}")
        else:
            st.warning("⚠️ Inserisci un ticker valido")

if __name__ == "__main__":
    test_single_ticker()
