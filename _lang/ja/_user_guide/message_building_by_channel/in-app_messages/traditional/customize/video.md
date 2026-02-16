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

**自動再生**:ハードウェアアクセラレーションを有効にした場合でも、Android WebView でメディア再生を始めるにはユーザージェスチャが必要になることがあります。自動再生が必要な場合は、HTML アプリ内メッセージs のレンダリングに使用するWebView を設定して、設定[`WebSettings.setMediaPlaybackRequiresUserGesture(false)`](https://developer.android.com/reference/android/webkit/WebSettings#setMediaPlaybackRequiresUserGesture(boolean)) でユーザージェスチャ要件を無効にします。これには、HTML アプリ内メッセージの表示方法をSDKレベルでカスタマイズする必要があります。セットアップガイダンスについては、[Braze SDKのアプリ内メッセージのカスタマイズ]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android)を参照してください。

## iOSの考慮事項

iOS デバイスをサポートするには:

- フルスクリーン再生はサポートされていないため、`playsinline` 属性を含める必要があります。
- iOSでは**auto-playは保証されません。iOSの再生動作は`WKWebView`とOSレベルのメディアポリシーに依存し、`autoplay`と`muted`が設定されていてもユーザーなジェスチャが必要になる場合があります。目的のiOS 版および端末でHTML アプリ内メッセージをテストします。

自動再生が必要で、テストでデフォルトで動作しないことが示された場合は、HTML アプリ内メッセージ s で使用される`WKWebViewConfiguration` をカスタマイズして、`mediaTypesRequiringUserActionForPlayback` プロパティを設定するなどして、メディアプレイバックのユーザー-アクション条件を調整できます。これには、SDKレベルのカスタマイズが必要です。Swift リソースについては、[Braze SDK]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=swift) のアプリ内メッセージs のカスタマイズおよび[Swift]({{site.baseurl}}/developer_guide/in_app_messages/html_messages/?sdktab=swift) のWebView へのBraze JavaScript インターフェイスの追加を参照してください。

## Webの考察

現代のほとんどのブラウザでは、特定の条件下(通常、動画がミュートされている場合)でのみ自動再生が可能です。Web アプリ内メッセージで`autoplay` を使用する場合は、`muted` を含めて、サポートされているブラウザとデバイスでテストします。ブラウザのポリシーは異なり、場合によってはユーザージェスチャが必要になることがあります。