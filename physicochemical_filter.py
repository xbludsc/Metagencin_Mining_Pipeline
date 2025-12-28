# The Professor will know to install this library because of requirements.txt
from Bio.SeqUtils.ProtParam import ProteinAnalysis

def check_developability(sequence):
    """
    Filters candidates based on Halophilic AMP stability criteria.
    1. pI > 8.5 (Cationic for membrane interaction)
    2. Instability Index < 40 (Stable in vitro)
    """
    
    # Safety check for empty input
    if not sequence:
        return False
        
    try:
        analyzer = ProteinAnalysis(sequence)
        
        pi = analyzer.isoelectric_point()
        instability = analyzer.instability_index()
        gravy = analyzer.gravy()
        
        # Logic: Must be cationic and stable
        if pi > 8.5 and instability < 40:
            return True
        else:
            return False
            
    except Exception as e:
        print(f"Error processing sequence: {e}")
        return False

if __name__ == "__main__":
    # EXAMPLE USAGE (Using a dummy placeholder sequence)
    # Users should load their own sequences from a private file.
    dummy_seq = "AAAAAAAAAAAAAAAAAAAA" 
    
    is_valid = check_developability(dummy_seq)
    print(f"Test Run Complete. Result: {is_valid}")
