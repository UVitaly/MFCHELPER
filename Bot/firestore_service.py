from booking import Booking
import threading
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from booking import Booking
import datetime as dt


cred = credentials.Certificate("firebase-adminsdk.json")
app = firebase_admin.initialize_app(cred)
db = firestore.client()

booking_collection = db.collection(u'booking')
booking_list = []
display = 'Не удается отобразить список бронирования.'


def add_booking(new_booking):
    print(new_booking.to_dict())
    booking_collection.document().set(new_booking.to_dict())


def delete_booking_by_userid(user_id):
    global booking_list
    for booking in booking_list:
        if(booking.user_id==user_id):
            booking_collection.document(booking.id).delete()
            return True
    return False


def delete_booking_by_documentid(id):
    booking_collection.document(id).delete()


def get_booking_list():
    dates = []
    to_display = 'Список бронирования.\n\n'
    dates.clear()
    for booking in booking_list:
        if not booking.datetime.date() in dates:
            dates.append(booking.datetime.date())

    for date in dates:
        ampm = dt.datetime(year=date.year,month=date.month,day=date.day).strftime("%A")
        to_display += str(date.day) +'/'+str(date.month) +'/'+str(date.year) +' '+ampm+'\n'
        for booking in booking_list:
            if(booking.datetime.date()==date):
                to_display += booking.name + '   ' + booking.datetime.strftime("%I:%M %p") +'\n'
        to_display += '\n'
    return to_display



stream_callback = threading.Event()
def on_snapshot(doc_snapshot, changes, read_time):
    global booking_list
    global display
    booking_list.clear()
    for doc in doc_snapshot:
        booking = Booking()
        booking.from_dict(doc.to_dict(),doc.id)
        booking_list.append(booking)
        print('id: ',booking,' ',doc.to_dict())
    print('\n')
    #sort by datetime
    booking_list.sort(key=lambda booking: booking.datetime)
    display = get_booking_list()
    stream_callback.set()
doc_watch = booking_collection.on_snapshot(on_snapshot)

