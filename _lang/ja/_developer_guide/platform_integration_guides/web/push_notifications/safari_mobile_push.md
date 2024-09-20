---
nav_title: サファリ・モバイル・ウェブ・プッシュ
article_title: サファリ・モバイル・ウェブ・プッシュ
platform: Web
channel: push
page_order: 5
page_type: reference
description: "この参考記事では、iOSとiPadのSafariブラウザでウェブプッシュを統合する方法を説明する。"
search_rank: 3
---

# Safariモバイルウェブプッシュ（iOSおよびiPadOS）

> [Safari v16.4は][safari-release-notes]モバイル・ウェブ・プッシュに対応しており、iOSとiPadOSのプッシュ通知でモバイル・ユーザーを再度エンゲージできるようになった。<br><br>この記事では、サファリのモバイルプッシュを設定するために必要な手順を説明する。

## 統合のステップ

まず、標準的な[ウェブプッシュ統合ガイドを][web-push-integration]読み、それに従ってほしい。以下の手順は、iOSとiPadOSサポートのSafariでウェブプッシュをサポートするためにのみ必要である。

### ステップ1:マニフェスト・ファイルを作成する {#manifest}

[ウェブ・アプリケーション・マニフェストは][manifest-file]、ユーザーのホーム画面にインストールされたときに、ウェブサイトがどのように表示されるかを制御するJSONファイルである。

例えば、[App Switcherが][app-switcher]使用する背景のテーマカラーやアイコン、ネイティブアプリのようにフルスクリーンでレンダリングするかどうか、アプリをランドスケープモードで開くかポートレートモードで開くかなどを設定できる。

ウェブサイトのルート・ディレクトリに、以下の必須フィールドを含む新しい`manifest.json` ファイルを作成する。 

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

サポートされるフィールドの全リストは[こちらで][manifest-file]見ることができる。

### ステップ2:マニフェストファイルをリンクする {#manifest-link}

ウェブサイトの`<head>` 要素に、マニフェストファイルがホストされている場所を指す次の`<link>` タグを追加する。

```html
<link rel="manifest" href="/manifest.json" />
```

### ステップ3:サービスワーカーを追加する {#service-worker}

Web[プッシュ統合ガイドに][service-worker]記載されているように、WebサイトにBrazeサービスワーカーライブラリをインポートしたサービスワーカーファイルがなければならない。

### ステップ4: ホーム画面に追加する {#add-to-homescreen}

ChromeやFirefoxのような主要ブラウザとは異なり、あなたのウェブサイトがユーザーのホーム画面に追加されていない限り、サファリiOS/iPadOSでプッシュ許可をリクエストすることはできない。 

[ホームスクリーンに追加][add-to-homescreen]機能は、ユーザーがあなたのウェブサイトをブックマークし、貴重なホームスクリーンの領域にあなたのアイコンを追加することができる。

![ウェブサイトをブックマークし、ホーム画面に保存するオプションを表示するiPhone][1]{: style="max-width:40%"}

### ステップ5:ネイティブのプッシュプロンプトを表示する {#push-prompt}
アプリがホーム画面に追加されると、ユーザーがアクション（ボタンのクリックなど）を起こしたときにプッシュ許可をリクエストできるようになる。これは [`requestPushPermission`][requestPushPermission]メソッドを使うか、[コードなしのプッシュ・プライマー・アプリ内メッセージを][push-primer]使うことができる。

{% alert note %}
プロンプトを受け入れるか拒否するかを選択したら、プロンプトを再び表示できるようにするには、ウェブサイトを削除してホーム画面に再インストールする必要がある。
{% endalert %}

![通知を「許可する」か「許可しない」かを尋ねるプッシュ・プロンプトが表示される。][2]{: style="max-width:40%"}

以下はその例です。

```typescript
import { requestPushPermission } from "@braze/web-sdk";

button.onclick = function(){
    requestPushPermission(() => {
        console.log(`User accepted push prompt`);
    }, (temporary) => {
        console.log(`User ${temporary ? "temporarily dismissed" : "permanently denied"} push prompt`);
    });
};
```


## 次のステップ:

次に、自分自身に[テスト・メッセージを送って][test-message]、統合を検証する。統合が完了したら、[プッシュオプトイン][push-primer]率を最適化するために、[コードなしのプッシュプライマーメッセージを][push-primer]使用することができる。

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
