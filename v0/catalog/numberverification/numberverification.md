---
title: Number Verification API
category:
  uri: API Catalog
content:
  excerpt: >-
    The Number Verification API is a pivotal tool for bolstering security and
    reliability in your applications. In today's digital landscape, verifying
    the authenticity of phone numbers is paramount for safeguarding against
    fraud and ensuring seamless user interactions. The Number Verification API
    offers a streamlined solution to validate phone numbers in real-time,
    empowering developers to implement robust identity verification mechanisms
    with ease.
---

<div style={{display: 'flex', gap: '8px', marginBottom: '15px'}}>
  <span style={{backgroundColor: '#f0f0f0', border: '1px solid #ccc', borderRadius: '15px', padding: '4px 12px', fontSize: '12px', fontWeight: 'bold', color: '#666'}}>Under CAMARA project</span>
  <span style={{backgroundColor: '#8a8a8a', color: 'white', borderRadius: '15px', padding: '4px 12px', fontSize: '12px', fontWeight: 'bold'}}>GSMA Certified API</span>
</div>

The Number Verification API is part of the Open Gateway initiative, providing developers with access to network-based phone number validation. This API verifies user identity by confirming phone number ownership through network operator mechanisms, eliminating the need for manual verification processes.

Apply to join the [Developer Hub](https://opengateway.telefonica.com/en/developer-hub/join) and gain access to our Sandbox.

### Getting started on the Telefónica Open Gateway Sandbox

<iframe  
  width="560"  
  height="315"  
  src="https://www.youtube.com/embed/FUQGNlMwYSg?si=tC_C2oS44YjSS_lw"  
  title="YouTube video player"  
  frameborder="0"  
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"  
  referrerpolicy="strict-origin-when-cross-origin"  
  allowfullscreen>
</iframe>

## API Overview

### Technical Definition

The Number Verification CAMARA API validates user identity by confirming that the provided phone number matches the number associated with the user's device connection to the mobile network operator.

### Available Operations

- **POST verify:** Validates if the provided phone number matches the device's registered number. Returns a boolean result indicating verification status.

	[Check the API Reference](/reference/phonenumberverify-2)
  
- **GET device-phone-number:** Retrieves the phone number associated with the user's device without requiring input parameters.

	***This feature is pending availability***

### Technical Implementation

The API leverages network operator infrastructure to perform verification without requiring user interaction. This network-based approach provides:

- Real-time validation against operator records
- No dependency on SMS or voice calls
- Transparent verification process for end users
- Integration with existing network authentication mechanisms

The API can be combined with other Open Gateway APIs such as Device Location Verification or SIM SWAP detection to create comprehensive security solutions.

## Use Cases and Benefits

Phone number verification addresses critical security requirements in digital services. Traditional verification methods using SMS or voice calls are vulnerable to SIM swapping, interception, and social engineering attacks.

![NumberVerification Before](https://github.com/Telefonica/opengateway-developers-website/raw/main/v0/catalog/numberverification/images/NV(1).png)

The Number Verification API provides network-level authentication that validates phone number ownership through the mobile operator's infrastructure, offering superior security compared to conventional methods.

![NumberVerification After](https://github.com/Telefonica/opengateway-developers-website/raw/main/v0/catalog/numberverification/images/NV(2).png)

For desktop applications, the Number Verification API supports cross-device authentication through QR code scanning, enabling users to verify their phone number from their mobile device while using a desktop application.

![NumberVerification Desktop](https://github.com/Telefonica/opengateway-developers-website/raw/main/v0/catalog/numberverification/images/NV(3).png)

### Key Advantages

**Network-Based Verification:** Utilizes the mobile network operator's authentication mechanisms, providing verification without user interaction or exposure to interception.

**Real-Time Validation:** Immediate confirmation of phone number ownership through active network connection verification.

**Enhanced Security:** Eliminates vulnerabilities associated with SMS-based verification, including SIM swapping and message interception.

**Seamless Integration:** RESTful API design enables straightforward integration into existing authentication workflows.

The API verifies that the provided mobile phone number (MSISDN) corresponds to the device establishing the data connection, ensuring users access services from authenticated devices.
