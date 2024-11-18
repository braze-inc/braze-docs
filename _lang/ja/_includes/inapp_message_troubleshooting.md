## 基本チェック

#### あるユーザーのアプリ内メッセージが表示されない

1. SDKが新しいアプリ内メッセージを要求したとき、ユーザーはセッション開始時にセグメンテーションにいたか？
2. ユーザーはキャンペーンターゲティングルールに従ってアプリ内メッセージを受信する資格があったか、または再資格があったか。
3. ユーザーはフリークエンシーキャップの影響を受けたのか？
4. ユーザーはコントロールグループにいたのか？キャンペーンがABテスト用に設定されているか確認する。
5. 期待されたメッセージの代わりに、より優先順位の高い別のアプリ内メッセージが表示されたか？
6. 私のデバイスはキャンペーンで指定された正しい向きになっていたか？
7. 私のメッセージは、SDKによって強制された、トリガー間のデフォルトの最小時間間隔30秒によって抑制されたのだろうか？

#### このプラットフォームでは、アプリ内メッセージがすべてのユーザーに表示されなかった。

1. キャンペーンは、モバイルアプリまたはWebブラウザのいずれかを適切にターゲットとするように設定されているか。例として、キャンペーンがWebブラウザのみをターゲットにしている場合、Androidデバイスには送信されない。
2. カスタムUIを実装し、意図したとおりに機能しているか？他のアプリ側のカスタム処理や抑制が表示を妨げていないか？ 
3. この特定のプラットフォームとアプリのバージョンで、アプリ内メッセージが正常に表示されたことはあるか？
4. トリガーはデバイスのローカルで行われたのか？RESTコールはSDKのアプリ内メッセージのトリガーには使えないことに注意。

#### アプリ内メッセージがすべてのユーザーに表示されなかった。

1. ダッシュボードやアプリとの連携で、トリガーアクションは適切に設定されたか？
2. 期待されたメッセージの代わりに、より優先順位の高い別のアプリ内メッセージが表示されたか？
3. SDKのバージョンは新しいか？アプリ内メッセージの種類によってはSDKのバージョン要件がある。
4. セッションは適切に統合されているか？このアプリでセッション分析は機能しているか？

これらのシナリオの詳細については、[高度なトラブルシューティングのセクションを](#troubleshooting-in-app-advanced)参照のこと。

## インプレッションとクリック分析の問題点

{% if include.sdk == "iOS" %}
#### インプレッションとクリックが記録されない

アプリ内メッセージデリゲートを設定し、メッセージ表示やクリックアクションを手動で処理する場合、アプリ内メッセージの[クリック](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:))数や[インプレッションを](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logimpression(using:))手動で[記録する](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:))必要がある。
{% elsif include.sdk == "Android" %}
#### インプレッションとクリックが記録されない
アプリ内メッセージデリゲートを設定し、メッセージ表示やクリックアクションを手動で処理する場合、アプリ内メッセージのクリック数やインプレッションを手動で記録する必要がある。
{% endif %}

#### インプレッションが予想より低い

トリガーはセッション開始時にデバイスへの同期に時間がかかるため、ユーザーがセッション開始直後にイベントや購入を記録すると競合状態が発生する可能性があります。考えられる回避策の 1 つは、キャンペーンを変更してセッションの開始をトリガーし、目的のイベントまたは購入をセグメント化することです。なお、イベント発生後の次回セッション開始時にアプリ内メッセージが配信されることに注意してください。

## 高度なトラブルシューティング {#troubleshooting-in-app-advanced}

ほとんどのアプリ内メッセージの問題は、配信と表示の 2 つの主要なカテゴリに分けることができます。期待したアプリ内メッセージがデバイスに表示されなかった原因をトラブルシューティングするには、[アプリ内メッセージがデバイスに配信された](#troubleshooting-in-app-message-delivery)ことを確認し、[メッセージ表示のトラブルシューティングを行う](#troubleshooting-in-app-message-display)。

### アプリ内メッセージ配信のトラブルシューティング {#troubleshooting-in-app-message-delivery}

SDK はセッション開始時に Braze サーバーからアプリ内メッセージを要求します。アプリ内メッセージがデバイスに配信されているかどうかを確認するには、アプリ内メッセージが SDK によってリクエストされ、Braze サーバーによって返されていることを確認する必要があります。

#### メッセージが要求され、返されたかどうかを確認する

1. ダッシュボードの[テストユーザー]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) )として追加する。
2. ユーザーを対象としたアプリ内メッセージキャンペーンを設定します。
3. アプリケーションで新しいセッションが発生することを確認します。
4. event user logs]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) ) を使って、デバイスがセッション開始時にアプリ内メッセージを要求していることを確認する。テストユーザーのセッション開始イベントに関連付けられた SDK リクエストを見つけます。
  - トリガーされたアプリ内メッセージをリクエストするためのアプリであれば、[**レスポンスデータ**] の [**リクエスト済みレスポンス**] フィールドに `trigger` が表示されます。
  - アプリが元のアプリ内メッセージをリクエストするためのものだった場合、[**レスポンスデータ］**] の [**リクエスト済みレスポンス**] フィールドに `in_app` が表示されます。
