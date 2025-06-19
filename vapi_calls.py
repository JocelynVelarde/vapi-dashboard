from vapi_python import Vapi
import streamlit as st

PUBLIC_KEY = st.secrets["PUBLIC_KEY"]

vapi = Vapi(api_key=PUBLIC_KEY)

vapi.start(assistant_id='bbb5e0f9-f004-4736-9511-7fdc0329247f')


