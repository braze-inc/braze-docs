---
nav_title: Okta
article_title: Okta
page_order: 4
page_type: tutorial
description: "この記事では、シングルサインオンに Okta を使用するように Braze を設定する方法を順に説明します。" 

---

# Okta 

![Okta SSO を有効にした Braze ダッシュボードログイン。][4]{: style="float:right;max-width:30%;margin-left:15px;margin-bottom:15px;"}

> Okta は、あらゆるデバイス上のあらゆるアプリケーションとあらゆるユーザーを接続します。Okta はクラウド向けに構築されたエンタープライズクラスの ID 管理サービスですが、多くのオンプレミスアプリケーションと互換性があります。Okta を使用すると、IT チームはあらゆる従業員によるあらゆるアプリケーションやデバイスへのアクセスを管理できます。
<br>

## 要件

| 要件 | 詳細 |
| ----------- | ------- |
| アカウントで Okta がオンになっている | Braze アカウントマネージャーに連絡して、アカウントでこれを有効にしましょう。 |
| Okta 管理者権限 | Okta を設定する前に、管理者権限があることを確認してください。 |
| Braze管理者権限 | Okta を設定する前に、管理者権限があることを確認してください。 |
| RelayState API キー | IdP ログインを有効にするには、[**設定**] > [**API キー**] に移動し、`sso.saml.login` 権限を持つ API キーを作成します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、API キーは [**開発者コンソール**] > [**API 設定**] の [**設定**] にあります。
{% endalert %}

## ステップ 1: Braze の設定

### ステップ 1a: Braze の [セキュリティ設定] に移動

アカウントマネージャーがアカウントの SAML SSO を有効にした後、[**設定**] > [**管理者設定**] > [**セキュリティ設定**] に移動し、SAML SSO セクションを [**オン**] に切り替えます。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、アカウントアイコンを選択し、[**会社の設定**] > [**セキュリティ設定**] に移動して、[SAML SSO] セクションを見つけます。
{% endalert %}

![[セキュリティ設定] ページで、Okta SAML SSO が有効になっています。][1]

### ステップ 1b: SAML SSO 設定の編集

Okta Admin ダッシュボードから、ターゲットURL (ログインURL) と`x.509` 証明書が提供されます。これをBraze アカウントの**セキュリティ設定** ページに入力する必要があります。

![][7]{: style="max-width:75%"}

| 要件 | 詳細 |
|---|---|
| `SAML Name` | これはログイン画面のボタンテキストとして表示されます。これは通常、ID プロバイダーの名前です(例: "Okta")。 |
| `Target URL` | これは、Okta 管理者ダッシュボードで提供されるログイン URL です。これを確認するには、[**アプリケーション**] > 自分のアプリケーション > [**一般**] タブ > [**アプリ埋め込みリンク**] > [**埋め込みリンク**] に移動します。 |
| `Certificate` | PEM エンコードされた `x.509` 証明書は、ID プロバイダーから提供されます。このフィールドにコピーアンドペーストする必要があります。これを Okta で取得するには、[**SAML 署名証明書**] に移動し、> [**アクション**] > [**証明書をダウンロード**] を選択します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

完了したら、ページ下部の [**変更内容を保存**] を選択します。

## ステップ 2: Okta の設定

Okta で、Braze SAML アプリの [**サインオン**] タブを選択し、[**編集**] をクリックします。 

次に、[**デフォルトのリレーステート**] フィールドに、`sso.saml.login` 権限を持つ RelayState API キーを入力します。 

![[サインオン] タブの Okta のデフォルト RelayState。][2]{: style="max-width:75%"}

これらの新しい設定を必ず保存してください。

{% alert tip %}
Braze アカウントユーザーを SAML SSO でのみサインイン可能にする場合は、[**会社の設定**] ページから[シングルサインオン認証を制限]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction)できます。
{% endalert %}

## ステップ 3: ログイン

これで、Okta を使用して Braze にログインできます。

[1]: {% image_buster/assets/img/Okta/okta1.png %}
[2]: {% image_buster /assets/img/Okta/okta2.png %}
[4]: {% image_buster /assets/img/Okta/okta4.png %}
[7]: {% image_buster /assets/img/Okta/okta5.png %}
[5]: {% image_buster /assets/img/sso2.png %}
[6]: {% image_buster /assets/img/samlsso.gif %}