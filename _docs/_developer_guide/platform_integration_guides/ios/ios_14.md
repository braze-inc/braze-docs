---
nav_title: iOS 14 Upgrade Guide
page_order: 10
platform: iOS
---

# iOS 14 SDK Upgrade Guide

This guide describes Braze-related changes introduced in iOS 14 and the required upgrade steps for your Braze iOS SDK integration.

For a complete list of new iOS 14 updates, see Apple's [iOS 14 Page](https://www.apple.com/ios/ios-14/).

{% alert tip %}
As of iOS 14.5, **IDFA** collection and [certain data sharing][5] will require the new [AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency) Framework permission prompt ([Learn More](#idfa)).
{% endalert %}

#### Summary of iOS 14 breaking changes

- Apps targeting iOS 14 / Xcode 12 must use our [official iOS 14 release][1].
- Geofences are [no longer supported by iOS][4] for users who choose the new  _approximate location_ permission.
- Use of the "Last Known Location" targeting features will require an upgrade to Braze iOS SDK v3.26.1+ for compatibility with _approximate location_ permission. Note that if you are using XCode 12, you will need to upgrade to at least v3.27.0.
- As of iOS 14.5, IDFA collection and [certain data sharing][5] require the new [AppTrackingTransparency](https://developer.apple.com/documentation/apptrackingtransparency) Framework permission prompt.
- If you use the “Ad Tracking Enabled” field for campaign targeting or analytics, you will need to upgrade to Xcode 12 and use the new AppTrackingTransparency framework to report end users’ opt-in status.

## Upgrade Summary

<style>
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2) {
    min-width:230px;
}
table td {
    word-break: break-word;
}
</style>

|If Your App Uses:|Upgrade Recommendation|Description|
|------|--------|---|
|Xcode 12|**Upgrade to iOS SDK v3.27 or above**|Customers using Xcode 12 must use v3.27.0+ for compatibility. If you experience any issues or questions related to our iOS 14 compatibility, please open a new [Github Issue][2].|
|Most Recent Location| **Upgrade to iOS SDK v3.26.1 or above**|If you use the Most Recent Location targeting feature and are still using XCode 11, you should upgrade to at least iOS SDK v3.26.1 which supports the new  _Approximate Location_ feature. Older SDKs will not be able to reliably collect location when a user upgrades to iOS 14 _and_ choose Approximate Location.<br><br>Even though your app might not target iOS 14, your end users may upgrade to iOS 14 and begin to use the new location accuracy option. Apps that do not upgrade to iOS SDK v3.26.1+ will not be able to reliably collect location attributes when users provide their _approximate location_  on iOS 14 devices.|
|IDFA Ad Tracking ID| **Upgrade to Xcode 12 and iOS SDK v3.27 may be required**|Sometime in 2021, Apple will begin to require a permission prompt for the collection of the IDFA. At that time, apps must upgrade to Xcode 12 and use the new `AppTrackingTransparency` framework in order to continue collecting IDFA. If you pass IDFA to the Braze SDK you must also upgrade to v3.27.0+ at that time.<br><br>Apps that do not use the new iOS 14 APIs will be unable to collect IDFA, and will instead collect a blank ID (`00000000-0000-0000-0000-000000000000`) once Apple begins to enforce this change in 2021. For more information on whether or not this applies to your app, [read the details below](#idfa).|


## iOS 14 Behavior Changes

### Approximate Location Permission

![Precise Location]({% image_buster /assets/img/ios/ios14-approximate-location.png %}){: style="float:right;max-width:45%;margin-left:15px;"}

#### Overview

When requesting location permission, users will now have a choice to provide their _precise location_ (previous behavior), or the new _approximate location_. Approximate location will return a larger radius in which the user is located, instead of their exact coordinates.

#### Geofences {#geofences}

Geofences are [no longer supported by iOS][4] for users who choose the new  _approximate location_ permission. While no updates are required for your Braze SDK integration, you may need to adjust your [location-based marketing strategy](https://www.braze.com/blog/geofencing-geo-targeting-beaconing-when-to-use/) for campaigns that rely on geofences.

#### Location Targeting {#location-tracking}

To continue to collect users' _last known location_ when _approximate location_ is granted, your app will need to upgrade to at least v3.26.1 of the Braze iOS SDK. Keep in mind that the location will be less precise, and based on our testing has been upwards of 12,000 meters (7+ miles). When using the _last known location_ targeting options in the Braze Dashboard, be sure to increase the location's radius to account for new _approximate locations_ (we recommend at least a 1 mile/1.6km radius).

Apps that do not upgrade their Braze iOS SDK to at least v3.26.1 will no longer be able to use location tracking when _approximate location_ is granted on iOS 14 devices.

Users who have already granted location access will continue to provide _precise location_ after upgrading.

Note that if you are using XCode 12, you will need to upgrade to at least v3.27.0.

For more information on Approximate Location, see Apple's [What's New In Location](https://developer.apple.com/videos/play/wwdc2020/10660/) WWDC Video.

### IDFA and App Tracking Transparency {#idfa}

#### Overview

IDFA (Identifier for Advertisers) is an identifier provided by Apple for use with advertising and attribution partners for cross-device tracking and is tied to an individual's Apple ID.

Starting in iOS 14.5, a new permission prompt (launched by the new `AppTrackingTransparency` framework) must be shown to collect explicit user consent for IDFA. This permission prompt to "track you across apps and websites owned by other companies" will be requested similarly to how you’d prompt users to request their location.

If a user does not accept the prompt, or if you do not upgrade to Xcode 12's `AppTrackingTransparency` framework, then a blank IDFA value (`00000000-0000-0000-0000-000000000000`) will be returned, and your app will not be allowed to prompt the user again.

{% alert important %}
These IDFA updates will take effect once end-users upgrade their device to iOS 14.5. Please ensure your app uses the new `AppTransparencyFramework` with Xcode 12 if you plan to collect IDFA.
{% endalert %}

#### Changes to Braze IDFA collection
![IDFA]({% image_buster /assets/img/ios/ios14-idfa.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

1. Braze will continue to allow apps to provide a user's IDFA value _to_ the Braze SDK.

2. The `ABK_ENABLE_IDFA_COLLECTION` compilation macro, which would conditionally compile in optional automatic IDFA collection, will no longer function in iOS 14 and has been removed in 3.27.0. 

3. If you use the “Ad Tracking Enabled” field for campaign targeting or analytics, you will need to upgrade to Xcode 12 and use the new AppTrackingTransparency framework to report end users’ opt-in status. The reason for this change is that in iOS 14, the old [`advertisingTrackingEnabled`](https://developer.apple.com/documentation/adsupport/asidentifiermanager/1614148-advertisingtrackingenabled) field will always return No.

4. If your app has used IDFA or IDFV as your Braze External ID, we strongly recommend migrating away from these identifiers in favor of a UUID. For more information on migrating External IDs, see our new [External ID Migration API Endpoint]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/).

Read more from Apple about their [Privacy Updates](https://developer.apple.com/app-store/user-privacy-and-data-use/) and the new [App Tracking Transparency framework](https://developer.apple.com/documentation/apptrackingtransparency).

### Push Authorization {#push-provisional-auth}

{% alert important %}
No changes to Provisional Push Authorization are included in iOS 14. In an earlier beta version of iOS 14, Apple introduced a change which has since been reverted back to prior behavior.
{% endalert %}


## iOS 14 New Features

### App Privacy and Data Collection Overview {#app-privacy}

The App Store's new App Privacy feature will disclose to users what personal information an app collects and how it may track users across other apps and websites. Apple has [stated](https://www.apple.com/ios/ios-14-preview/), "Privacy information on the App Store will be coming in an iOS 14 update later this year".

Braze will continue to monitor this new feature announcement to help you understand how your usage of Braze may be disclosed in the App Privacy summary.

To learn more about this feature, see [Apple's Privacy and Data Use](https://developer.apple.com/app-store/user-privacy-and-data-use/).

### App Clips {#app-clips}

![App Clip]({% image_buster /assets/img/ios/ios14-app-clips.png %}){: style="float:right;max-width:45%;margin-left:15px;border:0"}

An _App clip_ is a small part of your app that can be quickly accessed without installation by visiting a URL or scanning a QR code.

This feature gives users quicker access to sample your app, with an opportunity to either upgrade to the full app experience or auto-delete after a period of inactivity.

To learn more about App Clips, see [Apple's App Clip Documentation](https://developer.apple.com/app-clips/)

If you're interested in using Braze within App Clips, please submit feedback in our [Product Portal](https://dashboard.braze.com/resources/roadmap).

[1]: https://github.com/Appboy/appboy-ios-sdk/releases/tag/3.27.0
[2]: https://github.com/Appboy/appboy-ios-sdk/issues
[4]: https://developer.apple.com/documentation/corelocation/cllocationmanager/3600215-accuracyauthorization
[5]: https://developer.apple.com/app-store/user-privacy-and-data-use/#permission-to-track