5. event user logs]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) ) を使って、レスポンスデータに正しいアプリ内メッセージが返されているかどうかをチェックする。<br>![]({% image_buster /assets/img_archive/event_user_log_iams.png %})

##### リクエストされていないメッセージのトラブルシューティング

アプリ内メッセージがリクエストされていない場合、アプリ内メッセージはセッション開始時にリフレッシュされるため、アプリがセッションを正しくトラッキングしていない可能性があります。また、アプリのセッションタイムアウトセマンティクスに基づいて、アプリが実際にセッションを開始していることを確認してください:

![成功したセッション開始イベントを表示するイベントユーザーログで見つかったSDKリクエスト。]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

##### メッセージが返されない問題のトラブルシューティング

アプリ内メッセージが返されない場合、キャンペーンターゲティングの問題が発生している可能性があります。

- セグメントにユーザーが含まれていない。
  - ユーザーの[\*\*エンゲージメント**]({{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) タブで、**セグメントの**下に正しいセグメンテーションが表示されているか確認する。
- ユーザーが以前にアプリ内メッセージを受け取ったことがあり、再度受け取る資格がなかった。
  - **キャンペーンコンポーザーの** **配信**ステップにある[キャンペーンの再資格設定]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/) )を確認し、再資格設定があなたのテスト設定と一致していることを確認する。
- ユーザーがキャンペーンのフリークエンシーキャップに達した。
  - キャンペーン[フリークエンシーキャップ設定]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) )を確認し、テストの設定と一致していることを確認する。
- キャンペーンにコントロールグループが存在した場合、ユーザーがコントロールグループに分類された可能性があります。
  - キャンペーンバリアントが [**制御**] に設定されている受信キャンペーンバリアントフィルターでセグメントを作成し、ユーザーがそのセグメントに分類されたかどうかを確認することで、これが発生したかどうかを確認できます。
  - 統合テスト目的でキャンペーンを作成する場合は、コントロールグループの追加をオプトアウトしてください。


### アプリ内メッセージ表示のトラブルシューティング {#troubleshooting-in-app-message-display}

アプリ内メッセージのリクエストと受信に成功しているにもかかわらず表示されない場合、デバイス側のロジックが表示を妨げている可能性がある：

{% if include.sdk == "iOS" %}
- トリガーされたアプリ内メッセージは、[トリガー間の最小時間間隔]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers) (デフォルトは30秒) に基づいてレート制限されます。
{% elsif include.sdk == "Android" %}
- トリガーされたアプリ内メッセージは、[トリガー間の最小時間間隔]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers) (デフォルトは30秒) に基づいてレート制限されます。
{% elsif include.sdk == "Web" %}
- トリガーされたアプリ内メッセージは、[トリガー間の最小時間間隔]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers) (デフォルトは30秒) に基づいてレート制限されます。
{% endif %}
- 画像のダウンロードに失敗すると、画像付きのアプリ内メッセージが表示されなくなります。画像のダウンロードに失敗していないか、デバイスのログを確認してください。
{% case include.sdk %}
  {% when "iOS", "Android" %}
- アプリ内メッセージ処理をカスタマイズするようにデリゲートを設定している場合は、デリゲートがアプリ内メッセージ表示に影響していないことを確認してください。
  {% when "Web" %}
- `braze.subscribeToInAppMessage` または `appboy.subscribeToNewInAppMessages` を介してカスタムのアプリ内メッセージを処理する場合は、そのサブスクリプションをチェックして、それがアプリ内メッセージの表示に影響を及ぼしていないことを確認します。
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
- 端末の向きがアプリ内メッセージで指定された向きと一致しなかった場合、アプリ内メッセージは表示されません。デバイスの向きが正しいことを確認してください。
{% endcase %}