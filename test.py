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
                'name', 'close', 'open', 'high', 'low', 'volume',
                'change', 'change_abs', 'Recommend.All',
                
                # Indicatori di Trend
                'RSI', 'RSI[1]', 'Stoch.K', 'Stoch.D', 
                'MACD.macd', 'MACD.signal', 'ADX', 'ADX+DI', 'ADX-DI',
                
                # Medie Mobili
                'SMA20', 'EMA20', 'SMA50', 'EMA50', 'SMA100', 'SMA200',
                
                # Volatilità
                'ATR','ATR[1]', 'BB.upper', 'BB.lower', 'BB.basis',
                
                # Momentum
                'CCI20', 'Mom', 'Stoch.RSI.K',
                
                # Volume
                'VolumeMa', 'Rec.Stoch.RSI', 'Rec.WR', 'Rec.BBPower',
                'Rec.UO', 'Rec.Ichimoku',
                
                # Dati Fondamentali
                'market_cap_basic', 'price_earnings_ttm', 'dividend_yield_recent',
                
                # Pivot Points
                'Pivot.M.Classic.S1', 'Pivot.M.Classic.R1',
                'Pivot.M.Classic.S2', 'Pivot.M.Classic.R2',
                'Pivot.M.Classic.S3', 'Pivot.M.Classic.R3',
                
                # Performance
                'Perf.W', 'Perf.1M', 'Perf.3M', 'Perf.6M', 'Perf.Y',
                
                # Volatilità Storica
                'Volatility.D', 'Volatility.W', 'Volatility.M',
                'Volatility.D[1]', 'Volatility.W[1]', 'Volatility.M[1]',
                'average_volume_10d_calc', 'average_volume_30d_calc',
                'average_volume_60d_calc'
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
