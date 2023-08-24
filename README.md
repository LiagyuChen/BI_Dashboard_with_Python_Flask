# BI_Dashboard_with_Python_Flask
Creating Business Intelligence dashboard using the backend data sent from python Flask

## Technology Stack
Pandas + Matplotlib + Seaborn + Flask + JavaScript + HTML + CSS

## Procedures
### Dataset
A dataset called "supermarket.xls" is downloaded from web.

### Data Preprocessing
- Foramt the date and time into datetime series using Python Pandas.
- Extract the month, day, day_of_week, hour from the datetime columns.
- Delete all the useless columns.

### Exploratory Data Analysis (EDA)
Visulaize the distributions of each column data and the relationships between multiple columns.

### Data Processing
Extract and format the columns data to be used as axis data in dashboard charts.

### Sending Data
Using Python Flask to send data from server to client in real time.

### Fetch Data
Using JavaScript to fetch the data sent by Flask.

### Visualization
Visualize the data through beautiful charts using Apache ECharts.js.

### Dashboard
Write HTML and CSS code to organize the sizes and positions of each chart and put them together to form a dashboard.

## Get Started
1. Install the 'Pandas', 'Matplotlib', 'Seaborn', 'Flask' using pip:
   ```python
    pip install pandas matplotlib seaborn flask
   ```
2. Install the Jupyter Notebook by using pip or using Anaconda environment.
   ```python
      pip install jupyter
    ```
3. Open and run the notebook file "DataAnalysis.ipynb".
4. Run dashboardDesigner.py in your PC's command line:
    ```bash
      cd [your_project_path]
      python dashboardDesigner.py
    ```
6. Open "http://127.0.0.1:5000/" in your browser.

## Dashborad
![Dashboard](/data/dashboard.png)


