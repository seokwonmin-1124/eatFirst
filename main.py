# start 2024 04 19
# end 2024 00 00
# made by LESH
# 누군가 나중에 유지보수 할 수도 있으니까(과연..) 주석을 좀 달아봤다.

import datetime
import sqlite3
import qrcode
from PIL import Image

now = datetime.datetime.now()
nowDate = now.strftime('%Y%m%d')

def dbSetting(): # 데이터베이스 초기 세팅(테이블 생성)
    conn = sqlite3.connect('wsdb.db')
    cur = conn.cursor()

    cur.execute("""CREATE TABLE IF NOT EXISTS woosun(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        schNum TEXT,
        name TEXT,
        reason TEXT,
        Tel TEXT,
        date TEXT
        )""")
    conn.commit()

    conn.close()
    return print('DB setting is Done')

# dbSetting()

def addOnDb(schNum, name, reason, Tel): # 우선급식증 학생 정보 추가(우선급식증 qr 생성 자료를 db에 저장)
    conn = sqlite3.connect('wsdb.db')
    cur = conn.cursor()

    dataList = list(tuple())
    dataList.append((str(schNum), name, reason, str(Tel), str(nowDate)))

    cur.executemany('INSERT INTO woosun (schNum, name, reason, Tel, date) VALUES (?, ?, ?, ?, ?)', dataList)
    conn.commit()

    conn.close()

    return print(f'{dataList} is added on database')

def checkTimeQrAv(): # 현재 시간이 우선급식증(qr)을 사용할 수 있는 시간인지 체크
    qrAvTimeSt = datetime.datetime(now.year, now.month, now.day, 12, 30) # qr available time star
    qrAvTimeEd = datetime.datetime(now.year, now.month, now.day, 13, 30)

    if qrAvTimeSt <= now <= qrAvTimeEd:
        return(True)
    else:
        return(False)

def searchDb(type, value=None): # db 값 조회 type: 조회할 타입(all이면 전체 값 출력), value: 타입 내에서 검색할 값 | ex) type: Tel, value: 01099998888
    conn = sqlite3.connect("wsdb.db")

    cur = conn.cursor()
    noValue = None
    haveValue = None

    if type == 'all': # 전체 데이터 조회
        cur.execute("SELECT * FROM woosun")
        noValue = cur.fetchall()
    elif type == 'id': # id(자동증가값)
        value = int(value)
        cur.execute("SELECT * FROM woosun WHERE id=?", (value,))
        haveValue = cur.fetchall()
    elif type == 'last': # 마지막(제일 최근) 데이터 조회
        cur.execute("SELECT * FROM woosun ORDER BY ROWID DESC LIMIT 1;")
        haveValue = cur.fetchone()
    else:
        query = f"SELECT * FROM woosun WHERE {type}=?"
        cur.execute(query, (value,))
        haveValue = cur.fetchall()

    conn.close()

    if noValue == None:
        return haveValue
    else:
        return noValue

def createQr(stdInfo): #qr코드 생성
    stdInfo = list(stdInfo)
    stdInfo.remove(stdInfo[4]) # 전화번호 삭제

    img = 'bulgokLogo.png'

    img = Image.open(img)
    img.thumbnail((90, 90))

    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(stdInfo)
    qr.make()

    qrInfo = qr.make_image().convert('RGB')
    pos = ((qrInfo.size[0]-img.size[0])// 2, (qrInfo.size[1]-img.size[1])//2)
    qrInfo.paste(img, pos)

    qrInfo.save(f'./Qr/{stdInfo}.png')

    return True

# createQr(searchDb('last')) #qr생성


# qr 스캔은 급식지도쌤 -> 그냥 단일 js/html 페이지로 만들기
# qr flask로 웹에 올리고(localhost:5001/암호화된주소) Ngrok으로 외부접속 가능하게 하면 끝
# qr은 메시지로 학생한테 전송(flask로 웹에 올린 링크)
# 링크에서 checkTimeQrAv함수로 유효기간 설정 -> 캡쳐하면 끝나지 않나.. 싶지만 flask에서 한번, 급식지도쌤 단일페이지에서 두번 거르기 때문에(날짜/시간) 악용할 방법은 없다(아마..?)


# dbSetting()