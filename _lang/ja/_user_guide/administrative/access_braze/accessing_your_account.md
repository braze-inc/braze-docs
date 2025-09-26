---
nav_title: アカウントへのアクセス
article_title: アカウントへのアクセス
page_order: 2
page_type: reference
description: "この記事では、Braze アカウントの取得方法、アクセス権が付与された後のログイン方法、Braze パスワードのリセット方法について説明します。"

---

# アカウントへのアクセス

> この記事では、Brazeアカウントの取得方法、アクセス許可後のログイン方法、ダッシュボードへのアクセスとダッシュボードのパフォーマンスのトラブルシューティング方法について説明する。

会社の最初の Braze ユーザーが初めてログインする場合、契約初日に `@alerts.braze.com` からメールの確認とログインを求めるウェルカムメールが届きます。

アカウントを確認したら、ダッシュボードの [[会社ユーザー]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/)] ページから他のユーザーを追加できます。追加されたすべてのユーザーに、アカウントの確認を求めるメールが届きます。

御社のBrazeアカウントの最初のユーザーでない場合は、御社のBrazeアカウント管理者に連絡し、アカウントの作成を依頼する。その後、`@alerts.braze.com` からメールの確認とログインを求めるウェルカムメールが届きます。

## ログイン

初回であれ、100万回目であれ、ログインする方法について話そう！会社の最初のユーザーの場合は、前のセクションのガイダンスに従ってください。そうでない場合は、会社の Braze 管理者がアカウントを作成した後にログインできます。

[Braze.com](https://www.braze.com) のホームサイトからログインするか、特定の [Braze インスタンス]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/)に対応するダッシュボード URL を使用する方法もあります。便利なように、Braze には以下のようないくつかのシングルサインオン (SSO) オプションがあります。

* [SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/)
    * [SAMLジャストインタイムプロビジョニング]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit/)
* [Microsoft Entra SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/)
* [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)
* [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)

{% alert note %}
SSOでBrazeにログインした後、パスワードを使ってダッシュボードにログインすることはできなくなる。
{% endalert %}

## サポートされているブラウザー

Braze ダッシュボードは次のブラウザーをサポートしています。
- Chrome（バージョン87以降）
- Firefox（バージョン85以降）
- Safari (バージョン 15.4 以降)
- Edge (バージョン 87 以降)

ダッシュボードに予期せぬエラーが発生したと表示され、ブラウザのコンソールツールにエラー`ReferenceError: structuredClone is not defined` が表示されている場合、ブラウザが古い。このエラーが繰り返される場合は、ブラウザをアンインストールして再インストールする。

## トラブルシューティング

### パスワードのリセット

パスワードをリセットするには、ダッシュボード・ログイン・ページで「**パスワードをお忘れですか？**パスワードをリセットするリンクを受け取るメールアドレスの入力が求められます。

![[パスワードをお忘れですか?] プロンプトが表示されているダッシュボード ログイン。]({% image_buster /assets/img_archive/enable_reset.png %}){: style="max-width:60%"}

### ブラウザのキャッシュと Cookie のクリア

ダッシュボードやセグメントのパフォーマンスリストが読み込まれないなど、ダッシュボードのパフォーマンスに問題がある場合は、各ブラウザのステップに従って、ブラウザのキャッシュとCookieをクリアしてみてください。

{% alert important %}
Cookieをクリアするとログアウトするので、未保存の作業は失われる。
{% endalert %}

- [ChromeのキャッシュとCookieを消去する](https://support.google.com/accounts/answer/32050?hl=en&co=GENIE.Platform%3DDesktop)
- [MacのSafariでCookieを消去する](https://support.apple.com/en-gb/guide/safari/sfri11471/16.1/mac/13.0)
- [FirefoxでCookieとサイトデータを消去する](https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox)
- [Microsoft EdgeですべてのCookieを削除する](https://support.microsoft.com/en-us/windows/manage-cookies-in-microsoft-edge-view-allow-block-delete-and-use-168dab11-0753-043d-7c16-ede5947fc64d#bkmk_deleteallcookies)

ブラウザのキャッシュとCookieをクリアしても問題が解決しない場合は、[サポートに]({{site.baseurl}}/support_contact/)連絡してください。

### ドラッグ＆ドロップエディターへのアクセス

ほとんどの Braze ユーザーの場合、ドラッグ＆ドロップエディターが読み込まれます。しかし、VPN を使用していたり、ファイアウォールで保護されている場合は、ドメインを許可リストに追加する必要があることがあります。IT管理者に連絡し、`*.bz-rndr.com` が許可リストに登録されていることを確認する。

エディターでは、以下のエラーが原因で読み込みの問題が発生することがあります。

- **一時的なエラー:**接続、通信、データ転送に影響する可能性がある一時的な障害です。このような障害は多くの場合、短期間の状況が原因で引き起こされ、体系的な問題を示すものではないため、大規模な介入を必要とせず、自然に解決することが一般的です。
- **大規模なエラー:**これはインフラや製品の問題に関係している可能性があります。 このような状況に気付いて積極的に解決に取り組む際に、[Braze のシステムステータスのページ](https://braze.statuspage.io/)を確認できます。

{% alert important %}
それでも問題が解決しない場合は、[サポートチケットを開封する]({{site.baseurl}}/user_guide/administrative/access_braze/support/)。その前に、`*.bz-rndr.com` がユーザー側で許可リストに追加されていることを IT 管理者が確認していることを確認してください。
{% endalert %}

