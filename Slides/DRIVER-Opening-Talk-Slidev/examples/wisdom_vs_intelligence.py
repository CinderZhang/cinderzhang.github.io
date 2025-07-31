"""
AI Intelligence vs Human Wisdom in Finance
A live coding example for the DRIVER opening talk
"""

import numpy as np
import pandas as pd

# AI's Intelligence: Perfect Optimization
def ai_portfolio_optimization(returns, risk_tolerance=0.1):
    """AI optimizes for maximum Sharpe ratio"""
    mean_returns = returns.mean()
    cov_matrix = returns.cov()
    
    # Simplified optimization (in reality, much more complex)
    weights = np.array([0.6, 0.3, 0.1])  # "Optimal" weights
    portfolio_return = np.sum(weights * mean_returns) * 252
    portfolio_risk = np.sqrt(np.dot(weights.T, np.dot(cov_matrix * 252, weights)))
    sharpe_ratio = portfolio_return / portfolio_risk
    
    return {
        "weights": weights,
        "return": f"{portfolio_return:.2%}",
        "risk": f"{portfolio_risk:.2%}",
        "sharpe": f"{sharpe_ratio:.2f}"
    }

# Human Wisdom: Understanding Context
def human_wisdom_portfolio(client_profile, market_conditions):
    """Human wisdom considers what AI cannot"""
    
    if client_profile["age"] > 65 and market_conditions["volatility"] == "high":
        decision = {
            "action": "Preserve capital, reduce risk",
            "reasoning": "Client needs stability more than returns",
            "weights": [0.7, 0.2, 0.1],  # More conservative
            "human_insight": "Fear matters more than math at this life stage"
        }
    
    elif client_profile["first_time_investor"] and client_profile["savings"] < 10000:
        decision = {
            "action": "Start simple, build confidence",
            "reasoning": "Education more important than optimization",
            "weights": [0.5, 0.5, 0.0],  # Balanced and simple
            "human_insight": "Trust is built through understanding, not returns"
        }
    
    else:
        decision = {
            "action": "Follow AI recommendation with adjustments",
            "reasoning": "Client can handle volatility for growth",
            "weights": [0.6, 0.3, 0.1],
            "human_insight": "Sometimes the 'optimal' solution is actually optimal"
        }
    
    return decision

# Example usage
if __name__ == "__main__":
    # Simulated return data
    returns = pd.DataFrame({
        'Stock': [0.001, 0.002, -0.001, 0.0015],
        'Bonds': [0.0005, 0.0004, 0.0006, 0.0005],
        'Gold': [0.0, 0.001, -0.0005, 0.0008]
    })
    
    print("=" * 50)
    print("AI INTELLIGENCE: Perfect Optimization")
    print("=" * 50)
    ai_result = ai_portfolio_optimization(returns)
    for key, value in ai_result.items():
        print(f"{key}: {value}")
    
    print("\n" + "=" * 50)
    print("HUMAN WISDOM: Understanding Context")
    print("=" * 50)
    
    # Scenario 1: Retired couple
    client1 = {"age": 68, "first_time_investor": False, "savings": 500000}
    market1 = {"volatility": "high"}
    wisdom1 = human_wisdom_portfolio(client1, market1)
    print(f"\nScenario: 68-year-old in volatile market")
    print(f"Decision: {wisdom1['action']}")
    print(f"Wisdom: {wisdom1['human_insight']}")
    
    # Scenario 2: Young professional
    client2 = {"age": 25, "first_time_investor": True, "savings": 5000}
    market2 = {"volatility": "normal"}
    wisdom2 = human_wisdom_portfolio(client2, market2)
    print(f"\nScenario: 25-year-old first-time investor")
    print(f"Decision: {wisdom2['action']}")
    print(f"Wisdom: {wisdom2['human_insight']}")
    
    print("\n" + "=" * 50)
    print("THE LESSON:")
    print("AI gives you the HOW. Wisdom tells you the WHY and WHEN.")
    print("Your value = AI's intelligence + Your wisdom")
    print("=" * 50)