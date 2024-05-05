import pandas as pd

# input_path = "dob_nyc_200.csv"
input_path = "DOB_Job_Application_Filings_20240424.csv"
output_path = "dob_nyc_project.csv"

col = ["Job Type", "BUILDING_CLASS", "Pre- Filing Date", "Paid", "Fully Paid", "Assigned", "Approved", "Fully Permitted", "SIGNOFF_DATE", "Borough", "GIS_LATITUDE","GIS_LONGITUDE"]

df = pd.read_csv(input_path, usecols=col)
df.to_csv(output_path, index=False)

