---
nav_title: Custom sounds
article_title: Custom Push Notification Sounds for iOS
platform: iOS
page_order: 3
description: "This reference article covers implementing custom sounds in your iOS push notifications."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Custom sounds

## Step 1: Hosting the sound in the app

Custom push notification sounds must be hosted locally within the main bundle of the client application. The following audio data formats are accepted:

- Linear PCM
- MA4
- µLaw
- aLaw

You can package the audio data in an AIFF, WAV, or CAF file. In Xcode, add the sound file to your project as a non-localized resource of the application bundle.

You may use the afconvert tool to convert sounds. For example, to convert the 16-bit linear PCM system sound Submarine.aiff to IMA4 audio in a CAF file, use the following command in the terminal:

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

You can inspect a sound to determine its data format by opening it in QuickTime Player and choosing **Show Movie Inspector** from the **Movie** menu.

Custom sounds must be under 30 seconds when played. If a custom sound is over that limit, the default system sound is played instead.

## Step 2: Providing the dashboard with a protocol URL for the sound

Your sound must be hosted locally within the app. You must specify a protocol URL that directs to the location of the sound file in the app within the **Sound** field in the push composer. Specifying "default" in this field will play the default notification sound on the device. This can be specified via our [messaging API]({{site.baseurl}}/api/endpoints/messaging/) or our dashboard under **Settings** in the push composer, as pictured in the following screenshot:

![]({% image_buster /assets/img_archive/sound_push_ios.png %})

If the specified sound file doesn't exist or the keyword "default" is entered, Braze will use the default device alert sound. Aside from our dashboard, sound can also be configured via our [messaging API]({{site.baseurl}}/api/endpoints/messaging/). See the Apple Developer Documentation regarding [preparing custom alert sounds](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html) for additional information.

