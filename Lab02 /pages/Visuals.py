# This creates the page for displaying data visualizations.

import streamlit as st
import json
import matplotlib.pyplot as plt
from pathlib import Path
import plotly.express as px
import pandas as pd


# PAGE CONFIGURATION
st.set_page_config(
    page_title="Visuals",
    page_icon="📈",
)

# PAGE TITLE
st.title("Data Visualizations 📈")


# PART 1: GRAPHS FROM data.json
# --- YOUR CODE GOES HERE ---
file_path=Path(__file__).resolve().parent.parent/"data.json"
with open(file_path, "r") as file:
    data=json.load(file)
labels=[]
values=[]
for thing in data["data_points"]:
    labels.append(thing["label"])
    values.append(thing["value"])
st.header("Clothing Price")
fig, ax=plt.subplots()
ax.plot(labels, values, marker="*")
ax.set_title(data["chart_title"])
ax.set_xlabel("Clothing Items")
ax.set_ylabel("Price ($)")
st.pyplot(fig)
plt.close(fig)

st.header ("Lets Shop!")
st.subheader("Due to clothing shortage, limit yourself to 10 items per category!")
if "shirtamount" not in st.session_state:
    st.session_state.shirtamount=0
if "pantsamount" not in st.session_state:
    st.session_state.pantsamount=0
if "shoesamount" not in st.session_state:
    st.session_state.shoesamount=0
if "jacketamount" not in st.session_state:
    st.session_state.jacketamount=0
    
shirtamount=st.slider("Number of shirts",0,10,key="shirtamount")
pantsamount=st.slider("Number of pants",0,10,key="pantsamount")
shoesamount=st.slider("Number of shoes",0,10,key="shoesamount")
jacketamount=st.slider("Number of jacket",0,10,key="sjacketamount")

shirtprice=values[0]
pantsprice=values[1]
shoeprice=values[2]
jacketprice=values[3]

total= (shirtprice*shirtamount)+(pantsprice*pantsamount)+(shoeprice*shoesamount)+(jacketprice*jacketamount)

st.subheader("Your Total:")
with st.expander("Click to see"):
    st.subheader(total)
    st.subheader("Happy Shopping! 🛍️")
    shirttotal=shirtprice*shirtamount
    pantstotal=pantsprice*pantsamount
    shoestotal=shoeprice*shoesamount
    jackettotal=jacketprice*jacketamount
    clothes=['shirt', 'pants', 'shoes', 'jacket']
    totals=[shirttotal, pantstotal, shoestotal, jackettotal]

    if total>0:
        fig=px.pie(names=clothes, values=totals, title="Price distribution")
        st.plotly_chart(fig)
# PART 2: GRAPHS FROM data.csv
# --- YOUR CODE GOES HERE ---
st.header("Survey Results")
data_csv=pd.read_csv("data.csv")
st.dataframe(data_csv)

fig, ax=plt.subplots()
ax.bar(data_csv["Category"], data_csv["Value"])
ax.set_title("Clothes Spending Habit")
ax.set_xlabel("Clothing Items")
ax.set_ylabel("Price ($)")
st.pyplot(fig)
plt.close(fig)

st.header("Clothes Spending Habit")
if "responses" not in st.session_state:
    st.session_state.responses=len(data_csv)
if len(data_csv)>0:
    responses=st.slider("survey reponses amount", 1, len(data_csv), key="responses")
    fig=px.pie(data_csv.head(responses), names="Category", values="Value", title="Clothes Spending Habit")
    st.plotly_chart(fig)
else:
    st.warning("Enter survey response")
