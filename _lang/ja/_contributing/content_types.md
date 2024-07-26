---
nav_title: コンテンツタイプ
article: Content Types
page_order: 4
---

# コンテンツタイプ

> Braze Docsは[Diátaxisフレームワーク](https://diataxis.fr/)に従っており、各ページを4つのコンテンツタイプのいずれかに分類し、それぞれが異なる学習目標を満たしています。Braze Docsの単一ページには複数のコンテンツタイプが含まれている場合がありますが、各タイプにはページに専用のセクションを設ける必要があります。

これらはBraze Docsで見つけることができるコンテンツタイプです:

| ドキュメントタイプ | 目的 |
| --- | --- |
| [ハウツーガイド](#how-to-guides) | ユーザーが知識を**適用する**のを助ける。 |
| [チュートリアル](#tutorials) | ユーザーが**知識を得る**のを助ける。 |
| [参考文献](#references) | ユーザーに**技術的な知識**を提供する。 |
| [説明](#explanations) | ユーザーの**文脈に応じた知識**を広げる。 |
| [リリースノート](#release-notes) | ユーザーに製品の更新について通知します。 |

## テンプレートの使用

各コンテンツタイプには、Braze Docsで[ページ]({{site.baseurl}}/contributing/content_management/pages/)や[セクション]({{site.baseurl}}/contributing/content_management/sections/)を作成するために使用できる専用のテンプレートがあります。

テンプレートの各セクションについて詳しく知るには、次のようなHTMLコメントを読んでください:

```markdown
<!-- Here's an HTML comment! -->
```

{% alert important %}
これらのコメントをファイルに書き込んでいる間は保持できますが、公開する前に削除する必要があります。
{% endalert %}

## コンテンツタイプ

### ハウツーガイド

ハウツーガイドは、特定のタスクを完了する方法をユーザーに示す、アクションベースの時系列ステップです。例については、[コンテンツカードの作成]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/)を参照してください。

![「コンテンツカードの作成」ページのスクリーンショット。]({% image_buster /assets/img/contributing/content_types/how_to_guide_example.png %}){: style="max-width:70%;"}

{% multi_lang_include contributing/templates/how_to_guide.md %}

#### ガイドライン

- ユーザーがアクションを起こすために知っておくべきことだけをカバーする。 
- タスクを完了するための最良または推奨される方法のみをカバーしてください。文書の代替方法を提供しないでください。
- エンドユーザーの目標に不可欠な[参考資料](#references)のみを含めてください。例えば、ステップ中にユーザーが選択できるオプションのリストなどです。
- 同じ記事に含めるには長すぎる参考文献へのリンクを張ります。例えば、[セグメンテーションフィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/)などです。
- トラブルシューティングの手順を提供しないでください。代わりに、この情報をこのページの別のセクションまたは別の記事に含めることができます。

#### ヘッダー構文

H2ヘッダー（`##`Markdown）にはアクション指向で、このステップの一般的な目標を反映する必要があります。任意の手順がある場合は、ヘッダーに`(Optional)`を追加します。以下に例を示します。

{% raw %}
```
## Creating a page

1. Open the relevant directory in `braze-docs`.
2. Create a new Markdown file for your page.
3. Use a filename that follows our [naming guidelines](#naming-guidelines).
4. (Optional) You can generate a preview by running `rake` in your terminal.
```
{% endraw %}

長いまたは複雑な手順の場合、関連する手順をグループ化するためにネストされたヘッダーを使用します。任意の手順がある場合は、ヘッダーに`(optional)`を追加します。以下に例を示します。

{% raw %}
``````markdown
## Creating a page

### Step 1: Create a new file

Open the relevant directory, then create a new Markdown file for your page.

```plaintext
PAGE_TITLE.md
```

### Step 2: Add a template

Copy and paste one of the following templates into your Markdown file. For more information, see [Templates]({{site.baseurl}}/contributing/templates/).

### Step 3: Generate a preview (optional)

To generate a preview, open your terminal and run the following command:

```bash
rake
```
``````
{% endraw %}

### チュートリアル

チュートリアルは学習指向の実践的なレッスンです。彼らは、ユーザーが用語に慣れること、物事がどのように相互作用するか、コマンドの使い方など、学ぶことに焦点を当てています。例については、[ルールベースの推奨事項]({{site.baseurl}}/user_guide/sage_ai/recommendations/rules_based_recommendations/)を参照してください。

![「ルールベースの推奨事項」ページのスクリーンショット。]（{% image_buster /assets/img/contributing/content_types/tutorial_example.png %}）{: style="max-width:70%;"}

{% multi_lang_include contributing/templates/tutorial.md %}

#### ガイドライン

- ユーザーが従ったりロールプレイしたりするためのガイド付きのステップバイステップのアクティビティやシナリオを作成します。 
- ユーザーがアクティビティ中に使用されるプラットフォーム、ツール、またはワークフローにほとんど馴染みがないと仮定します。

{% alert tip %}
ユーザーが入力するための既製のアセットを提供しますが、それはあなたのチュートリアルの主要な焦点ではありません。例えば、キャンペーンを作成する際に、さまざまな機能の使い方を教えるチュートリアルのために、写真、メッセージング、Liquidコーディングを提供することができます。
{% endalert %}

##### ヘッダー構文

タイトルヘッダーは`Tutorial:`で先頭に追加され、一般的にユーザーが行うことや作成するものを説明する必要があります。例えば、「チュートリアル：あなたの最初の貢献 

### 参考文献

参考文献は情報指向のコンテンツです。彼らはユーザーに客観的で権威のある技術的な知識を提供することに焦点を当てています。例については、[メッセージエンゲージメントイベント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/)（イベント用語集）を参照してください。

![「メッセージエンゲージメントイベント」ページのスクリーンショット。]({% image_buster /assets/img/contributing/content_types/reference_example.png %}){: style="max-width:70%;"}

{% multi_lang_include contributing/templates/reference.md %}

#### ガイドライン

- タスクを完了するために必要な技術的な説明や情報を作成します。
- 情報をアルファベット順、カテゴリ別、または階層別に整理します。
- 参照は、それぞれの記事に配置します。ただし、1つの記事に対して長すぎる場合や、複数の記事で参照される場合は除きます。 
    - それらが単一のハウツーガイドでのみ参照され、手順の流れを妨げるほど長い場合は、それらを[折りたたみ可能にする]({{site.baseurl}}/contributing/styling_examples/#collapsible-content)ことができます。

##### ヘッダー構文

最上位は名詞であるべきです。例えば、[Editor blocks]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/)の参照には次の名前があります:

![「エディターブロック」ページのインページ目次のスクリーンショット。見出しには以下が含まれます:タイプ (H2)、プロパティ (H2)、タイトル (H3)、段落 (H3)、リスト (H3)、ボタン (H3)、区切り (H3)、スペーサー (H3)、画像 (H3)、動画 (H3)、ソーシャル (H3)、アイコン (H3)、HTML (H3)、メニュー (H3)。]({% image_buster /assets/img/contributing/content_types/explanation_header_syntax_example.png %}){: style="max-width:25%;"}

### 説明

説明は理解志向のコンテンツです。彼らはユーザーの概念的理解を向上させることに焦点を当てています。例については、「[入門」を参照してください。Braze概要]({{site.baseurl}}/user_guide/getting_started/overview/)。

![「はじめに」のスクリーンショット:Braze概要"ページ。]({% image_buster /assets/img/contributing/content_types/explanation_example.png %}){: style="max-width:70%;"}

{% multi_lang_include contributing/templates/explanation.md %}

#### ガイドライン

- 概念のテキストまたは視覚的な説明を作成します。例えば、データが機能、サードパーティのパートナー、ツールなどの間をどのように移動するかなどです。
- 機能や技術がユーザーにどのように利益をもたらすかについて議論する。
- 最も関連性の高い記事に説明を配置します。たとえば、基本的な機能記事には、その機能のワークフローを説明する「仕組み」という説明が含まれている場合があります。 
- 説明が1つの記事に収まりきらない場合は、[キャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns)のような一般的なトピックのランディングページに配置することを検討してください。

{% alert tip %}
説明は特定の結果を達成するためにユーザーに何をすべきかを伝えるものではありませんが、一般的な目標を達成するための時系列のステップを大まかに説明することができます（例えば、ABテストを使用してメッセージングを改善するなど）。同じ詳細に入らないでください [how-to guide](#how-to-guides) または [tutorial](#tutorials)。
{% endalert %}

##### ヘッダー構文

H1 ヘッダー (`#` in Markdown) は `About TOPIC_NAME` としてフォーマットされます。説明が異なるコンテンツタイプのページのサブセクションである場合、**説明**を意味する限り、構文を調整できます。**方法**ではありません。ここにいくつかの例があります:

- `About TOPIC_NAME`
- `TOPIC_NAME overview`
- `How TOPIC works`
- `How TOPIC is handled`
- `What does Braze check?`

### リリースノート

リリースノートは、Brazeの製品アップデートを毎月まとめたものです。各{更新}は次のカテゴリのいずれかに配置されます:

| カテゴリー               | 説明                                                             |
|------------------------|-------------------------------------------------------------------------|
| データの柔軟性       | データ構造化、保存、およびアクセスの改善に関する更新。             |
| 創造性の解放   | プラットフォーム内でユーザーの創造性を高める機能。              |
| 強力なチャネル        | 通信チャネルの信頼性とスケーラビリティの更新。   |
| AIとMLオートメーション   | プラットフォーム内のAIおよび機械学習機能の更新。                  |
| 新しいBrazeのパートナーシップ | 新しいプラットフォームやサービスとの統合を導入します。          |
| SDKの更新            | 新しいSDKまたは更新をリストし、重大な変更や新機能を含みます。 |
{: .reset-td-br-1 .reset-td-br-2}

このテンプレートを使用して、Braze Docsのリリースノートを作成できます。例については、[2024年1月9日のリリース]({{site.baseurl}}/help/release_notes/2024/1_9_24/)を参照してください。

{% multi_lang_include contributing/templates/release_notes.md %}
