---
nav_title: ANALYTICS
article_title: Push Notifications for the Unreal Engine Braze SDK
platform:
  - Cordova
  - iOS
  - Android
page_order: 2
page_type: reference
description: "This article covers implementing push notifications on Cordova."
channel: push
---

# ANALYTICS

> Learn how to set up push notifications for the Unreal Engine Braze SDK.

{% multi_lang_include developer_guide/prerequisites/unreal_engine.md %}

## Classes and functions

### Disabling Data Collection

| Class    | Function                        |
|----------|---------------------------------|
| `UBraze` | `RequestImmediateDataFlush`    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Setting User Attributes

| Class        | Function                           |
|-------------|------------------------------------|
| `UBrazeUser` | `SetCustomUserAttribute`         |
| `UBrazeUser` | `SetCustomAttributeArray`        |
| `UBrazeUser` | `UnsetCustomAttribute`           |
| `UBrazeUser` | `IncrementCustomUserAttribute`   |
| `UBrazeUser` | `AddToCustomAttributeArray`      |
| `UBrazeUser` | `RemoveFromCustomAttributeArray` |
| `UBrazeUser` | `SetEmail`                       |
| `UBrazeUser` | `SetFirstName`                   |
| `UBrazeUser` | `SetLastName`                    |
| `UBrazeUser` | `SetGender`                      |
| `UBrazeUser` | `SetLanguage`                    |
| `UBrazeUser` | `SetCountry`                     |
| `UBrazeUser` | `SetHomeCity`                    |
| `UBrazeUser` | `SetPhoneNumber`                 |
| `UBrazeUser` | `SetDateOfBirth`                 |
| `UBrazeUser` | `SetPushSubscriptionType`        |
| `UBrazeUser` | `SetEmailSubscriptionType`       |
| `UBrazeUser` | `SetAttributionData`             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Setting User IDs

| Class    | Function      |
|----------|--------------|
| `UBraze` | `ChangeUser` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Tracking Events

| Class    | Function                        |
|----------|---------------------------------|
| `UBraze` | `LogCustomEvent`               |
| `UBraze` | `LogCustomEventWithProperties` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Tracking Location

| Class        | Function                 |
|-------------|--------------------------|
| `UBrazeUser` | `SetLastKnownLocation`  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Tracking Purchases

| Class    | Function                        |
|----------|---------------------------------|
| `UBraze` | `LogPurchase`                  |
| `UBraze` | `LogPurchaseWithProperties`    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Tracking Sessions

| Class    | Function                 |
|----------|--------------------------|
| `UBraze` | `GetCurrentUser`         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Tracking Uninstalls

*(No specific functions are listed for uninstall tracking in this table.)*

### Catch-All (Unmapped to a Specific Page)

| Class    | Function                        |
|----------|---------------------------------|
| `UBraze` | `RequestImmediateDataFlush`    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Creating `FBrazeProperties` in Blueprint

The Blueprint Library `BrazePropertiesLibrary` includes helper functions to make creating Braze properties easier. Use the `Make FBrazeAny*` Nodes with a `MakeMap` when using the `MakeBrazeProperties` node. For example:

![A Blueprint project using Make Braze Properties.]({% image_buster /assets/img/unreal_engine/MakeBrazeProperties.png %})
