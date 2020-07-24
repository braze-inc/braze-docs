---
nav_title: iOS 14 Upgrade Guide
page_order: 10
platform: iOS
---

# iOS 14 SDK Upgrade Guide

This guide describes relevant changes introduced in iOS 14 and the required upgrade steps for your Braze iOS SDK integration.

For a complete list of the new features and changes announced this year at WWDC, see Apple's [iOS 14 Preview](https://www.apple.com/ios/ios-14-preview/).

## Braze SDK Compatibility

To test and build an app targeting iOS 14, we recommend integrating our Braze iOS Beta Release, which can be found [here][1] TODO!. This beta release for iOS 14 will be regularly updated based on changes to Apple's iOS 14 beta releases.

If you experience any issues or questions related to our iOS 14 compatibility or beta release, please open a new [Github Issue][2].

### Upgrade Summary

For apps targeting iOS 14, the following features have a change in behavior, or will require upgrading to Braze iOS SDK vX.X.X.

- [ ] Geofences are not supported for users who choose the new  _approximate location_ permission
- [ ] Updating a user's Last Known Location using the new _approximate location_ permission requires upgrading your Braze SDK.
- [ ] Expect a sudden decrease in IDFA availability which now requires a permission prompt

## iOS 14 Behavior Changes

### Approximate Location Permission

#### Overview

When an app requests location permission, users will now have a choice to provide their _precise location_ (previous behavior), or the new _approximate location_ which returns a larger radius in which the user is located.

#### Geofences

Geofences, which previously relied on precise location permission, are no longer recorded by apps that have obtained the new _approximate location_ permission. While no updates are required to your Braze SDK integration, you may need to adjust your [location-based marketing strategy](https://www.braze.com/blog/geofencing-geo-targeting-beaconing-when-to-use/) for campaigns that rely on geofences.

#### Location Targeting

To continue to collect users' _last known location_ when _approximate location_ is granted, your app will need to upgrade to the latest Braze iOS SDK. Keep in mind that the location will be less precise, and based on our testing has been upwards of 12,000 meters (7+ miles).

Users who have already granted location access will continue to provide _precise location_ after upgrading.

For more information on Approximate Location, see Apple's [What's New In Location](https://developer.apple.com/videos/play/wwdc2020/10660/) WWDC Video.

### IDFA and App Tracking Transparency

#### Overview

IDFA (Identity for Advertisers) is an identifier provided by Apple used by advertising and attribution partners for cross-device tracking, tied to an individual's Apple ID.

Beginning in iOS 14, a new permission prompt, known as the AppTrackingTransparency framework, will require explicit user consent to access the IDFA. This permission to “track you across apps and websites owned by other companies” will be requested similarly to how you’d prompt users to request their location.

If a user does not accept the prompt then a blank IDFA value ("00000000-0000-0000-0000-000000000000") will be returned, and your app will not be allowed to prompt the user again.

#### Changes to Braze IDFA collection

1. Braze will continue to allow apps to provide a user's IDFA value

2. SDK macros which previously instructed the Braze SDK to retrieve the IDFA have been removed

3. If your app has used IDFA or IDFV as your Braze External ID, we strongly recommend migrating away from these identifiers in favor of a UUID. For more information on migrating External IDs, see our new External ID Migration API Endpoint.

To learn more, check out about Apple's [App Tracking Transparency framework](https://developer.apple.com/documentation/apptrackingtransparency).

### Push Authorization

iOS 14 has removed Provisional Push Authorization introduced in 2018 (iOS 12). As a result, newly installed apps will be authorized to receive push notifications _quietly_, within the user's notification tray.


## iOS 14 New Features

### App Privacy and Data Collection Overview

The App Store's new App Privacy feature will disclose to users what personal information an app collects and how it may track users across other apps and websites. Apple has [stated](https://www.apple.com/ios/ios-14-preview/), "Privacy information on the App Store will be coming in an iOS 14 update later this year".

Braze will continue to monitor this new feature announcement to help make sure that your use of Braze is appropriately disclosed in the App Privacy summary.

### App Clips

### Widgets


### Safari Intelligent Tracking Prevention (ITP)

Apple introduced _Intelligent Tracking Prevention_ (ITP) in 2017 as a set of new privacy improvements for Safari. 

This year, Apple announced a new Safari feature,  “Privacy Report”, which will show users which trackers or 3rd party domains have been blocked to prevent cross-site tracking or identification.


How customers are affected
Braze does not do any cross-site tracking, does not set any 3rd party cookies, and does not use any fingerprinting technologies. Based on our current testing, Braze does not appear in Safari’s Privacy Report list displayed to end users.

Braze has already updated the Web SDK (v2.5.2+) to address the shorter browser-storage duration from ITP 2.1, to account for Safari’s updated storage expiration restrictions.
Action items for customers
Customers should update their Braze Web SDK to version 2.5.2+ 





[1]: https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md
[2]: https://github.com/Appboy/appboy-ios-sdk/issues
