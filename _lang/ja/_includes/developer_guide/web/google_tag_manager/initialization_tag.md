### 前提条件

この統合方法を使用する前に、[Googleタグマネージャ](https://support.google.com/tagmanager/answer/14842164)のアカウントとコンテナを作成する必要があります。

### ステップ 1: タグ テンプレートギャラリーを開く

[Googleタグマネージャ](https://tagmanager.google.com/)で、ワークスペースを選択し、**Templates**を選択します。**Tag Template**ペインで、**Search Gallery**を選択します。

![Google Tag Manager.]({% image_buster /assets/img/web-gtm/search_tag_template_gallery.png %})のサンプルワークスペースのテンプレート s ページ{: style="max-width:95%;"}

### ステップ 2:初期化タグ テンプレートの追加

テンプレートギャラリーで`braze-inc` を検索し、**Braze初期化タグ** を選択します。

![さまざまな'braze-inc' テンプレートs.]({% image_buster /assets/img/web-gtm/template_gallery_results.png %})を示すテンプレートギャラリー{: style="max-width:80%;"}

**ワークスペースに追加**> **追加**を選択します。

![Googleタグマネージャの「Braze初期化タグ」ページ]({% image_buster /assets/img/web-gtm/add_to_workspace.png %}){: style="max-width:70%;"}

### ステップ 3:タグの設定

**テンプレート s** セクションから、新しく追加したテンプレートを選択します。

![" テンプレート s" Google タグマネージャのページに、Braze初期化タグテンプレートが表示されます。]({% image_buster /assets/img/web-gtm/select_tag_template.png %}){: style="max-width:95%;"}

鉛筆アイコンを選択し、**Tag Configuration**ドロップダウンを開封します。

![タグ設定タイル。'pencil' アイコンが表示されます。]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

必要最小限の情報を入力します。

| フィールド         | 説明 |
| ------------- | ----------- |
| **API キー**   | **設定**> **アプリ設定**のBraze ダッシュボードにある[Braze APIキー]({{site.baseurl}}/api/basics/#about-rest-api-keys)。 |
| **API エンドポイント** | RESTエンドポイントのURL。エンドポイントは、[インスタンス]({{site.baseurl}}/api/basics/#endpoints)のBraze URLによって異なります。 |
| **SDK バージョン**  | [changelog]({{site.baseurl}}/developer_guide/changelogs/?sdktab=web)にリストされているWeb Braze SDKの最新の`MAJOR.MINOR`バージョン。たとえば、最新バージョンが`4.1.2` の場合、`4.1` と入力します。詳細については、[SDKバージョン管理について]({{site.baseurl}}/developer_guide/sdk_integration/version_management/)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

追加の初期化設定では、**Braze初期化オプション**を選択し、必要なオプションを選択します。

!['Tag Configuration'.]({% image_buster /assets/img/web-gtm/braze_initialization_options.png %})にあるBraze初期化オプションの一覧{: style="max-width:65%;"}

### ステップ 4: *すべてのページでトリガに設定*

初期化タグは、サイトのすべてのページで実行する必要があります。これにより、Braze SDKメソッドを使用したり、Web プッシュ 分析を録音したりできます。

### ステップ 5: 統合を検証する

次のいずれかのオプションを使用して、統合を確認できます。

- **オプション 1:**Googleタグマネージャの[デバッグツール](https://support.google.com/tagmanager/answer/6107056?hl=en)を使用して、Braze初期化タグが設定されたページまたはイベントで正しくトリガーされているかどうかを確認できます。
- **オプション 2:**ウェブページからBrazeへのネットワークリクエストを確認します。さらに、グローバル`window.braze` ライブラリーを定義する必要があります。
