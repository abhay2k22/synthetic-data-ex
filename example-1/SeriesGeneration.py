import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def loadData(fileName):
    data = pd.read_csv(fileName, delimiter=',')
    return data

def generateNoOfCases(df):
    # drop the row or column with any null value
    data = df.dropna(how='any')
    # find unique cases list
    cases_list = data.case_in_country.unique()
    # calculate weight to generate random selected data
    weights = data['case_in_country'].value_counts()
    weights = weights / np.sum(weights)
    case_values = []
    for i in range(len(data.index)):
        val = np.random.choice(cases_list, p=weights, size=(1,))
        case_values.append(val[0])

    synthetic_data = pd.DataFrame({'age': data['age'], 'case_in_country': case_values})
    return synthetic_data

def plotCases(data, synthetic_data):
    original_data = data[['age', 'case_in_country']].groupby(['age']).count()
    synthetic_data = synthetic_data[['age', 'case_in_country']].groupby(['age']).count()

    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12,6))
    original_data.plot(title='Real Data', ax=axes[0], subplots=True)
    synthetic_data.plot(title='Synthetic data', ax=axes[1], subplots=True)
    plt.legend(loc='best')
    axes[0].set_title("Real Data")
    axes[1].set_title("Synthetic Data")
    plt.show()

if __name__=="__main__":
    '''
    Synthetically Generating data for gender column.
    Loading Dataset.
    '''
    data = loadData('data.csv')
    print(data.head(5))
    ''' Shape of Data. i.e No. of Rows to generate data for '''
    print("No of rows to be generated : {}".format(data.shape))

    ''' Generating Data for # of Cases  '''
    synthetic_data = generateNoOfCases(data)
    plotCases(data, synthetic_data)