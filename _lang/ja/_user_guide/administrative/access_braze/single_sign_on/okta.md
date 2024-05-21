---
nav_title: Okta
article_title: Okta
page_order: 4
page_type: tutorial
description: "この記事では、シングルサインオンに Okta を使用するように Braze を設定する方法を順に説明します。" 

---

# Okta 

![Okta の SSOを有効にした Braze ダッシュボードへのログイン。][4]{: style="float:right;max-width:30%;margin-left:15px;margin-bottom:15px;"}

> Okta は、あらゆるデバイス上のあらゆるアプリケーションとあらゆるユーザーを接続します。Okta はクラウド向けに構築されたエンタープライズクラスの ID 管理サービスですが、多くのオンプレミスアプリケーションと互換性があります。Okta を使用すると、IT チームはあらゆる従業員によるあらゆるアプリケーションやデバイスへのアクセスを管理できます。
<br>

## 要件

| 要件 | 詳細 |
| ----------- | ------- |
| 自分のアカウントで Okta がオンであること | 自分のアカウントの Okta をオンにするように、Braze アカウントマネージャーに依頼します。 |
| Okta 管理者権限 | Okta を設定するには、管理者権限が必要です。 |
| Braze 管理者権限 | Okta を設定するには、管理者権限が必要です。|
| RelayState API キー | IdP ログインを有効にするには、[**設定**] > [**API キー**] に移動して、`sso.saml.login` 権限を持つ API キーを作成します。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、API キーは [**開発者コンソール**] > [**API 設定**] の [**設定**] にあります。
{% endalert %}

## ステップ 1: Braze の設定

### ステップ 1a: Braze の [セキュリティ設定] に移動

アカウントマネージャーがアカウントの SAML SSO を有効にしたら、[**設定**] > [**管理者設定**] > ［**セキュリティ設定**］ に移動し、［SAML SSO］ セクションを [**オン**] に切り替えます。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、アカウントアイコンを選択し、[**会社の設定**] > [**セキュリティ設定**] に移動して、[SAML SSO] セクションを見つけます。
{% endalert %}

![[セキュリティ設定] ページで Okta SAML SSOが有効。][1]

### ステップ 1b: SAML SSO 設定の編集

Okta の管理者ダッシュボードの [**SAML 署名証明書**] にターゲット URL (ログイン URL) と `x.509`証明書が表示されます。それらを Braze アカウントに入力する必要があります。

![][7]{: style="max-width:75%"}

| 要件 | 詳細 |
|---|---|
| `SAML Name` | これは、ログイン画面にボタンのテキストとして表示されます。これは通常、「Okta」のような ID プロバイダーの名前です。 |
| `Target URL` | Okta の管理者ダッシュボードが提供するログイン URL です。 |
| `Certificate` | `x.509` PEMでエンコードされた証明書は、ID プロバイダーから提供されます。コピーしてこのフィールドに貼り付ける必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

完了したら、ページ下部の [**変更内容を保存**] を選択します。

## ステップ 2: Okta の設定

Okta で、Braze SAML アプリの [**サインオン**] タブを選択し、[**編集**] をクリックします。 

次に、[**デフォルトのリレーステート**] フィールドに、`sso.saml.login` 権限を持つ RelayState API キーを入力します。 

![Okta の [サインオン] タブの [デフォルトのリレーステート]。][2]{: style="max-width:75%"}

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