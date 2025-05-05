---
title: Quality on Demand API
excerpt: The QoD API allows the developer to optimize the network traffic on their customers' devices on demand.
category: 681879c3afc1a0003709c745
---

One good example is an application for enriching the audience experience when attending a live sporting event: add the capability to watch replays of relevant games. 

To do this, the application activates a Quality on Demand session on the device of the customer just before it is about to start the video-streaming, so the customer can watch it regardless of the
number of simultaneous users attending the sporting event in the same location. 

> 📘 Want to give it a try?
> Apply to join the [Developer Hub](https://opengateway.telefonica.com/en/developer-hub/join) and gain access to our Sandbox.

### Getting started on the Telefónica Open Gateway Sandbox
[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2FovVWzyx34Do%3Ffeature%3Doembed&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DovVWzyx34Do&image=https%3A%2F%2Fi.ytimg.com%2Fvi%2FovVWzyx34Do%2Fhqdefault.jpg&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen; encrypted-media; picture-in-picture;\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=ovVWzyx34Do",
  "title": "Better Connectivity with QoD Mobile and QoD Wi-Fi APIs",
  "favicon": "https://www.youtube.com/favicon.ico",
  "image": "https://i.ytimg.com/vi/ovVWzyx34Do/hqdefault.jpg",
  "provider": "https://www.youtube.com/",
  "href": "https://www.youtube.com/watch?v=ovVWzyx34Do",
  "typeOfEmbed": "youtube"
}
[/block]

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



