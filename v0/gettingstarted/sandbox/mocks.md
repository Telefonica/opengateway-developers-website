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
| **device** missing or invalid | 400           | message: <error details>          |
| **device** > **ipv4Address** > **publicPort** missing when device = ipv4Address  | 400           | message: "Missing publicPort" 		|
| device > **networkAccessIdentifier** / **phoneNumber** / **ipv4Address** / **ipv6Address** ends in **9**  | 409           | code: "CONFLICT"<br>message: "Another session is created for the same UE"         |
| **applicationServer** missing or invalid | 400           | message: error on IPv4/IPv6 format          |
| **qosProfile** missing or invalid | 400           | message: error on QoS profile not listed in the GET profiles operation          |
| **duration** Not in range **1...86400** seconds | 400           | message: error on duration not in range          |
| Valid input | 201           | Provided input adding: sessionId, startedAt, expiresAt, qosStatus, messages        |