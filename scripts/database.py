import sqlite3

class Aplication_database():

    def insert_user(self,user_name,user_email,user_phone,user_date,user_login,user_password):
        try:
            self.connect = sqlite3.connect("../static/database/users.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER NOT NULL PRIMARY KEY, Nome TEXT,Email TEXT, Telefone TEXT,\
                Nascimento DATE, Usuario TEXT, Senha TEXT)")
            self.cursor.execute("INSERT INTO users (Nome,Email,Telefone,Nascimento,Usuario,Senha) VALUES (?,?,?,?,?,?)",\
                (user_name,user_email,user_phone,user_date,user_login,user_password,))
            self.connect.commit()
            self.connect.close()
            sucess = "Login criado com sucesso!"
            return sucess
        except Exception as error:
            print(error)
            invalid = "Algum erro inesperado aconteceu, tente novamente."
            return invalid

    def select_user(self,user):
        try:
            self.connect = sqlite3.connect("../static/database/users.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT Usuario, Senha FROM users WHERE Usuario =?",(user,))
            self.my_user = self.cursor.fetchone()
            self.connect.close()
            return self.my_user
        except Exception as error:
            print(error)

    def create_tables(self):
        self.connect = sqlite3.connect("../static/database/system.db")
        self.cursor = self.connect.cursor()
        #CRIA A TABELAS SALES (VENDAS)
        self.cursor.execute("CREATE TABLE IF NOT EXISTS sales (id INTEGER NOT NULL PRIMARY KEY, Data DATE, Mesa TEXT, Produtos TEXT, Observacoes TEXT,\
                                    Endereco TEXT, Numero NUMBER, Bairro TEXT, Complemento TEXT, Total NUMBER, Condicao TEXT)")
        #CRIA A TABELA PRODUCTS(PRODUTOS)
        self.cursor.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER NOT NULL PRIMARY KEY, Nome TEXT, Marca TEXT, Quantidade NUMBER, Valor NUMBER,\
                            Categoria TEXT, Descricao TEXT)")
        #CRIA A TABELA CASHIER (CAIXA)
        self.cursor.execute("CREATE TABLE IF NOT EXISTS cashier (id INTEGER NOT NULL PRIMARY KEY, Instrucao TEXT, Data DATE, ValorA NUMBER, ValorF NUMBER)")

        self.connect.close()

    def register_new_product(self,new_name, new_marca, new_qtd, new_valor, new_categ, new_description):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("INSERT INTO products (Nome,Marca,Quantidade,Valor,Categoria,Descricao) VALUES (?,?,?,?,?,?)",\
                                (new_name, new_marca, new_qtd, new_valor, new_categ, new_description,))
            self.connect.commit()
            self.connect.close()
            self.register_sucess = "Registrado com sucesso"
            return self.register_sucess
        except Exception as error:
            self.register_failed = "Erro ao registrar!"
            print(error)
            return self.register_failed

    def edit_product_base(self, get_name, get_marca, get_qtd, get_valor, get_categ, get_description, get_search_name):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("UPDATE products SET Nome = ?, Marca = ?, Quantidade = ?, Valor = ?, Categoria = ?, Descricao = ? WHERE Nome = ?",\
                                        (get_name, get_marca, get_qtd, get_valor, get_categ, get_description, get_search_name,))
            self.connect.commit()
            self.connect.close()
            self.saved_sucess = "Update realizado com sucesso!"
            return self.saved_sucess
        except Exception as error:
            print(error)
            self.saved_failed = "Erro ao fazer o update!"
            return self.saved_failed

    def delete_product_base(self, name):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("DELETE FROM products WHERE Nome = ?",(name,))
            self.connect.commit()
            self.delete_ok = "Produto deletado com sucesso!"
            return self.delete_ok
        except Exception as error:
            print(error)
            self.delete_failed = "Erro ao deletar o produto!"
            return self.delete_failed

    def product_used(self, product):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT Quantidade FROM products WHERE Nome = ?",(product,))
            self.qtd_prod = self.cursor.fetchone()
            self.qtd_prod_total = 0
            for valor in self.qtd_prod:
                self.qtd_prod_total = valor
            self.qtd_prod_total -= 1
            self.cursor.execute("UPDATE  products SET Quantidade = ? WHERE Nome = ?",(self.qtd_prod_total, product,))
            self.connect.commit()
            self.connect.close
        except Exception as error:
            print(error)


    def select_product_edit(self, search_name):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT * FROM products WHERE Nome = ?", (search_name,))
            self.select_product_name = self.cursor.fetchall()
            self.connect.close()
            return self.select_product_name
        except Exception as error:
            print(error)
            self.error_select = "Erro ao selecionar"
            return self.error_select

    def select_product_category(self, category):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT * FROM products WHERE Categoria = ?", (category,))
            self.select_product_category = self.cursor.fetchall()
            self.connect.close()
            return self.select_product_category
        except Exception as error:
            print(error)
            self.error_select = "Erro ao selecionar"
            return self.error_select

    def select_all_products_name(self):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT Nome FROM products")
            self.all_products = self.cursor.fetchall()
            self.connect.close()
            return self.all_products
        except Exception as error:
            print(error)

    def select_product_valor(self,Nome):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT Valor FROM products WHERE Nome=?",(Nome,))
            self.product_valor = self.cursor.fetchone()
            self.connect.close()
            return self.product_valor
        except Exception as error:
            print(error)

    def select_all_products(self):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT * FROM products")
            self.all_products = self.cursor.fetchall()
            self.connect.close()
            return self.all_products
        except Exception as error:
            print(error)
            return error


    def sales_register(self, data, mesa, produtos, observacoes, endereco, numero, bairro, complemento, total, condicao):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            j = 0
            while j < len(produtos) - 1 :
                self.cursor.execute("INSERT INTO sales (Data, Mesa, Produtos, Observacoes, Endereco, Numero, Bairro, Complemento, Total, Condicao)\
                                    VALUES (?,?,?,?,?,?,?,?,?,?)", (data, mesa, produtos[j] ,observacoes, endereco, numero, bairro, complemento, 0, condicao,))
                j +=1
            str(total).replace(",",".")
            self.cursor.execute("INSERT INTO sales (Data, Mesa, Produtos, Observacoes, Endereco, Numero, Bairro, Complemento, Total, Condicao)\
                                VALUES (?,?,?,?,?,?,?,?,?,?)", (data, mesa, produtos[j] ,observacoes, endereco, numero, bairro, complemento, total, condicao,))
            self.connect.commit()
            self.connect.close()
        except Exception as error:
            print(error)

    def total_sales(self):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT id FROM sales")
            self.sales_total = self.cursor.fetchall()
            self.connect.close()
            return self.sales_total
        except Exception as error:
            print(error)
            return error
    def select_all_sales(self):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT * FROM sales")
            self.all_sales = self.cursor.fetchall()
            self.connect.close()
            return self.all_sales
        except Exception as error:
            print(error)
            return error
    def select_sales_all_day(self, data):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT * FROM sales WHERE Data = ?",(data,))
            self.sales_for_day = self.cursor.fetchall()
            return self.sales_for_day
        except Exception as error:
            print(error)
            return error

    def select_valor_all_sales(self):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT Total FROM sales")
            self.total_valor_sales = self.cursor.fetchall()
            return self.total_valor_sales
        except Exception as error:
            print(error)
            return error

    def select_valor_day_sales(self,data):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT Total FROM sales WHERE Data = ?", (data,))
            self.total_valor_sales_day = self.cursor.fetchall()
            return self.total_valor_sales_day
        except Exception as error:
            print(error)
            return error

    def select_open_sales(self,condition):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT * FROM sales WHERE Condicao = ?",(condition,))
            self.sales_for_condition = self.cursor.fetchall()
            return self.sales_for_condition
        except Exception as error:
            print(error)
            return error

    def select_valor_condition_sales(self,condition):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT Total FROM sales WHERE Condicao = ?", (condition,))
            self.total_valor_sales_day = self.cursor.fetchall()
            return self.total_valor_sales_day
        except Exception as error:
            print(error)
            return error

    def select_table_sales(self,table):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT * FROM sales WHERE Mesa = ?",(table,))
            self.sales_for_table = self.cursor.fetchall()
            return self.sales_for_table
        except Exception as error:
            print(error)
            return error

    def select_valor_table_sales(self,table):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT Total FROM sales WHERE Mesa = ?", (table,))
            self.total_valor_sales_table = self.cursor.fetchall()
            return self.total_valor_sales_table
        except Exception as error:
            print(error)
            return error


    def search_table_products(self,mesa):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT Produtos FROM sales WHERE Mesa = ? AND Condicao =?",(mesa,"ABERTO",))
            self.products_table = self.cursor.fetchall()
            self.cursor.execute("SELECT Observacoes FROM sales WHERE Mesa = ? AND Condicao =?",(mesa,"ABERTO",))
            self.obs_table = self.cursor.fetchall()
            self.cursor.execute("SELECT Total FROM sales WHERE Mesa = ? AND Condicao =?",(mesa,"ABERTO",))
            self.total_table = self.cursor.fetchall()
            self.connect.close()
            return self.products_table, self.obs_table, self.total_table
        except Exception as error:
            print(error)

    def open_cash_box(self,instruction, get_date, valor):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("INSERT INTO cashier (Instrucao, Data, ValorA) VALUES(?,?,?)",(instruction, get_date, valor,))
            self.connect.commit()
        except Exception as error:
            print(error)
    def search_cashier_open(self,data):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT Instrucao, ValorA FROM cashier WHERE Data = ? AND Instrucao =?",(data, "ABERTO",))
            self.open_cashier = self.cursor.fetchall()
            self.connect.close()
            return self.open_cashier

        except Exception as error:
            print(error)

    def profit(self,get_date):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("SELECT Total FROM sales WHERE Condicao =? AND Data = ?",("FECHADO", get_date,))
            self.total = self.cursor.fetchall()
            self.connect.close()
            return self.total
        except Exception as error:
            print(error)

    def close_cashier(self, get_inst, get_valor_final, get_date_final):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("UPDATE cashier SET Instrucao = ?, ValorF = ? WHERE Data = ?",(get_inst, get_valor_final, get_date_final,))
            self.connect.commit()
            self.connect.close()
            self.sucess_insert  = "FECHADO"
            return self.sucess_insert
        except Exception as error:
            print(error)
            self.error_close = "ERRO AO FECHAR"
            return self.error_close

    def close_table(self, condition, table):
        try:
            self.connect = sqlite3.connect("../static/database/system.db")
            self.cursor = self.connect.cursor()
            self.cursor.execute("UPDATE sales SET Condicao = ? WHERE Condicao = ? AND Mesa = ?",("FECHADO", condition, table))
            self.connect.commit()
            self.connect.close()
            self.close_table_sucess = "Mesa Fechada!"
            return self.close_table_sucess
        except Exception as error:
            print(error)

    def tables_opened(self):
        self.connect = sqlite3.connect("../static/database/system.db")
        self.cursor = self.connect.cursor()
        self.cursor.execute("SELECT Mesa FROM sales WHERE Condicao = ?",("ABERTO",))
        self.mesas = self.cursor.fetchall()
        return self.mesas
