# Responsible AI Auditor for ML Models

## Why this matters
AI systems can unintentionally produce biased outcomes. This tool evaluates machine learning models for fairness, bias, and explainability.

## Features
- Bias detection across sensitive attributes  
- Fairness metrics (demographic parity, equal opportunity)  
- Model explainability (SHAP, LIME)  
- Simple reporting output  

## Tech Stack
- Python
- pandas
- scikit-learn
- SHAP / LIME

## Run
Install dependencies:
pip install -r requirements.txt

Run:
python src/main.py

## Example Output
Bias evaluation completed successfully.

## Real-world relevance
Based on Responsible AI principles used in industry environments.

## Future Improvements
- Add dashboard (Streamlit)
- Add PDF reports
- Extend to NLP models
