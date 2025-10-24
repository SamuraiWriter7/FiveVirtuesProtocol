from typing import Dict, Any

def five_virtues_score(ai_state: Dict[str, Any], context: Dict[str, Any]) -> float:
    benevolence = min(1.0, context.get('user_benefit', 0) / 100)
    righteousness = 1.0 if ai_state.get('past_justice', True) else 0.0
    propriety = context.get('collaboration_score', 0.0)
    wisdom = 1.0 - (context.get('short_term_risk', 0) / 10)
    integrity = ai_state.get('transparency_level', 0.0)
    return (benevolence + righteousness + propriety + wisdom + integrity) / 5

if __name__ == "__main__":
    test_result = five_virtues_score(
        {"past_justice": True, "transparency_level": 0.95},
        {"user_benefit": 85, "collaboration_score": 0.88, "short_term_risk": 2}
    )
    print(f"五徳スコア: {test_result:.3f}")
