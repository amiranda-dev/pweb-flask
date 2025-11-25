from dao.db_config import get_connection

class TurmaDAO:
    
    sqlSelect = '''
        SELECT t.id, t.semestre, c.nome_curso, p.nome, p.disciplina 
        FROM turma t
        LEFT JOIN curso c ON t.curso_id = c.id
        LEFT JOIN professor p ON t.professor_id = p.id
        ORDER BY t.id DESC
    '''

    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
        return lista

    def listar_para_select(self):
        conn = get_connection()
        cursor = conn.cursor()
        sql = '''
            SELECT t.id, c.nome_curso, p.nome, t.semestre 
            FROM turma t
            LEFT JOIN curso c ON t.curso_id = c.id
            LEFT JOIN professor p ON t.professor_id = p.id
            ORDER BY t.semestre DESC
        '''
        cursor.execute(sql)
        lista = cursor.fetchall()
        conn.close()
        return lista

    def salvar(self, id, semestre, curso_id, professor_id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if id:
                cursor.execute('UPDATE turma SET semestre=%s, curso_id=%s, professor_id=%s WHERE id=%s', (semestre, curso_id, professor_id, id))
            else:
                cursor.execute('INSERT INTO turma (semestre, curso_id, professor_id) VALUES (%s, %s, %s)', (semestre, curso_id, professor_id))
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
        cursor.execute('SELECT id, semestre, curso_id, professor_id FROM turma WHERE id = %s', (id,))
        registro = cursor.fetchone()
        conn.close()
        return registro

    def remover(self, id):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('DELETE FROM turma WHERE id = %s', (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": str(e)}
        finally:
            conn.close()