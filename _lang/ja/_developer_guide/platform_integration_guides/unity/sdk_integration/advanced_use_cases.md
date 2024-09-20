---
nav_title: 高度な実装
article_title: 高度なSDKの実装
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "このリファレンス記事では、Unityプラットフォーム向けの高度なSDK実装について説明する。"
---

# 高度な実装

> このリファレンス記事では、Unityプラットフォーム向けの高度なSDK実装について説明する。

## Unityパッケージをカスタマイズする

提供されるスクリプトを使用して、Braze Unityパッケージをカスタマイズしてエクスポートすることもできる。

1. [Braze Unity SDK GitHubプロジェクトを][1]クローンする：

	```bash
	git clone git@github.com:braze-inc/braze-unity-sdk.git
	```
2. `braze-unity-sdk/scripts` ディレクトリから、`./generate_package.sh` を実行し、Unity パッケージをエクスポートする。`generate_package.sh` を実行している間は、Unityを開いておく必要がある。
3. パッケージは`braze-unity-sdk/unity-package/` にエクスポートされる。
4. Unityエディターで、**Assets**>**Import Package**>**Custom Packageと**進み、目的のパッケージをUnityプロジェクトにインポートする。
5. (オプション）インポートしたくないファイルの選択を解除する。

`generate_package.sh` と`Assets/Editor/Build.cs` にあるエクスポートスクリプトの両方を編集することで、エクスポートされたUnityパッケージをカスタマイズできる。

## プライム31との互換性

Prime31プラグインでBraze Unityプラグインを使用するには、プロジェクトの`AndroidManifest.xml` 、Prime31互換のActivityクラスを使用するように編集する。の参照をすべて変更する。
`com.braze.unity.BrazeUnityPlayerActivity` への `com.braze.unity.prime31compatible.BrazeUnityPlayerActivity`

## アマゾンADMプッシュ

Brazeは、[Amazon ADMプッシュを][10]Unityアプリに統合することをサポートしている。Amazon ADMプッシュを統合したい場合は、ADM APIキーを含む`api_key.txt` というファイルを作成し、`Plugins/Android/assets/` フォルダに置く。 Amazon ADMとBrazeの統合の詳細については、[ADMプッシュ統合手順を][11]参照のこと。

## Android SDKの高度な実装オプション {#android-sdk-advanced}

### Unityエディタで冗長ロギングを有効にする
Unityエディターで冗長ロギングを有効にするには、以下のようにする：

1. **Braze**>**Braze Configurationに**移動して、Braze Configuration Settingsを開く。
2. **Show Braze Android Settings**ドロップダウンをクリックする。
3. **SDK Log Level**フィールドに値 "0 "を入力する。

### Braze Unityプレーヤーを拡張する（Android） {#extending-braze-unity-player}

`AndroidManifest.xml` 、アクティビティ・クラスが1つ登録されている、 [`BrazeUnityPlayerActivity`](https://github.com/braze-inc/braze-android-sdk/blob/e804cb3a10ae68364b354b52abf1bef8a0d1a9dc/android-sdk-unity/src/main/java/com/braze/unity/BrazeUnityPlayerActivity.kt).このクラスは、Braze SDKと統合され、セッション処理、アプリ内メッセージ登録、プッシュ通知分析ロギングなどで`UnityPlayerActivity` 。`UnityPlayerActivity` クラスの拡張については[Unityを](https://docs.unity3d.com/Manual/AndroidUnityPlayerActivity.html)参照のこと。

ライブラリやプラグインプロジェクトで独自のカスタム`UnityPlayerActivity` を作成する場合は、カスタム機能をBrazeと統合するために、当社の`BrazeUnityPlayerActivity` を拡張する必要がある。`BrazeUnityPlayerActivity` を拡張する作業を始める前に、UnityプロジェクトにBrazeを統合するための説明に従ってほしい。
1. Braze Android[SDK統合の説明に従って]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/)、Braze Android SDKをライブラリまたはプラグインプロジェクトに依存関係として追加する。
2. Unity固有の機能を含むUnity`.aar` を、Unity用にビルドしているAndroidライブラリ・プロジェクトに統合する。`appboy-unity.aar` は我々の[公開レポから](https://github.com/braze-inc/braze-unity-sdk/tree/master/Assets/Plugins/Android)入手できる。Unityライブラリがうまく統合されたら、`UnityPlayerActivity` を修正して、`BrazeUnityPlayerActivity` を拡張する。
3. ライブラリまたはプラグインプロジェクトをエクスポートし、通常通り`/<your-project>/Assets/Plugins/Android` 。ライブラリやプラグインにBrazeのソースコードを含めないこと。それらはすでに`/<your-project>/Assets/Plugins/Android` に存在するからである。
4. `/<your-project>/Assets/Plugins/Android/AndroidManifest.xml` を編集し、`BrazeUnityPlayerActivity` のサブクラスをメイン・アクティビティとして指定する。

これでUnity IDEから、Brazeと完全に統合され、カスタム`UnityPlayerActivity` 機能を含む`.apk` をパッケージできるようになるはずだ。

## iOS SDKの高度な実装オプション {#ios-sdk-advanced}

### Unityエディタで冗長ロギングを有効にする
Unityエディターで冗長ロギングを有効にするには、以下のようにする：

1. **Braze**>**Braze Configurationに**移動して、Braze Configuration Settingsを開く。
2. **Show Braze iOS Settings**ドロップダウンをクリックする。
3. **SDK Log Level**フィールドに値 "0 "を入力する。

### SDKを拡張する（iOS）

SDKの動作を拡張するには、[Braze Unity SDK GitHubプロジェクトを](https://github.com/appboy/appboy-unity-sdk)フォークし、必要な変更を加える。

修正したコードをUnityパッケージとして公開するには、[Advanced use casesを]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/advanced_use_cases/)参照のこと。

### 手動から自動統合への移行（iOS）

Braze Unity SDKで提供される自動化されたiOSインテグレーションを利用するには、手動から自動化されたインテグレーションに移行するための以下のステップに従う。

1. Xcodeプロジェクトの`UnityAppController` サブクラスから、Braze関連のコードをすべて削除する。
2. UnityまたはXcodeプロジェクトからBraze iOSライブラリ（`Appboy_iOS_SDK.framework` 、`SDWebImage.framework` など）を削除し、[Braze Unityパッケージを](#step-1-importing-the-braze-unity-package)Unityプロジェクトに[インポートする](#step-1-importing-the-braze-unity-package)。
3. [Unityを通してAPIキーを設定](#step-2-setting-your-api-key)するための統合の指示に従う。

[1]: https://github.com/appboy/appboy-unity-sdk
[10]: https://developer.amazon.com/public/apis/engage/device-messaging
[11]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/adm_push_notifications/
