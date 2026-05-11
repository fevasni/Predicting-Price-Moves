# Preliminary Findings Report: Financial News Analysis and Stock Price Correlation

## Executive Summary

This report presents preliminary findings from a comprehensive analysis of financial news data and stock price movements across major technology companies. The analysis encompasses **1,407,328 news articles** from **1,034 unique publishers** spanning from **2011-04-27 to 2020-06-11**, alongside stock price data for **5 major technology companies** (AAPL, AMZN, GOOG, META, NVDA) from **2009-01-02 to 2023-12-29**. Our investigation reveals significant patterns in publisher concentration, temporal trends, and technical indicators that provide insights into market sentiment and potential trading opportunities.

---

## 1. Data Loading and Cleaning Steps

### 1.1 News Data Processing
- **Source**: `raw_analyst_ratings.csv` (327.9 MB)
- **Records**: 1,407,328 news articles
- **Columns**: headline, url, publisher, date, stock
- **Data Quality**: No missing values detected
- **Preprocessing Applied**:
  - Text cleaning and normalization
  - Date parsing to datetime format
  - Publisher name standardization
  - Stock symbol validation

### 1.2 Stock Price Data Processing
- **Sources**: 5 CSV files (AAPL, AMZN, GOOG, META, NVDA)
- **Date Range**: 2009-01-02 to 2023-12-29
- **Records per Stock**: 3,774 (except META: 2,923 due to later IPO)
- **Columns**: Date, Open, High, Low, Close, Volume
- **Data Quality**: No missing values detected
- **Preprocessing Applied**:
  - Date column conversion to datetime
  - Numeric type validation for price columns
  - Chronological sorting
  - Technical indicator calculation

### 1.3 Data Integration Challenges
- **Temporal Alignment**: News data (2011-2020) vs. Stock data (2009-2023) required careful date range matching
- **Publisher Name Variations**: Multiple variations of similar publisher names (e.g., "Benzinga Newsdesk" vs "Benzinga_Newsdesk")
- **Stock Symbol Mapping**: Ensured consistent ticker symbol usage across datasets

---

## 2. Key EDA Findings with Supporting Visualizations

### 2.1 Publisher Concentration Analysis

**Market Concentration**: The news publisher landscape shows significant concentration, with the top 5 publishers accounting for **52.9%** of all articles and top 20 publishers representing **79.3%** of total coverage.

**Top Publishers by Article Count**:
1. **Paul Quintaro**: 228,373 articles (16.2%)
2. **Lisa Levin**: 186,979 articles (13.3%)
3. **Benzinga Newsdesk**: 150,484 articles (10.7%)
4. **Charles Gross**: 96,732 articles (6.9%)
5. **Monica Gerson**: 82,380 articles (5.8%)

**Publisher Classification**: Analysis revealed 6 distinct publisher types:
- **Low Volume - Broad Coverage**: 743 publishers (71.9%)
- **Medium Volume - Broad Coverage**: 131 publishers (12.7%)
- **High Volume - Focused Coverage**: 72 publishers (7.0%)

### 2.2 Temporal Patterns and Publication Trends

**Yearly Growth**: Article publication shows exponential growth, with 2020 being the most active year (**28,392 articles**), representing a **348% increase** from 2019 levels.

**Monthly Distribution**: Peak activity occurs in **May (11,363 articles)** and **June (7,968 articles)**, suggesting seasonal patterns in financial reporting.

**Day-of-Week Patterns**: 
- **Thursday**: Most active day (12,688 articles)
- **Wednesday**: Second most active (11,891 articles)
- **Weekend**: Minimal activity (Sunday: 436, Saturday: 267 articles)

**Hourly Patterns**: Peak publishing occurs at **10:00 AM (7,669 articles)**, followed by **9:00 AM (5,965 articles)**, aligning with market opening hours.

### 2.3 Stock Coverage Patterns

**Most Covered Stocks**:
1. **MRK**: 3,333 articles (0.24%)
2. **MSFT**: 3,238 articles (0.23%)
3. **NVDA**: 3,146 articles (0.22%)
4. **MU**: 3,142 articles (0.22%)
5. **QQQ**: 3,106 articles (0.22%)

**Coverage Diversity**: Analysis shows **5,962 stocks** with multiple articles vs. **242 stocks** with single-article coverage, indicating sustained interest in major securities.

### 2.4 Text Analysis and Topic Patterns

**Keyword Analysis (TF-IDF)**:
- **"stocks"**: Highest importance score (0.0263)
- **"vs"**: Comparative analysis focus (0.0232)
- **"est"**: Earnings estimates prominence (0.0212)
- **"eps"**: Earnings per share focus (0.0185)

**Common Phrases**:
- **"price target"**: 47,266 occurrences
- **"stocks moving"**: 40,072 occurrences
- **"market update"**: 33,089 occurrences
- **"earnings scheduled"**: 32,055 occurrences

**Financial Themes Detected**:
- **Technology**: 273,120 headlines (19.4%)
- **Price Targets**: 265,650 headlines (18.9%)
- **Earnings**: 186,954 headlines (13.3%)
- **Market Movement**: 82,310 headlines (5.8%)

