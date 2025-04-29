---
nav_title: Safari Mobile の Web プッシュ
article_title: Safari Mobile の Web プッシュ
platform: Web
channel: push
page_order: 5
page_type: reference
description: "この参考記事では、iOSとiPadのSafariブラウザでウェブプッシュを統合する方法を説明する。"
search_rank: 3
---

# Safariモバイルウェブプッシュ（iOSおよびiPadOS）

> [Safari v16.4](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes) はモバイルウェブプッシュに対応しており、iOS と iPadOS のプッシュ通知でモバイルユーザーを再度エンゲージできるようになりました。<br><br>この記事では、サファリのモバイルプッシュを設定するために必要な手順を説明する。

## 統合のステップ

まず、標準的な [Web プッシュ統合ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/)を読み、それに従ってください。以下のステップは、iOS と iPadOS サポートの Safari で Web プッシュをサポートするためにのみ必要です。

### ステップ1:マニフェスト・ファイルを作成する {#manifest}

[ウェブ・アプリケーション・マニフェストは](https://developer.mozilla.org/en-US/docs/Web/Manifest)、ユーザーのホーム画面にインストールされたときに、ウェブサイトがどのように表示されるかを制御するJSONファイルである。

例えば、[App Switcherが](https://support.apple.com/en-us/HT202070)使用する背景のテーマカラーやアイコン、ネイティブアプリのようにフルスクリーンでレンダリングするかどうか、アプリをランドスケープモードで開くかポートレートモードで開くかなどを設定できる。

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

サポートされるフィールドの全リストは[こちらで](https://developer.mozilla.org/en-US/docs/Web/Manifest)見ることができる。

### ステップ2:マニフェストファイルをリンクする {#manifest-link}

ウェブサイトの`<head>` 要素に、マニフェストファイルがホストされている場所を指す次の`<link>` タグを追加する。

```html
<link rel="manifest" href="/manifest.json" />
```

### ステップ3:サービスワーカーを追加する {#service-worker}

[Web プッシュ統合ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-1-configure-your-sites-service-worker)で説明されているように、Web サイトには Braze service-worker ライブラリをインポートするサービスワーカーファイルが必要です。

### ステップ4: ホーム画面に追加する {#add-to-homescreen}

ChromeやFirefoxのような主要ブラウザとは異なり、あなたのウェブサイトがユーザーのホーム画面に追加されていない限り、サファリiOS/iPadOSでプッシュ許可をリクエストすることはできない。 

[[ホーム画面に追加](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc)] 機能を使用すると、ユーザーはあなたの Web サイトをブックマークし、あなたのサイトのアイコンをホーム画面に追加できます。

![ウェブサイトをブックマークし、ホーム画面に保存するためのオプションを示すiPhone ]({% image_buster /assets/img/push_implementation_guide/add-to-homescreen.png %}){: style="max-width:40%"}

### ステップ5: ネイティブのプッシュプロンプトを表示する {#push-prompt}
アプリがホーム画面に追加されると、ユーザーがアクション（ボタンのクリックなど）を起こしたときにプッシュ許可をリクエストできるようになる。これを行うには、[`requestPushPermission`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission) メソッドを使用するか、[コードなしのプッシュプライマーのアプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/)を使用します。

{% alert note %}
プロンプトを受け入れるか拒否したら、プロンプトを再び表示できるようにするには、Web サイトを削除してホーム画面に再インストールする必要があります。
{% endalert %}

![通知を「許可する」か「許可しない」かを尋ねるプッシュプロンプト]({% image_buster /assets/img/push_implementation_guide/safari-mobile-push-prompt.png %}){: style="max-width:40%"}

以下に例を示します。

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

次に、自分自身に[テスト・メッセージを送って]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/)、統合を検証する。統合が完了したら、プッシュオプトイン率を最適化するために、[コードなしのプッシュプライマーメッセージを]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/)使用することができる。

