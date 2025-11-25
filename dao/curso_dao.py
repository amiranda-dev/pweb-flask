from dao.db_config import get_connection 


class CursoDAO: 

<<<<<<< HEAD
    sqlSelect = 'SELECT id, nome_curso FROM curso ORDER BY id DESC'
=======
    sqlSelect = 'SELECT c.id, c.nome_curso, p.disciplina, p.nome FROM turma t JOIN curso c ON t.curso_id = c.id JOIN professor p ON t.professor_id = p.id'
>>>>>>> 70f4be88010779fb5bbb05e41146c3575fc2d540


    def listar(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(self.sqlSelect)
        lista = cursor.fetchall()
        conn.close()
<<<<<<< HEAD
        return lista
    
     
    def salvar(self, id, nome_curso):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if id:
                cursor.execute('UPDATE curso SET nome_curso = %s WHERE id = %s', (nome_curso, id))
            else:
                cursor.execute('INSERT INTO curso (nome_curso) VALUES (%s)', (nome_curso,))
            
            conn.commit() 
            return {"status": "ok"}
        except Exception as e:
            conn.rollback() 
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()

    def buscar_por_id(self,id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, nome_curso FROM curso WHERE id = %s', (id,))        
        registro = cursor.fetchone() # retorna o registro selecionado
        conn.close()
        return registro
    
    def remover(self,id):
        conn = get_connection()
        cursor = conn.cursor()
        try: 
            cursor.execute('DELETE FROM curso WHERE id = %s', (id,))
            conn.commit()
            return {"status": "ok"}
        except Exception as e:
            return {"status": "erro", "mensagem": f"Erro: {str(e)}"}
        finally:
            conn.close()
=======
        return lista
>>>>>>> 70f4be88010779fb5bbb05e41146c3575fc2d540
