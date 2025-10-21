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

<div style="display: flex; gap: 8px; margin-bottom: 15px;">
  <span style="background-color: #f0f0f0; border: 1px solid #ccc; border-radius: 15px; padding: 4px 12px; font-size: 12px; font-weight: bold; color: #666;">Under CAMARA project</span>
  <span style="background-color: #8a8a8a; color: white; border-radius: 15px; padding: 4px 12px; font-size: 12px; font-weight: bold;">GSMA Certified API</span>
</div>

Built as part of the Open Gateway initiative, the Number Verification API provides developers with universal access to essential network functionalities. Whether you're enhancing user registration processes, securing transactions, or optimizing user engagement strategies, integrating the Number Verification API enriches your application's security posture while ensuring a seamless user experience.

> 📘 Want to give it a try?
> Apply to join the [Developer Hub](https://opengateway.telefonica.com/en/developer-hub/join) and gain access to our Sandbox.

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

## Overview of the Number Verification CAMARA API

### High level definition

The Number Verification CAMARA API validates user identity by confirming ownership of the phone number being registered, matching it with the number identified by the operator through the user’s device connection.

### API Operations

The Number Verification CAMARA API specifies the following two operations:

- **POST verify:** Determines if the provided phone number matches the one currently in use by the user (parameter `phoneNumber`). This operation is ideal for user authentication.

	[Check the API Reference](/reference/phonenumberverify-2)
  
- **GET device-phone-number:** Identifies the phone number currently associated with the user's device without requiring input, providing a straightforward way to retrieve this information.

	***This feature is pending availability***

The Number Verification CAMARA API enables developers to seamlessly integrate authentication mechanisms into their applications, enhancing the user experience and security. It can also be combined with other Open Gateway APIs focused on anti-fraud measures to further bolster security.

Integration with channel partners and service aggregators streamlines the incorporation of telco functionalities with additional security algorithms, backup authentication methods, or external data sources. This collaboration enhances service reliability and security, leveraging APIs like Device Location Verification or SIM SWAP within the Open Gateway framework.

## Why Number Verification?
![NumberVerification Before](https://github.com/Telefonica/opengateway-developers-website/raw/main/v0/catalog/numberverification/images/NV(1).png)

In today's digital landscape, verifying phone number ownership is critical to prevent identity fraud and secure online transactions. The Number Verification CAMARA API offers a reliable solution to **authenticate users by confirming their phone numbers**. This ensures that only legitimate users gain access to digital services, bolstering security measures and building trust among customers.

![NumberVerification After](https://github.com/Telefonica/opengateway-developers-website/raw/main/v0/catalog/numberverification/images/NV(2).png)

### How does the Number Verification API help facilitate authentication? 

The Number Verification API utilizes telco mechanisms to authenticate users seamlessly based on their device's connection to the network. This method contrasts with traditional authentication solutions by enhancing user convenience and security. Unlike manual processes or plain-text codes, network-based validation requires no user interaction, bolstering protection against unauthorized access.

This API verifies that the provided mobile phone number (MSISDN) matches the device initiating data communication, ensuring users interact with digital services from authenticated devices.
