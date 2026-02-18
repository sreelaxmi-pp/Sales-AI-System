def generate_strategy(hiring_signal, pricing_changes):

    strategy = []

    # Hiring signal logic
    if hiring_signal > 5:
        strategy.append("Competitor expanding sales team. Expect aggressive acquisition.")

    # Pricing signal logic
    if pricing_changes:
        strategy.append("Competitor changed pricing. Review positioning.")

    if not strategy:
        strategy.append("No major competitive signals detected. Maintain current sales approach.")

    print("\n--- Strategy Output ---")
    for s in strategy:
        print("-", s)

    return strategy
