from sdv import SDV
import pandas as pd
import json


def loadData():
    ''' Generating Data For Two Tables Joined By User_id Column.  '''
    users = pd.DataFrame({
        'user_id': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'country': ['USA', 'UK', 'ES', 'UK', 'USA', 'DE', 'BG', 'ES', 'FR', 'UK'],
        'gender': ['M', 'F', None, 'M', 'F', 'M', 'F', None, 'F', None],
        'age': [34, 23, 44, 22, 54, 57, 45, 41, 23, 30]
    })

    sessions = pd.DataFrame({
        'session_id': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'user_id': [0, 1, 1, 2, 4, 5, 6, 6, 6, 8],
        'device': ['mobile', 'tablet', 'tablet', 'mobile', 'mobile',
                   'mobile', 'mobile', 'tablet', 'mobile', 'tablet'],
        'os': ['android', 'ios', 'android', 'android', 'ios',
               'android', 'ios', 'ios', 'ios', 'ios']
    })

    ''' Original Data '''
    tables = {
        'users': users,
        'sessions': sessions
    }
    return tables


def createmodel(tables, mfile):
    sdv = SDV()
    with open('./join_table_metadata.json') as metadata_file:
        metadata = json.load(metadata_file)
        sdv.fit(metadata, tables)
        sdv.save(mfile)


def generateSyntheticData(mfile):
    sdv = SDV.load(mfile)
    samples = sdv.sample_all(10)
    return samples


if __name__ == "__main__":
    tables = loadData()
    mfile = 'join_table_model.pkl'
    createmodel(tables, mfile)

    # generating data
    samples = generateSyntheticData(mfile)
    print(samples['users'])
    print('\n')
    print(samples['sessions'])
    print('\n')


