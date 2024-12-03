---
nav_title: Android TV プッシュ
article_title: Android TV プッシュ
platform: Android
page_order: 8
description: "この記事では、Android TV プッシュを実装してテストする方法を説明します。"
channel:
  - push

---

# Android TV プッシュ
![]({% image_buster /assets/img/Television.png %}){: style="float:right;max-width:25%;margin-left:15px; border: 0"}

> Android TV プッシュ統合は、ネイティブ機能ではありませんが、Braze Android SDK と Firebase Cloud Messaging を利用して Android TV のプッシュトークンを登録することで使用可能になります。ただし、通知ペイロードを受信した後にそれを表示する UI を構築する必要があります。

## 実装

1. **Braze Android SDK を統合する**<br>
まず、[Braze Android SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/?redirected=true) を統合する必要があります (まだ完了していない場合)。<br><br>
2. **プッシュ通知を統合する**<br>
次に、[Android プッシュ通知]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/)を統合する必要があります (まだ完了していない場合)。<br><br>
3. **カスタムトーストビューを作成する**<br>
次に、アプリで通知を表示するためのカスタムビューを作成します。<br><br>
4. **カスタム通知ファクトリーを作成する**<br>
最後に、[カスタム通知ファクトリー]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#custom-displaying-notifications)を作成する必要があります。これにより、デフォルトの SDK 動作がオーバーライドされ、通知を手動で表示できるようになります。`null` を返すことで SDK の処理が妨げられ、通知を表示するためにカスタムコードが必要になります。これらの手順が完了したら、Android TV へのプッシュの送信を開始できます。<br><br>
5. **クリック分析トラッキングを設定する (オプション)**<br>
Braze はメッセージの表示を自動的に処理しないため、クリック分析を効果的に追跡するには、手動で行うことが必要となります。これを行うには、Braze プッシュ通知の開封および受信インテントをリッスンする[プッシュコールバック]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback)を作成します。

{% alert note %}
これらの通知は**永続化されず**、デバイスが通知を表示するときにのみユーザーに表示されます。これは、Android TV の通知センターが過去の通知をサポートしていないためです。
{% endalert %} 

## Android TV でプッシュをテストする方法

プッシュ実装が成功したかどうかをテストするには、通常 Android デバイスで行うように、Braze ダッシュボードから通知を送信します。

- **アプリケーションが閉じている場合**:プッシュメッセージでは、画面にトースト通知が表示されます。
- **アプリケーションが開いている場合**:独自にホストしている UI でメッセージを表示できます。Android Mobile SDK のアプリ内メッセージの UI スタイルに従うことをお勧めします。

## 追加情報
Braze のマーケティングエンドユーザーにとって、Android TV へのキャンペーンの開始は、Android モバイルアプリへのプッシュの開始と同じになります。これらのデバイスのみをターゲットにするには、セグメンテーションで Android TV アプリを選択することをお勧めします。 

FCM によって返される、配信およびクリックされた応答は、モバイル Android デバイスと同じ規則に従います。そのため、エラーがあれば、メッセージアクティビティログに表示されます。

