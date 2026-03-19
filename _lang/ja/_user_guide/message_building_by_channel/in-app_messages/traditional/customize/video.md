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

**自動再生**ハードウェアアクセラレーションのイネーブルメントを有効にしている場合でも、Android WebViewではメディア再生を開始するためにユーザーの操作が必要になることがある。自動再生が必要な場合、アプリ内メッセージのHTMLレンダリングに使用するWebViewの設定で[`WebSettings.setMediaPlaybackRequiresUserGesture(false)`](https://developer.android.com/reference/android/webkit/WebSettings#setMediaPlaybackRequiresUserGesture(boolean))、ユーザー操作の要求を無効にする必要がある。これは、アプリ内メッセージのHTML表示方法をSDKレベルでカスタマイズする必要がある。設定の手順については、[Braze SDKのアプリ内メッセージのカスタマイズを]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android)参照せよ。

## iOSの考慮事項

iOS デバイスをサポートするには:

- フルスクリーン再生はサポートされていないため、この`playsinline`属性を必ず含めなければならない。
- **iOSでは自動再生は保証されない**。iOSの再生動作はOSレベル`WKWebView`でのメディアポリシーに依存し、[`muted`設定]と[設定]`autoplay`が有効な場合でもユーザー操作が必要となる場合がある。対象のiOSバージョンとデバイスで、アプリ内メッセージのHTMLをテストせよ。

自動再生が必要な場合で、テストによりデフォルトでは機能しないことが判明したときは、HTMLアプリ内メッセージで使用される`WKWebViewConfiguration` をカスタマイズできる。例えば の`mediaTypesRequiringUserActionForPlayback`プロパティを設定することで、メディア再生におけるユーザーアクション要件を調整できる。これはSDKレベルのカスタマイズが必要だ。Swiftのリソースについては、[Braze SDKのアプリ内メッセージのカスタマイズ]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=swift)と、[Swift向けWebViewへのBraze JavaScriptインターフェイスの追加を]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/?sdktab=swift)参照のこと。

## Web上の考慮事項

ほとんどの現代のブラウザは、特定の条件下でのみ自動再生を許可している（一般的に動画がミュートされている場合である）。ウェブアプリ内メッセージ`autoplay`で  を使用する場合、  を含め`muted`、サポート対象のブラウザとデバイスでテストすること。ブラウザのポリシーは異なり、場合によってはユーザーの操作を依然として必要とする可能性があるためだ。