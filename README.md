# monte_carlo_portfolio_optimization                  Author: Aman Meda
Finding optimal stock portfolios using Monte Carlo Analysis in Python

This project uses **Monte Carlo simulations** to determine the optimal portfolio allocation by generating thousands of random weight distributions. The goal is to identify the best risk-return trade-off for a diversified portfolio of stocks.

## 📈 Overview

- Simulates **100,000** random portfolio weight combinations.
- Calculates **expected return, risk (standard deviation), and Sharpe ratio**.
- Identifies **the optimal portfolio** based on the highest Sharpe ratio.
- Uses **historical stock price data (2020-2024)** from Yahoo Finance.
- Visualizes portfolio performance through a **scatter plot of risk vs. return**.

---

## 🔧 Technologies Used

- **Python**
- `yfinance` – Fetches historical stock price data
- `numpy` – Mathematical operations and random weight generation
- `matplotlib` – Data visualization
- **Monte Carlo Method** – Simulating thousands of random portfolio allocations

---

## 📊 Dataset & Stocks Used

The portfolio consists of stocks from various sectors:

- **Technology:** NVDA, NFLX, MSFT  
- **Communication:** VZ, AMT  
- **Financial Services:** AXP  
- **Consumer Staples:** PG, KO  
- **Healthcare:** JNJ, PFE  
- **Industrial:** HON, UNP  
- **Utilities:** DUK, NEE, ED  
- **Real Estate:** AMT, SPG  
- **Consumer Discretionary:** MCD, HD  

Historical adjusted closing prices from **January 2020 to October 2024** were used.

---

## 🏆 Key Results

- **Optimal Portfolio Return:** *X.XX%*  
- **Optimal Portfolio Risk (Std Dev):** *X.XX%*  
- **Optimal Sharpe Ratio:** *X.XX*  
- **Optimal Weights for Each Stock:**
  
  | Stock | Weight |
  |-------|--------|
  | NVDA  | XX%    |
  | MSFT  | XX%    |
  | …     | …      |

*(Full breakdown is available in the code output.)*

---

## 📌 How It Works

1. **Download Stock Data**: Fetches historical prices for selected stocks.
2. **Calculate Returns & Covariance Matrix**: Computes daily returns and portfolio variance.
3. **Simulate Portfolios**: Generates **100,000 portfolios** with random weight distributions.
4. **Compute Performance Metrics**:
   - Expected portfolio return
   - Portfolio risk (standard deviation)
   - Sharpe ratio (risk-adjusted return)
5. **Identify Optimal Portfolio**:
   - Maximum Sharpe ratio (best risk-adjusted return)
   - Lowest risk portfolio (minimum volatility)
   - Highest return portfolio
6. **Visualize Efficient Frontier**:
   - Scatter plot of portfolio risk vs. return.
   - Highlights the **optimal portfolio**, **max return**, **min risk**, and **highest risk**.

---

## 📉 Visualization

The scatter plot below shows **100,000 simulated portfolios** with different allocations. The **color represents the Sharpe ratio** (higher = better).  
Key points marked:
- **⭐ Optimal Portfolio (Max Sharpe)**
- **🔵 Highest Return Portfolio**
- **🟢 Lowest Risk Portfolio**
- **🟠 Most Risky Portfolio**

![Efficient Frontier]

<img width="1195" alt="PNG image" src="https://github.com/user-attachments/assets/30902360-ad55-4096-9675-a088de001848" />





