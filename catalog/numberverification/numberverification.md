---
title: Number Verification API
excerpt: The Number Verification API is a pivotal tool for bolstering security and reliability in your applications. In today's digital landscape, verifying the authenticity of phone numbers is paramount for safeguarding against fraud and ensuring seamless user interactions. The Number Verification API offers a streamlined solution to validate phone numbers in real-time, empowering developers to implement robust identity verification mechanisms with ease.
category: 6810d7141058bd00184cf1b4
version: 0
---

Built as part of the Open Gateway initiative, the Number Verification API provides developers universal access to essential network functionalities. Whether you're enhancing user registration processes, securing transactions, or optimizing user engagement strategies, integrating the Number Verification API enriches your application's security posture while ensuring a seamless user experience.

> 📘 Want to give it a try?
> Apply to join the [Developer Hub](https://opengateway.telefonica.com/en/developer-hub/join) and gain access to our Sandbox.

### Getting started on the Telefónica Open Gateway Sandbox
[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FFUQGNlMwYSg%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DFUQGNlMwYSg&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FFUQGNlMwYSg%2Fhqdefault.jpg&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen; encrypted-media; picture-in-picture;\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=FUQGNlMwYSg",
"title": "Smoother Identity Validations with the Number Verification API",
  "favicon": "https://www.youtube.com/favicon.ico",
  "image": "https://i.ytimg.com/vi/FUQGNlMwYSg/hqdefault.jpg",
  "provider": "https://www.youtube.com/",
  "href": "https://www.youtube.com/watch?v=FUQGNlMwYSg",
  "typeOfEmbed": "youtube"
}
[/block]

## Overview of the Number Verification CAMARA API

### High level definition

The Number Verification CAMARA API validates user identity by confirming ownership of the phone number being registered, matching it with the number identified by the operator through the user’s device connection.

### API Operations

The Number Verification CAMARA API specifies the following two operations:

- **POST verify:** Determines if the provided phone number matches the one currently in use by the user (parameter `phoneNumber`). This operation is ideal for user authentication.

	[Check the API Reference](/reference/phonenumberverify-2)
  
- **GET device-phone-number:** Identifies the phone number currently associated with the user's device without requiring input, providing a straightforward way to retrieve this information.

	***Pending for availability***

The Number Verification CAMARA API enables developers to seamlessly integrate authentication mechanisms into their applications, enhancing the user experience and security. It can also be combined with other Open Gateway APIs focused on anti-fraud measures to further bolster security.

Integration with channel partners and service aggregators streamlines the incorporation of telco functionalities with additional security algorithms, backup authentication methods, or external data sources. This collaboration enhances service reliability and security, leveraging APIs like Device Location Verification or SIM SWAP within the Open Gateway framework.

##  Why Number Verification?
![NumberVerification Before](https://github.com/Telefonica/opengateway-developers-website/raw/main/catalog/numberverification/images/NV(1).png)

In today's digital landscape, verifying phone number ownership is critical to prevent identity fraud and secure online transactions. The Number Verification CAMARA API offers a reliable solution to **authenticate users by confirming their phone numbers**. This ensures that only legitimate users gain access to digital services, bolstering security measures and building trust among customers.

![NumberVerification After](https://github.com/Telefonica/opengateway-developers-website/raw/main/catalog/numberverification/images/NV(2).png)

### How does the Number Verification API help to facilitate authentication? 

The Number Verification API utilizes telco mechanisms to authenticate users seamlessly based on their device's connection to the network. This method contrasts with traditional authentication solutions by enhancing user convenience and security. Unlike manual processes or plain-text codes, network-based validation requires no user interaction, bolstering protection against unauthorized access.

This API verifies that the provided mobile phone number (MSISDN) matches the device initiating data communication, ensuring users interact with digital services from authenticated devices.


## General Informations

> ⚙️ Problem Solved ? 
>
> When you want to validate the user's digital identity.


> ⚙️ How it works 
>
> - Check if the registered phone number matches the number provided by the operator
> -  Excellent resource to reduce the number of steps when validating an application.


> ⚙️ Parameters sent in the request 
>
> - phoneNumber: “34612345678” (mobile phone number in the format - +551199999999)


> ⚙️ Data received in the response
>
> - POST 
>
>  {
>		"devicePhoneNumberVerified": true
>  }
>
> - GET
>
>	{
>		"devicePhoneNumber": "+34612345678"
>	}
>
>


