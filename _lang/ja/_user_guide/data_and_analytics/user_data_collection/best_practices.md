---
nav_title: 収集のベストプラクティス
article_title: 収集のベストプラクティス
page_order: 3.1
page_type: reference
description: "次の記事は、新規ユーザーデータと既存のユーザーデータを収集するためのさまざまな方法とベストプラクティスを明確に理解するうえで役立ちます。"

---

# 収集のベストプラクティス

> 顧客のユーザープロファイルのライフサイクルを想定するときに、既知および未知のユーザーについてユーザーデータをいつ、どのように収集すべきかを知ることが困難な場合があります。次の記事は、新規ユーザーデータと既存のユーザーデータを収集するためのさまざまな方法とベストプラクティスを明確に理解するうえで役立ちます。

## 概要

次の例はメール収集のユースケースですが、ロジックはさまざまなデータ収集シナリオで使用できます。この例では、サインアップフォーム、またはユーザー情報を収集する方法をすでに連携していることを前提としています。 

ユーザーがログに記録するための情報を提供したら、データがデータベースにすでに存在するかどうかを確認し、必要に応じてエイリアスのユーザープロファイルを作成するか、既存のユーザープロファイルを更新することをお勧めします。 

ある未知のユーザーがサイトを表示してから、後日アカウントを作成したか、メールサインアップで身元を明らかにした場合は、プロファイルのマージを慎重に処理する必要があります。マージ方法に基づいて、エイリアスのみを持つユーザー情報または匿名データが上書きされる場合があります。

## Web フォームを使用したユーザーデータのキャプチャ

### ステップ 1: ユーザーが存在するかどうかの確認

ユーザーが Web フォームから情報を入力したら、そのメールアドレスを持つユーザーがデータベース内にすでに存在するかどうかを確認します。これは、次の 2 つの方法のいずれかで実行できます。

- **内部データベースのチェック (推奨)**<br>提供されたユーザー情報を含む外部レコードまたはデータベースが Braze の外部にある場合は、メール送信時またはアカウント作成時に参照して、そのユーザーの情報がまだ取得されていないことを確認します。<br><br>
- **[`/users/export/id`エンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)**<br>次の呼び出しを実行して、返されたユーザー配列が空か、値を含んでいるかを確認します。
  ```json
  --data-raw '{
    "email_address": "example@braze.com",
    "fields_to_export": ["external_id", "user_aliases"]
  }'
  ```

{% alert important %}
1 人のユーザーを照会するときに、このエンドポイントを多用することはお勧めしません。このエンドポイントには、1 分あたり 2500 件のリクエストのレート制限が適用されます。エンドポイントのレート制限の詳細については、「[リクエストタイプ別のレート制限]({{site.baseurl}}/api/api_limits/#rate-limits-by-request-type)」を参照してください。
{% endalert %}

### ステップ 2: ユーザーの記録または更新

- **ユーザーが存在する場合:**
  - 新しいプロファイルを作成しません。
  - そのユーザープロファイルにカスタム属性 (`newsletter_subscribed: true` など) を記録して、そのユーザーがニュースレターのサブスクリプションを介してメールアドレスを送信したことを示します。Braze 内に同じメールアドレスを持つ複数のユーザープロファイルが存在する場合、すべてのプロファイルがエクスポートされます。<br><br>
- **ユーザーが存在しない場合:**
  - [`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)を使用してエイリアスのみを持つプロファイルを作成します。このエンドポイントは [`user_alias` オブジェクト]({{site.baseurl}}/api/objects_filters/user_alias_object/)を受け入れ、`update_existing_only` が `false` に設定されている場合にエイリアスのみを持つプロファイルを作成します。ユーザーのメールアドレスをユーザーエイリアスとして設定し、今後そのユーザーを参照します (ユーザーには `external_id` がないため)。

![エイリアスのみを持つユーザープロファイルを更新するプロセスを示す図。 あるユーザーが、マーケティングのランディングページでメールアドレスとカスタム属性 (郵便番号) を送信します。ランディングページの収集からエイリアスのみを持つユーザープロファイルを指す矢印は、ユーザー追跡エンドポイントに対する Braze の API リクエストを示します。リクエスト本文には、ユーザーのエイリアス名、エイリアスラベル、メールアドレス、および郵便番号が含まれます。プロファイルには「Braze で作成されたエイリアスのみを持つユーザー」ラベルとリクエスト本文から取得した属性があり、その属性は新規に作成されたプロファイルを反映するデータを示します。][3]{: style="max-width:90%;"}

## メールアドレスのキャプチャフォームを使用したユーザーのメールアドレスのキャプチャ

メールキャプチャフォームを使用して、ユーザーにメールアドレスの送信を促すことができます。入力されたメールアドレスはユーザープロファイルに追加されます。このフォームの設定方法の詳細については、「[メールキャプチャフォーム]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/)」を参照してください。
 
## エイリアスのみを持つユーザーの識別

アカウントの作成時にユーザーを識別する場合、[`/users/identify` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/)を介してエイリアスのみを持つユーザーを識別し、エイリアスのみを持つユーザーを既知のプロファイルとマージすることにより、external ID を割り当てることができます。 

ユーザーがエイリアスのみを持つかどうかを確認するには、ユーザーが[データベース内](#step-1-check-if-user-exists)に存在するかどうかを確認します。
\- 外部レコードが存在する場合、`/users/identify/` エンドポイントを呼び出すことができます。
- [`/users/export/id` エンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) が `external_id` を返す場合、`/users/identify/` エンドポイントを呼び出すことができます。
\- エンドポイントが何も返さない場合、`/users/identify/` 呼び出しを行うべきではありません。

## エイリアスのみを持つユーザーの情報がすでに存在する場合のユーザーデータのキャプチャ

ユーザーがアカウントを作成したり、メールサインアップで身元を明らかにしたりしたときに、プロファイルをマージできます。マージできるフィールドのリストについては、[マージ更新の動作]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior)を参照してください。

### 重複するユーザープロファイルのマージ

ユーザーデータが大きくなるに従って、Braze ダッシュボードから重複するユーザープロファイルをマージできます。これらの重複するプロファイルは、同じ検索クエリを使用して検出する必要があります。ユーザープロファイルを複製する方法の詳細については、[プロファイルのマージ]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#merge-profiles)を参照してください。

また、[プロファイルのマージエンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)を使用して、あるユーザープロファイルを別のユーザープロファイルにマージすることもできます。 

ユーザープロファイルがマージされた後に、この操作を元に戻すことはできません。

## その他のリソース
- 追加のコンテキストについては、Braze の「[ユーザープロファイルのライフサイクル]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/)」の記事を参照してください。<br>
- [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/)、[iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#suggested-user-id-naming-convention)、および [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/) でのユーザー ID の設定および `changeUser()` メソッドの呼び出しに関するドキュメント。

[1]: {% image_buster /assets/img/user_profile_process.png %}
[2]: {% image_buster /assets/img/user_profile_process2.png %}
[3]: {% image_buster /assets/img/user_profile_process3.png %}
