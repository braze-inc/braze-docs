---
nav_title: 参考文献とサンプルアプリ
article_title: Braze SDKリファレンス、リポジトリ、サンプルアプリ
page_order: 5.5
description: "各SDKに属するリファレンスドキュメント、GitHubリポジトリ、サンプルアプリの一覧である。"
---

# リファレンス、リポジトリ、サンプルアプリ

> 各SDKに属するリファレンスドキュメント、GitHubリポジトリ、サンプルアプリの一覧である。SDKのリファレンス・ドキュメントには、使用可能なクラス、型、関数、変数の詳細が記載されている。GitHubリポジトリは、SDKの関数やアトリビューションの宣言、コードの変更、バージョン管理に関するインサイトを提供している。各リポジトリには、Brazeの機能をテストしたり、独自のアプリケーションと一緒に実装するために使用できる、完全にビルド可能なサンプルアプリケーションも含まれている。

## リソース一覧

{% alert note %}
現在、いくつかのSDKには専用のリファレンス・ドキュメントがないが、我々は積極的に取り組んでいる。
{% endalert %}

| プラットフォーム          | 参考                                                                                                                                    | リポジトリ                                                                 | サンプルアプリ                                                                |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Android SDK       | [参考ドキュメント](https://braze-inc.github.io/braze-android-sdk/kdoc/index.html)                                                                           | [GitHubリポジトリ](https://github.com/braze-inc/braze-android-sdk)      | [サンプルアプリ](https://github.com/braze-inc/braze-android-sdk/tree/master/samples)      |
| SWIFT SDK         | [参考ドキュメント](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze)                                                                | [GitHubリポジトリ](https://github.com/braze-inc/braze-swift-sdk)            | [サンプルアプリ](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)            |
| ウェブSDK           | [参考ドキュメント](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)                                                               | [GitHubリポジトリ](https://github.com/braze-inc/braze-web-sdk)              | [サンプルアプリ](https://github.com/braze-inc/braze-web-sdk/tree/master/sample-builds)              |
| Cordova SDK       | [宣言ファイル](https://github.com/braze-inc/braze-cordova-sdk/blob/master/www/BrazePlugin.js)                                      | [GitHubリポジトリ](https://github.com/braze-inc/braze-cordova-sdk)      | [サンプルアプリ](https://github.com/braze-inc/braze-cordova-sdk/tree/master/sample-project)      |
| Flutter SDK       | [参考ドキュメント](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/)                                                   | [GitHubリポジトリ](https://github.com/braze-inc/braze-flutter-sdk)      | [サンプルアプリ](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example)      |
| ReactネイティブSDK  | [宣言ファイル](https://github.com/braze-inc/braze-react-native-sdk/blob/master/src/index.d.ts)                   | [GitHubリポジトリ](https://github.com/braze-inc/braze-react-native-sdk) | [サンプルアプリ](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject) |
| Roku SDK          | N/A                                                                                                                                                         | [GitHubリポジトリ](https://github.com/braze-inc/braze-roku-sdk)            | [サンプルアプリ](https://github.com/braze-inc/braze-roku-sdk/tree/main/torchietv)            |
| Unity SDK         | [宣言ファイル](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs)     | [GitHubリポジトリ](https://github.com/braze-inc/braze-unity-sdk)          | [サンプルアプリ](https://github.com/braze-inc/braze-unity-sdk/tree/master/unity-samples)          |
| アンリアルエンジンSDK | N/A                                                                                                                                                         | [GitHubリポジトリ](https://github.com/braze-inc/braze-unreal-sdk)        | [サンプルアプリ](https://github.com/braze-inc/braze-unreal-sdk/tree/master/BrazeSample)        |
| .NET MAUI SDK       | N/A                                                                                                                                                         | [GitHubリポジトリ](https://github.com/braze-inc/braze-xamarin-sdk)      | [サンプルアプリ](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples)      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## サンプルアプリを作る

{% tabs %}
{% tab Android %}
### ドロイド・ボーイを作る

[Android SDK GitHub repository](https://github.com/braze-inc/braze-android-sdk "Braze Android GitHub Repository")内のテストアプリケーションは、Droidboy と呼ばれます。次の手順に従って、プロジェクトとともに完全に機能する Droidboy のコピーを構築します。

1. 新しい[ワークスペース]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#app-group-configuration)を作成し、Braze API 識別子キーを書き留めます。<br><br>
2. FCM 送信者 ID と Braze API 識別子キーを `/droidboy/res/values/braze.xml` 内の適切な場所 (それぞれ `com_braze_push_fcm_sender_id` と `com_braze_api_key` という文字列のタグの間) にコピーします。<br><br>
3. FCM サーバーキーとサーバー ID を [**設定の管理**] のワークスペース設定にコピーします。<br><br>
4. Droidboy APK をアセンブルするには、SDK ディレクトリ内で `./gradlew assemble` を実行します。Windows では `gradlew.bat` を使用します。<br><br>
5. Droidboy APK をテストデバイスに自動的にインストールするには、SDK ディレクトリ内で `./gradlew installDebug` を実行します。

### "ハローBraze "を作る

Hello Braze テストアプリケーションは、Braze SDK の最小限のユースケースを示し、さらに Braze SDK を Gradle プロジェクトに簡単に統合する方法も示します。

1. [**設定の管理**] ページの API 識別子キーを `res/values` フォルダーの `braze.xml` ファイルにコピーします。
![]({% image_buster /assets/img_archive/hello_appboy.png %})<br><br>
2. サンプルアプリをデバイスまたはエミュレーターにインストールするには、SDK ディレクトリ内で次のコマンドを実行します。
```
./gradlew installDebug
```
`ANDROID_HOME` 変数が適切に設定されていない場合、または有効な `sdk.dir` フォルダーを含む `local.properties` フォルダーがない場合、このプラグインはベース SDK もインストールします。詳細については、[プラグインリポジトリ](https://github.com/JakeWharton/sdk-manager-plugin)を参照してください。

Android SDK ビルドシステムの詳細については、[GitHub リポジトリの README](https://github.com/braze-inc/braze-android-sdk/blob/master/README.md) を参照してください。
{% endtab %}

{% tab swift %}
### SWIFTテストアプリを作る

以下の手順に従って、テストアプリケーションをビルドして実行します。

1. 新しい[ワークスペース]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps)を作成し、アプリ識別子APIキーおよびエンドポイントに注意してください。
2. 統合方法 (Swift Package Manager、CocoaPods、Manual) に基づいて、適切な `xcodeproj` ファイルを選択して開きます。
3. `Credentials`ファイルの適切なフィールドにAPIキーとエンドポイントを配置します。
{% endtab %}
{% endtabs %}

{% alert note %}
SDKインテグレーションのQAを行う際、[SDKデバッガーを]({{site.baseurl}}/developer_guide/sdk_integration/debugging)使用すれば、アプリの冗長ロギングをオンにすることなく、問題のトラブルシューティングを行うことができる。
{% endalert %}