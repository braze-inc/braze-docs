# テストメッセージの送信

> メッセージング キャンペーンをユーザーに送信する際には、まず、正しく表示され、意図した方法で動作することを確認するために、テストを行うことができます。ダッシュボードを使用して、プッシュ通知 s、アプリ内メッセージ s (IAM)、または メール でテストメッセージを作成および送信できます。

## テストメッセージの送信

### ステップ 1: 指定した試験Segmentを作成する <a class="margin-fix" name="test-segment"></a>

テストSegmentを設定したら、それを使用してBraze メッセージング チャネルs をテストできます。正しく設定されている場合、これは1 回だけ行う必要があります。

試験Segmentを設定するには、**Segment s** に移動し、新しいSegmentを作成します。**フィルターを追加**を選択し、試験フィルターsのいずれかを選択します。

![ターゲットステップで使用可能なフィルターを表示するBraze試験キャンペーン。]({% image_buster /assets/img_archive/testmessages1.png %})

テストフィルターs では、指定したメールアドレスまたは[外部ユーザー ID]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#setting-user-ids) を持つユーザーs のみがテストメッセージを送信するようにできます。

![「テスト」という項目の下にいくつかのフィルターがリストされたドロップダウンメニュー]({% image_buster /assets/img_archive/testmessages2.png %})

メールアドレスと外部ユーザー識別フィルターの両方に、以下の選択肢があります。

| 演算子          | 説明 |
|------------------|--------------------------------------------------------------------------------------------------------------------------------|
| `equals`      | これにより、指定したメールまたはユーザー IDと完全に一致するものが検索されます。これは、1 つのメールまたはユーザー ID に関連付けられたデバイスにのみテストキャンペーンを送信する場合に使用します。 |
| `does not equal` | 特定のメールまたはユーザー IDを試験キャンペーンsから除外する場合に使用します。 |
| `matches`     | これにより、指定した検索語句の一部と一致するメールの住所またはユーザー IDs を持つユーザーs が検索されます。これを使用して、`@yourcompany.com` アドレスを持つユーザーs のみを検索できます。これにより、自分のチームの全員にメッセージを送信できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

"`matches`"オプションを使用し、メールの住所を| 文字で区切ることで、複数のメールを選択できます。例: "`matches`" "`email1@braze.com` | `email2@braze.com`"複数の演算子を組み合わせることもできます。たとえば、テストSegmentには、"`matches`" "`@braze.com`" および" `does not equal`" " `sales@braze.com`" という別のフィルターを含めることができます。 

テストフィルターs をテストSegmentに追加した後、**プレビュー** を選択するか、**設定** > **CSV エクスポートすべてのユーザーデータ** を選択して、そのSegmentのユーザーデータをCSVファイルにエクスポートすることで、動作していることを確認できます。

![「セグメントの詳細」というタイトルの Braze キャンペーンのセクション]({% image_buster /assets/img_archive/testmessages3.png %})

{% alert note %}
SegmentのユーザーデータをCSVファイルにエクスポートすることは、ユーザーsのサンプルのみがプレビューに表示され、すべてのユーザーsが含まれているわけではないため、最もACキュレートな確認方法です。
{% endalert %}

### ステップ 2:メッセージを送信する

Braze ダッシュボードまたはコマンドラインを使用して、メッセージを送信できます。

{% tabs local %}
{% tab Using the dashboard %}
{% subtabs %}
{% subtab push or in-app message %}
テストプッシュ通知またはアプリ内メッセージを送信するには、以前に作成したテストセグメントを対象とする必要があります。まず、キャンペーンを作成し、通常のステップに従います。**Target Audiences**ステップに到達したら、ドロップダウンメニューからテストSegmentを選択します。

![ターゲットステップで使用可能なSegmentを表示するBraze試験キャンペーン。]({% image_buster /assets/img_archive/test_segment.png %})

キャンペーンを確認し、起動してプッシュ通知とアプリ内メッセージ s を確認します。

{% alert note %}
1つのキャンペーンを使用して自分自身にテストメッセージを複数回送信する場合は、キャンペーンコンポーザーの [**スケジュール**] 部分で [**ユーザーがキャンペーンを受け取る資格を再取得できるようにする**] を選択してください。
{% endalert %}
{% endsubtab %}

{% subtab email message %}
メールをテストするだけの場合は、必ずしもテストセグメントを設定する必要はありません。キャンペーンのメールを作成するキャンペーンコンポーザーの最初のステップで、**Send Test**をクリックし、テストメールを送信したいメールを入力します。 

![[テスト送信] タブが選択された Braze キャンペーン]({% image_buster /assets/img_archive/testmessages45.png %})

{% alert tip %}
[TEST (または SEED)]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#append-email-subject-lines) がテストメッセージに追加されるのを有効または無効にすることもできます。
{% endalert %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Using the command line %}
または、cURL と[ Braze メッセージAPI]({{site.baseurl}}/api/endpoints/messaging/) を使用して単一の通知を送信できます。これらの例では、`US-01` インスタンスを使用してリクエストを作成しています。詳細については、[API エンドポイント s]({{site.baseurl}}/api/basics/#endpoints)を参照してください。

{% subtabs local %}
{% subtab android %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "CUSTOM_KEY":"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}

{% subtab swift %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert": "Test push",
      "extra": { 
        "CUSTOM_KEY" :"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}

{% subtab kindle %}
```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {BRAZE_API_KEY}" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "kindle_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "CUSTOM_KEY":"CUSTOM_VALUE"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
{% endsubtab %}
{% endsubtabs %}

次のように置き換えます。

| placeholder         | 説明                                               |
|---------------------|-----------------------------------------------------------|
| `BRAZE_API_KEY`      | 認証に使用するBraze API キー。Braze で、**Settings** > **API Keys** に移動してキーを見つけます。 |
| `EXTERNAL_USER_ID` | 指定したユーザーにメールを送信するために使用する外部ユーザー ID。Brazeで、**Audience**> **検索ユーザーs**に移動し、ユーザーを検索します。 |
| `CUSTOM_KEY`         | (オプション) 追加データ用のカスタムキー。              |
| `CUSTOM_VALUE`       | (オプション) カスタムキーに割り当てられたカスタム値。    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}

## 試験の限界

テストメッセージに完全な機能パリティがなく、キャンペーンまたはキャンバスを実際のユーザーの集合に起動できない場合があります。このような場合、この動作を検証するには、限られたテストユーザーに対してキャンペーンまたはキャンバスを開始する必要があります。

- [ユーザー設定センター]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups)というBrazeを**テストメッセージ**から表示すると、送信ボタンがグレー表示になります。
- list-配信停止 ヘッダーは、テストメッセージ機能によって送信されるメールには含まれません。
- アプリ内メッセージおよびコンテンツカードの場合、ターゲットユーザーにはターゲットデバイスのプッシュトークンが必要です。
