def apply_consensus_rules(macrel_result, camp_svm_prob, camp_rf_prob, camp_da_prob):
    """
    Applies the consensus logic used in the study.
    
    Criteria for Acceptance:
    1. Must be predicted as AMP by Macrel (Random Forest).
    2. Must be validated by at least one model from CAMP-R3 (SVM, RF, or DA) with Prob > 0.5.
    """
    
    # 1. Primary Screen: Macrel
    if macrel_result != "AMP":
        return "Rejected"

    # 2. Secondary Screen: CAMP-R3 Validation
    # We accept the candidate if ANY of the three models validate it.
    camp_consensus = any([
        camp_svm_prob > 0.5,
        camp_rf_prob > 0.5,
        camp_da_prob > 0.5
    ])

    if camp_consensus:
        return "Accepted (Consensus)"
    else:
        return "Rejected (No Consensus)"

if __name__ == "__main__":
    # Test with hypothetical values (NO REAL DATA HERE)
    test_result = apply_consensus_rules("AMP", 0.45, 0.65, 0.20)
    print(f"Hypothetical Test Verdict: {test_result}")