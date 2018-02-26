<?php

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

?>