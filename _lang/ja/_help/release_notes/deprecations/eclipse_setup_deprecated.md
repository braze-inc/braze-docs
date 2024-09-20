---
nav_title: EclipseでSDKを初期セットアップする
page_order: 1

page_type: update
description: "このアーカイブ記事では、EclipseでSDKの初期セットアップを行う方法を説明する。BrazeはEclipse IDEのサポートを廃止した。"
---

# EclipseでSDKを初期セットアップする

{% alert update %}
[GoogleがEclipse Android Developer Tools Pluginのサポートを終了した](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html)ため、BrazeはEclipse IDEのサポートを終了した。移行前にEclipseとの統合についてサポートが必要な場合は、[サポートまでEメールで]({{site.baseurl}}/support_contact/)問い合わせを。
{% endalert %}

## ステップ 1
コマンドラインで、[Braze Android GitHub Repositoryを][03]クローンする。

```bash
$ git clone git@github.com:braze-inc/braze-android-sdk.git
```

## ステップ 2
Brazeプロジェクトをローカルのワークスペースにインポートする。

エクリプス』だ：

  - ファイル＞インポートに移動する。

    ![ファイルインポート][04]
  - Android > Existing Android Code into Workspaceを選択する。

    ![Androidドインポート][05]
  - Browse "をクリックする。

    ![ブラウズ][06]
  - Braze UIプロジェクトフォルダと "copy project into workspace "にチェックを入れ、"Finish "をクリックする。

    ![Android UIプロジェクトを選択する][07]

## ステップ 3
自分のプロジェクトでBrazeを参照する。
エクリプス』だ：

  - プロジェクトを右クリックし、"Properties "を選択する。

    ![プロパティをクリックする][08]
  - Android」で、Libraryセクションの「Add...」をクリックし、アプリにライブラリとしてandroid-sdk-uiを追加する。

    ![ブレイズ・アッド][09]

## ステップ 4
依存性エラーを解決し、ビルドターゲットを修正する。

このとき、Brazeのコードでエラーが出るかもしれないが、これは依存関係が入力されておらず、ビルドターゲットが間違っている可能性があるためだ：

   - Braze UIプロジェクトを右クリックし、Properties->Androidを選択し、ビルドターゲットがBrazeの現在のビルドツールバージョンに設定されていることを確認する。

      ![ビルド・ターゲット][10]
   - Braze UIプロジェクトを右クリックし、Properties->Java Build Path->Add JARs...を選択し、メインアプリケーションの'android-support-v4.jar'をライブラリとして追加する。

      ![サポート][11]

## ステップ5

最後のピースを加える。

  - SDKのバージョンが1.10.0以上の場合、次のように追加する必要がある。
  `<service android:name="com.appboy.services.AppboyDataSyncService" />`
  AndroidManifest.xmlEclipseはマニフェストのマージをサポートしていない。

  - SDKバージョン1.7.0以上の場合、ライブラリ・プロジェクトから "assets/fontawesome-webfont.ttf" をアプリケーションにコピーする必要がある。Eclipseはライブラリからassetsフォルダを自動的にインクルードしない。

[03]: https://github.com/braze-inc/braze-android-sdk "Appboy Android GitHubリポジトリ"
[04]: {{site.baseurl}}/assets/img_archive/file_import.png
[05]: {{site.baseurl}}/assets/img_archive/android_import.png
[06]: {{site.baseurl}}/assets/img_archive/click_browse.png
[07]: {{site.baseurl}}/assets/img_archive/select_project_android.png
[08]: {{site.baseurl}}/assets/img_archive/click_properties.png
[09]: {{site.baseurl}}/assets/img_archive/add_appboy_ui.png
[10]: {{site.baseurl}}/assets/img_archive/build_target.png
[11]: {{site.baseurl}}/assets/img_archive/android_support_v4.png
