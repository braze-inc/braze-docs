---
nav_title: Advanced Notes
page_order: 6
search_rank: 5
platform: Android
---

# Advanced Notes

## Android Dialogs

Braze doesn't support displaying in-app messages in [Android Dialogs][39] at this time.

## Button Text Capitalization

Android Material Design specifies that Button text should be upper case by default. Braze's in-app message buttons follow this convention as well.

## Youtube in HTML in-app messages

Starting in Braze Android SDK version 2.0.1, Youtube and other HTML5 content can play in HTML in-app messages. This requires hardware acceleration to be enabled in the Activity where the in-app message is being displayed, please see the [Android developer guide][71] for more details. Also that hardware acceleration is only available on API versions 11 and above.

{% include archive/troubleshooting_iams.md platform="Android" %}

[39]: https://developer.android.com/guide/topics/ui/dialogs.html
[71]: https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling
