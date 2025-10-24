from dao.db_config import get_connection

class CursoDAO:

    sqlSelect = ''' SELECT curso.id, curso.nome_curso, turma.semestre, professor.nome AS professor
                    FROM curso
                    JOIN turma ON turma.curso_id = curso.id
                    JOIN professor ON professor.id = turma.professor_id;
                '''
    
    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista