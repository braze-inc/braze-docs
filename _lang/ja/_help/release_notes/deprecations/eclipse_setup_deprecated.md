---
nav_title: Eclipseでの初期SDKセットアップ
page_order: 1

page_type: update
description: "この記事は、Eclipseを使用して初期SDKセットアップを行う方法について説明しています。BrazeはEclipse IDEのサポートを非推奨にしました。"
---

# Eclipseでの初期SDKセットアップ

{% alert update %}
Brazeは、[GoogleがEclipse Android開発者ツールプラグインのサンセッティング（配信停止）を行ったため](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html)、Eclipse IDEのサポートを終了しました。移行前にEclipse統合に関して支援が必要な場合は、[サポートにメール]({{site.baseurl}}/support_contact/)して支援を受けてください。
{% endalert %}

## ステップ 1
コマンドラインで、[Braze Android GitHub Repository][03]を複製します。

```bash
$ git clone git@github.com:braze-inc/braze-android-sdk.git
```

## ステップ 2
Brazeプロジェクトをローカルワークスペースにインポートする

エクリプスで:

  - ファイル > インポートに移動します。

    ![ファイルインポート][04]
  - Android を選択 > 既存の Android コードをワークスペースに追加。

    ![Androidドインポート][05]
  - 「参照」をクリックします。

    ![ブラウズ][06]
  - 「Braze UI プロジェクトフォルダ」を確認し、「ワークスペースにプロジェクトをコピー」を選択して、「完了」をクリックします。

    ![Android UI プロジェクトを選択][07]

## ステップ 3
独自のプロジェクトでBrazeを参照してください。
エクリプスで:

  - プロジェクトを右クリックして「プロパティ」を選択します。

    ![プロパティをクリック][08]
  - 「Android」の下で、ライブラリーセクションの「追加...」をクリックし、android-sdk-uiをライブラリーとしてアプリに追加します。

    ![Braze 追加][09]

## ステップ 4
依存関係のエラーを解決し、ビルドターゲットを修正します。

この時点で、Brazeコードにエラーが表示されることがあります。これは、依存関係が設定されておらず、ビルドターゲットが正しくない可能性があるためです。

   - Braze UIプロジェクトを右クリックし、プロパティ->Androidを選択して、ビルドターゲットがBrazeの現在のビルドツールバージョンに設定されていることを確認します。

      ![ビルドターゲット][10]
   - Braze UIプロジェクトを右クリックし、プロパティ->Javaビルドパス->JARの追加...を選択し、メインアプリケーションから'android-support-v4.jar'をライブラリーとして追加します。

      ![サポート][11]

## ステップ 5

最後のピースを追加します。

  - SDK バージョン 1.10.0 以上の場合、追加する必要があります
  `<service android:name="com.appboy.services.AppboyDataSyncService" />`
  あなたのAndroidManifest.xmlへ、Eclipseはマニフェストのマージをサポートしていないため。

  - SDK バージョン 1.7.0 以上の場合、ライブラリー プロジェクトからアプリケーションに "assets/fontawesome-webfont.ttf" をコピーする必要があります。エクリプスはライブラリからアセットフォルダを自動的に含めません。

[03]: https://github.com/braze-inc/braze-android-sdk "Appboy Android GitHub リポジトリ"
[04]: {{site.baseurl}}/assets/img_archive/file_import.png
[05]: {{site.baseurl}}/assets/img_archive/android_import.png
[06]: {{site.baseurl}}/assets/img_archive/click_browse.png
[07]: {{site.baseurl}}/assets/img_archive/select_project_android.png
[08]: {{site.baseurl}}/assets/img_archive/click_properties.png
[09]: {{site.baseurl}}/assets/img_archive/add_appboy_ui.png
[10]: {{site.baseurl}}/assets/img_archive/build_target.png
[11]: {{site.baseurl}}/assets/img_archive/android_support_v4.png
