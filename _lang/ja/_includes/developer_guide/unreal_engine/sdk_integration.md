## Unreal Engine Braze SDKについて

Braze Unreal SDKプラグインを使用すると、次のことができる：

* アプリやゲーム内のセッションを測定、追跡する
* アプリ内購入とカスタムイベントを追跡する
* 標準およびカスタム属性でユーザープロファイルを更新する
* プッシュ通知を送信する
* Unreal アプリを大規模なキャンバスジャーニーと統合する
* アプリ内の行動に基づいて、EメールやSMSなどのクロスチャネルメッセージを送信する。

## Unreal Engine SDK の開発

### ステップ1:Brazeプラグインを追加する

ターミナルで、[Unreal Engine Braze SDK GitHubリポジトリを](https://github.com/braze-inc/braze-unreal-sdk)複製する。

```bash
git clone git@github.com:braze-inc/braze-unreal-sdk.git
```

次に、`BrazeSample/Plugins/Braze` ディレクトリをコピーし、アプリのPluginフォルダに追加する。

### ステップ2: プラグインをイネーブルメントにする

C++またはBlueprintプロジェクトのプラグインをイネーブルメントする。

{% tabs %}
{% tab C++ %}
C++プロジェクトの場合は、Brazeモジュールを参照するようにモジュールを設定する。`\*.Build.cs file` の`"Braze"` を`PublicDependencyModuleNames` に追加する。

```cpp
PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "Braze" });
```
{% endtab %}

{% tab 青写真 %}
Blueprintプロジェクトでは、**設定**＞**プラグインと**進み、**Brazeの**横にある「**イネーブルメント**」にチェックを入れる。

![EnablePlugin]({% image_buster /assets/img/unreal_engine/EnablePlugin.png %})
{% endtab %}
{% endtabs %}

### ステップ 3:APIキーとエンドポイントを設定する。

プロジェクトの`DefaultEngine.ini` にAPIキーとエンドポイントを設定する。

```cpp
[/Script/Braze.BrazeConfig]
bAutoInitialize=True ; true by default, initialize when the project starts
AndroidApiKey= ; your API key
IOSApiKey= ; your API key
CustomEndpoint= ; your endpoint
```

{% alert warning %}
Android SDK 31+ をターゲットとするプロジェクトの場合、アンリアルは Android 12+ デバイスへのインストール時に INSTALL_PARSE_FAILED_MANIFEST_MALFORMED エラーで失敗するビルドを生成する。これを修正するには、このリポジトリのルートにある`UE4_Engine_AndroidSDK_31_Build_Fix.patch` git patch ファイルを探し、Unreal のソースビルドに適用する。
{% endalert %}

## オプション構成

### ロギング

{% tabs local %}
{% tab Android %}
C++またはブループリント・ノードを使って、実行時にログ・レベルを設定することができる。

{% subtabs %}
{% subtab C++ %}
実行時にログレベルを設定するには、`UBrazeSubsystem::AndroidSetLogLevel` を呼ぶ。

```cpp
UBrazeSubsystem* const BrazeSubsystem = GEngine->GetEngineSubsystem<UBrazeSubsystem>();
BrazeSubsystem->AndroidSetLogLevel(EBrazeLogLevel::Verbose);
UBraze* const BrazeInstance = BrazeSubsystem->InitializeBraze();
```
{% endsubtab %}

{% subtab Blueprint %}
ブループリントでは、**Android Set Log Level**ノードを使用できる：

![ブループリントのAndroid Set Log Levelノード]({% image_buster /assets/img/unreal_engine/AndroidSetLogLevel.png %})
{% endsubtab %}
{% endsubtabs %}

Braze SDK Initializeが呼び出されたときにロギングが確実に設定されるように、`InitializeBraze` の前にこれを呼び出すことを推奨する。
{% endtab %}

{% tab iOS %}
`info.plist` でログレベルをイネーブルメントにするには、**設定**>**プロジェクト設定に**進み、**プラットフォームで** **iOSを**選択する。**Extra PList Data**」で「**Additional Plist Data**」を探し、ログレベルを入力する：

```xml
<key>Appboy</key>
<dict>
  <key>LogLevel</key>
  <string>0</string>
</dict>
```

デフォルトのログレベルは8で、これは最小限のロギングである。ログレベルについてもっと読む：[その他のSDKカスタマイズ]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/)
{% endtab %}
{% endtabs %}
