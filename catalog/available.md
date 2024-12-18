---
title: Available APIs
excerpt: The Open Gateway initiative is led to create a standardized framework of Application Programming Interfaces (APIs) that enables simplified and universal access to advanced mobile network capabilities and associated services. Designed to promote interoperability, innovation, and operational efficiency within the digital ecosystem, Open Gateway APIs are essential for modern application development.
category: 66aa4f941e51e7000fa353ce
---

Open Gateway enables software developers to leverage Telco Application Programming Interfaces (Telco APIs) for building applications that seamlessly integrate our underlying networks' capabilities and operators' data. These APIs provide a consistent method for accessing analytical and statistical data from networks, facilitating the implementation of customer experience-focused use cases. Open Gateway empowers developers to retrieve network information and request configuration changes efficiently.

Open Gateway utilizes these Telco APIs to offer a unified standard interface across multiple operator networks worldwide, abstracting the inherent complexities associated with their systems and infrastructures. This approach simplifies integration and enhances interoperability for developers and applications alike.

![available_apis](https://github.com/Telefonica/opengateway-developers-website/raw/main/catalog/images/available_apis.png)

> 📘 Want to give Open Gateway APIs a try?
> Apply to join the [Developer Hub](https://opengateway.telefonica.com/en/developer-hub) and gain access to our Sandbox.

## Technical Description of Open Gateway APIs

### Interoperability and Open Standards

Open Gateway APIs are built on open standards that ensure interoperability between different telecommunications operators and development platforms. By adopting common technical specifications and universal protocols, these APIs facilitate the integration of services and applications across various mobile networks, including 4G, 5G, and future technologies.

### API Architecture

Open Gateway APIs are designed using a _RESTful_ (Representational State Transfer) architecture, enabling simple and efficient communication between clients and servers through standard HTTP methods such as GET, POST, PUT, and DELETE. This architecture is highly scalable and easy to implement, making it ideal for distributed and high-performance environments.

### Security and Authentication

Open Gateway APIs implement robust security and authentication mechanisms to protect data integrity and confidentiality. This includes the use of _OAuth 2.0_ for authorization and _JWT_ (JSON Web Tokens) for secure user and application authentication.

## Commercially available APIs

The following APIs are already commercially available in some regions for developers to use through our Channel Partners. For seamless integration and access to our services, please contact our authorized aggregation partners.

<a href="https://opengateway.telefonica.com/en/partner-program" target="_blank">Check the benefits of joining the Telefónica Open Gateway Partner Program</a>

### SIM Swap

The standardized SIM Swap API enables seamless integration of SIM swap detection and management functionality into your applications. This API enhances security by identifying potentially fraudulent activity and providing an additional layer of protection against unauthorized access.

Additionally, the SIM Swap's Unified API Access feature ensures access to network capabilities of various carriers through a single, standardized interface. This simplifies integration and improves efficiency for developers by consolidating access to multiple carrier networks.

### Number Verification API

The standardized Number Verification API enhances the security of your users' identities and credentials. This API provides a quick, convenient, reliable, and secure method for verifying user information, ensuring robust protection against unauthorized access.

## Technically available APIs

The following APIs are available for testing and can be accessed in mock or production mode in certain regions. This setup allows for evaluating functionality and integration in a controlled environment.

### Device location

The standardised Device Location Verification API provides the option of verifying the geographical location of a given SIM-based device and validating whether it is within a requested geographical area without spoofing or GPS.

This solution validates the location of a device to enable services or allow transactions by verifying the location.

### Device status

The standardised Device Status API provides information regarding particular conditions of devices equipped with the end-user's SIM card, such as whether the device is in a roaming state and the country it is in.

Again, this API enables use cases around specific services related to the end-user's situation, or preventing frauds from foreign locations.

### Quality on Demand Mobile (QoD Mobile) API

The standardized QoD Mobile API allows you to manage and control your customers' mobile connectivity. This capability enables you to focus on creating the best possible user experiences, ensuring optimal performance and reliability for mobile applications.

### Know Your Customer (KYC) API

The standardized Know Your Customer (KYC) API enables real-time verification of customer information, providing an efficient way to validate the authenticity of personal data provided by users. By leveraging this API, businesses can mitigate risks associated with identity fraud, and enhance overall customer trust.