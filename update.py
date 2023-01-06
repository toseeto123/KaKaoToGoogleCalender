from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime

CLIENT_SECRET_FILE='credentials.json'
API_NAME='calendar'
API_VERSION='v3'
SCOPES=['https://www.googleapis.com/auth/calendar']

service=Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

# 캘린더 id는 구글캘린더 내부에서 직접적으로 확인도 가능함.
calendar_id='8d762569ee30e088994ea3a39d894a289a99bdb4792c960ff6b9c220cfeb5dbe@group.calendar.google.com'

# create an event
colors = service.colors().get().execute()
pprint(colors)

#필요없는 조정 adjustment일수있음.
hour_adjustment=-1
event_request_body={
    'start': {
      'dateTime': convert_to_RFC_datetime(2023,1,5,12 + hour_adjustment,30),
      'timeZone': 'Asia/Taipei'
    },
    'end':{
        'dateTime': convert_to_RFC_datetime(2023,1,5,12 + hour_adjustment,30),
        'timeZone': 'Asia/Taipei'
    },
    'summary': '가족식사',
    'description': '부모님과 저녁먹기',
    'colorId': 5,
    'status':'confirmed',
    'transparency': 'opaque',
    'visibility': 'private',
    'location' : 'seoul',
    'attendees':[
        {
            'displayName':'JJ',
            'comment':' I enjoy coding',
            'email': 'taipoone@naver.com',
            'optional': False,
            'organizer': True,
            'responseStatus':'accepted'
        }
    ]
}

maxAttendees=5
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

###update 구간

eventId=response['id']

###update 구간 코드
start_dateTime= convert_to_RFC_datetime(2023 , 1 , 5 ,18 + hour_adjustment,30)
end_dateTime= convert_to_RFC_datetime(2023 , 1 , 6, 20 + hour_adjustment, 30)
response['start']['dateTime']=start_dateTime
response['end']['dateTime']=end_dateTime
response['summary'] = '바비파티로 수정 업데이트'
response['Description']='파뤼파뤼투나잇'
service.events().update(
    calendarId=calendar_id,
    eventId=eventId,
    body=response).execute()
