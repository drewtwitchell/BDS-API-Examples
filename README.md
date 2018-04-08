# BDS-API-Examples

Black Duck Software API Code Examples

All the examples utilize authorization tokens which can be generated within an instance of the Hub.

## Table of Contents

  1. [Go](#go)
  1. [JavaScript](#javascript)
  1. [PHP](#php)
  1. [Python](#python)
  1. [Shell](#shell)

## Go

  <a name="go"></a>
**Authorization**

```go
package main

import (
    "fmt"
    "net/http"
    "io/ioutil"
)

func main() {

    host := "https://hubtest.com"

    url := host + "/api/tokens/authenticate"

    req, _ := http.NewRequest("POST", url, nil)

    // Add 'token ' before inserting the token from the Hub
    req.Header.Add("authorization", "token ")
    req.Header.Add("cache-control", "no-cache")

    res, _ := http.DefaultClient.Do(req)

    defer res.Body.Close()
    body, _ := ioutil.ReadAll(res.Body)

    fmt.Println(res)
    fmt.Println(string(body))

}
```

**[⬆ back to top](#table-of-contents)**

## JavaScript

  <a name="javascript"></a>
**Authorization**

```javascript
const request = require('request')

// Reminder to add 'token ' before auth from Hub
HUB_CONFIG = {
    host: 'https://hubtest.com',
    token: 'token '
}
const headers = {
    'authorization': HUB_CONFIG.token,
    'cache-control': 'no-cache'
}

const options = {
    url: HUB_CONFIG.host + '/api/tokens/authenticate',
    method: 'POST',
    headers: headers
}

function authorizeHub() {
    request(options, function (error, response, body) {
        if (error) {
            return console.log(error)
        }
            
        let res = JSON.parse(body)
        // Pass bearer token as auth headers during subsequent requests
        return console.log(res.bearerToken)
    })
}

authorizeHub()

```

**[⬆ back to top](#table-of-contents)**

## PHP

  <a name="php"></a>
**Authorization**

    class HubAuthorization {
        public $hubHost = "hubtest.com";
        public $authToken = "token ";

        function authorizeHub() {
            $request = new HttpRequest();
            $requestUrl = "https://" . $this->hubHost . "/api/tokens/authenticate";
            $request->setUrl($requestUrl);
            $request->setMethod(HTTP_METH_POST);
    
            $request->setHeaders(array(
                'authorization' => $authToken,
                'cache-control' => 'no-cache'
            ));

            try {
                $response = $request->send();
                echo $response->getBody();
            } catch (HttpException $ex) {
                echo $ex;
            }

        }

    }

    $authorize = new HubAuthorization; 
    $authorize->authorizeHub()

**[⬆ back to top](#table-of-contents)**

## Python

  <a name="python--authorization"></a>
**Authorization**

```python
import http.client
import json

# Hub Variables
# Reminder to add 'token ' before the auth token from the Hub

HUB_CONFIG = {
    'host': 'huburl.com',
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

authorize = HubAuthorization()
authorize.authorizeHub()
```

**GET request**

```python
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

        
notifications = HubNotifications()
notifications.getNotifications()
```


**[⬆ back to top](#table-of-contents)**

## Shell
For Shell, it is highly recommended that you install jq to deal with the challenges that are introduced when parsing JSON responses. 

  <a name="shell"></a>
  
    #!/bin/bash
    HUB_HOST="hubtest.com"
    HUB_AUTH_TOKEN=""

    REQUEST_URL="https://"$HUB_HOST"/api/tokens/authenticate"

    curl --request POST --url $REQUEST_URL --header 'authorization: token '$HUB_AUTH_TOKEN --header 'cache-control: no-cache'

**[⬆ back to top](#table-of-contents)**