---
nav_title: SAML SSO の設定
article_title: SAML SSO の設定
page_order: 0
page_type: tutorial
description: "この記事では、Braze アカウントの SAML シングルサインオンを有効にする方法を順に説明します。"

---

# サービスプロバイダー (SP) が開始するログイン

> この記事では、BrazeアカウントのSAMLシングルサインオンを有効にする方法と、SAMLトレースを取得する方法を説明する。

## 要件

設定時に、サインオン URL と Assertion Consumer Service (ACS) の URL を指定するように求められます。  

| 必要条件 | 詳細 |
|---|---|
| アサーションコンシューマーサービス (ACS) の URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback`<br><br> 欧州連合のドメインの場合、ASCのURLは`https://<SUBDOMAIN>.braze.eu/auth/saml/callback` 。<br><br> IdP によっては、これを応答 URL、サインオン URL、オーディエンス URL、またはオーディエンス URI と呼ぶこともあります。 |
| エンティティ ID | `braze_dashboard` |
| RelayState APIキー | **Settings（設定）**＞**API Keys（APIキー**）に進み、`sso.saml.login` 権限を持つAPIキーを作成し、生成されたAPIキーをIdP内の`RelayState` パラメータとして入力する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、API キーは [**開発者コンソール**] > [**API 設定**] の [**設定**] にあります。
{% endalert %}

## SAML SSOの設定

### ステップ 1: ID プロバイダーの設定

ID プロバイダー (IdP) で以下の情報を指定して、Braze をサービスプロバイダー (SP) として設定します。さらに、SAML 属性マッピングを設定します。

{% alert important %}
ID プロバイダーとして Okta を使用する予定がある場合は、必ず [Okta のサイト](https://www.okta.com/integrations/braze/)にあるビルド済みの連携を使用してください。
{% endalert %}

| SAML 属性 | 必要か？ | 許容される SAML 属性 |
|---|---|---|
|`email` | required | `email`<br> `mail`<br> `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/email` |
| `first_name` | オプション | `first_name`<br> `firstname`<br> `firstName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/first_name` |
| `last_name` | オプション | `last_name`<br> `lastname`<br> `lastName`<br>`http://schemas.xmlsoap.org/ws/2005/05/identity/claims/last_name` |

{% alert note %}
Braze は SAML アサーションに `email` のみが必要です。
{% endalert %}

### ステップ 2: Braze の設定

ID プロバイダーでの Braze の設定が完了すると、Braze アカウントに入力するターゲット URL と `x.509` 証明書が ID プロバイダーから提供されます。

アカウントマネージャーがアカウントの SAML SSO をオンにしたら、[**設定**] > [**管理者設定**] > ［**セキュリティ設定**］ に移動し、［SAML SSO］ セクションを [**オン**] に切り替えます。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、アカウントアイコンを選択し、[**会社の設定**] > [**セキュリティ設定**] に移動して、[SAML SSO] セクションを見つけます。
{% endalert %}

そのページで、次の項目を入力します。

| 必要条件 | 詳細 |
|---|---|
| `SAML Name` | これは、ログイン画面にボタンのテキストとして表示されます。<br>これは通常、「Okta」のような ID プロバイダーの名前です。 |
| `Target URL` | これは、IdP 内で Braze を設定した後に提供されます。<br> IdP によってはこれを SSO URL または SAML 2.0 エンドポイントと呼びます。 |
| `Certificate` | ID プロバイダが提供する`x.509` 証明書。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

ダッシュボードに `x.509` 証明書を追加するときに、次の形式になっていることを確認してください。

```
-----BEGIN CERTIFICATE-----
<certificate>
-----END CERTIFICATE-----
```

![セキュリティ設定を開き、SAML SSOの詳細を追加する]({% image_buster /assets/img/samlsso.gif %})

### ステップ 3:Braze へのサインイン

セキュリティ設定を保存してログアウトします。次に、ID プロバイダーにサインインし直します。

![SSOを有効にしたダッシュボードのログイン画面]({% image_buster /assets/img/sso1.png %}){: style="max-width:40%;"}

## SSO の動作

SSO の利用を選択したメンバーは、以前とは異なり、パスワードを利用できなくなります。パスワードを使用し続けるユーザーは、以下の設定によって制限されない限り、パスワードを使用できます。

## 制限

サインインに Google SSO または SAML SSOのいずれかのみを使用するように、組織のメンバーを制限できます。制限をオンにするには、［**セキュリティ設定**］ に移動し、［**Google SSO のみのログインを強制する**］、または ［**カスタム SAML SSO のみのログインを強制する**］ のいずれかを選択します。

![セキュリティ設定ページの「認証ルール」セクション]({% image_buster /assets/img/sso3.png %})

制限をオンにすると、たとえ以前にパスワードでログインしていたとしても、会社の Braze ユーザーはパスワードを使用したログインができなくなります。

## SAML トレースを取得する。

SSO に関連するログインの問題が発生した場合、SAML トレースを取得することで、SAML要求で送信された内容を特定して、SSO 接続のトラブルシューティングに役立てることができます。

### 前提条件

SAMLトレースを実行するには、SAMLトレーサが必要である。以下は、お使いのブラウザに応じた2つのオプションである：

- [Google Chrome](https://chromewebstore.google.com/detail/saml-tracer/mpdajninpobndbfcldcmbpnnbhibjmch)
- [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/saml-tracer/)

### ステップ 1: SAML トレーサを開く

ブラウザのナビゲーション・バーから SAML トレーサを選択する。「**一時停止**」が選択されていないことを確認します。一時停止を選択すると、SAML トレーサが SAML リクエストで送信された内容をキャプチャできなくなるためです。SAML トレーサを開くと、トレースに入力されるのがわかります。

![Google Chrome 用 SAML トレーサー]({% image_buster /assets/img/saml_tracer_example.png %})

### ステップ 2: SSOを使ってBrazeにサインインする

Brazeのダッシュボードに行き、SSOを使ってサインインを試みる。エラーが発生した場合は、SAML トレーサを開いて再試行します。`https://dashboard-XX.braze.com/auth/saml/callback` のような URL の行があり、オレンジ色の SAML タグがあれば、SAML トレースは正常に収集されている。

### ステップ 3:エクスポートしてBrazeに送る

[**エクスポート**] を選択します。**Select Cookie-filter profile "**で "**None "**を選択する。次に [**エクスポート**] を選択します。これでJSONファイルが生成され、Brazeサポートに送信してさらにトラブルシューティングを行うことができる。

![[Export SAML-trace preferences] メニューで [None] オプションが選択されている。]({% image_buster /assets/img/export_saml_trace_preferences.png %})
