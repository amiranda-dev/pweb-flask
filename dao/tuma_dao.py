from dao.db_config import get_connection

class TurmaDAO:

    sqlSelect = ''' SELECT matricula.id, aluno.nome, curso.nome_curso, turma.semestre
                    FROM matricula
                    JOIN aluno ON aluno.id = matricula.aluno_id
                    JOIN curso ON curso.id = matricula.curso_id
                    JOIN turma ON turma.id = matricula.turma_id;
                '''

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista