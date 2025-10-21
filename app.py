from flask import Flask, render_template
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.tuma_dao import TurmaDAO
from dao.matricula_dao import MatriculaDAO
from dao.curso_dao import CursoDAO


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/aluno')
def listar_aluno():
    dao = AlunoDAO()
    lista = dao.listar()
    return render_template('aluno/lista.html', lista=lista)


@app.route('/professor')
def listar_professor():
    dao = ProfessorDAO()
    lista = dao.listar()
    return render_template('professor/lista.html', lista=lista)


@app.route('/turma')
def listar_turma():
    dao = TurmaDAO()
    lista = dao.listar()
    return render_template('turma/lista.html', lista=lista)


@app.route('/matricula')
def listar_matricula():
    dao = MatriculaDAO()
    lista = dao.listar()
    return render_template('matricula/lista.html', lista=lista)


@app.route('/curso')
def listar_curso():
    dao = CursoDAO()
    lista = dao.listar()
    return render_template('curso/lista.html', lista=lista)


if __name__ == '__main__':
    app.run(debug=True)
