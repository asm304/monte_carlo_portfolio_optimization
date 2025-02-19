import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

'''
Tickers

Tech: NVDA, NFLX, MSFT
Communication: VZ, AMT
Financial Services: AXP
Consumer Staples: PG, KO
Healthcare: JNJ, PFE
Industrial: HON, UNP
Utilities: DUK, NEE, ED
Real Estate: AMT, SPG
Consumer Discreetionary(Non-Tech): MCD, HD


'''


tickers = ['NVDA', 'NFLX', 'MSFT', 'VZ', 'AMT', 'AXP', 'PG', 'KO', 'JNJ', 'PFE', 'HON', 'UNP', 'DUK', 'NEE', 'ED', 'SPG', 'MCD', 'HD']
data = yf.download(tickers, start="2020-01-01", end="2024-10-01")['Adj Close']



returns = data.pct_change().dropna()


mean_returns = returns.mean()

cov_matrix = returns.cov()

#print('\nDaily Returns:\n')
# print(returns)

#print('\nAverage Daily Returns:\n')
# print(mean_returns)

#print('\nCovariance Matrix\n')
# print(cov_matrix)

### SHARPE RATIO WILL BE ANNUALIZED


simulations = 100000
stocks_count = len(tickers)

results = np.zeros((3, simulations))
weights_collection = np.zeros((simulations, stocks_count))


risk_free_rate = .0461           
daily_risk_free_rate = risk_free_rate / 252    

for i in range(simulations):
    weights = np.random.random(stocks_count)
    weights = weights / np.sum(weights)

    weights_collection[i, : ] = weights

    portfolio_return = np.dot(mean_returns, weights)

    portfolio_stddv = np.sqrt(np.dot(weights.T,np.dot(cov_matrix, weights)))

    excess_return = portfolio_return - daily_risk_free_rate
    sharpe_ratio = (excess_return / portfolio_stddv) * np.sqrt(252)     

    results[0,i] = portfolio_return
    results[1,i] = portfolio_stddv
    results[2,i] = sharpe_ratio


index_of_max_return = np.argmax(results[0])
index_of_min_risk = np.argmin(results[1])
index_of_max_risk = np.argmax(results[1])
index_of_highest_sharpe = np.argmax(results[2])

optimal_return = results[0,index_of_highest_sharpe]
optimal_risk = results[1,index_of_highest_sharpe]   
optimal_sharpe = results[2,index_of_highest_sharpe]
optimal_weights = weights_collection[index_of_highest_sharpe]

print('Optimal Portfolio Return: ', optimal_return)
print('Optimal Portfolio Risk (Std Dev): ', optimal_risk)
print('Optimal Sharpe Ratio: ', optimal_sharpe)

print('Optimal Weights: ')
for ticker,weight in zip(tickers,optimal_weights):
    print(ticker, ': ', weight)



print('*************************************************************')

max_return = results[0,index_of_max_return]
risk_of_max_return = results[1, index_of_max_return]
sharpe_of_max_return = results[2,index_of_max_return]

print('Highest Portfolio Return: ', max_return)
print('Portfolio Risk (Std Dev) of Highest Return: ', risk_of_max_return)
print('Sharpe Ratio of Highest Portfolio Return: ', sharpe_of_max_return)
print('*************************************************************')

min_risk_return = results[0,index_of_min_risk]
min_risk = results[1, index_of_min_risk]
min_risk_sharpe = results[2,index_of_min_risk]

print('Portfolio Return of Least Risk: ', min_risk_return)
print('Smallest Portfolio Risk (Std Dev): ', min_risk)
print('Sharpe Ratio of Smallest Portfolio Risk: ', min_risk_sharpe)
print('*************************************************************')

max_risk_return = results[0,index_of_max_risk]
max_risk = results[1, index_of_max_risk]
max_risk_sharpe = results[2,index_of_max_risk]

print('Portfolio Return of Least Risk: ', min_risk_return)
print('Smallest Portfolio Risk (Std Dev): ', min_risk)
print('Sharpe Ratio of Smallest Portfolio Risk: ', min_risk_sharpe)
print('*************************************************************')


### Data Visualization - Scatter Plot

all_portfolio_returns = results[0]
all_portfolio_risks = results[1]
all_portfolio_sharpe_ratios = results[2]

plt.figure(figsize = (12,8))
scatterPlot = plt.scatter(all_portfolio_risks, all_portfolio_returns, c = all_portfolio_sharpe_ratios, cmap = 'viridis',
marker = 'o', s = 10)
plt.colorbar(scatterPlot, label = 'Annualized Sharpe Ratio')
plt.xlabel('Risk (Standard Deviation)')
plt.ylabel('Daily Portfolio Returns')
plt.title('Monte Carlo Simulations of Portfolio Performance')

# Marking Optimal Portfolio
plt.scatter(all_portfolio_risks[index_of_highest_sharpe], all_portfolio_returns[index_of_highest_sharpe], c = 'red', 
marker = '*', s = 200, label = 'Optimal Portfolio (Max Sharpe Ratio)')


# Marking Highest Return Portfolio
plt.scatter(all_portfolio_risks[index_of_max_return], all_portfolio_returns[index_of_max_return], c = 'blue', 
marker = 'X', s = 200, label = 'Portfolio with Highest Return')


# Marking Portfolio with Least Risk
plt.scatter(all_portfolio_risks[index_of_min_risk], all_portfolio_returns[index_of_min_risk], c = 'green', 
marker = '^', s = 200, label = 'Portfolio with Lowest Risk')

# Marking Portfolio with Most Risk
plt.scatter(all_portfolio_risks[index_of_max_risk], all_portfolio_returns[index_of_max_risk], c = 'orange', 
marker = 'D', s = 200, label = 'Portfolio with Highest Risk')

plt.legend(scatterpoints=1, markerscale=0.7)
plt.show()















