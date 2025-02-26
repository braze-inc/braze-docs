---
nav_title: キーと値のペア
article_title: キーと値のペア
page_order: 4
description: "この参考記事では、キー・バリュー・ペアと、それを使ってユーザー・デバイスに特別なデータ・ペイロードを送信する方法について説明する。"
channel:
  - push
  - in-app messages
  - content cards

---

# キーと値のペア

> Brazeを使用すると、キーと値のペアを介してユーザーデバイスに余分なデータペイロードを送信することができる。この機能は、プッシュ、アプリ内、メール、およびコンテンツカードのメッセージングチャネルで使用できます。 

キーと値のペアを使って、メッセージに構造化メタデータを追加する。これらの追加のデータペイロードは、メッセージのレンダリング方法や処理方法に影響を与えることができる追加の文脈に応じた情報で、メッセージを充実させることができます。

キーと値のペアはメタデータであるため、このデータは必ずしも受信者に見えるわけではないが、接続されたシステムやプロセスによって、メッセージ・ハンドリングをカスタマイズするために使用することができる。 

各ペアは以下のように構成されている：

- **キー:**識別子 (例:`utm_source`)
- **値:**関連データ (例:`newsletter`)

## ユースケース

キーと値のペアでメタデータを追加するユースケースをいくつか紹介しよう：

1. **トラッキングパラメータ：**分析のためにUTMパラメータを付加する
   - キー: `utm_campaign`
   - 値: `spring_sale`
2. **カスタムタグ:**内部ルーティングや分類のためにタグを追加する。
   - キー: `priority`
   - 値: `high`
3. **行動トリガー:**アプリ内行動のトリガーやカスタマイズに使用されるメタデータ
   - キー: `deep_link`
   - 値: `app://promo-page`

## プッシュ通知

キーと値のペアは、Android、iOS、および Web のプッシュ通知に追加できます。キーと値のペアを使用して、内部メトリクスやアプリのコンテンツを更新したり、アラートの優先順位、ローカライゼーション、サウンドなどのプッシュ通知のプロパティをカスタマイズしたりすることができる。

メッセージ作成画面で [**設定**] タブを選択し、[**新しいペアを追加**] をクリックして、キーと値のペアを指定します。

### iOS

Apple のプッシュ通知サービス (APN) は、アラートの設定、およびキーと値のペアを使用するカスタムデータの送信をサポートしています。APN は、Apple が予約している ```aps``` ライブラリーを活用します。このライブラリーには、アラートのプロパティを管理する、あらかじめ決められたキーと値があります。

##### APSライブラリー

| キー  | 値のタイプ  | 値の説明 |
|-------------------|-----------------------------|----------------------------------|
| アラート             | 文字列または辞書オブジェクト | 文字列入力の場合、その文字列をメッセージとするアラートを表示し、[閉じる] ボタンと [表示] ボタンを表示すします。文字列以外の入力の場合は、入力の子のプロパティに応じてアラートまたはバナーを表示します。 |
| バッジ             | 番号                      | アプリアイコンのバッジとして表示される番号を管理する。                                                                                                                              |
| サウンド             | ストリング                      | アラートとして再生するサウンドファイルの名前。アプリのバンドルまたは ```Library/Sounds``` フォルダーになければなりません。                                                                                    |
| 利用可能なコンテンツ | 番号                      | 入力値 1 は、起動時またはセッション再開時に、新しい情報があることをアプリに通知します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


##### アラート・プロパティ・ライブラリ

| キー            | 値のタイプ               | 値の説明                                                                                                                             |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| タイトル         | ストリング                   | Apple Watchが通知の一部として短く表示する文字列。                                                                    |
| body         | ストリング                   | プッシュ通知の内容                                                                                                                  |
| title-loc-key  | 文字列またはNULL           | ```Localizable.strings``` ファイルから、現在のローカライゼーションのタイトル文字列を設定するキー。                                          |
| title-loc-args | 文字列の配列またはNULL | title-loc-keyのタイトル地域化書式指定子の代わりに使用できる文字列値。                                           |
| action-loc-key | 文字列またはNULLの配列  | 存在する場合、指定された文字列は閉じるボタンと表示ボタンのローカライズを設定する                                                         |
| loc-key        | 文字列またはNULL           | ```Localizable.strings``` ファイルから、現在のローカライゼーションの通知メッセージを設定するキー。                                  |
| loc-args       | 文字列の配列         | loc-keyの地域化書式指定子の代わりに使用できる文字列。                                                       |
| launch-image   | ストリングス                  | ユーザーがアクションボタンをタップしたり、アクションスライドを動かしたときに、起動画像として使用したいアプリバンドル内の画像ファイル名。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Braze のメッセージ作成画面は、**alert** と**そのプロパティ**、**content-available**、**sound**、**category** の各キーの作成を自動的に処理します。 

これらの値は、プッシュ・メッセージを作成する際に**Settings**タブで入力することができる。[**アラートオプション**] を選択し、新しいキーと値のエントリに自動的に入力される、キーのアラートディクショナリーキーを選択します。

![][16]
{% raw %}
BrazeがAPNにプッシュ通知を送信する際、ペイロードはJSONとしてフォーマットされる。

**シンプルなペイロード**

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

##### カスタムキーと値のペア

```aps``` ライブラリーのペイロード値のほかに、カスタムのキーと値のペアをユーザーのデバイスに送信できます。これらのペアの値は、ディクショナリ（オブジェクト）、配列、文字列、数値、およびブール値というプリミティブな型に制限されている。

![][17]

