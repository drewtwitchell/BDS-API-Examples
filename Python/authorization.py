import http.client
import json

# Hub Variables
# Reminder to add 'token ' before the auth token from the Hub

HUB_CONFIG = {
    'host': 'hub.com',
    'token': 'token '
}

# Hub Connect

class HubAuthorization:
    def authorizeHub(self):
        try:
            hubConn = http.client.HTTPSConnection(HUB_CONFIG['host'])
            headers = {
                'authorization': HUB_CONFIG['token'],
                'cache-control': 'no-cache'
            }
            hubConn.request('POST', '/api/tokens/authenticate', headers=headers)
            res = hubConn.getresponse()
            data = res.read().decode('utf-8')
            auth_obj = json.loads(data)
            # Pass bearer token as auth headers in subsequent requests
            bearerToken = auth_obj['bearerToken']
            print('Hub Authorization Succeeded.')
            return bearerToken

        except Exception as e:
            print('Cannot connect to Hub. Invalid token.')
            print(e)



#authorize = HubAuthorization()
#authorize.authorizeHub()