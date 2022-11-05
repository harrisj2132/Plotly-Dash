from distutils.log import debug
from turtle import width
import dash
from dash import dcc,html,Input,Output,State
from dash_table import DataTable
import pandas as pd

df=pd.read_excel(r'C:\Users\venkat\Downloads\Sample - Superstore.xls')
df['State']='['+df['State']+']'+'(https://en.wikipedia.org/wiki/'+df['State'].str.replace(' ','')+')'

app=dash.Dash(__name__)

def hyperlink(col):
    if col in ['State']:
        return {'id':col,'name':col,'presentation':'markdown'}
    else:
        return {'id':col,'name':col}

app.layout=html.Div([
    html.Div([
        html.Div(dcc.Dropdown(id='catdrop',options=sorted(df['Category'].unique())),style=dict(width='48%',display='inline-block')),
        html.Div(dcc.Dropdown(id='subcatdrop',options=sorted(df['Sub-Category'].unique())),style=dict(width='48%',display='inline-block')),
    ]),
        dcc.Loading(DataTable(id='table',data=df.to_dict('records'),columns=[hyperlink(col) for col in df.columns]),fullscreen=True,type='circle')
            
])

if __name__=='__main__':
    app.run_server(debug=True)