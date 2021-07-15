from django.shortcuts import render

# Create your views here.
import sqlite3
def list(request):
    result = dict()
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row  # for getting columns
    curs = conn.cursor()

    # economics
    curs.execute('select * from polls_economics pe')
    data = curs.fetchall() # 커서에서 값을 모두 뽑아내서 뱉어내는 작업
    for row in data:
        print(row['title'],' : ', row['href'])
    result['erows'] = data

    # user
    curs.execute('select * from auth_user au')
    result['members'] = curs.fetchall()
    for row in result['members']:
        print(row['username'], ', ', row['email'])
    return render(request, 'board/list.html', result)
