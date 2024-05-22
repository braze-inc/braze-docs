---
nav_title: Firebase Cloud Messaging への移行
article_title: Firebase Cloud Messaging API への移行
platform: Android
page_order: 29
description: "この記事では、Google の廃止予定の Cloud Messaging API から Firebase Cloud Messaging (FCM) に移行する方法について説明します。"
channel:
  - push
search_rank: 3
---

# Firebase Cloud Messaging API への移行

> Google の廃止予定の Cloud Messaging API から、完全にサポートされている Firebase Cloud Messaging (FCM) API への移行方法について説明します。詳細については、Google の [Firebase に関する FAQ - 2023 年](https://firebase.google.com/support/faq#fcm-23-deprecation)を参照してください。

{% alert important %}
Android のプッシュ統合を初めて設定する場合は、代わりに[標準 Android プッシュ統合]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration)を参照してください。
{% endalert %}

## ステップ 1:送信者 ID を確認する

まず、Braze を開き、<i class="fa-solid fa-gear"></i>[**設定**] > [**アプリ設定**] を選択します。

![The "Settings" menu open in Braze with "App Settings" highlighted.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %})

Android アプリの [**プッシュ通知の設定**] で、[**Firebase Cloud Messaging の送信者 ID**] フィールドの番号を確認します。次にこれを Firebase プロジェクトのものと比較します。

![The form for "Push Notification Settings".]({% image_buster /assets/img/android/push_integration/migration/verify-sender-id/verify-sender-id.png %})

次に、Firebase Console を開き、<i class="fa-solid fa-gear"></i>[**設定**] > [**プロジェクト設定**] を選択します。

![The Firebase project with the "Settings" menu open.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

[**Cloud Messaging**] を選択します。[**Cloud Messaging API (レガシー)**] で、**送信者 ID** が Braze ダッシュボードに表示されているものと一致していることを確認します。

![The Firebase project's "Cloud Messaging" page with the "Sender ID" highlighted.]({% image_buster /assets/img/android/push_integration/migration/verify-sender-id/verify-sender-id-firebase.png %})

## ステップ 2:Firebase Cloud Messaging API を有効にする

Google Cloud で、Android アプリが使用しているプロジェクトを選択し、[Firebase Cloud Messaging API](https://console.cloud.google.com/apis/library/fcm.googleapis.com) を有効にします。

![Enabled Firebase Cloud Messaging API]({% image_buster /assets/img/android/push_integration/create_a_service_account/firebase-cloud-messaging-api-enabled.png %}){: style="max-width:80%;"}

## ステップ 3:サービスアカウントを作成する

次に、新しいサービスアカウントを作成し、FCM トークンの登録時に Braze が許可された API 呼び出しを行えるようにします。Google Cloud で、[**サービスアカウント**] に移動し、プロジェクトを選択します。[**サービスアカウント**] ページで [**サービスアカウントの作成**] を選択します。

![A project's service account home page with "Create Service Account" highlighted.]({% image_buster /assets/img/android/push_integration/create_a_service_account/select-create-service-account.png %})

サービスアカウント名、ID、説明を入力して、[**作成して続行**] を選択します。

![The form for "Service account details."]({% image_buster /assets/img/android/push_integration/create_a_service_account/enter-service-account-details.png %})

[**ロール**] フィールドで、ロールのリストから [**Firebase Cloud Messaging API 管理者**] を見つけて選択します。アクセスをより制限する場合は、`cloudmessaging.messages.create` 権限を持つ[カスタムロール](https://cloud.google.com/iam/docs/creating-custom-roles)を作成し、代わりにリストからそれを選択します。[**完了**] を選択します。

{% alert warning %}
[_Firebase Cloud Messaging 管理者_] ではなく、[_Firebase Cloud Messaging **API** 管理者_] を選択してください。
{% endalert %}

![The form for "Grant this service account access to project" with "Firebase Cloud Messaging API Admin" selected as the role.]({% image_buster /assets/img/android/push_integration/create_a_service_account/add-fcm-api-admin.png %})

## ステップ 4:JSON 認証情報を生成する

次に、FCM サービスアカウントの JSON 認証情報を生成します。Google Cloud IAM & Admin で、[**サービスアカウント**] に移動し、プロジェクトを選択します。[先ほど作成した](#step-2-create-a-service-account) FCM サービスアカウントを見つけて、<i class="fa-solid fa-ellipsis-vertical"></i>[**アクション**] > [**キーの管理**] を選択します。

![The project's service account homepage with the "Actions" menu open.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-manage-keys.png %})

[**キーの追加**] > [**新しいキーを作成**] を選択します。

{% alert note %}
新しいキーを作成しても、レガシーキーは削除されません。[**認証情報を元に戻す**] を選択して誤って新しいキーを削除した場合、Braze はバックアップとしてレガシーキーを使用します。
{% endalert %}

![The selected service account with the "Add Key" menu open.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create-new-key.png %})

[**JSON**] を選択し、[**作成**] を選択します。

![The form for creating a private key with "JSON" selected.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create.png %}){: style="max-width:65%;"}

{% alert warning %}
秘密キーが漏洩した場合は、セキュリティリスクが生じる可能性があります。JSON の認証情報は安全な場所に保存しておいてください。キーは Braze にアップロードした後で削除します。
{% endalert %}

## ステップ 5:JSON の認証情報を Braze にアップロードする

Braze で、<i class="fa-solid fa-gear"></i>[**設定**] > [**アプリの設定**] を選択します。

![The "Settings" menu open in Braze with "App Settings" highlighted.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %})

[**プッシュ通知の設定**] で [**JSON ファイルのアップロード**] を選択し、[先ほど生成した](#step-3-generate-json-credentials)ファイルを選択します。完了したら、[**保存**] を選択します。

## ステップ 6:プッシュ統合をテストする

新しい認証情報がアップロードされたら、テスト用のプッシュ通知を送信して、統合が正しく設定されていることを確認します。

統合が正しく機能しない場合は、[認証情報を元に戻す] ボタンを使用して、新しい JSON 認証情報を削除し、廃止予定の送信者 ID とサーバーキー認証情報にフォールバックできます。

{% alert tip %}
プッシュメッセージを確実に送信するには、次の点を確認してください。

- 認証情報が Google Cloud Platform の正しいプロジェクト ID (正しい送信者 ID) に存在する。
- 認証情報の権限スコープが正しい。
- 正しい認証情報を正しい Braze ワークスペース (正しい送信者 ID) にアップロードした。
{% endalert %}

![The form for "Push Notification Settings" with the private key updated in the "Firebase Cloud Messaging Server Key" field.]({% image_buster /assets/img/android/push_integration/migration/upload_json_credentials/upload-json-file.png %})

{% alert warning %}
秘密キーが漏洩した場合は、セキュリティリスクが生じる可能性があります。キーが Braze にアップロードされたので、[先に生成した](#step-4-generate-json-credentials)ファイルをコンピューターから削除します。
{% endalert %}
