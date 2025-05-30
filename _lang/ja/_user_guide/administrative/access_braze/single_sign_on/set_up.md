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
| RelayState APIキー | **Settings（設定）**＞**API Keys（APIキー**）に進み、`sso.saml.login` 権限を持つAPIキーを作成し、生成されたAPIキーをIdP内の`RelayState` パラメータとして入力する。詳細なステップについては、[RelayStateの設定を](#setting-up-your-relaystate)参照のこと。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

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

## RelayStateの設定

1. Brazeで、**設定**＞**APIと識別子と**進む。
2. **API Keys**タブで、**Create API key**ボタンを選択する。
3. **APIキー名**フィールドに、キーの名前を入力する。
4. **権限の**下にある**SSO**ドロップダウンを拡張し、以下をチェックする。 **sso.saml.login**.<br><br>![sso.saml.login をチェックした「権限」セクション]({% image_buster /assets/img/relaystate_troubleshoot.png %}){: style="max-width:70%;"}<br><br>
5. **APIキーの作成**」を選択する。
6. **API Keys**タブで、作成したAPIキーの横にある識別子をコピーする。
7. RelayState API KeyをIdPのRelayStateに貼り付ける（IdPによっては「Relay State」または「Default Relay State」と表示される場合もある）。

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

## トラブルシューティング

### ユーザーのメールは正しく設定されているか？

エラー`ERROR_CODE_SSO_INVALID_EMAIL` 、ユーザーのメールアドレスが有効でない。SAML トレースで、`saml2:Attribute Name="email"` フィールドが、ユーザがログインに使用しているメール・アドレスと一致することを確認する。Microsoft Entra ID を使用する場合、属性マッピングは`email = user.userprincipalname` となる。

Eメールアドレスは大文字と小文字を区別し、IDプロバイダー（Okta、OneLogin、Azure Active Directoryなど）で設定されたものを含め、Brazeで設定されたものと完全に一致する必要がある。

ユーザーのメール・アドレスに問題があることを示すエラーには、他にも以下のようなものがある：
- `ERROR_CODE_SSO_EMAIL_DOES_NOT_EXIST`:ユーザーのメールアドレスがダッシュボード内にない。
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISSING`:ユーザーのEメールアドレスが空白であるか、その他の誤設定である。
- `ERROR_CODE_SSO_SESSION_SIGN_IN_EMAIL_MISMATCH` または`ERROR_CODE_SSO_SIGN_IN_EMAIL_MISMATCH` ：ユーザーのメールがSSOの設定に使用したものと一致しない。

### 有効な SAML 証明書（x.509 ）を持っているか。

[この SAML 検証ツールを](https://www.samltool.com/validate_response.php)使用して、SAML 証明書を検証できる。期限切れの SAML 証明書は、無効な SAML 証明書でもあることに注意。

### 正しい SAML 証明書（x.509 証明書）をアップロードしたか。

SAMLトレースの`ds:X509Certificate` セクションの証明書が、Brazeにアップロードした証明書と一致していることを確認する。これには、`-----BEGIN CERTIFICATE-----` ヘッダーと`-----END CERTIFICATE-----` フッターは含まれていない。

### SAML 証明書（x.509 ）のタイプや書式を間違えたか。

ダッシュボードで提出した証明書に空白や余分な文字がないことを確認する。

証明書をBrazeに入力する際、証明書はPrivacy Enhanced Mail (PEM)エンコードされ、正しくフォーマットされている必要がある（`-----BEGIN CERTIFICATE-----` ヘッダーと`-----END CERTIFICATE-----` フッターを含む）。 

以下は、正しくフォーマットされた証明書の例である：

```
-----BEGIN CERTIFICATE-----
THIS_IS_A_MOCKED_CERTIFICATE_4ysJLTzETANBgkqhkiG9w0BAQsFADA0MTIwMAYDVQQDEylNaWNyb3NvZnQgQXp1cmUgRmVkZXJhdGVkIFNTTyBDZXJ0aWZpY2F0ZTAeFw0yMjA1MjcwOTA4MzFaFw0yNTAbMjcwOTA4MzFaMDQxMjAwBgNVBAMTKU1pY3Jvca9mdCBBenVyZSBGZWRlcmF0ZWQgU1NPIENlcnAFWAOKGPAWIGKJPOAMWANBgkqhkiG9w0BAQEFAAaCAQ8AMIIBCgKCAQEA1+KFJwxoac6jdFztQd+vQu59qM8rgfX5RICk0ODfpXkuDUNudcI0XmOAkKHRoMNPYlmMEf5NSiZ7TMElEPtK9zZlpAoSchxxC0Ndegc1AMFi7i2BsEIqPwrer0G6kx2vuAjdrDROPPafkmwalkfmklaw23FlYmV7doE0Vrj2WxR1PG0eFAdsxPLsO1ny55fPj2ibwaqc0XpDkfTrO9GnFvmZAS8ebYtLZsYAMAGLKWAMLGKAWMLKMFDW6vBDaK290s9FdaWza3GPHTcDstawRhyqbXpVjiqpQ0mtxANW4WduSiohhpeqv05TlSOhx87QalkfmwalfmAWMFLKQEBCwUAA4IBAQBdZ5E9FqICfL1q+G6D1tChKl1Y6I6IVULQb4LESSJRaxv53nakmflwakmMALKFMWOYKAeUWO2hdED54qGMgUnLL6YheQBrsm6ilBC68F7ZFmIzVKycvw65yamWbTMi2f2lF60GNYMrq8sGQUkgO0O2zTN07J9wGTe9M+MAFLKWAMFLKalkmflkawoij4jpcsLXXFZJoHSXnF3+qQuzu+49D6pR2lF7DDW+5+PRoc1QpDSytdXxWzItsjQ6IFRuvIGsbrMg0FVaze7ePdKrc47wSlElno7SQ0H+6g40q25rsDSLO
-----END CERTIFICATE-----
```

### ユーザーのセッション・トークンは有効か？

影響を受けたユーザーに[ブラウザのキャッシュと Cookie をクリアして](https://its.uiowa.edu/services/how-clear-cache-and-cookies-your-web-browser)もらい、SAML SSO でのログインを再試行する。

### RelayStateを設定したか？

エラー`ERROR_CODE_SSO_INVALID_RELAY_STATE` 、RelayStateが誤って設定されているか、存在しない可能性がある。まだの場合は、IdP管理システムでRelayStateを設定する必要がある。ステップについては、[RelayStateの設定を](#setting-up-your-relaystate)参照のこと。 

### ユーザーはOktaとBrazeの間でサインインループから抜け出せないのか？

ユーザーがOkta SSOとBrazeダッシュボードの間を行き来してサインインできない場合は、OktaにアクセスしてSSO URLの送信先を[Brazeインスタンスに]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)設定する必要がある（たとえば、`https://dashboard-07.braze.com` ）。 

他のIdPを使用している場合は、貴社が正しいSAMLまたはx.509 証明書をBrazeにアップロードしたかどうかを確認する。

### 手動統合を使用しているか？

御社がIdPのアプリストアからBrazeアプリをダウンロードしていない場合は、事前に構築された統合をダウンロードする必要がある。例えば、OktaがあなたのIdPなら、Brazeの[統合](https://www.okta.com/integrations/braze/)ページからアプリをダウンロードする。
