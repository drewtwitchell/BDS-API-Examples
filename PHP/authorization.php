<?php

    class HubAuthorization {
        public $hubHost = "hubeval74.blackducksoftware.com";
        public $authToken = "token MDBjOWU1YjItOWE1OC00YTZiLWE4MzktOTE3MWZiMDg1YzI5OjczNjE1N2Q2LTc3MjEtNDU1ZC05NmQ3LWYwNGJhOThhOWQyYg";

        function authorizaHub() {
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
    $authorize->authorizaHub()

?>