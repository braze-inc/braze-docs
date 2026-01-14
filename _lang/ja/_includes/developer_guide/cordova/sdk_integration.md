## Cordova SDKを統合する

### 前提条件

開始する前に、お使いの環境が[最新のBraze Cordova SDKバージョンに](https://github.com/braze-inc/braze-cordova-sdk?tab=readme-ov-file#minimum-version-requirements)対応していることを確認する。

### ステップ 1: SDK をプロジェクトに追加する

{% alert warning %}
以下の方法でBraze Cordova SDKのみを追加する。セキュリティ侵害につながる可能性があるため、他の方法でインストールを試みないこと。
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
このステップを繰り返すことで、いつでも`master` と`geofence-branch` を切り替えることができる。
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

以下のセクションでは、iOSやAndroidでCordovaを使用する際のプラットフォーム固有の構文について説明する。

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

## オプション構成 {#optional}

次の設定をプロジェクトの `config.xml` ファイルの `platform` 要素に追加できます。

{% tabs %}
{% tab ios %}
| メソッド
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
\|`ios_api_key` | アプリケーションのAPIキーを設定する。                                                                                                                                                                                                                |
\|`ios_api_endpoint` | アプリケーションの[SDKエンドポイントを]({{site.baseurl}}/api/basics/#endpoints)設定する。                                                                                                                                                                 |
\|`ios_disable_automatic_push_registration` | 自動プッシュ登録を無効にするかどうかを設定する。                                                                                                                                                                                          |
\|`ios_disable_automatic_push_handling` | 自動プッシュ処理を無効にするかどうかを設定する。                                                                                                                                                                                              |
\|`ios_enable_idfa_automatic_collection` | Braze SDKが自動的にIDFA情報を収集するかどうかを設定する。詳しくは、[Braze IDFAメソッドのドキュメントを](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/)参照のこと。|
\|`enable_location_collection` | 自動ロケーション収集をイネーブルメントにするかどうかを設定する（ユーザーが許可した場合）。The`geofence-branch` |
\|`geofences_enabled` | ジオフェンスをイネーブルメントにするかどうかを設定する。                                                                                                                                                                                                                   |
\|`ios_session_timeout` | アプリケーションのBrazeセッションタイムアウトを秒単位で設定する。デフォルトは10秒である。                                                                                                                                                               |
\|`sdk_authentication_enabled` |[SDK認証]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication)機能を有効にするかどうかを設定する。                                                                                              |
\|`display_foreground_push_notifications` | アプリケーションがフォアグラウンドの間、プッシュ通知を表示するかどうかを設定する。                                                                                                                                                       |
\|`ios_disable_un_authorization_option_provisional` |`UNAuthorizationOptionProvisional` を無効にするかどうかを設定する。                                                                                                                                                                                   |
\|`trigger_action_minimum_time_interval_seconds` ｜トリガー間の最小時間間隔を秒単位で設定する。デフォルトは30秒である。                                                                                                                                                                   |
\|`ios_push_app_group` | iOSプッシュ拡張のアプリグループIDを設定する。                                                                                                                                                                                                        |
\|`ios_forward_universal_links` | SDKが自動的にユニバーサルリンクを認識し、システムメソッドに転送するかどうかを設定する。                                                                                                                                                     |
\|`ios_log_level` |`Braze.Configuration.Logger` の最小ログレベルを設定する。                                                                                                                                                                                      |
\|`ios_use_uuid_as_device_id` | ランダムに生成されたUUIDをデバイスIDとして使用するかどうかを設定する。                                                                                                                                                                                    |
\|`ios_flush_interval_seconds` ｜自動データフラッシュの間隔を秒単位で設定する。デフォルトは10秒である。                                                                                                                                                                  |
\|`ios_use_automatic_request_policy` |`Braze.Configuration.Api` のリクエストポリシーを自動にするか手動にするかを設定する。                                                                                                                                                          |
\|`should_opt_in_when_push_authorized` | プッシュ権限が許可されたときに、ユーザーのサブスクリプション状態を自動的に`optedIn` に設定するかどうかを設定する。                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert tip %}
詳細については、[GitHub:Braze iOS Cordova プラグイン](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/ios/BrazePlugin.m)を参照してください。
{% endalert %}
{% endtab %}

