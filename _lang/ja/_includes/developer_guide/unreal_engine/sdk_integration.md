## アンリアルエンジンBraze SDKについて

Braze アンリアルSDK プラグインを使用すると、次のことができます。

* アプリやゲーム内のセッションを測定、追跡する
* アプリ内購入とカスタムイベントを追跡する
* 標準およびカスタム属性でユーザープロファイルを更新する
* プッシュ通知を送信する
* Unreal アプリを大規模なキャンバスジャーニーと統合する
* アプリ内の行動に基づいて、EメールやSMSなどのクロスチャネルメッセージを送信する。

## アンリアルエンジンSDKの統合

### ステップ 1: Braze プラグインを追加する

ターミナルで、[Unreal Engine Braze SDK GitHub リポジトリ](https://github.com/braze-inc/braze-unreal-sdk) を複製します。

```bash
git clone git@github.com:braze-inc/braze-unreal-sdk.git
```

次に、`BrazeSample/Plugins/Braze` ディレクトリーをコピーし、アプリのPlugin フォルダーに追加します。

### ステップ 2:プラグインを有効にする

C++ またはブループリントプロジェクトのプラグインを有効にします。

{% tabs %}
{% tab C++ %}
C++ プロジェクトの場合は、Braze モジュールを参照するようにモジュールを設定します。`\*.Build.cs file` で、`"Braze"` を`PublicDependencyModuleNames` に追加します。

```cpp
PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "Braze" });
```
{% endtab %}

{% tab ブループリント %}
ブループリントプロジェクトの場合は、**Settings**> **Plugins** に移動し、**Braze** チェック**Enabled** に移動します。

![EnablePlugin]({% image_buster /assets/img/unreal_engine/EnablePlugin.png %})
{% endtab %}
{% endtabs %}

### ステップ 3:API キーとエンドポイントを設定する

API キーとエンドポイントをプロジェクトの`DefaultEngine.ini` に設定します。

```cpp
[/Script/Braze.BrazeConfig]
bAutoInitialize=True ; true by default, initialize when the project starts
AndroidApiKey= ; your API key
IOSApiKey= ; your API key
CustomEndpoint= ; your endpoint
```

{% alert warning %}
Android SDK 31+ アンリアルをターゲットとするプロジェクトの場合、INSTALL_PARSE_FAILED_MANIFEST_MALFORMED エラーを使用したAndroid 12+ デバイスへのインストール中に失敗するビルドが生成されます。これを修正するには、このリポジトリーのルートにある`UE4_Engine_AndroidSDK_31_Build_Fix.patch` git パッチファイルを見つけ、アンリアルソースビルドにアプリします。
{% endalert %}

### ステップ 4: SDKを手動で初期化する(オプション)

デフォルトでは、SDKは起動時に自動的に初期化されます。初期化をよりコントロールしたい場合(ユーザーの同意の待機やログレベルの設定など)、`AutoInitialize` を`DefaultEngine.ini` で無効にし、C++ またはブループリントで手動で初期化することができます。

{% tabs %}
{% tab C++ %}
ネイティブC++ では、BrazeSubsystem にアクセスして`InitializeBraze()` を呼び出し、オプションでConfig を渡してEngine.ini 設定s を上書きします。

```cpp
UBrazeSubsystem* const BrazeSubsystem = GEngine->GetEngineSubsystem<UBrazeSubsystem>();
UBraze* const BrazeInstance = BrazeSubsystem->InitializeBraze();
```
{% endtab %}

{% tab ブループリント %}
ブループリントでは、ブループリントノードと同じ機能にアクセスできます。  
`GetBrazeSubsystem` ノードを使用して、`Initialize` ノードを呼び出します。  
BrazeConfig オブジェクトは、ブループリントで任意に作成して渡すことができます `Initialize`

![初期化Braze]({% image_buster /assets/img/unreal_engine/InitializeBraze.png %})
{% endtab %}
{% endtabs %}

## オプション構成

### ロギング

{% tabs local %}
{% tab Android %}
ログレベルは、C++ またはブループリントノードを使用して実行時に設定できます。

{% subtabs %}
{% subtab C++ %}
実行時にログレベルを設定するには、`UBrazeSubsystem::AndroidSetLogLevel` を呼び出します。

```cpp
UBrazeSubsystem* const BrazeSubsystem = GEngine->GetEngineSubsystem<UBrazeSubsystem>();
BrazeSubsystem->AndroidSetLogLevel(EBrazeLogLevel::Verbose);
UBraze* const BrazeInstance = BrazeSubsystem->InitializeBraze();
```
{% endsubtab %}

{% subtab Blueprint %}
ブループリントでは、** Android ログレベル設定** ノードを使用できます。

![Blueprint.]({% image_buster /assets/img/unreal_engine/AndroidSetLogLevel.png %}) のAndroid ログレベル設定ノード
{% endsubtab %}
{% endsubtabs %}

Braze SDK初期化が呼び出されたときにロギングが確実に設定されるようにするには、`InitializeBraze` の前にこれを呼び出すことをお勧めします。
{% endtab %}

{% tab iOS %}
`info.plist` のログレベルを有効にするには、**Settings** > **Project Settings** に移動し、**iOS** の下の**Platforms** を選択します。**Extra PList Data**の下で、**Additional Plist Data**を見つけ、ログレベルを入力します。

```xml
<key>Appboy</key>
<dict>
  <key>LogLevel</key>
  <string>0</string>
</dict>
```

デフォルトのログレベルは8 で、これは最小のログです。ログレベルについて詳しくは、以下を参照してください。[他のSDKのカスタマイズ]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/)
{% endtab %}
{% endtabs %}
