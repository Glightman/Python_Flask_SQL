from flask import Flask, Blueprint, render_template

app = Flask(__name__)
bp = Blueprint('app', __name__)

filmes = [
    {
        'id': 1,
        'nome': 'Home Aranha: Longe de casa',
        'url': 'https://upload.wikimedia.org/wikipedia/pt/0/04/Spider-man-far-from-home-poster.jpg'
    },
    {
        'id': 2,
        'nome': 'Vingadores: Guerra Infinita',
        'url': 'https://lumiere-a.akamaihd.net/v1/images/unnamed_10_2a3389cf.jpeg?region=0%2C0%2C356%2C512'
    },
    {
        'id': 3,
        'nome': 'Capitão América 2: O Soldado Ivernal',
        'url': 'https://upload.wikimedia.org/wikipedia/pt/e/e8/Captain_America_The_Winter_Soldier.jpg'
    },
    {
        'id': 4,
        'nome': 'Pantera Negra',
        'url': 'https://www.geeknewsnow.net/wp-content/uploads/2020/11/black-panther-2018-movie-poster.jpg'
    },
    {
        'id': 5,
        'nome': 'Guardiões da Galáxia: Vol.2',
        'url': 'https://karga.pt/wp-content/uploads/2017/08/GuardioesGlaxiaVideoclube.png'
    },
    {
        'id': 6,
        'nome': 'Doutor Estranho',
        'url': 'https://i.pinimg.com/originals/5a/bb/1e/5abb1e4e1272f88e62f9a206c4314e91.jpg'
    }
]

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/read')
def listar_filmes():
    return render_template('listar-filmes.html', listaDeFilmes = filmes)

@bp.route('/read/<filme_id>')
def lista_detalhe_filme(filme_id):
    return 'Pagina filme -->' + filme_id

app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True)