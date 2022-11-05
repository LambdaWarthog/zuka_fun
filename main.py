import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

X=np.linspace(0, 4, 200)
Y=np.sin(X*np.pi)
dicttt={'X': X, 'Y': Y}
data=pd.DataFrame(dicttt)

image = px.line(data, x='X', y='Y')
st.plotly_chart(image)

