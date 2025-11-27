{% multi_lang_include developer_guide/prerequisites/unreal_engine.md %}

## プッシュ通知の設定

### ステップ 1: プロジェクトを設定する

{% tabs %}
{% tab Android %}
最初に、FirebaseをAndroidプロジェクトに追加します。手順については、Googleの[Firebaseセットアップガイド](https://firebase.google.com/docs/android/setup)を参照してください。
{% endtab %}

{% tab iOS %}
{% multi_lang_include developer_guide/swift/apns_token.md %}
{% endtab %}
{% endtabs %}

### ステップ 2: プッシュ通知を有効にする

{% tabs %}
{% tab Android %}
プロジェクトの`engine.ini` 。[Firebaseプロジェクトでは、](https://firebase.google.com/docs/cloud-messaging/concept-options#credentials) `YOUR_SEND_ID` を[送信者IDに置き換えて](https://firebase.google.com/docs/cloud-messaging/concept-options#credentials)おくこと。

```ini
bEnableFirebaseCloudMessagingSupport=true
bIsFirebaseCloudMessagingRegistrationEnabled=true
FirebaseCloudMessagingSenderIdKey=YOUR_SENDER_ID
```

と同じディレクトリ内に [BrazeUPLAndroid.xml](./BrazeSample/Plugins/Braze/Source/Braze/BrazeUPLAndroid.xml)と同じディレクトリ内に、`AndroidCopies` という名前の新しいディレクトリを作成し、そこに`google-services.json` ファイルを追加する。
{% endtab %}

{% tab iOS %}
プロジェクトで、**設定**＞**プロジェクト設定**＞**iOS**＞**オンラインと**進み、**イネーブルメント・サポートを有効にするを**チェックする。終了したら、プロビジョンのプッシュ機能がイネーブルメントになっていることを確認する。

{% alert important %}
iOS用のプッシュ機能をイネーブルメントするには、プロジェクトがソースからビルドされていなければならない。詳細については、[Unreal Engine を参照のこと：ソースからのビルド](https://dev.epicgames.com/documentation/en-us/unreal-engine/building-unreal-engine-from-source).
{% endalert %}
{% endtab %}
{% endtabs %}

## オプション構成

{% tabs %}
{% tab Android %}
#### 大小のアイコンを設定する

[大小の通知アイコンを]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android&tab=android#configure-icons)設定する：

1. `AndroidCopies/res` フォルダの内部で、適切な drawable フォルダ（デフォルトでは`drawable` ） にアイコンを追加する。
2. `AndroidCopies/res/values` フォルダーに`braze.xml` を追加し、アイコンを設定する。非常に基本的なbraze.xml ：
    ```xml
    <?xml version="1.0" encoding="utf-8"?>
    <resources>
        <drawable name="com_braze_push_small_notification_icon">@drawable/notification_small_icon</drawable>
        <drawable name="com_braze_push_large_notification_icon">@drawable/notification_large_icon</drawable>
    </resources>
    ```

{% alert note %}
`AndroidCopies` フォルダーのファイルは、`BrazeUPLAndroid.xml` で定義されているように、生成されたAndroidプロジェクト構造にコピーされる。
{% endalert %}
{% endtab %}

{% tab iOS %}
#### 遠隔地からの打ち上げ通知

Unreal Engine バージョン 4.25.3 の時点で、UE4 はアプリケーションの初期起動を引き起こすリモート通知を受信するための適切なサポートを欠いている。この通知の受信をサポートするために、UE4用とBraze SDKプラグイン用の2つのgitパッチを作成した。

1. UE4 Engine`Source` ディレクトリで、git patch`UE4_Engine-Cache-Launch-Remote-Notification.patch` を適用する。
2. Braze Unreal SDKディレクトリで、gitパッチ`Braze_SDK-Read-Cached-Remote-Launch-Notification.patch` を適用する。
{% endtab %}
{% endtabs %}
