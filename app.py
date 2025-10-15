from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    musica = {
        "titulo": "Asa Branca",
        "compositores": "Luiz Gonzaga e Humberto Teixeira",
        "ano": 1947,
        "genero": "Forró / Baião",
        "contexto": """A música fala sobre o Nordeste brasileiro e a migração causada pela seca. 
O personagem precisa deixar sua terra natal porque a seca destruiu a plantação, 
mostrando a realidade do sertanejo. 'Asa Branca' se refere a uma pomba que simboliza esperança e retorno.""",
        "relacao_materias": {
            "Geografia": "Estuda clima, relevo, recursos naturais e migração interna no Nordeste.",
            "História": "Mostra o modo de vida e dificuldades do sertanejo no século XX e questões socioeconômicas.",
            "Literatura e Cultura": "Analisa poesia popular, rimas e regionalismo na música brasileira."
        }
    }
    return render_template("musica.html", musica=musica)

if __name__ == '__main__':
    app.run()
