import streamlit as st 
from textblob import TextBlob 

# Title
st.title("Sentiment Analysis")

result_sentiment = 2
# Sentiment Analysis
st.subheader("Analyse Your Text")

message = st.text_area("Enter Text")
if st.button("Analyze"):
      blob = TextBlob(message)
      result_sentiment = blob.sentiment[0]
			
    
if result_sentiment > 0.5 and result_sentiment < 1 :
      st.write('Prediction  :')
      st.subheader('Positive')
      st.success(f'Score : {result_sentiment}')

elif result_sentiment < 0 :
      st.write('Prediction  :')
      st.subheader('Negative')
      st.success(f'Score : {result_sentiment}')

elif result_sentiment >= 0 and result_sentiment <= 0.5 :
      st.write('Prediction  :')
      st.subheader('Neutral')
      st.success(f'Score : {result_sentiment}')
