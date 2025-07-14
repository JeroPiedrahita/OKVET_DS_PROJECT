import re
import string

#Funcios de normalizacion de textos y limpieza
def clean_text(text):
  #Convertir a minusculas
  text = str(text).lower()

  #Eliminar textos entre corchetes (ej. :etiquetas)
  text = re.sub(r'\[.*?\]','', text)

  #Eliminar URLs
  text = re.sub(r'https?://\S+|WWW\. \S+', '', text)

  #Eliminar etiqetas HTML
  text = re.sub(r'<.*?>+', '', text)

  #Eliminar signos de puntuacion
  text =re.sub('[%s]' % re.escape(string.punctuation),'', text)

  #Eliminar saltos de linea
  text = re.sub(r'\n', ' ', text)

  #Eliminacion de palabras que contienen numeros
  text = re.sub(r'\w*\d\w*', '', text)

  #Eliminar emojis y caracteres especiales (no ASCII)
  text = re.sub(r'[^\x00-\x7F]+', '', text)

  #Eliminar espacios extras al inicio y final
  text = text.strip()

  return text