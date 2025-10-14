---
title: Device Swap API
category:
  uri: API Catalog
content:
  excerpt: >-
    The Device Swap API from Open Gateway allows to check for device swaps on a
    mobile line for fraud prevention purposes
---

The Device Swap API performs real-time checks on the last Device Swap event, providing real-time information about whether the SIM card associated with a user's phone number has been transferred to a different physical device.

Device Swap information can be invaluable for enhancing security, fraud detection, and ensuring compliance with regulatory requirements in various applications, apart from providing useful information of device upgrade trends in user segments.

> 📘 Want to give it a try?
> Apply to join the [Developer Hub](https://opengateway.telefonica.com/en/developer-hub/join) and gain access to our Sandbox.

## Overview of the Device Swap API

### High level definition

The Device Swap API provides a programmable interface for developers and other users (capabilities consumers) to request the last date of a device swap performed on the mobile line, or, to check whether a device swap has been performed during a past period.

### API Operations

The Device Swap CAMARA API specifies the following two operations:

- **POST retrieve-date:** Provides timestamp of latest device swap for a given phone number. If no device swap has been performed, the API will return the first phone number usage in the device (the timestamp of the first time that the phone number was connected to the network, it is, the first time that the SIM is installed in the device) by default. It will return an empty string in case is not possible to retrieve the date (e.g. in case local regulations are preventing the safekeeping of the information for longer than the stated period, or in some edge error cases). In case no data is available in the operators records (e.g. no recorded event), API will return a 422 error.

  [Check the API Reference](/reference/retrievedeviceswapdate-3)

- **POST check:** Checks if device swap has been performed during a past period (defined in the request with 'maxAge' attribute) for a given phone number, the API will return boolean response (true/false), indicating that the device has been swapped or not in the specified period. In case the phone number has never been installed in a device, or no data is available in the operators records (e.g. database error), API will return a 422 error.

  [Check the API Reference](/reference/retrievedeviceswapdate-3)

## Why Device Swap?

With the Device Swap Open Gateway API, any digital service provider can integrate the functionality of detecting changes in device usage directly into their software. This can be done both alone and in combination with other external inputs. Additionally, they can leverage other Open Gateway APIs related to anti-fraud measures that may be of interest.

Aggregators play a crucial role in the anti-fraud industry. They can integrate this functionality into their software and build more sophisticated algorithms by combining other security checks, such as SIM Swap detection, device location verification, phone number validation, external data sources, AI-based fraud detection, and behavioral analysis. To achieve this, aggregators can use other Open Gateway APIs like SIM Swap, Device Location Verification, Number Verification, or KYC-Match.By using the Device Swap Open Gateway API, developers can significantly enhance the security and reliability of their applications, providing a robust defense against unauthorized device usage and fraud.

![DeviceSwap](https://github.com/Telefonica/opengateway-developers-website/raw/main/v0/catalog/deviceswap/images/DeviceSwap.png)

### Understanding Device Swap Fraud

Device Swap fraud is a growing security risk that enables unauthorized access to user accounts. Your mobile phone is a critical tool for managing various services, from banking and insurance to shopping and communication. Many of these services rely on device-based authentication to verify user identity and authorize transactions.

Unauthorized device changes pose a serious threat to account security. When a fraudster inserts a SIM into a new device, they can bypass security checks tied to trusted devices. This allows them to take over accounts, approve fraudulent transactions, or gain access to sensitive information. Beyond financial loss, this type of fraud can lead to identity theft, data breaches, and reputational damage for businesses and individuals alike.

### How Device Swaps Are Used by Telecom Operators

A mobile device is identified by a unique number called the IMEI, which telecom operators link to your phone number. If your phone number is used in a different device, this change is recorded and can indicate legitimate usage or potential unauthorized access.

This is where Device Swap fraud becomes a security risk. When a fraudster inserts a SIM into a new device, they can bypass authentication systems that rely on trusted devices. This can allow them to take over accounts, approve fraudulent transactions, or access sensitive data without detection.

### Protecting Against Device Swap Fraud

To mitigate the risks of Device Swap fraud, businesses must adopt real-time monitoring of device changes. Security measures such as verifying device consistency, implementing adaptive authentication, and leveraging APIs like Device Swap Detection can help detect unauthorized changes before damage occurs.

By understanding how Device Swap fraud works and integrating proactive security measures, companies and individuals can reduce the risk of account takeovers, identity theft, and financial fraud.
