import mysql.connector


class DataBase:
    def __init__(self):
        self.connector = mysql.connector.connect(host="localhost", user='kurs_user',
                                                 password="qwerty12", database='kurs_db')

    def cursor_execute(self, prompt: str, return_data=True):
        cursor = self.connector.cursor(dictionary=True)
        cursor.execute(prompt)
        if not return_data:
            self.connector.commit()
            return
        res = cursor.fetchall()
        cursor.close()
        return res

    def __gen_where_prompt(self, conditions={}):
        where_prompt = ''
        i = 0
        for key, value in conditions.items():
            fv = f'\"{value}\"' if isinstance(value, str) else value
            where_prompt += f' {"" if i == 0 else "AND"} {key} = {fv} '
            i += 1
        return where_prompt

    def __gen_order_prompt(self, order_by=None, order_desc=True):
        return f' ORDER BY {order_by} {"DESC" if order_desc else "ASC"} '

    def __create_request_prompt(self, show_fields, conditions, order_by, order_desc, from_tables, join):
        request_prompt = 'SELECT '

        # fields to include in table
        request_prompt += ', '.join(show_fields) if len(show_fields) > 0 else '*'
        request_prompt += f' FROM {from_tables} ' if isinstance(from_tables, str) else f' FROM {", ".join(from_tables)} '

        # prompt to add conditions
        request_prompt += f' {join} '
        request_prompt += f'WHERE{self.__gen_where_prompt(conditions)}' if len(conditions) > 0 else ''
        # prompt to add ordering by field
        request_prompt += self.__gen_order_prompt(order_by, order_desc)

        request_prompt += ";"
        return request_prompt

    def request_data(self, show_fields=[], conditions={}, order_by=None, order_desc=True, from_tables=["coursework", "student", "advisor"], join=""):
        """Generates request for database
        Args:
            show_fields: list of fields to output
            conditions: dictionary of conditions
            order_by: field to order by
            order_desc: order in descending
        """
        prompt = self.__create_request_prompt(show_fields, conditions, order_by, order_desc, from_tables, join)
        print(prompt)
        return self.cursor_execute(prompt)

    def insert_data(self, table, data={}):
        prompt = f'INSERT INTO {table} '
        prompt += f'({", ".join(data.keys())}) values ('

        values = list(data.values())
        for i in range(len(values)):
            prompt += f'\"{values[i]}\"' if isinstance(values[i], str) else f'{values[i]}'
            prompt += ", " if len(values) > i+1 else ");"
        print(prompt)
        self.cursor_execute(prompt, False)

    def delete_data(self, table, conditions={}):
        prompt = f'DELETE FROM {table} '
        prompt += f'WHERE{self.__gen_where_prompt(conditions)};'

        print(prompt)
        self.cursor_execute(prompt, False)

