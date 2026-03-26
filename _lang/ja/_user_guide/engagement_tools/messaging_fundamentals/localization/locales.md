---
nav_title: メッセージ内のロケール
article_title: ローカライゼーションの翻訳
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "この記事では、メッセージでロケールを使用する方法についてのステップを説明します。"
---

# ローカライゼーションの翻訳

> ワークスペースにロケールを追加した後、単一のプッシュ通知、メール、バナー、アプリ内メッセージ、またはコンテンツブロック内で、異なる言語のユーザーをすべてターゲットにできます。

{% multi_lang_include locales.md section="Prerequisites" %}

## ロケールの使用

### ステップ 1:ワークスペースにロケールを設定する {#workspace-setup}

ロケールと翻訳タグを使用する前に、まず[ワークスペースにロケールを追加する]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings)必要があります。

### ステップ 2:メッセージに翻訳用 Liquid タグを追加する {#add-translation-tags}

翻訳するすべてのテキスト、画像、リンクURLを囲むために、{% raw %}`{% translation your_id_here %}` と `{% endtranslation %}`{% endraw %} の翻訳タグを追加します。

各翻訳には固有の `id` が必要です。例えば、簡単な挨拶を翻訳する場合、IDを「greeting」と名付けることができます：

{% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

#### HTML ブロックのローカライゼーション

より複雑な段落には複数の翻訳タグ（「offer_text」と「offer_amount」）が含まれる場合があります：

{% raw %}
```
{% translation offer_text %}Sign up now to save{% endtranslation %}
<b>{% translation offer_amount %}50% Off{% endtranslation %}</b>
```
{% endraw %}

{% alert important %}
大きな HTML ブロックを翻訳タグで囲むと、スタイルシートやスタイル設定の問題を引き起こすことがあります。可能な限り小さなテキストセクションを囲むようにしてください。
{% endalert %}

#### リンクのローカライゼーション

アンカータグのリンクをローカライズする際は、`href` URL 属性全体ではなく、**言語固有の部分だけを**囲むようにしてください。URL 全体を囲むと、リンクのテンプレート機能が正しく動作しない可能性があります。

##### 正しい使い方

{% raw %}
```
<a href="https://www.braze.com/{% translation link_href %}en{% endtranslation %}/page"></a>
```
{% endraw %}

##### 誤った使い方

{% raw %}
```
<a href="{% translation link_href %}https://www.braze.com/en/page{% endtranslation %}"></a>
```
{% endraw %}

### ステップ 3:メッセージのロケールを選択する {#choose-locales}

翻訳タグをメッセージに追加したら、そのメッセージの多言語設定に移動し、翻訳対象のロケールを1つ以上選択します。

![ロケールを選択するドロップダウンフィールドがある多言語設定。]({% image_buster /assets/img/multi-language_support/manage_language_dropdown.png %}){: style="max-width:80%;"}

{% tabs %}
{% tab Email %}
メッセージを編集する際に、コンテンツメニューから**「多言語」**を選択します。

![メールの多言語設定。]({% image_buster /assets/img/multi-language_support/email_multi_language.png %}){: style="max-width:45%;"}

{% endtab %}

{% tab Push %}
メッセージを編集する際に**「言語の管理」**を選択します。

![プッシュ通知の多言語設定。]({% image_buster /assets/img/multi-language_support/push_manage_languages.png %})

{% endtab %}

{% tab In-app message %}
{% subtabs %}
{% subtab Drag-and-Drop Editor %}
**ビルド**セクションの下部にある**「言語の管理」**を選択します。

![アプリ内ドラッグ＆ドロップメッセージの多言語設定。]({% image_buster /assets/img/multi-language_support/iam_dnd_manage_languages.png %}){: style="max-width:45%;"}

{% endsubtab %}
{% subtab Traditional editor %}

メッセージを編集する際に**「言語の管理」**を選択します。

![アプリ内 HTML メッセージの多言語設定。]({% image_buster /assets/img/multi-language_support/iam_html_manage_languages.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Banner %}
メッセージを編集する際に**「言語の管理」**を選択します。

![バナーの多言語設定。]({% image_buster /assets/img/multi-language_support/banner_manage_languages.png %})

{% endtab %}

{% tab Content Block %}
コンテンツブロックを編集する際に**「言語の管理」**を選択します。

{% alert important %}
関連する翻訳がアップロードされているコンテンツブロックは、個別のキャンペーンやキャンバスメッセージによって上書きすることはできません。
{% endalert %}

![コンテンツブロックの多言語設定。]({% image_buster /assets/img/multi-language_support/content_block_manage_languages.png %})

{% endtab %}
{% endtabs %}

### ステップ 4:CSV テンプレートをダウンロードする {#download-csv}

ロケールを選択した後、**[テンプレートをダウンロード]** を選択すると、選択した翻訳 ID とロケールの対応表を含む CSV テンプレートがダウンロードされます。

![英語、フランス語、スペイン語のロケール用 CSV の例。]({% image_buster /assets/img/multi-language_support/example_translation_csv.png %}){: style="max-width:70%;"}

### ステップ 5:完成した CSV をアップロードする {#upload-csv}

{% alert important %}
CSV ファイルの ID やロケールを変更しても、メッセージは自動的に更新されません。翻訳を更新するには、CSV ファイルを編集し、ファイルを再アップロードしてください。
{% endalert %}

以下は完成した CSV の例のフォーマットです：

```
Variant1,,,,
,Translation tags,en,es,fr
title,We noticed you've left something behind,We noticed you've left something behind,Notamos que has dejado algo atrás,Nous avons remarqué que vous avez oublié quelque chose derrière vous
offer_text,Check out now and receive,Check out now and receive,Paga ahora y recibe,Payez maintenant et recevez
offer_amount,10% Off,10% Off,10% de Descuento,10 % de réduction
cta,CHECK OUT NOW,CHECK OUT NOW,VERIFICAR AHORA,VÉRIFIER MAINTENANT
```

### ステップ 6:ロケールをプレビューする {#preview-locales}

メッセージをプレビューする際は、**[ユーザーとしてプレビュー]** ドロップダウンから**「多言語ユーザー」**オプションを選択します。これにより、異なるロケール定義を切り替えて、メッセージの全翻訳をプレビューできます。

![ロケールプレビュー]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %})

