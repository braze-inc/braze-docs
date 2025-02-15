---
nav_title: カスタマイズ
article_title: Cordova Braze SDK のカスタマイズ
page_order: 1
---

# Cordova Braze SDK のカスタマイズ

> これらは、Cordova Braze SDK で利用可能なカスタマイズです。

{% multi_lang_include cordova/prerequisites.md %}

## カスタマイズオプション

次の設定をプロジェクトの `config.xml` ファイルの `platform` 要素に追加できます。

{% tabs %}
{% tab ios %}
| メソッド                                         | 説明                                                                                                                                            |
| -----------------------------------------------| -------------------------------------------------------------------------------------------------------------------------------------------------------|
| `api_key`                                      | アプリケーションの API キーを設定します。 |
| `ios_api_endpoint`                             | アプリケーションの [SDK エンドポイント]({{site.baseurl}}/api/basics/#endpoints)を設定します。 |
| `ios_disable_automatic_push_registration`      | 自動プッシュ登録を無効にするかどうかを設定します。 |
| `ios_disable_automatic_push_handling`          | 自動プッシュ処理を無効にするかどうかを設定します。 |
| `ios_enable_idfa_automatic_collection`         | Braze SDK が IDFA 情報を自動的に収集するかどうかを設定します。詳細については、[Braze の IDFA メソッドのドキュメント](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/)を参照してください。 |
| `enable_location_collection`                   | 自動位置情報収集を有効にするかどうかを設定します (ユーザーが許可した場合)。`geofence-branch`  |
| `geofences_enabled`                            | ジオフェンスを有効にするかどうかを設定します。 |
| `ios_session_timeout`                          | アプリケーションの Braze セッションタイムアウトを秒単位で設定します。デフォルトは 10 です。 |
| `sdk_authentication_enabled`                   | [SDK 認証](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication)機能を有効にするかどうかを設定します。 |
| `display_foreground_push_notifications`        | アプリケーションがフォアグラウンドにあるときにプッシュ通知を表示するかどうかを設定します。 |
| `ios_disable_un_authorization_option_provisional` | `UNAuthorizationOptionProvisional` を無効にする必要があるかどうかを設定します。 |
| `trigger_action_minimum_time_interval_seconds` | トリガー間の最小時間間隔を秒単位で設定します。デフォルトは 30 秒です。 |
| `ios_push_app_group`| iOS プッシュ拡張機能のアプリグループ ID を設定します。 |
| `ios_forward_universal_links`| SDK がユニバーサルリンクを自動的に認識してシステムメソッドに転送するかどうかを設定します。 |
| `ios_log_level`| `Braze.Configuration.Logger` の最小ログレベルを設定します。 |
| `ios_use_uuid_as_device_id`| ランダムに生成された UUID をデバイス ID として使用するかどうかを設定します。 |
| `ios_flush_interval_seconds`| 自動データフラッシュの間隔を秒単位で設定します。デフォルトは 10 秒です。 |
| `ios_use_automatic_request_policy`| `Braze.Configuration.Api` のリクエストポリシーを自動にするか手動にするかを設定します。 |
| `should_opt_in_when_push_authorized`| プッシュ権限が承認されたときに、ユーザーの通知サブスクリプション状態を自動的に `optedIn` に設定するかどうかを設定します。 |

{% alert tip %}
詳細については、[GitHub:Braze iOS Cordova プラグイン](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/ios/BrazePlugin.m)を参照してください。
{% endalert %}
{% endtab %}

{% tab Android %}
| メソッド                                         | 説明                                                                                                                                            |
| -----------------------------------------------| -------------------------------------------------------------------------------------------------------------------------------------------------------|
| `api_key`                                      | アプリケーションの API キーを設定します。 |
| `android_api_endpoint`                         | アプリケーションの [SDK エンドポイント]({{site.baseurl}}/api/basics/#endpoints)を設定します。 |
| `android_small_notification_icon`              | 通知の小さいアイコンを設定します。 |
| `android_large_notification_icon`              | 通知の大きいアイコンを設定します。 |
| `android_notification_accent_color`            | 通知のアクセントカラーを 16 進数で設定します。 |
| `android_default_session_timeout`              | アプリケーションの Braze セッションタイムアウトを秒単位で設定します。デフォルトは 10 秒です。 |
| `android_handle_push_deep_links_automatically` | Braze SDK がプッシュディープリンクを自動的に処理するかどうかを設定します。 |
| `android_log_level`                            | アプリケーションのログレベルを設定します。デフォルトのログレベルは 4 で、最小限の情報をロギングします。デバッグのために詳細ロギングを有効にするには、ログレベル 2 を使用します。|
| `firebase_cloud_messaging_registration_enabled`| プッシュ通知に Firebase Cloud Messaging を使用するかどうかを設定します。 |
| `android_fcm_sender_id`                        | Firebase Cloud Messaging の送信者 ID を設定します。 |
| `enable_location_collection`                   | 自動位置情報収集を有効にするかどうかを設定します (ユーザーが許可した場合)。 |
| `geofences_enabled`                            | ジオフェンスを有効にするかどうかを設定します。 |
| `android_disable_auto_session_tracking`        | Android Cordova プラグインによるセッションの自動追跡を無効にするかどうかを設定します。 |
| `sdk_authentication_enabled`                   | [SDK 認証](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication#sdk-authentication)機能を有効にするかどうかを設定します。 |
| `trigger_action_minimum_time_interval_seconds` | トリガー間の最小時間間隔を秒単位で設定します。デフォルトは 30 秒です。 |
| `is_session_start_based_timeout_enabled`       | セッションのタイムアウト動作がセッション開始イベントまたはセッション終了イベントのどちらに基づくかを設定します。 |
| `default_notification_channel_name`            | Braze のデフォルト `NotificationChannel` の `NotificationChannel.getName` 経由で表示されるユーザー向けの名前を設定します。 |
| `default_notification_channel_description`     | Braze のデフォルト `NotificationChannel` の `NotificationChannel.getDescription` 経由で表示されるユーザー向けの説明を設定します。 |
| `does_push_story_dismiss_on_click`             | プッシュ通知ストーリーをクリックしたときに自動的に閉じるかどうかを設定します。 |
| `is_fallback_firebase_messaging_service_enabled`| フォールバック Firebase Cloud Messaging Service の使用を有効にするかどうかを設定します。 |
| `fallback_firebase_messaging_service_classpath`| フォールバック Firebase Cloud Messaging Service のクラスパスを設定します。 |
| `is_content_cards_unread_visual_indicator_enabled`| コンテンツ カードの未読視覚表示バーを有効にするかどうかを設定します。 |
| `is_firebase_messaging_service_on_new_token_registration_enabled`| Braze SDK が `com.google.firebase.messaging.FirebaseMessagingService.onNewToken` にトークンを自動的に登録するかどうかを設定します。 |
| `is_push_deep_link_back_stack_activity_enabled`| Braze がディープリンクを自動的にたどってプッシュするときにアクティビティをバックスタックに追加するかどうかを設定します。 |
| `push_deep_link_back_stack_activity_class_name`| Braze がディープリンクを自動的にたどってプッシュするときにバックスタックに追加するアクティビティを設定します。 |
| `should_opt_in_when_push_authorized`| プッシュが承認されたときに Braze がユーザーを自動的にオプトインするかどうかを設定します。 |

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

{% tab Android %}
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

## プラットフォーム固有の構文

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

{% tab Android %}
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

{% tab Android %}
ブール値の設定は、次の例のように、`true` および `false` キーワードを文字列表現として使用して SDK によって読み取られます。

```xml
<platform name="android">
    <preference name="com.braze.should_opt_in_when_push_authorized" value="true" />
    <preference name="com.braze.is_session_start_based_timeout_enabled" value="false" />
</platform>
```
{% endtab %}
{% endtabs %}
