import list_to_json as data
import firebase_admin

from firebase_admin import credentials
from firebase_admin import db 
 
print(data.korea_dict)

#Firebase database 인증 및 앱 초기화
cred = credentials.Certificate("./firebase_admin/aid-pbl-cd481-firebase-adminsdk-5l0u0-1f708ecd97.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : 'https://aid-pbl-cd481-default-rtdb.firebaseio.com/'
})

dir = db.reference('test') #기본 위치 지정
dir.update({'온도':'35'})
dir.update({'습도':'80'})

test = db.reference('test2')
test.update({'test':'123'})


