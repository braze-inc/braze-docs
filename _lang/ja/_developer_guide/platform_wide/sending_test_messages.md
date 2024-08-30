---
nav_title: テストメッセージの送信
article_title: テストメッセージの送信
page_order: 3
description: "このリファレンス記事では、さまざまなチャネルに対するテストメッセージの送信について説明します。"

---

# テストメッセージの送信

> メッセージング キャンペーンをユーザー s に送信する際には、まず、正しく表示され、意図した方法で動作することを確認するために、テストを行うことができます。テストメッセージを作成して送信し、デバイスまたはチームメンバーを選択するのは、ダッシュボードのツールを使用すると非常に簡単です。

## 指定試験Segmentの作成 <a class="margin-fix" name="test-segment"></a>

テストSegmentを設定したら、これを使用してメッセージング チャネルs の**any** をテストできます。適切に設定されている場合、プロセスは一度だけ実行する必要があります。

テストSegmentを設定するには、ダッシュボードの**Segment s** ページに移動し、新しいSegmentを作成します。**フィルターを追加**をクリックして、ドロップダウンメニューの下部にあるテストフィルターのいずれかを選択します。

![ターゲットステップで使用可能なフィルターを表示するBraze試験キャンペーン。][1]

このような2 つのテストフィルターs を使用すると、特定のメールアドレスまたは外部\[ユーザー ID s][2]] を持つユーザーs を選択できます。

![テストを読む見出しの下にいくつかのフィルターが表示されるドロップダウンメニュー][3]

メールアドレスと外部ユーザー識別フィルターの両方に、次の3 つの選択肢があります。

  1) **"Equals"** -指定したメールまたはユーザー IDと完全に一致するものが検索されます。これは、1 つのメールまたはユーザー ID に関連付けられたデバイスにのみテストキャンペーンを送信する場合に使用します。

  2) **"Does Not Equal"** \- 特定のメールまたはユーザー IDを試験キャンペーンsから除外する場合に使用します。

  3) **"Matches"** \- 指定した検索語句の一部に一致するメールの住所またはユーザー IDs を持つユーザーs が検索されます。これを使用すると、"@yourcompany.com" address を持つユーザーs のみを検索できます。これにより、自分のチームの全員にメールを送信できます。

"matches"オプションを使用して、メールの住所を| 文字で区切ることで、複数の特定のメールs を選択できます(たとえば、"matches" "email1@braze.com\|email2@braze.com")。

これらのフィルターs は、テストユーザーs の一覧を絞り込むために、互いに組み合わせて使用することもできます。たとえば、テストSegmentには、"matches""@braze.com"と、"と等しくない"sales@braze.com"という別のフィルターを含めることができます。

テストフィルターs をテストSegmentに追加した後、Segmentエディタの上部にある**プレビュー** をクリックするか、エディタの右隅にあるギアアイコンをクリックしてそのSegmentのユーザーデータをCSV にエクスポートし、ドロップダウンメニューから**すべてのユーザーデータをエクスポート** を選択することで、意図したユーザーのみを選択したことを確認できます。

![セグメントディテールというBraze キャンペーンの一部][4]

>  セグメントのユーザーデータを CSV にエクスポートすると、そのセグメントに該当するユーザーを最も正確に把握できます。**プレビュー**タブは、Segment内のユーザーsの見本にすぎないため、意図したすべてのメンバが選択されていないというアプリがあります。

## 試験プッシュ通知またはアプリ内メッセージの送信 <a class="margin-fix" name="push-inapp-test"></a>

テストプッシュ通知s またはアプリ内メッセージs を送信するには、以前に作成したテストSegmentを対象とする必要があります。まず、キャンペーンを作成し、通常のステップs に従います。**Target Users**ステップに到達したら、ドロップダウンメニューからテストSegmentを選択します。

![ターゲットステップで使用可能なSegmentを表示するBraze試験キャンペーン。][11]

キャンペーンの確認を完了し、それを起動してプッシュ通知とアプリ内メッセージ s を確認します。

>  キャンペーンコンポーザーの**Schedule**の部分で、1つのキャンペーンを使用して複数回テストメッセージを送信する場合は、必ず**ユーザーがキャンペーン**を受信できるようにします。

## 試験メールを送信する

