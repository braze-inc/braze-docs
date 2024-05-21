---
nav_title: 動画
article_title: アプリ内メッセージ内の動画
page_order: 4
page_type: reference
description: "この記事では、HTML アプリ内メッセージに動画を埋め込む方法について説明します。"
channel:
  - in-app messages
---

# ビデオ {#video}

> HTML アプリ内メッセージで動画を再生するには、HTML `<video>` に次の要素を含め、動画名をファイル名 (またはリモートアセットのURL) に置き換えます。[MDN Web Docs `<video>`][9] には他にも可能なオプションがあります。

```html
<video class="video" autoplay muted playsinline controls>
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.mp4" type="video/mp4">
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.ogg" type="video/ogg">
  Your device does not support playing this video.
</video>
```

ローカル動画アセットを使用するには、キャンペーンにアセットをアップロードするときにこのファイルを必ず含めてください。

{% alert note %}
ビデオコンテンツは、ビデオがデバイスからローカルに供給されている場合を除き、デバイスのネットワーク速度が適度な場合にのみ利用できます。
{% endalert %}

## アンドロイドに関する注意事項

Android の HTML アプリ内メッセージに動画やその他の HTML5 コンテンツを埋め込むには、アプリ内メッセージが表示されるアクティビティでハードウェアアクセラレーションを有効にする必要があります。詳細については、[Android デベロッパーガイドを参照してください]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/youtube_in_html/)。

## iOS に関する注意事項

iOS デバイスをサポートするには、`playsinline`この属性を含める必要があります。フルスクリーン再生は現時点ではサポートされていないためです。

- iOSはデフォルトでは自動再生をサポートしていません。このデフォルトオプションを更新するには、以下を変更します。 [`ABKInAppMessageHTMLViewController`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ViewControllers/ABKInAppMessageHTMLViewController.m)
- フルスクリーンビデオは iOS では正しくレンダリングされないため、現時点ではサポートされていません。代わりに、HTML `playsinline` メッセージ内に動画を表示する属性を含める必要があります。

[9]: https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video
