---
nav_title: HTML による YouTube
article_title: Android と FireOS のHTML アプリ内メッセージの YouTube
platform: 
  - Android
  - FireOS
page_order: 8
description: "このリファレンス記事では、Android または FireOS アプリケーションの HTML アプリ内メッセージに YouTube 動画を追加する方法について説明します。"
channel:
  - in-app messages

---

# HTML による YouTube

> YouTube やその他の HTML5コンテンツは、HTML アプリ内メッセージで再生できます。これには、アプリ内メッセージが表示されるアクティビティでハードウェアアクセラレーションが有効になっている必要があります。詳細については、[Android 開発者ガイド](https://developer.android.com/guide/topics/graphics/hardware-accel.html#controlling)を参照してください。ハードウェアアクセラレーションは、Android API バージョン11以降でのみ利用できます。

以下は、HTML スニペットに YouTube 動画を埋め込んだ例です。

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

