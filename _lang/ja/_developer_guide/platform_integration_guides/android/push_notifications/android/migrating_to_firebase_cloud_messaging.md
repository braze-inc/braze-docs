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

## レート制限

Firebase Cloud Messaging (FCM) API には、1分当たりに600,000リクエストというデフォルトのレート制限があります。この制限に達した場合、Brazeは数分後に自動的に再試行します。増加をリクエストするには、[Firebaseサポート](https://firebase.google.com/support)に連絡してください。

## FCMへの移行

### ステップ1:プロジェクトIDを確認してください

まず、Google Cloud を開きます。プロジェクトのホームページで、**プロジェクトID**フィールドの番号を確認します。次に、これをFirebaseプロジェクトの番号と比較します。

![Google Cloud プロジェクトのホームページで「プロジェクトID」が強調表示されています。]({% image_buster /assets/img/android/push_integration/migration/verify-project-id/project-id-gcp.png %})

次に、Firebase Console を開き、<i class="fa-solid fa-gear"></i>[**設定**] > [**プロジェクト設定**] を選択します。

![[設定] メニューが開いた状態の Firebase プロジェクト。]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

「**一般**」タブで、「**プロジェクトID**」がGoogle Cloudプロジェクトに記載されているものと一致していることを確認します。

![Firebase プロジェクトの「設定」ページで「プロジェクト ID」がハイライトされています。]({% image_buster /assets/img/android/push_integration/migration/verify-project-id/project-id-gfb.png %})

### ステップ2:送信者 ID を確認する

まず、Braze を開き、<i class="fa-solid fa-gear"></i>[**設定**] > [**アプリ設定**] を選択します。

![[アプリ設定] が強調表示された状態で Braze で [設定] メニューが開いています。]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %}){: style="max-width:80%;"}

Android アプリの [**プッシュ通知の設定**] で、[**Firebase Cloud Messaging の送信者 ID**] フィールドの番号を確認します。次にこれを Firebase プロジェクトのものと比較します。

![「プッシュ通知設定」のフォームです。]({% image_buster /assets/img/android/push_integration/migration/verify-sender-id/verify-sender-id.png %})

次に、Firebase Console を開き、<i class="fa-solid fa-gear"></i>[**設定**] > [**プロジェクト設定**] を選択します。

![[設定] メニューが開いた状態の Firebase プロジェクト。]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

[**Cloud Messaging**] を選択します。[**Cloud Messaging API (レガシー)**] で、**送信者 ID** が Braze ダッシュボードに表示されているものと一致していることを確認します。

![[送信者 ID] が強調表示されている Firebase プロジェクトの「Cloud Messaging」ページ。]({% image_buster /assets/img/android/push_integration/migration/verify-sender-id/verify-sender-id-firebase.png %})

### ステップ3:Firebase Cloud Messaging API を有効にする

Google Cloud で、Android アプリが使用しているプロジェクトを選択し、[Firebase Cloud Messaging API](https://console.cloud.google.com/apis/library/fcm.googleapis.com) を有効にします。

![有効になっている Firebase Cloud Messaging API]({% image_buster /assets/img/android/push_integration/create_a_service_account/firebase-cloud-messaging-api-enabled.png %}){: style="max-width:80%;"}

### ステップ4: サービスアカウントを作成する

次に、新しいサービスアカウントを作成し、FCM トークンの登録時に Braze が許可された API 呼び出しを行えるようにします。Google Cloud で、[**サービスアカウント**] に移動し、プロジェクトを選択します。[**サービスアカウント**] ページで [**サービスアカウントの作成**] を選択します。

![「サービス アカウントの作成」が強調表示されたプロジェクトのサービス アカウントのホーム ページ。]({% image_buster /assets/img/android/push_integration/create_a_service_account/select-create-service-account.png %})

サービスアカウント名、ID、説明を入力して、[**作成して続行**] を選択します。

![[サービスアカウントの詳細] のフォーム。]({% image_buster /assets/img/android/push_integration/create_a_service_account/enter-service-account-details.png %})

[**ロール**] フィールドで、ロールのリストから [**Firebase Cloud Messaging API 管理者**] を見つけて選択します。アクセスをより制限する場合は、`cloudmessaging.messages.create` 権限を持つ[カスタムロール](https://cloud.google.com/iam/docs/creating-custom-roles)を作成し、代わりにリストからそれを選択します。[**完了**] を選択します。

{% alert warning %}
[_Firebase Cloud Messaging 管理者_] ではなく、[_Firebase Cloud Messaging **API** 管理者_] を選択してください。
{% endalert %}

![[Firebase Cloud Messaging API 管理者] がロールとして選択されている、「このサービスアカウントにプロジェクトへのアクセス権を付与」するためのフォーム。]({% image_buster /assets/img/android/push_integration/create_a_service_account/add-fcm-api-admin.png %})

### ステップ5:権限を確認する（オプション）

サービスアカウントが持っている権限を確認するには、Google Cloud を開き、プロジェクトに移動して、[**IAM**] を選択します。**プリンシパル別に表示** で、**過剰な権限** を選択します。

![各プリンシパルごとに過剰な権限の数が一覧表示される「原則別表示」タブ。]({% image_buster /assets/img/android/push_integration/create_a_service_account/select-excess-permissions.png %})

これで、選択した役割に割り当てられている現在の権限を確認できます。

![選択した役割に割り当てられている現在の権限のリスト。]({% image_buster /assets/img/android/push_integration/create_a_service_account/review-permissions.png %}){: style="max-width:75%;"}

### ステップ 6:JSON 認証情報を生成する

次に、FCM サービスアカウントの JSON 認証情報を生成します。Google Cloud IAM & Admin で、[**サービスアカウント**] に移動し、プロジェクトを選択します。[先ほど作成した](#step-4-create-a-service-account) FCM サービスアカウントを見つけて、<i class="fa-solid fa-ellipsis-vertical"></i>[**アクション**] > [**キーの管理**] を選択します。

![[アクション] メニューが開いた状態の、プロジェクトのサービスアカウントホームページ。]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-manage-keys.png %})

[**キーの追加**] > [**新しいキーを作成**] を選択します。

{% alert note %}
新しいキーを作成しても、レガシーキーは削除されません。[**認証情報を元に戻す**] を選択して誤って新しいキーを削除した場合、Braze はバックアップとしてレガシーキーを使用します。
{% endalert %}

![[キーを追加] メニューが開いた状態の選択されたサービスアカウント。]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create-new-key.png %})

[**JSON**] を選択し、[**作成**] を選択します。FCM プロジェクト ID とは異なる Google Cloud のプロジェクト ID を使用してサービスアカウントを作成した場合は、JSON ファイルで `project_id` に割り当てられた値を手動で更新する必要があります。

キーをどこにダウンロードしたかを覚えておいてください。次のステップで必要になります。

![「JSON」が選択された秘密キーの作成フォームです。]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create.png %}){: style="max-width:65%;"}

{% alert warning %}
秘密キーが漏洩した場合は、セキュリティリスクが生じる可能性があります。JSON の認証情報は安全な場所に保存しておいてください。キーは Braze にアップロードした後で削除します。
{% endalert %}

### ステップ 7: JSON の認証情報を Braze にアップロードする

Braze で、<i class="fa-solid fa-gear"></i>[**設定**] > [**アプリの設定**] を選択します。

![[アプリ設定] が強調表示された状態で Braze で [設定] メニューが開いています。]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %})

