---
nav_title: 代替Webプッシュドメイン
article_title: 代替Webプッシュドメイン
platform: Web
page_order: 20
page_type: reference
description: "ここでは、代替ドメイン上のBraze Webプッシュを統合する方法について説明します。"
channel: push

---

# 代替Web プッシュ領域

> Web プッシュ を統合するには、ドメインが[secure][2] である必要があります。これは、一般に`https`、`localhost`、および[W3C プッシュ標準][1] で定義されている他の例外を意味します。また、ドメインのルートにサービスワーカーを登録するか、少なくともそのファイルのHTTP ヘッダーs にコントロールできる必要があります。ここでは、代替ドメイン上のBraze Webプッシュを統合する方法について説明します。

_これらの条件をすべて満たすことができない場合は、このガイドを使用して、Web サイトにプッシュプロンプトダイアログを追加できる回避策を設定します。たとえば、ユーザーが`http`(安全でない)Web サイトからオプトインするか、プッシュプロンプトが表示されないブラウザ拡張ポップアップからオプトインする場合に、この記事は役立ちます。

## 注意事項
Web上の多くの回避策と同様に、ブラウザは継続的に進化し、将来は意図したとおりに動作しない可能性があることに留意してください。

- これには以下が必要です。
  - 別のセキュア・ドメイン(`https://`)を所有し、そのドメインにサービス・ワーカーを登録するためのアクセス権を持っていること。
  - Web サイトにログインするユーザは、プッシュトークンが同じプロファイルs に関連付けられていることを確認します。

{% alert note %}
この方法では、プッシュ・フォー・Shopifyは実装できません。Shopify は、プッシュを配信するために必要なヘッダーs を削除するためにステップs を使用します。
{% endalert %}

## 統合

次の例を明確にするために、`http://insecure.com` と`https://secure.com` を2 つのドメインとして使用します。訪問者が`http://insecure.com` にプッシュ登録することを目的としています。この例題は、ブラウザー拡張のポップアップページの`chrome-extension://`スキームにアプリ当てはまるかもしれません。

### ステップ1:プロンプトフローの開始

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

### ステップ2:プッシュ用レジスタ

この時点で、`secure.com` はポップアップウィンドウを開封します。ポップアップウィンドウでは、同じユーザー IDのBraze Web SDKを初期化し、Webプッシュに対するユーザーの権限をリクエストできます。

**https://secure.com/push-registration.html**

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Falternate-push-domain-registration.html&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

### ステップ3:ドメイン間の通信(オプション)

ユーザーが`insecure.com` で生成されたこのワークフローからオプトインできるようになったので、ユーザーがすでにオプトインされているかどうかに基づいてサイトを変更することができます。ユーザーに、すでにプッシュを登録しているかどうかを尋ねる意味はありません。

iFrames と [`postMessage`][3] API を使用して、2 つのドメイン間で通信できます。 

**insecure.com**

`insecure.com` ドメインでは、セキュアなドメイン(push は_実際に_ 登録済み) に、カレントユーザーのプッシュ登録に関する情報を問い合わせます。

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

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Falternate-push-domain-status.html&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

[1]: https://www.w3.org/TR/service-workers/#security-considerations
[2]: https://w3c.github.io/webappsec-secure-contexts/
[3]: https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage
