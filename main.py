import nltk
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
