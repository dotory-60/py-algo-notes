import pymysql

from pymysql.cursors import Cursor

def show_menu() -> str:
    print("1. 일정 추가")  # insert
    print("2. 일정 보기")  # select
    print("3. 일정 완료")  # update
    print("4. 종료")
    return get_user_choice()

def get_user_choice() -> str:
    return input("선택: ")

def get_db_connection() -> pymysql.Connection:
    try:
        return pymysql.connect(host="localhost", port=3307, user="root", password='1234', database='schedule_db')
    except Exception as e:
        print(f"데이터베이스 연결 실패: {e}")
        exit(1)

# 일정 추가
def add_schedule(cursor: Cursor):
    title = input("제목 : ")
    description = input("내용 : ")
    start_datetiem = input("시작 날짜(yyyymmddhhmmss) : ")
    end_datetiem = input("종료 날짜(yyyymmddhhmmss) : ")

    sql = "INSERT INTO schedules (title, description, start_datetime, end_datetime) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (title, description, start_datetiem, end_datetiem))

def get_schedules(cursor: Cursor):

    # cursor.execute('SELECT * FROM schedules')
    # schedules = cursor.fetchall()
    # for schedule in schedules:
    #     print(schedule)

    sql = "SELECT id, title, description, start_datetime, end_datetime, is_completed FROM schedules"

    cursor.execute(sql)
    schedules = cursor.fetchall()
    if not schedules:
        print("등록된 일정이 없습니다.")
        return

    for schedule in schedules:
        id, title, description, start_datetime, end_datetime, is_complete = schedule
        status = "완료" if is_complete else "미완료"

        print(f"[{id}] {title}")
        print(f"   상태: {status}")
        print(f"   시간: {start_datetime}")
        print(f"   종료: {end_datetime}")
        if description:
            print(f"   설명: {description}")
        print()

def complete_schedule(cursor: Cursor):
    id = int(input("ID 값을 입력해주세요 :"))

    sql = "UPDATE schedules SET is_completed = %s WHERE id = %s"
    cursor.execute(sql, (True, id))

    print(f"{id}번 일정이 완료되었습니다.")

    # affected_rows_count = cursor.execute(sql, id)
    # if affected_rows_count == 0:
    #     print("존재하지 않는 일정 id입니다.")
    # else:
    #     print(f"{id} 일정이 완료되었습니다.")

def main():
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        while True:
            choice = show_menu()
            if choice == "1":
                add_schedule(cursor)
                conn.commit()
            elif choice == "2":
                get_schedules(cursor)
            elif choice == "3":
                complete_schedule(cursor)
                conn.commit()
            elif choice == "4":
                print("종료합니다.")
                break
            else:
                print("다시 선택해주세요")

    except Exception as e:
        print(f"프로그램 실행 중 오류 발생: {e}")

    finally:
        cursor.close()
        conn.close()

if __name__ == '__main__':
    main()