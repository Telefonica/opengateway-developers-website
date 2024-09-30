---
title: Device Status API
excerpt: The Device Status API makes it possible to check the roaming status of a specific SIM-based device by using events from the operators' network.
category: 66aa4f941e51e7000fa353ce
---

The standardised Device Status API provides the ability to check the roaming status of a given SIM-based device without identity theft or GPS.

This solution allows you to control resource management during international roaming in a more secure way.

## Overview of the Device Status API

### High level definition

The Device Status CAMARA API is a software interface that enables a requester to provide a mobile device identifier (such as MSISDN, IP, or an external identifier) and receive a response indicating whether the device is currently in roaming status.

### API Operations

The Device Status Camara API specifies one operation:

- **POST /roaming**: answers the question 'is the device in roaming?'

[Check the API Reference](/reference/getroamingstatus)

## Why Device Status?
![DeviceStatus](./images/DeviceStatus.jpg)

By integrating this API, you can elevate the user experience by enabling, for example, personalised offers on travel services and improve security by quickly identifying and addressing potentially fraudulent SIM card locations.

This API provides a streamlined solution for accessing network capabilities across various operators. By offering a single, standardized interface, it simplifies the integration process and reduces the complexity associated with managing multiple operator-specific APIs. This unified access not only saves development time and resources but also ensures consistent performance and reliability across different network environments. As a result, businesses can focus on delivering high-quality services without worrying about the underlying network intricacies.

### Improved User Experience

Device Status allows companies to offer personalized services. Travel apps, for instance, can use the data provided by the API to offer valuable information, such as currency exchange rates or recommendations for data packages to users traveling abroad. This enhances the user experience and strengthens customer loyalty.

### Cost Reduction

The information provided by Device Status enables the implementation of cost-saving strategies, the setting of data routing rules, and the notification of customers about more affordable roaming options. This helps companies reduce international roaming fees, enhancing their offering.

###  Fraud Prevention and Detection

By integrating this API, it's possible to generate fraud alerts to identify and mitigate suspicious activities. The API can automatically detect and respond to anomalies such as unusual changes in the location of a SIM, increasing app security and benefiting both developers and users.

### Ease of Integration

Since it is a standardized API, integration is straightforward and doesn’t require custom implementations for each carrier. This simplifies the development process and accelerates time to market.

### Unified Access to Telecom Functions

The standardized API provides uniform access to other telecom capabilities, such as detecting if a user is roaming, through a single interface. This ensures consistency and flexibility across different carriers and markets.