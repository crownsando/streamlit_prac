import streamlit as st
import pandas as pd
import FinanceDataReader as fdr
import datetime
import matplotlib.pyplot as plt
import matplotlib 
from io import BytesIO
import plotly.graph_objects as go
import pandas as pd

def get_stock_info():
    base_url =  "http://kind.krx.co.kr/corpgeneral/corpList.do"    
    method = "download"
    url = "{0}?method={1}".format(base_url, method)   
    df = pd.read_html(url, header=0)[0]
    df['종목코드']= df['종목코드'].apply(lambda x: f"{x:06d}")     
    df = df[['회사명','종목코드']]
    return df

def get_ticker_symbol(company_name):     
    df = get_stock_info()
    code = df[df['회사명']==company_name]['종목코드'].values    
    ticker_symbol = code[0]
    return ticker_symbol

with st.sidebar:
    st.header("회사이름과 기간을 입력하세요")
    stock_name = st.text_input('회사이름',value='NAVER')
    date_range = st.date_input('시작일-종료일',[datetime.date(1991,1,2),datetime.date(2023,4,30)])

# 코드 조각 추가
ticker_symbol = get_ticker_symbol(stock_name)     
start_p = date_range[0]               
end_p = date_range[1] + datetime.timedelta(days=1) 
df = fdr.DataReader(ticker_symbol, start_p, end_p, exchange="KRX")
df.index = df.index.date
st.subheader(f"[{stock_name}] 주가 데이터")
st.dataframe(df.head())