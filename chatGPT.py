import os
import openai
import requests
import json
openai.api_key = "sk-..."

def BasicGeneration(userPrompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": userPrompt}
        ]
    )
    return completion.choices[0].message.content

def GetBitcoinPrices():
    

    url = "https://coinranking1.p.rapidapi.com/coin/Qwsogvtv82FCd/history"

    querystring = {"referenceCurrencyUuid":"yhjMzLPhuIDl","timePeriod":"7d"}

    headers = {
        "X-RapidAPI-Key": "5c539e37c9mshc254819b769a52ap17ca86jsn773b2a0f9832",
        "X-RapidAPI-Host": "coinranking1.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    JSONResult = json.loads(response.text)
    history = JSONResult["data"]["history"]
    prices = []
    for change in history:
        prices.append(change["price"])
        
    pricesList = ",".join(prices)
    return pricesList

prompt1 = "role: you are a teacher with 10 years of experience in JavaScript \ncontent: explain to a 6 years old how to declare variables in JavaScript \nlength: max 100 tokens"

bitcoinPrices = GetBitcoinPrices()

chatGPTPrompt = f"""role: you are an expert crypto trader with more than 10 years of experience
content: I will provide you with a list of bitcoin prices for the last 7 days
question: can you provide me with a technical analyses of bitcoin based on these prices?
result: here is what i want: Price Overview, Moving Averages, Relative Strength Index (RSI), Moving Average Converge Divergence (MACD), Advice and Suggestion. Do I buy or sell? Please be as detailed as you can, and explain in a way any beginner can understand, and here is the price list: {bitcoinPrices}"""
# print(basicGeneration(prompt1))
print(BasicGeneration(chatGPTPrompt))


