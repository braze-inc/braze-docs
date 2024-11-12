---
nav_title: アカウントからロックアウトされる
article_title: アカウントからロックアウトされる
page_order: 0

page_type: solution
description: "このヘルプ記事では、Braze アカウントからロックアウトされている場合のトラブルシューティングステップについて説明します。"
tool: Dashboard
---

# アカウントからロックアウトされる

Braze アカウントからロックアウトされても、心配はいりません。再び入れるようサポートします。	

受信したエラー情報によって、どのようなロックアウトが発生しているかを確認できます。	

- [パスワードに関するエラーが表示される。](#password-error)	
- [エラーは表示されないが、Braze に入れない。](#instance-error)	
- [アカウント停止のエラーが表示される。](#account-suspension)	

## パスワードエラー

あなたのアカウントセキュリティーは私たちにとって大切なので、パスワードはあなたのBrazeアカウントにログインするために必要です。	
- 正しい[Braze ダッシュボードインスタンス][1]にログインしていることを確認します。アカウント管理者またはBraze アカウントマネージャーに確認してください。	
- パスワードの有効期限が切れている可能性があるため、[リセットする必要があります][2]。	
- [single sign-on][3]サービスを使用する場合は、セットアップが適切に完了したことをアカウント管理者に確認してください。	
- Braze のインスタンスが複数ある場合は、間違ったメールを使用してログインしている可能性があります。  	

疑わしい場合は、常に[パスワードをリセットできます][2]。	

## インスタンスエラー

通常、ログインに使用するマシンと同じマシンを使用している場合、Braze は自動的に正しいインスタンスを検出します。ただし、ログインしていない場合や初めてログインする場合は、次のことを考慮することをお勧めします。	

- 正しい[Braze ダッシュボードインスタンス][1]にログインしていることを確認します。アカウント管理者またはBraze アカウントマネージャーに確認してください。
- Braze のインスタンスが複数ある場合は、間違ったメールを使用してログインしている可能性があります。	

## アカウント停止	

この状況はあまり頻繁には発生しませんが、アカウントの停止と削除は非常に深刻な問題です。このエラーを見つけた場合、最善の策は、自社のBraze管理者、Braze アカウントマネージャー、または[Brazeサポート][support]に連絡することです。

_最終更新日2019年10月19日_

[support]: {{site.baseurl}}/support_contact/	
[1]: {{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/#braze-instances
[2]: {{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password
[3]: {{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/
