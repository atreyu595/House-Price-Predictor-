# House-Price-Predictor-

The Following repository contains source code belonging to personal project of mine that extends upon the conventional House Price prediction using Linear Regression.

The following project aims at developing a crucial understanding of Full-stack Data Science development. The project consists of:
- Requirements Analysis: Understand the goal, context and key metrics to observe.
- Data Collection: The data was sourced from a reliable website such as Kaggle -> Dataset: USA Housing: https://www.kaggle.com/vedavyasv/usa-housing.
- Exploratory Analysis: Understand key descriptive and sample statistics, determine any null values, generate plots which assess the distributions and normality of the dataset.
- Data Wrangling/Manipulation: Separate and convert data types, isolate explanatory and predictor variables.
- Data Pre-processing: Split data into training and testing sets
- Model Development: Develop regression analysis
- Model Evaluation: Analyse goodness-of-fit, RMSE and correlations.
- Deployment: Deploy model into website application

The full script can be viewed in file "House Price Predictor - Exploratory Analysis.ipynb"
A full overview and analysis of the whole project can be read in my recently published article in Towards Data Science -> https://towardsdatascience.com/deploying-machine-learning-models-into-a-website-using-flask-8582b7ce8802

## After Analysis
After the analysis, the following scripts were then developed to deploy the model:
- app.py: The Flask application
- model.py: The regression model program  
- model.pkl: the saved model using the "pickle" library
- index.html: The home page of the application

Additionally, there are the 2 images which were used for the design.

Finally, the working tree directory used for this project is:

\project
    app.py
    model.py
    model.pkl
    \static
        \img 
          \images in repo 
        \styles 
          \styling is implemented within "index.html"
    \template
        index.html
