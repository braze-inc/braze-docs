{% multi_lang_include developer_guide/prerequisites/web.md %} また、Web SDKの[プッシュ通知を設定する]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web)必要がある。なお、プッシュ通知を送信できるのは、[Safari v16.4](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes)以降を使用しているiOSおよびiPadOSユーザーだけである。

## モバイル用Safariプッシュの設定

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

一般的なブラウザ（Safari、Chrome、FireFox、Edgeなど）はすべて、それ以降のバージョンでWebプッシュ通知をサポートしている。iOSまたはiPadOSでプッシュ権限を要求するには、**Share To**>**Add to Home Screenを**選択して、Webサイトをユーザーのホーム画面に追加する必要がある。[Add to Homescreenは](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc)、ユーザーがWebサイトをブックマークし、貴重なホーム画面の領域にあなたのアイコンを追加することができる。

![ウェブサイトをブックマークし、ホーム画面に保存するオプションを表示するiPhone]({% image_buster /assets/img/push_implementation_guide/add-to-homescreen.png %}){: style="max-width:40%"}

### ステップ5:ネイティブのプッシュプロンプトを表示する {#push-prompt}
アプリがホーム画面に追加された後、ユーザーがアクション（ボタンのクリックなど）を起こしたときにプッシュアクションボタンを許可するようリクエストできるようになった。これを行うには、[`requestPushPermission`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission) メソッドを使用するか、[コードなしのプッシュプライマーのアプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)を使用します。

{% alert note %}
プロンプトを承認または拒否した後、プロンプトを再び表示できるようにするには、Webサイトを削除してホーム画面に再インストールする必要がある。
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
