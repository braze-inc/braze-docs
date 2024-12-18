---
nav_title: ユーザー
article_title: Braze ユーザーの管理
page_order: 0
page_type: reference
description: "このリファレンス記事では、ユーザーの追加、一時停止、削除など、会社アカウントのユーザーを管理する方法について説明します。"

---

# Braze ユーザーの管理

> ユーザーの追加、一時停止、削除など、会社アカウントのユーザーを管理する方法について学びましょう。

{% alert note %}
このページのいくつかのセクションでは、「**会社ユーザー**」ページを参照しています。[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、[**会社ユーザー**] は [**ユーザーを管理**] と呼ばれ、アカウントアイコンの下にあります。
{% endalert %}

## Braze ユーザーの追加

Brazeアカウントにユーザーを追加するには、管理者権限が必要。 

新しいユーザーを追加する：

1. [**設定**] > [**会社ユーザー**] に移動します。
2. [**\+ 新規ユーザーを追加**] をクリックします。
3. 指示に従って、メールアドレス、部署、[ユーザーロール]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#creating-a-role)などの情報を入力します。

{% alert tip %}
ユーザーのプロフィールに記載されている部署によって、Brazeから受け取る通信の種類が決まる。これにより、誰もがBrazeの使い方に関連したコミュニケーションやアラートだけを受け取ることができる。
{% endalert %}

![][2]

{:start="4"}

4. 管理者でないユーザーについては、このユーザーに付与する会社レベルとワークスペースレベルの[権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#editing-a-users-permissions)を選択します。

![][3]

### 電子メールアドレスの要件

[インスタンスで]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints)使用されるすべての電子メールアドレスは一意でなければならない。つまり、そのインスタンスで会社のワークスペースにアクセスしていた、または現在もアクセスしているユーザーに関連付けられているメールアドレスを追加しようとすると、エラーメッセージが表示される。 

チームがGmailを使用していて、メールアドレスの追加に問題がある場合は、メールアドレスに「+1」や「+test」のようなプラス記号（+）を追加することで、エイリアスを作成することができる。例えば、`contractor@braze.com` は、`contractor+1@braze.com` というエイリアスを持つことができます。`contractor+1@braze.com` 宛のメールは`contractor@braze.com` に配信されるが、エイリアスは一意のメールアドレスとして認識される。

### Brazeアカウントのメールアドレスを変更できますか?

セキュリティ上の理由から、ユーザはBraze アカウントに関連付けられたメールアドレスを変更できません。ユーザがメールアドレスを更新する場合、管理者は[ 希望のメールアドレスで新しいアカウント](#adding-braze-users) を作成する必要があります。

## Braze ユーザーの一時停止

ユーザーを一時停止すると、そのアカウントが非アクティブ状態になり、ユーザーはログインできなくなりますが、そのアカウントに関連付けられたデータは保持されます。管理者のみが Braze ユーザーの一時停止または停止解除ができます。

ユーザーをサスペンドするには、**Settings**> **Company Users**に移動し、ユーザー名を見つけて<i class="fa-solid fa-user-lock"></i>**Suspend**を選択します。

![ユーザーを一時停止する][4]

管理者は、リストからユーザー名を選択し、フッターの [**ユーザーを一時停止**] をクリックしてユーザーを一時停止することもできます。

![ユーザー詳細の編集時にユーザーを一時停止する。][5]

## Braze ユーザーの削除

ユーザーを削除するには、**「Settings（設定）**」＞「**Company Users（会社ユーザー）**」と進み、ユーザー名を見つけ、「<i class="fa fa-trash-can"></i> **Delete user（ユーザーを削除）**」を選択する。

![ユーザーを削除する][34]

ユーザーを削除すると、Braze は以下のデータを一切保持しません。

- ユーザーが持っていたすべての属性
- メールアドレス
- 電話番号
- 外部ユーザー ID
- 性別
- 国
- 言語
- その他の類似データ

[1]: {% image_buster /assets/img/add_new_user_1.png %}
[2]: {% image_buster /assets/img/add_new_user_2.png %}
[3]: {% image_buster /assets/img/add_new_user_3.png %}
[4]: {% image_buster /assets/img_archive/suspend_user.png %}
[5]: {% image_buster /assets/img_archive/suspend_user2.png %}
[27]: {% image_buster /assets/img/add-user.gif %} 「新規ユーザープロセスの追加」
[34]: {% image_buster /assets/img_archive/delete_user_new.png %}