---
nav_title: Dynamic APNs Gateway Management
article_title: Dynamic APNs Gateway Management
platform: Swift
page_order: 30
description: "This page covers how to leverage dynamic APNs gateway management to eliminate the need for manual gateway selection."
channel:
  - push
---

# Dynamic APNs gateway management for push notifications

> Dynamic Apple Push Notification Service (APNs) gateway management enhances the reliability and efficiency of iOS push notifications by automatically detecting the correct APNs environment. Previously, you would manually select APNs environments (development or production) for your push notifications, which sometimes led to incorrect gateway configurations, delivery failures, and `BadDeviceToken` errors.

## Benefits

- **Improved reliability:** Notifications are always delivered to the correct APNs environment, reducing failed deliveries.
- **Simplified configuration:** You no longer need to manually manage APNs gateway settings.
- **Error resilience:** Invalid or missing gateway values are gracefully handled, providing uninterrupted service.

## Prerequisites

Braze supports Dynamic APNs gateway management for push notifications on iOS with the following SDK version requirement:

{% sdk_min_versions swift:10.0.0 %}

## How it works

When an iOS app integrates with the Braze Swift SDK, it sends device-related data, including [`aps-environment`](https://developer.apple.com/documentation/bundleresources/entitlements/aps-environment) if available, to the Braze SDK API.

The `apns_gateway` value indicates whether the app is using the:
- Development (dev) APNs environment
- Production (prod) APNs environment

### Dynamic gateway updates

Braze stores the reported gateway value for each device. If a new, valid gateway value is received, Braze updates the stored value automatically.

### Push notification delivery

When Braze sends a push notification:

- If a valid gateway value (dev or prod) is stored for the device, Braze uses it to determine the correct APNs environment.
- If no gateway value is stored, Braze defaults to the APNs environment configured in the **App Settings** page.

## Frequently asked questions

### Why was this feature introduced?

With dynamic APNs gateway management, the correct environment is selected automatically. Previously, you had to manually configure the APNs gateway, which could lead to `BadDeviceToken` errors, token invalidation, and potential APNs rate-limiting issues.

### How does this impact push delivery performance?

This feature improves delivery rates by ensuring push tokens are always routed to the correct APNs environment, avoiding failures caused by misconfigured gateways.

### Can I disable this feature?

Dynamic APNs Gateway Management is turned on by default and provides reliability improvements. If you have specific use cases that require manual gateway selection, contact [Braze Support]({{site.baseurl}}/help/support).