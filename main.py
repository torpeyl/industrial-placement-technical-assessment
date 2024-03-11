# To successfully complete this assessment, you'll need to follow these general steps:

#     Calculate Returns: Calculate the daily returns from prices for each asset in the portfolio.
#     Merge Dataframes: Merge the RAW_CLIENT_DATA and THIRD_PARTY_MARKET_DATA dataframes on the date and security ID.
#     Calculate Daily Contribution: Calculate the daily contribution of each asset to the overall fund performance.
#     Sum Daily Contributions: Sum the daily contributions for each day to obtain the total fund performance.
#     Compound Returns: Compound the daily returns to obtain cumulative returns for each day.
#     Rebase to 100: Rebase the cumulative returns to start from 100.
#     Visualize the output: Plot the cumulative fund performance over time.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_excel('2024_01_25 Behaviour Lab Assessment Data.xlsx', sheet_name=[0, 1])

dataset[1]['returns'] = ((dataset[1]['price'].shift(1) - dataset[1]['price']) / dataset[1]['price']) * 100
merged_df = pd.merge(dataset[0], dataset[1], on=['date', 'security id']).fillna(0)
merged_df['changed-asset'] = merged_df["security name"].shift(1) != merged_df["security name"]
merged_df.loc[merged_df['changed-asset'] == True, 'returns'] = 0
# where name changes replace return with nan or 0

merged_df['daily-contribution'] = (merged_df['PortfolioWeight'] * merged_df['returns']).fillna(0)

merged_df = merged_df.merge(merged_df.groupby(['date'])['daily-contribution'].sum(), on='date')
merged_df = merged_df.rename(columns={'daily-contribution_x': 'daily-contribution'})
merged_df = merged_df.rename(columns={'daily-contribution_y': 'daily-contribution-sum'})
merged_df['returns-amount'] = merged_df['price'] * merged_df['returns']
merged_df['cum-returns'] = merged_df['returns-amount'].sum()

# print(merged_df.head(10))

plt.plot(merged_df['date'], merged_df['daily-contribution-sum'])
plt.show()

# Ran out of time for rebasing


