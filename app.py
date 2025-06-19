import streamlit as st
import requests
import json

st.title("Vapi Call Logs")
st.divider()
st.write("You will find all of the information from each call here")

API_KEY = st.secrets["API_KEY"]
API_ENDPOINT = "https://api.vapi.ai/call"

def call_logs():
    headers = {
        'Authorization': f"Bearer {API_KEY}",
        'Content-Type': 'application/json'
    }

    response = requests.get(API_ENDPOINT, headers=headers)
    if response.status_code == 200:
        print(response.json())
        return response.json()
    else:
        print("error")
        st.error("The app encountered an error: " + response.status_code)
        return []
    
data = call_logs()
if not data: 
    st.error("There is no call history, try making a call first")
else: 
    for call in data: 
        with st.expander("📞 Call ID: " + call.get('id') + "Status: " + call.get("status")):
            st.subheader("Basic call information")
            st.json({
                "Type: ": call.get('type'), 
                "Started at: ": call.get('startedAt'),
                "Ended at": call.get("endedAt"),
                "Cost: ": call.get("cost")
            })
            st.subheader("URLs")
            st.write("⏺️ Recording link: " + call.get("recordingUrl"))

            st.subheader("Insights")
            st.markdown(call.get("summary"))