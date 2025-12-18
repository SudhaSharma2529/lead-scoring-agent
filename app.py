import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lead Scoring Agent", layout="wide")

st.title("Lead Scoring Agent – 3D In-Vitro Models")
st.write("Demo project for lead identification and ranking")

data = [
    {
        "Name": "Dr. Alice Morgan",
        "Title": "Director of Toxicology",
        "Company": "BioNova Therapeutics",
        "Funding": "Series B",
        "Uses Similar Tech": True,
        "Recent Liver Paper": True,
        "Person Location": "Cambridge, MA",
        "Company HQ": "Cambridge, MA",
        "Email": "alice@bionova.com",
        "LinkedIn": "https://linkedin.com/in/alicemorgan"
    },
    {
        "Name": "Dr. John Lee",
        "Title": "Junior Scientist",
        "Company": "HealthX Labs",
        "Funding": "Not Funded",
        "Uses Similar Tech": False,
        "Recent Liver Paper": False,
        "Person Location": "Austin, TX",
        "Company HQ": "Austin, TX",
        "Email": "john@healthx.com",
        "LinkedIn": "https://linkedin.com/in/johnlee"
    }
]

df = pd.DataFrame(data)

def calculate_score(row):
    score = 0

    if "toxicology" in row["Title"].lower() or "safety" in row["Title"].lower():
        score += 30

    if row["Funding"] in ["Series A", "Series B"]:
        score += 20

    if row["Uses Similar Tech"]:
        score += 15

    if row["Recent Liver Paper"]:
        score += 40

    if any(city in row["Person Location"].lower() for city in ["cambridge", "boston", "basel"]):
        score += 10

    return min(score, 100)

df["Probability Score"] = df.apply(calculate_score, axis=1)
df["Rank"] = df["Probability Score"].rank(ascending=False).astype(int)

st.subheader("Ranked Leads")
st.dataframe(df, use_container_width=True)

st.download_button(
    "Download CSV",
    df.to_csv(index=False),
    "ranked_leads.csv",
    "text/csv"
)
