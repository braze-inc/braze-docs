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

> Brazeを使用すると、キーと値のペアを介してユーザーデバイスに余分なデータペイロードを送信することができる。この機能は、プッシュ、アプリ内、Eメール、コンテンツカードのメッセージング・チャンネルで利用できる。 

余分なデータペイロードは、アラートの優先順位付け、ローカライズ、サウンドなどのプッシュ通知のプロパティをカスタマイズするだけでなく、内部メトリクスやアプリのコンテンツを更新するのに役立つ。

## プッシュ通知

キー・バリュー・ペアは、Android、iOS、ウェブプッシュ通知にも追加できる。メッセージ・コンポーザーで、**Settings**タブを選択し、**Add New Pairを**クリックし、キーと値のペアを指定する。

### iOS

アップル・プッシュ・ノーティフィケーション・サービス（APNs）は、アラートのプリファレンスを設定し、キーと値のペアを使用してカスタムデータを送信することをサポートしている。APNsは、Appleが予約した```aps``` ライブラリを使用する。このライブラリには、アラートのプロパティを管理する所定のキーと値が含まれている。

##### APSライブラリー

| キー  | バリュー・タイプ  | 説明 |
|-------------------|-----------------------------|----------------------------------|
| アラート             | 文字列または辞書オブジェクト | 文字列入力の場合、その文字列をメッセージとするアラートを表示し、「閉じる」ボタンと「表示」ボタンを表示する。 |
| バッジ             | 番号                      | アプリアイコンのバッジとして表示される番号を管理する。                                                                                                                              |
| サウンド             | ストリング                      | アラートとして再生するサウンドファイルの名前。アプリのバンドルまたは```Library/Sounds``` フォルダになければならない。                                                                                    |
| コンテンツ利用可能 | 番号                      | 1の入力値は、起動時またはセッション再開時に、新しい情報が利用可能であることをアプリに知らせる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}


##### アラート・プロパティ・ライブラリ

| キー            | バリュー・タイプ               | 説明                                                                                                                             |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| タイトル         | ストリング                   | Apple Watchが通知の一部として短く表示する文字列。                                                                    |
| ボディ         | ストリング                   | プッシュ通知の内容                                                                                                                  |
| タイトル・ロック・キー  | 文字列またはNULL           | ```Localizable.strings``` ファイルから、現在のローカライゼーションのタイトル文字列を設定するキー。                                          |
| タイトル位置引数 | 文字列の配列またはNULL | title-loc-keyのタイトル地域化書式指定子の代わりに使用できる文字列値。                                           |
| アクション・ロック・キー | 文字列またはNULLの配列  | 存在する場合、指定された文字列は閉じるボタンと表示ボタンのローカライズを設定する                                                         |
| ロックキー        | 文字列またはNULL           | ```Localizable.strings``` ファイルから、現在のローカライゼーションの通知メッセージを設定するキー。                                  |
| loc-args       | 文字列の配列         | loc-keyの地域化書式指定子の代わりに使用できる文字列。                                                       |
| 打ち上げ画像   | ストリングス                  | ユーザーがアクションボタンをタップしたり、アクションスライドを動かしたときに、起動画像として使用したいアプリバンドル内の画像ファイル名。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Brazeのメッセージコンポーザーは、**alertと** **そのプロパティ**、**content-available**、**sound**、**categoryという**キーの作成を自動的に処理する。 

これらの値は、プッシュ・メッセージを作成する際に**Settings**タブで入力することができる。**アラート・オプションを**選択し、新しいキー・バリュー項目に自動的に入力されるキーのアラート・ディクショナリー・キーを選択する。

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

##### カスタム・キーと値のペア

```aps``` ライブラリのペイロード値に加えて、カスタムのキーと値のペアをユーザーのデバイスに送信することができる。これらのペアの値は、ディクショナリ（オブジェクト）、配列、文字列、数値、およびブール値というプリミティブな型に制限されている。

![][17]

カスタムキーと値のペアの使用例としては、内部的なメトリクスの保持や、ユーザーインターフェイスのコンテキストの設定が挙げられるが、これらに限定されるものではない。Brazeでは、追加のキーと値のペアをプッシュ通知と一緒に送信することができ、[extrasキー][1]内のアプリケーションから、どのようにでも使用することができる。別のキーを使いたい場合は、アプリがこのカスタムキーを扱えることを確認すること。

{% alert warning %}
アプリケーションでabというトップレベルのキーや辞書を扱うのは避けるべきである。
{% endalert %}

アップル社は顧客に対し、顧客情報や機密データをカスタムペイロードデータに含めないよう助言している。さらにアップルは、アラートメッセージに関連するいかなるアクションも、デバイス上のデータを削除しないことを推奨している。

