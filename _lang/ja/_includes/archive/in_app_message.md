### スライドアップアプリ内メッセージ

[`Slideup`]{% if include.platform == "iOS" %}[in_app_message_1]{% elsif include.platform == "Android" %}[in_app_message_2]{% endif %} アプリ内メッセージは、画面の上部または下部から「スライドアップ」または「スライドダウン」するため、このような名前が付けられています。 画面の一部分だけを覆い、効果的で邪魔にならないメッセージング機能を提供します。

![スライドアップの例]({% image_buster /assets/img_archive/In-App_Slideup.png %})

### モーダルのアプリ内メッセージ

[`Modal`]{% if include.platform == "iOS" %}[in_app_message_3]{% elsif include.platform == "Android" %}[in_app_message_4]{% endif %} アプリ内メッセージは画面中央に表示され、半透明のパネルに囲まれます。より重要なメッセージングに役立つ、最大2つのクリックアクションと分析有効ボタンを装備できます。

![モーダルの例]({% image_buster /assets/img_archive/In-App_Modal.png %})

### 完全なアプリ内メッセージ

[`Full`]{% if include.platform == "iOS" %}[in_app_message_5]{% elsif include.platform == "Android" %}[in_app_message_6]{% endif %} アプリ内メッセージは、ユーザーコミュニケーションの内容とインパクトを最大化するのに有効です。 `full` アプリ内メッセージの上半分には画像が含まれ、下半分にはテキストが表示されます。また、最大2つのクリックアクションおよび分析が有効になっているボタンも表示されます。

![完全な例]({% image_buster /assets/img_archive/In-App_Full.png %})

### HTML フルアプリ内メッセージ

[`HTML Full`]{% if include.platform == "iOS" %}[in_app_message_7]{% elsif include.platform == "Android" %}[in_app_message_8]{% endif %} アプリ内メッセージは、完全にカスタマイズされたユーザーコンテンツを作成するのに便利です。ユーザー定義の HTML アプリ内のフルメッセージコンテンツは、{% if include.platform == "iOS" %}`WKWebView`{% elsif include.platform == "Android" %}`WebView`{% endif %} に表示され、必要に応じて画像やフォントなどの他のリッチコンテンツを含めることができます。これにより、メッセージの外観と機能を完全に制御できます。

 {% if include.platform == "iOS" %}
次の例は、ページ分割された HTML の完全アプリ内メッセージを示しています。

![HTML5の例]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

 {% elsif include.platform == "Android" %}次の例は、SoundCloud によって作成されたアンケート HTML の完全アプリ内メッセージを示しています。

![HTML5の例]({% image_buster /assets/img_archive/HTML5.gif %})
{% endif %}

完全 HTML アプリ内のメッセージコンテンツは、WKWebView に表示され、必要に応じて画像やフォントなどの他のリッチコンテンツを含めることができます。これにより、メッセージの外観と機能を完全に制御できます。**現在、iOS および Android プラットフォームでのiFrame でのカスタム HTML インアプリメッセージの表示はサポートされていません。**

## アプリ内メッセージ配信

### アプリ内メッセージ (トリガー)

以下のドキュメントでは、Braze の `In-App Messaging` 製品 (「トリガー付きアプリ内メッセージ」とも呼ばれます) を参照しています。これらは、「キャンペーンの作成」ドロップダウンで以下のようにブランド名として強調表示されています。

![アプリ内メッセージングコンポーザー]({% image_buster /assets/img_archive/trigger-iam-composer.png %})

非推奨の [`Original In-App Messaging`]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/create/#original-in-app-messages) 製品のドキュメントも参照できます。

#### トリガーの種類

アプリ内メッセージ製品を使用すると、次のようなさまざまなイベントタイプの結果としてアプリ内メッセージ表示をトリガーできます: `Any Purchase`、`Specific Purchase`、`Session Start`、`Custom Event`、および `Push Click`。 さらに、`Specific Purchase` および `Custom Event` トリガーには堅牢なプロパティフィルターを含めることができます。

{% alert note %}
トリガーされたアプリ内メッセージは、Braze SDK を通じて記録されたカスタムイベントでのみ機能します。アプリ内メッセージは、API または API イベント (購入イベントなど) によってトリガーすることはできません。Android を使用している場合は、[Android でカスタムイベントをログに記録する方法]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events).)を確認してください。iOS で作業している場合は、[iOS でカスタムイベントをログに記録する方法]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/#tracking-custom-events).を確認してください。
{% endalert %}

#### 配信セマンティクス

ユーザーが対象になるすべてのアプリ内メッセージは、セッション開始時にユーザーのデバイスに配信されます。SDK のセッション開始セマンティクスの詳細については、[session lifecycle documentation]{% if include.platform == "iOS" %}[in_app_message_15a]{% elsif include.platform == "Android" %}[in_app_message_15b]{% endif %} を参照してください。配信時に、SDK はアセットをプリフェッチしてトリガー時にすぐに利用できるようにし、表示遅延を最小限に抑えます。

トリガーイベントに複数の適格なアプリ内メッセージが関連付けられている場合、最も優先度の高いアプリ内メッセージのみが配信されます。

配信時にすぐに表示されるアプリ内メッセージ(セッションの開始、プッシュクリックなど) では、アセットがプリフェッチされないために遅延が発生することがあります。

#### トリガー間の最小時間間隔

デフォルトでは、高品質のユーザーエクスペリエンスを確保するために、アプリ内メッセージのレートが 30 秒に 1 回に制限されています。

{% if include.platform == "iOS" %}この値は、`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` に渡された `appboyOptions` パラメーター内の `ABKMinimumTriggerTimeIntervalKey` を使用してオーバーライドできます。`ABKMinimumTriggerTimeIntervalKey` を、アプリ内メッセージ間の最小時間 (秒) として使用する整数値に設定します。

```objc
// Sets the minimum trigger time interval to 5 seconds
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKMinimumTriggerTimeIntervalKey : @(5) }];
```

{% elsif include.platform == "Android" %}
この値をオーバーライドするには、`braze.xml` で `com_appboy_trigger_action_minimum_time_interval_seconds` を次のように設定します。

```xml
  <integer name="com_appboy_trigger_action_minimum_time_interval_seconds">5</integer>
```
{% endif %}

[in_app_message_1]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_slideup.html
[in_app_message_2]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html
[in_app_message_3]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_modal.html
[in_app_message_4]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html
[in_app_message_5]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_full.html
[in_app_message_6]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html
[in_app_message_7]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_h_t_m_l_full.html
[in_app_message_8]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html-full/index.html
[in_app_message_15a]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/#session-lifecycle
[in_app_message_15b]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#session-lifecycle

