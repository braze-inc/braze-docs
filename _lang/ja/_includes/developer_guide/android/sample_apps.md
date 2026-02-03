# サンプルアプリ

> Braze SDK にはそれぞれ、利便性を高めるためにリポジトリ内にサンプルアプリケーションが付属しています。これらのアプリはそれぞれ完全にビルド可能であるため、独自のアプリケーション内で実装すると同時に、Braze 機能をテストできます。 

ご自身のアプリケーション内での動作のテストと、予期される動作のテスト、およびサンプルアプリケーション内でのコードパスは、問題が発生した場合に、それをデバッグするための優れた方法です。

## Droidboy テストアプリケーションの構築
[Android SDK GitHub リポジトリ](https://github.com/braze-inc/braze-android-sdk)内のテスト アプリケーションは Droidboy と呼ばれます。次の手順に従って、プロジェクトとともに完全に機能する Droidboy のコピーを構築します。

1. 新しい[ワークスペース]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#app-group-configuration)を作成し、Braze API 識別子キーを書き留めます。<br><br>
2. FCM 送信者 ID と Braze API 識別子キーを `/droidboy/res/values/braze.xml` 内の適切な場所 (それぞれ `com_braze_push_fcm_sender_id` と `com_braze_api_key` という文字列のタグの間) にコピーします。<br><br>
3. FCM サーバーキーとサーバー ID を [**設定の管理**] のワークスペース設定にコピーします。<br><br>
4. Droidboy APK をアセンブルするには、SDK ディレクトリ内で `./gradlew assemble` を実行します。Windows では `gradlew.bat` を使用します。<br><br>
5. Droidboy APK をテストデバイスに自動的にインストールするには、SDK ディレクトリ内で `./gradlew installDebug` を実行します。

## Hello Braze テストアプリケーションの構築
Hello Braze テストアプリケーションは、Braze SDK の最小限のユースケースを示し、さらに Braze SDK を Gradle プロジェクトに簡単に統合する方法も示します。

1. [**設定の管理**] ページの API 識別子キーを `res/values` フォルダーの `braze.xml` ファイルにコピーします。
![]({% image_buster /assets/img_archive/hello_appboy.png %})<br><br>
2. サンプルアプリをデバイスまたはエミュレーターにインストールするには、SDK ディレクトリ内で次のコマンドを実行します。
```
./gradlew installDebug
```
`ANDROID_HOME` 変数が適切に設定されていない場合、または有効な `sdk.dir` フォルダーを含む `local.properties` フォルダーがない場合、このプラグインはベース SDK もインストールします。詳細については、[プラグインリポジトリ](https://github.com/JakeWharton/sdk-manager-plugin)を参照してください。

Android SDK ビルドシステムの詳細については、[GitHub リポジトリの README](https://github.com/braze-inc/braze-android-sdk/blob/master/README.md) を参照してください。

