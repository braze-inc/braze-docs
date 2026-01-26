---
nav_title: Video
article_title: Video in In-App Messages
page_order: 4
page_type: reference
description: "This article describes how to embed videos into your HTML in-app messages."
channel:
  - in-app messages
---

# Video {#video}

> To play a video in an HTML in-app message, include the following `<video>` element in your HTML, and replace the video names with your file's name (or the remote asset's URL). You can find other possible `<video>` options on [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video).

```html
<video class="video" autoplay muted playsinline controls>
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.mp4" type="video/mp4">
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.ogg" type="video/ogg">
  Your device does not support playing this video.
</video>
```

To use a local video asset, be sure to include this file when uploading assets to your campaign.

{% alert note %}
Video content is only available when the device has a reasonable network speed, unless the video is sourced from the device locally.
{% endalert %}

## Android considerations

To embed video and other HTML5 content in HTML in-app messages on Android, hardware acceleration is required to be enabled in the Activity where the in-app message is displayed. For more information, refer to the [Android developer guide]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/#android_embedding-youtube-content).

**auto-play**: Even with hardware acceleration enabled, Android WebViews may require a user gesture to start media playback. If you need auto-play, configure the WebView used to render HTML in-app messages to disable the user gesture requirement by setting [`WebSettings.setMediaPlaybackRequiresUserGesture(false)`](https://developer.android.com/reference/android/webkit/WebSettings#setMediaPlaybackRequiresUserGesture(boolean)). This requires SDK-level customization of how HTML in-app messages are displayed. For setup guidance, see [Customize in-app messages for the Braze SDK]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android).

## iOS considerations

To support iOS devices:

- You must include the `playsinline` attribute because full screen playback is not supported.
- **auto-play is not guaranteed on iOS**. iOS playback behavior depends on `WKWebView` and OS-level media policies, and may require a user gesture even when `autoplay` and `muted` are set. Test your HTML in-app message on your target iOS versions and devices.

If auto-play is required and your tests show it doesn’t work by default, you can customize the `WKWebViewConfiguration` used by HTML in-app messages to adjust the media playback user-action requirement, for example by setting the `mediaTypesRequiringUserActionForPlayback` property. This requires SDK-level customization. For Swift resources, see [Customize in-app messages for the Braze SDK]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=swift) and [Adding the Braze JavaScript interface to WebViews for Swift]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/?sdktab=swift).

## Web considerations

Most modern browsers allow auto-play only under certain conditions (commonly when the video is muted). If you use `autoplay` in a web in-app message, include `muted` and test across your supported browsers and devices, as browser policies vary and may still require a user gesture in some cases.