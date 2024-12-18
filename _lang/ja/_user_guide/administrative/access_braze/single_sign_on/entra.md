---
nav_title: Microsoft Entra SSO
article_title: Microsoft Entra SSO
page_order: 3
page_type: tutorial
description: "この記事では、Braze を使用して Microsoft Entra のシングルサインオン機能を設定する方法を順に説明します。"

---

# Microsoft Entra SSO

> [Microsoft Entra SSO](https://learn.microsoft.com/en-us/entra/identity/saas-apps/braze-tutorial) は、ID およびアクセスを管理する Microsoft のクラウドベースサービスであり、従業員がサインインしてリソースにアクセスするときに役立ちます。Entra SSO を使用すると、ビジネス要件に基づいてアプリとアプリリソースへのアクセスをコントロールできます。

## 要件

設定時に、サインオン URL と Assertion Consumer Service (ACS) の URL を指定するように求められます。  

| 必要条件 | 詳細 |
|---|---|
| サインオンURL | `https://<SUBDOMAIN>.braze.com/sign_in`<br><br> サブドメインの場合は、[Braze インスタンス の URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) にリストされている調整サブドメインを使用します。例えば、インスタンスが `US-01` の場合、URL は `https://dashboard-01.braze.com` です。つまり、サブドメインが `dashboard-01` になります。 |
| アサーションコンシューマーサービス (ACS) の URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback`<br> ID プロバイダーによっては、これを応答 URL、オーディエンス URL、またはオーディエンス URI と呼ぶこともあります。 |
| エンティティ ID | `braze_dashboard`|
| RelayState APIキー | IDプロバイダー・ログインを有効にするには、**「Settings（設定）**」＞「**API Keys（APIキー）**」と進み、`sso.saml.login` 権限を持つAPIキーを作成する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、API キーは [**開発者コンソール**] > [**API 設定**] の [**設定**] にあります。
{% endalert %}

## Microsoft Entra SSO 内でサービスプロバイダー (SP) が開始するログイン

### ステップ1:ギャラリーから Braze を追加

1. Microsoft Entra 管理センターで、[**Identity**] > [**Applications**] > [**Enterprise Applications**] に移動し、[**New application**] を選択します。
2. 検索ボックスで**Braze**を検索し、結果パネルから選択して**Add**を選択します。

### ステップ2:Microsoft Entra SSO の設定

1. Microsoft Entra 管理センターの Braze アプリケーション統合ページに移動し、[**Single sign-on**] を選択します。
2. **シングルサインオンメソッド**ページで、**SAML**をメソッドとして選択します。
3. **Set up Single Sign-On with SAML** ページで、**Basic SAML Configuration** の編集アイコンを選択します。
4. [Braze インスタンス]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances)とパターン `https://<SUBDOMAIN>.braze.com/auth/saml/callback` を組み合わせた**応答 URL** を入力して、IdP 開始モードでアプリケーションを構成します。
5. 必要に応じて、[**リレー状態**] (オプション) フィールドにリレー状態生成 API キーを入力して、RelayState を設定します。
6. アプリケーションをサービスプロバイダー開始モードで設定する場合は、[**追加の URL を設定します**] をクリックし、[Braze インスタンス]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances)とパターン `https://<SUBDOMAIN>.braze.com/sign_in` を組み合わせたサインオン URL を入力します。
7. Braze の要求する特定の形式で SAML アサーションをフォーマットします。ユーザー属性とユーザークレームのフォーマット方法については、それらの属性と値に関する次のタブを参照してください。

{% tabs %}
{% tab ユーザー属性 %}
これらの属性の値は、[**アプリケーション連携**] ページの [**ユーザー属性**] セクションから管理できます。

次の属性のペアを使用します。

- `givenname` = `user.givenname`
- `surname`= `user.surname`
- `emailaddress` = `user.mail`
- `name` = `user.userprincipalname`
- `email` = `user.userprincipalname`
- `first_name` = `user.givenname`
- `last_name` = `user.surname`
- `Unique User Identifier` = `user.userprincipalname`

{% alert important %}
メールのフィールドが、Braze でユーザーに設定されているものと一致することが非常に重要です。ほとんどの場合、これは `user.userprincipalname` と同じになりますが、構成が異なる場合はシステム管理者と協力して、確実にこれらのフィールドを正確に一致させてください。
{% endalert %}

{% endtab %}
{% tab ユーザークレーム %}

**Set up Single Sign-On with SAML」**ページで、「**Edit**」を選択して「**User Attributes」**ダイアログを開く。次に、適切な形式に従ってユーザークレームを編集します。

次のクレーム名のペアを使用します。

- `claims/givenname` = `user.givenname`
- `claims/surname` = `user.surname`
- `claims/emailaddress` = `user.userprincipalname`
- `claims/name` = `user.userprincipalname`
- `claims/nameidentifier` = `user.userprincipalname`

{% alert important %}
メールのフィールドが、Braze でユーザーに設定されているものと一致することが非常に重要です。ほとんどの場合、これは `user.userprincipalname` と同じになりますが、構成が異なる場合はシステム管理者と協力して、確実にこれらのフィールドを正確に一致させてください。
{% endalert %}

これらのユーザー請求と値は、**Manage claim**セクションから管理できる。

{% endtab %}
{% endtabs %}

{: start="8"}
8\.[**SAML によるシングルサインオンのセットアップ**] ページに移動し、[**SAML 署名証明書**] セクションまでスクロールして、要件に基づいて適切な**証明書 (Base64)** をダウンロードします。
9\.[**Braze のセットアップ**] セクションに移動し、[Braze の構成](#step-3)で使用する適切な URL をコピーします。

### ステップ 3:Braze 内で Microsoft Entra SSO を設定する {#step-3}

Microsoft Entra 管理センターで Braze を設定すると、ターゲット URL (ログイン URL) と **x.509** 証明書が提供されます。これらを Braze アカウントに入力します。

アカウントマネージャーがアカウントの SAML SSO を有効にしたら、次の手順を実行します。

1. [**設定**] > [**管理者設定**] > [**セキュリティ設定**] に移動し、[SAML SSO] セクションを [**オン**] に切り替えます。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、アカウントアイコンを選択し、[**会社の設定**] > [**セキュリティ設定**] に移動して、[SAML SSO] セクションを見つけます。
{% endalert %}

{: start="2"}
2\.そのページで、次の項目を追加します。

| 必要条件 | 詳細 |
|---|---|
| `SAML Name` | これはログイン画面のボタンテキストとして表示されます。これは通常、「Microsoft Entra」のような ID プロバイダーの名前です。 |
| `Target URL` | これは、Microsoft Entra が提供するログインURL です。|
| `Certificate` | PEM エンコードされた `x.509` 証明書は、ID プロバイダーから提供されます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Braze アカウントユーザーを SAML SSO でのみサインイン可能にする場合は、[**会社の設定**] ページから[シングルサインオン認証を制限]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction)できます。
{% endalert %}
