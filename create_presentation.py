from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN

# Create presentation
prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(7.5)

# Slide 1: Title Slide
slide1 = prs.slides.add_slide(prs.slide_layouts[0])
title = slide1.shapes.title
subtitle = slide1.placeholders[1]

title.text = "Healthcare Provider Fraud Detection System"
subtitle.text = "(Medicare Fraud Detection Capstone)\n\nTeam: Mohamed Osama • Malak Khaled • Bahy Hany • Mohamed Wael"

# Slide 2: The Problem & Objective
slide2 = prs.slides.add_slide(prs.slide_layouts[1])
title2 = slide2.shapes.title
content2 = slide2.placeholders[1]

title2.text = "Slide 1 — The Problem & Our Objective\nBy Mohamed"
tf2 = content2.text_frame
tf2.text = "US healthcare fraud exceeds $68B/year"
p = tf2.add_paragraph()
p.text = "Legacy auditing misses hidden fraud patterns"
p = tf2.add_paragraph()
p.text = "Fraudulent providers ≈ 9% → ML bias"
p = tf2.add_paragraph()
p.text = ""
p = tf2.add_paragraph()
p.text = "Goal"
p.level = 0
p = tf2.add_paragraph()
p.text = "Detect high-risk providers (not individual claims)"
p.level = 1
p = tf2.add_paragraph()
p.text = "Handle severe class imbalance"
p.level = 1
p = tf2.add_paragraph()
p.text = "Reduce false investigations & financial loss"
p.level = 1

# Slide 3: Data Architecture
slide3 = prs.slides.add_slide(prs.slide_layouts[1])
title3 = slide3.shapes.title
content3 = slide3.placeholders[1]

title3.text = "Slide 2 — Data Architecture Overview (Phase 1)\nBy Malak"
tf3 = content3.text_frame
tf3.text = "Inputs"
p = tf3.add_paragraph()
p.text = "Beneficiary"
p.level = 1
p = tf3.add_paragraph()
p.text = "Inpatient"
p.level = 1
p = tf3.add_paragraph()
p.text = "Outpatient"
p.level = 1
p = tf3.add_paragraph()
p.text = "Provider labels"
p.level = 1
p = tf3.add_paragraph()
p.text = ""
p = tf3.add_paragraph()
p.text = "Join Level"
p.level = 0
p = tf3.add_paragraph()
p.text = "BeneID → Patient Events"
p.level = 1
p = tf3.add_paragraph()
p.text = "Provider → Target Entity (Fraud label)"
p.level = 1
p = tf3.add_paragraph()
p.text = ""
p = tf3.add_paragraph()
p.text = "Challenge"
p.level = 0
p = tf3.add_paragraph()
p.text = "Claims are transactional"
p.level = 1
p = tf3.add_paragraph()
p.text = "Fraud is behavioral at provider level"
p.level = 1
p = tf3.add_paragraph()
p.text = ""
p = tf3.add_paragraph()
p.text = "➡️ Build provider-level profiles"

# Slide 4: Data Cleaning
slide4 = prs.slides.add_slide(prs.slide_layouts[1])
title4 = slide4.shapes.title
content4 = slide4.placeholders[1]

title4.text = "Slide 3 — Data Cleaning Strategy\nBy Malak"
tf4 = content4.text_frame
tf4.text = "Problems Detected"
p = tf4.add_paragraph()
p.text = "Missing physician codes"
p.level = 1
p = tf4.add_paragraph()
p.text = "Nonsensical claim durations"
p.level = 1
p = tf4.add_paragraph()
p.text = "Zero-information columns"
p.level = 1
p = tf4.add_paragraph()
p.text = ""
p = tf4.add_paragraph()
p.text = "Actions"
p.level = 0
p = tf4.add_paragraph()
p.text = "Encode missing physicians as \"Unknown\""
p.level = 1
p = tf4.add_paragraph()
p.text = "Drop invalid-duration claims"
p.level = 1
p = tf4.add_paragraph()
p.text = "Remove redundant fields"
p.level = 1
p = tf4.add_paragraph()
p.text = ""
p = tf4.add_paragraph()
p.text = "Outcome"
p.level = 0
p = tf4.add_paragraph()
p.text = "Fraud distribution confirmed at ~9–10%"
p.level = 1

# Slide 5: Feature Engineering
slide5 = prs.slides.add_slide(prs.slide_layouts[1])
title5 = slide5.shapes.title
content5 = slide5.placeholders[1]

title5.text = "Slide 4 — Feature Engineering\nBy Mohamed"
tf5 = content5.text_frame
tf5.text = "We convert millions of claims → provider behavioral vectors"
p = tf5.add_paragraph()
p.text = ""
p = tf5.add_paragraph()
p.text = "Feature Groups"
p.level = 0
p = tf5.add_paragraph()
p.text = "Financial: reimbursements, avg deductible, mean claim cost"
p.level = 1
p = tf5.add_paragraph()
p.text = "Operational: volume, inpatient/outpatient balance"
p.level = 1
p = tf5.add_paragraph()
p.text = "Service Diversity: unique diagnoses & procedures"
p.level = 1
p = tf5.add_paragraph()
p.text = "Patient mix: chronic ratios, unique patient count"
p.level = 1
p = tf5.add_paragraph()
p.text = ""
p = tf5.add_paragraph()
p.text = "Final Dataset: 5410 providers × ~134 features"

