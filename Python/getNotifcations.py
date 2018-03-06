import http.client
import json
import authorization

class HubNotifications:
    def getNotifications(self):
        try:
            authorize = authorization.HubAuthorization()
            bearerToken = authorize.authorizeHub()          
            hubConn = http.client.HTTPSConnection(authorization.HUB_CONFIG['host'])
            headers = {
                'authorization': 'bearer ' + bearerToken,
                'content-type': 'application/json'
            }
            hubConn.request('GET', '/api/projects', headers=headers)
            res = hubConn.getresponse()
            data = res.read()
            print(data)
        except Exception as e:
            print(e)
    
#notifications = HubNotifications()
#notifications.getNotifications()
