---
title: Quality on Demand API
category:
  uri: API Catalog
content:
  excerpt: >-
    The QoD API allows the developer to optimize the network traffic on their
    customers' devices on demand.
---

<div style="display: flex; gap: 8px; margin-bottom: 15px;">
  <span style="background-color: #f0f0f0; border: 1px solid #ccc; border-radius: 15px; padding: 4px 12px; font-size: 12px; font-weight: bold; color: #666;">Under CAMARA project</span>
  <span style="background-color: #8a8a8a; color: white; border-radius: 15px; padding: 4px 12px; font-size: 12px; font-weight: bold;">GSMA Certified API</span>
</div>

One good example is an application for enriching the audience experience when attending a live sporting event: add the capability to watch replays of relevant games. 

To do this, the application activates a Quality on Demand session on the device of the customer just before it is about to start the video-streaming, so the customer can watch it regardless of the
number of simultaneous users attending the sporting event in the same location. 

> 📘 Want to give it a try?
> Apply to join the [Developer Hub](https://opengateway.telefonica.com/en/developer-hub/join) and gain access to our Sandbox.

### Getting started on the Telefónica Open Gateway Sandbox

<iframe  
  width="560"  
  height="315"  
  src="https://www.youtube.com/embed/ovVWzyx34Do?si=hTcAXEtOeAiYwPaJ"  
  title="YouTube video player"  
  frameborder="0"  
  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"  
  referrerpolicy="strict-origin-when-cross-origin"  
  allowfullscreen>
</iframe>

## Overview of the QoD CAMARA API

### High level definition

The QoD CAMARA API enables application developers to integrate network configuration and optimization functionalities into their software, without the need for the End Users to run complex processes on their devices, so developers can focus on provide a better user experience.


### API Operations

The QoD CAMARA API specifies the following operations:

- **Discover the available QoS Profiles:** An operation to retrieve the list of available QoS profiles.

[Check the API Reference](/reference/getqosprofiles-2)

- **Create a new session:** An operation to assign a QoS Profile for a given device for a given duration. 

[Check the API Reference](/reference/createsession-2)

- **Read session information:** An operation to read the information about a QoD session created previously. 

[Check the API Reference](/reference/getsession-2)

- **Extend a session:** An operation to extend the duration of a QoD session created previously.

[Check the API Reference](/reference/extendqossessionduration-2)

- **Finish a session:** An operation to terminate a QoD session created previously. 

[Check the API Reference](/reference/deletesession-2)

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



