from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime

CLIENT_SECRET_FILE= '../../credentials.json'
API_NAME='calendar'
API_VERSION='v3'
SCOPES=['https://www.googleapis.com/auth/calendar']

service=Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

# 캘린더 id는 구글캘린더 내부에서 직접적으로 확인도 가능함.
calendar_id='8d762569ee30e088994ea3a39d894a289a99bdb4792c960ff6b9c220cfeb5dbe@group.calendar.google.com'

# # create an event
# colors = service.colors().get().execute()
# pprint(colors)

#insert 구간
#필요없는 조정 adjustment일수있음. 왜냐면 시간조정용 이니깐..
hour_adjustment=-1
event_request_body={
    'start': {
      'dateTime': convert_to_RFC_datetime(2023,1,9,12 + hour_adjustment,30),
      'timeZone': 'Asia/Taipei'
    },
    'end':{
        'dateTime': convert_to_RFC_datetime(2023,1,9,15 + hour_adjustment,30),
        'timeZone': 'Asia/Taipei'
    },
    'summary': 'API Insert 2222',
    'description': 'Final insert',
    'colorId': 5,
    'status':'confirmed',
    'transparency': 'opaque',
    'visibility': 'private',
    'location' : 'seoul',
    'attendees':[
        {
            'displayName':'nsnsnsns',
            'comment':' I enjoy coding',
            'email': 'taipoone@naver.com',
            'optional': False,
            'organizer': True,
            'responseStatus':'accepted'
        }
    ]
}

maxAttendees=1
sendNotification=True
sendUpdate='none'
supportsAttachments=True

response =service.events().insert(
    calendarId=calendar_id,
    maxAttendees=maxAttendees,
    sendNotifications=sendNotification,
    sendUpdates=sendUpdate,
    supportsAttachments=supportsAttachments,
    body=event_request_body
).execute()

pprint(response)
