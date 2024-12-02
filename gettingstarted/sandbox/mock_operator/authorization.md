---
title: Athorization mock 
excerpt: Technical guide to the Mock Operator a safe and controlled space for developers to simulate and test API integrations effectively
category: 66d5624a492663000f4ed527
---

# Mock Operator Documentation


This document outlines the behavior of the Mock Operator for within the Open Gateway Sandbox. It describes the simulated responses for the **Client-Initiated Backchannel Authentication (CIBA)** flow and **Auth Code Flow** , focusing on authentication and authorization requests. 

---

## CIBA Authentication (Backend Flow)

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




