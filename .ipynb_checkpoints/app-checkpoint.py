import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(layout='wide')
nav = st.sidebar.radio("Navigation",["Home","EDA","Vizzes"])


if nav == "Home":
    st.title('Data Analysis on Anime-Planet')
    st.write("![Your Awsome GIF](https://media.giphy.com/media/1CEoPFtZIIHbG/source.gif)")
    
    st.header("Research goal:")
    st.write("My goal is to identify some of the top Anime on Anime-planet and look at their relationships")
    
    st.subheader("Hypothesis:")
    st.write(" The anime 'One Piece' will be one of the top rated anime's as well as the anime with the highest number of episodes. ")
    

    
if nav == "EDA":
    st.header("Anime-Planet Exploratory Data Analysis")
    df = pd.read_csv('datasets/anime.csv')
    st.dataframe(df)
    
   
    

if nav == "Vizzes":
    st.header("Data Visualization using Bokeh")
    
    df = pd.read_csv('datasets/anime.csv')
    st.header("Top 20 longest running Anime")
    
    df.replace({"Unknown":0}, inplace = True)
    df = df.astype({'Episodes': 'int64'})
    df_sorted= df.sort_values('Episodes',ascending=False)
    x = df_sorted['Name'].head(20)
    y = df_sorted['Episodes'].head(20)
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd',
          '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
    fig = plt.figure(figsize=(20,10))
    plt.xlabel('Episodes')
    plt.ylabel('Anime')
    plt.barh(x,y,color=colors)
    st.pyplot(fig)
    
    