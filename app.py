<<<<<<< HEAD
from flask import Flask, render_template , request, redirect, flash
=======
from flask import Flask, render_template , request
>>>>>>> 70f4be88010779fb5bbb05e41146c3575fc2d540
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.curso_dao import CursoDAO
from dao.turma_dao import TurmaDAO
from dao.matricula_dao import MatriculaDAO

app = Flask(__name__)
app.secret_key = "Uma_chave_não_muito_confiável"



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/aluno')
def listar_aluno():
    dao = AlunoDAO()
    lista = dao.listar()
    return render_template('aluno/listar.html', lista=lista)
<<<<<<< HEAD

@app.route('/aluno/form') 
def form_aluno():
    return render_template('/aluno/form.html', aluno=None)

@app.route('/aluno/salvar/', methods=['POST'])  # Inserção
@app.route('/aluno/salvar/<int:id>', methods=['POST']) # Atualização
def salvar_aluno(id=None):
    nome = request.form['nome']
    idade = request.form['idade']
    cidade = request.form['cidade']
    dao = AlunoDAO()
    result = dao.salvar(id, nome, idade, cidade) 

    if result["status"] == "ok":
        flash("Regitro salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/aluno')

#Editar Aluno
@app.route('/aluno/editar/<int:id>')
def editar_aluno(id):
    dao = AlunoDAO()
    aluno = dao.buscar_por_id(id)
    return render_template('aluno/form.html', aluno=aluno)

#Remover Aluno
@app.route("/aluno/remover/<int:id>")
def remover_aluno(id):
    dao = AlunoDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
        flash("Registro removido com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/aluno')
=======
>>>>>>> 70f4be88010779fb5bbb05e41146c3575fc2d540

@app.route('/professor')
def listar_professor():
    dao = ProfessorDAO()
    lista = dao.listar()
    return render_template('professor/listar.html', lista=lista)
<<<<<<< HEAD

@app.route('/professor/form') 
def form_professor():
    professor_vazio = [0, "", ""]
    return render_template('professor/form.html', professor=professor_vazio)

@app.route('/professor/salvar/', methods=['POST']) 
@app.route('/professor/salvar/<int:id>', methods=['POST'])
def salvar_professor(id=None):
    id = request.form.get('id')
    if id == '0' or id == '':
        id = None
        
    nome = request.form['nome']
    disciplina = request.form['disciplina'] 
    
    dao = ProfessorDAO()
    result = dao.salvar(id, nome, disciplina) 

    if result["status"] == "ok":
        flash("Professor salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/professor')

#Editar Professor
@app.route('/professor/editar/<int:id>')
def editar_professor(id):
    dao = ProfessorDAO()
    professor = dao.buscar_por_id(id)
    return render_template('professor/form.html', professor=professor)
=======
>>>>>>> 70f4be88010779fb5bbb05e41146c3575fc2d540

#Remover Porfessor
@app.route("/professor/remover/<int:id>")
def remover_professor(id):
    dao = ProfessorDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
        flash("Registro removido com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/professor')

# Curso
@app.route('/curso')
def listar_curso():
    dao = CursoDAO()
    lista = dao.listar()
    return render_template('curso/listar.html', lista=lista)

<<<<<<< HEAD
# Formulário Novo Curso
@app.route('/curso/form') 
def form_curso():
    curso_vazio = [0, ""]
    return render_template('curso/form.html', curso=curso_vazio)

# Salvar Curso - Inserir ou Atualizar
@app.route('/curso/salvar/', methods=['POST']) 
@app.route('/curso/salvar/<int:id>', methods=['POST'])
def salvar_curso(id=None):
    nome_curso = request.form['nome_curso']
    
    dao = CursoDAO()
    result = dao.salvar(id, nome_curso) 

    if result["status"] == "ok":
        flash("Curso salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/curso')

#Editar Curso
@app.route('/curso/editar/<int:id>')
def editar_curso(id):
    dao = CursoDAO()
    curso = dao.buscar_por_id(id)
    return render_template('curso/form.html', curso=curso)

#Remover Curso
@app.route("/curso/remover/<int:id>")
def remover_curso(id):
    dao = CursoDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
        flash("Registro removido com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/curso')

# Saudação com parâmetro via URL e Query String
@app.route('/saudacao/<nome>')
def saudacao1(nome):
    return render_template('saudacao/saudacao.html', valor_recebido=nome)

# Saudação com parâmetro via Query String
=======
@app.route('/saudacao/<nome>')
def saudacao1(nome):
    #grava no banco de dados nome
    return render_template('saudacao/saudacao.html', valor_recebido=nome)

>>>>>>> 70f4be88010779fb5bbb05e41146c3575fc2d540
@app.route('/saudacao2/')
def saudacao2():
    nome = request.args.get('nome')
    return render_template('saudacao/saudacao.html', valor_recebido=nome)

<<<<<<< HEAD
# Saudação com parâmetros via Formulário (método POST)
=======
>>>>>>> 70f4be88010779fb5bbb05e41146c3575fc2d540
@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    email = request.form['email']
    senha = request.form['senha']
    dados = f"Usuário: {usuario}, Senha: {senha}, E-mail: {email}"
    return render_template('saudacao/saudacao.html', valor_recebido=dados)

<<<<<<< HEAD
# Cadastro com múltiplos campos via Formulário (método GET e POST)
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    dados = "" 
    
    if(request.method == 'POST'):
=======
@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    dados = "" # Crie a variável de dados vazia
    
    if(request.method == 'POST'):
        # --- CORREÇÃO 1: 'name' mudado para 'nome' ---
>>>>>>> 70f4be88010779fb5bbb05e41146c3575fc2d540
        nome = request.form['nome'] 
        data_nascimento = request.form['data_nascimento']
        cpf = request.form['cpf']
        nome_mae = request.form['nome_mae']
        
<<<<<<< HEAD
        dados = f"Cadastro Recebido: \n\n Nome: {nome}, \n Nasc: {data_nascimento}, \n CPF: {cpf}, \n Mãe: {nome_mae}"
        
        return render_template('cadastro/cadastro.html', valor_recebido=dados)

    return render_template('cadastro/cadastro.html', valor_recebido=dados) 


# Listar Turma
@app.route('/turma')
def listar_turma():
    dao = TurmaDAO()
    lista = dao.listar() 
    return render_template('turma/listar.html', lista=lista)

# Turma 
@app.route('/turma/form')
def form_turma():
  listar_professores = ProfessorDAO().listar()
  listar_cursos = CursoDAO().listar()
  return render_template('turma/form.html', 
    turma=None, 
    lista_professores=listar_professores, 
    lista_cursos=listar_cursos)         


#Salvar Turma 
@app.route('/turma/salvar/', methods=['POST']) 
@app.route('/turma/salvar/<int:id>', methods=['POST'])
def salvar_turma(id=None): 
    semestre = request.form['semestre']
    curso_id = request.form['curso_id']
    professor_id = request.form['professor_id']
    
    dao = TurmaDAO()
    result = dao.salvar(id, semestre, curso_id, professor_id) 

    if result["status"] == "ok":
        flash("Turma salva com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/turma')


# Turma Editar
@app.route('/turma/editar/<int:id>')
def editar_turmas(id):
  listar_professores = ProfessorDAO().listar() 
  listar_cursos = CursoDAO().listar()
  dao = TurmaDAO()
  turma = dao.buscar_por_id(id)
  return render_template('turma/form.html', 
    turma=turma, 
    lista_professores=listar_professores, 
    lista_cursos=listar_cursos)


# Turma Remover 
@app.route("/turma/remover/<int:id>")
def remover_turma(id):
    dao = TurmaDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
        flash("Registro removido com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/turma')

# Listar Matrículas
@app.route('/matricula')
def listar_matriculas():
    dao = MatriculaDAO()
    lista = dao.listar()
    return render_template('matricula/listar.html', lista=lista)

# Formulário Nova Matrícula
@app.route('/matricula/form')
def form_matricula():
    aluno_dao = AlunoDAO()
    turma_dao = TurmaDAO()
    
    # Busca dados para preencher os <select>
    alunos = aluno_dao.listar() # Assume que você tem esse método no AlunoDAO
    turmas = turma_dao.listar_para_select()
    
    return render_template('matricula/form.html', matricula=None, alunos=alunos, turmas=turmas)

# salvar matrícula
@app.route('/matricula/salvar', methods=['POST'])
@app.route('/matricula/salvar/<int:id>', methods=['POST'])
def salvar_matricula(id=None):
    if id is None:
        id = request.form.get('id')
        if not id: id = None

    aluno_id = request.form['aluno_id']
    turma_id = request.form['turma_id']
    
    # Nota: O curso_id será descoberto automaticamente pelo DAO
    dao = MatriculaDAO()
    dao.salvar(id, aluno_id, turma_id)
    
    return redirect('/matricula')

# editar matrícula
@app.route('/matricula/editar/<int:id>')
def editar_matricula(id):
    dao = MatriculaDAO()
    matricula = dao.buscar_por_id(id)
    
    aluno_dao = AlunoDAO()
    turma_dao = TurmaDAO()
    
    alunos = aluno_dao.listar()
    turmas = turma_dao.listar_para_select()
    
    return render_template('matricula/form.html', matricula=matricula, alunos=alunos, turmas=turmas)

# remover matrícula
@app.route('/matricula/remover/<int:id>')
def remover_matricula(id):
    dao = MatriculaDAO()
    dao.remover(id)
    return redirect('/matricula')
=======
        # Agora a variável 'nome' existe e pode ser usada aqui
        dados = f"Cadastro Recebido: \n\n Nome: {nome}, \n Nasc: {data_nascimento}, \n CPF: {cpf}, \n Mãe: {nome_mae}"
        
        # Envia os dados para a página de saudação ver o resultado
        # --- CORREÇÃO DE CAMINHO ---
        return render_template('cadastro/cadastro.html', valor_recebido=dados)

    # --- CORREÇÃO 2: Adicionado o 'return' para o método GET ---
    # Se o método não for POST, significa que é GET.
    # Então, apenas mostre a página com o formulário de cadastro.
    # --- CORREÇÃO DE CAMINHO ---
    return render_template('cadastro/cadastro.html', valor_recebido=dados) # Passa 'dados' vazios
>>>>>>> 70f4be88010779fb5bbb05e41146c3575fc2d540

if __name__ == '__main__':
    app.run(debug=True)