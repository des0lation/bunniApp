import requests
import json
import streamlit as st

st.set_page_config(
    page_title="My Streamlit App",  # default page title
    page_icon="🌐",  # default favicon
    layout="wide",  # wide mode
    initial_sidebar_state="expanded",  # sidebar state
)



url = "https://thegraph.com/hosted-service/subgraph/bunniapp/bunni-mainnet"

headers = {
    "Content-Type": "application/json",
}

body = {
    "query": """
        {
          gauges(
            where: {
              address: "0xa718193e1348fd4def3063e7f4b4154baacb0214"
            }
          ){
            votes {
              power
              timestamp
              weight
              voter
            }
          }
        }
    """
}

response = requests.post(url, headers=headers, data=json.dumps(body))
response_json = response.json()

print(json.dumps(response_json, indent=4))

