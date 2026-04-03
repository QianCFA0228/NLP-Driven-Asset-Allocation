import pandas as pd
import numpy as np

# Note: In a production environment, this would import from the HuggingFace transformers library:
# from transformers import pipeline
# nlp_model = pipeline("sentiment-analysis", model="ProsusAI/finbert")

def analyze_financial_sentiment(news_text):
    """
    Simulates the FinBERT NLP model output for demonstration purposes.
    Extracts sentiment from macroeconomic and political news.
    """
    print(f"[News Alert]: '{news_text}'")
    
    # Simulating NLP processing to detect trade/tariff risks
    if "tariff" in news_text.lower() or "strict" in news_text.lower():
        return {"label": "negative", "score": 0.88}
    return {"label": "neutral", "score": 0.50}

def adjust_expected_returns(base_returns, sentiment_result, target_indices, penalty_factor=0.03):
    """
    Translates NLP sentiment scores into quantitative adjustments for Expected Returns.
    This acts as the 'View' generation in a Black-Litterman framework.
    """
    adjusted_returns = base_returns.copy()
    
    if sentiment_result['label'] == 'negative':
        adjustment = penalty_factor * sentiment_result['score']
        for idx in target_indices:
            adjusted_returns[idx] -= adjustment
            print(f"[Action]: Sentiment is HIGHLY NEGATIVE. Downgrading asset index {idx} return by {adjustment:.4f}")
            
    return adjusted_returns

if __name__ == "__main__":
    print("--- Institutional Portfolio AI Overlay System ---\n")
    
    # 1. Define Asset Universe and Base Expected Returns (Historical)
    assets = ['US_Large_Cap', 'Emerging_Markets', 'Tech_Sector', 'US_Treasuries']
    base_returns = np.array([0.08, 0.11, 0.12, 0.04]) 
    
    # 2. Ingest Unstructured Data (e.g., Political Speech / News)
    breaking_news = "The administration is planning to impose strict tariffs on imported tech components and emerging market goods."
    sentiment = analyze_financial_sentiment(breaking_news)
    
    # 3. NLP-Driven Adjustment (Impacting Emerging Markets [1] and Tech [2])
    print("\n--- AI Sentiment Analysis & Portfolio Adjustment ---")
    adjusted_returns = adjust_expected_returns(base_returns, sentiment, target_indices=[1, 2])
    
    # 4. Output Results to Portfolio Optimizer
    df = pd.DataFrame({
        'Asset_Class': assets,
        'Historical_Expected_Return': base_returns,
        'AI_Adjusted_Expected_Return': adjusted_returns
    })
    
    print("\n[Final Output for Optimizer]")
    print(df.to_string(index=False))
    print("\n[Conclusion]: The Mean-Variance optimizer will now automatically tilt the $11B+ portfolio towards US Treasuries and defensive equities, mitigating the unquantified risk in the correlation matrix.")
