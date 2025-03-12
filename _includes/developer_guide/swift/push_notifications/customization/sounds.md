## Customizing sounds

### Step 1: Hosting the sound in the app

Custom push notification sounds must be hosted locally within the main bundle of your app. The following audio data formats are accepted:

- Linear PCM
- MA4
- µLaw
- aLaw

You can package the audio data in an AIFF, WAV, or CAF file. In Xcode, add the sound file to your project as a non-localized resource of the application bundle.

{% alert note %}
Custom sounds must be under 30 seconds when played. If a custom sound is over that limit, the default system sound is played instead.
{% endalert %}

#### Converting sound files

You can use the afconvert tool to convert sounds. For example, to convert the 16-bit linear PCM system sound Submarine.aiff to IMA4 audio in a CAF file, use the following command in the terminal:

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

{% alert tip %}
You can inspect a sound to determine its data format by opening it in QuickTime Player and choosing **Show Movie Inspector** from the **Movie** menu. 
{% endalert %}

### Step 2: Providing a protocol URL for the sound

You must specify a protocol URL that directs to the location of the sound file in your app. There are two methods for doing this:

* Use the `sound` parameter of the [Apple push object]({{site.baseurl}}/api/objects_filters/messaging/apple_object#apple-push-object) to pass the URL to Braze.
* Specify the URL in the dashboard. In the [push composer]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#step-3-select-notification-type-ios-and-android), select **Settings** and enter the protocol URL in the **Sound** field. 

![The push composer in the Braze dashboard]({% image_buster /assets/img_archive/sound_push_ios.png %})

If the specified sound file doesn't exist or the keyword "default" is entered, Braze will use the default device alert sound. Aside from our dashboard, sound can also be configured via our [messaging API][12].

See the Apple Developer Documentation regarding [preparing custom alert sounds](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html) for additional information.
