---
nav_title: キーと値のペア
article_title: キーと値のペア
page_order: 4
description: "このリファレンス記事では、キーと値のペアと、それらを使用して追加のデータペイロードをユーザーデバイスに送信する方法について説明します。"
channel:
  - push
  - in-app messages
  - content cards

---

# キーと値のペア

> Brazeでは、キーと値のペアを介して追加のデータペイロードをユーザーデバイスに送信できます。この機能は、プッシュ、アプリ内、メール、コンテンツカードのメッセージングチャネルで利用できます。 

追加のデータペイロードは、内部メトリックとアプリコンテンツを更新したり、アラートの優先順位付け、ローカリゼーション、サウンドなどのプッシュ通知プロパティをカスタマイズしたりするのに役立ちます。

## プッシュ通知

キーと値のペアは、Android、iOS、および Web プッシュ通知に追加することもできます。メッセージコンポーザーで、「 **設定** 」タブを選択し、「 **新しいペアを追加**」をクリックして、キーと値のペアを指定します。

### iOS

Apple Push Notification Service (APNs) は、キーと値のペアを使用したアラート設定とカスタムデータの送信をサポートしています。APNs は、アラートのプロパティを制御する事前定義されたキーと値を含む、Apple が予約した ```aps``` ライブラリを利用します。

##### APS ライブラリ

|キー |値の型 |値の説明 |
|-------------------|-----------------------------|----------------------------------|
|アラート |文字列または辞書オブジェクト |文字列入力の場合、文字列をメッセージとしてアラートを [閉じる] ボタンと [表示] ボタンで表示します。文字列以外の入力の場合、入力の子プロパティに応じてアラートまたはバナーを表示します |
|バッジ |数値 |アプリアイコンにバッジとして表示される番号を管理します |
|サウンド |文字列 |アラートとして再生するサウンドファイルの名前。アプリのバンドルまたは ```Library/Sounds``` フォルダーにある必要があります |
|コンテンツ利用可能 |数値 |入力値 1 は、起動時またはセッション再開時に新しい情報が利用可能であることをアプリに通知します |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}


##### アラート・プロパティ・ライブラリ

|キー |値の型 |値の説明 |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
|タイトル |文字列 |Apple Watchが通知の一部として短時間表示する短い文字列 |
|ボディ |文字列 |プッシュ通知の内容 |
|タイトル・ロケーション・キー |string または null |ファイルからの ```Localizable.strings``` 現在のローカライゼーションのタイトル文字列を設定するキー |
|タイトル・ロック・アーグス |文字列の配列または null |title-loc-key |
|アクション・ロケーション・キー |string または null の配列 |存在する場合、指定された文字列は [閉じる] ボタンと [表示] ボタン |
|ロックキー |string または null |ファイルから ```Localizable.strings``` 現在のローカライゼーションの通知メッセージを設定するキー |
|loc-引数 |文字列の配列 |loc-key |
|ローンチイメージ |文字列 |ユーザーがアクションボタンをタップしたり、アクションスライドを移動したりしたときに起動画像として使用するApp Bundle内の画像ファイルの名前 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Braze メッセージコンポーザーは、 **alert** とその **プロパティ**、 **content-available**、 **sound**、 **category** の各キーの作成を自動的に処理します。 

これらの値は、プッシュメッセージ作成時に **「設定** 」タブで入力できます。[ **アラート オプション** ] を選択し、新しいキーと値のエントリに自動的に入力されるキーのアラート ディクショナリ キーを選択します。

![][16]
{% raw %}
BrazeがAPNsにプッシュ通知を送信すると、ペイロードはJSONとしてフォーマットされます。

**単純なペイロード**

```
{
    "aps" : { "alert" : "Message received from Spencer" },
}
```

**複雑なペイロード**

```
{
    "aps" : {
        "alert" : {
            "body" : "Hi, welcome to our app!",
            "loc-key" : "France",
            "loc-args" : ["Bonjour", "bienvenue"],
            "action-loc-key" : "Button_Type_1",
            "launch-image" : "Paris"
      },
        "content-available" : 1
    },
}
```

{% endraw %}

##### カスタムのキーと値のペア

ライブラリのペイロード値に加えて ```aps``` 、カスタムのキーと値のペアをユーザーのデバイスに送信できます。これらのペアの値は、ディクショナリ (オブジェクト)、配列、文字列、数値、ブール値などのプリミティブ型に制限されます。

![][17]

カスタムキーと値のペアのユースケースには、ユーザーインターフェースのコンテキストを保持および設定する内部指標が含まれますが、これらに限定されません。Brazeでは、追加のキーと値のペアをプッシュ通知とともに送信して、 [アプリケーションを介してextrasキー][1]内で使用できます。別のキーを使用する場合は、アプリがこのカスタム キーを処理できることを確認してください。

{% alert warning %}
アプリケーションで ab という最上位のキーまたはディクショナリを処理することは避けてください。
{% endalert %}

Appleは、顧客情報や機密データをカスタムペイロードデータとして含めないようにクライアントにアドバイスしています。さらに、Appleは、アラートメッセージに関連するアクションでデバイス上のデータを削除しないことをお勧めします。

{% alert warning %}
HTTP/2 プロバイダー API を使用している場合、APNs に送信する個々のペイロードのサイズは 4096 バイトを超えることはできません。まもなく廃止されるレガシーバイナリインターフェイスは、2048バイトのペイロードサイズのみをサポートします。
{% endalert %}

###### APIトリガーキャンペーン

Braze では、カスタム定義の文字列のキーと値のペア ( ) `extras`を送信できます。APIトリガーキャンペーンおよびスケジュールされたAPIトリガーキャンペーンのエクストラにアクセスするには、ダッシュボードでキーを「example\_key」、値を {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}「」に設定します。これにより、開発者コンソールの出力は `"extras": { "test": { "foo": 1, "bar": 1 }`

