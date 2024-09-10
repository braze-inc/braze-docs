---
nav_title: SAML SSO の設定
article_title: SAML SSO の設定
page_order: 0
page_type: tutorial
description: "この記事では、Braze アカウントの SAML シングルサインオンを有効にする方法を順に説明します。"

---

# サービスプロバイダー (SP) が開始するログイン

> この記事では、Braze アカウントの SAML シングルサインオンを有効にする方法を順に説明します。

## 要件

設定時に、サインオン URL と Assertion Consumer Service (ACS) の URL を指定するように求められます。  

| 必要条件 | 詳細 |
|---|---|
| アサーション・コンシューマー・サービス（ACS）URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback`<br><br> 欧州連合のドメインの場合、ASCのURLは`https://<SUBDOMAIN>.braze.eu/auth/saml/callback` 。<br><br> IdPによっては、これはReply URL、Sign-On URL、Audience URL、または Audience URIとも呼ばれる。 |
| エンティティID | `braze_dashboard` |
| RelayState APIキー | **Settings（設定）**＞**API Keys（APIキー**）に進み、`sso.saml.login` 権限を持つAPIキーを作成し、生成されたAPIキーをIdP内の`RelayState` パラメータとして入力する。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、API キーは \[**開発者コンソール**] > \[**API 設定**] の \[**設定**] にあります。
{% endalert %}

## SAML SSO の設定

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

アカウントマネージャーがアカウントの SAML SSO をオンにしたら、\[**設定**] > \[**管理者設定**] > ［**セキュリティ設定**］ に移動し、［SAML SSO］ セクションを \[**オン**] に切り替えます。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、アカウントアイコンを選択し、\[**会社の設定**] > \[**セキュリティ設定**] に移動して、\[SAML SSO] セクションを見つけます。
{% endalert %}

そのページで、次の項目を入力します。

| 必要条件 | 詳細 |
|---|---|
| `SAML Name` | これはログイン画面のボタンテキストとして表示される。<br>これは通常、「Okta」のようなIDプロバイダの名前である。 |
| `Target URL` | これは、IdP内でBrazeをセットアップした後に提供される。<br> 一部の IdP は、これを SSO URL または SAML 2.0 Endpoint と呼ぶ。 |
| `Certificate` | ID プロバイダが提供する`x.509` 証明書。|
{: .reset-td-br-1 .reset-td-br-2}

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
