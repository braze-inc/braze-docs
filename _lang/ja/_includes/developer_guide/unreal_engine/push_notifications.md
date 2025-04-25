{% multi_lang_include developer_guide/prerequisites/unreal_engine.md %}

## プッシュ通知の設定

### ステップ1:プロジェクトを設定する

{% tabs %}
{% tab Android %}
最初に、FirebaseをAndroidプロジェクトに追加します。手順については、Googleの[Firebaseセットアップガイド](https://firebase.google.com/docs/android/setup)を参照してください。
{% endtab %}

{% tab iOS %}
{% multi_lang_include developer_guide/swift/apns_token.md %}
{% endtab %}
{% endtabs %}

### ステップ2:プッシュ通知を有効にする

{% tabs %}
{% tab Android %}
プロジェクトの`engine.ini` ファイルに次の行を追加します。`YOUR_SEND_ID` は必ずFirebase プロジェクト の[送信者ID に置き換えてください。

```ini
bEnableFirebaseCloudMessagingSupport=true
bIsFirebaseCloudMessagingRegistrationEnabled=true
FirebaseCloudMessagingSenderIdKey=YOUR_SENDER_ID
```

[BrazeUPLAndroid.xml](./BrazeSample/Plugins/Braze/Source/Braze/BrazeUPLAndroid.xml) と同じディレクトリ内に`AndroidCopies` という名前の新しいディレクトリを作成し、`google-services.json` ファイルを追加します。
{% endtab %}

{% tab iOS %}
プロジェクトで、**Settings** > **Project Settings** > **iOS** > **Online**に移動し、**Enable Remote Notifications Support**完了したら、プロビジョニングでプッシュ機能が有効になっていることを確認します。

{% alert important %}
iOS のプッシュ機能を有効にするには、プロジェクトがソースから構築されている必要があります。詳細については、[Unreal Engine を参照してください。source](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-unreal-engine-from-source)からビルドします。
{% endalert %}
{% endtab %}
{% endtabs %}

## オプション構成

{% tabs %}
{% tab Android %}
#### 大小のアイコンを設定する

[小規模かつ大規模な通知アイコン]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android&tab=android#configure-icons)を設定するには:

1. `AndroidCopies/res` フォルダ内の適切な描画可能フォルダ(デフォルトでは`drawable`) にアイコンを追加します。
2. `braze.xml` を`AndroidCopies/res/values` フォルダに追加してアイコンを設定します。非常に基本的なbraze.xml ファイル:
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <drawable name="com_braze_push_small_notification_icon">@drawable/notification_small_icon</drawable>
        <drawable name="com_braze_push_large_notification_icon">@drawable/notification_large_icon</drawable>
    </resources>
    ```

{% alert note %}
`AndroidCopies` フォルダのファイルは、`BrazeUPLAndroid.xml` で定義されたように、生成されたAndroid プロジェクト構造にコピーされます。
{% endalert %}
{% endtab %}

{% tab iOS %}
#### リモート起動通知

Unreal Engine バージョン4.25.3 では、UE4 はアプリケーションの初期起動を引き起こすリモート通知を受信するための適切なサポートを欠いています。この通知の受信をサポートするために、2 つのgit パッチ(UE4 用とBraze SDK プラグイン用) を作成しました。

1. UE4 Engine `Source` ディレクトリで、git パッチ`UE4_Engine-Cache-Launch-Remote-Notification.patch` を適用します。
2. Braze Unreal SDK ディレクトリで、git パッチ`Braze_SDK-Read-Cached-Remote-Launch-Notification.patch` を適用します。
{% endtab %}
{% endtabs %}
