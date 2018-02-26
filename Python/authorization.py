import http.client
import json

# Hub Variables
HUB_CONFIG = {
    'host': 'hubeval74.blackducksoftware.com',
    'token': 'token MDBjOWU1YjItOWE1OC00YTZiLWE4MzktOTE3MWZiMDg1YzI5OjIyY2Y3YTQzLTYwYTctNGQ1My05NWI5LWFiM2Q1MWRkYWRjZg=='
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
            bearerToken = auth_obj['bearerToken']
            print('Hub Authorization Succeeded.')

        except Exception as e:
            print('Cannot connect to Hub. Invalid token.')
            print(e)

authorize = HubAuthorization()
authorize.authorizeHub()



