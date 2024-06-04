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

| 要件 | 詳細 |
|---|---|
|サインオン URL | `https://<SUBDOMAIN>.braze.com/sign_in`<br><br> サブドメインの場合は、[Braze インスタンス の URL]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) にリストされている調整サブドメインを使用します。例えば、インスタンスが `US-01` の場合、URL は `https://dashboard-01.braze.com` です。つまり、サブドメインが `dashboard-01` になります。 |
| Assertion Consumer Service (ACS) の URL | `https://<SUBDOMAIN>.braze.com/auth/saml/callback`<br> ID プロバイダーによっては、これを応答 URL、オーディエンス URL、またはオーディエンス URI と呼ぶこともあります。 |
| エンティティ ID | `braze_dashboard`|
| RelayState API キー | ID プロバイダーのログインを有効にするには、[**設定**] > [**API キー**] に移動し、`sso.saml.login` 権限を使用して API キーを作成します。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、API キーは [**開発者コンソール**] > [**API 設定**] の [**設定**] にあります。
{% endalert %}

## Azure AD 内でサービスプロバイダー (SP) が開始するログイン

### ステップ 1: ギャラリーから Braze を追加

1. Azure Portal に移動し、左側のナビゲーションパネルで [**Azure Active Directory**] ​​をクリックします。
2. [**エンタープライズ アプリケーション**] に移動し、[**すべてのアプリケーション**] を選択します。<br><br>![Azure portal selecting all enterprise applications.]({% image_buster /assets/img/azure_2.png %})

{: start="3"}
3. ダイアログの上部にある [**\+ 新しいアプリケーション**] をクリックして、新しいアプリケーションを追加します。
4. 検索ボックスで「**Braze**」を検索し、結果パネルからそれを選択して [**追加**] をクリックします。

### ステップ 2: Azure AD のシングルサインオンを構成

1. Azure Portal の [**Braze アプリケーション統合**] ページに移動し、[**シングルサインオン**] を選択します。
2. [**シングルサインオン方法の選択**] ダイアログから方法として[ **SAML/WS-Fed**] を選択し 、[**SAML によるシングルサインオンのセットアップ**] ページを開きます。<br><br>![Azure portal select a single sign-on method dialog.]({% image_buster /assets/img/azure_6.png %})

{: start="3"}
3. 編集アイコンをクリックして、[**基本的な SAML 構成**] ダイアログを開きます。<br><br>![Azure portal editing basic SAML configuration.]({% image_buster /assets/img/azure_7.png %})

{: start="4"}
4. [Braze インスタンス]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances)と次のパターンを組み合わせた URL を入力して、IdP 開始モードでアプリケーションを構成します。`https://<SUBDOMAIN>.braze.com/auth/saml/callback`。<br><br>![Azure portal editing basic SAML configuration.]({% image_buster /assets/img/azure_8.png %})

{: start="5"}
5. RelayState で生成された API キーを [RelayState] ボックスに入力して、RelayState を構成します。<br><br>![\]({% image_buster /assets/img/relaystate2.png %})

{: start="6"}
6. アプリケーションを SP 開始モードで構成する場合は、[**追加の URL を設定します**] をクリックし、[Braze インスタンス]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances)と次のパターンを組み合わせた URL を入力します: `https://<SUBDOMAIN>.braze.com/sign_in`。<br><br>![Azure portal setting additional sign on URLs.]({% image_buster /assets/img/azure_9.png %})

{: start="7"}
7\.Braze の要求する特定の形式で SAML アサーションをフォーマットします。ユーザー属性とユーザークレームのフォーマット方法については、それらの属性と値に関する次のタブを参照してください。

{% tabs %}
{% tab User Attributes %}
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
{% tab User Claims %}

[**SAML を使用したシングルサインオンのセットアップ**] ページで、[**編集**] をクリックして [**ユーザー属性**] ダイアログを開きます。次に、適切な形式に従ってクレームを編集します。

![User Attributes dialog in Azure.]({% image_buster /assets/img/azure_11.png %})

次のクレーム名のペアを使用します。

- `claims/givenname` = `user.givenname`
- `claims/surname` = `user.surname`
- `claims/emailaddress` = `user.userprincipalname`
- `claims/name` = `user.userprincipalname`
- `claims/nameidentifier` = `user.userprincipalname`

{% alert important %}
メールのフィールドが、Braze でユーザーに設定されているものと一致することが非常に重要です。ほとんどの場合、これは `user.userprincipalname` と同じになりますが、構成が異なる場合はシステム管理者と協力して、確実にこれらのフィールドを正確に一致させてください。
{% endalert %}

これらのユーザークレームと値は、[**ユーザークレームの管理**] ダイアログから管理できます。

![Manage claim dialog in Azure]({% image_buster /assets/img/azure_12.png %})

{% endtab %}
{% endtabs %}

{: start="8"}
8\.[**SAML によるシングルサインオンのセットアップ**] ページに移動し、[**SAML 署名証明書**] セクションまでスクロールして、要件に基づいて適切な**証明書 (Base64)** をダウンロードします。<br><br>![Azure download SAML signing certificate.]({% image_buster /assets/img/azure_13.png %})

{: start="9"}
9\.[**Braze のセットアップ**] セクションに移動し、[Braze の構成](#step-3)で使用する適切な URL をコピーします。<br><br>![Azure URLs for configuration.]({% image_buster /assets/img/azure_14.png %})

### ステップ 3: Braze での Azure AD の設定{#step-3}

Azure AD で Braze を設定すると、ターゲット URL (ログイン URL) と **x.509** 証明書が提供されます。これらを Braze アカウントに入力します。

アカウントマネージャーがアカウントの SAML SSO を有効にしたら、次の手順を実行します。

1. [**設定**] > [**管理者設定**] > [**セキュリティ設定**] に移動し、[SAML SSO] セクションを [**オン**] に切り替えます。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、アカウントアイコンを選択し、[**会社の設定**] > [**セキュリティ設定**] に移動して、[SAML SSO] セクションを見つけます。
{% endalert %}

{: start="2"}
2. そのページで、次の項目を追加します。

| 要件 | 詳細 |
|---|---|
| `SAML Name` | これは、ログイン画面にボタンのテキストとして表示されます。これは通常、「Azure AD」のような ID プロバイダーの名前です。 |
| `Target URL` | Azure AD が提供するログイン URL です。|
| `Certificate` | `x.509` PEM エンコードされた証明書は、ID プロバイダーから提供されます。 |
{: .reset-td-br-1 .reset-td-br-2}

![Opening Security Settings and adding SAML SSO details.]({% image_buster /assets/img/samlsso.gif %})

{% alert tip %}
Braze アカウントユーザーを SAML SSO でのみサインイン可能にする場合は、[**会社の設定**] ページから[シングルサインオン認証を制限]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction)できます。
{% endalert %}
