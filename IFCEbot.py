import nltk
import numpy as np
import random
import string 
import warnings
warnings.filterwarnings("ignore")

#nltk.download('punkt')   # for first-time use only. Punkt is a Sentence Tokenizer
#nltk.download('wordnet')    # for first-time use only. WordNet is a large lexical database of English.

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from difflib import get_close_matches

# Abrir o arquivo de texto com as respostas padrão
f=open('chatbot.txt','r',errors = 'ignore', encoding = 'utf-8')

# Ler o arquivo e converter as palavras para lowercase
raw=f.read()
raw=raw.lower()

sent_tokens = nltk.sent_tokenize(raw)# converter para uma lista de sentenças
word_tokens = nltk.word_tokenize(raw)# converter para uma lista de palavras

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

GREETING_INPUTS = (
    "oi",
    "hey",
    "ola",
    "olá",
    "eae",
    "oie",
    "hi",
    "hello",
    "bom dia",
    "boa tarde",
    "boa noite"
)
GREETING_RESPONSES = [
    "Oi, humano! Posso ajudar?", 
    "Eae, bro! Posso ajudar?", 
    "Oi oi! Posso ajudar?", 
    "Opa, eae? Posso ajudar?", 
    "*Beep beep!* Posso ajudar?", 
    "Oie! *Beep beep* posso ajudar?"
]

THANKS_INPUTS = (
    "obrigado",
    "obrigada",
    "valeu",
    "vlw"
)
THANKS_RESPONSES = ["Disponha! Tem algo mais em que eu possa te ajudar? Digite <ajuda> se estiver com alguma dúvida"]

HELP_INPUTS = (
    "ajuda",
    "help",
    "temas"
)
HELP_RESPONSES = ["Eu posso responder suas perguntas em relação a:"+
"\ntrancamento, calendário acadêmico, jardineira, contatos do IFCE e dos professores,"+
" biblioteca, carteirinhas, coordenadores do curso, reingresso e reabertura de matrícula"]


def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
        elif word.lower() in THANKS_INPUTS:
            return random.choice(THANKS_RESPONSES)
        elif word.lower() in HELP_INPUTS:
            return random.choice(HELP_RESPONSES)

def response(user_response):
    robo_response=''
    #user_response = corretor(user_response)
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    
    if(req_tfidf==0):
        robo_response=robo_response+"Me desculpe, mas eu não entendi. Pode refazer sua pergunta?"
        sent_tokens.remove(user_response)
        return robo_response
    else:
        robo_response = robo_response+sent_tokens[idx]
        sent_tokens.remove(user_response)
        return robo_response