{% tab android %}
| メソッド
| ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
\|`android_api_key` | アプリケーションのAPIキーを設定する。                                                                                                                                                        |
\|`android_api_endpoint` | アプリケーションの[SDKエンドポイントを]({{site.baseurl}}/api/basics/#endpoints)設定する。                                                                                                         |
\|`android_small_notification_icon` | 通知小アイコンを設定する。                                                                                                                                                             |
｜`android_large_notification_icon` ｜通知の大きなアイコンを設定する。                                                                                                                                                             |
\|`android_notification_accent_color` | 通知アクセントカラーを16進数で設定する。                                                                                                                        |
\|`android_default_session_timeout` | アプリケーションのBrazeセッションタイムアウトを秒単位で設定する。デフォルトは10秒である。                                                                                                       |
\|`android_handle_push_deep_links_automatically` | Braze SDKが自動的にプッシュディープリンクを処理するかどうかを設定する。                                                                                                                       |
\|`android_log_level` アプリケーションのログレベルを設定する。デフォルトのログレベルは 4 で、最小限の情報をロギングします。デバッグのために冗長ロギングを有効にするには、ログレベル2を使う。                                    |
\|`firebase_cloud_messaging_registration_enabled` | Firebase Cloud Messagingをプッシュ通知に使用するかどうかを設定する。                                                                                                                          |
\|`android_fcm_sender_id` | Firebase Cloud Messaging の送信者 ID を設定する。                                                                                                                                                  |
\|`enable_location_collection` | 位置情報の自動収集をイネーブルメントにするかどうかを設定する（ユーザーが許可した場合）。                                                                                                              |
\|`geofences_enabled` | ジオフェンスをイネーブルメントにするかどうかを設定する。                                                                                                                                                           |
\|`android_disable_auto_session_tracking` | Cordovaプラグインが自動的にセッションをトラッキングするのを無効にする。詳しくは、[自動セッション追跡を無効にする](#cordova_disable-automatic-session-tracking)｜を参照のこと。
\|`sdk_authentication_enabled` |[SDK認証]({{site.baseurl}}/developer_guide/platform_wide/sdk_authentication#sdk-authentication)機能を有効にするかどうかを設定する。                                      |
\|`trigger_action_minimum_time_interval_seconds` ｜トリガー間の最小時間間隔を秒単位で設定する。デフォルトは30秒である。                                                                                                           |
\|`is_session_start_based_timeout_enabled` | セッションタイムアウトの動作を、セッション開始イベントとセッション終了イベントのどちらに基づいて行うかを設定する。                                                                                          |
\|`default_notification_channel_name` | Brazeのデフォルト`NotificationChannel` に対して、`NotificationChannel.getName` 経由で見られるユーザー向けの名前を設定する。                                                                              |
\|`default_notification_channel_description` | Brazeのデフォルト`NotificationChannel` に対して、`NotificationChannel.getDescription` を介して見られるユーザー向けの説明を設定する。                                                                |
｜`does_push_story_dismiss_on_click` ｜プッシュストーリーをクリックしたときに自動的に解除するかどうかを設定する。                                                                                                                            |
\|`is_fallback_firebase_messaging_service_enabled` | フォールバック Firebase Cloud Messaging Service の使用をイネーブルメントするかどうかを設定する。                                                                                                               |
\|`fallback_firebase_messaging_service_classpath` | フォールバック Firebase Cloud Messaging Service のクラスパスを設定する。                                                                                                                         |
\|`is_content_cards_unread_visual_indicator_enabled` | コンテンツカード未読視覚表示バーをイネーブルメントにするかどうかを設定する。                                                                                                                       |
\|`is_firebase_messaging_service_on_new_token_registration_enabled` | Braze SDKが自動的にトークンを`com.google.firebase.messaging.FirebaseMessagingService.onNewToken` に登録するかどうかを設定する。                                                         |
\|`is_push_deep_link_back_stack_activity_enabled` | ディープリンクを自動的にたどってプッシュする際に、Brazeがアクティビティをバックスタックに追加するかどうかを設定する。                                                                                   |
\|`push_deep_link_back_stack_activity_class_name` | ディープリンクを自動的にたどってプッシュする際に、Brazeがバックスタックに追加するアクティビティを設定する。                                                                                     |
\|`should_opt_in_when_push_authorized` | プッシュが許可されたときに、Brazeが自動的にユーザーをオプトインするかどうかを設定する。                                                                                                                   |
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

## 自動セッション追跡を無効にする（Androidのみ） {#disable-automatic-session-tracking}

デフォルトでは、Android Cordova プラグインは自動的にセッションを追跡します。自動セッショントラッキングを無効にするには、プロジェクトの `config.xml` ファイル内の `platform` 要素に次の設定を追加します。

```xml
<platform name="android">
    <preference name="com.braze.android_disable_auto_session_tracking" value="true" />
</platform>
```

トラッキングセッションを再開するには、`BrazePlugin.startSessionTracking()` を呼び出します。次回の `Activity.onStart()` 以降に開始されたセッションのみが追跡されることに注意してください。
