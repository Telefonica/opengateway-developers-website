---
title: Know Your Customer API
excerpt: The Know Your Customer API makes it possible to validates users info with MNO (Mobile Network Operator) data, ensuring compliance and preventing identity fraud.
category: 681879c3afc1a0003709c745
---

The standardised Know Your Customer API allows you to validate user contact information against data from Mobile Network Operators (MNOs), ensuring accuracy and improving both conversion rates and the quality of user onboarding for new services.

This API provides a quick and efficient method to verify customer contact details, helping you prevent identity fraud, including synthetic identities and identity theft. Additionally, by utilizing this standardized API, you can expand your user reach across multiple MNOs.

> 📘 Want to give it a try?
> Apply to join the [Developer Hub](https://opengateway.telefonica.com/en/developer-hub/join) and gain access to our Sandbox.

### Getting started on the Telefónica Open Gateway Sandbox
[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FMmQK8dg1Poo%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DMmQK8dg1Poo&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FMmQK8dg1Poo%2Fhqdefault.jpg&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen; encrypted-media; picture-in-picture;\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=MmQK8dg1Poo",
"title": "Stronger Identity Authentications with the Know Your Customer-Match API",
  "favicon": "https://www.youtube.com/favicon.ico",
  "image": "https://i.ytimg.com/vi/MmQK8dg1Poo/hqdefault.jpg",
  "provider": "https://www.youtube.com/",
  "href": "https://www.youtube.com/watch?v=MmQK8dg1Poo",
  "typeOfEmbed": "youtube"
}
[/block]

## Overview of the Know Your Customer API

### High level definition

The Know Your Customer CAMARA API is a software interface that enables a requester to check if an user data is correct or not making a check with the mobile network operator records. 

### API Operations

The Know Your Customer Camara API specifies one operation:

- **POST /match**: answers the question 'is this informacion true?'

[Check the API Reference](/reference/kyc_match_v02-2)

## Why Know Your Customer?

This API provides a streamlined solution for accessing network capabilities across various operators. By offering a single, standardized interface, it simplifies the integration process and reduces the complexity associated with managing multiple operator-specific APIs. This unified access not only saves development time and resources but also ensures consistent performance and reliability across different network environments. As a result, businesses can focus on delivering high-quality services without worrying about the underlying network intricacies.

### Fraud prevention

Utilizing the KYC-Match API helps mitigate risks associated with your customers’ identities, including synthetic identity fraud and fraudulent transactions stemming from identity theft.

###  Conversion rate and ​high-quality users

The API enhances the conversion rate quality during customer onboarding. The API cross-references user-provided contact information with data from their respective Mobile Network Operators (MNOs), ensuring a highly reliable source of verification. Additionally, it strictly adheres to privacy regulations.

### Simplified Integration

By using a standardized API, you can effortlessly incorporate the KYC-Match process into your onboarding system without requiring custom implementations for each telecom operator. This streamlines development and accelerates your time-to-market.

### Footprint for your Identify Service​

The standardized API provides uniform access to multiple telecom companies, broadening your business reach and ensuring consistent and flexible operations across different providers.
