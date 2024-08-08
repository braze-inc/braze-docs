---
nav_title: 高度な実装
article_title: 高度なSDK 実装
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "このリファレンス記事では、Unityプラットフォームの高度なSDK実装について説明します。"
---

# 高度な実装

> このリファレンス記事では、Unityプラットフォームの高度なSDK実装について説明します。

## Unityパッケージのカスタマイズ

提供されているスクリプトを使用して、Braze Unityパッケージをカスタマイズおよびエクスポートすることができます。

1. [Braze Unity SDK GitHub プロジェクト][1] をクローンします。

	```bash
	git clone git@github.com:braze-inc/braze-unity-sdk.git
	```
2. `braze-unity-sdk/scripts`ディレクトリから、`./generate_package.sh`を実行してUnityパッケージをエクスポートします。`generate_package.sh` の実行中はUnity を開いておく必要があります。
3. パッケージは`braze-unity-sdk/unity-package/` にエクスポートされます。
4. Unityエディタで、**Assets**> **Import Package**> **Custom Package**に移動して、希望するパッケージをUnityプロジェクトにインポートします。
5. (オプション)インポートしないファイルの選択を解除します。

`generate_package.sh`と`Assets/Editor/Build.cs`にあるエクスポートスクリプトの両方を編集することで、エクスポートされたUnityパッケージをカスタマイズできます。

## Prime 31の互換性

Prime31プラグインでBraze Unityプラグインを使用するには、プロジェクトの`AndroidManifest.xml`を編集してPrime31互換アクティビティクラスを使用します。すべての参照を変更する
`com.braze.unity.BrazeUnityPlayerActivity`から`com.braze.unity.prime31compatible.BrazeUnityPlayerActivity`

## Amazon ADM プッシュ

Brazeは、[Amazon ADMプッシュ][10]をUnityアプリに統合することをサポートしています。Amazon ADM プッシュを統合する場合は、ADM API キーを含む`api_key.txt` というファイルを作成し、`Plugins/Android/assets/` フォルダに配置します。 Amazon ADM とBraze の統合の詳細については、[ADM プッシュ統合命令][11] を参照してください。

## Android SDK の高度な実装オプション {#android-sdk-advanced}

### Unityエディタでの詳細なロギングの有効化
Unityエディタで詳細ログを有効にするには、次の手順を実行します。

1. **Braze**> **Braze Configuration** に移動して、Braze Configuration Settings を開きます。
2. **Show Braze Android Settings**ドロップダウンをクリックします。
3. **SDK Log Level**フィールドに、値"0"を入力します。

### Braze Unityプレーヤーの拡張(Android) {#extending-braze-unity-player}

`AndroidManifest.xml` ファイルの例では、[`BrazeUnityPlayerActivity`](https://github.com/braze-inc/braze-android-sdk/blob/e804cb3a10ae68364b354b52abf1bef8a0d1a9dc/android-sdk-unity/src/main/java/com/braze/unity/BrazeUnityPlayerActivity.kt) という1 つのActivity クラスが登録されています。このクラスは、Braze SDK と統合され、セッション処理、アプリ内メッセージ登録、プッシュ通知分析ロギングなどで`UnityPlayerActivity` を拡張します。`UnityPlayerActivity` クラスの拡張の詳細については、[Unity](https://docs.unity3d.com/Manual/AndroidUnityPlayerActivity.html) を参照してください。

ライブラリまたはプラグインプロジェクトで独自のカスタム`UnityPlayerActivity` を作成する場合は、`BrazeUnityPlayerActivity` を拡張してカスタム機能をBraze に統合する必要があります。`BrazeUnityPlayerActivity` の拡張作業を開始する前に、Braze をUnity プロジェクトに統合する手順に従ってください。
1. Braze Android SDK を依存関係としてライブラリまたはプラグインプロジェクトに追加します([Braze Android SDK 統合手順]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/) を参照)。
2. Unity固有の機能を含むUnity `.aar`を、Unity用に構築しているAndroidライブラリプロジェクトに統合します。`appboy-unity.aar` は、[public repo](https://github.com/braze-inc/braze-unity-sdk/tree/master/Assets/Plugins/Android) から入手できます。Unityライブラリが正常に統合されたら、`UnityPlayerActivity`を変更して`BrazeUnityPlayerActivity`を拡張します。
3. ライブラリまたはプラグインプロジェクトをエクスポートし、通常どおり`/<your-project>/Assets/Plugins/Android` にドロップします。Braze ソースコードは`/<your-project>/Assets/Plugins/Android` にすでに存在するため、ライブラリまたはプラグインには含めないでください。
4\.`/<your-project>/Assets/Plugins/Android/AndroidManifest.xml` を編集して、`BrazeUnityPlayerActivity` サブクラスをメインアクティビティとして指定します。

これで、Brazeと完全に統合され、カスタム`UnityPlayerActivity`機能を含むUnity IDEから`.apk`をパッケージ化できるようになります。

## iOS SDK の高度な実装オプション {#ios-sdk-advanced}

### Unityエディタでの詳細なロギングの有効化
Unityエディタで詳細ログを有効にするには、次の手順を実行します。

1. **Braze**> **Braze Configuration** に移動して、Braze Configuration Settings を開きます。
2. **Show Braze iOS Settings**ドロップダウンをクリックします。
3. **SDK Log Level**フィールドに、値"0"を入力します。

### SDK (iOS) の拡張

SDK の動作を拡張するには、[Braze Unity SDK GitHub プロジェクト](https://github.com/appboy/appboy-unity-sdk) をフォークして必要な変更を加えます。

変更したコードをUnityパッケージとしてパブリッシュするには、[高度なユースケース]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/advanced_use_cases/)を参照してください。

### 手動から自動統合(iOS)への移行

Braze Unity SDK で提供されている自動iOS 統合を活用するには、手動から自動統合に移行するときに次の手順を実行します。

1. Xcode プロジェクトの`UnityAppController` サブクラスからすべての Braze 関連コードを削除します。
2. UnityまたはXcodeプロジェクトから Braze iOSライブラリ(`Appboy_iOS_SDK.framework`や`SDWebImage.framework`など)を削除し、[ Braze Unityパッケージ](#step-1-importing-the-braze-unity-package)をUnityプロジェクトにインポートします。
3. [ Unity](#step-2-setting-your-api-key) を使用してAPI キーを設定するには、[ の統合手順に従ってください。

[1]: https://github.com/appboy/appboy-unity-sdk
[10]: https://developer.amazon.com/public/apis/engage/device-messaging
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/adm_push_notifications/
