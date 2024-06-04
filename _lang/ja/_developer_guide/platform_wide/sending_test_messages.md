---
nav_title: テストメッセージの送信
article_title: テストメッセージの送信
page_order: 3
description: "この参考記事では、さまざまなチャネルへのテストメッセージの送信について説明しています。"

---

# テストメッセージの送信

> メッセージキャンペーンをユーザーに送信する前に、キャンペーンをテストして、正しく表示され、意図したとおりに動作することを確認するとよいでしょう。ダッシュボードのツールを使用すると、テストメッセージを作成して特定のデバイスやチームメンバーに送信するのが非常に簡単です。

## 指定されたテストセグメントの作成 <a class="margin-fix" name="test-segment"></a>

テストセグメントを設定すると、**それを使用して任意のメッセージングチャネルをテストできます**。正しく設定されていれば、この処理は 1 回実行するだけで済みます。

テストセグメントを設定するには、**ダッシュボードのセグメントページに移動して新しいセグメントを作成します**。[**フィルターを追加**] をクリックして、ドロップダウンメニューの下部にあるテストフィルターのいずれかを選択します。

![ターゲティングステップで利用できるフィルターを表示するブレイズテストキャンペーン] [1]

このような2つのテストフィルターにより、特定のメールアドレスまたは外部の [ユーザーID] [2] を持つユーザーを選択できます。

![Testing] という見出しの下に複数のフィルタが一覧表示されたドロップダウンメニュー] [3]

メールアドレスフィルタと外部ユーザ ID フィルタには、どちらも 3 つのオプションがあります。

  1) **「同等」**-入力したメールアドレスまたはユーザーIDと完全に一致するものを探します。これは、1 つのメールまたはユーザー ID に関連付けられたデバイスにのみテストキャンペーンを送信する場合に使用します。

  2) **「等しくない」**-特定のメールまたはユーザーIDをテストキャンペーンから除外したい場合に使用します。

  3) **「一致」**-指定した検索語の一部と一致するメールアドレスまたはユーザーIDを持つユーザーを検索します。これを使用して、」@yourcompany .com」アドレスを持つユーザーのみを検索し、チームの全員にメッセージを送信できます。

「一致」オプションを使用し、電子メールアドレスを | 文字で区切ると、複数の特定の電子メールを選択できます（たとえば、「一致」「email1@braze.com | email2@braze.com「）。

これらのフィルターを相互に組み合わせて使用して、テストユーザーのリストを絞り込むこともできます。たとえば、テストセグメントには、」@braze .com」と「一致する」メールアドレスフィルターと、「sales@braze.com」と「等しくない」別のフィルターを含めることができます。 

テストセグメントにテストフィルターを追加したら、セグメントエディターの上部にある「**プレビュー**」をクリックするか、エディターの右隅にある歯車アイコンをクリックし、ドロップダウンメニューから「CSV Export **All User Data」を選択して、セグメントのユーザーデータを CSV にエクスポートすることで、目的のユーザーのみを選択したことを確認できます**。

![Braze キャンペーンの「セグメント詳細」というタイトルのセクション] [4]

>  セグメントのユーザーデータを CSV にエクスポートすると、そのセグメントに該当するユーザーを最も正確に把握できます。[**プレビュー**] タブはセグメント内のユーザーのサンプルにすぎないため、目的のメンバーがすべて選択されていないように見える場合があります。

## テストプッシュ通知またはアプリ内メッセージの送信 <a class="margin-fix" name="push-inapp-test"></a>

テストプッシュ通知またはアプリ内メッセージを送信するには、以前に作成したテストセグメントをターゲットにする必要があります。まず、キャンペーンを作成し、通常の手順に従います。**Target Users** ステップに到達したら、ドロップダウンメニューからテストセグメントを選択します。

![ターゲティングステップで利用可能なセグメントを表示するブレイズテストキャンペーン] [11]

キャンペーンの確認を完了して起動し、プッシュ通知とアプリ内メッセージをテストします。

>  1 **つのキャンペーンを使用して自分自身にテストメッセージを複数回送信する場合は、キャンペーン作成画面の「**スケジュール**」セクションで、必ず「ユーザーにキャンペーンの再受諾を許可する**」を選択してください。