[**プッシュ通知の設定**] で [**JSON ファイルのアップロード**] を選択し、[先ほど生成した](#step-6-generate-json-credentials)ファイルを選択します。完了したら、[**保存**] を選択します。

![[Firebase Cloud Messaging サーバーキー] フィールドで秘密キーが更新されている [プッシュ通知設定] のフォーム。]({% image_buster /assets/img/android/push_integration/migration/upload_json_credentials/upload-json-file.png %})

{% alert warning %}
秘密キーが漏洩した場合は、セキュリティリスクが生じる可能性があります。キーが Braze にアップロードされたので、[先に生成した](#step-6-generate-json-credentials)ファイルをコンピューターから削除します。
{% endalert %}

### ステップ 8新しい資格情報をテストする（オプション）

認証情報を Braze にアップロードするとすぐに、新しい認証情報を使用してプッシュ通知の送信を始めることができます。新しい認証情報をテストするには、実際のまたはテストのプッシュ通知を FCM または Braze を使用してアプリに送信します。プッシュ通知が通れば、すべてが正常に動作しています。それがない場合:

- [送信者 ID を確認します](#step-2-verify-your-sender-id)
- [自分の権限を確認します](#step-5-verify-permissions-optional)
- [メッセージアクティビティログ]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)でプッシュ通知エラーを確認する

お困りの場合は、[資格情報のリセット](#reverting-your-credentials)をご覧ください。

## 認証情報を元に戻す

いつでも、新しい認証情報を削除し、レガシー認証情報を復元できます。認証情報が復元されるとすぐに、代わりに新しい認証情報を使用してプッシュ通知の送信を始めることができます。

Braze で、<i class="fa-solid fa-gear"></i>[**設定**] > [**アプリの設定**] を選択します。**プッシュ通知設定**で、**資格情報を元に戻す**を選択します。

{% alert warning %}
新しい認証情報を削除すると、後で復元することはできません。[新しい認証情報を生成](#step-6-generate-json-credentials)し、もう一度[それらを Braze にアップロード](#step-7-upload-your-json-credentials-to-braze)する必要があります。
{% endalert %}

![「プッシュ通知設定」のフォームで「資格情報を元に戻す」ボタンが強調表示されています。]({% image_buster /assets/img/android/push_integration/revert-credentials.png %})

## よくある質問 (FAQ) {#faq}

### 新しい資格情報が機能しているかどうかはどうすればわかりますか？

新しい認証情報は、Brazeにアップロードするとすぐに機能し始めます。それらをテストするには、**テスト資格情報**を選択します。エラーが発生した場合は、いつでも[資格情報を元に戻す](#reverting-your-credentials)ことができます。

### 未使用のアプリや開発中のアプリのためにFCMに移行する必要がありますか？

いいえ。ただし、未使用のアプリと開発アプリには、移行を求める警告メッセージが引き続き表示されます。このメッセージを削除するには、新しい認証情報をアップロードするか、それらのアプリをワークスペースから削除します。これらのアプリを削除することを選択した場合、誰かが使用している可能性があるため、最初にチームに確認してください。

### エラーメッセージはどこで確認できますか？

[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)でプッシュ通知エラーを確認できます。

### 移行する前に、アプリやSDKを更新する必要がありますか？

いいえ。新しい資格情報をBrazeにアップロードするだけで済みます。

### 古いレガシー認証情報を先に削除する必要がありますか?

いいえ。新しい認証情報を削除する必要がある場合は、[レガシー認証情報を代わりに使用できます](#reverting-your-credentials)。

### 移行後、なぜBrazeに警告メッセージがまだ表示されるのですか？

移行が必要な Android アプリがワークスペースに少なくとも1つある場合は、この警告メッセージが引き続き表示されます。必ずすべてのAndroidアプリをGoogleの完全にサポートされているFCM APIに移行してください。

### 移行後、プッシュ通知を再送信するまでどのくらいかかりますか？

移行後、すぐに新しい認証情報を使用して、プッシュ通知の送信を開始できます。

### FCMプロジェクトとは異なるプロジェクトを使用してサービスアカウントを作成した場合はどうなりますか？

FCM プロジェクト ID とは異なる Google Cloud のプロジェクト ID を使用してサービスアカウントを作成した場合は、[新しいアカウントを作成](#step-6-generate-json-credentials)した後に、JSON ファイルで `project_id` に割り当てられた値を手動で更新する必要があります。
