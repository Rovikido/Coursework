import eel
from DB import *
import json

kon = DataBase()
eel.init('GUI')


@eel.expose
def fetch_all_data(include_row, include_data, order_by):
    join_str = f'LEFT JOIN {STUDENT_TABLE} ON {COURSEWORK_STUDENT_ID}={STUDENT_ID} '
    join_str += f'LEFT JOIN {ADVISOR_TABLE} ON {COURSEWORK_ADVISOR_ID}={ADVISOR_ID} '
    kon_request = kon.request_data(show_fields=[], order_by=order_by, order_desc=False,
                                   from_tables=COURSEWORK_TABLE, join=join_str,
                                   conditions=({include_row: include_data} if include_row != "" else {}))
    res = json.dumps(kon_request, indent=2)
    eel.update_table(res)


@eel.expose
def get_advisor_dict():
    kon_request = kon.request_data(show_fields=[ADVISOR_ID, ADVISOR_INITIALS], order_by=ADVISOR_INITIALS, order_desc=False, from_tables=ADVISOR_TABLE)
    kon_request = dict(zip([item['advisor_id'] for item in kon_request], [item['advisor_initials'] for item in kon_request]))
    eel.populate_advisor_dict(json.dumps(kon_request, indent=2))


@eel.expose
def get_student_dict():
    kon_request = kon.request_data(show_fields=[STUDENT_ID, STUDENT_INITIALS], order_by=STUDENT_INITIALS, order_desc=False, from_tables=STUDENT_TABLE)
    kon_request = dict(zip([item['student_id'] for item in kon_request], [item['student_initials'] for item in kon_request]))
    eel.populate_student_dict(json.dumps(kon_request, indent=2))


@eel.expose
def add_coursework(json_data):
    data = json.loads(json_data)
    kon.insert_data(COURSEWORK_TABLE, data)
    fetch_all_data('','','student.student_initials')


@eel.expose
def delete_coursework(json_data):
    data = json.loads(json_data)
    kon.delete_data(COURSEWORK_TABLE, data)
    fetch_all_data('','','student.student_initials')
