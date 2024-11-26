---
title: Device Swap API
excerpt: The Device Swap API from Open Gateway allows to check for device swaps on a mobile line for fraud prevention purposes
category: 66aa4f941e51e7000fa353ce
---

The Device Swap API performs real-time checks on the last Device Swap event, providing real-time information about whether the SIM card associated with a user's phone number has been transferred to a different physical device.

Device Swap information can be invaluable for enhancing security, fraud detection, and ensuring compliance with regulatory requirements in various applications, apart from providing useful information of device upgrade trends in user segments.

> 📘 Want to give it a try?
> Apply to join the [Developer Hub](https://opengateway.telefonica.com/en/developer-hub) and gain access to our Sandbox.

## Overview of the Device Swap API

### High level definition

The Device Swap API provides a programmable interface for developers and other users (capabilities consumers) to request the last date of a device swap performed on the mobile line, or, to check whether a device swap has been performed during a past period.

### API Operations

The Device Swap CAMARA API specifies the following two operations:

- **POST retrieve-date:** Provides timestamp of latest device swap for a given phone number. If no device swap has been performed, the API will return the first phone number usage in the device (the timestamp of the first time that the phone number was connected to the network, it is, the first time that the SIM is installed in the device) by default. It will return an empty string in case is not possible to retrieve the date (e.g. in case local regulations are preventing the safekeeping of the information for longer than the stated period, or in some edge error cases). In case no data is available in the operators records (e.g. no recorded event), API will return a 422 error.

  [Check the API Reference](/reference/retrievedeviceswapdate)

- **POST check:** Checks if device swap has been performed during a past period (defined in the request with 'maxAge' attribute) for a given phone number, the API will return boolean response (true/false), indicating that the device has been swapped or not in the specified period. In case the phone number has never been installed in a device, or no data is available in the operators records (e.g. database error), API will return a 422 error.

  [Check the API Reference](/reference/checkdeviceswap)