---
title: Sandbox mock responses
excerpt: Get deterministic responses from our Sandbox environment when using the mock mode, according to the following guidelines.
category: 680a72d37e7640001804095b
---

## Using the Sandbox on mock mode

You can use the Sandbox environment in mock mode to get deterministic responses. This is useful for testing and development purposes, as it allows you to simulate API responses without making requests from an actual mobile device.

[Learn more about usage modes](/docs/sandbox#usage-modes)

## Mock responses

When using the Sandbox in mock mode, the following rules apply:

### Number Verification

| Input | Response Status | Response Body |
|--------------|--------------------|------------------|
| **phoneNumber** ends in **1**  | 200           | devicePhoneNumberVerified: **true**          |
| **phoneNumber** ends in **2**  | 200           | devicePhoneNumberVerified: **false**          |
| **phoneNumber** ends in **3...0**  | 200           | devicePhoneNumberVerified: random (depends on request timestamp being even or odd)          |

### QoD (v0.10) create session

| Input | Response Status | Response Body |
|--------------|--------------------|------------------|
| device > **networkAccessIdentifier** / **phoneNumber** / **ipv4Address** / **ipv6Address** ends in **9**  | 409           | code: "CONFLICT"<br>message: "Another session is created for the same UE"         |
| **duration** Not in range **1...86400** seconds | 400           | message: error on duration not in range          |
| Valid input | 201           | Provided input adding: sessionId, startedAt, expiresAt, qosStatus, messages        |

### SIM Swap

Check operation

| Input | Response Status | Response Body |
|--------------|--------------------|------------------|
| **phoneNumber** ends in **1**  | 200           | simSwapped: **true**          |
| **phoneNumber** ends in **2**  | 200           | simSwapped: **false**          |
| **phoneNumber** ends in **3...0**  | 200           | simSwapped: random (depends on request timestamp being even or odd)          |

Retrieve date

| Input | Response Status | Response Body |
|--------------|--------------------|------------------|
| **phoneNumber** ends in **9**  | 409           | code: "CONFLICT"<br>message: "Another request is created for the same phone number"          |
| **phoneNumber** ends in **0...8**  | 200           | latestSimChange: "2024-01-14T13:16:33.167Z"          |

### Device Location Verification (v0.2)

| Input | Response Status | Response Body |
|--------------|--------------------|------------------|
| **device** > **networkAccessIdentifier** / **phoneNumber** / **ipv4Address** / **ipv6Address** ends in **4**  | 404           | message: Device not found          |
| **maxAge** included and > 14400 | 404           | message: Device not found in the given maxAge          |
| **maxAge** not included<br>**center** > **latitude** round to integer ends in **0**  | 200           | verificationResult: **"UNKNOWN"**          |
| **maxAge** included<br>**center** > **latitude** round to integer ends in **0**  | 200           | verificationResult: **"UNKNOWN"**<br>lastLocationTime: (30 minutes + maxAge) to now          |
| **center** > **latitude** round to integer ends in **1**  | 200           | verificationResult: **"PARTIAL"**<br>lastLocationTime: (30 minutes + maxAge) to now<br>matchRate: something between 50 if radius=2 and 99 if radius=200          |
| **center** > **latitude** round to integer is **even** | 200           | verificationResult: **"TRUE"**          |
| **center** > **latitude** round to integer is **odd** | 200           | verificationResult: **"FALSE"**          |

### Device Status (v0.4)

| Input | Response Status | Response Body |
|--------------|--------------------|------------------|
| **ueId** > **externalId** / **msisdn** / **ipv4addr** / **ipv6addr** ends in **1**  | 200           | roaming: **true**          |
| **ueId** > **externalId** / **msisdn** / **ipv4addr** / **ipv6addr** ends in **2**  | 200           | roaming: **false**          |
| **ueId** identifier ends in **3...0**  | 200           | roaming: random (depends on request timestamp being even or odd)          |

### Know Your Customer (KYC) Match (v0.2)

| Input | Response Status | Response Body |
|--------------|--------------------|------------------|
| Any invalid input | 400           | message: Details on the invalid input value          |
| Valid input | 200           | For every input value, response includes...<br>match: boolean<br>matchScore: 0...100 (only for some keys)<br>Those will be the result of matching the request data with a [mock user persona](https://github.com/camaraproject/KnowYourCustomer/blob/a2575b08550640999614a43dd2146ceab6b6e469/code/API_definitions/kyc-match.yaml#L105)          |

### KYC Age Verification (v0.1)

For this API, the rules's input is the **login_hint** parameter, which is used to retrieve the access token used to authenticate the request (not directly as a request parameter). The response will be based on the last digit of the **login_hint**.

It will determine which mock user persona is used to verify the age of the user, by comparing the **ageThreshold** in the request body with the user's age.

| Input | Response Status | Response Body |
|--------------|--------------------|------------------|
| login_hint is **even**  | 200           | ageCheck: Result of verifying the **ageThreshold** for a mock user born in **June 10th, 2004**          |
| login_hint is **odd**  | 200           | ageCheck: Result of verifying the **ageThreshold** for a mock user born in **January 31st, 1971**          |

### KYC Tenure (v0.1)

For this API, the rules's input is the **login_hint** parameter, which is used to retrieve the access token used to authenticate the request (not directly as a request parameter). The response will be based on the last digit of the **login_hint**.

It will determine which mock user persona is used to verify the line holding tenure, by comparing the **tenureDate** in the request body with the user's tenure.

| Input | Response Status | Response Body |
|--------------|--------------------|------------------|
| login_hint is **even**  | 200           | tenureDateCheck: Result of verifying the **tenureDate** for a mock user with a tenure start date of **April 30th, 2025**         |
| login_hint is **odd**  | 200           | tenureDateCheck: Result of verifying the **tenureDate** for a mock user with a tenure start date of **December 30th, 2023**          |

### Scam Signal (v0.2)

| Input | Response Status | Response Body |
|--------------|--------------------|------------------|
| **phoneNumber** is **even**  | 200           | callInProgress: **false**          |
| **phoneNumber** is **odd**  | 200           | callInProgress: **true**<br>callStartTime: "2023-07-03T12:27:08.312Z"          |