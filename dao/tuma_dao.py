from dao.db_config import get_connection

class TurmaDAO:

    sqlSelect = '''
        SELECT turma.id, turma.semestre, curso.nome_curso, professor.nome
        FROM turma
        JOIN curso ON curso.id = turma.curso_id
        JOIN professor ON professor.id = turma.professor_id
    '''

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista