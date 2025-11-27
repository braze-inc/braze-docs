## Android TVのプッシュ通知について

![]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

Android TV プッシュ統合は、ネイティブ機能ではありませんが、Braze Android SDK と Firebase Cloud Messaging を利用して Android TV のプッシュトークンを登録することで使用可能になります。ただし、通知ペイロードを受信した後にそれを表示する UI を構築する必要があります。

## 前提条件

この機能を使うには、以下を完了する必要がある：

- [Braze Android SDK を統合する]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)
- [Braze Android SDKのプッシュ通知の設定]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android)

## プッシュ通知の設定

Android TVのプッシュ通知を設定する：

1. アプリにカスタムビューを作成し、通知を表示する。
2. カスタム通知ファクトリーを作成するこれにより、デフォルトの SDK 動作がオーバーライドされ、通知を手動で表示できるようになります。`null` を返すことで SDK の処理が妨げられ、通知を表示するためにカスタムコードが必要になります。これらの手順が完了したら、Android TV へのプッシュの送信を開始できます。<br><br>
3. (オプション）クリック分析を効果的にトラッキングするために、クリック分析トラッキングを設定する。これを行うには、Braze プッシュ通知の開封および受信インテントをリッスンする[プッシュコールバック]({{site.baseurl}}/developer_guide/push_notifications/customization#push-callback)を作成します。

{% alert note %}
これらの通知は**持続せず**、デバイスがそれらを表示するときのみユーザーに見える。これは、Android TV の通知センターが過去の通知をサポートしていないためです。
{% endalert %} 

## Android TVのプッシュ通知をテストする

プッシュ実装が成功したかどうかをテストするには、通常 Android デバイスで行うように、Braze ダッシュボードから通知を送信します。

- **アプリケーションが閉じている場合**:プッシュメッセージでは、画面にトースト通知が表示されます。
- **アプリケーションが開いている場合**:独自にホストしている UI でメッセージを表示できます。Android Mobile SDK のアプリ内メッセージの UI スタイルに従うことをお勧めします。

## ベストプラクティス

マーケターにとって、Android TVへのキャンペーンは、Androidモバイルアプリへのプッシュと同じである。これらのデバイスのみをターゲットにするには、セグメンテーションで Android TV アプリを選択することをお勧めします。

FCM によって返される、配信およびクリックされた応答は、モバイル Android デバイスと同じ規則に従います。そのため、エラーがあれば、メッセージアクティビティログに表示されます。
