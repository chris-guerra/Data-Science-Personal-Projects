# data-science-and-ML-scripts
This repository consists of data science and machine learning standard code that I use often and have accumulated, it is a growing repository where I include explanations for the reader with examples.

## LangChain

LangChain is a framework and toolkit for building applications that leverage large language models, like GPT, to automate tasks and enhance natural language understanding. This section is a full overview on how to use it.

## Classification

This section summarizes different data science topics with general information to help the viewer to select different metrics and build good systems for a variety of tasks.

- [**Classification:**](classification/Classification.ipynb) This notebooks is a summary on classification. Specifically how to select good metrics for classification tasks, pick the appropiate precision/recall trade-off, compare classifiers, and build good classification systems for a variety of tasks. **Keywords:** ***Binary Classifier, Confusion Matrix, Precision, Recall, F1 Score, PR Curve, ROC Curve, Multiclass Classification, OvR, OvO***.

### Examples
- [**Classification - Predicting Passenger Survival on Titanic:**](<classification/Classification - Predict Passenger Survival On Titanic.ipynb>) This notebook has the purpose of predict whether or not a passenger survived the Titanic based on attributes such as their age, sex, passenger class, where they embarked and so on. The result is an 82% accuracy based on the suggested models. **Keywords:** ***Classification, EDA, Creating Custom Transformers, Creating Pipelines, Model Selection, Random Search, Model Evaluation, Random Forest, K-Nearest Neighbours***.

## Regression

### Examples
- [**Regression - Predicting Median Housing Price per District:**](examples/Predicting Median Housing Price per District.ipynb) This Jupyter notebook has the purpose of showing a complete project to predict the median housing price of a district in California, from obtaining data to model evaluation. **Keywords:** ***EDA, Creating Custom Transformers, Creating Pipelines, Model Selection, Grid Search and Random Search, Model Evaluation***.

## Web Scrapping
- [**Web Scraping Spanish Book Data:**](web_scrapping/Web Scraping Spanish Book Data.ipynb) This Jupyter notebook shows the code and results of web scraping 'Lectulandia', a website where books in spanish could be downloaded. The objective is to obtain a database with all of the books available in the website with information as genre and description plus the hyperlink to download them both in pdf and epub. **Keywords:** ***Web-Scraping***.

## Misc

This section has different miscellaneous code that has been developed that might not directly apply to data science.

- [**Algorithms for Stanford Coursera Course:**](misc/Programmed Algorithms .ipynb) This Jupyter notebook has all of the algorithms that had to be developed for the Stanford coursera course. **Keywords:** ***Recursions, Divide & Conquer Algorithms, QuickSort, Randomized Selection, Graphs And The Contraction Algorithm, Graph Search and Connectivity, Computing strongest components, Dijkstra's Shortest Path Algorithm, Heaps, Greedy algorithms, Scheduling Algorithms***.

## Functions
Many functions I have used and reused for múltiple scripts.
- [**SSH Tunnel**](functions/data_conections.py)
- [**OpenAI API**](functions/openai_models.py)
- [**General Statistics**](functions/stats.py)

## Useful Prompts
- [**EDA Prompts**](useful_prompts/EDA.txt)

## Instructions to set up the repo

### Crear venv
1. Crear el venv: python3 -m venv venv
2. Activar el venv: source venv/bin/activate
3. Desactivar: deactivate

### Import libraries
pip install -r requirements.txt