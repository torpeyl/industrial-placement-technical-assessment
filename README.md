# Industrial Placement Technical Assessment: Calculating Fund Performance

Welcome to the technical assessment for the 2024 Industrial Placements at Behaviour Lab. This assessment is designed to evaluate your ability to handle and analyze financial data using Python.

## Overview

In this assessment, you will be working with data stored in an excel spreadsheet containing two sheets: `RAW_CLIENT_DATA` and `THIRD_PARTY_MARKET_DATA`. The `RAW_CLIENT_DATA` sheet contains time series of portfolio weights for various assets, while the `THIRD_PARTY_MARKET_DATA` sheet includes FactSet data, specifically prices and metadata for these assets. Your task is to calculate the overall fund performance of the portfolio using the provided data.

## Requirements

To successfully complete this assessment, you'll need to follow these general steps:

- *Calculate Returns*: Calculate the daily returns from prices for each asset in the portfolio.
- *Merge Dataframes*: Merge the `RAW_CLIENT_DATA` and `THIRD_PARTY_MARKET_DATA` dataframes on the date and security ID.
- *Calculate Daily Contribution*: Calculate the daily contribution of each asset to the overall fund performance.
- *Sum Daily Contributions*: Sum the daily contributions for each day to obtain the total fund performance.
- *Compound Returns*: Compound the daily returns to obtain cumulative returns for each day.
- *Rebase to 100*: Rebase the cumulative returns to start from 100.
- *Visualize the output*: Plot the cumulative fund performance over time.

These requirements cover the base requirements for completing the exercise but they are by no means complete. Please investigate the data carefully and ask questions as we progress through the excercise. State clearly any assumptions that you make.
