---
title: How to use the API reference
excerpt: Find out how to start testing the Open Gateway APIs with our tools in the API Reference
category: 66d5624a492663000f4ed527
---

An API reference is a comprehensive document that provides detailed information about an API (Application Programming Interface), including how to use its functions, methods, endpoints, parameters, and data structures. It serves as a guide for developers who want to integrate or interact with the API in their applications.

In our developers’ website, you will find also a simple tool that uses your real credentials to make test calls.

>📘 Note
>
> If you do not have credentias, you can [create an application in the Sandbox](https://opengateway.telefonica.com/developer-hub) and sign up.

## Before getting started
### Purposes
Each API has a string called “purpose” that defines the intended use of that API. This is a predefined string, and it is necessary to specify it in order to obtain the first part of the credential authentication:
- <u>SIM Swap</u>: dpv:FraudPreventionAndDetection#sim-swap
- <u>Number Verification</u>: dpv:FraudPreventionAndDetection#number-verification-verify-read
- <u>Device Location Verification</u>: dpv:FraudPreventionAndDetection#device-location-read
- <u>Device Status</u>: dpv:FraudPreventionAndDetection#device-status-roaming-read

## Config the API Reference step by step
### Step 1: Get the authorization code
For a faster and easier authorization it is recomended to use a [CIBA](../about/glossary.md). This CIBA is going to authorize an application to access a resource from the backend:
- <u>login_hint</u>: The phone number you own and provided when creating your application. If you are using [the Sandbox](https://sandbox.opengateway.telefonica.com/my-apps), it is the number you provided when requesting access to production. If your application is a mock, you can enter any invented number that does not end with 9. The sintax is <id_type>:<id_value> (tel:+34666555432)
- <u>purpose</u>: The purpose string for the API you want to call. You can check the purpose by clicking on one of the test calls in this API reference. If not, you have a list in the *Before Getting Started* section of this page.
- <u>credentials</u>: The username is your client_id and your password is you client_secret. You can get both from the info in your aplication. If you are using [a Sandbox app](https://sandbox.opengateway.telefonica.com/my-apps) you have this information in My Apps page, clicking in your app.

When finished, you page will look similar to the image below.
![CIBA Auth example](https://github.com/Telefonica/opengateway-developers-website/raw/main/gettingstarted/images/CIBA%20auth.png)

### Step 2: Get the access token
For this step, go to the [*Retrieve an access token*](https://developers.opengateway.telefonica.com/reference/token) secction. Because this tutorial is using the CIBA, you must copy the authorization code in the *ACCESSTOKENCIBAREQUEST* tab:
- <u>grant_type</u>: Select the option *urn:openid:params:ggrant-type:ciba*
- <u>auth_req_id</u>: The *auth_req_id* you get in response of the last step

When finished, you page will look similar to the image below.
![CIBA Auth example](https://github.com/Telefonica/opengateway-developers-website/raw/main/gettingstarted/images/Access%20token.png)

### Step 3: Make your calls
The API Reference is now prepared to make calls to the Open Gateway's APIs. Check that the credentials you made are just for one API because of the purpose. Everytime you change the API you are consuming, you must change the purpose.
The variable common to all APIs is the *access_token* you get in response of the last step, which should be placed in the authentication section.

![CIBA Auth example](https://github.com/Telefonica/opengateway-developers-website/raw/main/gettingstarted/images/SIM%20Swap%20call.png)
