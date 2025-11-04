---
nav_title: SAML ジャストインタイム・プロビジョニング
article_title: SAMLジャストインタイムプロビジョニング
page_order: 1
page_type: tutorial
description: "この記事では、新しいダッシュボードユーザーが最初のサインインで Braze アカウントを作成できるように SAML ジャストインタイムプロビジョニングを設定する方法について順に説明します。" 

---

# SAMLジャストインタイムプロビジョニング 

> ジャストインタイムプロビジョニングは、[ SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/) で動作し、新しいダッシュボード ユーザーs が最初のサインイン時にBraze アカウントを作成できるようにします。これにより、管理者が新しいダッシュボード ユーザーのアカウントを手動で作成し、権限を選択してワークスペースに割り当て、アカウントの有効化を待機する必要がなくなります。

セキュリティ対策として、SAMLジャストインタイム・プロビジョニング（JITP）は、社内にすでに存在するメール・ドメインのユーザーに対してのみ機能する。JITPは、偽装またはなりすましでない開発者が社内に少なくとも1人いることが確認されているドメインに対してのみ可能である。 

例えば、アカウント```jon.smith@decorumsoft.com``` 、JITPを使ってDecorumsoftにログインできるとしよう。アカウント```jane.smith@decorumsoft.com``` 、同じドメインを持ち、プロビジョニングを許可することもできる。しかし、```jon.smith@decorumsoft.eu``` でJITPを使用しようとすると、Decorumsoftダッシュボード内に```decorumsoft.eu``` のアカウントがないため、プロビジョニングが許可されない。 

企業のために例外を設けるには、[サポートに]({{site.baseurl}}/braze_support/)連絡すること。

## 前提条件

SAML JITP は、SAML SSO が設定され、統合されていることを必要とする。Google SSOとは互換性がなく、Identity Provider Initiated（IdP主導）のログイン・ワークフローにのみ対応している。

## SAML ジャストインタイム・プロビジョニング（JITP）を設定する。

Braze管理者に次の操作を依頼します。

1. **設定**>**管理者設定**>**セキュリティ設定に**移動する。
2. ** SAML SSO** セクションで、** 自動ユーザープロビジョニング** オプションを切り替えます。
3. デフォルト ワークスペースを選択して、新しいダッシュボード ユーザーを追加します。
4. 新しいダッシュボード ユーザーに割り当てるデフォルト権限セットを選択します。権限セットの作成方法については、[ユーザー権限の設定]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/)を参照してください。
6. ページ下部の**変更の保存**を選択します
7. SSO プロバイダーの設定で、Braze のアクセスが必要なすべてのユーザーを SSO プロバイダーのディレクトリに追加します。
8. これで、ユーザーはサインアップまたはログインができます。

## よくある質問

### SAML JITP を無効にする方法は？

JITP設定後、[サポートに連絡して]({{site.baseurl}}/braze_support/)JITPをオフにする必要がある。

## トラブルシューティング

### Microsoft Entra IDでシングルサインボタンが表示されない

Microsoft Entraの**Basic SAML Configuration**フォームの**Basic SAML ConfigurationフォームのBasic SAML ConfigurationフォームのBasic SAML Configuration**フォームの**Sign-On URL**フィールドにより、IdP主導のログインでユーザーにSSOボタンではなくパスワードオプションしか表示されないことがある。この問題を防ぐには、Microsoft Entra管理センターでBrazeを設定する際、**サインオンURL**フィールドを空白のままにしておく。