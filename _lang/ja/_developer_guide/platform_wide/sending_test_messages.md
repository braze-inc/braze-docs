---
nav_title: テストメッセージの送信
article_title: テストメッセージの送信
page_order: 3
description: "このリファレンス記事では、さまざまなチャネルに対するテストメッセージの送信について説明します。"

---

# テストメッセージの送信

> メッセージング キャンペーンをユーザー s に送信する際には、まず、正しく表示され、意図した方法で動作することを確認するために、テストを行うことができます。テストメッセージを作成して送信し、デバイスまたはチームメンバーを選択するのは、ダッシュボードのツールを使用すると非常に簡単です。

## 指定されたテストセグメントの作成 <a class="margin-fix" name="test-segment"></a>

テストセグメントを設定したら、それを使用して**任意の**メッセージングチャネルをテストできます。正しく設定されていれば、このプロセスは1回実行するだけで済みます。

テストセグメントを設定するには、ダッシュボードの**セグメント**ページに移動し、新しいセグメントを作成します。**フィルターを追加**をクリックして、ドロップダウンメニューの下部にあるテストフィルターのいずれかを選択します。

![ターゲットステップで使用可能なフィルターを表示するBraze試験キャンペーン。][1]

このような2つのテストフィルターを使用すると、特定のメールアドレスまたは外部 \[ユーザー ID][2] を持つユーザーを選択できます。

![「テスト」という項目の下にいくつかのフィルターがリストされたドロップダウンメニュー][3]

メールアドレスと外部ユーザー ID フィルターの両方に、次の3つの選択肢があります。

  1) **"Equals"** -指定したメールまたはユーザー IDと完全に一致するものが検索されます。これは、1 つのメールまたはユーザー ID に関連付けられたデバイスにのみテストキャンペーンを送信する場合に使用します。

  2) **"Does Not Equal"** \- 特定のメールまたはユーザー IDを試験キャンペーンsから除外する場合に使用します。

  3) **"Matches"** \- 指定した検索語の一部と一致するメールアドレスまたはユーザー ID を持つユーザーを検索します。これを使用すると、"@yourcompany.com" address を持つユーザーs のみを検索できます。これにより、自分のチームの全員にメールを送信できます。

"matches"オプションを使用して、メールの住所を| 文字で区切ることで、複数の特定のメールs を選択できます(たとえば、"matches" "email1@braze.com\|email2@braze.com")。

これらのフィルターを組み合わせて使用すると、テストユーザーのリストを絞り込むこともできます。例えば、テストセグメントには、「@braze.com」に「一致する」 メールアドレスフィルターと、「sales@braze.com」に「等しくない」別のフィルターを含めることができます。 

テストフィルターをテストセグメントに追加した後、セグメントエディターの上部にある \[**プレビュー**] をクリックするか、エディターの右上隅にある歯車アイコンをクリックし、ドロップダウンメニューから \[**すべてのユーザーデータを CSV 形式でエクスポートする**] を選択して、セグメントのユーザーデータを CSV にエクスポートすることにより、意図したユーザーのみが選択されていることを確認できます。

![「セグメントの詳細」というタイトルの Braze キャンペーンのセクション][4]

>  セグメントのユーザーデータを CSV にエクスポートすると、そのセグメントに該当するユーザーを最も正確に把握できます。\[**プレビュー**] タブはセグメント内のユーザーのサンプルにすぎないため、目的のメンバーがすべて選択されていないように見える場合があります。

## テストプッシュ通知またはアプリ内メッセージの送信 <a class="margin-fix" name="push-inapp-test"></a>

テストプッシュ通知s またはアプリ内メッセージs を送信するには、以前に作成したテストSegmentを対象とする必要があります。まず、キャンペーンを作成し、通常のステップs に従います。**Target Users**ステップに到達したら、ドロップダウンメニューからテストSegmentを選択します。

![ターゲットステップで使用可能なSegmentを表示するBraze試験キャンペーン。][11]

キャンペーンの確認を完了し、それを起動してプッシュ通知とアプリ内メッセージをテストします。

>  1つのキャンペーンを使用して自分自身にテストメッセージを複数回送信する場合は、キャンペーンコンポーザーの \[**スケジュール**] 部分で \[**ユーザーがキャンペーンを受け取る資格を再取得できるようにする**] を選択してください。

## テストメールメッセージの送信

メールをテストするだけの場合は、必ずしもテストSegmentを設定する必要はありません。キャンペーンのメールを作成するキャンペーンコンポーザーの最初のステップで、**Send Test**をクリックし、テストメールを送信したいメールを入力します。 

![\[テスト送信] タブが選択された Braze キャンペーン][5]

{% alert tip %}
[TEST (または SEED)]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#append-email-subject-lines) がテストメッセージに追加されるのを有効または無効にすることもできます。
{% endalert %}

## コマンドラインからのテスト

または、コマンドラインを使用してプッシュ通知をテストする場合は、プラットフォームごとに次の例に従うことができます。

### cURL を使用した iOS アプリでのプッシュのテスト

CURL と \[メッセージング API][13] を使用して、端末経由で通知を1回送信できます。次のフィールドをテストケースの正しい値に置き換える必要があります。

- `YOUR_API_KEY` - **設定**> **APIキー**で利用可能
- `YOUR_EXTERNAL_USER_ID` - **Search Users**ページで利用可能
- `YOUR_KEY1` (省略可能)
- `YOUR_VALUE1` (省略可能)

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、これらのページは別の場所にあります。<br>\- \[**API キー**] は \[**開発者コンソール**] > \[**API 設定**] にあります。<br>\- \[**ユーザー検索**]は、\[**ユーザー**] > \[**ユーザー検索**] にあります。
{% endalert %}

>  次の例では、`US-01` インスタンスの顧客に適した API エンドポイントを示します。このインスタンスを使用していない場合は、\[API のドキュメント][66] を参照して、リクエストを行うエンドポイントを確認してください。

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

### cURL を使用した Android アプリでのプッシュのテスト

cURL と \[メッセージング API][13] を使用して、端末経由で通知を1回送信できます。次のフィールドをテストケースの正しい値に置き換える必要があります。

- `YOUR_API_KEY` ([**設定**] > [**API キー**]に移動)
- `YOUR_EXTERNAL_USER_ID` ([**ユーザーを検索**] ページでプロファイルを検索)
- `YOUR_KEY1` (省略可能)
- `YOUR_VALUE1` (省略可能)

>  次の例では、`US-01` インスタンスの顧客に適した API エンドポイントを示します。このインスタンスを使用していない場合は、\[API のドキュメント][66] を参照して、リクエストを行うエンドポイントを確認してください。

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

cURL と \[メッセージング API][13] を使用して、端末経由で通知を1回送信できます。次のフィールドをテストケースの正しい値に置き換える必要があります。

- `YOUR_API_KEY` - **Developer Console**ページで利用可能
- `YOUR_EXTERNAL_USER_ID` - **ユーザー検索**ページで利用可能
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

テストメッセージに完全な機能パリティがなく、キャンペーンまたはキャンバスを実際のユーザーs の集合に起動できない場合があります。このような場合、この動作を検証するには、限られたテストユーザーに対してキャンペーンまたはキャンバスを開始する必要があります。

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
