---
nav_title: 高度な設定
article_title: FireOS の高度な設定
platform: FireOS
page_order: 4
page_type: reference
description: "この記事では、Braze ダッシュボードを通じて送信される FireOS プッシュ通知で使用できる高度な設定について説明します。"
channel: push

---

# 高度な設定

> Braze ダッシュボードを通じて送信される Android および FireOS プッシュ通知には、多くの高度な設定を利用できます。この記事では、これらの機能とそれらを効果的に使用する方法について説明します。

![][1]

## 有効時間 (TTL) {#ttl}

**有効期間** (TTL) フィールドを使用すると、プッシュメッセージングサービスでメッセージを保存する期間をカスタム設定できます。有効期間のデフォルト値は、FCM の場合は 4 週間、ADM の場合は 31 日です。

## 要約テキスト {#summary-text}

要約テキストを使用すると、拡張通知ビューに追加のテキストを設定できます。画像付きの通知のキャプションとしても機能します。

![タイトル「Greetings from Appboy！」、メッセージ「This is the message body！絵文字を追加することもできる。" と要約文 "これは要約文である。" を追加する。][9]

要約テキストは、展開されたビューのメッセージ本文の下に表示されます。

画像を含むプッシュ通知の場合、折りたたまれたビューにはメッセージテキストが表示され、通知が展開されると、要約テキストが画像のキャプションとして表示されます。 

![タイトル "Appboy!"、メッセージ "This is the message body..."、要約テキスト "and this is the Summary Text. "のAndroidメッセージ。][15]

## カスタム URI {#custom-uri}

**カスタム URI** 機能を使用すると、通知がクリックされたときの誘導先 Web URL または Android リソースを指定できます。カスタム URI が指定されていない場合、通知をクリックするとユーザーはアプリに誘導されます。カスタム URI を使用してアプリ内でディープリンクし、アプリ外部のリソースにユーザーを誘導することができます。これは、\[Messaging API][13] ] またはダッシュボードのプッシュコンポーザーの**\[Advanced Settings]**で指定できる：

![Brazeプッシュコンポーザーのディープリンク詳細設定。][12]

## 通知の表示優先度

{% alert important %}
通知の表示優先度設定は、Android O 以降を実行しているデバイスでは使用されなくなりました。新しいデバイスの場合は、[通知チャネル設定](https://developer.android.com/training/notify-user/channels#importance)を使用して優先度を設定します。
{% endalert %}

プッシュ通知の優先度レベルは、通知トレイ内で他の通知と比較して通知がどのように表示されるかに影響します。また、通常のメッセージや優先度の低いメッセージは、バッテリー寿命を延ばすために遅延がわずかに長くなったり、バッチ処理で送信されたりするのに対し、優先度の高いメッセージは常に即座に送信されるため、配信の速度と方法にも影響する可能性があります。

Android O では、通知の優先度が通知チャネルのプロパティになりました。開発者と協力して設定中にチャネルの優先度を定義し、ダッシュボードを使用して通知音を送信するときに適切なチャネルを選択する必要があります。Android O より前のバージョンを実行しているデバイスの場合は、Braze ダッシュボードとメッセージング API を使用して、Android および FireOS 通知の優先度レベルを指定できます。 

特定の優先順位で全ユーザーベースにメッセージを送るには、\[通知チャネル設定]][17] (O+デバイスをターゲットにする)を通じて間接的に優先順位を指定*し、*ダッシュボードから個々の優先順位を送信する(<Oデバイスをターゲットにする)ことを推奨する。

Android または Fire OS プッシュ通知で設定できる優先度レベルは次のとおりです。

| 優先順位 | 説明／使用目的 | `priority` 値（APIメッセージ用） |
|----------|--------------------------|-------------------------------------|
| マックス      | 緊急または一刻を争うメッセージ | `2` |
| 高     | 友人からの新着メッセージなど、重要なコミュニケーション | `1` |
| デフォルト  | ほとんどの通知 - メッセージが他の優先順位タイプに明確に該当しない場合に使用する。 | `0` |
| 低      | ユーザーに知ってもらいたいが、すぐに行動を起こす必要のない情報 | `-1` |
| 最小      | 文脈や背景に関する情報。 | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

詳細はGoogleの\[Android notification][2] documentation]を参照のこと。

## サウンド {#sounds}

Android O では、通知音は通知チャネルのプロパティになりました。開発者と協力して設定時にチャネルのサウンドを定義し、通知を送信するときにダッシュボードを使用して適切なチャネルを選択する必要があります。

Android O より前のバージョンを実行しているデバイスの場合、Braze を使用すると、ダッシュボードコンポーザーを通じて個々のプッシュメッセージのサウンドを設定できます。これを行うには、デバイスのローカルサウンドリソースを指定します (例: `android.resource://com.mycompany.myapp/raw/mysound`)。このフィールドに「default」を指定すると、デフォルトの通知音がデバイスで再生されます。これは、\[Messaging API][13] ]またはプッシュ・コンポーザーの**\[Settings]**にあるダッシュボードから指定できる。

![Brazeのプッシュコンポーザーでサウンドの詳細設定を行う。][11]

完全なサウンドリソース URI (例: `android.resource://com.mycompany.myapp/raw/mysound`) をダッシュ​​ボードプロンプトに入力します。

特定のサウンドで全ユーザーにメッセージを送るには、\[通知チャンネル設定][16] （O+デバイスをターゲットにする）]から間接的にサウンドを指定*し、*ダッシュボードから個々のサウンドを送信する（<Oデバイスをターゲットにする）ことを推奨する。

[1]: {% image_buster /assets/img_archive/android_advanced_settings.png %}
[2]: http://developer.android.com/design/patterns/notifications.html
[9]: {% image_buster /assets/img_archive/summary_text.png %}
[11]: {% image_buster /assets/img_archive/sound_android.png %}
[12]: {% image_buster /assets/img_archive/deep_link.png %}
[13]: {{site.baseurl}}/api/endpoints/messaging
[15]: {% image_buster /assets/img_archive/messagesummary.gif %}
[17]: https://developer.android.com/training/notify-user/channels#importance
[16]: https://developer.android.com/training/notify-user/channels
