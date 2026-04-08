from streamlit_lottie import st_lottie
import requests

def load(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()
lott=load("https://assets2.lottiefiles.com/packages/lf20_touohxv0.json")
st_lottie(lott,height=300)