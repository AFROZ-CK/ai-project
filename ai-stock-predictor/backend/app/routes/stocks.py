from fastapi import APIRouter, HTTPException, Query
from app.models.lstm_model import StockPredictionModel
from app.services.sentiment_service import SentimentService
from app.services.market_summary import MarketSummaryService
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

router = APIRouter()
sentiment_service = SentimentService()
market_service = MarketSummaryService()

# Cache models in memory
_model_cache: dict[str, StockPredictionModel] = {}


@router.get("/{ticker}")
async def get_stock_data(
    ticker: str,
    period: str = Query("1y", regex="^(1mo|3mo|6mo|1y|2y|5y)$")
):
    """Get stock data with technical indicators and AI prediction."""
    ticker = ticker.upper()
    
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        
        if not info.get("currentPrice"):
            raise HTTPException(status_code=404, detail=f"Ticker {ticker} not found")
        
        hist = stock.history(period=period)
        
        return {
            "ticker": ticker,
            "name": info.get("longName", ticker),
            "sector": info.get("sector", "Unknown"),
            "current_price": info.get("currentPrice"),
            "market_cap": info.get("marketCap"),
            "pe_ratio": info.get("forwardPE"),
            "52w_high": info.get("fiftyTwoWeekHigh"),
            "52w_low": info.get("fiftyTwoWeekLow"),
            "volume": info.get("volume"),
            "avg_volume": info.get("averageVolume"),
            "history": [
                {
                    "date": date.strftime("%Y-%m-%d"),
                    "open": row["Open"],
                    "high": row["High"],
                    "low": row["Low"],
                    "close": row["Close"],
                    "volume": row["Volume"]
                }
                for date, row in hist.iterrows()
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{ticker}/predict")
async def predict_stock(
    ticker: str,
    days: int = Query(7, ge=1, le=30)
):
    """Get AI price predictions for a stock."""
    ticker = ticker.upper()
    
    # Use cached model or create new one
    if ticker not in _model_cache:
        model = StockPredictionModel(ticker)
        try:
            model._load_saved_model()
            _model_cache[ticker] = model
        except FileNotFoundError:
            # Train a quick model if not available
            raise HTTPException(
                status_code=503,
                detail=f"Model for {ticker} not yet trained. Please request training first."
            )
    
    model = _model_cache[ticker]
    predictions = model.predict(days_ahead=days)
    
    # Add sentiment context
    sentiment = await sentiment_service.get_stock_sentiment(ticker)
    
    return {
        "ticker": ticker,
        "predictions": predictions,
        "sentiment": sentiment,
        "disclaimer": "AI predictions are for educational purposes only. Not financial advice.",
        "model_info": {
            "type": "Bidirectional LSTM",
            "lookback_days": 60,
            "features": 24
        }
    }


@router.get("/{ticker}/sentiment")
async def get_sentiment(ticker: str):
    """Get news and social media sentiment analysis."""
    sentiment = await sentiment_service.get_stock_sentiment(ticker.upper())
    return sentiment


@router.get("/market/summary")
async def get_market_summary():
    """Get AI-generated daily market summary."""
    summary = await market_service.generate_daily_summary()
    return summary


# Updated: 2026-07-28T13:08:00

# Updated: 2026-06-29T22:11:00

# Updated: 2026-07-27T10:37:00

# Updated: 2026-08-10T11:49:00

# Updated: 2026-06-30T14:48:00

# Updated: 2026-10-01T11:15:00

# Updated: 2026-09-23T18:35:00

# Updated: 2026-05-24T13:26:00

# Updated: 2026-09-21T11:16:00

# Updated: 2026-07-24T09:20:00

# Updated: 2026-07-19T14:07:00

# Updated: 2026-07-18T15:15:00

# Updated: 2026-05-24T09:16:00

# Updated: 2026-11-20T16:20:00