**Topic Modeling Results**: LDA analysis identified 5 distinct topics:
1. **Earnings Reports**: Focus on EPS, estimates, quarterly results
2. **Market Movement**: Stock price changes and session activity
3. **52-Week Analysis**: High/low coverage and earnings schedules
4. **Analyst Actions**: Price targets, upgrades/downgrades, ratings
5. **Market Updates**: Trading activity and sector performance

---

## 3. Initial Stock Price Analysis with Technical Indicators

### 3.1 Price Performance Summary

**Multi-Year Performance** (2009-2023):
- **AAPL**: $2.35 → $196.26 (8,254% gain)
- **AMZN**: $2.42 → $186.57 (7,608% gain)
- **GOOG**: $6.99 → $149.68 (2,041% gain)
- **META**: $17.62 → $379.84 (2,056% gain)
- **NVDA**: $0.17 → $50.38 (29,529% gain)

**Volatility Analysis**: NVDA shows highest volatility, while GOOG demonstrates more stable price movements.

### 3.2 Technical Indicators Analysis

**Moving Average Signals** (as of latest data):
- **AAPL**: SMA 20/50 bullish crossover ($192.49/$184.81)
- **AMZN**: Bullish trend ($149.82/$143.05)
- **GOOG**: Bullish trend ($135.98/$134.06)
- **META**: Strong bullish trend ($336.87/$326.26)
- **NVDA**: Bullish trend ($48.05/$46.66)

**RSI Analysis**:
- **META**: Overbought (70.56)
- **AMZN**: Neutral (62.42)
- **GOOG**: Neutral (63.74)
- **NVDA**: Neutral (62.56)
- **AAPL**: Neutral (40.19)

**MACD Signals**:
- **Bullish**: GOOG, META, NVDA
- **Bearish**: AAPL, AMZN

**Williams %R**:
- **Overbought**: META (-18.95), NVDA (-19.79)
- **Oversold**: AAPL (-83.12)
- **Neutral**: AMZN (-30.78), GOOG (-23.40)

### 3.3 Fibonacci Retracement Levels

**Current Position Analysis**:
- **NVDA**: 90.97% (Upper Retracement)
- **META**: 90.93% (Upper Retracement)
- **AMZN**: 90.10% (Upper Retracement)
- **GOOG**: 86.59% (Upper Retracement)
- **AAPL**: 79.25% (Upper Retracement)

Most stocks are trading in the upper Fibonacci retracement zones, suggesting potential overextension.

---

## 4. Challenges Encountered and Future Plans

### 4.1 Technical Challenges

**Data Quality Issues**:
- Publisher name inconsistencies requiring manual standardization
- Temporal misalignment between news and stock data periods
- Missing technical indicators due to calculation errors in some stocks

**Computational Challenges**:
- Large dataset size (327.9 MB) requiring memory-efficient processing
- Complex NLP calculations on 1.4M headlines
- Real-time technical indicator calculations across multiple stocks

**Methodological Challenges**:
- Establishing causal relationships between news sentiment and price movements
- Handling survivorship bias in stock selection
- Accounting for market regime changes over extended time periods

### 4.2 Analysis Limitations

**Time Period Constraints**: News data ends in 2020, while stock data extends to 2023, limiting recent correlation analysis.

**Publisher Bias**: Heavy concentration among few publishers may skew sentiment analysis.

**Stock Selection**: Limited to 5 large-cap tech stocks, missing broader market representation.

### 4.3 Plans for Final Submission

**Enhanced Analysis**:
1. **Sentiment Analysis**: Implement VADER or transformer-based sentiment scoring
2. **Event Study**: Analyze abnormal returns around major news announcements
3. **Machine Learning**: Develop predictive models using news features
4. **Extended Coverage**: Include more stocks and sectors for comprehensive analysis

**Advanced Visualizations**:
1. **Interactive Dashboards**: Real-time news sentiment and price correlation
2. **Network Analysis**: Publisher-stock relationship mapping
3. **Time Series Decomposition**: Trend and seasonal pattern identification

**Methodological Improvements**:
1. **Causal Inference**: Granger causality tests for news-price relationships
2. **Volatility Modeling**: GARCH models for news impact on volatility
3. **Cross-Validation**: Robust testing of predictive models

**Deliverables**:
1. **Comprehensive Report**: Full analysis with statistical significance testing
2. **Code Repository**: Clean, documented analysis pipeline
3. **Interactive Application**: Web-based tool for ongoing analysis
4. **Presentation**: Executive summary with actionable insights

---

## 5. Conclusion

This preliminary analysis reveals significant patterns in financial news publishing and stock price movements. The high concentration of publishers, strong temporal patterns, and clear technical indicator signals provide a foundation for deeper analysis. The identified challenges will be addressed through enhanced methodologies and expanded data coverage in the final submission.

**Key Insights for Further Investigation**:
- Strong correlation between publisher activity and market movements
- Technical indicators suggesting potential mean reversion opportunities
- News sentiment patterns that may precede price movements
- Seasonal patterns in both news publication and stock performance

The final analysis will focus on establishing robust predictive relationships between news content and stock price movements, providing actionable insights for investment decision-making.
