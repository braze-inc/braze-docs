---
nav_title: Safari モバイルウェブプッシュ
article_title: Safari モバイルウェブプッシュ
platform: Web
channel: push
page_order: 5
page_type: reference
description: "このリファレンス記事では、iOS およびiPad Safari ブラウザでWeb プッシュを統合する方法について説明します。"
search_rank: 3
---

# Safari Mobile Web プッシュ(iOS およびiPadOS)

> [Safari v16.4][safari-release-notes] はモバイルウェブプッシュをサポートしています。つまり、iOS およびiPadOS でモバイルユーザにプッシュ通知を再び適用できます。<br><br>この記事では、safari のモバイルプッシュのセットアップに必要な手順について説明します。

## 統合手順

まず、標準の[Web プッシュ統合ガイド][web-push-integration] を読み、それに従ってください。次の手順は、Safari for iOS およびiPadOS サポートでWeb プッシュをサポートする場合にのみ必要です。

### ステップ 1:マニフェストファイルの作成 {#manifest}

[Webアプリケーションマニフェスト][manifest-file]は、ユーザのホーム画面にインストールしたときにWebサイトをどのように表示するかを制御するJSONファイルです。

たとえば、[App Switcher][app-switcher] が使用する背景テーマの色とアイコンを、ネイティブアプリに似たフルスクリーンとしてレンダリングするかどうか、またはアプリを横向きまたは縦向きモードで開くかどうかを設定できます。

Web サイトのルートディレクトリに、次の必須フィールドを含む新しい`manifest.json` ファイルを作成します。 

```json
{
  "name": "your app name",
  "short_name": "your app name",
  "display": "fullscreen",
  "icons": [{
    "src": "favicon.ico",
    "sizes": "128x128",
  }]
}
```

サポートされるフィールドの完全なリストは、[here][manifest-file] にあります。

### ステップ 2: マニフェストファイルをリンクする {#manifest-link}

以下の`<link>` タグをウェブサイトの`<head>` 要素に追加し、マニフェストファイルがホストされている場所をポイントします。

```html
<link rel="manifest" href="/manifest.json" />
```

### ステップ 3: サービスワーカーの追加 {#service-worker}

Web サイトには、[Web プッシュ統合ガイド][service-worker] に記載されているように、Braze サービスワーカーライブラリをインポートするサービスワーカーファイルが必要です。

### ステップ 4: ホーム画面に追加 {#add-to-homescreen}

Chrome やFirefox などの主要なブラウザとは異なり、Web サイトがユーザのホーム画面に追加されていない限り、Safari iOS/iPadOS でプッシュ権限を要求することはできません。 

[ホーム画面に追加][add-to-homescreen]機能を使用すると、ユーザはウェブサイトをブックマークし、貴重なホーム画面の不動産にアイコンを追加できます。

![ウェブサイトをブックマークしてホーム画面に保存するためのオプションを表示するiPhone][1]{: style="max-width:40%"}

### ステップ 5: ネイティブプッシュプロンプトを表示する {#push-prompt}
アプリがホーム画面に追加されると、ユーザがアクション(ボタンをクリックするなど) を実行したときにプッシュ権限を要求できるようになります。これは、[`requestPushPermission`][requestPushPermission] メソッドを使用するか、[no-code push primer in-app message][push-primer] を使用して行うことができます。

{% alert note %}
プロンプトを承認または拒否すると、プロンプトを再度表示するには、ホーム画面からウェブサイトを削除して再インストールする必要があります。
{% endalert %}

!["allow" または"don't allow" Notifications][2] に尋ねるプッシュプロンプト{: style="max-width:40%"}

以下に例を示します。

\`\`\`typescript
import { requestPushPermission } from "@braze/web-sdk";

button.onclick = function(){
    requestPushPermission(() => {
        console.log(`User accepted push prompt`);
    }, (temporary) => {
        console.log(`User ${temporary ? "temporarily dismissed" : "permanently denied"} push prompt`);
    });
()
\`\`\`


## 次のステップ

次に、[test message][test-message] を送信して、統合を検証します。統合が完了したら、[no-code push primer messages][push-primer]を使用してプッシュオプトインレートを最適化できます。

[webkit-release-notes]: https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/
[safari-release-notes]: https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes
[manifest-file]: https://developer.mozilla.org/en-US/docs/Web/Manifest
[app-switcher]: https://support.apple.com/en-us/HT202070
[add-to-homescreen]: https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc
[web-push-integration]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/
[service-worker]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-1-configure-your-sites-service-worker
[test-message]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/
[push-primer]: {{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/
[requestPushPermission]: https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission
[1]: {% image_buster /assets/img/push_implementation_guide/add-to-homescreen.png %}
[2]: {% image_buster /assets/img/push_implementation_guide/safari-mobile-push-prompt.png %}
