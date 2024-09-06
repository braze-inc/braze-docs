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

| 必要条件 | 詳細 |
|---|---|
| ブレイズ・ドメイン | OneLoginでBrazeをセットアップするには、Brazeドメインが必要である。インスタンスが `US-01` の場合、OneLogin ダッシュボードにダッシュボード URL を入力する必要があります。<br><br> 例えば、ダッシュボードのURLが`https://dashboard-01.braze.com` の場合、`dashboard-01.braze.com` と入力する必要がある。  |
| RelayState APIキー | IdPログインを有効にするには、**\[Settings**] > \[**API Keys**]に進み、`sso.saml.login` 権限を持つAPIキーを作成する。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、API キーは \[**開発者コンソール**] > \[**API 設定**] の \[**設定**] にあります。
{% endalert %}

## OneLogin 内での IdP 開始ログイン

### ステップ 1: Braze アプリを設定

1. [OneLogin](https://app.onelogin.com/login) にログインします。![OneLogin**管理**ページ]({% image_buster /assets/img/onelogin_1.jpg %})<br><br>
2. 上部のナビゲーションバーの \[**アプリ**] > \[**アプリの追加**] に移動します。![OneLoginでのBrazeの検索結果。]({% image_buster /assets/img/onelogin_2.jpg %})<br><br>
3. ![]({% image_buster /assets/img/onelogin_3.jpg %})<br><br>
4. 保存されたら、**Configurationに**移動し、**Braze Domainと** **RelayState**APIキーを追加する。![BrazeアプリのOneLogin Configurationタブ。]({% image_buster /assets/img/onelogin_4.png %})<br><br>
5. Braze には、[特定の形式][1]の SAML アサーションが必要です。Braze によりサポートされる \[**パラメーター**] の 属性は事前入力されます。![OneLogin の Braze SAML パラメータ。]({% image_buster /assets/img/onelogin_5.jpg %})<br><br>
6. Brazeダッシュボードのセットアップに必要な**証明書と** **SAML 2.0エンドポイント（HTTP**）を**SSO**タブからコピーする。![OneLoginのBrazeアプリSSOタブからコピーする証明書。]({% image_buster /assets/img/onelogin_6.jpg %})

### ステップ2:Braze での OneLogin の構成

OneLogin で Braze を設定すると、ターゲット URL (`SAML 2.0 Endpoint (HTTP)`) と `x.509` 証明書が提供されます。これらを Braze アカウントに入力します。

アカウントマネージャーがアカウントの SAML SSO を有効にしたら、\[**設定**] > \[**管理者設定**] > ［**セキュリティ設定**］ に移動し、［SAML SSO］ セクションを \[**オン**] に切り替えます。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、アカウントアイコンを選択し、\[**会社の設定**] > \[**セキュリティ設定**] に移動して、\[SAML SSO] セクションを見つけます。
{% endalert %}

このページでは、次の項目を入力します。

| 必要条件 | 詳細 |
|---|---|
| `SAML Name` | これはログイン画面のボタンテキストとして表示される。これは通常、「OneLogin」のようなIDプロバイダの名前である。 |
| `Target URL` | これはOneLoginが提供する`SAML 2.0 Endpoint (HTTP)` URLである。|
| `Certificate` | `x.509` PEMエンコードされた証明書は、OneLoginから提供される。 |
{: .reset-td-br-1 .reset-td-br-2}

![Brazeのセキュリティ設定を開き、SAML SSOの詳細を追加する。]({% image_buster /assets/img/samlsso.gif %})

{% alert tip %}
Braze アカウントユーザーを SAML SSO でのみサインイン可能にする場合は、\[**会社の設定**] ページから[シングルサインオン認証を制限]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction)できます。
{% endalert %}

[1]: {{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#configure-your-identity-provider
