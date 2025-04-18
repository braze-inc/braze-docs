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

> To play a video in an HTML in-app message, include the following `<video>` element in your HTML, and replace the video names with your file's name (or the remote asset's URL). You can find other possible `<video>` options on [MDN Web Docs][9].

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

## iOS considerations

To support iOS devices:

- You must include the `playsinline` attribute because full screen playback is not supported at this time.
- iOS does not support auto-play by default. To update this default option, you can modify the [`ABKInAppMessageHTMLViewController`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ViewControllers/ABKInAppMessageHTMLViewController.m)

## Accessibility considerations

When adding video to an in-app message, keep the following best practices in mind to support a more inclusive experience:

- **Avoid auto-play.** Automatically playing video can be disruptive for users with motion sensitivity, screen reader users, or anyone who prefers to control playback themselves.
- **Always include playback controls.** Users should be able to start and stop videos on their own terms.
- **Provide captions or subtitles.** Captions ensure that Deaf and hard-of-hearing users—and anyone in a sound-off environment—can access your video content.

For more tips on making your messages accessible, see our [Building accessible messages]({{site.baseurl}}/help/accessibility/) guide.


[9]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video
