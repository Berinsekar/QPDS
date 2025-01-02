import pandas as pd
from scipy.stats import spearmanr


study_hours = [2, 4, 6, 8, 10]
exam_scores = [50, 55, 65, 75, 85]


data = pd.DataFrame({
    'Study Hours': study_hours,
    'Exam Scores': exam_scores
})


spearman_corr, _ = spearmanr(data['Study Hours'], data['Exam Scores'])

print(f"Spearman Rank Correlation: {spearman_corr}")
