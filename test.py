#
#
# 테스트 기록은 삭제하지 말고 유지하자.
#
#



# a, b = str(1), str(2)
# print(a)

# def a(aa=None):
#     if aa ==  None:
#       print(type(aa))
#       return True

# a()

# import sqlite3

# def searchDb(type, value=None): # db 값 조회 type: 조회할 타입(all이면 전체 값 출력), value: 타입 내에서 검색할 값
#     conn = sqlite3.connect("wsdb.db")

#     cur = conn.cursor()
#     noValue = None
#     haveValue = None

#     if type == 'all':
#         cur.execute("SELECT * FROM woosun")
#         noValue = cur.fetchall()
#     else:
#         query = f"SELECT * FROM woosun WHERE {type}=?"
#         cur.execute(query, (value,))
#         haveValue = cur.fetchall()

#     conn.close()

#     if noValue == None:
#         return haveValue
#     else:
#         return noValue

# # print(searchDb("all"))
# print(searchDb("schNum", "20612"))

#qr생성해야함

# import main
# import qrcode
# from PIL import Image

# def createQr(stdInfo):
#     stdInfo = list(stdInfo)
#     stdInfo.remove(stdInfo[4])

#     img = 'bulgokLogo.png'

#     img = Image.open(img)
#     img.thumbnail((90, 90))

#     qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
#     qr.add_data(stdInfo)
#     qr.make()

#     qrInfo = qr.make_image().convert('RGB')
#     pos = ((qrInfo.size[0]-img.size[0])// 2, (qrInfo.size[1]-img.size[1])//2)
#     qrInfo.paste(img, pos)

#     qrInfo.save(f'./Qr/{stdInfo}.png')

#     return True

# createQr(main.searchDb('last'))

#웹에서 qr 스캔(js)