# Final-Project-JCDS-Bekasi
## Term Deposit Prediction
Sri Astuti Heyanti's Final Project of Job Connector Data Science Purwadhika Digital Technology School Bekasi.

Term Deposit Prediction is project with apply machine learning algorithms to build a predictive model of the dataset in order to provide a necessary suggestion for the marketing campaign team. The goal is to predict whether a client will open a term deposit or not.

Detailed description of the dataset's content is describe in this source

https://www.kaggle.com/janiobachmann/bank-marketing-dataset

### Explore Data

In this step, we do Exploratory Data Analysis (EDA). EDA includes looking for missing values and outliers, data visualization, feature selection and statistical tests.

Data Visualization :

![alt text](https://github.com/achiastuti/Final-Project-JCDS-Bekasi/blob/master/data/deposit.png?raw=true)

Statistical Test


![alt text](https://github.com/achiastuti/Final-Project-JCDS-Bekasi/blob/master/assets/img/statistic.png?raw=true)


Dataframe after EDA look like this : 


![alt text](https://github.com/achiastuti/Final-Project-JCDS-Bekasi/blob/master/assets/img/dataframe.png?raw=true)

### Machine Learning

Before we feed our data into the model, we need to split our dataset into train and test datasets. We will use sklearn train test split.

After that we fit model to algorithms. We use four classification approach:
1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier
4. Gradient Boost Classifier

Among the four classification approach used to model the data, the Logistic Regression is the best algorithms with highest precision positive and recall negative.


![alt text](https://github.com/achiastuti/Final-Project-JCDS-Bekasi/blob/master/assets/img/bestmodel.png?raw=true)

### Best Model
To optimize model Logistic Regression , we do resampling with SMOTE , Random Over Sampling, and Random Under Sampler


![alt text](https://github.com/achiastuti/Final-Project-JCDS-Bekasi/blob/master/assets/img/bestmodel2.png?raw=true)

In this prediction, the choice is to reduce the likelihood of the model making a False Positive (the customers are not potential to open term deposit but are predicted potential) as this will make the marketing team's campaign effective and efficient. This will help in minimizing the cost to the bank by avoiding to call customers who are unlikely to open the term deposit. Based on the comparing above, select logistic regression with shift threshold to 0.9 as the best model to predict. This can be seen from the smallest false positive value in the confusion matrix.


![alt text](https://github.com/achiastuti/Final-Project-JCDS-Bekasi/blob/master/assets/img/threshold2.png?raw=true)

### Dashboard
There are 4 pages, which are:

#### Home 
This page is contain about objective dashboard

![alt text](https://github.com/achiastuti/Final-Project-JCDS-Bekasi/blob/master/assets/img/home.png?raw=true)

#### Prediction
This page is to fill features for prediction term deposit. There is 11 features which is, age, job, marital, education, default, housing, loan, duration, campaign, previous, poutcome.


![alt text](https://github.com/achiastuti/Final-Project-JCDS-Bekasi/blob/master/assets/img/prediction.png?raw=true)

#### Visualization
This page shows some plot. There are countplot for categorical feature, histogram for numerical features and pie chart for count percentage deposit.


![alt text](https://github.com/achiastuti/Final-Project-JCDS-Bekasi/blob/master/assets/img/visualization.png?raw=true)

### Author
This page tells you more about me.


![alt text](https://github.com/achiastuti/Final-Project-JCDS-Bekasi/blob/master/assets/img/author.png?raw=true)
