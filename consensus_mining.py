import pandas as pd

def apply_consensus_rules(macrel_result, camp_svm, camp_rf, camp_da):
    """
    Applies the consensus logic used in the study.
    
    Criteria for Acceptance:
    1. Must be predicted as AMP by Macrel (Random Forest).
    2. Must be validated by at least one model from CAMP-R3 (SVM, RF, or DA).
    """
    
    # 1. Check Macrel (Primary Screen)
    if macrel_result != "AMP":
        return "Rejected"

    # 2. Check CAMP-R3 Validation (Secondary Screen)
    # Passing any one of the three models is considered validation
    camp_consensus = any([
        camp_svm > 0.5,  # SVM Probability > 0.5
        camp_rf > 0.5,   # Random Forest Probability > 0.5
        camp_da > 0.5    # Discriminant Analysis Probability > 0.5
    ])

    if camp_consensus:
        return "Accepted (Consensus)"
    else:
        return "Rejected (No Consensus)"

# Example Data (From Metagencin-2 Results)
# Macrel: AMP, CAMP-RF: 0.583 (Pass), SVM/DA: Fail
result = apply_consensus_rules("AMP", 0.35, 0.583, 0.18)
print(f"Metagencin-2 Verdict: {result}")