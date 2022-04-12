---
nav_title: Youtube in HTML
article_title: Youtube in HTML In-App Messages for Android and FireOS
platform: 
  - Android
  - FireOS
page_order: 8
description: "This reference article covers how to add Youtube videos into HTML in-app messages for your Android or FireOS application."
channel:
  - in-app messages

---

# YouTube in HTML in-app messages

YouTube and other HTML5 content can play in HTML in-app messages. This requires hardware acceleration to be enabled in the activity where the in-app message is being displayed; see the [Android developer guide][84] for more details. Hardware acceleration is only available on Android API versions 11 and later.

The following is an example of an embedded YouTube video in an HTML snippet:

```html
<body>
    <div class="box">
        <div class="relativeTopRight">
            <a href="appboy://close">X</a>
        </div>
        <iframe width="60%" height="50%" src="https://www.youtube.com/embed/_x45EB3BWqI">
        </iframe>
    </div>
</body>
```

[84]: https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling
