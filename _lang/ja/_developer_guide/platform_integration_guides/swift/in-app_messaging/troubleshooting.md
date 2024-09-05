---
nav_title: トラブルシューティング
article_title: iOSのアプリ内メッセージングのトラブルシューティング
platform: Swift
page_order: 6
description: "この参考記事では、Swift SDKのiOSアプリ内メッセージのトラブルシューティングのトピックを取り上げる。"
channel:
  - in-app messages

---

# トラブルシューティング

> このリファレンス記事では、iOS のアプリ内メッセージのトラブルシューティングに関する潜在的なトピックを取り上げます。

## インプレッション

### インプレッション分析やクリック分析が記録されていない

メッセージ表示やクリックアクションを手動で処理するようにアプリ内メッセージデリゲートを設定した場合、アプリ内メッセージの[クリック](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:))数と[インプレッション](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logimpression(using:)) [数を](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:))手動で[記録](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:))する必要がある。

### インプレッションが予想より低い

トリガーはセッション開始時にデバイスへの同期に時間がかかるため、ユーザーがセッション開始直後にイベントや購入を記録すると競合状態が発生する可能性があります。考えられる回避策の 1 つは、キャンペーンを変更してセッションの開始をトリガーし、目的のイベントまたは購入をセグメント化することです。なお、イベント発生後の次回セッション開始時にアプリ内メッセージが配信されることに注意してください。

## 予期したアプリ内メッセージが表示されなかった

ほとんどのアプリ内メッセージの問題は、配信と表示の 2 つの主要なカテゴリに分けることができます。期待したアプリ内メッセージがデバイスに表示されなかった原因をトラブルシューティングするには、まず \[アプリ内メッセージがデバイスに配信されたことを確認する]]\[iam_11] 次に、\[メッセージ表示のトラブルシューティング]\[iam_12].

### アプリ内メッセージ配信のトラブルシューティング {#troubleshooting-in-app-message-delivery}

SDK はセッション開始時に Braze サーバーからアプリ内メッセージを要求します。アプリ内メッセージがデバイスに配信されているかどうかを確認するには、アプリ内メッセージが SDK によってリクエストされ、Braze サーバーによって返されていることを確認する必要があります。

#### メッセージが要求され、返されたかどうかを確認する

1. ダッシュボードに\[test user]\[iam_1] ] として追加する。
2. ユーザーを対象としたアプリ内メッセージキャンペーンを設定します。
3. アプリケーションで新しいセッションが発生することを確認します。
4. event user logs]\[iam_3] ] を使って、デバイスがセッション開始時にアプリ内メッセージを要求していることを確認する。テストユーザーのセッション開始イベントに関連するSDKリクエストを見つける。
  - トリガーされたアプリ内メッセージをリクエストするためのアプリであれば、\[**レスポンスデータ**] の \[**リクエスト済みレスポンス**] フィールドに `trigger` が表示されます。
  - アプリが元のアプリ内メッセージをリクエストするためのものだった場合、\[**レスポンスデータ］**] の \[**リクエスト済みレスポンス**] フィールドに `in_app` が表示されます。
5. event user logs]\[iam_3] ] を使って、レスポンスデータに正しいアプリ内メッセージが返されているかどうかをチェックする。<br>![]\[iam_5]

#### メッセージが要求されていない

アプリ内メッセージがリクエストされていない場合、アプリ内メッセージはセッション開始時にリフレッシュされるため、アプリがセッションを正しくトラッキングしていない可能性があります。また、アプリのセッションタイムアウトセマンティクスに基づいて、アプリが実際にセッションを開始していることを確認してください:

![]\[iam_10] 成功したセッション開始イベントを表示するイベントユーザーログで見つかったSDKリクエスト。]

#### メッセージが返されない

アプリ内メッセージが返ってこない場合、キャンペーンのターゲティングに問題がある可能性が高い。

##### セグメントにユーザーが含まれていない
ユーザーの\[\*\*Engagement**]\[iam_6] ] タブで、**Segmentsの**下に正しいセグメントが表示されているか確認する。

##### ユーザーが以前にアプリ内メッセージを受信しており、再度受信する資格がない
**キャンペーンコンポーザーの** **配信**ステップの下にある\[キャンペーンの再資格設定]\[iam_7] ]] をチェックし、再資格設定があなたのテストセットアップと一致していることを確認する。

##### キャンペーン回数の上限を超えた
キャンペーン\[フリークエンシーキャップの設定]]\[iam_8] ] を確認し、テストのセットアップと一致していることを確認する。

##### 対照群から脱落したユーザー
キャンペーンにコントロールグループが存在した場合、ユーザーがコントロールグループに分類された可能性があります。キャンペーンバリアントが \[**制御**] に設定されている受信キャンペーンバリアントフィルターでセグメントを作成し、ユーザーがそのセグメントに分類されたかどうかを確認することで、これが発生したかどうかを確認できます。 

統合テスト目的でキャンペーンを作成する場合は、コントロールグループの追加をオプトアウトしてください。

### アプリ内メッセージ表示のトラブルシューティング {#troubleshooting-in-app-message-display}

アプリがアプリ内メッセージのリクエストと受信に成功しているのに表示されない場合は、デバイス側のロジックによって表示が妨げられている可能性があります。

- トリガーされたアプリ内メッセージは、[トリガー間の最小時間間隔]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers) (デフォルトは30秒) に基づいてレート制限されます。
- アプリ内メッセージ処理をカスタマイズするようにデリゲートを設定している場合は、デリゲートがアプリ内メッセージ表示に影響していないことを確認してください。
- 画像のダウンロードに失敗すると、画像付きのアプリ内メッセージが表示されなくなります。画像のダウンロードに失敗していないか、デバイスのログを確認してください。
- 端末の向きがアプリ内メッセージで指定された向きと一致しなかった場合、アプリ内メッセージは表示されません。デバイスの向きが正しいことを確認してください。

### アセット・ローディングのトラブルシューティング (`NSURLError` コード`-1008`)

`NSURLError` Brazeをサードパーティのネットワークロギングライブラリと統合する場合、開発者は一般的にドメインコード`-1008` 。このエラーは、画像やフォントなどのアセットが取得できなかったか、キャッシュに失敗したことを示している。このようなケースを回避するには、BrazeのCDN URLを、これらのライブラリによって無視されるべきドメインのリストに登録する必要がある。

#### ドメイン

CDNドメインの全リストは以下の通り：

* `"appboy-images.com"`
* `"braze-images.com"`
* `"cdn.braze.eu"`
* `"cdn.braze.com"`

#### 例

以下は、Brazeのアセットキャッシュと競合することが知られているライブラリと、その問題を回避するためのサンプルコードである。使用できないリソース・エラーを引き起こすライブラリを使用しているプロジェクトで、以下にリストアップされていない場合は、そのライブラリのドキュメントを参照して、同様の使用APIを確認してほしい。

##### ネットフォックス

{% tabs %}
{% tab スウィフト %}
```swift
NFX.sharedInstance().ignoreURLs(["https://cdn.braze.com"])
```
{% endtab %}
{% tab Objective-C %}
```objc
[NFX.sharedInstance ignoreURLs:@[@"https://cdn.braze.com"]];
```
{% endtab %}
{% endtabs %}

##### ネットガード

{% tabs %}
{% tab スウィフト %}
```swift
NetGuard.blackListHosts.append(contentsOf: ["cdn.braze.com"])
```
{% endtab %}
{% tab Objective-C %}
```objc
NSMutableArray<NSString *> *blackListHosts = [NetGuard.blackListHosts mutableCopy];
[blackListHosts addObject:@"cdn.braze.com"];
NetGuard.blackListHosts = blackListHosts;
```
{% endtab %}
{% endtabs %}

##### XNロガー

{% tabs %}
{% tab スウィフト %}
```swift
let brazeAssetsHostFilter = XNHostFilter(host: "https://cdn.braze.com")
XNLogger.shared.addFilters([brazeAssetsHostFilter])
```
{% endtab %}
{% tab Objective-C %}
```objc
XNHostFilter *brazeAssetsHostFilter = [[XNHostFilter alloc] initWithHost: @"https://cdn.braze.com"];
[XNLogger.shared addFilters:@[brazeAssetsHostFilter]];
```
{% endtab %}
{% endtabs %}

\[iam_1]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users
\[iam_2]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
\[iam_3]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
\[iam_5]:  {% image_buster /assets/img_archive/event_user_log_iams.png %}
\[iam_6]: {{ site.baseurl }}/user_guide/engagement_tools/segments/user_profiles/#engagement-tab
\[iam_7]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/
\[iam_8]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping
\[iam_10]: {% image_buster /assets/img_archive/event_user_log_session_start.png %}
\[iam_11]: #troubleshooting-in-app-message-delivery
\[iam_12]: #troubleshooting-in-app-message-display

