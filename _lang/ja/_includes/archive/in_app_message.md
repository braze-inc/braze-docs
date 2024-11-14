### スライドアップアプリ内メッセージs

[`Slideup`]{% if include.platform == "iOS" %}[in_app_meta_1]{% elsif include.platform == "Android" %}[in_app_message_2]{% endif %}アプリ内メッセージは"slide up"slide down" 画面の上部または下部から、so-namedです。 画面の一部分だけを覆い、効果的で邪魔にならないメッセージング機能を提供します。

![スライドアップの例][in_app_message_9]

### モーダルのアプリ内メッセージ

[`Modal`]{% if include.platform == "iOS" %}[in_app_message_3]{% elsif include.platform == "Android" %}[in_app_message_4]{% endif %}アプリ内メッセージが画面中央に表示され、透過パネルで囲まれます。より重要なメッセージングに役立つ、最大2 つのクリックアクションと分析有効ボタンを装備できます。

![モードの例][in_app_message_10]

### 完全なアプリ内メッセージ

[`Full`]{% if include.platform == "iOS" %}[in_app_message_5]{% elsif include.platform == "Android" %}[in_app_message_6]{% endif %} アプリ内メッセージは、ユーザ通信の内容と影響を最大限にするために役立ちます。 `full` アプリ内メッセージの上半分には画像が含まれ、下半分にはテキストが表示されます。また、最大2 つのクリックアクションおよび分析が有効になっているボタンも表示されます。

![完全な例][in_app_message_11]

### HTML 完全アプリ内メッセージ

[`HTML Full`]{% if include.platform == "iOS" %}[in_app_message_7]{% elsif include.platform == "Android" %}[in_app_message_8]{% endif %} アプリ内メッセージは、完全にカスタマイズされたユーザーコンテンツの作成に役立ちます。ユーザー定義のHTML Full in-app メッセージコンテンツは、{% if include.platform == "iOS" %}`WKWebView`{% elsif include.platform == "Android" %}`WebView`{% endif %} に表示され、オプションで画像やフォントなどの他のリッチコンテンツを含むことができ、メッセージの外観と機能を完全に制御できます。

 {% if include.platform == "iOS" %}
次の例は、ページ分割された HTML の完全アプリ内メッセージを示しています。

![HTML5 の例][in_app_message_23]

 {% elsif include.platform == "Android" %}次の例は、SoundCloud によって作成されたアンケートHTML Full in-app メッセージを示しています。

![HTML5 の例][in_app_message_12]
{% endif %}

完全なアプリ内メッセージコンテンツは、WKWebView に表示されます。また、オプションで、画像やフォントなどの豊富なコンテンツを含めることもできます。これにより、メッセージの外観や機能を完全に制御できます。**現在、iOS およびAndroid プラットフォームでのiFrame でのカスタムHTML インアプリメッセージの表示はサポートされていません。**

## アプリ内メッセージ配信

### アプリ内メッセージ(トリガー)

以下のドキュメントでは、Braze の`In-App Messaging` 製品("triggered in-app messages,&quot とも呼ばれます) を参照しています。これらは、"Create Campaign" dropdown で以下のようにハイライト表示されています

![アプリ内メッセージングコンポーザー][in_app_message_13]

非推奨の[`Original In-App Messaging`][in_app_message_14] 製品のドキュメントも参照できます。

#### トリガーの種類

アプリ内メッセージ製品では、`Any Purchase`、`Specific Purchase`、`Session Start`、`Custom Event`、`Push Click` のように、いくつかの異なるイベントタイプの結果としてアプリ内メッセージ表示をトリガすることができます。 さらに、`Specific Purchase` および `Custom Event` トリガーには堅牢なプロパティフィルターを含めることができます。

{% alert note %}
トリガーされたアプリ内メッセージは、Braze SDK を通じて記録されたカスタムイベントでのみ機能します。アプリ内メッセージは、API または API イベント (購入イベントなど) によってトリガーすることはできません。Android を使用している場合は、[Android でカスタムイベントをログに記録する方法][in_app_message_24]] を確認してください。iOS を使用している場合は、[iOS][in_app_message_25] にカスタムイベントを記録する方法を確認してください。
{% endalert %}

#### 配信セマンティクス

ユーザーが対象になるすべてのアプリ内メッセージは、セッション開始時にユーザーのデバイスに配信されます。SDK のセッション開始セマンティクスの詳細については、[session lifecycle documentation]{% if include.platform == "iOS" %}[in_app_message_15a]{% elsif include.platform == "Android" %}[in_app_message_15b]{% endif %} を参照してください。配信時に、SDK はアセットをプリフェッチし、トリガー時にすぐに使用できるようにします。これにより、表示レイテンシーが最小限に抑えられます。

トリガーイベントに複数の適格なアプリ内メッセージが関連付けられている場合、最も優先度の高いアプリ内メッセージのみが配信されます。

配信時にすぐに表示されるアプリ内メッセージ(セッションの開始、プッシュクリックなど) では、アセットがプリフェッチされないために遅延が発生することがあります。

#### トリガー間の最小時間間隔

デフォルトでは、アプリ内メッセージのレートは、質の高いユーザーエクスペリエンスに対して30 秒ごとに1 回に制限されます。

{% if include.platform == "iOS" %}この値は、`ABKMinimumTriggerTimeIntervalKey` に渡される`appboyOptions` パラメータ内の`ABKMinimumTriggerTimeIntervalKey` で上書きできます。`ABKMinimumTriggerTimeIntervalKey` を、アプリ内メッセージ間の最小時間 (秒) として使用する整数値に設定します。

```objc
// Sets the minimum trigger time interval to 5 seconds
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKMinimumTriggerTimeIntervalKey : @(5) }];
```

{% elsif include.platform == "Android" %}
この値をオーバーライドするには、`braze.xml` で`com_appboy_trigger_action_minimum_time_interval_seconds` を設定します。

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
[in_app_message_9]: {% image_buster /assets/img_archive/In-App_Slideup.png %}
[in_app_message_10]: {% image_buster /assets/img_archive/In-App_Modal.png %}
[in_app_message_11]: {% image_buster /assets/img_archive/In-App_Full.png %}
[in_app_message_12]: {% image_buster /assets/img_archive/HTML5.gif %}
[in_app_message_13]: {% image_buster /assets/img_archive/trigger-iam-composer.png %}
[in_app_message_14]: {{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/create/#original-in-app-messages
[in_app_message_15a]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/#session-lifecycle
[in_app_message_15b]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#session-lifecycle
[in_app_message_19]: {{ site.baseurl }}/developer_guide/platform_integration_guides/{{ include.platform }}/in-app_messaging/#in-app-messages-triggered
[in_app_message_23]: {% image_buster /assets/img_archive/ios-html-full-iam.gif %}
[in_app_message_24]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events
[in_app_message_25]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/#tracking-custom-events

