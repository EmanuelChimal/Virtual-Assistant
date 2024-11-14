import nltk
import requests
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Descargar recursos necesarios
nltk.download('punkt')
nltk.download('stopwords')

def handle_common_questions(question):
    responses = {
        "¿cómo estás?": "¡Estoy bien, gracias por preguntar! ¿En qué puedo ayudarte hoy?",
        "¿qué puedes hacer?": "Puedo responder preguntas comunes, proporcionarte el clima, o realizar cálculos simples.",
        # Agrega más preguntas/respuestas aquí.
    }
    return responses.get(question.lower(), "Lo siento, no tengo una respuesta para eso.")



def get_weather(city):
    api_key = 'aea42fe6022b3e9064b8e3cc9542eb25'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        return f"El clima en {city} es {weather} con una temperatura de {temp}°C."
    else:
        return "No se pudo obtener la información del clima. Verifica la ciudad."
