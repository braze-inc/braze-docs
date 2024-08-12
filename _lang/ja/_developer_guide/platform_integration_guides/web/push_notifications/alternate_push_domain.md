---
nav_title: 代替 Web プッシュドメイン
article_title: 代替 Web プッシュドメイン
platform: Web
page_order: 20
page_type: reference
description: "この記事では、Braze Web Push を別のドメインに統合する方法について説明します。"
channel: push

---

# 代替 Web プッシュドメイン

> Web Push を統合するには、[ドメインが安全である必要があります][2]。一般的には`https`、`localhost`、と [W3C プッシュ標準で定義されているその他の例外がこれに該当します][1]。また、ドメインのルートに Service Worker を登録できるか、少なくともそのファイルの HTTP ヘッダーを制御できる必要があります。この記事では、Braze Web Push を別のドメインに統合する方法について説明します。

_これらの条件をすべて満たすことができない場合は_、このガイドを使用して、ウェブサイトにプッシュプロンプトダイアログを追加するための回避策を設定してください。たとえば、この記事は、`http`（安全ではない）Webサイトや、プッシュプロンプトが表示されないようにするブラウザ拡張ポップアップからユーザーにオプトインしてもらいたい場合に役立ちます。

## 注意事項
ウェブ上の多くの回避策と同様に、ブラウザは絶えず進化しており、将来的にはこれが意図したとおりに機能しなくなる可能性があることを覚えておいてください。

- これには以下が必要です。
  - 別の安全なドメイン (`https://`) を所有しており、そのドメインに Service Worker を登録するためのアクセス権があります。
  - プッシュトークンが同じプロファイルに紐付けられるように、ユーザーはウェブサイトにログインする必要があります。

{% alert note %}
Shopifyのプッシュをこの方法では実装できません。Shopifyは、プッシュ配信に必要なヘッダーを削除するための措置を講じています。
{% endalert %}

## 統合

次の例をわかりやすくするために、`https://secure.com`訪問者にプッシュオンを登録してもらうことを目的として、use `http://insecure.com` とを 2 `http://insecure.com` つのドメインとして使用します。この例は、`chrome-extension://`ブラウザ拡張機能のポップアップページのスキームにも適用できます。

### ステップ 1:プロンプトフローを開始

次に`insecure.com`、URL パラメータを使用してセキュアドメインへの新しいウィンドウを開き、現在ログインしているユーザーの Braze 外部 ID を渡します。

**http://insecure.com**
\`\`\`html
<button id="opt-in">プッシュのオプトイン</button>
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

### ステップ 2: プッシュ登録

この時点で、`secure.com`同じユーザーIDのBraze Web SDKを初期化し、ユーザーにWebプッシュの許可をリクエストできるポップアップウィンドウが開きます。

**https://secure.com/push-registration.html**

<script src="https://braze-inc.github.io/embed-like-gist/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Falternate-push-domain-registration.html&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

### ステップ 3: ドメイン間の通信 (オプション)

ユーザーが開始したこのワークフローからオプトインできるようになったので`insecure.com`、ユーザーがすでにオプトインしているかどうかに基づいてサイトを変更したい場合があります。すでに登録している場合、ユーザーにプッシュの登録を依頼しても意味がありません。

iFrame と [`postMessage`][3]API を使用して 2 つのドメイン間で通信できます。 

**insecure.com**

`insecure.com`私たちのドメインでは、現在のユーザーのプッシュ登録に関する情報をセキュアドメイン（_実際にプッシュが登録されているドメイン_）に問い合わせます。

\`\`\`html
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
