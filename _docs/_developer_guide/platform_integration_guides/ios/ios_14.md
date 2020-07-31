---
nav_title: iOS 14 Upgrade Guide
page_order: 10
platform: iOS
---

# iOS 14 SDK Upgrade Guide

This guide describes Braze-related changes introduced in iOS 14 and the required upgrade steps for your Braze iOS SDK integration.

For a complete list of new iOS 14 updates announced this year at WWDC, see Apple's [iOS 14 Preview](https://www.apple.com/ios/ios-14-preview/).

#### Summary of iOS 14 breaking changes

- Geofences are no longer supported by iOS for users who choose the new  _approximate location_ permission.
- Customers using the "Last Known Location" targeting features are required to upgrade their Braze iOS SDK to at least v3.26.1 in order to accept the new _approximate location_ permission.
- IDFA collection now requires a permission prompt. Failure to update your IDFA collection code will result in a blank value, as if a user declined to provide this permission.
- Apps targeting iOS 14 / Xcode 12 for beta releases can use our [iOS 14 Beta release][1], and our official iOS 14 release after Apple's "Golden Master" release.

### Upgrade Summary

There are two necessary upgrades that are required to continue using Braze messaging features on iOS.

#### Location Targeting

Customers who are using the _Most Recent Location_ targeting features must upgrade to at least iOS SDK v3.26.1 which contains updates related to the new _Approximate Location_ feature in iOS 14. 

Even though your app might not target iOS 14, your end users may upgrade their devices which adds this new location accuracy option. Apps that do not upgrade to iOS SDK v3.26.1+ will not be able to collect location attributes when users provide their _approximate location_  on iOS 14 devices.

#### iOS 14 + Xcode 12

We have released [Beta versions][1] of our upcoming iOS 14 / Xcode 12 compatible SDK. Customers who relase Beta versions of their iOS apps with iOS 14 support are encouraged to use Braze's iOS 14 Beta SDK version which includes Xcode 12 compatibility and support for new iOS 14 APIs. 

We will continue to release updates and fixes to future beta releases as Apple continues to release newer versions of iOS 14 beta. If you experience any issues or questions related to our iOS 14 compatibility or beta release, please open a new [Github Issue][2].

Our official iOS 14 compatible SDK will be released shortly after Apple's final iOS 14 beta is released, known as the "Golden Master" release.

#### IDFA permissions

Once users upgrade to iOS 14, apps that collect the IDFA advertising ID must use the new iOS 14 APIs to prompt users for IDFA permission. Failure to update your code will result in a blank IDFA value (`00000000-0000-0000-0000-000000000000`), similar to a user declining this new prompt.

## iOS 14 Behavior Changes

### Approximate Location Permission

![Precise Location]({% image_buster /assets/img/ios/ios14-approximate-location.png %}){: style="float:right;max-width:45%;margin-left:15px;"}

#### Overview

When requesting location permission, users will now have a choice to provide their _precise location_ (previous behavior), or the new _approximate location_. Approximate location will return a larger radius in which the user is located, instead of their exact coordinates.

#### Geofences

