import tweepy
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Recupera as credenciais do Twitter das variáveis de ambiente
api_key = os.getenv("API_KEY")
api_key_secret = os.getenv("API_KEY_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Autenticação
auth = tweepy.OAuthHandler(access_token, access_token_secret)
auth.set_access_token(api_key, api_key_secret)

# Criação de uma instância da API do Twitter
api = tweepy.API(auth)

# Defina os parâmetros da busca
palavra_chave = "openai"
quantidade_tweets = 10

# Realiza a busca
tweets = tweepy.Cursor(api.search, q=palavra_chave).items(quantidade_tweets)

# Itera pelos tweets encontrados
for tweet in tweets:
    print(tweet.text)
    print("----")
