# 📈 AI Stock Predictor Dashboard

A full-stack AI-powered stock market prediction and analysis platform that uses LSTM neural networks and sentiment analysis to forecast stock prices and provide investment insights.

> ⚠️ **Disclaimer**: This tool is for educational and informational purposes only. Not financial advice. Never invest based solely on AI predictions.

## 🚀 Features

- **Stock Price Prediction** – LSTM model predicts next 7/30 day price movements
- **Sentiment Analysis** – Analyzes news and social media sentiment for stocks
- **Technical Indicators** – RSI, MACD, Bollinger Bands, Moving Averages
- **Portfolio Tracker** – Track your portfolio with real-time P&L
- **AI Market Summary** – Daily AI-generated market briefing
- **Backtesting Engine** – Test strategies on historical data
- **Watchlist Alerts** – Price alerts with AI-triggered notifications
- **Risk Assessment** – AI evaluates risk level for each stock

## 🏗️ Tech Stack

### Frontend
- **Next.js 14** + TypeScript
- **TradingView Lightweight Charts** for candlestick charts
- **Tailwind CSS** + Tremor UI
- **SWR** for real-time data fetching

### Backend
- **FastAPI** + Python 3.11
- **TensorFlow/Keras** – LSTM model for time series prediction
- **yfinance** – Yahoo Finance data
- **Pandas** + NumPy for data processing
- **OpenAI** – Market narrative generation
- **PostgreSQL** + TimescaleDB (time-series optimized)

### ML Pipeline
- **Data Collection** – yfinance + Alpha Vantage API
- **Feature Engineering** – 25+ technical indicators
- **Model** – Bidirectional LSTM with attention mechanism
- **Training** – AWS SageMaker (or local GPU)

## 📁 Project Structure

```
ai-stock-predictor/
├── frontend/              # Next.js 14 dashboard
├── backend/
│   ├── app/
│   │   ├── routes/        # API endpoints
│   │   ├── models/        # LSTM model definitions
│   │   ├── services/      # Business logic
│   │   └── ml/            # ML training scripts
│   └── requirements.txt
└── docker-compose.yml
```

## 🌐 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/stocks/{ticker}` | Get stock data + prediction |
| GET | `/api/stocks/{ticker}/predict` | 30-day price prediction |
| GET | `/api/stocks/{ticker}/sentiment` | Sentiment analysis |
| POST | `/api/portfolio` | Create/update portfolio |
| GET | `/api/market/summary` | AI market summary |
| POST | `/api/backtest` | Run strategy backtest |

## 📄 License

MIT


<!-- 2026-07-31T11:32:00 -->

<!-- 2026-10-24T17:12:00 -->

<!-- 2026-05-23T14:39:00 -->

<!-- 2026-07-17T22:01:00 -->

<!-- 2026-08-17T12:29:00 -->

<!-- 2026-06-21T22:07:00 -->

<!-- 2026-11-12T16:26:00 -->

<!-- 2026-07-06T11:56:00 -->

<!-- 2026-10-25T11:04:00 -->

<!-- 2026-07-02T10:26:00 -->

<!-- 2026-11-09T17:33:00 -->

<!-- 2026-08-21T12:53:00 -->

<!-- 2026-07-19T15:50:00 -->

<!-- 2026-06-04T11:48:00 -->

<!-- 2026-07-26T18:06:00 -->

<!-- 2026-08-31T09:04:00 -->

<!-- 2026-10-20T18:17:00 -->

<!-- 2026-09-27T21:04:00 -->

<!-- 2026-06-17T11:10:00 -->

<!-- 2026-05-28T16:02:00 -->

<!-- 2026-08-01T21:37:00 -->

<!-- 2026-11-16T14:53:00 -->

<!-- 2026-08-20T19:16:00 -->

<!-- 2026-08-08T19:40:00 -->
