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


