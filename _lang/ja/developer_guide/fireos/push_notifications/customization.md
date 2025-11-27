{% multi_lang_include developer_guide/prerequisites/android.md %} [プッシュ通知の設定も]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)必要だ。

## 設定

Brazeダッシュボードから送信されるFireOSプッシュ通知には、多くの詳細設定が用意されている。この記事では、これらの機能とそれらを効果的に使用する方法について説明します。

![]({% image_buster /assets/img_archive/android_advanced_settings.png %})

### 有効時間 (TTL) {#ttl}

**有効期間** (TTL) フィールドを使用すると、プッシュメッセージングサービスでメッセージを保存する期間をカスタム設定できます。有効期間のデフォルト値は、FCM の場合は 4 週間、ADM の場合は 31 日です。

### 要約テキスト {#summary-text}

要約テキストを使用すると、拡張通知ビューに追加のテキストを設定できます。画像付きの通知のキャプションとしても機能します。

![タイトルが「This is the title for the notification.」、要約テキストが「This is the summary text for the notification.」の Android メッセージ。]({% image_buster /assets/img/android/push/collapsed-android-notification.png %})({: style="max-width:65%;"})

要約テキストは、展開されたビューのメッセージ本文の下に表示されます。 

![タイトルが「This is the title for the notification.」、要約テキストが「This is the summary text for the notification.」の Android メッセージ。]({% image_buster /assets/img/android/push/expanded-android-notification.png %})({: style="max-width:65%;"})

画像を含むプッシュ通知の場合、折りたたまれたビューにはメッセージテキストが表示され、通知が展開されると、要約テキストが画像のキャプションとして表示されます。 

### カスタム URI {#custom-uri}

**カスタム URI** 機能を使用すると、通知がクリックされたときの誘導先 Web URL または Android リソースを指定できます。カスタム URI が指定されていない場合、通知をクリックするとユーザーはアプリに誘導されます。カスタム URI を使用してアプリ内でディープリンクし、アプリ外部のリソースにユーザーを誘導することができます。この設定は、[メッセージングAPI]({{site.baseurl}}/api/endpoints/messaging)またはダッシュボードのプッシュ作成画面の「**詳細設定**」から行うことができる：

![Braze プッシュコンポーザーのディープリンクの高度な設定。]({% image_buster /assets/img_archive/deep_link.png %})

### 通知の表示優先度

{% alert important %}
通知の表示優先度設定は、Android O 以降を実行しているデバイスでは使用されなくなりました。新しいデバイスの場合は、[通知チャネル設定](https://developer.android.com/training/notify-user/channels#importance)を使用して優先度を設定します。
{% endalert %}

プッシュ通知の優先度レベルは、通知トレイ内で他の通知と比較して通知がどのように表示されるかに影響します。また、通常のメッセージや優先度の低いメッセージは、バッテリー寿命を延ばすために遅延がわずかに長くなったり、バッチ処理で送信されたりするのに対し、優先度の高いメッセージは常に即座に送信されるため、配信の速度と方法にも影響する可能性があります。

Android O では、通知の優先度が通知チャネルのプロパティになりました。開発者と協力して設定中にチャネルの優先度を定義し、ダッシュボードを使用して通知音を送信するときに適切なチャネルを選択する必要があります。AndroidのバージョンがOより前の端末では、ダッシュボードとメッセージングAPIを使ってFireOS通知の優先度を指定することができる。 

特定の優先度でユーザーベース全体にメッセージを送信するには、[通知チャネル設定](https://developer.android.com/training/notify-user/channels#importance) (ターゲットO+ デバイスへ) で間接的に優先度を指定し、ダッシュボード(ターゲット<O デバイスへ) から個々の優先度を送信することをお勧めします。

Fire OSのプッシュ通知で設定できる優先度は以下の通りだ：

| 優先順位 | 説明／使用目的 | `priority` 値 (API メッセージ用) |
|----------|--------------------------|-------------------------------------|
| マックス      | 緊急または一刻を争うメッセージ | `2` |
| 高     | 友人からの新着メッセージなど、重要なコミュニケーション | `1` |
| デフォルト  | ほとんどの通知 - メッセージが他の優先度タイプのいずれにも明示的に該当しない場合に使用します | `0` |
| 低      | ユーザーに知ってもらいたいが、すぐに行動を起こす必要のない情報 | `-1` |
| 最小      | コンテキストまたは背景情報 | `-2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

詳細については、Googleの[Android通知](http://developer.android.com/design/patterns/notifications.html)ドキュメントを参照のこと。

### サウンド {#sounds}

Android O では、通知音は通知チャネルのプロパティになりました。開発者と協力して設定時にチャネルのサウンドを定義し、通知を送信するときにダッシュボードを使用して適切なチャネルを選択する必要があります。

Android O より前のバージョンを実行しているデバイスの場合、Braze を使用すると、ダッシュボードコンポーザーを通じて個々のプッシュメッセージのサウンドを設定できます。これを行うには、デバイスのローカルサウンドリソースを指定します (例: `android.resource://com.mycompany.myapp/raw/mysound`)。このフィールドに「default」を指定すると、デフォルトの通知音がデバイスで再生されます。これは、[メッセージングAPI]({{site.baseurl}}/api/endpoints/messaging)またはダッシュボードのプッシュ作成画面の**「設定**」から指定できる。

![Braze プッシュコンポーザーのサウンドの高度な設定。]({% image_buster /assets/img_archive/sound_android.png %})

完全なサウンドリソース URI (例: `android.resource://com.mycompany.myapp/raw/mysound`) をダッシュ​​ボードプロンプトに入力します。

特定のサウンドでフルユーザーベースにメッセージを送るには、[通知チャネル設定](https://developer.android.com/training/notify-user/channels)(ターゲットO+ デバイスへ)でサウンドを間接的に指定し、ダッシュボードから個別のサウンド(ターゲット<O デバイスへ)を送ることをお勧めします。
