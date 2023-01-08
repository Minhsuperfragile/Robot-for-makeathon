from firebase import Firebase
import json

config = {
  "apiKey": "AIzaSyAkqKQ-bqLIk_hNgJPwc8hwZBusbXYUpjs",
  "authDomain": "robottieptan.firebaseapp.com",
  "databaseURL": "https://robottieptan-default-rtdb.asia-southeast1.firebasedatabase.app/",
  "storageBucket": "robottieptan.appspot.com"
}

firebase = Firebase(config)

db = firebase.database()
ntm = db.child('dtbs').child('humanResource').get()
print(ntm.val())

data = json.load(open('assets/database.json'))