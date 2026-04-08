# ✅ STEP 1: Install
#!pip install transformers requests

# ✅ STEP 2: Imports
import requests
from transformers import pipeline

# ✅ STEP 3: Load free local LLM
generator = pipeline("text-generation", model="distilgpt2")

# ✅ STEP 4: Perception function — get country data (NO API key!)
def get_country_info(country):
    url = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url).json()
    if isinstance(response, list) and len(response) > 0:
        data = response[0]
        info = {
            "Name": data.get("name", {}).get("common"),
            "Population": data.get("population"),
            "Region": data.get("region"),
            "Subregion": data.get("subregion"),
            "Capital": data.get("capital", ["N/A"])[0],
            "Currency": ", ".join(data.get("currencies", {}).keys()),
            "Languages": ", ".join(data.get("languages", {}).values()),
            "Flag": data.get("flags", {}).get("png"),
            "Borders": ", ".join(data.get("borders", [])) if data.get("borders") else "None"
        }
        return info
    else:
        return None

# ✅ STEP 5: Reasoning & Generation with LLM
def summarize_country_info(info):
    prompt = f"""
Create a short, friendly summary for a traveler about this country:

Name: {info['Name']}
Population: {info['Population']}
Region: {info['Region']}
Subregion: {info['Subregion']}
Capital: {info['Capital']}
Currency: {info['Currency']}
Languages: {info['Languages']}
Neighbors: {info['Borders']}
"""
    result = generator(
        prompt,
        max_new_tokens=100,
        do_sample=False,
        num_beams=2
    )[0]['generated_text']
    return result

# ✅ STEP 6: Agent loop
def agentic_country_researcher():
    print("🤖 Hello! I’m your Agentic AI Country Info Researcher 🌍")

    country = input("🌎 Which country do you want to know about? ")

    # Perceive: Web API
    info = get_country_info(country)
    if not info:
        print(f"❌ Sorry, I couldn't find information for '{country}'.")
        return

    # Output raw facts
    print("\n✅ Raw Facts:")
    for k, v in info.items():
        print(f"{k}: {v}")

    # Reason: Summarize with LLM
    summary = summarize_country_info(info)
    print("\n📝 AI Summary:")
    print(summary)

    # Control: Reflection step
    more = input("\n🔍 Do you want me to add more details? (yes/no) ")
    if more.lower() == "yes":
        more_prompt = f"Expand the summary for {country} with some travel tips."
        more_summary = generator(
            more_prompt,
            max_new_tokens=100,
            do_sample=False,
            num_beams=2
        )[0]['generated_text']
        print("\n✨ Expanded Summary:\n", more_summary)
    else:
        print("\n🎉 Done! Happy researching!")

# ✅ STEP 7: Run the agent
agentic_country_researcher()