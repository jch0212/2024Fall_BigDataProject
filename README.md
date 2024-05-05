# 2024Fall_BigDataProject

## The project contains three parts that were completed separately by different teammates.

## Part 1 by Jiahui Zhu
## Urban Zoning Visualization and Project Life Cycle Analysis

### Step 1:

- **Purpose**: To trim the datasource so that it can fit into the course's shared Jupyter Notebook environment (limited memory) in Step 2.
- **Environment**: NYU Dataproc
- **Input file**: [DOB_Job_Application_Filings_20240424.csv](https://drive.google.com/file/d/10iKs7pfTqVXpMk9xTDbXLeADR9kJSIF6/view?usp=drive_link)
- **Output file**: [dob_nyc_project.csv](https://drive.google.com/file/d/1VsRhWrJeVmfhZQ_-AwLq4URs8bRgCisO/view?usp=drive_link)
- **Script file**: [part1_jz5584/pre_process.py](https://github.com/jch0212/2024Fall_BigDataProject/blob/main/part1_jz5584/pre_process.py)
- **Steps**:
  1. Do not modify the input file name.
  2. Put the input file and script file under the same directory.
  3. Run `python pre_process.py`.
  4. Output file will be generated under the same directory.

### Step 2:

- **Purpose**: To perform analysis on the datasource.
- **Environment**: Course shared Jupyter Notebook - [Link](https://csgy-6513-spring.rcnyu.org/user/jz5584/tree/jz5584_project)
- **Input files**:
  - [nybb.csv](https://drive.google.com/file/d/1VsRhWrJeVmfhZQ_-AwLq4URs8bRgCisO/view?usp=drive_link)
  - [dob_nyc_project.csv](https://drive.google.com/drive/folders/1skDuhQt2xQXZehsV7X0nEeWBx2AoVBAS?usp=sharing/output/dob_nyc_project.csv)
- **Output files**:
  - [average_timeline_by_borough.csv](https://drive.google.com/file/d/1hsyFO_iinYafyHNP_OSyguimVoXeTr-4/view?usp=drive_link)
  - [average_timeline_by_borough.png](https://drive.google.com/file/d/1fxD2DlLMvqHcZ61_bNYJ9fYog1Xhe8-n/view?usp=drive_link)
  - [average_timeline_by_building.csv](https://drive.google.com/file/d/1jFdwe_2iWfUNwRyQ-0qHxNnoBVFD8DFD/view?usp=drive_link)
  - [average_timeline_by_building_class.csv](https://drive.google.com/file/d/1MzQ0_eyLIH63VtUT3jXOusGyDUofaLqr/view?usp=drive_link)
  - [average_timeline_by_building_classification.png](https://drive.google.com/file/d/1MzQ0_eyLIH63VtUT3jXOusGyDUofaLqr/view?usp=drive_link)
  - [average_timeline_by_building_type.csv](https://drive.google.com/file/d/1dJVBRxbpaqQtpzmFv8MW0xb-tvGaQxfg/view?usp=drive_link)
  - [average_timeline_by_building_type.png](https://drive.google.com/file/d/12Ve8_qAdKYB-F16fgL-gHHcCOgYRE6Jq/view?usp=drive_link)
  - [average_timeline_by_job_type.csv](https://drive.google.com/file/d/1wseqkzQOEunkl6Mi8t9CPtr75YemEW3K/view?usp=drive_link)
  - [average_timeline_by_job_type.png](https://drive.google.com/file/d/1dzNZp1hDePme5WXRP8t6GY1tPxE_FgIz/view?usp=drive_link)
  - [building_classification_in_nyc.png](https://drive.google.com/file/d/1OuQ-gPHpcZKEKn3ROx0dsY-UzR3X-xqk/view?usp=drive_link)
  - [building_types_in_nyc.png](https://drive.google.com/file/d/1VOdux-ypDK1OJnFUwv5zDagUm-hMMxQV/view?usp=drive_link)
  - [construction_job_types_in_nyc.png](https://drive.google.com/file/d/1TObFhSVmJxguXS0S_oi4oEGlCuPJT_n6/view?usp=drive_link)
  - [jz5584_project_final.pdf](https://drive.google.com/file/d/1yu5ikvI1pOaMFCrLVDWcNvgXx-mXPgOL/view?usp=drive_link) (Jupyter Notebook script with output)
- **Script file**: [part1_jz5584/jz5584_project_final.ipynb](https://github.com/jch0212/2024Fall_BigDataProject/blob/main/part1_jz5584/jz5584_project.ipynb)
- **Steps**:
  1. Do not modify the input file name.
  2. Put the input file and script file under the same Jupyter Notebook directory.
  3. Run the script file. Output file will be generated under the same directory.

## Part 2 by Ruining Li
## Construction Cost Analysis
### Step 1:

- **Purpose**: Load and analyze the dataset
- **Environment**: Python 3.11 with Spark
- **Input file**: [DOB_Job_Application_Filings_20240424.csv](https://drive.google.com/file/d/10iKs7pfTqVXpMk9xTDbXLeADR9kJSIF6/view?usp=drive_link)
- **Output file**: DOB_Job_Application_Filings_20240424.csv
- **Script file**: construction_cost_analysis.ipynb
- **Steps**:
  1. put the ipynb file with the dataset in one folder
  2. run the first 16 cells of the file(there might be some issue happen when running the application fee column because the dataset is so large, but restarting and running it again will fix it)
  3. the plot will be shown under each cell
 
### Step 2:

- **Purpose**: Build the predict model
- **Environment**: Python 3.11 with Spark
- **Input file**: [DOB_Job_Application_Filings_20240424.csv](https://drive.google.com/file/d/10iKs7pfTqVXpMk9xTDbXLeADR9kJSIF6/view?usp=drive_link)
- **Output file**: DOB_Job_Application_Filings_20240424.csv
- **Script file**: construction_cost_analysis.ipynb
- **Steps**:
  1. put the ipynb file with the dataset in one folder
  2. restart the notebook and run all the cells in the file
  3. in the final cell, the model will be built, trained and evaluated, the root mean square error will be cacluated

## Part 3 by Chenhao Jiang
## Application Approval Analysis

### Step 1:

- **Purpose**: Prepare the data.
- **Environment**: Python 3.8 with panda
- **Input file**: [DOB_Job_Application_Filings_20240424.csv](https://drive.google.com/file/d/10iKs7pfTqVXpMk9xTDbXLeADR9kJSIF6/view?usp=drive_link)
- **Output file**: processedData_.csv
- **Script file**: dataProcess.py
- **Steps**:
  1. Do not modify the input file name.
  2. Put the input file and script file under the same directory.
  3. Run `python dataProcess.py`.
  4. Output file will be generated under the same directory.
 
  ### Step 2:

- **Purpose**: Prepare the data.Calculate the SHAP value of choosed columns in dataset to figure out the correlation between columns and approval decisions.
- **Environment**: Python 3.8 with sklearn and shap
- **Input file**: Output from Step1
- **Output file**: shap_value_positive_.csv
- **Script file**: jobParam.py AdminManagement.py Owner.py
- **Steps**:
  1. Do not modify the input file name.
  2. Put the input file and script file under the same directory.
  3. Output file will be generated under the same directory.

  ### Step 3:

- **Purpose**: Visualize the results.
- **Environment**: Python 3.8 with matplotlib and panda
- **Input file**: Output from Step2
- **Output file**: result.png
- **Script file**: dataVisualization.py
- **Steps**:
  1. Do not modify the input file name.
  2. Put the input file and script file under the same directory.
  3. Output file will be generated under the same directory.
 

### Step 4:

- **Purpose**: Train the predictive model.
- **Environment**: Python 3.8 with sklearn
- **Input file**: [DOB_Job_Application_Filings_20240424.csv](https://drive.google.com/file/d/10iKs7pfTqVXpMk9xTDbXLeADR9kJSIF6/view?usp=drive_link)
- **Output file**: result.png
- **Script file**: recommendationSystem.py
- **Steps**:
  1. Do not modify the input file name.
  2. Put the input file and script file under the same directory.
  3. Output file will be generated under the same directory.
 










