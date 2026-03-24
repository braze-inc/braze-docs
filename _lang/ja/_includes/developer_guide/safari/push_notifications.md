{% multi_lang_include developer_guide/prerequisites/web.md %} Web SDK用の[プッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)も[設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)する必要がある。iOSおよびiPadOSユーザーにプッシュ通知を送信できるのは、[Safari v16.4](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes)以降を使用している場合に限られることに注意せよ。

## モバイル向けSafariプッシュ通知の設定

### ステップ 1: マニフェスト・ファイルを作成する {#manifest}

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

主要なブラウザ（Safari、Chrome、FireFox、Edgeなど）は、いずれも最新版でWeb プッシュ通知をサポートしている。iOSまたはiPadOSでプッシュ通知の権限を求めるには、ユーザーが**「共有」**＞「ホーム画面**に追加**」を選択して、あなたのWeb サイトをホーム画面に追加する必要がある。[ホーム画面に追加機能は](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc)、ユーザーがあなたの Web サイトをブックマークできるようにする。これにより、あなたのアイコンがユーザーの貴重なホーム画面スペースに追加されるのだ。

![ウェブサイトをブックマークし、ホーム画面に保存するオプションを表示するiPhone]({% image_buster /assets/img/push_implementation_guide/add-to-homescreen.png %}){: style="max-width:40%"}

### ステップ5:ネイティブのプッシュプロンプトを表示する {#push-prompt}
アプリがホーム画面に追加された後、ユーザーがアクション（ボタンをクリックするなど）を行った際にプッシュ通知の権限をリクエストできるようになる。これを行うには、[`requestPushPermission`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission) メソッドを使用するか、[コードなしのプッシュプライマーのアプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)を使用します。

{% alert note %}
プロンプトを受け入れるか拒否した後、再度プロンプトを表示するには、Web サイトをホーム画面から削除し、再インストールする必要がある。
{% endalert %}

![通知を「許可する」か「許可しない」かを尋ねるプッシュ・プロンプトが表示される。]({% image_buster /assets/img/push_implementation_guide/safari-mobile-push-prompt.png %}){: style="max-width:40%"}

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

次に、自分自身に[テスト・メッセージを送って]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/)、統合を検証する。統合が完了したら、プッシュオプトイン率を最適化するために、[コードなしのプッシュプライマーメッセージを]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)使用することができる。
