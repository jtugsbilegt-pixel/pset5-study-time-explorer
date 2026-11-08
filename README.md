# PSET5 — Study Time Explorer

A simple interactive Streamlit application by Tugsbilegt Jargalsaikhan.

## Features
- Text input for your name.
- Dropdown to choose a bar, pie, or line chart.
- Numeric inputs for study hours across five subjects.
- Weekly goal slider, summary metrics, and progress bar.
- Interactive Plotly visualization, data table, and CSV download.
- Handles a plan with zero hours gracefully.

## Run locally

```sh
pip install -r requirements.txt
streamlit run app.py
```

## Deploy
Use Streamlit Community Cloud with this repository, branch `main`, and entry point `app.py`.

## Usage
Enter your name, change subject hours, and choose a chart type in the sidebar. The visualization updates automatically. Inputs are used only in the current session.

Built with Python, Streamlit, pandas, and Plotly.