# Slide 6: Exploratory Insights
slide6 = prs.slides.add_slide(prs.slide_layouts[1])
title6 = slide6.shapes.title
content6 = slide6.placeholders[1]

title6.text = "Slide 5 — Exploratory Insights\nBy Mohamed"
tf6 = content6.text_frame
tf6.text = "Detected patterns:"
p = tf6.add_paragraph()
p.text = "Fraud providers show higher revenue throughput"
p.level = 1
p = tf6.add_paragraph()
p.text = "Greater diagnosis/procedure diversity"
p.level = 1
p = tf6.add_paragraph()
p.text = "Geographic hotspots (certain states)"
p.level = 1
p = tf6.add_paragraph()
p.text = "Sustained high billing across time → not random"
p.level = 1

# Slide 7: Handling Imbalance
slide7 = prs.slides.add_slide(prs.slide_layouts[1])
title7 = slide7.shapes.title
content7 = slide7.placeholders[1]

title7.text = "Slide 6 — Handling Imbalance (Phase 2)\nBy Bahy"
tf7 = content7.text_frame
tf7.text = "Issue: Fraud = minority → models default to \"No Fraud\""
p = tf7.add_paragraph()
p.text = ""
p = tf7.add_paragraph()
p.text = "Methods tested:"
p.level = 0
p = tf7.add_paragraph()
p.text = "Class Weighting"
p.level = 1
p = tf7.add_paragraph()
p.text = "SMOTE"
p.level = 1
p = tf7.add_paragraph()
p.text = "SMOTE + Tomek Links"
p.level = 1
p = tf7.add_paragraph()
p.text = ""
p = tf7.add_paragraph()
p.text = "Purpose:"
p.level = 0
p = tf7.add_paragraph()
p.text = "Improve detection power"
p.level = 1
p = tf7.add_paragraph()
p.text = "Preserve real distributions after oversampling"
p.level = 1

# Slide 8: Modeling Strategy
slide8 = prs.slides.add_slide(prs.slide_layouts[1])
title8 = slide8.shapes.title
content8 = slide8.placeholders[1]

title8.text = "Slide 7 — Modeling Strategy (Phase 3)\nBy Bahy"
tf8 = content8.text_frame
tf8.text = "Models:"
p = tf8.add_paragraph()
p.text = "Logistic Regression → interpretable baseline"
p.level = 1
p = tf8.add_paragraph()
p.text = "Decision Tree → simple benchmark"
p.level = 1
p = tf8.add_paragraph()
p.text = "Random Forest → robust ensemble"
p.level = 1
p = tf8.add_paragraph()
p.text = "XGBoost → non-linear excellence + imbalance tolerance"
p.level = 1
p = tf8.add_paragraph()
p.text = ""
p = tf8.add_paragraph()
p.text = "Tuning"
p.level = 0
p = tf8.add_paragraph()
p.text = "GridSearchCV (5-fold)"
p.level = 1
p = tf8.add_paragraph()
p.text = "Optimized for F1 score"
p.level = 1

# Slide 9: Model Selection Results
slide9 = prs.slides.add_slide(prs.slide_layouts[1])
title9 = slide9.shapes.title
content9 = slide9.placeholders[1]

title9.text = "Slide 8 — Model Selection Results\nBy Mohamed"
tf9 = content9.text_frame
tf9.text = "Model\tPrecision\tRecall\tF1\tROC-AUC\tPR-AUC"
p = tf9.add_paragraph()
p.text = "Logistic Regression\t0.43\t0.80\t0.56\t0.9284\t0.6300"
p = tf9.add_paragraph()
p.text = "Random Forest\t0.48\t0.77\t0.59\t0.9281\t0.5906"
p = tf9.add_paragraph()
p.text = "Decision Tree\t0.43\t0.68\t0.53\t0.7413\t0.3694"
p = tf9.add_paragraph()
p.text = "XGBoost\t0.59\t0.68\t0.63\t0.9311\t0.6534"
p = tf9.add_paragraph()
p.text = ""
p = tf9.add_paragraph()
p.text = "XGBoost = best balance: recall + precision + ROC-AUC"

# Slide 10: Final Test Evaluation
slide10 = prs.slides.add_slide(prs.slide_layouts[1])
title10 = slide10.shapes.title
content10 = slide10.placeholders[1]

