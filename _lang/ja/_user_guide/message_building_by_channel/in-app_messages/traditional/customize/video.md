---
nav_title: 動画
article_title: アプリ内メッセージの動画
page_order: 4
page_type: reference
description: "この記事では、ビデオをHTMLアプリ内メッセージに埋め込む方法について説明します。"
channel:
  - in-app messages
---

# ビデオ {#video}

> HTML アプリ内メッセージでビデオを再生するには、HTML に次の `<video>` 要素を含め、動画名を実際のファイル名 (またはリモートアセットの URL) に置き換えます。他の可能な`<video>`オプションは[MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video)で見つけることができます。

```html
<video class="video" autoplay muted playsinline controls>
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.mp4" type="video/mp4">
  <source src="https://video-provider.com/YOUR_VIDEO_FILE.ogg" type="video/ogg">
  Your device does not support playing this video.
</video>
```

ローカル動画アセットを使用するには、アセットをキャンペーンにアップロードする際にこのファイルを含めるようにしてください。

{% alert note %}
動画コンテンツは、デバイスが適切なネットワーク速度を持っている場合にのみ利用可能です。ただし、動画がデバイスからローカルに供給されている場合を除きます。
{% endalert %}

## Androidに関する考慮事項

Android 上の HTML アプリ内メッセージに動画およびその他の HTML5 コンテンツを埋め込むには、アプリ内メッセージが表示されるアクティビティでハードウェアアクセラレーションを有効にする必要があります。詳細については、[Android開発者ガイド]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/#android_embedding-youtube-content)を参照してください。

## iOSの考慮事項

iOS デバイスをサポートするには:

- この時点ではフルスクリーン再生がサポートされていないため、`playsinline`属性を含める必要があります。
- iOSはデフォルトで自動再生をサポートしていません。このデフォルトオプションを更新するには、[`ABKInAppMessageHTMLViewController`](https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyUI/ABKInAppMessage/ViewControllers/ABKInAppMessageHTMLViewController.m)を変更できます。