カスタムキーと値のペアの使用例としては、内部的なメトリクスの保持や、ユーザーインターフェイスのコンテキストの設定が挙げられるが、これらに限定されるものではない。Braze では、アプリケーション経由で使用するプッシュ通知とともに、[extras キー][1]内の追加のキーと値のペアを送信できます。別のキーを使いたい場合は、アプリがこのカスタムキーを扱えることを確認すること。

{% alert warning %}
アプリケーションでabというトップレベルのキーや辞書を扱うのは避けるべきである。
{% endalert %}

アップル社は顧客に対し、顧客情報や機密データをカスタムペイロードデータに含めないよう助言している。さらに Apple は、アラートメッセージに関連するいかなるアクションも、デバイス上のデータを削除しないことを推奨しています。

{% alert warning %}
HTTP/2プロバイダーAPIを使用している場合、APNに送信する個々のペイロードは4096バイトのサイズを超えることはできない。もうすぐ廃止予定のレガシーバイナリインターフェイスは、2048 バイトのペイロードサイズのみをサポートしています。
{% endalert %}

###### API トリガーキャンペーン

Braze では、`extras` として知られるカスタム定義の文字列キーと値のペアを送信できます。API トリガーおよびスケジュールされた API トリガー キャンペーンから extras にアクセスするには、ダッシュボードでキーを「example_key」に設定し、値を {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %} に設定します。これにより、開発者コンソールに `"extras": { "test": { "foo": 1, "bar": 1 }` が出力されます。

### Android

Brazeでは、キーと値のペアを使用して、プッシュ通知に追加のデータペイロードを送信することができる。

##### データペイロード

iOSのプッシュと同様に、カスタムのキーと値のペアをユーザーのデバイスに送ることができる。

カスタムKey-Valueペアの使用例としては、内部メトリクスの保持やユーザーインターフェイスのコンテキストの設定などがあるが、どのような目的にも使用することができる。

{% alert important %}
データペイロードが適切に機能するには、アプリのバックエンドがカスタムキーと値のペアを処理できる必要があります。
{% endalert %}

###### API トリガーキャンペーン

Braze では、`extras` として知られるカスタム定義の文字列キーと値のペアを送信できます。API トリガーおよびスケジュールされた API トリガー キャンペーンから extras にアクセスするには、ダッシュボードでキーを「example_key」に設定し、値を {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %} に設定します。これにより、開発者コンソールに `"extras": { "test": { "foo": 1, "bar": 1 }` が出力されます。

##### FCMメッセージング・オプション

アンドロイドのプッシュ通知は、FCMメッセージオプションでさらにカスタマイズできる。これには、[通知の優先順位][8]、[音][10]、遅延、寿命、折りたたみ可能性などが含まれる。これらの値は、プッシュ・メッセージを作成する際に**Settings**タブで指定することができる。Braze メッセージ作成画面でこれらのオプションを設定する方法の詳細については、[プッシュ通知の詳細設定][7]を参照してください。

![][18]

### サイレントプッシュ通知

サイレントプッシュ通知は、アラートメッセージやサウンドを含まないプッシュ通知で、アプリのインターフェースやコンテンツをバックグラウンドで更新するために使用される。これらの通知はキーと値のペアを使用して、バックグラウンドアプリのアクションをトリガーします。サイレント・プッシュ通知も[アンインストールのトラッキングに役立って][4]いる。

マーケティング担当者は、アプリのユーザーにプッシュ通知を送る前に、サイレント・プッシュ通知が期待される行動を引き起こすかどうかをテストすべきである。[iOS][2] または [Android][13] のサイレントプッシュ通知を作成したら、必ず[外部ユーザー ID][14] または[メールアドレス][15]をフィルター処理して、テストユーザーのみをターゲットにしてください。

キャンペーンの開始時に、表示されるプッシュ通知がテストデバイスで受信していないことを確認する必要があります。

{% alert note %}
iOSオペレーティングシステムは、一部の機能（アンインストールトラッキング、ジオフェンス、プッシュストーリー）の[通知をゲートする]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/#ios-silent-notifications-limitations)ことがある。これらの機能で問題が発生している場合は、iOS のサイレント通知ゲートが原因である可能性があることに注意してください。
{% endalert %}

## アプリ内メッセージ

アプリ内メッセージにキーと値のペアを追加するには、メッセージ作成画面の [**設定**] タブを選択し、[**新しいペアを追加**] をクリックしてキーと値のペアを指定します。

![][21]

#### API トリガーキャンペーン

Braze では、`extras` として知られるカスタム定義の文字列キーと値のペアを送信できます。API トリガーおよびスケジュールされた API トリガー キャンペーンから extras にアクセスするには、ダッシュボードでキーを「example_key」に設定し、値を {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %} に設定します。これにより、開発者コンソールに `"extras": { "test": { "foo": 1, "bar": 1 }` が出力されます。

## メール

SparkPostとSendGridの両方が、電子メールのキーと値のペアをサポートしている。SendGrid を使用する場合、キーと値のペアは[一意の引数][11]として送信されます。SendGrid では、データが 10,000 バイトに達するまでキーと値のペアを無制限にアタッチできます。これらのキーと値のペアについては、SendGrid の [Event Webhook][12] の投稿を参照してください。

{% alert note %}
メールがバウンスされた場合、SparkPost または SendGrid にキーと値のペアは配信されません。
{% endalert %}

![Brazeのメールメッセージ作成画面の [送信情報] タブ。][22]

## コンテンツカード

コンテンツカードにキーと値のペアを追加するには、Braze のメッセージ作成画面の [**設定**] タブに移動し、[**新しいペアを追加**] をクリックします。

![コンテンツ・カードにキーと値のペアを追加する][24]{: style="max-width:70%;"}


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
