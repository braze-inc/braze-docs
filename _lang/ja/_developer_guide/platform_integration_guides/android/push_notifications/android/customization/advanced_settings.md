---
nav_title: 高度な設定
article_title: Android の高度なプッシュ通知設定
platform: Android
page_order: 40
description: "このリファレンス記事では、TTL、通知 ID、通知の優先度などの Android プッシュ通知の詳細設定について説明します。"
channel:
  - push

---

# 高度な設定

> Braze ダッシュボードを通じて送信される Android および FireOS プッシュ通知には、多くの高度な設定を利用できます。この記事では、これらの機能とそれらを効果的に使用する方法について説明します。

![]({% image_buster /assets/img_archive/android_advanced_settings.png %})

## 通知 ID {#notification-id}

**通知 ID** は、選択したメッセージカテゴリの一意の識別子です。その ID からの最新のメッセージのみを尊重するようメッセージングサービスに通知する役割を果たします。通知 ID を設定すると、古くて無関係なメッセージのスタックではなく、最新で関連性の高いメッセージだけを送信できます。

## Firebase メッセージング配信の優先度 {#fcm-priority}

[Firebase Messaging Delivery Priority](https://firebase.google.com/docs/cloud-messaging/concept-options#setting-the-priority-of-a-message) フィールドでは、「通常」または「高」のどちらの優先度でプッシュを Firebase Cloud Messaging に送信するかを制御できます。

## 有効時間 (TTL) {#ttl}

**有効期間** (TTL) フィールドを使用すると、プッシュメッセージングサービスでメッセージを保存する期間をカスタム設定できます。有効期間のデフォルト値は、FCM の場合は 4 週間、ADM の場合は 31 日です。

## 要約テキスト {#summary-text}

要約テキストを使用すると、拡張通知ビューに追加のテキストを設定できます。画像付きの通知のキャプションとしても機能します。

![Androidのメッセージで、タイトルが"Greetings from Appboy!"、メッセージ"これはメッセージ本文です!絵文字を追加することもできます。" と要約テキスト "これが要約テキストです。"]({% image_buster /assets/img_archive/summary_text.png %})

要約テキストは、展開されたビューのメッセージ本文の下に表示されます。

画像を含むプッシュ通知の場合、折りたたまれたビューにはメッセージテキストが表示され、通知が展開されると、要約テキストが画像のキャプションとして表示されます。 

![タイトルが「Appboy!」、メッセージが「これはメッセージ本文です。」、要約テキストが「これは要約テキストです。」である Android メッセージ]({% image_buster /assets/img_archive/messagesummary.gif %})

## カスタム URI {#custom-uri}

**カスタム URI** 機能を使用すると、通知がクリックされたときの誘導先 Web URL または Android リソースを指定できます。カスタム URI が指定されていない場合、通知をクリックするとユーザーはアプリに誘導されます。カスタム URI を使用してアプリ内でディープリンクし、アプリ外部のリソースにユーザーを誘導することができます。この設定は、[メッセージングAPI]({{site.baseurl}}/api/endpoints/messaging/)またはダッシュボードのプッシュ作成画面の「**詳細設定**」から行うことができる：

![Braze プッシュコンポーザーのディープリンクの高度な設定。]({% image_buster /assets/img_archive/deep_link.png %})

## 通知の表示優先度 {#notification-priority}

{% alert important %}
通知の表示優先度設定は、Android O 以降を実行しているデバイスでは使用されなくなりました。新しいデバイスの場合は、[通知チャネル設定](https://developer.android.com/training/notify-user/channels#importance)を使用して優先度を設定します。
{% endalert %}

プッシュ通知の優先度レベルは、通知トレイ内で他の通知と比較して通知がどのように表示されるかに影響します。また、通常のメッセージや優先度の低いメッセージは、バッテリー寿命を延ばすために遅延がわずかに長くなったり、バッチ処理で送信されたりするのに対し、優先度の高いメッセージは常に即座に送信されるため、配信の速度と方法にも影響する可能性があります。

Android O では、通知の優先度が通知チャネルのプロパティになりました。開発者と協力して設定中にチャネルの優先度を定義し、ダッシュボードを使用して通知音を送信するときに適切なチャネルを選択する必要があります。Android O より前のバージョンを実行しているデバイスの場合は、Braze ダッシュボードとメッセージング API を使用して、Android および FireOS 通知の優先度レベルを指定できます。 

特定の優先順位で全ユーザーベースにメッセージングするには、[通知チャネル構成で](https://developer.android.com/training/notify-user/channels#importance)間接的に優先順位を指定し（O+デバイスをターゲットにする）*、*ダッシュボードから個々の優先順位を送信する（<Oデバイスをターゲットにする）ことを推奨する。

Android または Fire OS プッシュ通知で設定できる優先度レベルは次のとおりです。

| 優先順位 | 説明／使用目的 | `priority` 値 (API メッセージ用) |
|----------|--------------------------|-------------------------------------|
| マックス      | 緊急または一刻を争うメッセージ | `2` |
| 高     | 友人からの新着メッセージなど、重要なコミュニケーション | `1` |
| デフォルト  | ほとんどの通知 - メッセージが他の優先度タイプのいずれにも明示的に該当しない場合に使用します | `0` |
| 低      | ユーザーに知ってもらいたいが、すぐに行動を起こす必要のない情報 | `-1` |
| 最小      | コンテキストまたは背景情報 | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

詳細はGoogleの[Android通知](http://developer.android.com/design/patterns/notifications.html)ドキュメントを参照のこと。

## サウンド {#sounds}

Android O では、通知音は通知チャネルのプロパティになりました。開発者と協力して設定時にチャネルのサウンドを定義し、通知を送信するときにダッシュボードを使用して適切なチャネルを選択する必要があります。

Android O より前のバージョンを実行しているデバイスの場合、Braze を使用すると、ダッシュボードコンポーザーを通じて個々のプッシュメッセージのサウンドを設定できます。これを行うには、デバイスのローカルサウンドリソースを指定します (例: `android.resource://com.mycompany.myapp/raw/mysound`)。このフィールドに「default」を指定すると、デフォルトの通知音がデバイスで再生されます。これは、[メッセージングAPI]({{site.baseurl}}/api/endpoints/messaging/)またはダッシュボードのプッシュ作成画面の「**詳細設定**」で指定できる。

![Braze プッシュコンポーザーのサウンドの高度な設定。]({% image_buster /assets/img_archive/sound_android.png %})

完全なサウンドリソース URI (例: `android.resource://com.mycompany.myapp/raw/mysound`) をダッシュ​​ボードプロンプトに入力します。

特定のサウンドを指定したメッセージを全ユーザーベースに送信するには、[[通知チャネル設定](https://developer.android.com/training/notify-user/channels)] (O 以降のデバイスを対象とする) を通じて間接的にサウンドを指定し、*かつ*、ダッシュボードから個別のサウンドを送信する (O より前のデバイスを対象とする) ことをお勧めします。

