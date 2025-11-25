from dao.db_config import get_connection

class MatriculaDAO:
    
    sqlSelect = '''
        SELECT 
            m.id, 
            t.semestre, 
            a.nome, 
            c.nome_curso, 
            p.nome, 
            p.disciplina
        FROM matricula m
        LEFT JOIN aluno a ON m.aluno_id = a.id
        LEFT JOIN turma t ON m.turma_id = t.id
        LEFT JOIN curso c ON t.curso_id = c.id
        LEFT JOIN professor p ON t.professor_id = p.id
        ORDER BY m.id DESC
    '''

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista

    def salvar(self, id, aluno_id, turma_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT curso_id FROM turma WHERE id = %s", (turma_id,))
            resultado_turma = cursor.fetchone()
            curso_id = resultado_turma[0] if resultado_turma else None

            if id:
                cursor.execute('''
                    UPDATE matricula 
                    SET aluno_id=%s, turma_id=%s, curso_id=%s 
                    WHERE id=%s
                ''', (aluno_id, turma_id, curso_id, id))
            else:
                cursor.execute('''
                    INSERT INTO matricula (aluno_id, turma_id, curso_id) 
                    VALUES (%s, %s, %s)
                ''', (aluno_id, turma_id, curso_id))
            
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            conn.rollback()
            return {"status": "erro", "mensagem": str(e)}
        finally:
            conn.close()

    def buscar_por_id(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, aluno_id, turma_id FROM matricula WHERE id = %s', (id,))
        registro = cursor.fetchone()
        conn.close()
        return registro

    def remover(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM matricula WHERE id = %s', (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": str(e)}
        finally:
            conn.close()