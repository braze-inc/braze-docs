---
nav_title: September
page_order: 4
noindex: true
page_type: update
description: "This article contains release notes for September 2019."
---

# September 2019

## Braze app within OneLogin

Customers will be able to simply search and select Braze within [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/) for SP or IdP Initiated login. This means that customers will not have to add a custom application within OneLogin. As a result, this should pre-populate certain settings like attributes which we have seen come up since launching SAML SSO.

## Rokt calendar partnership

[Rokt Calendar]({{site.baseurl}}/partners/home/) provides Braze customers the ability to align their personalized marketing initiatives and extend personalized content to the end user's calendar. Thus, making it a more seamless experience for the end user and further develops stickiness with our customers' services. Customers will be able to...

- Send a calendar invite via Braze platform to 'save the date' and extend our communication
- Update an existing invite if the contents of the event has changed.

## Passkit partnership

With [Passkit]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/mobile_wallet/passkit/), Braze customers will be able to expand their customer engagement to mobile wallet. They will be able to personalized wallet campaigns while using Braze's powerful segmentation and orchestrate alongside channels like push, in-app messages, and more.

## Dispatch ID value return via messaging endpoints

A message's `dispatch_id` will be included in the following messaging endpoint responses:
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-via-API-triggered-delivery)
- [`/campaigns/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/#sending-messages-immediately-via-api-only)
- [`/messages/schedule`]({{site.baseurl}}/api/endpoints/messaging/#create-schedule-endpoint)
- [`/canvases/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/#canvas)
- [`/canvases/trigger/schedule`]({{site.baseurl}}/api/endpoints/messaging/#API-triggered-canvases)

This way, customers who use transactional messaging can trace the call back through Currents.

## Canvas changelogs

Did you even wonder more about the details of who is working on a Canvas in your account? Wonder no more! You can now access Canvas Changelogs.

![Canvas Changelogs]({% image_buster /assets/img/canvas-changelog1.png %})
![Canvas Changelogs]({% image_buster /assets/img/canvas-changelog2.png %})
