# Quantitative Analysis of Stock Price Data

A comprehensive financial analysis project that performs quantitative analysis on stock price data from major technology companies using Python, pandas, and various technical indicators.

## 📊 Project Overview

This project analyzes historical stock price data for major technology stocks (AAPL, AMZN, GOOG, META, NVDA) from 2009-2023, implementing various quantitative analysis techniques including:

- **Data preprocessing and cleaning**
- **Descriptive statistics and volatility analysis**
- **Technical indicators calculation** (RSI, MACD, Bollinger Bands, etc.)
- **Correlation analysis** between stocks
- **Time series analysis** and trend identification
- **Risk metrics and performance evaluation**

## 📁 Project Structure

```
Testing with sami/
├── Data/                    # Stock price datasets
│   └── yfinance_data/       # Raw CSV files for each stock
├── notebooks/               # Jupyter analysis notebooks
│   ├── Quantitative analysis .ipynb
│   ├── Descriptive_Statistics.ipynb
│   ├── Publisher_Analysis.ipynb
│   ├── Text_Analysis.ipynb
│   └── Time_Series_Analysis.ipynb
├── src/                    # Source code modules
├── scripts/                # Utility scripts
├── tests/                  # Test files
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Jupyter Notebook or JupyterLab
- Git (for version control)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Testing with sami"
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

### Dependencies

The project uses the following key libraries:

- **pandas** (2.2.3) - Data manipulation and analysis
- **numpy** (2.2.3) - Numerical computing
- **matplotlib** (3.9.2) - Data visualization
- **seaborn** (0.13.2) - Statistical data visualization
- **scipy** (1.14.1) - Scientific computing
- **streamlit** (1.41.1) - Web app framework
- **pandas-ta** - Technical analysis indicators
- **pytest** (8.2.0) - Testing framework
- **flake8** (7.0.0) - Code linting

## 📈 Data

### Stock Data Coverage

The analysis covers 5 major technology stocks:

| Symbol | Company | Date Range | Records |
|--------|---------|------------|---------|
| AAPL   | Apple Inc. | 2009-01-02 to 2023-12-29 | 3,774 |
| AMZN   | Amazon.com Inc. | 2009-01-02 to 2023-12-29 | 3,774 |
| GOOG   | Alphabet Inc. | 2009-01-02 to 2023-12-29 | 3,774 |
| META   | Meta Platforms Inc. | 2012-05-18 to 2023-12-29 | 2,923 |
| NVDA   | NVIDIA Corporation | 2009-01-02 to 2023-12-29 | 3,774 |

### Data Features

Each stock dataset includes:
- **Date**: Trading date
- **Open/High/Low/Close**: Daily price data
- **Volume**: Trading volume
- **Technical Indicators**: Calculated metrics (RSI, MACD, Bollinger Bands, etc.)

## 🔬 Analysis Features

### Technical Indicators Implemented

1. **Moving Averages**
   - Simple Moving Averages (SMA): 10, 20, 50, 100, 200 periods
   - Exponential Moving Averages (EMA): 10, 20, 50, 100, 200 periods

2. **Momentum Indicators**
   - Relative Strength Index (RSI) - 14 period
   - Stochastic Oscillator
   - Williams %R

3. **Trend Indicators**
   - MACD (Moving Average Convergence Divergence)
   - Bollinger Bands
   - Fibonacci Retracements

4. **Volatility Indicators**
   - Average True Range (ATR)
   - Historical volatility calculations

### Analysis Types

- **Descriptive Statistics**: Mean, median, standard deviation, percentiles
- **Correlation Analysis**: Cross-stock correlation matrices
- **Volatility Analysis**: Rolling volatility, risk metrics
- **Returns Analysis**: Daily returns, cumulative returns, risk-adjusted performance
- **Time Series Analysis**: Trend detection, seasonality, decomposition

## 📓 Notebooks

### Main Analysis Notebook
`Quantitative analysis .ipynb` - Comprehensive analysis covering:
- Data loading and preprocessing
- Technical indicator calculations
- Advanced financial metrics
- Visualization and interpretation

### Specialized Notebooks
- `Descriptive_Statistics.ipynb` - Statistical analysis and summaries
- `Publisher_Analysis.ipynb` - Publisher-specific analysis
- `Text_Analysis.ipynb` - Text-based analysis of financial data
- `Time_Series_Analysis.ipynb` - Advanced time series modeling

## 🛠️ Usage

### Running the Analysis

1. **Start Jupyter Notebook**
   ```bash
   jupyter notebook
   ```

2. **Open the main analysis notebook**
   - Navigate to `notebooks/Quantitative analysis .ipynb`
   - Run cells sequentially to perform the complete analysis

3. **Customize Analysis**
   - Modify stock symbols in the data loading section
   - Adjust technical indicator parameters
   - Change visualization settings

### Key Functions

```python
# Calculate moving averages
def calculate_moving_averages(df, windows=[10, 20, 50, 100, 200]):
    # Implementation...

# Calculate RSI
def calculate_rsi(df, window=14):
    # Implementation...

# Calculate MACD
def calculate_macd(df, fast=12, slow=26, signal=9):
    # Implementation...
```

## 📊 Sample Results

### Technical Indicators Summary (Latest Values)

| Stock | Price | SMA 20/50 | RSI | MACD | Williams %R | Signal |
|-------|-------|-----------|-----|------|-------------|--------|
| AAPL  | $190.73 | $192.49/$184.81 | 40.19 | Bearish | -83.12 | Oversold |
| AMZN  | $151.94 | $149.82/$143.05 | 62.42 | Bearish | -30.78 | Neutral |
| GOOG  | $139.97 | $135.98/$134.06 | 63.74 | Bullish | -23.40 | Neutral |
| META  | $351.79 | $336.87/$326.26 | 70.56 | Bullish | -18.95 | Overbought |
| NVDA  | $49.50 | $48.05/$46.66 | 62.56 | Bullish | -19.79 | Overbought |

## 🧪 Testing

Run the test suite:

```bash
pytest tests/
```

Run code linting:

```bash
flake8 src/ notebooks/
```

## 📝 Development

### Code Style

- Follow PEP 8 style guidelines
- Use descriptive variable names
- Add docstrings to functions
- Include type hints where appropriate

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## 🚨 Important Notes

- **Data Quality**: All datasets have been cleaned for missing values
- **Date Consistency**: All stocks aligned to common trading dates where possible
- **Indicator Calculations**: Technical indicators calculated using standard financial formulas
- **Accuracy**: Double-checked calculations against financial libraries

## 📚 References

- [pandas-ta Documentation](https://pandas-ta.readthedocs.io/)
- [Technical Analysis Concepts](https://www.investopedia.com/terms/t/technicalanalysis.asp)
- [Financial Data Analysis Best Practices](https://www.oreilly.com/library/view/python-for-finance/9781491945360/)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Acknowledgments

- yfinance for providing historical stock data
- pandas-ta library for technical analysis functions
- Financial data analysis community for best practices

---

**Last Updated**: December 2023  
**Version**: 1.0.0  
**Maintainer**: Financial Analysis Team