Geofences, which previously relied on precise location permission, are no longer recorded by apps that have obtained the new _approximate location_ permission. While no updates are required to your Braze SDK integration, you may need to adjust your [location-based marketing strategy](https://www.braze.com/blog/geofencing-geo-targeting-beaconing-when-to-use/) for campaigns that rely on geofences.

#### Location Targeting

To continue to collect users' _last known location_ when _approximate location_ is granted, your app will need to upgrade to at least v3.26.1 of the Braze iOS SDK. Keep in mind that the location will be less precise, and based on our testing has been upwards of 12,000 meters (7+ miles). When using the _last known location_ targeting options in the Braze Dashboard, be sure to increase the location's radius to account for new _approximate locations_ (we recommend at least a 1 mile/1.6km radius).

Apps that do not ugprade their Braze iOS SDK to at least v3.26.1 will no longer be able to use location tracking when _approximate location_ is granted on iOS 14 devices.

Users who have already granted location access will continue to provide _precise location_ after upgrading.

For more information on Approximate Location, see Apple's [What's New In Location](https://developer.apple.com/videos/play/wwdc2020/10660/) WWDC Video.

### IDFA and App Tracking Transparency

#### Overview

IDFA (Identity for Advertisers) is an identifier provided by Apple used by advertising and attribution partners for cross-device tracking and is tied to an individual's Apple ID.

Beginning in iOS 14, a new permission prompt (launched by the new `AppTrackingTransparency` framework) will require explicit user consent to access the IDFA. This permission to "track you across apps and websites owned by other companies" will be requested similarly to how you’d prompt users to request their location.

If a user does not accept the prompt then a blank IDFA value (`00000000-0000-0000-0000-000000000000`) will be returned, and your app will not be allowed to prompt the user again.

{% alert important %}
These IDFA updates take effect once end users upgrade their device to iOS 14. Please ensure your app is using the new `AppTransparencyFramework` even if you do not explicitly target iOS 14 support.
{% endalert %}

#### Changes to Braze IDFA collection

![App Clip]({% image_buster /assets/img/ios/ios14-idfa.png %}){: style="float:right;max-width:45%;margin-left:15px;"}

1. Braze will continue to allow apps to provide a user's IDFA value _to_ the Braze SDK

2. The `ABK_ENABLE_IDFA_COLLECTION` macro, which would conditionally compile in optional automatic IDFA collection, will be removed in our iOS 14 release.

3. If your app has used IDFA or IDFV as your Braze External ID, we strongly recommend migrating away from these identifiers in favor of a UUID. For more information on migrating External IDs, see our new [External ID Migration API Endpoint](https://www.braze.com/docs/api/endpoints/user_data/external_id_migration/).

Read more from Apple about their [Privacy Updates](https://developer.apple.com/app-store/user-privacy-and-data-use/) and the new [App Tracking Transparency framework](https://developer.apple.com/documentation/apptrackingtransparency).

### Push Authorization

Based on our testing of iOS 14 Beta 2, Apple has removed Provisional Push Authorization introduced in 2018 (iOS 12). As a result, newly installed apps may be authorized to receive push notifications _quietly_, within the user's notification tray. We'll continue to monitor and update this guide as future iOS 14 beta versions are released.


## iOS 14 New Features

### App Privacy and Data Collection Overview

The App Store's new App Privacy feature will disclose to users what personal information an app collects and how it may track users across other apps and websites. Apple has [stated](https://www.apple.com/ios/ios-14-preview/), "Privacy information on the App Store will be coming in an iOS 14 update later this year".

Braze will continue to monitor this new feature announcement to help you understand how your usage of Braze may be disclosed in the App Privacy summary.

To learn more about this feature, see [Apple's Privacy and Data Use](https://developer.apple.com/app-store/user-privacy-and-data-use/).

### App Clips

#### Overview

![App Clip]({% image_buster /assets/img/ios/ios14-app-clips.png %}){: style="float:right;max-width:45%;margin-left:15px;"}

An _App clip_ is a small part of your app that can be quickly accessed without installation by visiting a URL or scanning a QR code.

This feature give users quicker access to sample your app, with an opportunity to either upgrade to the full app experience, or auto-delete after a period of inactivity.

To learn more about App Clips, see [Apple's App Clip Documentation](https://developer.apple.com/app-clips/)

#### Braze Support

For customers interested in using Braze within App Clips, please contact your Braze Success Team or Support Team.

We will be releasing support and documentation in the near future.

### Widgets

#### Overview

For customers interested in using Braze within Widgets, please contact your Braze Success Team or Support Team.

We will be releasing support and documentation in the near future.


### Safari Intelligent Tracking Prevention (ITP)

![Safari ITP Privacy Report]({% image_buster /assets/img/ios/ios14-safari-itp-privacy-report.jpg %}){: style="float:right;max-width:45%;margin-left:15px;"}

This year, Apple announced a new Safari feature called the _Privacy Report_, which will show users which trackers or 3rd party domains have been blocked to prevent cross-site tracking or identification.

#### Braze Web SDK

The Braze Web SDK does not do cross-site tracking, does not set any 3rd party cookies, and does not use any fingerprinting technologies. Based on our current testing, Braze does not appear in Safari's _Privacy Report_.

Version 2.5.2 of the Braze Web SDK addresses the shorter browser-storage duration based on previous changes to Intelligent Tracking Prevention (ITP 2.1) which accounts for Safari’s updated storage expiration restrictions.


[1]: https://github.com/Appboy/appboy-ios-sdk/blob/ios14-beta/CHANGELOG.md
[2]: https://github.com/Appboy/appboy-ios-sdk/issues
