## Cordova SDKの統合

### 前提条件

起動する前に、[最新のBraze Cordova SDKバージョン](https://github.com/braze-inc/braze-cordova-sdk?tab=readme-ov-file#minimum-version-requirements)でサポートされていることを確認します。

### ステップ 1: SDK をプロジェクトに追加する

{% alert warning %}
以下の方法を使用して、Braze Cordova SDKのみを追加します。他の方法でインストールしないでください。セキュリティ違反が発生する可能性があります。
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
このステップを繰り返すことで、`master` と`geofence-branch` をいつでも切り替えるできます。
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

次の項では、iOS またはAndroid でCordova を使用する場合のプラットフォーム固有のシンタックスについて説明します。

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
| メソッド                                         | 説明                                                                                                                                            |

|                                       | アプリケーションの API キーを設定します。 |
|                          | アプリケーションの SDK エンドポイントを設定します。 |
|       | 自動プッシュ登録を無効にするかどうかを設定します。 |
|           | 自動プッシュ処理を無効にするかどうかを設定します。 |
|          | Braze SDK が IDFA 情報を自動的に収集するかどうかを設定します。詳細については、[Braze IDFAメソッドのドキュメント](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforadvertiser:)/)を参照してください。|
|                    | 自動位置情報収集を有効にするかどうかを設定します (ユーザーが許可した場合)。 |この
|                             | ジオフェンスを有効にするかどうかを設定します。 |
|               | アプリケーションの Braze セッションタイムアウトを秒単位で設定します。デフォルトは 10 秒です。 |
|                    | SDK 認証機能を有効にするかどうかを設定します。 |
|         | アプリケーションがフォアグラウンドにあるときにプッシュ通知を表示するかどうかを設定します。 |
|  |  を無効にする必要があるかどうかを設定します。 |
|  | トリガー間の最小時間間隔を秒単位で設定します。デフォルトは 10 秒です。 |
| | iOS プッシュ拡張機能のアプリグループ ID を設定します。 |
| | SDK がユニバーサルリンクを自動的に認識してシステムメソッドに転送するかどうかを設定します。 |
| |  の最小ログレベルを設定します。 |
| | ランダムに生成された UUID をデバイス ID として使用するかどうかを設定します。 |
| | 自動データフラッシュの間隔を秒単位で設定します。デフォルトは 10 秒です。 |
| |  のリクエストポリシーを自動にするか手動にするかを設定します。 |
| | プッシュ権限が承認されたときに、ユーザーの通知サブスクリプション状態を自動的に  に設定するかどうかを設定します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert tip %}
詳細については、[GitHub:Braze iOS Cordova プラグイン](https://github.com/braze-inc/braze-cordova-sdk/blob/master/src/ios/BrazePlugin.m)を参照してください。
{% endalert %}
{% endtab %}

{% tab android %}
| メソッド                                         | 説明                                                                                                                                            |

|                                       | アプリケーションの API キーを設定します。 |
|                          | アプリケーションの SDK エンドポイントを設定します。 |
|               | 通知の小さいアイコンを設定します。 |
|               | 通知の大きいアイコンを設定します。 |
|             | 通知のアクセントカラーを 16 進数で設定します。 |
|               | アプリケーションの Braze セッションタイムアウトを秒単位で設定します。デフォルトは 10 秒です。 |
|  | Braze SDK がプッシュディープリンクを自動的に処理するかどうかを設定します。 |
|                             | アプリケーションのログレベルを設定します。デフォルトのログレベルは 4 で、最小限の情報をロギングします。デバッグのために詳細ロギングを有効にするには、ログレベル 2 を使用します。|
| | プッシュ通知に Firebase Cloud Messaging を使用するかどうかを設定します。 |
|                         | Firebase Cloud Messaging の送信者 ID を設定します。 |
|                    | 自動位置情報収集を有効にするかどうかを設定します (ユーザーが許可した場合)。 |
|                             | ジオフェンスを有効にするかどうかを設定します。 |
| `android_disable_auto_session_tracking` | Android Cordova プラグインを自動的に"トラッキング セッション s から無効にします。詳細については、[自動セッション "トラッキングの無効化](#cordova_disable-automatic-session-tracking) |を参照してください。
|                    | SDK 認証機能を有効にするかどうかを設定します。 |
|  | トリガー間の最小時間間隔を秒単位で設定します。デフォルトは 10 秒です。 |
|        | セッションのタイムアウト動作がセッション開始イベントまたはセッション終了イベントのどちらに基づくかを設定します。 |
|             | Braze のデフォルト  の  経由で表示されるユーザー向けの名前を設定します。 |
|      | Braze のデフォルト  の  経由で表示されるユーザー向けの説明を設定します。 |
|              | プッシュ通知ストーリーをクリックしたときに自動的に閉じるかどうかを設定します。 |
| | フォールバック Firebase Cloud Messaging Service の使用を有効にするかどうかを設定します。 |
| | フォールバック Firebase Cloud Messaging Service のクラスパスを設定します。 |
| | コンテンツ カードの未読視覚表示バーを有効にするかどうかを設定します。 |
| | Braze SDK が  にトークンを自動的に登録するかどうかを設定します。 |
| | Braze がディープリンクを自動的にたどってプッシュするときにアクティビティをバックスタックに追加するかどうかを設定します。 |
| | Braze がディープリンクを自動的にたどってプッシュするときにバックスタックに追加するアクティビティを設定します。 |
| | プッシュが承認されたときに Braze がユーザーを自動的にオプトインするかどうかを設定します。 |
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

## 自動セッショントラッキングの無効化 (Android のみ)

デフォルトでは、Android Cordova プラグインは自動的にセッションを追跡します。自動セッショントラッキングを無効にするには、プロジェクトの `config.xml` ファイル内の `platform` 要素に次の設定を追加します。

```xml
<platform name="android">
    <preference name="com.braze.android_disable_auto_session_tracking" value="true" />
</platform>
```

トラッキングセッションを再開するには、`BrazePlugin.startSessionTracking()` を呼び出します。次回の `Activity.onStart()` 以降に開始されたセッションのみが追跡されることに注意してください。
