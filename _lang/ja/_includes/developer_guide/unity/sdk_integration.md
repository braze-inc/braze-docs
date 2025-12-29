## Unity Braze SDKについて

型、関数、変数などの完全なリストについては、[Unity宣言ファイルを](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs)参照のこと。さらに、すでにUnityをiOS用に手動で統合している場合は、代わりに[自動統合に切り替える](#unity_automated-integration)ことができる。

## Unity SDKを統合する

### 前提条件

開始する前に、お使いの環境が[最新のBraze Unity SDKバージョンで](https://github.com/braze-inc/braze-unity-sdk/releases)サポートされていることを確認する。

### ステップ 1: Braze Unity パッケージの選択

{% tabs %}
{% tab Android %}
Braze [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) は、Android プラットフォームと iOS プラットフォーム向けのネイティブバインディングを C# インターフェイスとともにバンドルします。

[Braze Unity リリースページ](https://github.com/Appboy/appboy-unity-sdk/releases)でいくつかの Braze Unity パッケージをダウンロードできます。
 
- `Appboy.unitypackage`
    - このパッケージは、Braze Android および iOS SDK と、iOS SDK の [SDWebImage](https://github.com/SDWebImage/SDWebImage) 依存関係をバンドルします。これは、Braze アプリ内メッセージングと、iOS 上のコンテンツカード機能を適切に機能させるために必要です。SDWebImage フレームワークは、GIF を含む画像のダウンロードと表示に使用されます。完全なBraze機能を使用する場合は、このパッケージを読み込むしてインポートします。
- `Appboy-nodeps.unitypackage`
    - このパッケージは `Appboy.unitypackage` に似ていますが、[SDWebImage](https://github.com/SDWebImage/SDWebImage) フレームワークが存在しない点が異なります。このパッケージは、iOS アプリに SDWebImage フレームワークが存在しないようにする場合に便利です。

{% alert note %}
Unity 2.6.0 以降、バンドルされた Braze Android SDK アーティファクトには [AndroidX](https://developer.android.com/jetpack/androidx) 依存関係が必要です。以前に`jetified unitypackage` を使用していた場合は、対応する`unitypackage` に安全に移行できます。
{% endalert %}
{% endtab %}

{% tab Swift %}
Braze [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) は、Android プラットフォームと iOS プラットフォーム向けのネイティブバインディングを C# インターフェイスとともにバンドルします。

Braze Unity パッケージは、次の2種類の統合オプションを使用して、[Braze Unity リリースページ](https://github.com/Appboy/appboy-unity-sdk/releases)でダウンロードできます。

1. `Appboy.unitypackage` のみ
  - このパッケージは、Braze Android と iOS SDK を追加の依存関係なしでバンドルします。この統合方法では、Braze アプリ内メッセージングと、iOS 上のコンテンツカード機能が適切に機能しません。カスタムコードなしで完全なBraze機能を使用する場合は、代わりに以下のオプションを使用してください。
  - この統合オプションを使用する場合は、[Braze 構成] の下にある Unity UI で `Import SDWebImage dependency` の横にあるボックスに*チェックマークが入れられていない*ことを確認してください。
2. `SDWebImage` を含む `Appboy.unitypackage`
  - この統合オプションは、Braze Android および iOS SDK と、iOS SDK の [SDWebImage](https://github.com/SDWebImage/SDWebImage) 依存関係をバンドルします。これは、Braze アプリ内メッセージングと、iOS 上のコンテンツカード機能を適切に機能させるために必要です。`SDWebImage` フレームワークは、GIF を含む画像のダウンロードと表示に使用されます。完全なBraze機能を使用する場合は、このパッケージを読み込むしてインポートします。
  - `SDWebImage` を自動的にインポートするには、[Braze 構成] の下にある Unity UIで `Import SDWebImage dependency` の横にあるボックスに*チェックマークが入れられている*ことを確認してください。

{% alert note %}
iOSプロジェクトに[SDWebImage](https://github.com/SDWebImage/SDWebImage)依存性が必要かどうかを確認するには、[iOSアプリ内メッセージドキュメント]]({{ site.baseurl }}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/) を参照すること。
{% endalert %}
{% endtab %}
{% endtabs %}

### ステップ 2:パッケージをインポートする

{% tabs %}
{% tab Android %}
Unity エディターで Unity プロジェクトにパッケージをインポートするには、**[アセット] > [パッケージをインポート] > [カスタムパッケージ]** の順に移動します。次に、**Import**をクリックします。

または、カスタム Unity パッケージのインポートに関して詳しくは、[Unity アセットパッケージのインポート](https://docs.unity3d.com/Manual/AssetPackages.html)の説明を参照してください。 

{% alert note %}
iOS またはAndroid プラグインのみをインポートする場合は、Braze`.unitypackage` をインポートするときに`Plugins/Android` または`Plugins/iOS` サブディレクトリの選択を解除します。
{% endalert %}
{% endtab %}

{% tab Swift %}
Unity エディターで Unity プロジェクトにパッケージをインポートするには、**[アセット] > [パッケージをインポート] > [カスタムパッケージ]** の順に移動します。次に、**Import**をクリックします。

または、カスタム Unity パッケージのインポートに関して詳しくは、[Unity アセットパッケージのインポート](https://docs.unity3d.com/Manual/AssetPackages.html)の説明を参照してください。 

{% alert note %}
iOS またはAndroid プラグインのみをインポートする場合は、Braze`.unitypackage` をインポートするときに`Plugins/Android` または`Plugins/iOS` サブディレクトリの選択を解除します。
{% endalert %}
{% endtab %}
{% endtabs %}

### ステップ 3:SDKを設定する

{% tabs %}
{% tab Android %}
#### ステップ 3.1:設定する `AndroidManifest.xml`

機能する [`AndroidManifest.xml`](https://docs.unity3d.com/Manual/android-manifest.html)を機能させる。アプリに`AndroidManifest.xml` がない場合は、以下をテンプレートとして使用できます。それ以外の場合、すでに`AndroidManifest.xml` がある場合は、次のいずれかの欠落セクションが既存の`AndroidManifest.xml` に追加されていることを確認します。

1. `Assets/Plugins/Android/` ディレクトリに移動し、`AndroidManifest.xml` ファイルを開封する。これは[Unityエディタのデフォルトの場所で](https://docs.unity3d.com/Manual/android-manifest.html)ある。
2. `AndroidManifest.xml` に、以下のテンプレートにある必要な権限とアクティビティを追加する。
3. 終了後、`AndroidManifest.xml` には、`"android.intent.category.LAUNCHER"` が存在するアクティビティが1つだけ含まれているはずだ。

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />

  <application android:icon="@drawable/app_icon" 
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity" 
      android:theme="@style/UnityThemeSelector"
      android:label="@string/app_name" 
      android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen" 
      android:screenOrientation="sensor">
      <meta-data android:name="android.app.lib_name" android:value="unity" />
      <meta-data android:name="unityplayer.ForwardNativeEventsToDalvik" android:value="true" />
      <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
      </intent-filter>
    </activity>

    <!-- A Braze specific FirebaseMessagingService used to handle push notifications. -->
    <service android:name="com.braze.push.BrazeFirebaseMessagingService"
      android:exported="false">
      <intent-filter>
        <action android:name="com.google.firebase.MESSAGING_EVENT" />
      </intent-filter>
    </service>
  </application>
</manifest>
```

{% alert important %}
`AndroidManifest.xml` ファイルに登録されているすべてのアクティビティクラスは、Braze Android SDKと完全に統合されている必要があり、そうでなければ分析は収集されない。独自のActivityクラスを追加する場合は、必ず[Braze Unityプレーヤーを拡張して](#unity_extend-unity-player)、これを防げるようにすること。
{% endalert %}

#### ステップ 3.2:`AndroidManifest.xml` をパッケージ名で更新する。

パッケージ名を確認するには、**[ファイル] > [ビルド設定] > [プレーヤー設定] > [Android タブ]**を選択します。

![]({% image_buster /assets/img_archive/UnityPackageName.png %})

`AndroidManifest.xml` では、`REPLACE_WITH_YOUR_PACKAGE_NAME` のすべてのインスタンスを前のステップの `Package Name` に置き換える必要があります。

#### ステップ3.3：gradleの依存関係を追加する

Unity プロジェクトに gradle の依存関係を追加するには、まず公開設定で [[Custom Main Gradle テンプレート]](https://docs.unity3d.com/Manual/class-PlayerSettingsAndroid.html#Publishing) を有効にします。これにより、プロジェクトで使用するテンプレートグラドルファイルが作成されます。gradle ファイルは、依存関係の設定やその他のビルド時のプロジェクト設定を処理します。詳細については、Braze Unity サンプルアプリの[mainTemplate.gradle](https://github.com/braze-inc/braze-unity-sdk/blob/master/unity-samples/Assets/Plugins/Android/mainTemplate.gradle) を参照してください。

次の依存関係が必要です。

```groovy
implementation 'com.google.firebase:firebase-messaging:22.0.0'
implementation "androidx.swiperefreshlayout:swiperefreshlayout:1.1.0"
implementation "androidx.recyclerview:recyclerview:1.2.1"
implementation "org.jetbrains.kotlin:kotlin-stdlib:1.6.0"
implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.6.1"
implementation 'androidx.core:core:1.6.0'
```

これらの依存関係は、[External Dependency Manager](https://github.com/googlesamples/unity-jar-resolver)を使用して設定することもできます。

#### ステップ 3.4:UnityのAndroidインテグレーションを自動化する

Braze は、Unity Android 統合を自動化するためのネイティブ Unity ソリューションを提供しています。 

1. Unity エディターで **[Braze] > [Braze 構成]** の順に移動して、[Braze 構成設定] を開きます。
2. [**Unity Android 統合の自動化**] ボックスにチェックマークを入れます。
3. **Braze API キー**フィールドで、**設定の管理**にあるアプリアプリケーションのAPI キーをBraze ダッシュボードから入力します。

{% alert note %}
手動で作成した `braze.xml` ファイルでは、プロジェクトのビルド中に設定値が競合する可能性があるため、この自動統合は使用しないでください。手動の`braze.xml` が必要な場合は、自動統合を無効にします。
{% endalert %}
{% endtab %}

{% tab Swift %}
#### ステップ 3.1:API キーの設定

Braze は、Unity iOS 統合を自動化するためのネイティブ Unity ソリューションを提供しています。このソリューションは、Unity の [`PostProcessBuildAttribute`](http://docs.unity3d.com/ScriptReference/Callbacks.PostProcessBuildAttribute.html) を使用してビルドされた Xcode プロジェクトを変更し、`IMPL_APP_CONTROLLER_SUBCLASS` マクロを使用して `UnityAppController` をサブクラス化します。

1. Unity エディターで **[Braze] > [Braze 構成]** の順に移動して、[Braze 構成設定] を開きます。
2. [**Unity iOS 統合の自動化**] ボックスにチェックマークを入れます。
3. **Braze API キー** フィールドで、**設定の管理** にあるアプリアプリケーションのAPI キーを入力します。

![]({% image_buster /assets/img_archive/unity-ios-appboyconfig.png %})

アプリですでに別の `UnityAppController` サブクラスが使用されている場合、サブクラスの実装を `AppboyAppDelegate.mm` とマージする必要があります。
{% endtab %}
{% endtabs %}

## Unityパッケージをカスタマイズする

### ステップ 1: リポジトリを複製する

ターミナルで、[Braze Unity SDK GitHubリポジトリを](https://github.com/braze-inc/braze-unity-sdk)複製し、そのフォルダに移動する：

{% tabs local %}
{% tab MacOS %}
```bash
git clone git@github.com:braze-inc/braze-unity-sdk.git
cd ~/PATH/TO/DIRECTORY/braze-unity-sdk
```
{% endtab %}

{% tab Windows Powershell %}
```powershell
git clone git@github.com:braze-inc/braze-unity-sdk.git
cd C:\PATH\TO\DIRECTORY\braze-unity-sdk
```
{% endtab %}
{% endtabs %}

### ステップ 2:リポジトリからパッケージをエクスポートする

まずUnityを起動し、バックグラウンドで起動しておく。次に、リポジトリのルートで以下のコマンドを実行して、パッケージを`braze-unity-sdk/unity-package/` にエクスポートする。

{% tabs local %}
{% tab MacOS %}
```bash
/Applications/Unity/Unity.app/Contents/MacOS/Unity -batchmode -nographics -projectPath "$(pwd)" -executeMethod Appboy.Editor.Build.ExportAllPackages -quit
```
{% endtab %}

{% tab Windows Powershell %}
```powershell
"%UNITY_PATH%" -batchmode -nographics -projectPath "%PROJECT_ROOT%" -executeMethod Appboy.Editor.Build.ExportAllPackages -quit	
```
{% endtab %}
{% endtabs %}

{% alert tip %}
これらのコマンドを実行した後に何らかの問題が発生した場合は、[Unityを参照のこと：コマンドライン引数](https://docs.unity3d.com/2017.2/Documentation/Manual/CommandLineArguments.html).
{% endalert %}

### ステップ 3:Unityにパッケージをインポートする

1. Unityで、**Assets**>**Import Package**>**Custom Packageと**進み、目的のパッケージをUnityプロジェクトにインポートする。
2. インポートしたくないファイルがあれば、今すぐ選択を解除する。
3. `Assets/Editor/Build.cs` にあるエクスポートされたUnityパッケージをカスタマイズする。

## 自動統合に切り替える（Swiftのみ） {#automated-integration}

Braze Unity SDKで提供される自動化されたiOSインテグレーションを利用するには、手動から自動化されたインテグレーションに移行するための以下のステップに従う。

1. Xcodeプロジェクトの`UnityAppController` サブクラスから、Braze関連のコードをすべて削除する。
2. UnityまたはXcodeプロジェクトからBraze iOSライブラリを削除する（`Appboy_iOS_SDK.framework` や`SDWebImage.framework` など）。
3. Braze Unityパッケージをプロジェクトに再度インポートする。完全なウォークスルーは、[ステップ2を参照のこと：](#unity_step-2-import-the-package) パッケージをインポートする。
4. APIキーを再度設定する。完全なウォークスルーは、[ステップ3.1を参照のこと：APIキーを設定する](#unity_step-31-set-your-api-key).

## オプション構成

### 詳細なログ記録

Unityエディターで冗長ロギングを有効にするには、以下のようにする：

1. [**Braze**] > [**Braze 構成**] の順に移動して、[Braze 構成設定] を開きます。
2. [**Braze Android 設定を表示する**] ドロップダウンをクリックします。
3. [**SDK ログレベル**] フィールドに値「0」を入力します。

### Prime 31 の互換性

Prime31 プラグインで Braze Unity プラグインを使用するには、Prime31 互換の Activity クラスを使用するようにプロジェクトの `AndroidManifest.xml` を編集します。の参照をすべて変更する。
`com.braze.unity.BrazeUnityPlayerActivity` から `com.braze.unity.prime31compatible.BrazeUnityPlayerActivity`

### アマゾン・デバイス・メッセージング（ADM）

Brazeは、Unityアプリへの[ADMプッシュの](https://developer.amazon.com/public/apis/engage/device-messaging)統合をサポートしている。ADMプッシュを統合したい場合は、ADM APIキーを含む`api_key.txt` というファイルを作成し、`Plugins/Android/assets/` フォルダに置く。 ADMとBrazeの統合の詳細については、[ADMプッシュ統合手順を]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=unity)参照。

### Braze Unityプレーヤーの拡張（Androidのみ） {#extend-unity-player}

提供されている `AndroidManifest.xml` ファイルの例では、1つの Activity クラス [`BrazeUnityPlayerActivity`](https://github.com/braze-inc/braze-android-sdk/blob/e804cb3a10ae68364b354b52abf1bef8a0d1a9dc/android-sdk-unity/src/main/java/com/braze/unity/BrazeUnityPlayerActivity.kt) が登録されています。このクラスは Braze SDK と統合され、セッション処理、アプリ内メッセージ登録、プッシュ通知分析ログなどを使用して `UnityPlayerActivity` を拡張します。`UnityPlayerActivity` クラスの拡張の詳細については、「[Unity](https://docs.unity3d.com/Manual/AndroidUnityPlayerActivity.html)」を参照してください。

ライブラリやプラグインプロジェクトで独自のカスタム`UnityPlayerActivity` を作成する場合は、カスタム機能をBrazeと統合するために、当社の`BrazeUnityPlayerActivity` を拡張する必要がある。`BrazeUnityPlayerActivity` を拡張する作業を始める前に、Unity プロジェクトに Braze を統合するための手順に従ってください。

1. [Braze Android SDK統合の説明]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)に従って、Braze Android SDK をライブラリまたはプラグインプロジェクトに依存関係として追加します。
2. Unity 固有の機能を含む Unity `.aar` を、Unity 用に構築している Android ライブラリプロジェクトに統合します。`appboy-unity.aar` は、[公開リポジトリ](https://github.com/braze-inc/braze-unity-sdk/tree/master/Assets/Plugins/Android)から入手できます。Unity ライブラリがうまく統合されたら、`BrazeUnityPlayerActivity` を拡張するように `UnityPlayerActivity` を変更します。
3. ライブラリまたはプラグインプロジェクトをエクスポートし、通常どおり `/<your-project>/Assets/Plugins/Android` にドロップします。ライブラリやプラグインにBrazeのソースコードを含めないこと。それらはすでに`/<your-project>/Assets/Plugins/Android` に存在するからである。
4. `/<your-project>/Assets/Plugins/Android/AndroidManifest.xml` を編集し、`BrazeUnityPlayerActivity` のサブクラスをメイン・アクティビティとして指定する。

これでUnity IDEから、Brazeと完全に統合され、カスタム`UnityPlayerActivity` 機能を含む`.apk` をパッケージできるようになるはずだ。

## トラブルシューティング

### エラー:「ファイルが読み込めなかった

以下のようなエラーは無視して問題ありません。アップルのソフトウェアはCgBIと呼ばれる独自のPNG拡張子を使用しているが、Unityはこれを認識しない。これらのエラーは、iOSのビルドやBrazeバンドルの関連画像の適切な表示には影響しない。

```
Could not create texture from Assets/Plugins/iOS/AppboyKit/Appboy.bundle/...png: File could not be read
```
