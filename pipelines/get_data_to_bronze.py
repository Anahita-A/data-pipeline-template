import requests
import pandas as pd
from pipelines.load import Load

def extract_data_from_source():
    """
    Get the top gainers, losers and most active stocks from the source

    params: 
        source: str
    """

    url = 'https://www.alphavantage.co/query?function=TOP_GAINERS_LOSERS&apikey={Params.API_KEY}'
    response = requests.get(url)
    data = response.json()

    return data

def main():
    load = Load()
    data = extract_data_from_source()
    df = pd.DataFrame(data)

    
    csv = df.to_csv().encode('utf-8')
    date = data['last_updated']
    year = date[:4]
    month = date[5:7]
    day = date[8:10]

    if df is not None:
        load.write(csv, 
                      bucket = "bronze", 
                      table = f"{year}/{month}/{day}")
        
        print("Load complete.")
    else:
        print("Load failed")

if __name__ == "__main__":
    main()