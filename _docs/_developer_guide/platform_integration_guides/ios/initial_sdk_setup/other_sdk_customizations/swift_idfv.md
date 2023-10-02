---
nav_title: Collecting IDFV
article_title: Collecting IDFV
platform: iOS
page_type: reference
description: "This reference article describes how to collect the optional IDFV field for the Swift SDK"

---

# Collecting IDFV - Swift

## Background

In previous versions of the Braze iOS SDK, the IDFV (Identifier for Vendor) field was automatically collected as the user's device ID. 

The optional `useUUIDAsDeviceId` feature configures the [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) to set the device ID as a UUID. Traditionally, the iOS SDK would assign the device ID equal to the Apple-generated IDFV value. With this feature enabled on your iOS app, all new users created via the SDK would be assigned a device ID equal to a UUID.

{% alert note %}
Beginning in Swift SDK v5.7.0, the IDFV field can optionally be disabled, and instead, Braze will set a random UUID as the device ID. Beginning in v7.0.0, the UUID option will become enabled by default.
{% endalert %}

If you still wish to collect IDFV, along with the UUID option enabled, you can still do so via the Swift SDK as outlined [here](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)).

## Getting Started

To set the device ID as a UUID instead of the IDFV, in the `Braze.Configuration` instance of your iOS application, set `useUUIDAsDeviceId` to `true`.

## Considerations

### SDK Version

When enabling `useUUIDAsDeviceId`, all new users created will be assigned a random device ID. All previously existing users will maintain their same device ID value, which may have been IDFV.

When this feature is not enabled (by default), devices will continue to be assigned IDFV upon creation.

The diagram below describes when a UUID or IDFV will be assigned as the device ID. Note that the IDFV field can only be read from devices that support this feature (e.g., iOS, tvOS, macCatalyst)

![Flow chart for Swift v5.7 Device ID Configuration Scenarios — full description of flow chart included under "Process description"]({% image_buster /assets/img/swift_idfv.png %}){: style="max-width:80%"}

{% details Process description %}
1. User initializes SDK v5.7+
2. Is the user upgraded from a previous SDK version?
	- If Obj-C or less than v5.7, proceed to step 3
	- If v5.7+, proceed to step 4
3. Use IDFV as `device_id`
	- **End of process**
4. Does the user have an existing `device_id`?
	- If yes, proceed to step 5
	- If no (new user), proceed to step 6
5. Use existing `device_id`
	- **End of process**
6. Is UUID setting enabled?
	- If yes, proceed to step 7
	- If no, return to step 3
7. Assign UUID as `device_id`
	- **End of process**
{% enddetails %}

### Downstream 

**Technology partners**: If this feature is enabled, any technology partners that derive the IDFV value from the Braze device ID will no longer have access to this piece of data. If the IDFV value derived from the device IS is needed for your partner integration, we recommend that you do not enable this feature.

**Currents**: Enabling the `useUUIDAsDeviceId` option will mean the device ID sent in Currents will no longer equal IDFV.

## Frequently asked questions

#### Will this change impact my existing users in Braze?
No. When enabled, this feature will not overwrite any user data in Braze. Only newly created devices - or after `wipedata()` is called - will generate new UUID device IDs.

#### Can I turn this feature off after turning it on?
Yes, this feature can be toggled on and off at your discretion. Previously stored device IDs will never be overwritten.

#### Can I still capture the IDFV value via Braze elsewhere? 
Yes, you can still optionally collect the IDFV via the Swift SDK (collection is disabled by default). 
