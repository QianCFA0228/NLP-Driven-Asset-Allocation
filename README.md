
# NLP-Driven Asset Allocation using FinBERT

## Project Overview
In institutional portfolio management, traditional Mean-Variance optimization and tools heavily rely on historical structural data (e.g., rigid correlation matrices and historical expected returns). However, macro-political shifts, executive speeches, and sudden policy changes introduce systemic risks that historical data fails to capture promptly.

This project bridges the gap between **unstructured qualitative data** and **quantitative asset allocation**. It acts as an AI overlay for institutional portfolios.

## Methodology
This Python framework leverages Natural Language Processing (NLP) to dynamically adjust portfolio weights:
1. **Data Ingestion:** Captures macroeconomic news headlines and executive speeches.
2. **Sentiment Scoring:** Utilizes Financial-specific LLMs (simulated FinBERT) to extract directional sentiment and confidence scores.
3. **Black-Litterman View Generation:** Translates the NLP sentiment score into a quantitative "View" (the $Q$ vector in the Black-Litterman model). 
4. **Dynamic Rebalancing:** Penalizes the expected returns of negatively impacted asset classes before feeding the data into the optimizer, forcing an automatic tilt towards defensive assets (e.g., US Treasuries) prior to a market drawdown.

## Why This Matters
As an Investment Analyst handling large-scale capital allocation, I realize that AI is not meant to replace foundational financial theories, but to enhance them. By quantifying news sentiment, we can update our Efficient Frontier in real-time, effectively managing tail risks that traditional models might overlook.

## Future Development
- Integrate live API feeds from Bloomberg/Reuters.
- Implement full covariance matrix scaling using GARCH models combined with NLP volatility indicators.
