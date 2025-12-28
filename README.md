# Metagencin Mining Pipeline

## Overview
This repository hosts the computational logic used for the discovery and validation of **Metagencin-1, -2, and -3**, novel antimicrobial peptides derived from halophilic metagenomes.

## Workflow

### 1. Consensus Mining Strategy
To mitigate false positives from single-algorithm predictions, we implemented a multi-stage consensus filter:
* **Primary Screen:** Macrel (Random Forest for Metagenomic Mining).
* **Secondary Validation:** CAMP-R3 Suite (SVM, Random Forest, Discriminant Analysis).
* **Selection Rule:** A candidate is accepted only if identified as an AMP by Macrel **AND** validated by at least one classifier in CAMP-R3 (Probability > 0.5).

### 2. Physicochemical Filtering
Selected candidates were filtered for developability using `Bio.SeqUtils.ProtParam`:
* **Isoelectric Point (pI):** > 8.5 (Ensures cationic charge for membrane attraction).
* **Instability Index:** < 40 (Ensures in vitro stability).

### 3. Structural Validation & Docking
* **Modeling:** AlphaFold2 (Primary) validated by I-TASSER (Consensus C-score).
* **Docking:** HADDOCK 2.4 (Ensemble docking).
    * **Metagencin-1** vs. FhuA/LPS (Outer Membrane)
    * **Metagencin-2** vs. MurD (Peptidoglycan Synthesis)
    * **Metagencin-3** vs. DNA Gyrase B (Replication)

## Dependencies
* Python 3.8+
* Biopython (`Bio.SeqUtils`)
* Pandas

## Contact
**Shubham Pandey**
PhD Scholar, Department of Microbiology
University of Delhi South Campus
