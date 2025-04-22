{% multi_lang_include developer_guide/prerequisites/android.md %} [プッシュ通知の設定]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android)も必要です。

## カスタム通知レイアウト

ブレーズ通知は[データメッセージ](https://firebase.google.com/docs/cloud-messaging/concept-options)として送信されます。これは、アプリケーションがバックグラウンドであっても(通知メッセージとは対照的に、アプリがバックグラウンドにあるときにシステムによって自動的に処理される)、常に応答し、それに従って動作を実行する機会があることを意味します。そのため、通知トレイに配信される通知にパーソナライズされた UI 要素を表示するなどして、アプリケーションでエクスペリエンスをカスタマイズできます。この方法でプッシュを実装することに慣れていない方もいるかもしれませんが、Braze でよく知られている機能の 1 つである[プッシュ通知ストーリー]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/)は、カスタムビューコンポーネントを使用して魅力的なエクスペリエンスを生み出す機能の良い例です。

{% alert important %}
Android では、カスタム通知ビューを実装するために使用できるコンポーネントにいくつかの制限があります。通知ビューレイアウトには、[RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews) フレームワークと互換性のある View オブジェクト_のみ_を含める必要があります。
{% endalert %}

## パーソナライズされたプッシュ通知

プッシュ通知では、カスタムビュー階層内にユーザー固有の情報を表示できます。次の例では、API-trigger を使用してパーソナライズされたプッシュ通知をユーザに送信し、アプリで特定のタスクを完了した後で現在の進行状況を追跡できるようにします。

![パーソナライズされたプッシュダッシュボードの例]({% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}){: style="max-width:65%;border:0"}

ダッシュボードでパーソナライズされたプッシュを設定するには、表示する特定のカテゴリを登録し、Liquid を使用して表示したい関連するユーザー属性を設定します。

![パーソナライズされたプッシュダッシュボードの例]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}
