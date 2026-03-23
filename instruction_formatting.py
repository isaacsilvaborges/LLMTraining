import pandas as pd 
import json
import random

def create_llm_dataset(X, y, file_name="farmer_dataset.jsonl"):

    system_prompt = "You are now an expert computational agronomist. Predict the crop yield in tons per hectare based on the farmer's description. Respond ONLY with the numerical value."

    # The more variations we have the better, but since it's a study thing, let1s focus on these three
    templates = [
        "Hey, there. I'm growing {crop} out here in the {region} on some {soil}. It's been pretty {weather} lately, and we've gotten a solid {rain} mm of rain and it's sitting around {temp} °C. {irrigation_text}, and {fertilizer_text}. With {days} days until harvest, what kind of yield per hectare should I be expecting?",
        "Morning! I'm trying to map out my harvest. I've got a {crop} crop going in {soil} dirt out {region}. We're looking at {days} days to harvest. {irrigation_text} and {fertilizer_text}. The weather's been {weather}, temperatures are hovering around {temp} °C, and we've seen about {rain} mm of rain. Can you give me a yield estimate in tons per hectare?",
        "Could use an expert opinion. I'm {days} days out from harvesting my {crop} in the {region} region. The ground is {soil}. We've had a lot of {weather} days, {rain} mm of rainfall, and average temps of {temp} °C. {irrigation_text}, and {fertilizer_text}. How many tons per hectare do you think this field will pull?"
    ]

    with open(file_name, 'w', encoding='utf-8') as file:

        for idx, row in X.iterrows():
            # Converting the values so the LLM can use it in the texts above
            crop = row['Crop']
            region = row['Region']
            soil = row['Soil_Type']
            weather = row['Weather_Condition']
            days = int(row['Days_to_Harvest'])
            rain = round(row['Rainfall_mm'], 1)
            temp = round(row['Temperature_Celsius'], 1)
            fert = bool(row['Fertilizer_Used'])
            irrig = bool(row['Irrigation_Used'])
            irrigation_text = "I've been keeping the irrigation running" if irrig else "I'm relying solely on rainfall"
            fertilizer_text = "I decided to use fertilizer this time around" if fert else "I skipped the fertilizer completely"

            yield_val = round(y.loc[idx], 4)

            template = random.choice(templates)

            message = template.format(
                crop=crop, region=region, soil=soil, weather=weather, 
                rain=rain, temp=temp, days=days, 
                irrigation_text=irrigation_text, fertilizer_text=fertilizer_text
            )

            json_record = {
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": message},
                    {"role": "assistant", "content": str(yield_val)}
                ]
            }

            file.write(json.dumps(json_record) + '\n')
            print(f"Dataset gerado com sucesso: '{file_name}' com {len(X)} exemplos!")
