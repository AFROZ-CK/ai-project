'use client';

import { useState, useEffect } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, AreaChart, Area } from 'recharts';
import { TrendingUp, TrendingDown, AlertCircle, RefreshCw } from 'lucide-react';

interface StockData {
  ticker: string;
  name: string;
  current_price: number;
  history: Array<{ date: string; close: number; volume: number }>;
}

interface Prediction {
  date: string;
  predicted_close: number;
  change_pct: number;
  confidence: number;
}

interface StockDashboardProps {
  ticker: string;
}

export function StockDashboard({ ticker }: StockDashboardProps) {
  const [stockData, setStockData] = useState<StockData | null>(null);
  const [predictions, setPredictions] = useState<Prediction[]>([]);
  const [period, setPeriod] = useState('6mo');
  const [predictDays, setPredictDays] = useState(7);
  const [isLoading, setIsLoading] = useState(false);
  const [sentiment, setSentiment] = useState<any>(null);

  useEffect(() => {
    if (ticker) {
      fetchStockData();
    }
  }, [ticker, period]);

  const fetchStockData = async () => {
    setIsLoading(true);
    try {
      const [stockRes, predRes] = await Promise.all([
        fetch(`/api/stocks/${ticker}?period=${period}`),
        fetch(`/api/stocks/${ticker}/predict?days=${predictDays}`)
      ]);
      
      const stock = await stockRes.json();
      const pred = await predRes.json();
      
      setStockData(stock);
      setPredictions(pred.predictions);
      setSentiment(pred.sentiment);
    } catch (error) {
      console.error('Failed to fetch stock data:', error);
    } finally {
      setIsLoading(false);
    }
  };

  if (!stockData) return <div className="animate-pulse h-96 bg-gray-200 rounded-xl" />;

  const chartData = [
    ...stockData.history.slice(-60).map(h => ({
      date: h.date,
      actual: h.close,
      type: 'historical'
    })),
    ...predictions.map(p => ({
      date: p.date,
      predicted: p.predicted_close,
      type: 'predicted',
      confidence: p.confidence
    }))
  ];

  const lastPrice = stockData.history[stockData.history.length - 1]?.close || 0;
  const firstPrediction = predictions[0];
  const priceChange = firstPrediction ? firstPrediction.change_pct : 0;
  const isPositive = priceChange >= 0;

  return (
    <div className="bg-white rounded-2xl shadow-sm border border-gray-100 p-6">
      {/* Header */}
      <div className="flex items-start justify-between mb-6">
        <div>
          <h2 className="text-2xl font-bold text-gray-900">{ticker}</h2>
          <p className="text-gray-500 text-sm">{stockData.name}</p>
        </div>
        <div className="text-right">
          <div className="text-3xl font-bold text-gray-900">
            ${lastPrice.toFixed(2)}
          </div>
          <div className={`flex items-center gap-1 justify-end text-sm font-medium ${
            isPositive ? 'text-green-600' : 'text-red-600'
          }`}>
            {isPositive ? <TrendingUp size={16} /> : <TrendingDown size={16} />}
            {isPositive ? '+' : ''}{priceChange.toFixed(2)}% (7-day forecast)
          </div>
        </div>
      </div>

      {/* Period Selector */}
      <div className="flex gap-2 mb-4">
        {['1mo', '3mo', '6mo', '1y'].map(p => (
          <button
            key={p}
            onClick={() => setPeriod(p)}
            className={`px-3 py-1 rounded-full text-xs font-medium transition-colors ${
              period === p
                ? 'bg-blue-600 text-white'
                : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
            }`}
          >
            {p}
          </button>
        ))}
      </div>

      {/* Chart */}
      <div className="h-64">
        <ResponsiveContainer width="100%" height="100%">
          <AreaChart data={chartData}>
            <defs>
              <linearGradient id="actualGradient" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.3} />
                <stop offset="95%" stopColor="#3b82f6" stopOpacity={0} />
              </linearGradient>
              <linearGradient id="predictedGradient" x1="0" y1="0" x2="0" y2="1">
                <stop offset="5%" stopColor="#8b5cf6" stopOpacity={0.3} />
                <stop offset="95%" stopColor="#8b5cf6" stopOpacity={0} />
              </linearGradient>
            </defs>
            <CartesianGrid strokeDasharray="3 3" stroke="#f0f0f0" />
            <XAxis dataKey="date" tick={{ fontSize: 10 }} tickLine={false} />
            <YAxis tick={{ fontSize: 10 }} tickLine={false} axisLine={false} />
            <Tooltip
              contentStyle={{ borderRadius: '8px', border: 'none', boxShadow: '0 4px 20px rgba(0,0,0,0.1)' }}
            />
            <Legend />
            <Area
              type="monotone"
              dataKey="actual"
              stroke="#3b82f6"
              fill="url(#actualGradient)"
              name="Actual Price"
              strokeWidth={2}
              dot={false}
            />
            <Area
              type="monotone"
              dataKey="predicted"
              stroke="#8b5cf6"
              fill="url(#predictedGradient)"
              name="AI Prediction"
              strokeWidth={2}
              strokeDasharray="5 5"
              dot={false}
            />
          </AreaChart>
        </ResponsiveContainer>
      </div>

      {/* Predictions Table */}
      <div className="mt-4">
        <h3 className="text-sm font-semibold text-gray-700 mb-2">📊 7-Day AI Forecast</h3>
        <div className="overflow-x-auto">
          <table className="w-full text-xs">
            <thead>
              <tr className="text-gray-400 border-b">
                <th className="text-left pb-2">Date</th>
                <th className="text-right pb-2">Price</th>
                <th className="text-right pb-2">Change</th>
                <th className="text-right pb-2">Confidence</th>
              </tr>
            </thead>
            <tbody>
              {predictions.map((p, i) => (
                <tr key={p.date} className="border-b border-gray-50">
                  <td className="py-2 text-gray-600">{p.date}</td>
                  <td className="py-2 text-right font-medium">${p.predicted_close}</td>
                  <td className={`py-2 text-right font-medium ${
                    p.change_pct >= 0 ? 'text-green-600' : 'text-red-600'
                  }`}>
                    {p.change_pct >= 0 ? '+' : ''}{p.change_pct}%
                  </td>
                  <td className="py-2 text-right text-gray-500">
                    {Math.round(p.confidence * 100)}%
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* Disclaimer */}
      <div className="mt-4 flex items-start gap-2 bg-yellow-50 rounded-lg p-3">
        <AlertCircle size={14} className="text-yellow-600 mt-0.5 flex-shrink-0" />
        <p className="text-xs text-yellow-700">
          AI predictions are for educational purposes only. Past performance does not guarantee future results. Not financial advice.
        </p>
      </div>
    </div>
  );
}


// Updated: 2026-07-24T18:30:00

// Updated: 2026-09-08T12:34:00

// Updated: 2026-07-31T14:01:00

// Updated: 2026-09-13T11:40:00

// Updated: 2026-11-20T22:33:00

// Updated: 2026-08-14T11:48:00

// Updated: 2026-09-28T16:14:00

// Updated: 2026-07-01T17:57:00

// Updated: 2026-10-08T20:08:00

// Updated: 2026-08-08T21:15:00

// Updated: 2026-05-30T19:47:00

// Updated: 2026-07-07T17:20:00

// Updated: 2026-08-09T21:06:00

// Updated: 2026-08-15T15:54:00
