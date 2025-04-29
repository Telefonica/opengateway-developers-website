---
title: Sample code for SIM Swap
excerpt: The following samples show how to use the [Open Gateway SIM Swap API](https://opengateway.telefonica.com/en/apis/sim-swap), for fraud prevention purposes, in order to check if a given mobile line, identified by its phone number, has gotten a SIM card swap lately.
category: 6810d75473b7c4005a02031a
version: 0
---

The following code shows, for didactic purposes, a hypothetical or sample SDK, in several programming languages, from a generic Open Gateway's channel partner, also known as aggregator. The final implementation will depend on the channel partner's development tools offering. Note that channel partners' Open Gateway SDKs are just code modules wrapping authorization and API calls providing an interface in your app's programming for convenience.

Sample code on how to consume the API without an SDK, directly with HTTP requests, is also provided, and it is common and valid no matter what your partner is, thanks to the CAMARA standardization. If you do not use an SDK you need to code the HTTP calls and additional stuff like encoding your credentials, calling authorization endpoints, handling tokens, etc. You can check our sample [Postman collection](https://github.com/Telefonica/opengateway-postman) as a reference.

> 📘 Want to give it a try before coding?
> Check the [API interactive reference](https://developers.opengateway.telefonica.com/reference/checksimswap)

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

> 📘 Note
> These are code samples and not finalized ready-to-run code:
> - Remember to replace 'my-app-id' and 'my-app-secret' with the credentials of your app.
If you registered your test app on our Sandbox, you can retrieve its credentials [here](https://sandbox.opengateway.telefonica.com/my-apps). 
> - Remember also to replace "aggregator/opengateway-sdk" with the SDK from your aggregator.
If you are using our sandbox SDK, check info and installation of de Sandbox SDK [here](/docs/sdkreference)

### Backend flow

Most likely, this API will be consumed in a backend flow, since it is the application owner not the end-user who wants to take advantage of its functionality. The authorization protocol used in Open Gateway for backend flows is the OIDC standard CIBA (Client-Initiated Backchannel Authentication). You can check the CAMARA documentation on this flow [here](https://github.com/camaraproject/IdentityAndConsentManagement/blob/release-0.1.0/documentation/CAMARA-API-access-and-user-consent.md#ciba-flow-backend-flow).

First step is to instantiate the SIM Swap service class included in the corresponding SDK. By providing your app's credentials to the class constructor, it handles the CIBA authorization on its behalf. Providing the phone number as well, as an identifier of the line to be checked for SIM swaps, allows authorization to be 3-legged and enables end-user consent management, and will let your app to just effectively use the API in a single line of code below.

#### Authorization

Since Open Gateway authorization is 3-legged, meaning it identifies the application, the operator and the operator's subscriber, who is also the end-user holder of the mobile line, each check for a different phone number needs its own SDK class instantiation, or access token if not using an SDK.

```python Sandbox SDK for Python
from opengateway_sandbox_sdk import Simswap

client_id = 'your_client_id'
client_secret = 'your_client_secret'
customer_phone_number = '+34555555555'

simswap_client = Simswap(client_id, client_secret, customer_phone_number)
```
```python Sample SDK for Python
from aggregator_opengateway_sdk import ClientCredentials, SimSwap

credentials = ClientCredentials(
    client_id='my-app-id',
    client_secret='my-app-secret'
)

customer_phone_number = '+34555555555'

simswap_client = SimSwap(credentials=credentials, phone_number=customer_phone_number)
```
```node Sandbox SDK for Node.js
import sandboxSdk from '@telefonica/opengateway-sandbox-sdk'
const { Simswap } = sandboxSdk

const credentials = {
    clientId: 'your_client_id',
    clientSecret: 'your_client_secret'
}

const CUSTOMER_PHONE_NUMBER = '+34666666666'

const simswapClient = new Simswap(credentials.clientId, credentials.clientSecret, CUSTOMER_PHONE_NUMBER)
```
```node Sample SDK for Node.js
import { ClientCredentials, SIMSwap } from "aggregator/opengateway-sdk"

const credentials: ClientCredentials(
    clientId: 'my-app-id',
    clientSecret: 'my-app-secret'
)

const CUSTOMER_PHONE_NUMBER = '+34555555555'

const simswapClient = new SIMSwap(credentials, null, CUSTOMER_PHONE_NUMBER)
```
```java Sample SDK for Java
import aggregator.opengatewaysdk.ClientCredentials;
import aggregator.opengatewaysdk.SIMSwap;

ClientCredentials credentials = new ClientCredentials(
    "my-app-id",
    "my-app-secret"
);

final String customerPhoneNumber = "+34555555555";

SIMSwap simswapClient = new SIMSwap(credentials, null, customerPhoneNumber);
```
```ecmascript HTTP using JavaScript (ES6)
// First step:
// Perform an authorization request

let customerPhoneNumber = "+34555555555";

let clientId = "my-app-id";
let clientSecret = "my-app-secret";
let appCredentials = btoa(`${clientId}:${clientSecret}`);
let apiScope = "dpv:FraudPreventionAndDetection#sim-swap";

const myHeaders = new Headers();
myHeaders.append("Content-Type", "application/x-www-form-urlencoded");
myHeaders.append("Authorization", `Basic ${appCredentials}`);

const urlencoded = new URLSearchParams();
urlencoded.append("login_hint", `tel:${customerPhoneNumber}`);
urlencoded.append("scope", apiScope);

const requestOptions = {
  method: "POST",
  headers: myHeaders,
  body: urlencoded
};

let authReqId;

fetch("https://opengateway.aggregator.com/bc-authorize", requestOptions)
  .then(response => response.json())
  .then(result => {
    authReqId = result.auth_req_id;
  })

// Second step:
// Requesting an access token with the auth_req_id included in the result above

const tokenHeaders = new Headers();
tokenHeaders.append("Content-Type", "application/x-www-form-urlencoded");
tokenHeaders.append("Authorization", `Basic ${appCredentials}`);

urlencoded = new URLSearchParams();
urlencoded.append("grant_type", "urn:openid:params:grant-type:ciba");
urlencoded.append("auth_req_id", authReqId);

const tokenRequestOptions = {
  method: "POST",
  headers: tokenHeaders,
  body: urlencoded
};

let accessToken;

fetch("https://opengateway.aggregator.com/token", tokenRequestOptions)
  .then(response => response.json())
  .then(result => {
    accessToken = result.access_token;
  })
```
```java HTTP using Java
// First step:
// Perform an authorization request

String customerPhoneNumber = "+34555555555";

String clientId = "my-app-id";
String clientSecret = "my-app-secret";
String appCredentials = clientId + ":" + clientSecret;
String credentials = Base64.getEncoder().encodeToString(appCredentials.getBytes(StandardCharsets.UTF_8));
String apiScope = "dpv:FraudPreventionAndDetection#sim-swap";

HttpClient client = HttpClient.newHttpClient();

Map<Object, Object> data = new HashMap<>();
data.put("login_hint", "tel:" + customerPhoneNumber);
data.put("scope", apiScope);

StringBuilder requestBody = new StringBuilder();
for (Map.Entry<Object, Object> entry : data.entrySet()) {
    if (requestBody.length() > 0) {
        requestBody.append("&");
    }
    requestBody.append(URLEncoder.encode(entry.getKey().toString(), StandardCharsets.UTF_8));
    requestBody.append("=");
    requestBody.append(URLEncoder.encode(entry.getValue().toString(), StandardCharsets.UTF_8));
}

HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://opengateway.aggregator.com/bc-authorize"))
    .header("Content-Type", "application/x-www-form-urlencoded")
    .header("Authorization", "Basic " + credentials)
    .POST(BodyPublishers.ofString(requestBody.toString()))
    .build();

HttpResponse<String> response = client.send(request, BodyHandlers.ofString());
JSONObject jsonResponse = new JSONObject(response.body());
String authReqId = jsonResponse.getString("auth_req_id");

// Second step:
// Requesting an access token with the auth_req_id included in the result above

Map<Object, Object> data = new HashMap<>();
data.put("grant_type", "urn:openid:params:grant-type:ciba");
data.put("auth_req_id", authReqId);

StringBuilder requestBody = new StringBuilder();
for (Map.Entry<Object, Object> entry : data.entrySet()) {
    if (requestBody.length() > 0) {
        requestBody.append("&");
    }
    requestBody.append(URLEncoder.encode(entry.getKey().toString(), StandardCharsets.UTF_8));
    requestBody.append("=");
    requestBody.append(URLEncoder.encode(entry.getValue().toString(), StandardCharsets.UTF_8));
}

HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://opengateway.aggregator.com/token"))
    .header("Content-Type", "application/x-www-form-urlencoded")
    .header("Authorization", "Basic " + credentials)
    .POST(BodyPublishers.ofString(requestBody.toString()))
    .build();

HttpResponse<String> response = client.send(request, BodyHandlers.ofString());
JSONObject jsonResponse = new JSONObject(response.body());
String accessToken = jsonResponse.getString("access_token");
```
```python Sample HTTP using Python
import base64
import requests
# First step:
# Perform an authorization request

customer_phone_number = "+34555555555"

client_id = "my-app-id"
client_secret = "my-app-secret"
app_credentials = f"{client_id}:{client_secret}"
credentials = base64.b64encode(app_credentials.encode('utf-8')).decode('utf-8')
api_scope = "dpv:FraudPreventionAndDetection#sim-swap"

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": f"Basic {credentials}"
}

data = {
    "login_hint": f"tel:{customer_phone_number}",
    "scope": api_scope
}

response = requests.post(
    "https://opengateway.aggregator.com/bc-authorize",
    headers=headers,
    data=data
)

auth_req_id = response.json().get("auth_req_id")

# Second step:
# Requesting an access token with the auth_req_id included in the result above

headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Authorization": f"Basic {credentials}"
}

data = {
    "grant_type": "urn:openid:params:grant-type:ciba",
    "auth_req_id": auth_req_id
}

response = requests.post(
    "https://opengateway.aggregator.com/token",
    headers=headers,
    data=data
)

access_token = response.json().get("access_token")
```

#### API usage

Once your app is authenticated it only takes a single line of code to use the service API and effectively get a result.

```python Sandbox SDK for Python
result = simswap_client.retrieve_date()

print(f"SIM was swapped: {result.strftime('%B %d, %Y, %I:%M:%S %p')}")
```
```python Sample SDK for Python
result = simswap_client.retrieve_date()

print(f"SIM was swapped: {result.strftime('%B %d, %Y, %I:%M:%S %p')}")
```
```node Sandbox SDK for Node.js
let result = await simswapClient.retrieveDate()

console.log(`SIM was swapped: ${result.toLocaleString('en-GB', { timeZone: 'UTC' })}`)
```
```node Sample SDK for Node.js
let result = await simswapClient.retrieve_date()

console.log(`SIM was swapped: ${result.toLocaleString('en-GB', { timeZone: 'UTC' })}`)
```
```java Sample SDK for Java
CompletableFuture<Boolean> resultFuture = simswapClient.retrieve_date();

resultFuture.thenAccept(result -> {
    System.out.println("SIM was swapped: " + DateTimeFormatter.ISO_LOCAL_DATE.format(result));
})
```
```ecmascript HTTP using JavaScript (ES6)
const apiHeaders = new Headers();
apiHeaders.append("Content-Type", "application/json");
apiHeaders.append("Authorization", `Bearer ${accessToken}`);

const apiRequestBody = JSON.stringify({
  "phoneNumber": customerPhoneNumber // as set in the authorization step
});

const apiRequestOptions = {
  method: "POST",
  headers: apiHeaders,
  body: apiRequestBody
};

fetch("https://opengateway.aggregator.com/sim-swap/v0/retrieve-date", apiRequestOptions)
  .then(response => response.json())
  .then(result => {
    console.log(`SIM was swapped: ${result.latestSimChange}`)
  })
```
```java HTTP using Java
JSONObject requestBody = new JSONObject();
requestBody.put("phoneNumber", customerPhoneNumber); // as set in the authorization step

HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://opengateway.aggregator.com/sim-swap/v0/retrieve-date"))
    .header("Content-Type", "application/json")
    .header("Authorization", "Bearer " + accessToken)
    .POST(BodyPublishers.ofString(requestBody.toString()))
    .build();

HttpResponse<String> response = client.send(request, BodyHandlers.ofString());
JSONObject jsonResponse = new JSONObject(response.body());
String swapDate = jsonResponse.getString("latestSimChange");

System.out.println("SIM was swapped: " +  DateTimeFormatter.ISO_LOCAL_DATE.format(swapDate));
```
```python Sample HTTP using Python
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}

data = {
    "phoneNumber": customer_phone_number,  # as set in the authorization step
}

response = requests.post(
    "https://opengateway.aggregator.com/sim-swap/v0/retrieve-date",
    headers=headers,
    json=data
)

result = response.json()
print(f"SIM was swapped: {result.get('latestSimChange').strftime('%B %d, %Y, %I:%M:%S %p')}")
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
let apiScope = "dpv:FraudPreventionAndDetection#sim-swap";
let myCallbackEndpoint = "https://my_app_server/simswap-callback";

const params = {
  client_id: clientId,
  response_type: "code",
  scope: apiScope,
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
        <input type="hidden" name="scope" value="dpv:FraudPreventionAndDetection#sim-swap">
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

```python Sandbox SDK for Python
from flask import Flask, request
from opengateway_sandbox_sdk import ClientCredentials, Simswap

credentials = ClientCredentials(
    clientid='my-app-id',
    clientsecret='my-app-secret'
)

app = Flask(__name__)


@app.route('/simswap-callback', methods=['GET'])
def callback():
    code = request.args.get('code', '')
    phone_number = request.args.get('state', '')
    simswap_client = Simswap(client=credentials, auth_code=code)

if __name__ == '__main__':
    app.run()
```
```python Sample SDK for Python
from flask import Flask, request
from aggregator_opengateway_sdk import ClientCredentials, SimSwap

credentials = ClientCredentials(
    clientid='my-app-id',
    clientsecret='my-app-secret'
)

app = Flask(__name__)


@app.route('/simswap-callback', methods=['GET'])
def callback():
    code = request.args.get('code', '')
    phone_number = request.args.get('state', '')
    simswap_client = SimSwap(client=credentials, auth_code=code)

if __name__ == '__main__':
    app.run()
```
```node Sandbox SDK for Node.js
import sandboxSdk from '@telefonica/opengateway-sandbox-sdk'
const { Simswap } = sandboxSdk
import express from "express"

const credentials = {
    clientId: 'your_client_id',
    clientSecret: 'your_client_secret'
}

const app = express()
const port = 3000

app.get('/simswap-callback', (req, res) => {
    const code = req.query.code
    const phoneNumber = req.query.state
    const simswapClient = new Simswap(credentials.clientId, credentials.clientSecret, undefined, code)
})

app.listen(port, () => {
    console.log(`SIM Swap callback URL is running`)
})
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
```python Sample HTTP using Python
import base64
import requests
from flask import Flask, request

client_id = "my-app-id"
client_secret = "my-app-secret"
app_credentials = f"{client_id}:{client_secret}"
credentials = base64.b64encode(app_credentials.encode('utf-8')).decode('utf-8')
api_scope = "dpv:FraudPreventionAndDetection#sim-swap"

app = Flask(__name__)


@app.route('/simswap-callback', methods=['GET'])
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
let apiScope = "dpv:FraudPreventionAndDetection#sim-swap"

const app = express()
const port = 3000

app.get('/simswap-callback', (req, res) => {
    const code = req.query.code
    const phoneNumber = req.query.state

    let accessToken

    const tokenHeaders = new Headers()
    tokenHeaders.append("Content-Type", "application/x-www-form-urlencode")
    tokenHeaders.append("Authorization", `Basic ${appCredentials}`)
    const tokenRequestBody = JSON.stringify({
        "grant_type": "authorization_code",
        "code": code
    })
    const tokenRequestOptions = {
        method: "POST",
        headers: tokenHeaders,
        body: tokenRequestBody
    }
    fetch("https://opengateway.aggregator.com/token", tokenRequestOptions)
        .then(response => response.json())
        .then(result => {
            accessToken = result.access_token
        })
})

app.listen(port, () => {
    console.log(`SIM Swap callback URL is running`);
})
```

#### API usage

Once your app is authenticated it only takes a single line of code to use the service API and effectively get a result.

```python Sandbox SDK for Python
result = await simswap_client.retrieve_date(phone_number)

print(f"SIM was swapped: {result.strftime('%B %d, %Y, %I:%M:%S %p')}")
```
```python Sample SDK for Python
result = await simswap_client.retrieve_date(phone_number)

print(f"SIM was swapped: {result.strftime('%B %d, %Y, %I:%M:%S %p')}")
```
```node Sandbox SDK for Node.js
let result = await simswapClient.retrieveDate(phoneNumber)

console.log(`SIM was swapped: ${result.toLocaleString('en-GB', { timeZone: 'UTC' })}`)
```
```node Sample SDK for Node.js
let result = await simswapClient.retrieve_date(phoneNumber)

console.log(`SIM was swapped: ${result.toLocaleString('en-GB', { timeZone: 'UTC' })}`)
```
```python Sample HTTP using Python
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {access_token}"
}
data = {
    "phoneNumber": phone_number
}
response = requests.post(
    "https://opengateway.aggregator.com/sim-swap/v0/retrieve-date",
    headers=headers,
    json=data
)
result = response.json().get("latestSimChange")

print(f"SIM was swapped: {result.strftime('%B %d, %Y, %I:%M:%S %p')}")
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

fetch("https://opengateway.aggregator.com/sim-swap/v0/retrieve-date", requestOptions)
  .then(response => response.json())
  .then(result => {
    const verified = result.latestSimChange
    
    console.log(`SIM was swapped: ${result.toLocaleString('en-GB', { timeZone: 'UTC' })}`)
  })
```
