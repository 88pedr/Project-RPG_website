from fastapi import FastAPI 
#este é o servido de minha aplicação onde pode ir rotas, configuração, 
# validações e documentações
app = FastAPI()

#Isto é um decorador, ele registra imediatamente a função abaixo como que deve 
# ser executado quando acessamor esta rota
#onde a rota que queremos acessar é a rota raiz / (home basicamente) www.x.com/
@app.get("/")
def caralho():
    return {"message": "caralho"}