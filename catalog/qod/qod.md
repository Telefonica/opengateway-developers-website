---
title: Quality on Demand API
excerpt: The QoD API allows the developer to prioritize network traffic on certain devices on demand.
category: 66aa4f941e51e7000fa353ce
---

An example of an application that aims to enrich the public experience when attending a live sporting event, an advanced feature for your viewers may be watching replays of relevant games. 

To do this, the application must ensure that the end user has adequate connectivity to watch it, regardless of the
number of simultaneous users watching the sporting event in the same location. 

> 📘 Want to give it a try?
> Apply to join the [Developer Hub](https://opengateway.telefonica.com/en/developer-hub) and gain access to our Sandbox.

## Overview of the QoD CAMARA API

### High level definition

The QoD CAMARA API is a software interface that enable application developers to integrate network configuration and optimization functionalities into their software, without the need for the End Users to run complex processes on their devices.

This functionality easily allows applications to gain the ability to interact seamlessly with mobile network operator systems, so developers can focus on provide a better user experience.


### API Operations

The QoD CAMARA API specifies the following three operations:

- **POST Creates a new session:** An operation to setup a new QoD provisioning for a given device. Parameters required:  

  - `ueId`: User equipment identifier ;
  - `asId`: Application server identifier ;
  - `qos` : Enum: "QOS_E" (Qualifier for enhanced communication profile),  "QOS_S" (Qualifier for the requested QoS profile S), "QOS_M" (Qualifier for the requested QoS profile M) ,  "QOS_L" (Qualifier for the requested QoS profile L);
  
  Other parameters :
    - `duration`: Session duration in seconds (maximal value of 24 hours is used if not set);
    - `uePorts` : Ports may be specified as a list of ranges or single ports ;
    - `asPorts` : Ports may be specified as a list of ranges or single ports ;
    - `notificationUri` : Allows asynchronous delivery of session related events ;
    - `notificationAuthToken` : Authentication token for callback API ;

[Check the API Reference](/reference/createsession)

- **GET Get session information:** An operation to get the information about a specific QoD provisioning.Path parameter required:  

  - `sessionId`:Session ID that was obtained from the createSession operation.

[Check the API Reference](/reference/getsession)

- **DELETE Free resources related to QoS session:** An operation to terminate a QoD provisioning, identified by Id .  Path parameter required:  

  - `sessionId`: Session ID that was obtained from the createSession operation.

[Check the API Reference](/reference/deletesession)

By utilizing the QoD Service, developers of applications can capitalize on the usability, ubiquity, security, quickness, and simplicity of the APIs to manage their End Users networking and focus on the experiences they want to offer.

## Why QoD?

### Optimize client’s networking

With QoD, you can activate the best networking configuration that suits better to the needs of your applications in real time. Regardless of whether your application requires a  short boost with better throughput or a temporal control on the maximum jitter or latency. 

### Seamless User Experience

Your clients will enjoy the enhanced services you build with the capabilities brough to you by the QoD service without even noticing their network has been modified. This allows you to upsell advanced features with the security they will not suffer undesirable network issues.

### Improve your client’s satisfaction

You can control and monitor the network conditions and adapt to them whenever your applications are being used. 

This will helps when customers didn’t experience your application as they should, and you weren’t able to manage.

### Quick and easy onboarding

With the QoD service, you can configure the network of your clients easily with only a couple of lines of code.

You will not have to guess and discover the available networking capabilities of their clients and will focus on what matters more to your business.


## General Informations

> ⚙️ Problem Solved ? 
>
> Do I need to prioritize network data traffic on certain devices?


> ⚙️ How it works 
>
> Prioritizes network data traffic on certain devices, thereby reducing browsing problems on those devices.


> ⚙️ Parameters sent in the request 
>
> - msisdn: Cell phone number in the format - +551199999999
> - ipv6addr: IPV6 address
> - qos : Qos profiles, connectivity characteristics in use of long-distance network 
> - duration : Duration of the process in seconds - if not passed, it will be considered 24 hours
> - notificationUri : Address to be redirected to
> - notificationAuthToken : Authentication key
>


> ⚙️ Data received in the response - POST 
>  
> {
>    "duration": 3600,
>    "ueId": {
>        "msisdn": "+5511852146260"
>    },
>    "asId": {
>        "ipv4addr": "0.0.0.0/0"
>    },
>    "qos": "QOS_E",
>    "id": "6a4d570a-6607-466d-889b-473e361afaa1",
>    "startedAt": 1740508025048,
>    "expiresAt": 1740508028648,
>    "qosStatus": "REQUESTED",
>    "messages": [
>        {
>            "severity": "INFO",
>            "description": "string"
>        }
>    ],
> }
>  

> ⚙️ Data received in the response - GET 
> 
> {
>    "duration": 77483,
>    "ueId": {
>        "externalId": "Kieran_Sauer3@hotmail.com",
>        "msisdn": "+34312468621",
>        "ipv4addr": "117.186.17.77",
>        "ipv6addr": "bdec:2f6a:b9de:6fc9:61a3:c233:391c:858a"
>    },
>    "asId": {
>        "ipv4addr": "55.2.85.35",
>        "ipv6addr": "3a6e:97df:0614:d555:a0db:66c4:1ac5:fbfb"
>    },
>    "uePorts": {
>        "ranges": [
>            {
>                "from": 61055,
>                "to": 56578
>            }
>        ],
>        "ports": [
>            14968,
>            49223
>        ]
>    },
>    "asPorts": {
>        "ranges": [
>            {
>                "from": 25113,
>                "to": 55764
>            }
>        ],
>        "ports": [
>            42391,
>            44401
>        ]
>    },
>    "qos": "QOS_E",
>    "notificationUri": "https://application-server.com/notifications",
>    "notificationAuthToken": "c8974e592c2fa383d4a3960714",
>    "id": "7c9c75e5-7691-484f-847b-5c6bc10bb778",
>    "startedAt": 1740508302143,
>    "expiresAt": 1740508362996,
>    "qosStatus": "REQUESTED",
>    "messages": [
>        {
>            "severity": "INFO",
>            "description": "string"
>        }
>    ],
>}
>
