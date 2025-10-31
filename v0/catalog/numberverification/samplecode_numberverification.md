---
title: Sample code for Number Verification
category:
  uri: API Catalog
content:
  excerpt: >-
    The following samples show how to use the [Open Gateway Number Verification
    API](https://opengateway.telefonica.com/en/apis/number-verification), for
    fraud prevention purposes, in order to check if a given phone number matches
    the one on the SIM card installed in the end-user's device.
---

## Implementation Architecture

The Number Verification API uses a **frontend-initiated, backend-completed** authentication flow:

- **Frontend starts**: The verification request must originate from the user's mobile device to establish network identity
- **Backend completes**: The authentication flow concludes on your backend server for security reasons (protecting client credentials)

This split architecture ensures both network-based verification and secure credential management.

## SDK vs HTTP Implementation

**Channel Partner SDKs**: Most aggregators provide SDKs that simplify authentication and API calls. Some offer both frontend and backend SDKs, with frontend SDKs handling network interface switching for proper mobile line identification.

**Direct HTTP Calls**: You can also consume the API directly using HTTP requests. This approach requires manual handling of credential encoding, authorization endpoints, and token management. Reference our [Postman collection](https://github.com/Telefonica/opengateway-postman) for HTTP examples.

> 📘 Want to give it a try before coding?
> Check the [API interactive reference](https://developers.opengateway.telefonica.com/reference/phonenumberverify)

### Table of contents
- [Frontend](#frontend)
    - [Requesting the authorization code from the frontend](#requesting-the-authorization-code-from-the-frontend)
- [Backend](#backend)
    - [Getting the access token from the callback endpoint at the backend](#getting-the-access-token-from-the-callback-endpoint-at-the-backend)
    - [Using the service API](#using-the-service-api)

## Code samples

**Important Notes:**
- Replace `my-app-id` and `my-app-secret` with your actual application credentials
- If using our Sandbox, retrieve credentials [here](https://sandbox.opengateway.telefonica.com/my-apps)
- Replace `aggregator/opengateway-sdk` with your aggregator's actual SDK package name
- For our Sandbox SDK, check installation details [here](/docs/sdkreference)

### Frontend

#### Why the Frontend Must Initiate the Flow

The Number Verification API must start from the end-user's device because:
- **Network Identity**: The mobile operator needs to identify which SIM card/phone number is making the request
- **Device Context**: Verification works by confirming the phone number matches the device's active mobile connection
- **Security**: The network-based authentication happens through the user's actual mobile data connection

#### Frontend Flow Steps

1. **Initiate Request**: Your frontend application makes an authorization request to the mobile operator
2. **Provide Callback**: You specify a `redirect_uri` (your backend callback URL) where the operator will send the authorization code
3. **Handle Redirect**: The mobile operator redirects to your callback URL with an authorization code
4. **Backend Processing**: Your backend receives the code and completes the token exchange (see [Backend](#backend) section)

**Important**: The `redirect_uri` must point to your backend server, not your frontend application, because:
- The authorization code must be securely exchanged for an access token using your client secret
- Client secrets should never be exposed in frontend code for security reasons

The authentication protocol used in Open Gateway for frontend flows is the OIDC standard Authorization Code Flow. You can check the CAMARA documentation on this flow [here](https://github.com/camaraproject/IdentityAndConsentManagement/blob/release-0.1.0/documentation/CAMARA-API-access-and-user-consent.md#authorization-code-flow-frontend-flow).

#### Requesting the authorization code from the frontend

The following samples show how your application can trigger the authentication flow from the frontend either from code or by submitting a simple HTML form. The same can be achieved from code in any other programming language with the ability to perform HTTP requests:
```javascript HTTP using JavaScript (ES6)
let userPhoneNumber = "+34555555555";

let clientId = "my-app-id";
let clientSecret = "my-app-secret";
let apiScope = "dpv:FraudPreventionAndDetection#number-verification-verify-read";
let myCallbackEndpoint = "https://my_app_server/numberverification-callback";

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
    <h1>Number verification</h1>
    <form id="apiRequestForm" action="https://opengateway.aggregator.com/authorize" method="GET">
        <input type="hidden" name="client_id" value="my-app-id">
        <input type="hidden" name="response_type" value="code">
        <input type="hidden" name="scope" value="dpv:FraudPreventionAndDetection#number-verification-verify-read">
        <input type="hidden" name="redirect_uri" value="/numberverification-callback">
        
        <label for="state">Your phone number:</label>
        <input type="text" id="state" name="state" value="+34555555555" required>
        
        <button type="submit">Verify</button>
    </form>
</body>
</html>
```

### Backend

#### Understanding the Callback URL Requirement

The Number Verification API uses the OAuth 2.0 Authorization Code Flow for security purposes. Here's why a callback URL is essential:

**Why a callback URL is needed:**
- **Security**: Your app's credentials (client secret) must remain secure and never be exposed to the frontend/browser
- **Token Exchange**: The authorization code received from the mobile operator must be exchanged for an access token on your secure backend
- **Network Verification**: The mobile operator needs to redirect back to your application after verifying the user's network connection

**How the callback URL works:**
1. Your frontend initiates the verification request
2. The user's device connects to the mobile operator for network-based authentication
3. The operator redirects back to your `redirect_uri` (callback URL) with an authorization code
4. Your backend receives this code and exchanges it securely for an access token
5. The access token is then used to call the verification API

The callback URL must be a publicly accessible endpoint on your backend server that can handle HTTP GET requests with query parameters.

#### Getting the access token from the callback endpoint at the backend

Samples represent how to publish the callback URL in Python or Node.js, so the code from the Auth Code Flow can be received. The same can be achieved in any other language with capabilities to run an HTTP server and listen for the redirect from the authentication flow:

```python Sandbox SDK for Python
from flask import Flask, request
from opengateway_sandbox_sdk import ClientCredentials, NumberVerification

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
```node Sandbox SDK for Node.js
import sandboxSdk from '@telefonica/opengateway-sandbox-sdk'
const { NumberVerification } = sandboxSdk
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
    console.log(`Number verification callback URL is running`)
})
```
```python Sample SDK for Python
from flask import Flask, request
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
    console.log(`Number verification callback URL is running`)
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
let apiScope = "dpv:FraudPreventionAndDetection#number-verification-verify-read"

const app = express()
const port = 3000

app.get('/numberverification-callback', (req, res) => {
    const code = req.query.code
    const phoneNumber = req.query.state

    let accessToken

    const myHeaders = new Headers()
    myHeaders.append("Content-Type", "application/x-www-form-urlencoded")
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
    console.log(`Number verification callback URL is running`)
})

```

#### Using the service API

Once your app is authenticated it only takes a single line of code to use the service API and effectively get a result.

```python Sandbox SDK for Python
result = await api_client.verify(phone_number)

print(f"Phone number {'verified' if result else 'does not match mobile line'}")
```
```node Sandbox SDK for Node.js
let result = await apiClient.verify(phoneNumber)

console.log(`Phone number ${result ? "verified" : "does not match mobile line"}`)
```
```python Sample SDK for Python
result = await api_client.verify(phone_number)

print(f"Phone number {'verified' if result else 'does not match mobile line'}")
```
```node Sample SDK for Node.js
let result = await apiClient.verify(phoneNumber)

console.log(`Phone number ${result ? "verified" : "does not match mobile line"}`)
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
    "https://opengateway.aggregator.com/number-verification/v0/verify",
    headers=headers,
    json=data
)
result = response.json().get("devicePhoneNumberVerified")

print(f"Phone number {'verified' if result else 'does not match mobile line'}")
```
```node HTTP using Node.js
const myHeaders = new Headers()
myHeaders.append("Content-Type", "application/json")
myHeaders.append("Authorization", `Bearer ${accessToken}`)

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
