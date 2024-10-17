---
title: Sample code for Device Status
excerpt: The following samples show how to use the [Open Gateway Device Status API](https://opengateway.telefonica.com/en/apis/device-status), to control your resource management during international roaming more securely
category: 66aa4f941e51e7000fa353ce
---

The following code shows, for didactic purposes, a hypothetical or sample SDK, in several programming languages, from a generic Open Gateway's channel partner, also known as aggregator. The final implementation will depend on the channel partner's development tools offering. Note that channel partners' Open Gateway SDKs are just code modules wrapping authorization and API calls providing an interface in your app's programming for convenience.

Sample code on how to consume the API without an SDK, directly with HTTP requests, is also provided, and it is common and valid no matter what your partner is, thanks to the CAMARA standardization. If you do not use an SDK you need to code the HTTP calls and additional stuff like encoding your credentials, calling authorization endpoints, handling tokens, etc. You can check our sample [Postman collection](https://bxbucket.blob.core.windows.net/bxbucket/opengateway-web/uploads/OpenGateway.postman_collection.json) as a reference.

> 📘 It is recomended to use the [API Reference tool](https://developers.opengateway.telefonica.com/reference/) for faster calls of our APIs

### Table of contents
- [Backend flow](#backend-flow)
    - [Authorization](#authorization)
    - [API usage](#api-usage)
- [Frontend flow](#frontend-flow)
    - [Authorization](#authorization-1)
        - [Requesting the authorization code from the frontend](#requesting-the-authorization-code-from-the-frontend)
        - [Getting the access token from the callback endpoint at the backend](#getting-the-access-token-from-the-callback-endpoint-at-the-backend)
    - [API usage](#api-usage-1)

## Code samples
> 📘 These are code examples
> - Remember to replace 'my-app-id' and 'my-app-secret' with the credentials of your app. (If you are using our Sandbox, you can get them [here](https://sandbox.opengateway.telefonica.com/my-apps)).
> - Remember also to replace "aggregator/opengateway-sdk" with the SDK from your aggregator. If you are using our sandbox SDK, check info and installation of de Sandbox SDK [here](../../gettingstarted/sandbox/sdkreference.md)

### Backend flow

Most likely, this API will be consumed in a backend flow, since it is the application owner not the end-user who wants to take advantage of its functionality. The authorization protocol used in Open Gateway for backend flows is the OIDC standard CIBA (Client-Initiated Backchannel Authentication). You can check the CAMARA documentation on this flow [here](https://github.com/camaraproject/IdentityAndConsentManagement/blob/release-0.1.0/documentation/CAMARA-API-access-and-user-consent.md#ciba-flow-backend-flow).

#### Authorization

```python Sample SDK for Python
from aggregator_opengateway_sdk import ClientCredentials, SimSwap

credentials = ClientCredentials(
    client_id='my-app-id',
    client_secret='my-app-secret'
)

customer_phone_number = '+34555555555'

simswap_client = SimSwap(credentials=credentials, phone_number=customer_phone_number)
```

### Frontend flow

Although it is not common to face a use case for SIM Swap where the user device is involved in the flow and, at the same time, it is easier to get the phone number on the frontend that on the backend, or it is more precise in terms of data quality on each end, if you wanted to start the service API consumption from a frontend application, you would need to implement the OIDC's Authorization Code Flow instead of CIBA. This flow implies your application providing a callback URL that you will need to publish online hosted on your backend server, and in which your application's backend will get a `code` authorizing it to use the Open Gateway APIs for your end-user.

This flow allows the mobile network operator to effectively identify the user by resolving the IP address of their device, running your application, by getting an HTTP redirection and returning a `code` that will reach out to your callback URL. You can check the CAMARA documentation on the Authorization Code Flow [here](https://github.com/camaraproject/IdentityAndConsentManagement/blob/release-0.1.0/documentation/CAMARA-API-access-and-user-consent.md#authorization-code-flow-frontend-flow).

From this point, your application, from its backend, will request an access token, and use it to call the service API.

#### Authorization

Some Channel Partners may provide you with frontend SDKs to handle the Authorization Code Flow on your application's behalf, providing some extra features like checking your end-user's device network interface to avoid problems caused from it being connected to a WiFi network, for instance, since this flow relies on the mobile line connectivity for the operator to identify the end-user and authorize your application.

The following samples show how to implement the flow without a frontend SDK with these premises:
* Application's frontend performs an HTTP request to get a `code`, and provides a `redirect_uri` it wants such `code` to be redirected to.
* Application's frontend will receive an HTTP redirect (status 302) and needs to be able to handle it. If it is a web application running on a web browser, the browser will natively follow the redirection. If it is not, in depends on the coding language and/or HTTP module or library used, or on its settings, how the flow will follow all the way to your application's backend through the mobile network operator authorization server.
* Application's backend receives the `code` from this HTTP redirection, by publishing an endpoint in the given `redirect_uri`, and then exchanges it for an access token. The latter can be achieved by using a backend SDK as shown in the [Backend flow](#backend-flow).

The authorization protocol used in Open Gateway for frontend flows is the OIDC standard Authorization Code Flow. You can check the CAMARA documentation on this flow [here](https://github.com/camaraproject/IdentityAndConsentManagement/blob/release-0.1.0/documentation/CAMARA-API-access-and-user-consent.md#authorization-code-flow-frontend-flow).

#### Requesting the authorization code from the frontend

The following samples show how your application can trigger the authorization flow from the frontend either from code or by submitting a simple HTML form. The same can be achieved from code in any other programming language with the ability to perform HTTP requests:

```ecmascript HTTP using JavaScript (ES6)
let userPhoneNumber = "+34555555555";

let clientId = "my-app-id";
let clientSecret = "my-app-secret";
let apiPurpose = "dpv:FraudPreventionAndDetection#sim-swap";
let myCallbackEndpoint = "https://my_app_server/simswap-callback";

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
    <h1>SIM swap date check</h1>
    <form id="apiRequestForm" action="https://opengateway.aggregator.com/authorize" method="GET">
        <input type="hidden" name="client_id" value="my-app-id">
        <input type="hidden" name="response_type" value="code">
        <input type="hidden" name="purpose" value="dpv:FraudPreventionAndDetection#sim-swap">
        <input type="hidden" name="redirect_uri" value="/simswap-callback">

        <label for="state">Your phone number:</label>
        <input type="text" id="state" name="state" value="+34555555555" required>

        <button type="submit">Check</button>
    </form>
</body>
</html>
```

#### Getting the access token from the callback endpoint at the backend

Samples represent how to publish the callback URL in Python or Node.js, so the code from the Auth Code Flow can be received. The same can be achieved in any other language with capabilities to run an HTTP server and listen for the redirect from the authorization flow:

```python Sample SDK for Python
from flask import Flask, request, jsonify
from aggregator_opengateway_sdk import ClientCredentials, SIMSwap

credentials = ClientCredentials(
    clientid='my-app-id',
    clientsecret='my-app-secret'
)

app = Flask(__name__)

@app.route('/simswap-callback', methods=['GET'])
def callback():
    code = request.args.get('code', '')
    phone_number = request.args.get('state', '')
    simswap_client = SIMSwap(client=credentials, auth_code=code)

if __name__ == '__main__':
    app.run()
```
```node Sample SDK for Node.js
import { ClientCredentials, SIMSwap } from "aggregator/opengateway-sdk"
import express from "express"

const credentials: ClientCredentials(
    clientId: 'my-app-id',
    clientSecret: 'my-app-secret'
)

const app = express()
const port = 3000

app.get('/simswap-callback', (req, res) => {
    const code = req.query.code
    const phoneNumber = req.query.state
    const simswapClient = new SIMSwap(credentials, code)
})

app.listen(port, () => {
    console.log(`SIM Swap callback URL is running`);
})
```

#### API usage

Once your app is authenticated it only takes a single line of code to use the service API and effectively get a result.

```python Sample SDK for Python
result = await simswap_client.retrieve_date(phone_number)

print(f"SIM was swapped: {result.strftime('%B %d, %Y, %I:%M:%S %p')}")
```
```node Sample SDK for Node.js
let result = await simswapClient.retrieveDate(phoneNumber)

console.log(`SIM was swapped: ${result.toLocaleString('en-GB', { timeZone: 'UTC' })}`)
```
