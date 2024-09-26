---
title: Sample code for Number Verification
excerpt: The following samples show how to use the [Open Gateway Number Verification API](https://opengateway.telefonica.com/en/apis/number-verification), for fraud prevention purposes, in order to check if a given phone number matches the one on the SIM card installed in the end-user's device.
category: 66aa4f941e51e7000fa353ce
---

Although the API consumption flow for this API must be always triggered from such end-user's device - therefore from the application's frontend - according to its intrinsic feature, the flow will always complete on the backend. The following code shows, for didactic purposes, a hypothetical or sample SDK used on the backend, in several programming languages, from a generic Open Gateway's channel partner, also known as aggregator.

The final implementation will depend on the channel partner's development tools offering. Some of them might even provide you with both backend SDKs and frontend SDKs, the latter handling details such as network interface switching for proper mobile line identification. Apart from this extra frontend features (available upon channel partner discretion), note that channel partners' Open Gateway SDKs are just code modules wrapping authentication and API calls providing an interface in your app's programming for convenience.

Sample code on how to consume the API without an SDK, directly with HTTP requests, is also provided, and it is common and valid no matter what your partner is, thanks to the CAMARA standardization. If you do not use an SDK you need to code the HTTP calls and additional stuff like encoding your credentials, calling authorization endpoints, handling tokens, etc. You can check our sample [Postman collection](https://bxbucket.blob.core.windows.net/bxbucket/opengateway-web/uploads/OpenGateway.postman_collection.json) as a reference.

>**.callout_info**
It is recomended to use the [API Reference tool](
https://developers.opengateway.telefonica.com/reference/
) for faster calls of our APIs

### Table of contents
- [Frontend](#frontend)
    - [Requesting the authorization code from the frontend](#requesting-the-authorization-code-from-the-frontend)
- [Backend](#backend)
    - [Getting the access token from the callback endpoint at the backend](#getting-the-access-token-from-the-callback-endpoint-at-the-backend)
    - [Using the service API](#using-the-service-api)

## Code samples
> **.callout_warn** These are code examples
> - Remember to replace 'my-app-id' and 'my-app-secret' with the credentials of your app. (If you are using our Sandbox, you can get them [here](https://sandbox.opengateway.telefonica.com/my-apps)). 
> - Remember also to replace "aggregator/opengateway-sdk" with the SDK from your aggregator. If you are using our sandbox SDK, check info and installation of de Sandbox SDK [here](../../gettingstarted/sandbox/sdkreference.md)

### Frontend

This API consumption flow must always start on the end-user's device, since its feature is precisely verifying that a given phone number is the one effectively used in such device, which can be verified by the operator by receiving the online request from it:
* Application's frontend performs an HTTP request to get a `code`, and provides a `redirect_uri` it wants such `code` to be redirected to.
* Application's frontend will receive an HTTP redirect (status 302) and needs to be able to handle it. If it is a web application running on a web browser, the browser will natively follow the redirection. If it is not, in depends on the coding language and/or HTTP module or library used, or on its settings, how the flow will follow all the way to your application's backend through the mobile network operator authentication server.
* Application's backend receives the `code` from this HTTP redirection, by publishing an endpoint in the given `redirect_uri`, and then exchanges it for an access token. The latter is achieved as shown in the [Backend](#backend) flow.

The authentication protocol used in Open Gateway for frontend flows is the OIDC standard Authorization Code Flow. You can check the CAMARA documentation on this flow [here](https://github.com/camaraproject/IdentityAndConsentManagement/blob/release-0.1.0/documentation/CAMARA-API-access-and-user-consent.md#authorization-code-flow-frontend-flow).

#### Requesting the authorization code from the frontend

The following samples show how your application can trigger the authentication flow from the frontend either from code or by submitting a simple HTML form. The same can be achieved from code in any other programming language with the ability to perform HTTP requests:
```javascript HTTP using JavaScript (ES6)
let userPhoneNumber = "+34555555555";

let clientId = "my-app-id";
let clientSecret = "my-app-secret";
let apiPurpose = "dpv:FraudPreventionAndDetection#number-verification-verify-read";
let myCallbackEndpoint = "https://my_app_server/numberverification-callback";

const params = {
  client_id: clientId,
  response_type: "code",
  purpose: apiPurpose,
  redirect_uri: myCallbackEndpoint,
  state: userPhoneNumber // Using `state` as the parameter that is always forwarded to the redirect_uri
};

// Create the query string
const queryString = new URLSearchParams(params).toString();

// URL with query string
const url = `https://opengateway.aggregator.com/authorize?${queryString}`;

const requestOptions = {
  method: "GET",
  redirect: "follow"
};

fetch(url, requestOptions);
```
```html HTML form
<!--
    In this example you need your callback URL to continue the flow calling the service API
    and providing an HTML response to be shown in the web browser displaying the result.
    The following form is published from the same web server hosting the callback URL.
-->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>API Request Form</title>
</head>
<body>
    <h1>Number verification</h1>
    <form id="apiRequestForm" action="https://opengateway.aggregator.com/authorize" method="GET">
        <input type="hidden" name="client_id" value="my-app-id">
        <input type="hidden" name="response_type" value="code">
        <input type="hidden" name="purpose" value="dpv:FraudPreventionAndDetection#number-verification-verify-read">
        <input type="hidden" name="redirect_uri" value="/numberverification-callback">
        
        <label for="state">Your phone number:</label>
        <input type="text" id="state" name="state" value="+34555555555" required>
        
        <button type="submit">Verify</button>
    </form>
</body>
</html>
```

### Backend

As the opposite to the flow triggering, this API consumption flow will always complete on the application's backend, since the authorization code is to be received via HTTP redirect on your redirect_uri, aka callback URL, which must be published on a web server.

#### Getting the access token from the callback endpoint at the backend

Samples represent how to publish the callback URL in Python or Node.js, so the code from the Auth Code Flow can be received. The same can be achieved in any other language with capabilities to run an HTTP server and listen for the redirect from the authentication flow:

```python Sample SDK for Python
from flask import Flask, request, jsonify
from aggregator_opengateway_sdk import ClientCredentials, NumberVerification

credentials = ClientCredentials(
    clientid='my-app-id',
    clientsecret='my-app-secret'
)

app = Flask(__name__)

@app.route('/numberverification-callback', methods=['GET'])
def callback():
    code = request.args.get('code', '')
    phone_number = request.args.get('state', '')
    api_client = NumberVerification(credentials, code)

if __name__ == '__main__':
    app.run()
```
```node Sample SDK for Node.js
import { ClientCredentials, NumberVerification } from "aggregator/opengateway-sdk"
import express from "express"

const credentials: ClientCredentials(
    clientId: 'my-app-id',
    clientSecret: 'my-app-secret'
)

const app = express()
const port = 3000

app.get('/numberverification-callback', (req, res) => {
    const code = req.query.code
    const phoneNumber = req.query.state
    const apiClient = new NumberVerification(credentials, code)
})

app.listen(port, () => {
    console.log(`Number verification callback URL is running`);
})
```
```python HTTP using Python
from flask import Flask, request, jsonify

client_id = "my-app-id"
client_secret = "my-app-secret"
app_credentials = f"{client_id}:{client_secret}"
credentials = base64.b64encode(app_credentials.encode('utf-8')).decode('utf-8')
api_purpose = "dpv:FraudPreventionAndDetection#number-verification-verify-read"

app = Flask(__name__)

@app.route('/numberverification-callback', methods=['GET'])
def callback():
    code = request.args.get('code', '')
    phone_number = request.args.get('state', '')
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {credentials}"
    }
    data = {
        "grant_type": "authorization_code",
        "code": code
    }
    response = requests.post(
        "https://opengateway.aggregator.com/token",
        headers=headers,
        data=data
    )
    access_token = response.json().get("access_token")

if __name__ == '__main__':
    app.run()
```
```node HTTP using Node.js
import express from "express"

let clientId = "my-app-id"
let clientSecret = "my-app-secret"
let appCredentials = btoa(`${clientId}:${clientSecret}`)
let apiPurpose = "dpv:FraudPreventionAndDetection#number-verification-verify-read"

const app = express()
const port = 3000

app.get('/numberverification-callback', (req, res) => {
    const code = req.query.code
    const phoneNumber = req.query.state

    let accessToken

    const myHeaders = new Headers()
    myHeaders.append("Content-Type", "application/x-www-form-urlencode")
    myHeaders.append("Authorization", `Basic ${appCredentials}`)
    const requestBody = JSON.stringify({
        "grant_type": "authorization_code",
        "code": code
    })
    const requestOptions = {
        method: "POST",
        headers: myHeaders,
        body: requestBody
    }
    fetch("https://opengateway.aggregator.com/token", requestOptions)
        .then(response => response.json())
        .then(result => {
            accessToken = result.access_token
        })
})

app.listen(port, () => {
    console.log(`Number verification callback URL is running`);
})

```

#### Using the service API

Once your app is authenticated it only takes a single line of code to use the service API and effectively get a result.

```python Sample SDK for Python
result = await api_client.verify(phone_number)

print(f"Phone number {'verified' if result else 'does not match mobile line'}")
```
```node Sample SDK for Node.js
let result = await apiClient.verify(phoneNumber)

console.log(`Phone number ${result ? "verified" : "does not match mobile line"}`)
```
```python HTTP using Python
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}
data = {
    "phoneNumber": phone_number
}
response = requests.post(
    "https://opengateway.aggregator.com/number-verification/v0/verify",
    headers=headers,
    json=data
)
result = response.json().get("devicePhoneNumberVerified")

print(f"Phone number {'verified' if result else 'does not match mobile line'}")
```
```node HTTP using Node.js
const myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");
myHeaders.append("Authorization", `Bearer ${accessToken}`);

const requestBody = JSON.stringify({
  "phoneNumber": phoneNumber
})
const requestOptions = {
  method: "POST",
  headers: myHeaders,
  body: requestBody
}

fetch("https://opengateway.aggregator.com/number-verification/v0/verify", requestOptions)
  .then(response => response.json())
  .then(result => {
    const verified = result.devicePhoneNumberVerified
    
    console.log(`Phone number ${verified ? "verified" : "does not match mobile line"}`)
  })
```
