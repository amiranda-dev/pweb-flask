from dao.db_config import get_connection

class MatriculaDAO:

    sqlSelect = ''' SELECT m.id AS matricula_id, a.nome AS aluno, c.nome_curso AS curso, t.semestre AS turma
                    FROM matricula m
                    JOIN aluno a ON a.id = m.aluno_id
                    JOIN curso c ON c.id = m.curso_id
                    JOIN turma t ON t.id = m.turma_id;
                '''

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista