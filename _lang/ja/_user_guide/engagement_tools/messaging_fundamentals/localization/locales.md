---
nav_title: メッセージ内のロケール
article_title: メッセージ内のロケール
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "ここでは、ロケールを使用する方法に関するステップについて説明します。"
---

# メッセージ内のロケール

> ロケールをワークスペースに追加した後、単一のプッシュ、メール、またはアプリ内メッセージ内のすべてのユーザーをさまざまな言語で対象にできます。

{% multi_lang_include locales.md section="Prerequisites" %}

{% alert important %}
メッセージの多言語サポートは、現在早期アクセス段階です。早期アクセスに参加することに興味がある場合は、Brazeのアカウントマネージャーに連絡してください。
{% endalert %}

## ロケールの使用

{% tabs %}
{% tab In-app message %}

メッセージングでロケールを使用するには、アプリ内メッセージキャンペーンまたはキャンバスを作成します。ドラッグアンドドロップエディタまたは従来のエディタのいずれかを選択し、エディタに基づいて手順を実行します。

{% subtabs %}
{% subtab traditional editor %}

1. 翻訳タグ{% raw %}`{% translation %}` と`{% endtranslation %}`{% endraw %} を追加して、翻訳するすべてのテキストと画像、リンクURLをラップする。 
2. 各翻訳タグに ID タグを追加します。例を挙げよう： {% raw %}`{% translation id_1 %}`{% endraw %}

![翻訳ID を持つ従来のエディタ。]({% image_buster /assets/img/multi-language_support/html_iam_editor_translation_tags.png %}){: style="max-width:60%;"}

{: start="3"}
3\.タグを追加したら、メッセージを下書きとして保存する。
4\.**言語の管理**を選択し、ドロップダウンを使用してメッセージのロケールを追加します。

!["languages"選択した1つのロケールでモーダルします。]({% image_buster /assets/img/multi-language_support/manage_languages_modal.png %})

{: start="5"}
5\.[**テンプレートをダウンロード**] を選択して、翻訳テンプレートを CSV ファイルとしてダウンロードします。次に、CSVファイルに翻訳を記入する。

![変換CSVファイルのサンプル。]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})

{: start="6"}
6. **Upload translationsを**選択し、翻訳が完了したCSVファイルをアップロードする。

{% endsubtab %}
{% subtab Drag-and-drop editor %}

1. 翻訳タグ{% raw %}`{% translation %}` と`{% endtranslation %}`{% endraw %} を追加して、翻訳するすべてのテキストと画像、リンクURLをラップする。 
2. 各翻訳タグに ID タグを追加します。例を挙げよう： {% raw %}`{% translation id_1 %}`{% endraw %} 

![2 つの変換ID を持つドラッグアンドドロップエディタ。]({% image_buster /assets/img/multi-language_support/dnd_iam_editor_translation_tags.png %}){: style="max-width:70%;"}

{: start="3"}
3\.タグを追加したら、メッセージを下書きとして保存してから、エディタを再度開きます。
4\.[**作成**] パネルで [**多言語サポート**] を選択し、そのドロップダウンを使用してメッセージのロケールを追加します。
5\.[**テンプレートをダウンロード**] を選択して、翻訳テンプレートを CSV ファイルとしてダウンロードします。 

!["多言語"ボタンを押してテンプレートを読み込むします。]({% image_buster /assets/img/multi-language_support/dnd_iam_download_template.png %}){: style="max-width:40%;"}

{: start="6"}
6. CSVファイルに翻訳を記入する。ステップ1から翻訳タグを直接コピー＆ペーストした場合は、CSVファイルの**翻訳タグ**欄から`<code>` 。
7. **Upload translationsを**選択し、翻訳が完了したCSVファイルをアップロードする。

!["多言語"テンプレートとアップロードの変換を読み込むするボタンがあるパネル。]({% image_buster /assets/img/multi-language_support/dnd_iam_upload_translations.png %}){: style="max-width:40%;"}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Email %}

メッセージングでロケールを使用するには、メールキャンペーンまたはキャンバスを作成します。HTMLエディタかドラッグ・アンド・ドロップ・エディタのいずれかを選択し、エディタに応じた手順に従う。

{% subtabs %}
{% subtab HTML editor %}

1. 翻訳するテキストを強調表示します。[**翻訳タグを挿入**] を選択します。これにより、テキストが翻訳タグで囲まれます。<br>![選択したロケールのエディタをHTMLします。]({% image_buster /assets/img/multi-language_support/html_editor_translation_tag_example.png %})
2. メッセージを下書きとして保存する。
3. [**多言語サポート**] を選択し、そのドロップダウンを使用してメッセージのロケールを追加します。
4. [**テンプレートをダウンロード**] を選択して、翻訳テンプレートを CSV ファイルとしてダウンロードします。次に、CSVファイルに翻訳を記入する。<br>![変換CSVファイルのサンプル。]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})
5. **Upload translationsを**選択し、翻訳が完了したCSVファイルをアップロードする。

{% endsubtab %}
{% subtab Drag-and-drop editor %}

1. 翻訳タグ{% raw %}`{% translation %}` と`{% endtranslation %}`{% endraw %} を追加して、翻訳するすべてのテキストと画像、リンクURLをラップする。 
2. 各翻訳タグに ID タグを追加します。例を挙げよう： {% raw %}`{% translation id_1 %}`{% endraw %}<br>![2 つの変換ID を持つドラッグアンドドロップエディタ。]({% image_buster /assets/img/multi-language_support/dnd_editor_translation_example.png %})
3. タグを追加したら、メッセージを下書きとして保存する。
4. [**多言語サポート**] を選択し、そのドロップダウンを使用してメッセージのロケールを追加します。
5. [**テンプレートをダウンロード**] を選択して、翻訳テンプレートを CSV ファイルとしてダウンロードします。 
6. CSVファイルに翻訳を記入する。ステップ1から翻訳タグを直接コピー＆ペーストした場合は、CSVファイルの**翻訳タグ**欄から`<code>` 。
7. **Upload translationsを**選択し、翻訳が完了したCSVファイルをアップロードする。

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Push %}

メッセージングでロケールを使用するには、プッシュキャンペーンまたはキャンバスを作成し、次の手順を実行します。

1. 翻訳タグs {% raw %}`{% translation id1%}` および`{% endtranslation %}`{% endraw %} を追加して、翻訳するすべての文字、"画像、またはリンクURL をラップします。各変換ID (`id1`) は一意である必要があります。

![通知コンポーザーを押し、変換タグsを題名とメールフィールドsに追加します。]({% image_buster /assets/img/multi-language_support/push_translation_tags.png %})

{: start="2"}
2\.メッセージを下書きとして保存します。
3\.**言語**を選択し、ドロップダウンを使用してメッセージのロケールを追加します。
4\.[**テンプレートをダウンロード**] を選択し、CSV テンプレート内に翻訳を入力します。

![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})

{: start="5"}
5\.完成した CSV テンプレートをアップロードするには、[**翻訳をアップロード**] を選択します。 

!["多言語メッセージ"ウィンドウでは、2つのロケールが選択され、テンプレートやアップロードの変換を下に読み込むします。]({% image_buster /assets/img/multi-language_support/upload_translation.png %})

{% endtab %}
{% endtabs %}

CSV ファイルの ID や ロケールに変更があっても、メッセージは自動的に更新されません。翻訳を更新するには、CSVファイルを更新し、ファイルを再アップロードする。

{% alert tip %}
キャンペーンとキャンバスの翻訳の管理および更新を行う方法については、[翻訳 API]({{site.baseurl}}/api/endpoints/translations) を参照してください。
{% endalert %}

### 右から左に読むメッセージ

右から左へ(アラビア語のように)書き込まれる言語の翻訳ファイルに入力する場合は、`span` を使用して翻訳をラップし、適切にフォーマットされます:```<span dir='rtl'>MESSAGE_TRANSLATION</span>```。

## ロケールのプレビュー

{% tabs %}
{% tab In-app message %}

[**メッセージをユーザーとしてプレビュー**] ドロップダウンの [**テスト**] タブで [**カスタムユーザー**] を選択します。異なる言語を入力してメッセージをプレビューし、メッセージが期待どおりに翻訳されるかどうかを確認します。


{% endtab %}
{% tab Email %}

**Preview & Test** セクションで、**Multi-language User** を選択して、メッセージが期待どおりに変換されるかどうかを確認します。

{% endtab %}
{% tab Push %}

[**メッセージをユーザーとしてプレビュー**] ドロップダウンの [**テスト**] タブで [**カスタムユーザー**] を選択します。異なる言語を入力してメッセージをプレビューし、メッセージが期待どおりに翻訳されるかどうかを確認します。

{% endtab %}
{% endtabs %}

## 翻訳をマネージャーする

### キャンペーンやキャンバスの翻訳を編集する

キャンペーンやキャンバスの開始後でも、下書きモードであれば翻訳を修正できます。これは、コンポーザーで直接翻訳を編集する場合でも、CSVアップロードを利用する場合でも、APIを利用する場合でも同じだ。 

翻訳を更新する前に、キャンペーンまたはキャンバスをまず下書きとして保存する必要があります。

1. [**キャンペーン/キャンバスを編集**] を選択し、作成画面で編集を行います。
2. [**下書きとして保存**] を選択し、モーダルで [**はい**] を選択します。
3. **設定確認**ステップに進み、[**キャンペーン/キャンバスを更新**] を選択します。
4. モーダルで [**キャンペーン/キャンバスを更新**] を選択します。

開始後のキャンペーンとキャンバスの管理については、[開始後のキャンペーンの編集]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/)と[キャンバスの下書きと開始後の編集]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_drafts/)を参照してください。

### キャンバスのステップまたはキャンペーンの複製と翻訳

キャンバスのステップやキャンペーンを複製する場合、立ち上げ後の下書きモードであれ、最初の作成中であれ、そのステップに関連する翻訳は引き継がれない。必要な翻訳は、新しいステップやキャンペーンに追加する必要がある。キャンバスやキャンペーンに修正を加える際には、必ず翻訳を確認し、適宜更新してください。

### Canvasesで多言語APIを使う

[キャンバスで多言語 API]({{site.baseurl}}/api/endpoints/translations/) を使用するには、パラメータリストに `workflow_id`、`step_id`、`message_variation_id` を含める必要があります。

#### 開始後の下書きに追加されたキャンバスステップ

キャンバス開始後に作成されたキャンバスステップで多言語 API を使用する場合、この API に渡す`message_variation_id` は空または空白になります。

## よくある質問

#### 自分のいずれかのロケールで翻訳文を変更できますか?
はい。まず、CSV で編集を行ってから、ファイルを再度アップロードすることで、翻訳文を変更します。

#### 翻訳タグをネストできますか?
いいえ。

#### 翻訳タグにHTMLスタイルを追加できるか？
はい。ただし、HTML のスタイル設定がコンテンツと一緒に翻訳されていないことを確認してください。

#### Brazeはどのような検証や追加チェックを行うのか？

| シナリオ                                                                                                                                                 | Braze での検証                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| 現在のメッセージに関連するロケールが翻訳ファイルにない。                                                                               | この翻訳ファイルはアップロードされない。                                                                       |
| 翻訳ファイルに、現在の電子メールメッセージから、リキッド翻訳タグ内のテキストなどのテキストブロックが欠落している。                                | この翻訳ファイルはアップロードされない。                                                                       |
| 翻訳ファイルには、現在のメール・メッセージのテキスト・ブロックと一致しないデフォルト・テキストが含まれている。                                          | この翻訳ファイルはアップロードされない。再アップロードを試みる前に、CSVでこれを修正する。               |
| 翻訳ファイルには、**多言語サポート**設定に存在しないロケールが含まれている。                                                           | これらのロケールは Braze に保存されません。                                                                      |
| 翻訳ファイルには、現在のメッセージ（翻訳がアップロードされた時点の草稿など）には存在しないテキストブロックが含まれる。 | 現在のメッセージに存在しないテキストブロックは、翻訳ファイルから Braze には保存されません。 |
| ロケールが翻訳ファイルの一部としてすでにメッセージにアップロードされた後に、メッセージからロケールを削除する。                           | ロケールを削除すると、メッセージ内のそのロケールに関連する翻訳がすべて削除される。                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }