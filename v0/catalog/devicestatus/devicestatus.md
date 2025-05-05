---
title: Device Status API
excerpt: The Device Status API makes it possible to check the roaming status of a specific SIM-based device by using events from the operators' network.
category: 681879c3afc1a0003709c745
---

The standardised Device Status API provides the ability to check the roaming status of a given SIM-based device without identity theft or GPS.

This solution allows you to control resource management during international roaming in a more secure way.

![DeviceStatus](https://github.com/Telefonica/opengateway-developers-website/raw/main/v0/catalog/devicestatus/images/DeviceStatus.png)

> 📘 Want to give it a try?
> Apply to join the [Developer Hub](https://opengateway.telefonica.com/en/developer-hub/join) and gain access to our Sandbox.

### Getting started on the Telefónica Open Gateway Sandbox
[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2F58KzlZHICtY%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D58KzlZHICtY&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2F58KzlZHICtY%2Fhqdefault.jpg&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen; encrypted-media; picture-in-picture;\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=58KzlZHICtY",
  "title": "Reducing Digital Risk with the Device Status API",
  "favicon": "https://www.youtube.com/favicon.ico",
  "image": "https://i.ytimg.com/vi/58KzlZHICtY/hqdefault.jpg",
  "provider": "https://www.youtube.com/",
  "href": "https://www.youtube.com/watch?v=58KzlZHICtY",
  "typeOfEmbed": "youtube"
}
[/block]

## Overview of the Device Status API

### High level definition

The Device Status CAMARA API is a software interface that enables a requester to provide a mobile device identifier (such as MSISDN, IP, or an external identifier) and receive a response indicating whether the device is currently in roaming status.

### API Operations

The Device Status Camara API specifies one operation:

- **POST /roaming**: answers the question 'is the device in roaming?'

[Check the API Reference](/reference/getroamingstatus-2)

## Why Device Status?

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
