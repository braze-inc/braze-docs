---
nav_title: Crowdin
article_title: Crowdin
description: "Crowdin の統合を使用して、翻訳メモリ、用語集、機械翻訳を活用しながら、キャンペーン、キャンバスエクスペリエンス、メールテンプレート、コンテンツブロックを翻訳できます。"
alias: /partners/crowdin/
page_type: partner
search_tag: Partner

---

# Crowdin

> [Crowdin](https://crowdin.com/) は、AI 駆動のローカライゼーション管理プラットフォームであり、ソフトウェア、アプリ、マーケティングコンテンツの翻訳を自動化するのに役立ちます。

Crowdin を Braze に接続して、キャンペーンやキャンバスエクスペリエンスの翻訳を管理できます。自動同期は機械翻訳、翻訳メモリ、用語集と連携するため、人手による翻訳ワークフローと自動化されたワークフローの一貫性が保たれます。

_この統合は Crowdin によって管理されています。_

## 統合について

Crowdin は Braze 向けに2つのアプリを提供しています：[Braze Campaigns & Canvas](https://store.crowdin.com/braze-content-translation) と [Braze Email Templates](https://store.crowdin.com/braze-app) です。ローカライズする Braze の機能に応じて選択してください。以下の表で比較できます。

### 適切な Crowdin アプリの選択

| チャネルまたは機能 | Braze Campaigns & Canvas | Braze Email Templates |
| --- | --- | --- |
| **キャンペーン** | ✅ 対応 | ❌ 非対応 |
| **キャンバスステップ** | ✅ 対応 | ❌ 非対応 |
| **メールテンプレート** | ❌ 非対応 | ✅ 対応 |
| **コンテンツブロック** | ❌ 非対応 | ✅ 対応 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| **Crowdin アカウント** | [Crowdin.com アカウント](https://accounts.crowdin.com/register)または [Crowdin Enterprise アカウント](https://accounts.crowdin.com/workspace/create)が必要です。 |
| **Crowdin プロジェクト** | Braze を接続する前に、Crowdin または Crowdin Enterprise で[翻訳プロジェクトを作成](https://support.crowdin.com/creating-project/)してください。 |
| **Braze REST API キー** | キャンペーン、キャンバス、コンテンツブロック、カスタム属性、メール、テンプレートの権限を持つ Braze REST API キー。 |
| **Braze REST エンドポイント** | お使いの Braze REST エンドポイント URL（例：`https://rest.iad-03.braze.com`）。 |
| **Braze 多言語設定** | Braze ダッシュボードの**「設定」**>**「ローカライゼーション設定」**でロケールを設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Braze Campaigns & Canvas 統合

ライブメッセージ内のコンテンツをローカライズする場合は、[Braze Campaigns & Canvas アプリ](https://store.crowdin.com/braze-content-translation)を使用して、キャンペーンやキャンバスの下書きから翻訳可能な文字列を Braze の多言語サポートと同期します。

動画によるウォークスルーについては、[Braze Campaigns & Canvas integration](https://youtu.be/ahG1ET4VRKA) をご覧ください。

### ステップ 1: Braze で多言語設定を行う

Crowdin を接続する前に、Braze でターゲット言語を追加します。

1. Braze で、**「設定」**>**「ローカライゼーション設定」**に移動します。
2. サポートする予定の言語を追加します。

![Braze の設定配下のロケールページ。ロケール名、ロケールキー、ロケールの追加が表示されています。]({% image_buster /assets/img/crowdin/braze_locales.png %})

{: start="3"}
3. 各**ロケールキー**（例：`en-US`、`fr-FR`、`es-ES`）をメモしてください。Crowdin で言語をマッピングする際にこれらの値を使用します。

### ステップ 2: Crowdin で Braze プロジェクトを設定する

1. Crowdin Enterprise または Crowdin.com アカウントで、左側メニューの**「Store」**に移動します。
2. **Braze Campaigns & Canvas** を検索し、**「Install」**を選択します。

![Crowdin Store で Braze Campaigns & Canvas が選択され、Install がハイライトされている画面。]({% image_buster /assets/img/crowdin/crowdin_store_campaigns_canvas.png %})

{: start="3"}
3. この統合を使用するプロジェクトを選択します。
4. 統合を開くには、プロジェクトの**「Integrations」**>**「Braze Campaigns & Canvas」**に移動します。

#### Braze を Crowdin に接続する

Braze API 認証情報を使用して接続を認可します：

![Crowdin の Braze Campaigns & Canvas 接続フォーム。REST API キー、REST エンドポイント、Log in with Braze Campaigns & Canvas が表示されています。]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_login.png %})

- **Braze REST API キー：** Braze の**「設定」**>**「API と識別子」**>**「API キー」**で作成します。この統合に必要な権限（キャンペーン、キャンバス、コンテンツブロック、カスタム属性）を付与してください。
- **Braze REST エンドポイント：** お使いのBrazeインスタンスの URL を入力します（例：`https://rest.iad-03.braze.com`）。詳細については、[REST API エンドポイント]({{site.baseurl}}/api/basics/#endpoints)を参照してください。

![Braze REST API キーページ。API キーの作成と REST エンドポイントのコピーコントロールが表示されています。]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

**「Log in with Braze Campaigns & Canvas」**を選択します。

### ステップ 3: Crowdin で言語マッピングを設定する

アカウントを接続したら、Crowdin プロジェクトの各言語を対応する Braze ロケールにマッピングします。

1. **Braze Campaigns & Canvas** 統合ダッシュボードで、右上の**「Settings」**歯車アイコンを選択します。

![Braze Campaigns & Canvas 統合画面。上部のアクションバーに Settings が表示されています。]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_settings.png %})

{: start="2"}
2. **「General Settings」**タブを開きます。
3. ロケールキーを入力します。Crowdin にはプロジェクトの言語（例：French、Italian）が一覧表示されます。各フィールドに、対応する **Braze ロケールキー**を入力します。
   - 例えば、Braze でイタリア語に `it` を使用している場合、Crowdin の Italian の横に `it` と入力します。
   - 各エントリは、Braze の**「ローカライゼーション設定」**にあるそのロケールの**ロケールキー**と正確に一致する必要があります。

![Settings モーダルの General Settings タブ。ファイルフィルターフィールドと言語マッピング行（例：French が fr にマッピング）が表示されています。]({% image_buster /assets/img/crowdin/crowdin_language_mapping_settings.png %})

{: start="4"}
4. **「Save」**を選択してマッピングを確定します。

### ステップ 4: Braze メッセージに翻訳タグを追加する

Crowdin は、Braze が多言語メッセージに使用するのと同じ Liquid **翻訳タグ**を読み取ります。翻訳したいテキスト、画像 URL、リンク URL のすべてを {% raw %}`{% translation your_id_here %}` と `{% endtranslation %}`{% endraw %} で囲みます。各ブロックには一意の `id`（例：`greeting` や `welcome_header`）が必要です。

**例：**

{% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

HTML、リンク内の Liquid、その他のパターンについては、[ロケールの翻訳]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales)と同じルールに従ってください（例：タグはできるだけ小さなセグメントの周りに配置し、リンクをローカライズする際は言語固有の部分のみを囲みます）。

Crowdin がコンテンツを検出して取得できるように、Braze メッセージを**下書き**として保存してください。

### ステップ 5: Crowdin で翻訳を管理する

統合画面には2つの側面があります：

- **右側（Braze）：** キャンペーンとキャンバス。
- **左側（Crowdin）：** 翻訳用に同期済みのコンテンツ。

![Crowdin と Braze Campaigns & Canvas パネル。キャンペーンとロケールのフォルダー、Sync to Braze、Sync to Crowdin が表示されています。]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_sync_panels.png %})

#### コンテンツの同期

1. **Braze（右側）**で、翻訳するキャンペーンまたはキャンバスのチェックボックスを選択します。
2. **「Sync to Crowdin」**を選択します。
3. 同期が完了すると、ファイルが **Crowdin（左側）**に表示されます。翻訳者は Crowdin エディターで文字列を開くことができます。

#### 翻訳を Braze に戻す

1. Crowdin で翻訳が100%完了したら、**「Integrations」**タブに戻ります。
2. **Crowdin（左側）**で完了したコンテンツを選択します。
3. **「Sync to Braze」**を選択します。これにより、翻訳された文字列が Braze キャンペーンの対応する言語バリアントにプッシュされます。

### ステップ 6: Braze で多言語ユーザーとしてメッセージをプレビューする

統合を確認するには：

1. **Braze メッセージ作成画面**でキャンペーンを開きます。
2. **「テスト」**タブに移動します。
3. **「ユーザーとしてメッセージをプレビュー」**を選択します。
4. 翻訳済みロケールのいずれかに一致する `language` 属性を持つユーザープロファイルを検索します。
5. コンテンツがソース言語から翻訳版に切り替わることを確認します。

## Braze Email Templates 統合

テンプレートレベルでメールをローカライズする場合は、[Braze Email Templates アプリ](https://store.crowdin.com/braze-app)を使用して、Braze メディアライブラリーから HTML を同期します。

動画によるウォークスルーについては、[Braze Email Templates integration](https://youtu.be/g0YMKW3jEjk) をご覧ください。

### ステップ 1: アプリをインストールする

1. Crowdin プロジェクトで、**「Store」**タブに移動します。
2. **Braze Email Templates** を検索し、**「Install」**を選択します。

![Crowdin Store で Braze Email Templates が選択され、Install がハイライトされている画面。]({% image_buster /assets/img/crowdin/crowdin_store_email_templates.png %})

{: start="3"}
3. この統合を使用するプロジェクトを選択します。
4. 統合を開くには、プロジェクトの**「Integrations」**>**「Braze Email Templates」**に移動します。

### ステップ 2: Braze に接続する

Braze API 認証情報を使用して接続を認可します：

![Crowdin の Braze Email Templates 接続フォーム。REST API キー、REST エンドポイント、Log in with Braze Email Templates が表示されています。]({% image_buster /assets/img/crowdin/crowdin_email_templates_login.png %}){: style="max-width:85%;"}

1. **Braze REST API キー：** `templates.email` と `content_blocks`（読み取りおよび書き込み）の権限を付与します。Braze の**「設定」**>**「API と識別子」**>**「API キー」**でキーを作成します。

![Braze REST API キーページ。API キーの作成と REST エンドポイントのコピーコントロールが表示されています。]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

{: start="2"}
2. **Braze REST エンドポイント**には、インスタンス固有の URL を使用します（例：`https://rest.iad-03.braze.com`）。
3. **「Log in with Braze Email Templates」**を選択します。

### ステップ 3: 翻訳用にコンテンツを同期する

統合画面には Braze ライブラリーが表示されます：

- **右側（Braze）：** 同期可能な**メールテンプレート**と**コンテンツブロック**。
- **左側（Crowdin）：** 翻訳中のコンテンツ。

1. **Braze（右側）**で、ローカライズしたいテンプレートまたはブロックの横にあるチェックボックスを選択します。
2. **「Sync to Crowdin」**を選択します。
3. Crowdin が HTML ソースを取得します。翻訳者はライブ **WYSIWYG プレビュー**付きの Crowdin エディターで作業できるため、レイアウトが維持されます。

![Crowdin エディターのプレビュータブ。ローカライズされたメール HTML と翻訳可能な文字列が表示されています。]({% image_buster /assets/img/crowdin/crowdin_editor_wysiwyg_preview.png %}){: style="max-width:85%;"}

### ステップ 4: 翻訳済みテンプレートを配信する

翻訳が100%完了したら：

1. **Crowdin（左側）**で完了したファイルを選択します。
2. **「Sync to Braze」**を選択します。
3. Crowdin が Braze メディアライブラリーにこれらのアセットのローカライズ版を自動的に作成します（例：`Template_Name_fr`）。

![Crowdin と Braze Email Templates パネル。メールテンプレートとコンテンツブロックが一覧表示され、Sync to Braze と Sync to Crowdin が表示されています。]({% image_buster /assets/img/crowdin/crowdin_email_templates_sync_panels.png %})