### Android

Brazeでは、キーと値のペアを使用して、プッシュ通知で追加のデータペイロードを送信送信できます。

##### データペイロード

iOS プッシュと同様に、カスタムのキーと値のペアをユーザーのデバイスに送信できます。

カスタムキーと値のペアのユースケースには、ユーザーインターフェースのコンテキストの保持と設定を行う内部メトリクスが含まれますが、これらは任意の目的で使用できます。

{% alert important %}
アプリのバックエンドは、データペイロードが正しく機能するために、カスタムのキーと値のペアを処理できる必要があります。
{% endalert %}

###### APIトリガーキャンペーン

Braze では、カスタム定義の文字列のキーと値のペア ( ) `extras`を送信できます。APIトリガーキャンペーンおよびスケジュールされたAPIトリガーキャンペーンのエクストラにアクセスするには、ダッシュボードでキーを「example\_key」、値を {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}「」に設定します。これにより、開発者コンソールの出力 `"extras": { "test": { "foo": 1, "bar": 1 }`は になります。

##### FCM メッセージング・オプション

Android プッシュ通知は、FCM メッセージ オプションを使用してさらにカスタマイズできます。これらには、 [通知の優先度][8]、 [サウンド][10]、遅延、有効期間、折りたたみ可能性が含まれます。これらの値は、プッシュメッセージ作成時に「 **設定** 」タブで指定できます。Braze メッセージコンポーザーでこれらのオプションを設定する方法の詳細については、 [高度なプッシュ通知設定][7] を参照してください。

![][18]

### サイレントプッシュ通知

サイレントプッシュ通知は、アラートメッセージやサウンドを含まないプッシュ通知で、アプリのインターフェースやコンテンツをバックグラウンドで更新するために使用されます。これらの通知では、キーと値のペアを使用して、これらのバックグラウンド アプリ アクションをトリガーします。サイレントプッシュ通知は、 [アンインストールの追跡][4]にも役立ちます。

マーケターは、サイレントプッシュ通知がアプリのユーザーに送信する前に、予期される動作をトリガーすることをテストする必要があります。[iOS][2] または [Android][13] のサイレントプッシュ通知を作成したら、[外部ユーザー ID][14] または[メールアドレス][15]でフィルタリングして、テストユーザーのみをターゲットにします。

キャンペーンの開始時に、テストデバイスで目に見えるプッシュ通知を受け取っていないことを確認する必要があります。

{% alert note %}
iOSオペレーティングシステムは、一部の機能(アンインストールトラッキング、ジオフェンス、プッシュストーリー)の [通知をゲートする]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/#ios-silent-notifications-limitations) 場合があります。これらの機能で問題が発生している場合は、iOSのサイレント通知ゲートが原因である可能性があることに注意してください。
{% endalert %}

## アプリ内メッセージ数

アプリ内メッセージにキーと値のペアを追加するには、メッセージ作成ツールで「 **設定** 」タブを選択し、「 **新しいペアを追加**」をクリックして、キーと値のペアを指定します。

![][21]

#### APIトリガーキャンペーン

Braze では、カスタム定義の文字列のキーと値のペア ( ) `extras`を送信できます。APIトリガーキャンペーンおよびスケジュールされたAPIトリガーキャンペーンのエクストラにアクセスするには、ダッシュボードでキーを「example\_key」、値を {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %}「」に設定します。これにより、開発者コンソールの出力 `"extras": { "test": { "foo": 1, "bar": 1 }`は になります。

## メール

SparkPost と SendGrid はどちらも、メール内のキーと値のペアをサポートしています。SendGrid を使用する場合、キーと値のペアは [一意の引数][11]として送信されます。SendGrid では、最大 10,000 バイトのデータまで、キーと値のペアを無制限にアタッチできます。これらのキーと値のペアは、SendGrid [Event Webhook][12] からの投稿で確認できます。

{% alert note %}
バウンスされたメールは、キーと値のペアを SparkPost または SendGrid に配信しません。
{% endalert %}

![Brazeのメールメッセージ作成ツールの送信情報タブ][22]

## コンテンツカード

コンテンツカードにキーと値のペアを追加するには、Brazeメッセージコンポーザーの「 **設定** 」タブに移動し、「 **新しいペアを追加**」をクリックします。

![コンテンツカードにキーと値のペアを追加する][24]{: style="max-width:70%;"}


[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/customization/advanced_settings/#extracting-data-from-push-key-value-pairs
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/
[4]: {{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#notification-priority
[9]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/advanced_settings/#delivery-options
[10]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/customization/advanced_settings/#sounds
[11]: https://docs.sendgrid.com/for-developers/sending-email/unique-arguments
[12]: https://sendgrid.com/docs/for-developers/tracking-events/event/
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications/
[14]: {{site.baseurl}}/developer_guide/rest_api/messaging/#external-user-id
[15]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
[16]: {% image_buster /assets/img_archive/keyvalue_automatickeys.png %}
[17]: {% image_buster /assets/img_archive/keyvalue_enterpairs.png %}
[18]: {% image_buster /assets/img_archive/keyvalue_androidkeys.png %}
[19]: {% image_buster /assets/img_archive/keyvalue_android.png %}
[20]: {% image_buster /assets/img_archive/keyvalue_web.png %}
[21]: {% image_buster /assets/img_archive/keyvalue_iam.png %}
[22]: {% image_buster /assets/img_archive/keyvalue_email.png %}
[23]: {% image_buster /assets/img_archive/keyvalue_newsfeed.png %}
[24]: {% image_buster /assets/img_archive/kvp_content_cards.png %}
