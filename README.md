# The Data Science Compendium

Welcome to the Data Science Compendium! This repository contains a collection of standard code snippets, explanations, and examples for data science and machine learning tasks. It’s a growing resource designed to help you understand and apply various concepts in data science.

## Table of Contents
- [Introduction to Data Science](introduction-to-data-science)
- [Classical Machine Learning](classical-machine-learning)
  - [Data Collection](data-collection)
  - [Data Cleaning](data-cleaning)
  - [Exploratory Data Analysis](exploratory-data-analysis)
  - [Feature Engineering](feature-engineering)
  - [Model Building](model-building)
    - [Supervised Learning](supervised-learning)
      - [Classification](classification)
      - [Regression](regression)
  - [Model Evaluation](model-evaluation)
- [Retrieval Augmented Generation](retrieval-augmented-generation)
- [Pending Topics](pending-topics)
- [Useful ML Code](useful-ml-cod)
- [Useful Prompts](useful-prompts)
- [Resources](resources)

## Introduction to Data Science

Here we explain from a large scope what data science is, it's key concepts and tools and libraries. We also include an example of how a classic Data Science project would look like end to end.
- [Introduction to Data Science](introduction_to_data_science/introduction_to_data_science.md)
- [Machine Learning Project Checklist](introduction_to_data_science/machine_learning_project_checklist.md)

## Classical Machine Learning

### Data Collection
Pending.
#### APIs
#### Web Scraping
- [**Web Scraping Spanish Book Data:**](<web_scrapping/Web Scraping Spanish Book Data.ipynb>) This Jupyter notebook shows the code and results of web scraping 'Lectulandia', a website where books in spanish could be downloaded. The objective is to obtain a database with all of the books available in the website with information as genre and description plus the hyperlink to download them both in pdf and epub. **Keywords:** ***Web-Scraping***.
#### Databases

### Data Cleaning
Pending.
#### Handling Missing Values
#### Data Transformation
#### Outlier Detection

### Exploratory Data Analysis
Pending.
#### Descriptive Statistics
#### Visualization Techniques
#### Correlation Analysis

### Feature Engineering
Pending.
#### Feature Selection
#### Feature Creation
#### Feature Scaling

### Model Building

#### Supervised Learning

##### Classification

- [**Classification:**](classification/Classification.ipynb) This notebooks is a summary on classification. Specifically how to select good metrics for classification tasks, pick the appropiate precision/recall trade-off, compare classifiers, and build good classification systems for a variety of tasks. **Keywords:** ***Binary Classifier, Confusion Matrix, Precision, Recall, F1 Score, PR Curve, ROC Curve, Multiclass Classification, OvR, OvO***.
- [**Classification - Predicting Passenger Survival on Titanic:**](<classification/Classification - Predict Passenger Survival On Titanic.ipynb>) This notebook has the purpose of predict whether or not a passenger survived the Titanic based on attributes such as their age, sex, passenger class, where they embarked and so on. The result is an 82% accuracy based on the suggested models. **Keywords:** ***Classification, EDA, Creating Custom Transformers, Creating Pipelines, Model Selection, Random Search, Model Evaluation, Random Forest, K-Nearest Neighbours***.

##### Regression
- [**Regression - Predicting Median Housing Price per District:**](<examples/Predicting Median Housing Price per District.ipynb>) This Jupyter notebook has the purpose of showing a complete project to predict the median housing price of a district in California, from obtaining data to model evaluation. **Keywords:** ***EDA, Creating Custom Transformers, Creating Pipelines, Model Selection, Grid Search and Random Search, Model Evaluation***.
#### Unsupervised Learning
#### Model Selection

### Model Evaluation

#### Metrics
#### Cross-Validation
#### Hyperparameter Tuning

## Retrieval Augmented Generation

## LangChain

LangChain is a framework and toolkit for building applications that leverage large language models, like GPT, to automate tasks and enhance natural language understanding. This section is a full overview on how to use it.

- [**Part 1 - Models, prompts and output parsers:**](langchain/models_prompts_parsers.ipynb) This section explains how to use templates with OpenAI and Langchain and using parsers to structure the output.

## Pending Topics
- DeepLearning
- Natural Language Processing
- Big Data Technologies
- Cloud services
- Time series


## Useful ML Code
Many functions I have used and reused for múltiple scripts.
- [**SSH Tunnel**](functions/data_conections.py)
- [**OpenAI API**](functions/openai_models.py)
- [**General Statistics**](functions/stats.py)

- [**EDA Prompts**](useful_prompts/EDA.txt)


## Resources
### Books
- Hand On ML
### Courses
### Tutorials