title10.text = "Slide 9 — Final Test Evaluation (Phase 4)\nBy Aly"
tf10 = content10.text_frame
tf10.text = "Test Results (20% unseen)"
p = tf10.add_paragraph()
p.text = "Accuracy: 93.63%"
p.level = 1
p = tf10.add_paragraph()
p.text = "Precision: 63.79%"
p.level = 1
p = tf10.add_paragraph()
p.text = "Recall: 73.27%"
p.level = 1
p = tf10.add_paragraph()
p.text = "F1: 68.20%"
p.level = 1
p = tf10.add_paragraph()
p.text = "ROC-AUC: 96.79%"
p.level = 1
p = tf10.add_paragraph()
p.text = "PR-AUC: 79.89%"
p.level = 1
p = tf10.add_paragraph()
p.text = ""
p = tf10.add_paragraph()
p.text = "Confusion Matrix"
p.level = 0
p = tf10.add_paragraph()
p.text = "TP: 74 — caught fraud"
p.level = 1
p = tf10.add_paragraph()
p.text = "FN: 27 — missed fraud"
p.level = 1
p = tf10.add_paragraph()
p.text = "FP: 42 — unnecessary audits"
p.level = 1
p = tf10.add_paragraph()
p.text = "TN: 940 — legitimate providers"
p.level = 1
p = tf10.add_paragraph()
p.text = ""
p = tf10.add_paragraph()
p.text = "➡️ High recall + very high ROC-AUC = excellent fraud ranking"

# Slide 11: Business Impact
slide11 = prs.slides.add_slide(prs.slide_layouts[1])
title11 = slide11.shapes.title
content11 = slide11.placeholders[1]

title11.text = "Slide 10 — Business Impact\nBy Mohamed"
tf11 = content11.text_frame
tf11.text = "Assumptions:"
p = tf11.add_paragraph()
p.text = "False Positive → ~$1,000 audit cost"
p.level = 1
p = tf11.add_paragraph()
p.text = "False Negative → ~$50,000 undetected fraud"
p.level = 1
p = tf11.add_paragraph()
p.text = ""
p = tf11.add_paragraph()
p.text = "Model advantages:"
p.level = 0
p = tf11.add_paragraph()
p.text = "Prevents silent financial leakage"
p.level = 1
p = tf11.add_paragraph()
p.text = "Strong ROC-AUC → optimal investigation prioritization"
p.level = 1
p = tf11.add_paragraph()
p.text = "Saves operational effort vs random review"
p.level = 1

# Slide 12: Error Analysis
slide12 = prs.slides.add_slide(prs.slide_layouts[1])
title12 = slide12.shapes.title
content12 = slide12.placeholders[1]

title12.text = "Slide 11 — Error Analysis\nBy Bahy"
tf12 = content12.text_frame
tf12.text = "False Positives"
p = tf12.add_paragraph()
p.text = "Legit high-throughput providers"
p.level = 1
p = tf12.add_paragraph()
p.text = "Resemble \"high-revenue fraud\""
p.level = 1
p = tf12.add_paragraph()
p.text = ""
p = tf12.add_paragraph()
p.text = "False Negatives"
p.level = 0
p = tf12.add_paragraph()
p.text = "Very low-volume clinics"
p.level = 1
p = tf12.add_paragraph()
p.text = "Mimic normal small providers"
p.level = 1
p = tf12.add_paragraph()
p.text = ""
p = tf12.add_paragraph()
p.text = "Future Enhancements"
p.level = 0
p = tf12.add_paragraph()
p.text = "Provider–patient graph relationships"
p.level = 1
p = tf12.add_paragraph()
p.text = "Temporal fraud drift tracking"
p.level = 1

# Slide 13: Key Drivers
slide13 = prs.slides.add_slide(prs.slide_layouts[1])
title13 = slide13.shapes.title
content13 = slide13.placeholders[1]

title13.text = "Slide 12 — Key Drivers of Risk\nBy Malak"
tf13 = content13.text_frame
tf13.text = "Top influential signals:"
p = tf13.add_paragraph()
p.text = "Total claims submitted"
p.level = 1
p = tf13.add_paragraph()
p.text = "Total & avg reimbursement"
p.level = 1
p = tf13.add_paragraph()
p.text = "Diagnosis & procedure diversity"
p.level = 1
p = tf13.add_paragraph()
p.text = "Chronic illness ratios"
p.level = 1
p = tf13.add_paragraph()
p.text = ""
p = tf13.add_paragraph()
p.text = "➡️ Features align with known real-world fraud behaviors"

# Slide 14: Recommendations
slide14 = prs.slides.add_slide(prs.slide_layouts[1])
title14 = slide14.shapes.title
content14 = slide14.placeholders[1]

title14.text = "Slide 13 — Final Recommendations\nBy Mohamed"
tf14 = content14.text_frame
tf14.text = "Deploy XGBoost for Medicare fraud triage"
p = tf14.add_paragraph()
p.text = "Investigate top risk percentile providers"
p = tf14.add_paragraph()
p.text = "Keep human analysts in loop"
p = tf14.add_paragraph()
p.text = "Retrain every quarter → prevent drift"

# Slide 15: Q&A
slide15 = prs.slides.add_slide(prs.slide_layouts[0])
title15 = slide15.shapes.title
title15.text = "Slide 14 — Q&A\n\nQuestions?"

# Save presentation
prs.save('reports/presentation.pptx')
print("PowerPoint presentation created successfully at reports/presentation.pptx")