## テストメールメッセージの送信

メールメッセージのみをテストする場合は、必ずしもテストセグメントを設定する必要はありません。キャンペーンのメールメッセージを作成するキャンペーンコンポーザーの最初のステップで、「**テストを送信**」をクリックし、テストメールの送信先のメールアドレスを入力します。 

![テスト送信タブを選択した状態の Braze キャンペーン] [5]

{% alert tip %}
[テストメッセージに追加される TEST (または SEED)]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#append-email-subject-lines) を有効または無効にすることもできます。
{% endalert %}

## コマンドラインからのテスト

または、コマンドラインでプッシュ通知をテストしたい場合は、プラットフォームごとに次の例に従うこともできます。

### cURL 経由の iOS アプリでのプッシュテスト

CURL と [メッセージング API] [13] を使用して、ターミナルから 1 つの通知を送信できます。次のフィールドをテストケースの正しい値に置き換える必要があります。

- `YOUR_API_KEY` - [**設定**] > [**API キー**] で利用できます。
- `YOUR_EXTERNAL_USER_ID` -「**ユーザーの検索**」ページで利用可能
- `YOUR_KEY1` (省略可能)
- `YOUR_VALUE1` (省略可能)

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、これらのページは別の場所にあります。<br>\- [**API キー**] は [**開発者コンソール**] > [**API 設定**] にあります。<br>\- [**ユーザー検索**]は、[**ユーザー**] > [**ユーザー検索**] にあります。
{% endalert %}

>  以下の例は、`US-01`インスタンスのお客様に適したAPIエンドポイントを示しています。このインスタンスを使用していない場合は、[API ドキュメント] [66] を参照して、リクエストを行うエンドポイントを確認してください。

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

### cURL 経由の Android アプリでのプッシュのテスト

cURL と [メッセージング API] [13] を使用して、ターミナルから 1 つの通知を送信できます。次のフィールドをテストケースの正しい値に置き換える必要があります。

- `YOUR_API_KEY` ([**設定**] > [**API キー**]に移動)
- `YOUR_EXTERNAL_USER_ID` ([**ユーザーを検索**] ページでプロファイルを検索)
- `YOUR_KEY1` (省略可能)
- `YOUR_VALUE1` (省略可能)

>  以下の例は、`US-01`インスタンスのお客様に適したAPIエンドポイントを示しています。このインスタンスを使用していない場合は、[API ドキュメント] [66] を参照して、リクエストを行うエンドポイントを確認してください。

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

### cURL 経由の Kindle アプリによるプッシュのテスト

cURL と [メッセージング API] [13] を使用して、ターミナルから 1 つの通知を送信できます。次のフィールドをテストケースの正しい値に置き換える必要があります。

- `YOUR_API_KEY` -**開発者コンソールページで利用可能**
- `YOUR_EXTERNAL_USER_ID` -**ユーザー検索ページで利用可能**
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

テストメッセージが、実際のユーザーに対してキャンペーンやキャンバスをローンチする場合と完全に同等の機能を備えていない状況がいくつかあります。このような場合、この動作を検証するには、限られた数のテストユーザーを対象にキャンペーンまたはキャンバスを起動する必要があります。

- **テストメッセージからBraze** [設定センター] [16] を表示すると、送信ボタンがグレー表示になります
- list-unsubscribe ヘッダーは、テストメッセージ機能によって送信される電子メールには含まれません
- アプリ内メッセージとコンテンツカードの場合、ターゲットユーザーはターゲットデバイスのプッシュトークンを持っている必要があります

[1]: {% image_buster /assets/img_archive/testmessages1.png %}
[2]:{{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#setting-user-ids
[3]: {% image_buster /assets/img_archive/testmessages2.png %}
[4]: {% image_buster /assets/img_archive/testmessages3.png %}
[5]: {% image_buster /assets/img_archive/testmessages45.png %}
[9]: {{site.baseurl}}/developer_guide/platform_wide/platform_features/#user-segmentation
[11]: {% image_buster /assets/img_archive/test_segment.png %}
[13]: {{site.baseurl}}/api/endpoints/messaging/
[66]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
[16]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups
[14]: {{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#append-email-subject-lines
