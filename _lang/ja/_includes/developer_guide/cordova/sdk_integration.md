## Cordova SDK の統合

### 前提条件

始める前に、お使いの環境が[最新の Braze Cordova SDK バージョン](https://github.com/braze-inc/braze-cordova-sdk?tab=readme-ov-file#minimum-version-requirements)でサポートされていることを確認せよ。

### ステップ 1: SDK をプロジェクトに追加する

{% alert warning %}
以下の方法で Braze Cordova SDK を追加するだけだ。他の方法でインストールしようと試みるな。セキュリティ侵害につながる恐れがある。
{% endalert %}

Cordova 6 以降では、GitHub から直接 SDK を追加できます。または、[GitHub リポジトリ](https://github.com/braze-inc/braze-cordova-sdk)の ZIP をダウンロードして、SDK を手動で追加することもできます。

{% tabs local %}
{% tab geofence disabled %}
ロケーションコレクションとジオフェンスを使用する予定がない場合は、GitHub の `master` ブランチを使用してください。

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master
```
{% endtab %}

{% tab geofence enabled %}
位置情報の収集とジオフェンスの使用を計画している場合は、GitHub の を使用します `geofence-branch` 。

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```
{% endtab %}
{% endtabs %}

{% alert tip %}
このステップを繰り返せば、いつでも `geofence-branch`と`master`  を切り替えられる。
{% endalert %}

### ステップ 2:プロジェクトを構成する

次に、プロジェクトの `config.xml` ファイル内の `platform` 要素に次の環境設定を追加します。

{% tabs %}
{% tab ios %}
```xml
<preference name="com.braze.ios_api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.ios_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}

{% tab android %}
```xml
<preference name="com.braze.android_api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.android_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}
{% endtabs %}

次のように置き換えます。

| 値                 | 説明                                                                                                                      |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `BRAZE_API_KEY`       | あなたの[Braze REST APIキー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys)。              |
| `CUSTOM_API_ENDPOINT` | カスタムAPIエンドポイント。このエンドポイントは、Brazeダッシュボードの正しいアプリグループにBrazeインスタンスデータをルーティングするために使用されます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

`config.xml` ファイルの `platform` 要素は次のようになります。

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.ios_api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.ios_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}

{% tab android %}
```xml
<platform name="android">
    <preference name="com.braze.android_api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.android_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}
{% endtabs %}

## プラットフォーム固有の構文

次のセクションでは、iOS または Android で Cordova を使用する場合のプラットフォーム固有の構文について説明する。

### 整数

{% tabs %}
{% tab ios %}
整数の設定は、次の例のように文字列表現として読み取られます。

```xml
<platform name="ios">
    <preference name="com.braze.ios_flush_interval_seconds" value="10" />
    <preference name="com.braze.ios_session_timeout" value="5" />
</platform>
```
{% endtab %}

{% tab android %}
Cordova 8.0.0 以降のフレームワークによる設定の処理方法に従って、整数のみの設定 (送信者 ID など) は、次の例のように先頭に `str_` が付加された文字列に設定する必要があります。

```xml
<platform name="android">
    <preference name="com.braze.android_fcm_sender_id" value="str_64422926741" />
    <preference name="com.braze.android_default_session_timeout" value="str_10" />
</platform>
```
{% endtab %}
{% endtabs %}

### ブール値

{% tabs %}
{% tab ios %}
ブール値の設定は、次の例のように、`YES` および `NO` キーワードを文字列表現として使用して SDK によって読み取られます。

```xml
<platform name="ios">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="YES" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
{% endtab %}

{% tab android %}
ブール値の設定は、次の例のように、`true` および `false` キーワードを文字列表現として使用して SDK によって読み取られます。

```xml
<platform name="android">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="true" />
    <preference name="com.braze.is_session_start_based_timeout_enabled" value="false" />
</platform>
```
{% endtab %}
{% endtabs %}

## オプション設定 {#optional}

次の設定をプロジェクトの `config.xml` ファイルの `platform` 要素に追加できます。

{% tabs %}
{% tab ios %}
| 方法                                            | 説明                                                                                                                                                                                                                                           |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
\|`ios_api_key`                                      | アプリケーションのAPI キーを設定する。                                                                                                                                                                                                                |
\|`ios_api_endpoint`                                 | アプリケーションの[SDK]({{site.baseurl}}/api/basics/#endpoints)エンドポイントを設定する。                                                                                                                                                                 |
\|`ios_disable_automatic_push_registration`          | 自動プッシュ登録を無効にするかどうかを設定する。                                                                                                                                                                                          |
\|`ios_disable_automatic_push_handling`              | 自動プッシュ処理を無効化するかどうかを設定する。                                                                                                                                                                      |
|            `ios_enable_idfa_automatic_collection` | Braze SDKがIDFA情報を自動的に収集するかどうかを設定する。詳細については、[BrazeのIDFAメソッドのドキュメントを](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/)参照せよ。 |
|                      `enable_location_collection` | 自動位置情報の収集のイネーブルメントを設定する（ユーザーが許可した場合）。その`geofence-branch`
\|`geofences_enabled`                                | ジオフェンスのイネーブルメントを設定する。                                                                                                                                                                                                                   |
\|`ios_session_timeout`                              | アプリケーションのBrazeセッションタイムアウトを秒単位で設定する。デフォルトは10秒だ。|
|                      `sdk_authentication_enabled` | [SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication)認証機能をイネーブルメントするかどうかを設定する。                                                                                              |
\|`display_foreground_push_notifications`            | アプリケーションがフォアグラウンドにある間、プッシュ通知を表示するかどうかを設定する。                                                                                                                                                       |
\|`ios_disable_un_authorization_option_provisional`  |  を無効にする`UNAuthorizationOptionProvisional`かどうかを設定する。                                                                                                                                                                                   |
|    `trigger_action_minimum_time_interval_seconds` | トリガー間の最小時間間隔を秒単位で設定する。デフォルトは30秒だ。|
\|`ios_push_app_group`                               | iOSプッシュ拡張機能のアプリグループIDを設定する。                                                                                                                                                                                                        |
\|`ios_forward_universal_links`                      | SDKがユニバーサルリンクを自動的に認識し、システムメソッドに転送するかどうかを設定する。iOSでプッシュ通知からのディープリンクを機能させるために必要だ。デフォルトは無効だ。
\|`ios_log_level`                                    | . `Braze.Configuration.Logger`の最小ログレベルを設定する。                                                                                                                                                                                      |
\|`ios_use_uuid_as_device_id`                        | ランダムに生成されたUUIDをデバイスIDとして使用するかどうかを設定する。                                                                                                                                                                                    |
|                      `ios_flush_interval_seconds` | 自動データフラッシュの間隔を秒単位で設定する。デフォルトは10秒だ。|
|                `ios_use_automatic_request_policy` | リクエストポリシーを自動`Braze.Configuration.Api`か手動か設定する。                                                                                                                                                          |
|              `should_opt_in_when_push_authorized` | プッシュ通知の許可が承認された際に`optedIn`、ユーザーの通知サブスクリプション状態を自動的に設定するかどうかを指定する。                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert tip %}
詳細については、[GitHub:Braze iOS Cordova プラグイン](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/ios/BrazePlugin.m)を参照してください。
{% endalert %}
{% endtab %}

{% tab android %}
| 方法                                                            | 説明                                                                                                                                                                                   |
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                `android_api_key`  | アプリケーションのAPI キーを設定する。                                                                                                                                                        |
\|`android_api_endpoint`                                             | アプリケーションの[SDK]({{site.baseurl}}/api/basics/#endpoints)エンドポイントを設定する。                                                                                                         |
通知の小さなアイコンを設定する`android_small_notification_icon`。
通知の大きなアイコンを設定する`android_large_notification_icon`。
\|`android_notification_accent_color`                                | 通知のアクセントカラーを16進数表記で設定する。                                                                                                                        |
\|`android_default_session_timeout`                                  | アプリケーションのBrazeセッションタイムアウトを秒単位で設定する。デフォルトは10秒だ。|
|                    `android_handle_push_deep_links_automatically` | Braze SDKがプッシュディープリンクを自動的に処理するかどうかを設定する。Androidでプッシュ通知からのディープリンクを機能させるために必要だ。デフォルトは無効だ。
|                                                `android_log_level`| アプリケーションのログレベルを設定する。デフォルトのログレベルは 4 で、最小限の情報をロギングします。デバッグ用の詳細ログのイネーブルメントを行うには、ログレベル2を使用する。
\|`firebase_cloud_messaging_registration_enabled`                    | プッシュ通知にFirebase Cloud Messagingを使用するかどうかを設定する。                                                                                                                          |
Firebase メッセージングの送信者 ID を設定する`android_fcm_sender_id`。
\|`enable_location_collection`                                       | 自動位置情報の収集のイネーブルメントを設定する（ユーザーが許可した場合）。                                                                                                              |
|                                                `geofences_enabled`| ジオフェンスのイネーブルメントを設定する。                                                                                                                                                           |
\|`android_disable_auto_session_tracking`                            | Android Cordovaプラグインによるセッションの自動トラッキングを無効にする。詳細については、[自動セッショントラッキングの無効化を](#cordova_disable-automatic-session-tracking)参照のこと。
\|`sdk_authentication_enabled`                                       | [SDK]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication)認証機能をイネーブルメントするかどうかを設定する。                                      |
|                    `trigger_action_minimum_time_interval_seconds` | トリガー間の最小時間間隔を秒単位で設定する。デフォルトは30秒だ。|
\|`is_session_start_based_timeout_enabled`                           | セッションタイムアウトの動作を、セッション開始イベントに基づくか終了イベントに基づくかを設定する。                                                                                          |
\|`default_notification_channel_name`                                | Brazeのデフォルト設定`NotificationChannel.getName`において`NotificationChannel`、ユーザーが閲覧する名称を設定する。                                                                              |
|                        `default_notification_channel_description` | Brazeのデフォルト設定`NotificationChannel.getDescription`において`NotificationChannel`、ユーザーが閲覧する説明文を設定する。                                                                |
\|`does_push_story_dismiss_on_click`                                 | プッシュストーリーがクリックされた際に自動的に非表示になるかどうかを設定する。                                                                                                                            |
|                  `is_fallback_firebase_messaging_service_enabled` | フォールバック用のFirebase Cloud Messagingサービスのイネーブルメントを有効にするかどうかを設定する。                                                                                                               |
\|`fallback_firebase_messaging_service_classpath`                    | フォールバック用のFirebase Cloud Messageングサービスのクラスパスを設定する。                                                                                                                         |
|                `is_content_cards_unread_visual_indicator_enabled` | コンテンツカードの未読視覚表示バーのイネーブルメントを設定する。                                                                                                                       |
\|`is_firebase_messaging_service_on_new_token_registration_enabled`  | Braze SDKが自動的にトークンを登録するかどうか`com.google.firebase.messaging.FirebaseMessagingService.onNewToken`を設定する。                                                         |
\|`is_push_deep_link_back_stack_activity_enabled`                    | プッシュ通知のディープリンクを自動追跡する際に、Brazeがバックスタックにアクティビティを追加するかどうかを設定する。                                                                                   |
\|`push_deep_link_back_stack_activity_class_name`                    | プッシュ通知のディープリンクを自動追跡する際、Brazeがバックスタックに追加するアクティビティを設定する。                                                                                     |
\|`should_opt_in_when_push_authorized`                               | プッシュ通知が許可された際に、Brazeがユーザーを自動的にオプトインするかどうかを設定する。                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert tip %}
詳細については、[GitHub:Braze Android Cordova プラグイン](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/android/BrazePlugin.kt)を参照してください。
{% endalert %}
{% endtab %}
{% endtabs %}

以下は、追加構成を含む `config.xml` ファイルの例です。

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO"/"YES" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO"/"YES" />
    <preference name="com.braze.ios_enable_idfa_automatic_collection" value="YES"/"NO" />
    <preference name="com.braze.enable_location_collection" value="NO"/"YES" />
    <preference name="com.braze.geofences_enabled" value="NO"/"YES" />
    <preference name="com.braze.ios_session_timeout" value="5" />
    <preference name="com.braze.sdk_authentication_enabled" value="YES"/"NO" />
    <preference name="com.braze.display_foreground_push_notifications" value="YES"/"NO" />
    <preference name="com.braze.ios_disable_un_authorization_option_provisional" value="NO"/"YES" />
    <preference name="com.braze.trigger_action_minimum_time_interval_seconds" value="30" />
    <preference name="com.braze.ios_push_app_group" value="PUSH_APP_GROUP_ID" />
    <preference name="com.braze.ios_forward_universal_links" value="YES"/"NO" />
    <preference name="com.braze.ios_log_level" value="2" />
    <preference name="com.braze.ios_use_uuid_as_device_id" value="YES"/"NO" />
    <preference name="com.braze.ios_flush_interval_seconds" value="10" />
    <preference name="com.braze.ios_use_automatic_request_policy" value="YES"/"NO" />
    <preference name="com.braze.should_opt_in_when_push_authorized" value="YES"/"NO" />
</platform>
```
{% endtab %}

{% tab android %}
```xml
<platform name="android">
    <preference name="com.braze.android_small_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.braze.android_large_notification_icon" value="RESOURCE_ENTRY_NAME_FOR_ICON_DRAWABLE" />
    <preference name="com.braze.android_notification_accent_color" value="str_ACCENT_COLOR_INTEGER" />
    <preference name="com.braze.android_default_session_timeout" value="str_SESSION_TIMEOUT_INTEGER" />
    <preference name="com.braze.android_handle_push_deep_links_automatically" value="true"/"false" />
    <preference name="com.braze.android_log_level" value="str_LOG_LEVEL_INTEGER" />
    <preference name="com.braze.firebase_cloud_messaging_registration_enabled" value="true"/"false" />
    <preference name="com.braze.android_fcm_sender_id" value="str_YOUR_FCM_SENDER_ID" />
    <preference name="com.braze.enable_location_collection" value="true"/"false" />
    <preference name="com.braze.geofences_enabled" value="true"/"false" />
    <preference name="com.braze.android_disable_auto_session_tracking" value="true"/"false" />
    <preference name="com.braze.sdk_authentication_enabled" value="true"/"false" />
    <preference name="com.braze.trigger_action_minimum_time_interval_seconds" value="str_MINIMUM_INTERVAL_INTEGER" />
    <preference name="com.braze.is_session_start_based_timeout_enabled" value="false"/"true" />
    <preference name="com.braze.default_notification_channel_name" value="DEFAULT_NAME" />
    <preference name="com.braze.default_notification_channel_description" value="DEFAULT_DESCRIPTION" />
    <preference name="com.braze.does_push_story_dismiss_on_click" value="true"/"false" />
    <preference name="com.braze.is_fallback_firebase_messaging_service_enabled" value="true"/"false" />
    <preference name="com.braze.fallback_firebase_messaging_service_classpath" value="FALLBACK_FIREBASE_MESSAGING_CLASSPATH" />
    <preference name="com.braze.is_content_cards_unread_visual_indicator_enabled" value="true"/"false" />
    <preference name="com.braze.is_firebase_messaging_service_on_new_token_registration_enabled" value="true"/"false" />
    <preference name="com.braze.is_push_deep_link_back_stack_activity_enabled" value="true"/"false" />
    <preference name="com.braze.push_deep_link_back_stack_activity_class_name" value="DEEPLINK_BACKSTACK_ACTIVITY_CLASS_NAME" />
    <preference name="com.braze.should_opt_in_when_push_authorized" value="true"/"false" />
</platform>
```
{% endtab %}
{% endtabs %}

## 自動セッショントラッキングを無効にする（Androidのみ） {#disable-automatic-session-tracking}

デフォルトでは、Android Cordova プラグインは自動的にセッションを追跡します。自動セッショントラッキングを無効にするには、プロジェクトの `config.xml` ファイル内の `platform` 要素に次の設定を追加します。

```xml
<platform name="android">
    <preference name="com.braze.android_disable_auto_session_tracking" value="true" />
</platform>
```

トラッキングセッションを再開するには、`BrazePlugin.startSessionTracking()` を呼び出します。次回の `Activity.onStart()` 以降に開始されたセッションのみが追跡されることに注意してください。
