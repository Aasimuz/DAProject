import pandas as pd 
from sqlalchemy import create_engine
engine = create_engine(
    "mysql+pymysql://root:Aasim_56789@localhost:3306/ecommerce"
)
list_csvs=[
    ('customers','customers.csv'),
    ('geolocation','geolocation.csv'),
    ('order_items','order_items.csv'),
    ('orders','orders.csv'),
    ('payments','payments.csv'),
    ('products','products.csv'),
    ('sellers','sellers.csv')
]

for table,file in list_csvs:
    filePath=f'./target/{file}'
    df = pd.read_csv(filePath)
    df.columns=df.columns.str.replace(" ","_")
    df.to_sql(
        name=table,
        con=engine,
        if_exists='replace',
        index=False
    )
    print(f"imported{file}succesfully into {table}")
engine.dispose()    
### use all unique cities where customers are located
query = 'select distinct customer_city as citiy from customers'
df =pd.read_sql(query,engine)
df
