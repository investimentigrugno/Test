import streamlit as st
from tradingview_screener import Query

def test_fundamental_data():
    markets = [
        'america', 'australia', 'belgium', 'brazil', 'canada', 'chile', 'china', 'italy',
        'czech', 'denmark', 'egypt', 'estonia', 'finland', 'france', 'germany', 'greece',
        'hongkong', 'hungary', 'india', 'indonesia', 'ireland', 'israel', 'japan', 'korea',
        'kuwait', 'lithuania', 'luxembourg', 'malaysia', 'mexico', 'morocco', 'netherlands',
        'newzealand', 'norway', 'peru', 'philippines', 'poland', 'portugal', 'qatar', 'russia',
        'singapore', 'slovakia', 'spain', 'sweden', 'switzerland', 'taiwan', 'uae', 'uk',
        'venezuela', 'vietnam', 'crypto'
    ]    

    ticker = st.text_input("Inserisci il ticker con prefisso (es. NASDAQ:AAPL):", "NASDAQ:AAPL")

    if st.button("Esegui Test"):
        try:
            query = Query().set_markets(*markets).set_tickers(ticker).select(
                'name', 'description', 'country', 'sector', 'close',
                'market_cap_basic', 'total_revenue_qoq_growth_fy', 'gross_profit_qoq_growth_fq',
                'net_income_qoq_growth_fq', 'earnings_per_share_diluted_qoq_growth_fq',
                'price_earnings_ttm', 'price_free_cash_flow_ttm', 'total_assets',
                'total_debt', 'shrhldr_s_equity_fq', 'operating_margin',
                'net_margin_ttm', 'free_cash_flow_qoq_growth_fq'
            )
            total_count, df = query.get_scanner_data()
            
            st.write(f"Totale risultati: {total_count}")
            if df.empty:
                st.warning("❌ Nessun dato trovato per questo ticker")
            else:
                st.dataframe(df.head())

        except Exception as e:
            st.error(f"Errore durante il test: {e}")

if __name__ == "__main__":
    test_fundamental_data()
