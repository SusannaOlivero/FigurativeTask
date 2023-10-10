import openai
import json

data = []
for line in open("/content/FigTask/FLUTE/FLUTEfinaltest.json"):
    line = json.loads(line)
    data.append(line)
    
# Imposta la tua chiave API di OpenAI
api_key = "LA_TUA_API_KEY"

for i in range(len(data)):
    sentence_A = data[i]["premise"]
    sentence_B = data[i]["hypothesis"]
    instruction = "Does the sentence "+'"'+sentence_A+'" entail or contradict the sentence "'+sentence_B+'"? Please answer between '+'"Entails" or "Contradicts".'# and explain your decision in a sentence.'    
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="davinci",
        prompt=instruction,
        max_tokens=1,  # Limita la risposta a una singola parola (yes o no)
    )
    answer = response.choices[0].text.strip()
    
    if "Entails." in answer:
        predictedlabel = "Entailment"
        #predictedExpl = answer.split("Entails.")[1].lstrip().capitalize()
    elif "Contradicts." in answer:
        predictedlabel = "Contradiction"
        #predictedExpl = answer.split("Contradicts.")[1].lstrip().capitalize()
    data[i]["predicted_label"] = predictedlabel
    #data[i]["model_explanation"] = predictedExpl

with open("./drive/MyDrive/NLP/predictions.json","w") as f:
    f.write(json.dumps(data,indent=4))
