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

提供されているスクリプトを使用して、Braze Unity パッケージをカスタマイズしてエクスポートすることもできます。

1. [Braze Unity SDK GitHub プロジェクト](https://github.com/appboy/appboy-unity-sdk)を複製します。

	```bash
	git clone git@github.com:braze-inc/braze-unity-sdk.git
	```
2. `braze-unity-sdk/scripts` ディレクトリから、`./generate_package.sh` を実行し、Unity パッケージをエクスポートする。`generate_package.sh` を実行している間は、Unity を開いておく必要があります。
3. パッケージは`braze-unity-sdk/unity-package/` にエクスポートされる。
4. Unity エディターで Unity プロジェクトに任意のパッケージをインポートするには、[**アセット**] > [**パッケージをインポート**] > [**カスタムパッケージ**] の順に移動します。
5. (オプション）インポートしたくないファイルの選択を解除する。

`generate_package.sh` と`Assets/Editor/Build.cs` にあるエクスポートスクリプトの両方を編集することで、エクスポートされたUnityパッケージをカスタマイズできる。

## Prime 31 の互換性

Prime31 プラグインで Braze Unity プラグインを使用するには、Prime31 互換の Activity クラスを使用するようにプロジェクトの `AndroidManifest.xml` を編集します。の参照をすべて変更する。
`com.braze.unity.BrazeUnityPlayerActivity` のすべての参照を `com.braze.unity.prime31compatible.BrazeUnityPlayerActivity` に変更します

## Amazon ADM プッシュ

Braze では、Unity アプリへの [Amazon ADM プッシュ](https://developer.amazon.com/public/apis/engage/device-messaging)の統合がサポートされています。Amazon ADMプッシュを統合したい場合は、ADM APIキーを含む`api_key.txt` というファイルを作成し、`Plugins/Android/assets/` フォルダに置く。 Amazon ADM と Braze の統合の詳細については、[ADM プッシュ統合手順]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/adm_push_notifications/)を参照してください。

## Android SDKの高度な実装オプション {#android-sdk-advanced}

### Unityエディタで冗長ロギングを有効にする
Unityエディターで冗長ロギングを有効にするには、以下のようにする：

1. [**Braze**] > [**Braze 構成**] の順に移動して、[Braze 構成設定] を開きます。
2. [**Braze Android 設定を表示する**] ドロップダウンをクリックします。
3. [**SDK ログレベル**] フィールドに値「0」を入力します。

### Braze Unity プレーヤーを拡張する （Android） {#extending-braze-unity-player}

提供されている `AndroidManifest.xml` ファイルの例では、1つの Activity クラス [`BrazeUnityPlayerActivity`](https://github.com/braze-inc/braze-android-sdk/blob/e804cb3a10ae68364b354b52abf1bef8a0d1a9dc/android-sdk-unity/src/main/java/com/braze/unity/BrazeUnityPlayerActivity.kt) が登録されています。このクラスは Braze SDK と統合され、セッション処理、アプリ内メッセージ登録、プッシュ通知分析ログなどを使用して `UnityPlayerActivity` を拡張します。`UnityPlayerActivity` クラスの拡張の詳細については、「[Unity](https://docs.unity3d.com/Manual/AndroidUnityPlayerActivity.html)」を参照してください。

ライブラリやプラグインプロジェクトで独自のカスタム`UnityPlayerActivity` を作成する場合は、カスタム機能をBrazeと統合するために、当社の`BrazeUnityPlayerActivity` を拡張する必要がある。`BrazeUnityPlayerActivity` を拡張する作業を始める前に、Unity プロジェクトに Braze を統合するための手順に従ってください。
1. [Braze Android SDK統合の説明]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/)に従って、Braze Android SDK をライブラリまたはプラグインプロジェクトに依存関係として追加します。
2. Unity 固有の機能を含む Unity `.aar` を、Unity 用に構築している Android ライブラリプロジェクトに統合します。`appboy-unity.aar` は、[公開リポジトリ](https://github.com/braze-inc/braze-unity-sdk/tree/master/Assets/Plugins/Android)から入手できます。Unity ライブラリがうまく統合されたら、`BrazeUnityPlayerActivity` を拡張するように `UnityPlayerActivity` を変更します。
3. ライブラリまたはプラグインプロジェクトをエクスポートし、通常どおり `/<your-project>/Assets/Plugins/Android` にドロップします。ライブラリやプラグインにBrazeのソースコードを含めないこと。それらはすでに`/<your-project>/Assets/Plugins/Android` に存在するからである。
4. `/<your-project>/Assets/Plugins/Android/AndroidManifest.xml` を編集し、`BrazeUnityPlayerActivity` のサブクラスをメイン・アクティビティとして指定する。

これでUnity IDEから、Brazeと完全に統合され、カスタム`UnityPlayerActivity` 機能を含む`.apk` をパッケージできるようになるはずだ。

## iOS SDKの高度な実装オプション {#ios-sdk-advanced}

### Unityエディタで冗長ロギングを有効にする
Unityエディターで冗長ロギングを有効にするには、以下のようにする：

1. [**Braze**] > [**Braze 構成**] の順に移動して、[Braze 構成設定] を開きます。
2. **Show Braze iOS Settings**ドロップダウンをクリックする。
3. [**SDK ログレベル**] フィールドに値「0」を入力します。

### SDKを拡張する（iOS）

SDK の動作を拡張するには、[Braze Unity SDK GitHubプロジェクト](https://github.com/appboy/appboy-unity-sdk)をフォークし、必要な変更を行います。

修正したコードを Unity パッケージとして公開するには、[高度なユースケース]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/advanced_use_cases/)を参照してください。

### 手動から自動統合への移行（iOS）

Braze Unity SDKで提供される自動化されたiOSインテグレーションを利用するには、手動から自動化されたインテグレーションに移行するための以下のステップに従う。

1. Xcodeプロジェクトの`UnityAppController` サブクラスから、Braze関連のコードをすべて削除する。
2. Unity プロジェクトまたは Xcode プロジェクト (`Appboy_iOS_SDK.framework` および `SDWebImage.framework` など) から Braze iOS ライブラリを削除し、[Braze Unity パッケージを Unity プロジェクトにインポート](#step-1-importing-the-braze-unity-package)します。
3. [Unity で API キーを設定する](#step-2-setting-your-api-key)統合手順に従います。

