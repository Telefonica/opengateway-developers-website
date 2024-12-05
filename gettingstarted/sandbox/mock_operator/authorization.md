---
title: Athorization mock 
excerpt: Technical guide to the Mock Operator a safe and controlled space for developers to simulate and test API integrations effectively
category: 66d5624a492663000f4ed527
---

# CIBA Authorization (Backend Flow)


This document outlines the behavior of the Mock Operator for within the Open Gateway Sandbox. It describes the simulated responses for the **Client-Initiated Backchannel Authentication (CIBA)** flow and **Auth Code Flow** , focusing on authentication and authorization requests. 

The authorization process involves two steps. First, your application's backend sends an authorization POST request, identifying the end user as a subscriber of the operator. This step generates an authorization request ID, which will be required for the next phase.

In the second step, the authorization request ID obtained earlier is used to retrieve an access token. This is done by making a POST request to the token endpoint of the Channel Partner's API gateway.

For more information see [Backend authorization flow](https://developers.opengateway.telefonica.com/docs/backend)

---

## CIBA Authorization request 

The backend flow handles authentication via **client credentials**. Below are the possible scenarios:

### Missing Client Credentials

- **Status**: `401`
- **Description**: The request lacks the required client credentials.
- **Response**:

  ```json
  {
      "message": "Missing credentials"
  }
### Invalid Client Credentials

- **Status**: `401`  
- **Description**: The provided client credentials are invalid.  
- **Response**:  

  ```json
  {
      "message": "Invalid credentials"
  }
### Missing Purpose

- **Status**: `400`  
- **Description**: The `scope` parameter is missing in the request.  
- **Response**:  

  ```json
  {
      "message": "Missing purpose"
  }
### Invalid Purpose

- **Status**: `400`  
- **Description**: The `scope` provided is invalid or not recognized by the mock OB product catalog.  
- **Response**:  

  ```json
  {
      "message": "Invalid purpose"
  }
### Missing login hint

- **Status**: `400`  
- **Description**: The `login_hint` parameter is missing from the request.  
- **Response**:
  
  ```json
  {
      "message": "Missing login_hint"
  }
### Invalid login hint type

- **Status**: `400`  
- **Description**: The `login_hint` type does not match the required value of `"phone_number"`.  
- **Response**:  

  ```json
  {
      "message": "Invalid login_hint type",
      "description": "Valid type is 'phone_number'"
  }

### MSISDN in login hint with Phone Number Prefix (CIBA)

- **Status**: `404`  
- **Description**: The phone number in the `login_hint` ends with a 9, simulating a scenario where the number does not belong to the operator in the mock environment.  
- **Response**:  

  ```json
  {
      "message": "Phone number matches no line from the Mock operator",
      "description": "This is a mock response. Phone numbers ending in 9 simulate not belonging to the operator. Try another phone number for a successful response"
  }
### Purpose Scope with Explicit Consent (CIBA)

- **Status**: `200`  
- **Description**: When the legitimate basis for consent is explicit, the request is processed successfully, and an `auth_req_id` is generated. This is used to simulate the need for out-of-band end-user consent before issuing an access token.  
- **Response**:  

  ```json
  {
      "auth_req_id": "<random_generated_string_with_consent_flag_as_suffix>",
      "expires_in": 300,
      "interval": 2
  }
- **Explanation**: The auth_req_id should be recognized by the /token endpoint for further processing.
The consent flag is added to the generated string to simulate the out-of-band consent process.
The team (TL) determines the flagging strategy for this process. The flag is not necessarily a fixed suffix or pattern.


### Purpose Scope without Explicit Consent (CIBA)

- **Status**: `200`  
- **Description**: When the legitimate basis for consent is not explicit, the request proceeds with a generated `auth_req_id`, but without a consent URL.  
- **Response**: 
 
  ```json
  {
      "auth_req_id": "<random_generated_string>",
      "expires_in": 300,
      "interval": 2,
      "consent_url": null
  }


## CIBA token retrieval
This second request in the Authorization flow, retrieves an access token from the authorization code (frontend) or auth_req_id (backend)


### Missing `auth_req_id`
- **Status**: `400`  
- **Description**: The `auth_req_id` parameter is missing from the request.  
- **Response**:  
  ```json
  {
      "message": "Missing auth_req_id"
  }


### `auth_req_id` Matches `random_generated_string_with_consent_flag_as_suffix`

- **Status**: `403`  
- **Description**: The provided `auth_req_id` matches the string pattern that indicates end-user consent is required but not yet gathered out-of-band.  
- **Response**:  
  ```json
  {
      "message": "Pending end-user consent, to be gathered out-of-band"
  }

### `auth_req_id` Does Not Match `random_generated_string_with_consent_flag_as_suffix`

- **Status**: `200`  
- **Description**: The provided `auth_req_id` does not match the consent-required pattern, allowing the request to proceed successfully.  
- **Response**:  
  ```json
  {
      "access_token": "<random_generated_ciba_suffix>",
      "expires_in": 3599,
      "token_type": "Bearer",
      "scope": "<as_provided_in_request>"
  }
- **Explanation**:
The random_generated_ciba_suffix string allows the Service API to identify that the access token was obtained via backend authentication of the end-user as an OB subscriber using the CIBA flow.

### Invalid `auth_req_id` (Final Mock OB - Stateful)

- **Status**: `403`  
- **Description**: The provided `auth_req_id` does not match the one generated in the authorization request.  
- **Response**:  
  ```json
  {
      "message": "Invalid auth_req_id"
  }
### Invalid `auth_req_id` (LITE Mock OB - Stateless)

- **Status**: `403`  
- **Description**: The provided `auth_req_id` starts with `"invalid"`, simulating an invalid ID not obtained from the authorization request.  
- **Response**:  
  ```json
  {
      "message": "Invalid auth_req_id",
      "description": "This is a mock response. auth_req_id starting with 'invalid' simulates one not obtained from the authorization request. Try another one for a successful response"
  }
### Missing `grant_type`

- **Status**: `400`  
- **Description**: The `grant_type` parameter is missing from the request.  

- **Response**:  
  ```json
  {
      "message": "Missing grant_type"
  }
### Invalid `grant_type`

- **Status**: `400`  
- **Description**: The provided `grant_type` is not valid. Accepted values include:  
  - `urn:openid:params:grant-type:ciba`  
  - `authorization_code`  

- **Response**:  
  ```json
  {
      "message": "Invalid grant_type"
  }