{% alert tip %}
キャンペーンとキャンバスの翻訳の管理および更新を行う方法については、[翻訳 API]({{site.baseurl}}/api/endpoints/translations) を参照してください。
{% endalert %}

## 右から左に読むメッセージ

右から左へ書く言語（アラビア語など）の翻訳ファイルを入力する際は、翻訳を `span` で囲んで正しくフォーマットされるようにしてください：

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

## 翻訳の管理

### 開始済みのキャンペーンやキャンバスの翻訳を編集する

キャンペーンやキャンバスの開始後でも、下書きモードであれば翻訳を修正できます。これは、コンポーザーで直接翻訳を編集する場合でも、CSV アップロードを利用する場合でも、API を利用する場合でも同様です。

開始後のキャンペーンとキャンバスの管理について詳しくは、[開始後のキャンペーンの編集]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/)と[キャンバスの下書きと開始後の編集]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_drafts/)を参照してください。

### キャンバスステップまたはキャンペーンの複製と翻訳

翻訳は、キャンバスステップ、キャンペーン、またはキャンペーンバリエーションと共にコピーされます。これは、ワークスペース間でコピーする場合にも当てはまりますが、コピー先のワークスペースでロケールが定義されている必要があります。キャンバスやキャンペーンに修正を加える際には、必ず翻訳を確認し、適宜更新してください。

### キャンバスでの多言語 API の使用

[キャンバスで多言語 API]({{site.baseurl}}/api/endpoints/translations/) を使用するには、パラメータリストに `workflow_id`、`step_id`、および `message_variation_id` を含める必要があります。

#### 開始後の下書きに追加されたキャンバスステップ

キャンバス開始後に作成されたキャンバスステップで多言語 API を使用する場合、API に渡す `message_variation_id` は空または空白になります。

## よくある質問

#### 自分のいずれかのロケールで翻訳文を変更できますか？
はい。まず CSV で編集を行ってから、ファイルを再度アップロードすることで翻訳文を変更できます。

#### 翻訳タグをネストできますか？
いいえ。

#### 翻訳はスタイル設定のための HTML をサポートしていますか？
はい。ただし、HTML のスタイル設定がコンテンツと一緒に翻訳されていないことを確認してください。

#### HTML メッセージ全体を翻訳タグで囲むことはできますか？
いいえ。翻訳タグはパフォーマンスやサイズの制限を避けるため、できるだけ小さくする必要があります。

#### Braze はどのような検証や追加チェックを行いますか？

| シナリオ                                                                                                                                                 | Braze での検証                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| 現在のメッセージに関連するロケールが翻訳ファイルにない。                                                                               | この翻訳ファイルはアップロードされません。                                                                       |
| 翻訳ファイルに、現在のメールメッセージの Liquid 翻訳タグ内のテキストなどのテキストブロックが欠落している。                                | この翻訳ファイルはアップロードされません。                                                                       |
| 翻訳ファイルに、現在のメールメッセージのテキストブロックと一致しないデフォルトテキストが含まれている。                                          | この翻訳ファイルはアップロードされません。再アップロードを試みる前に、CSV で修正してください。               |
| 翻訳ファイルに、**多言語サポート**設定に存在しないロケールが含まれている。                                                       | これらのロケールは Braze に保存されません。                                                                      |
| 翻訳ファイルに、現在のメッセージ（翻訳がアップロードされた時点の下書きなど）には存在しないテキストブロックが含まれている。 | 現在のメッセージに存在しないテキストブロックは、翻訳ファイルから Braze には保存されません。 |
| ロケールが翻訳ファイルの一部としてすでにメッセージにアップロードされた後に、メッセージからロケールを削除する。                           | ロケールを削除すると、メッセージ内のそのロケールに関連する翻訳がすべて削除されます。                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }