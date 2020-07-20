from sdv import SDV
import pandas as pd
import json


def fit_save_model(mfile):
    sdv = SDV()
    ''' Original Data '''
    users = pd.DataFrame({
        'user_id': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        'country': ['USA', 'UK', 'ES', 'UK', 'USA', 'DE', 'BG', 'ES', 'FR', 'UK'],
        'gender': ['M', 'F', None, 'M', 'F', 'M', 'F', None, 'F', None],
        'age': [34, 23, 44, 22, 54, 57, 45, 41, 23, 30]
    })

    tables = {
        'users': users
    }

    with open('./user_table_metadata.json') as metadata_file:
        metadata = json.load(metadata_file)
        sdv.fit(metadata, tables)
        sdv.save(mfile)


def genSyntheticData(mfile, rowcount):
    sdv = SDV.load(mfile)
    samples = sdv.sample_all(rowcount)
    df = pd.DataFrame(samples['users'])
    return df


if __name__ == "__main__":
    mfile = 'user_table_model.pkl'
    # create a model using metadata & data
    fit_save_model(mfile)

    # generate synthetic data based on given model file
    rowcount = 100
    df = genSyntheticData(mfile, rowcount)

    ''' Print Synthetsized Data '''
    print(df.head(5))