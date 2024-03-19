import requests

API_KEY = "AIzaSyACDgDdRuyt9r6vSU_KxHeSzWuyUofVUZ0"

url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + API_KEY

headers = {
    "Content-Type": "application/json"
}


result = f''' 
Ты помощник врача-диагноста, твоя задача, быть ему полезным и с точность до 90% при имеющемся анамнезе предсказывать наиближайший диагноз, 
далее я буду давать тебе вводную информацию, по которой ты сделаешь определенные выводы, имеется Пациент, он прошел тест 
и ты делаешь результаты на основании его ответов, помоги врачу и составь рекомендацию и диагноз в формате текста, чтобы это было максимально профессионально, и уложись в 100 слов,
ниже информация предоставленная пациентом: 
{checkupResult}
'''

data = {
    "contents": [{
        "parts":[{
            "text": result
        }]
    }]
}

response = requests.post(url, headers=headers, json=data)

print(response.json())