メールをテストするだけの場合は、必ずしもテストSegmentを設定する必要はありません。キャンペーンのメールを作成するキャンペーンコンポーザーの最初のステップで、**Send Test**をクリックし、テストメールを送信したいメールを入力します。

![「送信テスト」を選択したBraze キャンペーン][5]

{% alert tip %}
テストメッセージでアプリ終了する[TEST (またはSEED)]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#append-email-subject-lines)を有効または無効にすることもできます。
{% endalert %}

## コマンドラインからのテスト

または、コマンドラインを使用してプッシュ通知をテストする場合は、プラットフォームごとに以下のサンプルを実行できます。

### cURL によるiOS アプリ s によるプッシュのテスト

CURL および\[Messaging API][13] を使用して、端末から単一の通知を送信できます。次のフィールドをテストケースの正しい値に置き換える必要があります。

- `YOUR_API_KEY` - **設定**> **APIキー**で利用可能
- `YOUR_EXTERNAL_USER_ID` - **Search Users**ページで利用可能
- `YOUR_KEY1` (省略可能)
- `YOUR_VALUE1` (省略可能)

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、これらのページは別の場所にあります。<br>\- \[**API キー**] は \[**開発者コンソール**] > \[**API 設定**] にあります。<br>\- \[**ユーザー検索**]は、\[**ユーザー**] > \[**ユーザー検索**] にあります。
{% endalert %}

>  以下の例は、`US-01` インスタンスの顧客s のアプリの適切なAPI エンドポイントs を示しています。このインスタンスにいない場合は、\[API ドキュメント][66] を参照して、リクエストを実行するエンドポイントを確認します。

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert": "Test push",
      "extra": {
        "YOUR_KEY1" :"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

### cURL によるAndroid アプリ s によるプッシュのテスト

cURL と\[Messaging API][13] を使用して、端末から単一の通知を送信できます。次のフィールドをテストケースの正しい値に置き換える必要があります。

- `YOUR_API_KEY` ([**設定**] > [**API キー**]に移動)
- `YOUR_EXTERNAL_USER_ID` ([**ユーザーを検索**] ページでプロファイルを検索)
- `YOUR_KEY1` (省略可能)
- `YOUR_VALUE1` (省略可能)

>  以下の例は、`US-01` インスタンスの顧客s のアプリの適切なAPI エンドポイントs を示しています。このインスタンスにいない場合は、\[API ドキュメント][66] を参照して、リクエストを実行するエンドポイントを確認します。

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

### Kindle アプリ s によるcURL によるプッシュのテスト

cURL と\[Messaging API][13] を使用して、端末から単一の通知を送信できます。次のフィールドをテストケースの正しい値に置き換える必要があります。

- `YOUR_API_KEY` - **Developer Console**ページで利用可能
- `YOUR_EXTERNAL_USER_ID` - **User Search**ページで利用可能
- `YOUR_KEY1` (省略可能)
- `YOUR_VALUE1` (省略可能)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "kindle_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

## テストメッセージの制限

テストメッセージに完全な機能パリティがなく、キャンペーンまたはキャンバスを実際のユーザーs の集合に起動できない場合があります。このような場合、このビヘイビアを検証するには、キャンペーンまたはキャンバスを限定されたテストユーザーs で起動する必要があります。

- **テストメッセージ**からBraze\[ユーザー設定センター][16]を表示すると、送信ボタンがグレー表示になります
- list-配信停止 ヘッダーは、テストメッセージ機能によって送信されるメールには含まれません
- アプリ内メッセージおよびコンテンツカードの場合、ターゲットユーザーにターゲットデバイスのプッシュトークンが必要です

[1]: {% image_buster /assets/img_archive/testmessages1.png %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#setting-user-ids
[3]: {% image_buster /assets/img_archive/testmessages2.png %}
[4]: {% image_buster /assets/img_archive/testmessages3.png %}
[5]: {% image_buster /assets/img_archive/testmessages45.png %}
[9]: {{site.baseurl}}/developer_guide/platform_wide/platform_features/#user-segmentation
[11]: {% image_buster /assets/img_archive/test_segment.png %}
[13]: {{site.baseurl}}/api/endpoints/messaging/
[66]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
[16]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups
[14]: {{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#append-email-subject-lines
