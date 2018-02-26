#!/bin/bash
HUB_HOST="hubtest.com"
HUB_AUTH_TOKEN=""

REQUEST_URL="https://"$HUB_HOST"/api/tokens/authenticate"

curl --request POST --url $REQUEST_URL --header 'authorization: token '$HUB_AUTH_TOKEN --header 'cache-control: no-cache'