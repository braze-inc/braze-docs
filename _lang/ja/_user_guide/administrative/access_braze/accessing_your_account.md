---
nav_title: アカウントへのアクセス
article_title: アカウントへのアクセス
page_order: 2
page_type: reference
description: "この記事では、Braze アカウントの取得方法、アクセス権が付与された後のログイン方法、Braze パスワードのリセット方法について説明します。"

---

# アカウントへのアクセス

会社の最初の Braze ユーザーが初めてログインする場合、契約初日に `@alerts.braze.com` からメールの確認とログインを求めるウェルカムメールが届きます。

アカウントを確認したら、ダッシュボードの [[会社ユーザー]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/)] ページから他のユーザーを追加できます。追加されたすべてのユーザーに、アカウントの確認を求めるメールが届きます。

会社の Braze アカウントの最初のユーザーでない場合は、会社の Braze アカウント管理者にアカウントの作成を依頼してください。その後、`@alerts.braze.com` からメールの確認とログインを求めるウェルカムメールが届きます。

## ログイン

ログインの必要な場所が用意されたので、すでにわかっているかもしれませんが、ログイン方法を説明します。会社の最初のユーザーの場合は、前のセクションのガイダンスに従ってください。そうでない場合は、会社の Braze 管理者がアカウントを作成した後に自由にログインできます。

[Braze.com](https://www.braze.com) のホームサイトからログインするか、特定の [Braze インスタンス]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)に対応するダッシュボード URL を使用する方法もあります。便利なように、Braze には以下のようないくつかのシングルサインオン (SSO) オプションがあります。

* [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/)
* [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/)
* [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)
* [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)

{% alert note %}
SSOでBrazeにログインした後、パスワードを使ってダッシュボードにログインすることはできなくなる。
{% endalert %}

## パスワードのリセット

パスワードを再設定するには、ダッシュボードの [ログイン] ページの [**パスワードをお忘れですか?**] リンクをクリックします。その後、パスワードをリセットするリンクを受け取るメールアドレスの入力が求められます。

![パスワード再設定ボタン][45]

[45]: {% image_buster /assets/img_archive/enable_reset.png %}
