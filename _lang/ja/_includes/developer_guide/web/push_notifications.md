{% multi_lang_include archive/web-v4-rename.md %}

{% multi_lang_include developer_guide/prerequisites/web.md %}

## プッシュ・プロトコル

Web プッシュ通知は、大部分の主要ブラウザーでサポートされている [W3C プッシュ標準](http://www.w3.org/TR/push-api/)を使用します。特定のプッシュ・プロトコルの標準やブラウザのサポートについての詳細は、[アップル社や](https://developer.apple.com/notifications/safari-push-notifications/) [モジラ社](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility)、[マイクロソフト](https://developer.microsoft.com/en-us/microsoft-edge/status/pushapi/)社のリソースを参照されたい。

## プッシュ通知の設定

### ステップ 1: サービスワーカーを設定する

プロジェクトの`service-worker.js` ファイルに以下のスニペットを追加し、Web SDKの初期化時に初期化オプションを に設定する。 [`manageServiceWorkerExternally`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)初期化オプションを`true` に設定する。

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

{% alert important %}
サービスワーカーファイルを提供するときは、Web サーバーが `Content-Type: application/javascript` を返す必要があります。さらに、サービスワーカーファイルの名前が`service-worker.js` でない場合は、`serviceWorkerLocation` [初期化オプションを](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions)使う必要がある。
{% endalert %}

### ステップ 2:ブラウザを登録する

ブラウザがプッシュ通知を受け取れるように、ユーザーにプッシュ権限を即座に要求するには、`braze.requestPushPermission()` 。プッシュが相手のブラウザでサポートされているかどうかをテストするには、まず`braze.isPushSupported()` に電話する。

また、プッシュ権限を要求する前にユーザーに[ソフトプッシュプロンプトを送り]({{site.baseurl}}/developer_guide/push_notifications/soft_push_prompts/?sdktab=web)、独自のプッシュ関連UIを表示させることもできる。

{% alert important %}
macOSでは、プッシュ通知を表示する前に、**Google Chromeと** **Google Chrome Helper（Alerts）の**両方をエンドユーザーが**システム設定＞通知で**イネーブルメントにする必要がある（権限が与えられていても）。
{% endalert %}

### ステップ 3:`skipWaiting` を無効にする（オプション）。

Brazeサービスワーカーファイルは、インストール時に自動的に`skipWaiting` 。この機能を無効にしたい場合は、Brazeをインポートした後、サービスワーカーファイルに以下のコードを追加する：

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fservice-worker-skip-waiting.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## ユーザーの配信停止

ユーザーの配信停止は、`braze.unregisterPush()` 。

{% alert important %}
SafariとFirefoxの最近のバージョンでは、（ボタンをクリックするハンドラやソフトプッシュプロンプトのような）短時間のイベントハンドラからこのメソッドを呼び出す必要がある。これは、プッシュ登録に関する [Chrome のユーザーエクスペリエンスのベストプラクティス](https://docs.google.com/document/d/1WNPIS_2F0eyDm5SS2E6LZ_75tk6XtBSnR1xNjWJ_DPE)と一致しています。
{% endalert %}

## 代替ドメイン

Web プッシュを統合するには、ドメインが[セキュア](https://w3c.github.io/webappsec-secure-contexts/)である必要があります。一般にこれは、`https`、`localhost`、および [W3C プッシュ標準](https://www.w3.org/TR/service-workers/#security-considerations)で定義されているその他の例外である必要があります。また、ドメインのルートにサービスワーカーを登録するか、少なくともそのファイルの HTTP ヘッダーを制御できる必要もあります。この記事では、代替ドメイン上で Braze Web プッシュを統合する方法について説明します。

### ユースケース

[W3Cプッシュ標準に](https://www.w3.org/TR/service-workers/#security-considerations)概説されている基準をすべて満たすことができない場合は、この方法を使用して、代わりにWebサイトにプッシュ・プロンプト・ダイアログを追加することができる。これは、`http` Webサイトやブラウザ拡張機能のポップアップがプッシュプロンプトの表示を妨げている場合に、ユーザーにオプトインさせたい場合に役立つ。

### 考慮事項

Web上の多くの回避策がそうであるように、ブラウザは絶えず進化しており、この方法は将来的に実行不可能になる可能性があることを覚えておいてほしい。続行する前に、以下を確認する：

- あなたは別のセキュアドメイン（`https://` ）を所有し、そのドメインにサービスワーカーを登録する権限を持つ。
- ユーザーはWebサイトにログインし、プッシュトークンが正しいプロファイルに一致することを確認する。

{% alert important %}
Shopifyのプッシュ通知を実装するために、このメソッドを使用することはできない。Shopifyは、この方法でプッシュ配信に必要なヘッダーを自動的に削除する。
{% endalert %}

### 代替プッシュ・ドメインの設定

次の例をわかりやすくするために、訪問者を `http://insecure.com` でのプッシュに登録させることを目的として、`http://insecure.com` と `https://secure.com` の2つのドメインを使用します。この例題は、ブラウザー拡張のポップアップページの`chrome-extension://`スキームにアプリ当てはまるかもしれません。

#### ステップ1:プロンプトフローを開始する

`insecure.com` で、URL パラメータを使用してセキュアドメインに新しいウィンドウを開封し、現在ログイン中のユーザーのBraze外部ID を渡します。

**http://insecure.com**
```html
<button id="opt-in">Opt-In For Push</button>
<script>
// the same ID you would use with `braze.changeUser`:
const user_id = getUserIdSomehow();
// pass the user ID into the secure domain URL:
const secure_url = `https://secure.com/push-registration.html?external_id=${user_id}`;

// when the user takes some action, open the secure URL in a new window
document.getElementById("opt-in").onclick = function(){
    if (!window.open(secure_url, 'Opt-In to Push', 'height=500,width=600,left=150,top=150')) {
        window.alert('The popup was blocked by your browser');
    } else {
        // user is shown a popup window
        // and you can now prompt for push in this window
    }
}
</script>
```

#### ステップ2:プッシュを登録する

この時点で、`secure.com` はポップアップウィンドウを開封します。ポップアップウィンドウでは、同じユーザー IDのBraze Web SDKを初期化し、Webプッシュに対するユーザーの権限をリクエストできます。

**https://secure.com/push-registration.html**

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Falternate-push-domain-registration.html&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### ステップ3:ドメイン間で通信する (オプション)

ユーザーは `insecure.com` から発生したこのワークフローからオプトインできるようになったため、ユーザーがすでにオプトインしているかどうかに基づいてサイトを変更できます。ユーザーがすでにプッシュを登録している場合、それを尋ねることに意味はありません。

iFrames と [`postMessage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) API を使用して、2つのドメイン間で通信できます。 

**insecure.com**

`insecure.com` ドメインで、現在のユーザーのプッシュ登録に関する情報を (プッシュが_実際に_登録されている) セキュアドメインに問い合わせます。

```html
<!-- Create an iframe to the secure domain and run getPushStatus onload-->
<iframe id="push-status" src="https://secure.com/push-status.html" onload="getPushStatus()" style="display:none;"></iframe>

<script>
function getPushStatus(event){
    // send a message to the iframe asking for push status
    event.target.contentWindow.postMessage({type: 'get_push_status'}, 'https://secure.com');
    // listen for a response from the iframe's domain
    window.addEventListener("message", (event) => {
        if (event.origin === "http://insecure.com" && event.data.type === 'set_push_status') {
            // update the page based on the push permission we're told
            window.alert(`Is user registered for push? ${event.data.isPushPermissionGranted}`);
        }
    }   
}
</script>
```

**secure.com/push-status.html**

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Falternate-push-domain-status.html&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## よくある質問（FAQ）

### サービスワーカー

#### ルートディレクトリにサービスワーカーを登録できない場合は？

デフォルトでは、サービスワーカーは、それが登録されているのと同じディレクトリ内でのみ使用できる。たとえば、サービスワーカーファイルが `/assets/service-worker.js` に存在する場合、`example.com/assets/*`、または `assets` フォルダーのサブディレクトリー内にのみ登録でき、ホームページ (`example.com/`) には登録できません。このため、ルートディレクトリ (`https://example.com/service-worker.js` など) にサービスワーカーをホストして登録することをお勧めします。

ルートドメインにサービスワーカーを登録できない場合、別の方法として、サービスワーカーファイルを提供するときに [`Service-Worker-Allowed`](https://w3c.github.io/ServiceWorker/#service-worker-script-response)HTTP ヘッダを使うことである。サービスワーカーのレスポンスに`Service-Worker-Allowed: /` を返すようにサーバーを設定することで、ブラウザにスコープを広げ、別のディレクトリから使用できるように指示する。

#### タグマネージャを使用してサービスワーカーを作成できますか?

いいえ、サービスワーカーは Web サイトのサーバーでホストされている必要があり、タグマネージャで読み込むことはできません。

### サイトのセキュリティ

#### HTTPSは必要か？

はい。ウェブ標準は、プッシュ通知の許可を要求するドメインが安全であることを要求している。

#### サイトが「安全」とみなされるのはどのような場合か？

サイトが以下のsecure-originパターンのいずれかに一致する場合、そのサイトは安全であるとみなされる。BrazeのWebプッシュ通知は、この開封標準に基づいて構築されているため、中間者攻撃を防ぐことができる。

- `(https, , *)`
- `(wss, *, *)`
- `(, localhost, )`
- `(, .localhost, *)`
- `(, 127/8, )`
- `(, ::1/128, *)`
- `(file, *, —)`
- `(chrome-extension, *, —)`

#### 安全なサイトが利用できない場合はどうするのか？

業界のベストプラクティスは、サイト全体をセキュアにすることですが、サイトドメインをセキュアにできない顧客は、セキュアなモーダルを使用して要件に対処できます。詳細については、[代替プッシュドメイン]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain)を使用するためのガイド、または[作業デモ](http://appboyj.com/modal-test.html)を確認してください。
