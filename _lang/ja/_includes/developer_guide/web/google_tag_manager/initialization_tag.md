### 前提条件

この統合方法を使う前に、[Googleタグマネージャーのアカウントとコンテナを作成する](https://support.google.com/tagmanager/answer/14842164)必要がある。

### ステップ 1: タグテンプレートギャラリーを開封する

[Googleタグマネージャーで](https://tagmanager.google.com/)、ワークスペースを選択し、**テンプレートを**選択する。**タグテンプレートペインで**、**ギャラリーを検索を**選択する。

![Google Tag Managerのワークスペース例のテンプレートページ。]({% image_buster /assets/img/web-gtm/search_tag_template_gallery.png %}){: style="max-width:95%;"}

### ステップ 2:初期化タグのテンプレートを追加する

テンプレートギャラリーで、`braze-inc` を検索し、**Braze Initialization Tagを**選択する。

![様々な「Braze-inc」テンプレートを紹介するテンプレートギャラリー。]({% image_buster /assets/img/web-gtm/template_gallery_results.png %}){: style="max-width:80%;"}

**Add to workspace**>**Addを**選択する。

![Googleタグマネージャーの「Braze初期化タグ」ページ。]({% image_buster /assets/img/web-gtm/add_to_workspace.png %}){: style="max-width:70%;"}

### ステップ 3:タグを設定する

**テンプレート・**セクションから、新しく追加したテンプレートを選択する。

![Googleタグマネージャーの「テンプレート」ページにBraze初期化タグのテンプレートが表示されている。]({% image_buster /assets/img/web-gtm/select_tag_template.png %}){: style="max-width:95%;"}

鉛筆のアイコンを選択し、**タグ設定の**ドロップダウンを開封する。

![鉛筆」アイコンが表示されたタグ・コンフィギュレーション・タイル。]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

最低限必要な情報を入力する：

| フィールド         | 説明 |
| ------------- | ----------- |
| **API キー**   | [Braze]({{site.baseurl}}/api/basics/#about-rest-api-keys)ダッシュボードの**「設定」**>「**アプリ設定**」にある[APIキー]({{site.baseurl}}/api/basics/#about-rest-api-keys)。 |
| **API エンドポイント** | RESTエンドポイントのURL。エンドポイントは、[インスタンス]({{site.baseurl}}/api/basics/#endpoints)のBraze URLによって異なります。 |
| **SDK バージョン**  | [変更履歴に]({{site.baseurl}}/developer_guide/changelogs/?sdktab=web)記載されているWeb Braze SDKの最新の`MAJOR.MINOR` 。たとえば、最新バージョンが`4.1.2` の場合、`4.1` と入力します。詳しくは、[SDKのバージョン管理についてを]({{site.baseurl}}/developer_guide/sdk_integration/version_management/)参照のこと。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

追加の初期化設定については、**Braze Initialization Optionsを**選択し、必要なオプションを選択する。

![タグ設定」の下にあるBraze初期化オプションのリスト。]({% image_buster /assets/img/web-gtm/braze_initialization_options.png %}){: style="max-width:65%;"}

### ステップ 4: *すべてのページで*トリガーに設定する

初期化タグは、サイトのすべてのページで実行する必要がある。これにより、Braze SDKのメソッドを使用し、Webプッシュ分析を記録することができる。

### ステップ 5: 統合を確認する

以下のいずれかのオプションを使用して、統合を検証することができる：

- **オプション 1:**Googleタグマネージャーの[デバッグツールを使って](https://support.google.com/tagmanager/answer/6107056?hl=en)、設定したページやイベントでBraze初期化タグが正しくトリガーされているか確認できる。
- **オプション 2:**WebページからBrazeへのネットワークリクエストをチェックする。さらに、グローバルな`window.braze` ライブラリーを定義する必要がある。
