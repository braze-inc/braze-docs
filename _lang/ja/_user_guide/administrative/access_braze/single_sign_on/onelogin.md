---
nav_title: OneLogin
article_title: OneLogin
page_order: 5
page_type: tutorial
description: "この記事では、シングルサインオンに OneLogin を使用するように Braze を設定する方法を順に説明します。"

---

# OneLogin

> [OneLogin](https://www.onelogin.com/) は、ユーザー ID 管理用の包括的なソリューションを提供するクラウド ID プラットフォームです。OneLogin は SAML 2.0 を使用してクラウドおよびオンプレミスアプリケーションと連携し、シングルサインオン （SSO）、ユーザープロビジョニング、多要素認証などを実現します。

## 要件

設定時に、サインオン URL と Assertion Consumer Service (ACS) の URL を指定するように求められます。  

| 要件 | 詳細 |
|---|---|
| Braze ドメイン | OneLogin 内で Braze を設定するには、Braze ドメインが必要です。インスタンスが `US-01` の場合、OneLogin ダッシュボードにダッシュボード URL を入力する必要があります。<br><br> 例えば、ダッシュボードの URL が `https://dashboard-01.braze.com` の場合、「`dashboard-01.braze.com`」を入力する必要があります。|
| RelayState API キー | IdP ログインを有効にするには、[**設定**] > [**API キー**] に移動して、`sso.saml.login` 権限を持つ API キーを作成します。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、API キーは [**開発者コンソール**] > [**API 設定**] の [**設定**] にあります。
{% endalert %}

## OneLogin 内での IdP 開始ログイン

### ステップ 1: Braze アプリを設定

1. [OneLogin](https://app.onelogin.com/login) にログインします。[**管理**] をクリックします。![OneLogin Administration page.]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>
2. 上部のナビゲーションバーの [**アプリ**] > [**アプリの追加**] に移動します。「Braze」を検索し、Braze アプリを選択します。![Search results for Braze in OneLogin.]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>
3. Braze アプリを会社に保存します。![\]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>
4. 保存されたら [**設定**] に移動し、**Braze ドメイン**と **RelayState** API キーを追加します。![OneLogin Configuration tab for the Braze app.]({% image_buster /assets/img/onelogin_4.png %})<br><br>
5. Braze には、[特定の形式][1]の SAML アサーションが必要です。Braze によりサポートされる [**パラメーター**] の 属性は事前入力されます。それらの属性が正しいことを確認します。![Braze SAML parameters in OneLogin.]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>
6. [**SSO**] タブから、Braze ダッシュボードの設定に必要な**証明書**と **SAML 2.0 エンドポイント (HTTP)** をコピーします。![Certificates to copy from the Braze app SSO tab in OneLogin.]({% image_buster /assets/img/onelogin_6.jpg %})

### ステップ 2: Braze での OneLogin の構成

OneLogin で Braze を設定すると、ターゲット URL (`SAML 2.0 Endpoint (HTTP)`) と `x.509` 証明書が提供されます。これらを Braze アカウントに入力します。

アカウントマネージャーがアカウントの SAML SSO を有効にしたら、[**設定**] > [**管理者設定**] > ［**セキュリティ設定**］ に移動し、［SAML SSO］ セクションを [**オン**] に切り替えます。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、アカウントアイコンを選択し、[**会社の設定**] > [**セキュリティ設定**] に移動して、[SAML SSO] セクションを見つけます。
{% endalert %}

このページでは、次の項目を入力します。

| 要件 | 詳細 |
|---|---|
| `SAML Name` | これは、ログイン画面にボタンのテキストとして表示されます。これは通常、「OneLogin」のような ID プロバイダーの名前です。 |
| `Target URL` | OneLogin が提供する `SAML 2.0 Endpoint (HTTP)` の URLです。|
| `Certificate` | `x.509` PEM エンコード証明書は OneLogin から提供されます。 |
{: .reset-td-br-1 .reset-td-br-2}

![Opening Security Settings in Braze and adding SAML SSO details.]({% image_buster /assets/img/samlsso.gif %})

{% alert tip %}
Braze アカウントユーザーを SAML SSO でのみサインイン可能にする場合は、[**会社の設定**] ページから[シングルサインオン認証を制限]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction)できます。
{% endalert %}

[1]: {{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#configure-your-identity-provider
