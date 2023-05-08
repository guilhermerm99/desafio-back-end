import requests
from googletrans import Translator
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base

URL_PRODUTOS = "https://dummyjson.com/products"
URL_CHUCK_NORRIS = "https://api.chucknorris.io/jokes/random"

Base = declarative_base()


class Produto(Base):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    category = Column(String)
    price = Column(Float)


def fazer_requisicao(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {str(e)}")
        return None


def calcular_media_smartphones(data):
    smartphones = [produto for produto in data['products'] if produto['category'] == 'smartphones']
    if smartphones:
        precos = [produto['price'] for produto in smartphones]
        media = sum(precos) / len(precos)
        print("## Resultado da coleta de dados ##")
        print(f"Preço médio dos smartphones: $ {media:.2f}")
    else:
        print("Nenhum smartphone encontrado.")


def salvar_produtos(produtos):
    try:
        engine = create_engine('sqlite:///produtos.db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        for produto in produtos:
            novo_produto = Produto(title=produto['title'], category=produto['category'], price=produto['price'])
            session.add(novo_produto)

        session.commit()
        session.close()
    except Exception as e:
        print(f"Erro ao salvar os produtos no banco de dados: {str(e)}")


def obter_piada_chuck_norris():
    data = fazer_requisicao(URL_CHUCK_NORRIS)
    if data:
        return data.get('value')
    else:
        return None


def traduzir_texto(texto):
    trans = Translator()
    return trans.translate(texto, dest='pt').text


def main():
    data = fazer_requisicao(URL_PRODUTOS)
    if data:
        calcular_media_smartphones(data)
        salvar_produtos(data['products'])
        piada = obter_piada_chuck_norris()
        if piada:
            print("Piada sobre Chuck Norris:")
            piada_traduzida = traduzir_texto(piada)
            print(piada_traduzida)
        else:
            print("Não foi possível obter uma piada sobre Chuck Norris.")


if __name__ == "__main__":
    main()
