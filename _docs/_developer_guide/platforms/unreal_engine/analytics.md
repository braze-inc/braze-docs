---
nav_title: Analytics
article_title: Analytics for the Unreal Engine Braze SDK
description: Learn about analytics for the Unreal Engine Braze SDK.
page_order: 3
---

# Analytics

> Learn about analytics for the Unreal Engine Braze SDK.

{% multi_lang_include developer_guide/prerequisites/unreal_engine.md %}

## Classes and functions

The Braze Unreal SDK supports the following analytics classes and functions.

| Class             | Function                                                  |
|-------------------|-----------------------------------------------------------|
| `UBraze`          | `ChangeUser`                                              |
| `UBraze`          | `LogCustomEvent`                                          |
| `UBraze`          | `LogCustomEventWithProperties`                            |
| `UBraze`          | `LogPurchase`                                             |
| `UBraze`          | `LogPurchaseWithProperties`                               |
| `UBraze`          | `RequestImmediateDataFlush`                               |
| `UBraze`          | `GetCurrentUser`                                          |
| `UBrazeUser`      | `SetCustomUserAttribute`                                  |
| `UBrazeUser`      | `SetCustomAttributeArray`                                 |
| `UBrazeUser`      | `UnsetCustomAttribute`                                    |
| `UBrazeUser`      | `IncrementCustomUserAttribute`                            |
| `UBrazeUser`      | `AddToCustomAttributeArray`                               |
| `UBrazeUser`      | `RemoveFromCustomAttributeArray`                          |
| `UBrazeUser`      | `SetEmail`                                                |
| `UBrazeUser`      | `SetFirstName`                                            |
| `UBrazeUser`      | `SetLastName`                                             |
| `UBrazeUser`      | `SetGender`                                               |
| `UBrazeUser`      | `SetLanguage`                                             |
| `UBrazeUser`      | `SetCountry`                                              |
| `UBrazeUser`      | `SetHomeCity`                                             |
| `UBrazeUser`      | `SetPhoneNumber`                                          |
| `UBrazeUser`      | `SetDateOfBirth`                                          |
| `UBrazeUser`      | `SetPushSubscriptionType`                                 |
| `UBrazeUser`      | `SetEmailSubscriptionType`                                |
| `UBrazeUser`      | `SetAttributionData`                                      |
| `UBrazeUser`      | `SetLastKnownLocation`                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Creating `FBrazeProperties` in Blueprint

The Blueprint Library `BrazePropertiesLibrary` includes helper functions to make creating Braze properties easier. Use the `Make FBrazeAny*` Nodes with a `MakeMap` when using the `MakeBrazeProperties` node. For example:

![A Blueprint project using Make Braze Properties.]({% image_buster /assets/img/unreal_engine/MakeBrazeProperties.png %})
