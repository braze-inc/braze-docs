---
nav_title: Okta
article_title: Okta
page_order: 4
page_type: tutorial
description: "この記事では、シングルサインオンに Okta を使用するように Braze を設定する方法を順に説明します。" 

---

# Okta 

![オークタSSO を有効にした状態でのBraze ダッシュボードログイン。][4]{: style="float:right;max-width:30%;margin-left:15px;margin-bottom:15px;"}

> Okta は、あらゆるデバイス上のあらゆるアプリケーションとあらゆるユーザーを接続します。Okta はクラウド向けに構築されたエンタープライズクラスの ID 管理サービスですが、多くのオンプレミスアプリケーションと互換性があります。Okta を使用すると、IT チームはあらゆる従業員によるあらゆるアプリケーションやデバイスへのアクセスを管理できます。
<br>

## 要件

| 要件 | 詳細 |
| ----------- | ------- |
| アカウントでOktaがオンになっている | Braze アカウントマネージャーに連絡して、アカウントでこれを有効にしましょう。 |
| Okta 管理者権限 | オークタを設定するときは、事前に管理者権限を持っていることを確認してください。 |
| Braze管理者権限 | オークタを設定するときは、事前に管理者権限を持っていることを確認してください。 |
| リレーステートAPI キー | IdP ログインを有効にするには、**Settings** > **API キー s** に移動し、`sso.saml.login` 権限を持つAPI キーを作成します。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、API キーは \[**開発者コンソール**] > \[**API 設定**] の \[**設定**] にあります。
{% endalert %}

## ステップ 1: Braze の設定

### ステップ 1a: Braze の \[セキュリティ設定] に移動

アカウントマネージャーがアカウントのSAML SSO を有効にした後、**Settings**> **Admin Settings**> **Security Settings**に移動し、SAML SSO セクションを**ON**に切り替えます。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、アカウントアイコンを選択し、\[**会社の設定**] > \[**セキュリティ設定**] に移動して、\[SAML SSO] セクションを見つけます。
{% endalert %}

![セキュリティー設定ページで、OKTA SAML SSO が有効になっています。][1]

### ステップ 1b: SAML SSO 設定の編集

Okta Admin ダッシュボードから、ターゲットURL (ログインURL) と`x.509` 証明書が提供されます。これをBraze アカウントの**セキュリティ設定** ページに入力する必要があります。

![][7]{: style="max-width:75%"}

| 要件 | 詳細 |
|---|---|
| `SAML Name` | これにより、ログイン画面のボタンテキストとして耳がアプリされます。これは通常、ID プロバイダーの名前です(例: "Okta")。 |
| `Target URL` | これは、オークタ管理者ダッシュボードが提供するログインURL です。** アプリ lications** > あなたのアプリ lication > ** General** tab > ** アプリ 埋め込みリンク** > ** 埋め込みリンク</スパン> を検索します。 |
| `Certificate` | `x.509` PEM en コード d 証明書は、ID プロバイダーによって提供されます。このフィールドにコピーアンドペーストする必要があります。** SAML Signing 証明書 s** に進み、**Actions** > **Down 読み込む 証明書** を選択して、Okta で取得します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

完了したら、ページ下部の \[**変更内容を保存**] を選択します。

## ステップ 2: Okta の設定

Okta で、Braze SAML アプリの \[**サインオン**] タブを選択し、\[**編集**] をクリックします。 

次に、\[**デフォルトのリレーステート**] フィールドに、`sso.saml.login` 権限を持つ RelayState API キーを入力します。 

![サインオンタブのOkta Default RelayState。][2]{: style="max-width:75%"}

これらの新しい設定を必ず保存してください。

{% alert tip %}
Braze アカウントユーザーを SAML SSO でのみサインイン可能にする場合は、\[**会社の設定**] ページから[シングルサインオン認証を制限]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#restriction)できます。
{% endalert %}

## ステップ 3: ログイン

これで、Okta を使用して Braze にログインできます。

[1]: {% image_buster/assets/img/Okta/okta1.png %}
[2]: {% image_buster /assets/img/Okta/okta2.png %}
[4]: {% image_buster /assets/img/Okta/okta4.png %}
[7]: {% image_buster /assets/img/Okta/okta5.png %}
[5]: {% image_buster /assets/img/sso2.png %}
[6]: {% image_buster /assets/img/samlsso.gif %}