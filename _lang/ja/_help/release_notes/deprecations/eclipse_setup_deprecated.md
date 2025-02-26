---
nav_title: EclipseでSDKを初期セットアップする
page_order: 1

page_type: update
description: "このアーカイブ記事では、EclipseでSDKの初期セットアップを行う方法を説明する。BrazeはEclipse IDEのサポートを廃止した。"
---

# EclipseでSDKを初期セットアップする

{% alert update %}
Google が Eclipse Android Developer Tools プラグインの[サポートを終了](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html)したため、Braze は Eclipse IDE のサポートを中止しました。移行前に Eclipse の統合に関するサポートが必要な場合は、[サポートにメールで]({{site.baseurl}}/support_contact/)お問い合わせください。
{% endalert %}

## ステップ 1
コマンドラインで、[Braze Android GitHub リポジトリ][03]を複製します。

```bash
$ git clone git@github.com:braze-inc/braze-android-sdk.git
```

## ステップ 2
Brazeプロジェクトをローカルのワークスペースにインポートする。

Eclipse の場合:

  - [ファイル] > [インポート] に移動します。

    ![ファイルインポート][04]
  - [Android] > [ワークスペースに存在する Android コード] を選択します。

    ![Androidドインポート][05]
  - [参照] をクリックします。

    ![参照][06]
  - Braze UI プロジェクトフォルダーを確認し、「プロジェクトをワークスペースにコピー」して、[終了] をクリックします。

    ![Android UI プロジェクトを選択する][07]

## ステップ 3
自分のプロジェクトでBrazeを参照する。
Eclipse の場合:

  - プロジェクトを右クリックし、"Properties "を選択する。

    ![プロパティをクリックする][08]
  - [Android] で、[ライブラリー] セクションの [追加...]" をクリックし、android-sdk-ui をライブラリーとしてアプリに追加します。

    ![Braze 追加][09]

## ステップ 4
依存性エラーを解決し、ビルドターゲットを修正する。

このとき、Brazeのコードでエラーが出るかもしれないが、これは依存関係が入力されておらず、ビルドターゲットが間違っている可能性があるためだ：

   - Braze UI プロジェクトを右クリックし、[プロパティ] -> [Android] を選択して、ビルドターゲットが Braze の最新ビルドツールバージョンに設定されていることを確認します。

      ![ビルドターゲット][10]
   - Braze UI プロジェクトを右クリックし、[プロパティ] -> [Java ビルドパス] -> [JAR を追加...] を選択して、メインアプリケーションから「android-support-v4.jar」をライブラリーとして追加します。

      ![サポート][11]

## ステップ5

最終ピースを追加します。

  - SDK バージョン1.10.0以降の場合は、
  `<service android:name="com.appboy.services.AppboyDataSyncService" />`
  を AndroidManifest.xml に追加する必要があります。Eclipse ではマニフェストマージがサポートされていないためです。

  - SDK バージョン1.7.0以降では、「assets/fontawesome-webfont.ttf」をライブラリープロジェクトからアプリケーションにコピーする必要があります。Eclipse には、ライブラリーのアセットフォルダは自動的には含まれません。

[03]: https://github.com/braze-inc/braze-android-sdk "Appboy Android GitHubリポジトリ"
[04]: {{site.baseurl}}/assets/img_archive/file_import.png
[05]: {{site.baseurl}}/assets/img_archive/android_import.png
[06]: {{site.baseurl}}/assets/img_archive/click_browse.png
[07]: {{site.baseurl}}/assets/img_archive/select_project_android.png
[08]: {{site.baseurl}}/assets/img_archive/click_properties.png
[09]: {{site.baseurl}}/assets/img_archive/add_appboy_ui.png
[10]: {{site.baseurl}}/assets/img_archive/build_target.png
[11]: {{site.baseurl}}/assets/img_archive/android_support_v4.png
