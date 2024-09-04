---
title: Device Status API
excerpt: The Device Status API makes it possible to check the roaming status of a specific SIM-based device by using events from the operators' network.
category: 66aa4f941e51e7000fa353ce
---

The Device Location API is a software interface that allows applications to confirm if a user's device is in its intended location. The network must track a device's location at all times to effectively provide telecommunications services. This capability is utilized to offer device location as a service.

The Device Location API enhances security by verifying that a device is in the expected location during transactions, which helps prevent fraud and unauthorized activities. This verification process also streamlines authentication, leading to faster and smoother transactions, ultimately improving the user experience. 

Additionally, the API is a valuable tool for fraud prevention, as it can quickly detect and mitigate potential threats by identifying discrepancies between the claimed and actual device locations. It also helps businesses comply with regulatory requirements in industries where location verification is essential, such as finance and gaming. 
 
Furthermore, by knowing a user's location, businesses can offer more personalized and context-aware services, increasing customer engagement and satisfaction. The API's versatility makes it applicable across various industries, including retail, telecom, and logistics. For merchants, it also contributes to reducing chargebacks by verifying the location of a device during transactions.


## Overview of the SIM Swap CAMARA API

### High level definition

The Device Status CAMARA API is a software interface that enables a requester to provide a mobile device identifier (such as MSISDN, IP, or an external identifier) and receive a response indicating whether the device is currently in roaming status.

### API Operations

The Device Status Camara API specifies one operation:

- **POST /roaming**: answers the question 'is the device in roaming?'

[Check the API Reference](/reference/devicestatus)

