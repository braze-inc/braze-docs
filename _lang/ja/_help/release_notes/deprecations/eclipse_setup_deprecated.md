---
nav_title: Eclipse による初期 SDK セットアップ
page_order: 1

page_type: update
description: "このアーカイブ記事では、Eclipse で SDK の初期セットアップを実行する方法について説明します。Braze は Eclipse IDE のサポートを廃止しました。"
---

# Eclipse での初期 SDK セットアップ

{% alert update %}
[Google が Eclipse Android デベロッパーツールプラグインのサポートを終了したため、Braze は Eclipse IDE のサポートを終了しました](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html)。移行前に Eclipse 統合についてサポートが必要な場合は、[サポートにメールしてください]({{site.baseurl}}/support_contact/)。
{% endalert %}

## ステップ 1
コマンドラインで [Braze アンドロイド GitHub リポジトリのクローンを作成します][03]。

```bash
$ git clone git@github.com:braze-inc/braze-android-sdk.git
```

## ステップ 2
Braze プロジェクトをローカルワークスペースにインポートする

エクリプスでは:

  - [ファイル] > [インポート] に移動します。

    ![ファイルインポート][04]
  - [アンドロイド] > [既存の Android コードをワークスペースに追加] を選択します。

    ![Androidドインポート][05]
  - 「ブラウズ」をクリックします。」

    ![参照][06]
  - Braze UI プロジェクトフォルダと「プロジェクトをワークスペースにコピー」を確認し、「完了」をクリックします。」

    ![アンドロイド UI プロジェクトを選択][07]

## ステップ 3
自分のプロジェクトで Braze を参考にしてください。
エクリプスでは:

  - プロジェクトを右クリックし、[プロパティ] を選択します。」

    ![[プロパティ] をクリックします。][08]
  - [Android] の下にある [追加...] をクリックします。「ライブラリ」セクションで android-sdk-ui をライブラリとしてアプリに追加します。

    ![ブレイズアッド][09]

## ステップ 4
依存関係エラーを解決し、ビルドターゲットを修正します。

現時点では、Braze コードでエラーが発生することがあります。これは、依存関係が入力されておらず、ビルドターゲットが正しくない可能性があるためです。

   - Braze UI プロジェクトを右クリックし、[プロパティ]-> [Android] を選択して、ビルドターゲットが Braze の現在のビルドツールバージョンに設定されていることを確認します。

      ![ビルドターゲット][10]
   - Braze UI プロジェクトを右クリックし、「プロパティ」->「Java ビルドパス」->「JAR を追加...」を選択し、メインアプリケーションから「android-support-v4.jar」をライブラリとして追加します。

      ![サポート][11]

## ステップ 5

最後のピースを追加します。

  - SDK バージョン 1.10.0 以降では、追加する必要があります
  `<service android:name="com.appboy.services.AppboyDataSyncService" />`
  Eclipse はマニフェストのマージをサポートしていないため、AndroidManifest.xml に送ってください。

  - SDK バージョン 1.7.0 以降では、ライブラリプロジェクトから「assets/fontawesome-webfont.ttf」をアプリケーションにコピーする必要があります。Eclipse はライブラリのアセットフォルダーを自動的に含めません。

[03]: https://github.com/braze-inc/braze-android-sdk "アプリボーイアンドロイド GitHub リポジトリ"
[04]: {{site.baseurl}}/assets/img_archive/file_import.png
[05]: {{site.baseurl}}/assets/img_archive/android_import.png
[06]: {{site.baseurl}}/assets/img_archive/click_browse.png
[07]: {{site.baseurl}}/assets/img_archive/select_project_android.png
[08]: {{site.baseurl}}/assets/img_archive/click_properties.png
[09]: {{site.baseurl}}/assets/img_archive/add_appboy_ui.png
[10]: {{site.baseurl}}/assets/img_archive/build_target.png
[11]: {{site.baseurl}}/assets/img_archive/android_support_v4.png
