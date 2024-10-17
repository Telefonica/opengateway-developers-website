---
title: Device Location API
excerpt: The Device Location API from Open Gateway allows to check if a mobile phone is in a determined location.
category: 66aa4f941e51e7000fa353ce
---

> 📘 Note
>
> To try out our APIs, visit the [Sandbox](https://opengateway.telefonica.com/developer-hub/unirse).

The Device Location API is a software interface that allows applications to confirm if a user's device is in its intended location. The network must track a device's location at all times to effectively provide telecommunications services. This capability is utilized to offer device location as a service.

The Device Location API enhances security by verifying that a device is in the expected location during transactions, which helps prevent fraud and unauthorized activities. This verification process also streamlines authentication, leading to faster and smoother transactions, ultimately improving the user experience. 

Additionally, the API is a valuable tool for fraud prevention, as it can quickly detect and mitigate potential threats by identifying discrepancies between the claimed and actual device locations. It also helps businesses comply with regulatory requirements in industries where location verification is essential, such as finance and gaming. 
 
Furthermore, by knowing a user's location, businesses can offer more personalized and context-aware services, increasing customer engagement and satisfaction. The API's versatility makes it applicable across various industries, including retail, telecom, and logistics. For merchants, it also contributes to reducing chargebacks by verifying the location of a device during transactions.

![DeviceLocation](https://github.com/Telefonica/opengateway-developers-website/raw/main/catalog/devicelocation/images/DeviceLocation.png)

## Overview of the SIM Swap CAMARA API

### High level definition

The Device Location CAMARA API is a software interface that allows applications to confirm if a user’s device is in the expected location. For the network to deliver its telecommunications services effectively, it must be able to locate a device at any time. This capability is thus utilized to provide device location as a service.

### API Operations

The Device Location Camara API specifies one operation:

- **POST /verify**: answers the question ‘is the device in the circle determined by a center (latitude and longitude) and an accuracy (given in km as the radius of the circle)?’

[Check the API Reference](/reference/verifylocation-1)


## Why device location API

The standardised Device Location Verification API provides the option of verifying the geographical location of a given SIM-based device and validating whether it is within a requested geographical area without spoofing or GPS.

This solution validates the location of a device to enable services or allow transactions by verifying the location.

###  Fast and reliable location
The Device Location Verification API provides a swift and efficient way to validate customer locations, helping you maintain control over your application while enabling features like anti-fraud measures, personalization, and targeted advertising.

### Theft-free gps
Location verification is based on network data managed by telecom carriers, ensuring protection against device spoofing, GPS manipulation, or emulation.

###  Risk prevention
When combined with other APIs such as Number Verification, Device Swap, or Know Your Customer (KYC) Match, this API enhances service security, improves user experience, and reduces identity-related risks.

###  Simplified integration
As a standardized API, it allows seamless integration into your applications without the need for carrier-specific customizations, simplifying development and accelerating time to market.

###  Footprint for your identity service
The API's standardization ensures uniform access across multiple telecom providers, expanding your business reach and ensuring consistent functionality across different carriers.


## General Informations

> ⚙️ Problem Solved ? 
>
> When you want to know the location of a device.


> ⚙️ How it works 
>
> By providing latitude and longitude, it is checked whether the device is in that location.


> ⚙️ Parameters sent in the request 
>
> - msisdn (mobile phone number in the format - +551199999999) 
> - latitude (latitude in the format: -23.5042623 )
> - longitude (longitude in the format -46.8575631)
> - accuracy (precision of the data passed in km, put in the format: 2)


> ⚙️ Data received in the response
>
> If the device is not in place, it returns verificationResult: false . If the device is in the specified location, the value is verificationResult: true .

