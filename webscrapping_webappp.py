# IMPORTING LIBRARIES
import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

# CREATING SIDEBAR SELECT BOX

menu=["INFO","Scrapping"]
choice=st.sidebar.selectbox("Menu",menu)

def Scrapping():
    url=st.text_input("Enter the url here",key='1')
    if url is not None:

        # STEP 1: Getting the request
        r = requests.get(url)
        htmlContent=r.content
        # print(htmlContent)

        # STEP 2: PARSE THE HTML(In a good tree like structure)

        soup = BeautifulSoup( htmlContent, 'html.parser')

        # STEP 3: HTML TREE TRAVERSAL

        a = 1
        b = 2
        c = 3
        d = 4

        # FOR PRODUCT NAME
        nam = st.text_input("Enter name div", key="a")
        name = soup.find_all('div', {"class": nam})
        nm = []
        for i in name:
            nm.append(i.text)
        st.write(len(nm))

        # FOR PRICE
        pri = st.text_input("Enter price div", key="b")
        price = soup.find_all('div', {"class": pri})
        pr = []
        for j in price:
            pr.append(j.text)
        st.write(len(pr))


        # FOR RATINGS
        rat = st.text_input("Enter rating div", key="c")
        rating = soup.find_all('div', {"class": rat})
        rt = []
        for k in rating:
            rt.append(k.text)
        st.write(len(rt))

        # FOR DESCRIPTION
        des = st.text_input("Enter rating div", key="d")
        description = soup.find_all('div', {"class": des})
        ds = []
        for l in description:
            ds.append(l.text)
        st.write(len(ds))


        # CLEANING  DATA
        f=6
        cl=st.number_input("new length",key=6)
        NM=nm[0:int(cl)]
        PR=pr[0:int(cl)]
        RT=rt[0:int(cl)]
        DS=ds[0:int(cl)]

        # CONVERTING INTO DATAFRAME
        data = {"Name": NM, "Price": PR,"Rating": RT,"Description":DS}

        df = pd.DataFrame(data)
        st.write(df)
        st.download_button(label="Download csv", data=df.to_csv(), mime='text/csv')

if choice=="Scrapping":
    Scrapping()
