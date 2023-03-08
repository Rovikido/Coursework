from DB import *
from GUI_connector import *


if __name__ == '__main__':
    eel.start('index.html')
    # kon = DataBase()
    # kon_request = kon.request_data(conditions={}, order_by=STUDENT_FACULTY, from_tables=STUDENT_TABLE)
    # print(kon.cursor_execute("SELECT * FROM coursework  LEFT JOIN student ON coursework.student_id=student.student_id LEFT JOIN advisor ON coursework.advisor_id=advisor.advisor_id   ORDER BY student.student_initials DESC ;"))
    # # print(json.dumps(kon_request, indent=2))
    # # kon.insert_data(STUDENT_TABLE, {STUDENT_INITIALS: "Головацька Ольга Глібівна", STUDENT_COURSE: "2", STUDENT_GROUP: "ФЕС-22", STUDENT_FACULTY: FACULTY_ELECTRONIC})
    # # kon.delete_data(STUDENT_TABLE, {STUDENT_INITIALS: "Індик Дорогомисл Тарасович"})
    # # kon.delete_data(COURSEWORK_TABLE, conditions={WORK_ID: 1, THEME: "YES"})
    # # kon.cursor_execute("DELETE FROM student;", False)

