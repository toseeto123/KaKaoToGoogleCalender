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
#
# ###update 구간 코드
# start_dateTime= convert_to_RFC_datetime(2023 , 1 , 5 ,18 + hour_adjustment,30)
# end_dateTime= convert_to_RFC_datetime(2023 , 1 , 6, 20 + hour_adjustment, 30)
# response['start']['dateTime']=start_dateTime
# response['end']['dateTime']=end_dateTime
# response['summary'] = '바비파티로 수정 업데이트'
# response['Description']='파뤼파뤼투나잇'
# service.events().update(
#     calendarId=calendar_id,
#     eventId=eventId,
#     body=response).execute()
#
# ##delete 구간
# service.events().delete(calendarId=calendar_id,eventId=eventId).execute()
#
# #list 이벤트 구간
# today = datetime.date.today().isoformat()
# time_min = today + 'T00:00:00+09:00'
# time_max = today + 'T23:59:59+09:00'
# max_results = 5
# is_single_events = True
# orderby = 'startTime'
#
# response = service.events().list(
#         calendarId=calendar_id,
#         timeMin=time_min,
#         timeMax=time_max,
#         maxResults=250,
#         singleEvents=is_single_events,
#         orderBy=orderby
# ).execute()
# calendarItems = response.get('items')
# nextPageToken = response.get('nextPageToken')
#
# while nextPageToken:
#     response = service.events().list(
#         maxResults=250,
#         showDeleted=False,
#         showHidden=False,
#         pageToken=nextPageToken
#     ).execute()
#     calendarItems = extend(response.get('items'))
#     nextPageToken = response.get('nextPageToken')
#
# pprint(calendarItems)
#
#
#