{% alert warning %}
HTTP/2プロバイダーAPIを使用している場合、APNに送信する個々のペイロードは4096バイトのサイズを超えることはできない。レガシー・バイナリー・インターフェイスは、まもなく廃止される予定だが、ペイロードサイズは2048バイトしかサポートしていない。
{% endalert %}

###### API トリガーキャンペーン

Brazeでは、`extras` として知られるカスタム定義の文字列キーと値のペアを送信することができる。API トリガーおよびスケジュールされた API トリガー キャンペーンでエクストラにアクセスするには、ダッシュボードでキーを "example_key" として設定し、値を {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %} として設定します。この結果、開発者コンソールに次のような出力が出る。 `"extras": { "test": { "foo": 1, "bar": 1 }`

### Android

Brazeでは、キーと値のペアを使用して、プッシュ通知に追加のデータペイロードを送信することができる。

##### データペイロード

iOSのプッシュと同様に、カスタムのキーと値のペアをユーザーのデバイスに送ることができる。

カスタムKey-Valueペアの使用例としては、内部メトリクスの保持やユーザーインターフェイスのコンテキストの設定などがあるが、どのような目的にも使用することができる。

{% alert important %}
あなたのアプリのバックエンドは、データペイロードが正しく機能するために、カスタムキーと値のペアを処理できなければならない。
{% endalert %}

###### API トリガーキャンペーン

Brazeでは、`extras` として知られるカスタム定義の文字列キーと値のペアを送信することができる。API トリガーおよびスケジュールされた API トリガー キャンペーンでエクストラにアクセスするには、ダッシュボードでキーを "example_key"、値を {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %} に設定します。この結果、開発者コンソールには`"extras": { "test": { "foo": 1, "bar": 1 }` が出力される。

##### FCMメッセージング・オプション

アンドロイドのプッシュ通知は、FCMメッセージオプションでさらにカスタマイズできる。これには、[通知の優先順位][8]、[音][10]、遅延、寿命、折りたたみ可能性などが含まれる。これらの値は、プッシュ・メッセージを作成する際に**Settings**タブで指定することができる。Brazeメッセージコンポーザーでこれらのオプションを設定する方法については、[プッシュ通知の詳細設定を][7]参照のこと。

![][18]

### サイレントプッシュ通知

サイレントプッシュ通知は、アラートメッセージやサウンドを含まないプッシュ通知で、アプリのインターフェースやコンテンツをバックグラウンドで更新するために使用される。これらの通知は、キーと値のペアを使用して、バックグラウンド・アプリのアクションをトリガーする。サイレント・プッシュ通知も[アンインストールのトラッキングに役立って][4]いる。

マーケティング担当者は、アプリのユーザーにプッシュ通知を送る前に、サイレント・プッシュ通知が期待される行動を引き起こすかどうかをテストすべきである。[iOS][2]または[Androidの][13]サイレント・プッシュ通知を作成したら、[外部ユーザーID][14]または[メールアドレスで][15]フィルタリングして、テスト・ユーザーのみをターゲットにすることを確認する。

キャンペーンを開始したら、テスト・デバイスにプッシュ通知が表示されていないことを確認する。

{% alert note %}
iOSオペレーティングシステムは、一部の機能（アンインストールトラッキング、ジオフェンス、プッシュストーリー）の[通知をゲートする]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/#ios-silent-notifications-limitations)ことがある。これらの機能で問題が発生している場合は、iOS のサイレント通知ゲートが原因である可能性があることに注意してください。
{% endalert %}

## アプリ内メッセージ

アプリ内メッセージにKey-Valueペアを追加するには、メッセージ・コンポーザーの**Settings**タブを選択し、**Add New Pairを**クリックし、Key-Valueペアを指定する。

![][21]

#### API トリガーキャンペーン

Brazeでは、`extras` として知られるカスタム定義の文字列キーと値のペアを送信することができる。API トリガーおよびスケジュールされた API トリガー キャンペーンでエクストラにアクセスするには、ダッシュボードでキーを "example_key" として設定し、値を {% raw %}`"$json:{"foo": 1, "bar": 1}"`{% endraw %} として設定します。この結果、開発者コンソールには`"extras": { "test": { "foo": 1, "bar": 1 }` が出力される。

## メール

SparkPostとSendGridの両方が、電子メールのキーと値のペアをサポートしている。SendGridを使用すると、キーと値のペアが[ユニークな引数として][11]送信される。SendGridでは、10,000バイトのデータまで、キーと値のペアを無制限に添付することができる。これらのキーと値のペアは、SendGrid[Event Webhookからの][12]投稿で見ることができる。

{% alert note %}
バウンスされたメールは、SparkPostやSendGridにkey-valueペアを配信しない。
{% endalert %}

![Brazeのメールメッセージコンポーザーの「送信情報」タブ。][22]

## コンテンツカードによって促進された

コンテンツカードにキーと値のペアを追加するには、Brazeメッセージコンポーザーの**Settings**タブに行き、**Add New Pairを**クリックする。

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
