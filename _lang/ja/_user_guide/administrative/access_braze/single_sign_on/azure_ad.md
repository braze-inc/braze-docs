---
nav_title: Azure Active Directory
article_title: Azure Active Directory
page_order: 3
page_type: tutorial
description: "この記事では、Braze を使用して Azure AD のサインオン機能を設定する方法を順に説明します。"

---

# Azure Active Directory

> [Azure Active Directory (Azure AD)](https://docs.microsoft.com/en-us/azure/active-directory/saas-apps/braze-tutorial) は、ID およびアクセスを管理する Microsoft のクラウドベースサービスであり、従業員がサインインしてリソースにアクセスするときに役立ちます。Azure AD を使用すると、ビジネス要件に基づいてアプリとアプリリソースへのアクセスをコントロールできます。

## 要件

設定時に、サインオン URL と Assertion Consumer Service (ACS) の URL を指定するように求められます。  

| 必要条件 | 詳細 |
|---|---|
| サインオンURL | `https://<SUBDOMAIN>.braze.com/sign_in`<br><br> サブドメインの場合は、[Braze インスタンス の URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) にリストされている調整サブドメインを使用します。例えば、インスタンスが `US-01` の場合、URL は `https://dashboard-01.braze.com` です。これは、サブドメインが`dashboard-01` になることを意味する。 |
| アサーション・コンシューマー・サービス（ACS）URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback`<br> 一部の ID プロバイダでは、これは返信 URL、Audience URL、または Audience URI とも呼ばれる。 |
| エンティティID | `braze_dashboard`|
| RelayState APIキー | IDプロバイダー・ログインを有効にするには、**「Settings（設定）**」＞「**API Keys（APIキー）**」と進み、`sso.saml.login` 権限を持つAPIキーを作成する。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、API キーは \[**開発者コンソール**] > \[**API 設定**] の \[**設定**] にあります。
{% endalert %}

## Azure AD 内でサービスプロバイダー (SP) が開始するログイン

### ステップ 1: ギャラリーから Braze を追加

1. Azure Portal に移動し、左側のナビゲーションパネルで \[**Azure Active Directory**] ​​をクリックします。
2. \[**エンタープライズ アプリケーション**] に移動し、\[**すべてのアプリケーション**] を選択します。
3. ダイアログの上部にある \[**\+ 新しいアプリケーション**] をクリックして、新しいアプリケーションを追加します。
4. 検索ボックスで「**Braze**」を検索し、結果パネルからそれを選択して \[**追加**] をクリックします。

### ステップ 2: Azure AD のシングルサインオンを構成

1. Azure Portal の \[**Braze アプリケーション統合**] ページに移動し、\[**シングルサインオン**] を選択します。
2. **Select a single sign-on method**ダイアログで、**SAML/WS-Fedを**選択する。
3. **Set up Single Sign-On with SAML」**ページで、「**Basic SAML Configuration**」の編集アイコンを選択する。
4. [Brazeインスタンスと]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances)次のパターンを組み合わせた**Reply URLを**入力して、IdP起動モードでアプリケーションを構成する：`https://<SUBDOMAIN>.braze.com/auth/saml/callback`.
5. オプションでRelayStateを設定するには、Relay State**（オプション）**フィールドにRelay Stateが生成したAPIキーを入力する。
6. SP起動モードでアプリケーションを構成したい場合は、**Set additional URLsを**選択し、[Brazeインスタンスと]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances)次のパターンを組み合わせたサインオンURLを入力する：`https://<SUBDOMAIN>.braze.com/sign_in`.
7. Braze の要求する特定の形式で SAML アサーションをフォーマットします。ユーザー属性とユーザークレームのフォーマット方法については、それらの属性と値に関する次のタブを参照してください。

{% tabs %}
{% tab ユーザー属性 %}
これらの属性の値は、\[**アプリケーション連携**] ページの \[**ユーザー属性**] セクションから管理できます。

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
{% tab ユーザーの主張 %}

**Set up Single Sign-On with SAML」**ページで、「**Edit**」を選択して「**User Attributes」**ダイアログを開く。その後、適切なフォーマットに従ってユーザークレームを編集する。

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
8\.\[**SAML によるシングルサインオンのセットアップ**] ページに移動し、\[**SAML 署名証明書**] セクションまでスクロールして、要件に基づいて適切な**証明書 (Base64)** をダウンロードします。
9\.\[**Braze のセットアップ**] セクションに移動し、[Braze の構成](#step-3)で使用する適切な URL をコピーします。

### ステップ 3: Braze での Azure AD の設定{#step-3}

Azure AD内でBrazeをセットアップすると、ターゲットURL（ログインURL）と証明書が提供される。 **x.509**証明書が提供されるので、それをBrazeアカウントに入力する。

アカウントマネージャーがアカウントの SAML SSO を有効にしたら、次の手順を実行します。

1. \[**設定**] > \[**管理者設定**] > \[**セキュリティ設定**] に移動し、\[SAML SSO] セクションを \[**オン**] に切り替えます。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、アカウントアイコンを選択し、\[**会社の設定**] > \[**セキュリティ設定**] に移動して、\[SAML SSO] セクションを見つけます。
{% endalert %}

{: start="2"}
2. そのページで、次の項目を追加します。

| 必要条件 | 詳細 |
|---|---|
| `SAML Name` | これはログイン画面のボタンテキストとして表示される。これは通常、「Azure AD」のようなIDプロバイダーの名前である。 |
| `Target URL` | これはAzure ADが提供するログインURLである。|
| `Certificate` | `x.509` PEM エンコードされた証明書は、ID プロバイダから提供される。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
Braze アカウントユーザーを SAML SSO でのみサインイン可能にする場合は、\[**会社の設定**] ページから[シングルサインオン認証を制限]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction)できます。
{% endalert %}
