
import pandas as pd

# ovalilar = df[df.name.str.contains("ovali", case=False)]


def getGoogle(data):
    googleData = data[data['ga:sourceMedium'].str.contains("google", case=False)]
    criteoData = data[data['ga:sourceMedium'].str.contains("criteo", case=False)]
    print(googleData.values.__len__())
    return(googleData)

def get_google_dynamic_remarketing(datafr):
    data = datafr[datafr['ga:sourceMedium'].str.contains("google", case=False)]
    print(data.values.__len__())
    return(data)


def go():
    evciler1 = \
        [
            {
                'name': 'onur ovali',
                'age': 32
            },
            {
                'name': 'busra kabal ovali',
                'age': 28
            },
            {
                'name': 'buse kabal',
                'age': 23
            }
        ]

    evciler2 = {
        'name': ['onur ovali', 'busra kabal ovali', 'buse kabal'],
        'age': [32, 28, 23],
        'nick': ['iri', 'iri', 'bicirik'],
        'kilo': [95, 68, 56]
    }

    # df = pd.read_csv("evciler.csv")
    # df = pd.DataFrame(evciler1)
    df = pd.DataFrame(evciler2)

    rows, columns = df.shape

    print('')

    # print(df)
    # print(rows)
    # print(columns)
    # print(df.head(2))
    # print(df.tail(2))
    # print(df[2:5])
    # print(df[:])
    # print(df.columns)
    # print(df.age)
    # print(df['name'])
    # print(type(df['age']))
    # print( df[['name', 'nick']] )
    # print( df['age'].max() )
    # print(df['age'].mean())
    # print(df['age'].std())
    # print(df.describe())
    # print(df[df.kilo == df['kilo'].max()])
    # print(df[['name', 'age']][df.kilo == df['kilo'].max()])

    # df.set_index(['age'], inplace=True)
    # print(df.loc[23])
    # df.reset_index(inplace=True)
    # print(df) asdasd

    # df.set_index(['nick'], inplace=True)
    # print(df)
    # print(df.loc['iri'])

    # print(df[['name', 'age']][df.kilo > df['kilo'].min()])

    # ovalilar = df[ 'ovali' in df['name'] ]

    # ovalilar = df.name.str.contains("ovali", case=False)
    ovalilar = df[df.name.str.contains("ovali", case=False)]
    print(ovalilar)


