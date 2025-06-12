import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# input path
df_path = os.path.join('jira_report_generator', 'input_file/Jira_Export_Excel.csv')

# Load data
df = pd.read_csv(df_path)


columns_for_report = [
    "Summary",
    "Issue key",
    "Issue id",
    "Issue Type",
    "Status",
    "Project key"
]

def create_new_jira_report(df: pd.DataFrame, columns_to_check: list) -> pd.DataFrame:
    cols = [col for col in columns_to_check if col in df.columns]
    if not cols:
        raise ValueError("None of the specified columns are found in the dataframe")
    return df[cols]

df_new_report = create_new_jira_report(df=df, columns_to_check=columns_for_report)

# output folder
os.makedirs(os.path.join('jira_report_generator', 'output'), exist_ok=True)

# Save CSV
output_file = os.path.join('jira_report_generator', 'output', 'Jira_Export_SelectedColumns.csv')
df_new_report.to_csv(output_file, index=False)
logging.info(f"New report generated: {output_file}")
