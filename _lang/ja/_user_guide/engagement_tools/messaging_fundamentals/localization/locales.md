---
nav_title: メッセージ内のロケール
article_title: ローカライゼーションの翻訳
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "この記事では、メッセージングでロケールを使用する方法についてステップを説明する。"
---

# ローカライゼーションの翻訳

> ワークスペースにロケールを追加した後、単一のプッシュ通知、メール、バナー、アプリ内メッセージ、またはコンテンツブロック内で、異なる言語のユーザーをすべて対象にできる。

{% multi_lang_include locales.md section="Prerequisites" %}

## ロケールの使用

### ステップ 1: ワークスペースにロケールを設定する {#workspace-setup}

ロケールと翻訳タグを使用する前に、まず[ワークスペースにロケールを]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings)追加しなければならない。

### ステップ 2:メッセージに翻訳用Liquidタグを追加する {#add-translation-tags}

翻訳するテキスト、画像、リンクURLをすべて囲むために、{% raw %}`{% translation your_id_here %}` と `{% endtranslation %}`{% endraw %} の翻訳タグを追加する。

各翻訳には固有の `id`. が必要だ。例えば、簡単な挨拶を翻訳する場合、IDを「greeting」と名付けることができる：

{% raw %}`{% translation greeting %}Hello!{% endtranslation}`{% endraw %}

#### HTMLブロックのローカライゼーション

より複雑な段落には複数の翻訳タグ("offer_text"が含まれる場合がある。 "offer_amount"):

{% raw %}
```
{% translation offer_text %}Sign up now to save{% endtranslation %}
<b>{% translation offer_amount %}50% Off{% endtranslation %}</b>
```
{% endraw %}

{% alert important %}
大きなHTMLブロックを翻訳タグで囲むと、スタイルシートやスタイル設定の問題を引き起こすことがある。可能な限り小さなテキストセクションで改行する。
{% endalert %}

#### リンクのローカライゼーション

アンカータグのリンクのローカライゼーションを行う際は、URL`href`属性全体ではなく、**言語固有の部分だけを**囲むように注意せよ。URL全体を囲むと、リンクのテンプレート機能が正しく動作しない可能性がある。

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

### ステップ 3:メッセージのローカライゼーションを選択する {#choose-locales}

翻訳タグをメッセージに追加したら、そのメッセージの多言語設定に移動し、翻訳対象のロケールを一つ以上選択する。

![多言語設定で、ロケールを選択するドロップダウンフィールドがある。]({% image_buster /assets/img/multi-language_support/manage_language_dropdown.png %}){: style="max-width:80%;"}

{% tabs %}
{% tab Email %}
メッセージを編集する時は、コンテンツメニューから**「多言語」**を選択する。

![メールの多言語設定。]({% image_buster /assets/img/multi-language_support/email_multi_language.png %}){: style="max-width:45%;"}

{% endtab %}

{% tab Push %}
メッセージを編集する際に**「言語管理」**を選択せよ。

![プッシュ通知の多言語設定。]({% image_buster /assets/img/multi-language_support/push_manage_languages.png %})

{% endtab %}

{% tab In-app message %}
{% subtabs %}
{% subtab Drag-and-Drop Editor %}
**ビルド**セクションの下部にある**「言語の管理」**を選択する。

![アプリ内ドラッグ＆ドロップメッセージの多言語設定。]({% image_buster /assets/img/multi-language_support/iam_dnd_manage_languages.png %}){: style="max-width:45%;"}

{% endsubtab %}
{% subtab Traditional editor %}

メッセージを編集する際に**「言語管理」**を選択せよ。

![アプリ内HTMLメッセージの多言語設定。]({% image_buster /assets/img/multi-language_support/iam_html_manage_languages.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Banner %}
メッセージを編集する際に**「言語管理」**を選択せよ。

![バナーの多言語設定。]({% image_buster /assets/img/multi-language_support/banner_manage_languages.png %})

{% endtab %}

{% tab Content Block %}
コンテンツブロックを編集する際に**「言語管理」**を選択する。

{% alert important %}
関連する翻訳がアップロードされているコンテンツブロックは、個別のキャンペーンやキャンバスメッセージによって上書きすることはできない。
{% endalert %}

![コンテンツブロックの多言語設定。]({% image_buster /assets/img/multi-language_support/content_block_manage_languages.png %})

{% endtab %}
{% endtabs %}

### ステップ 4: CSVテンプレートをダウンロードする {#download-csv}

ロケールを選択した後、**[テンプレートをダウンロード]**を選択すると、選択した翻訳IDとロケールの対応表を含むCSVテンプレートがダウンロードされる。

![英語、フランス語、スペイン語のローカライゼーション用CSVの例。]({% image_buster /assets/img/multi-language_support/example_translation_csv.png %}){: style="max-width:70%;"}

### ステップ 5: 完成したCSVをアップロードする {#upload-csv}

{% alert important %}
CSV ファイルの ID や ロケールに変更があっても、メッセージは自動的に更新されません。翻訳を更新するには、CSVファイルを更新し、ファイルを再アップロードする。
{% endalert %}

以下は完成したCSVの例となるフォーマットだ：

```
Variant1,,,,
,Translation tags,en,es,fr
title,We noticed you've left something behind,We noticed you've left something behind,Notamos que has dejado algo atrás,Nous avons remarqué que vous avez oublié quelque chose derrière vous
offer_text,Check out now and receive,Check out now and receive,Paga ahora y recibe,Payez maintenant et recevez
offer_amount,10% Off,10% Off,10% de Descuento,10 % de réduction
cta,CHECK OUT NOW,CHECK OUT NOW,VERIFICAR AHORA,VÉRIFIER MAINTENANT
```

### ステップ 6: プレビューローカライゼーション {#preview-locales}

メッセージをプレビューする時は、[**プレビュー対象ユーザー**]ドロップダウンから**「多言語ユーザー**」オプションを選択する。これにより、異なるロケール定義を切り替えて、メッセージの全翻訳をプレビューできる。

![ローカライゼーションプレビュー]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %})

{% alert tip %}
キャンペーンとキャンバスの翻訳の管理および更新を行う方法については、[翻訳 API]({{site.baseurl}}/api/endpoints/translations) を参照してください。
{% endalert %}

## 右から左に読むメッセージ

右から左へ書く言語（アラビア語など）の翻訳ファイルを埋める時は、翻訳を\`<span>\`で囲むように`span`しろ。そうすれば正しくフォーマットされる：

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

## 翻訳をマネージャーする

### キャンペーンやキャンバスの翻訳を編集する

キャンペーンやキャンバスの開始後でも、下書きモードであれば翻訳を修正できます。これは、コンポーザーで直接翻訳を編集する場合でも、CSVアップロードを利用する場合でも、APIを利用する場合でも同じだ。 

開始後のキャンペーンとキャンバスの管理については、[開始後のキャンペーンの編集]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/)と[キャンバスの下書きと開始後の編集]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_drafts/)を参照してください。

### キャンバスのステップまたはキャンペーンの複製と翻訳

翻訳は、キャンバスステップ、キャンペーン、またはキャンペーンバリエーションと共にコピーされる。これは、ワークスペース間でコピーする場合にも当てはまる。ただし、そのコピー先のワークスペースでローカライゼーションが定義されている場合に限る。キャンバスやキャンペーンに修正を加える際には、必ず翻訳を確認し、適宜更新してください。

### キャンバスでの多言語APIの使用

[キャンバスで多言語API]({{site.baseurl}}/api/endpoints/translations/)を使用するには、パラメータリストに`message_variation_id` ,`step_id``workflow_id` , および  を含める必要がある。

#### 開始後の下書きに追加されたキャンバスステップ

キャンバス起動後に作成されたステップでマルチ言語APIを使用する場合、APIに渡す引`message_variation_id`数は空または空白になる。

## よくある質問

#### 自分のいずれかのロケールで翻訳文を変更できますか?
はい。まず、CSV で編集を行ってから、ファイルを再度アップロードすることで、翻訳文を変更します。

#### 翻訳タグをネストできますか?
いいえ。

#### 翻訳はスタイル設定のためのHTMLをサポートしているか？
はい。ただし、HTML のスタイル設定がコンテンツと一緒に翻訳されていないことを確認してください。

#### HTMLメッセージ全体を翻訳タグで囲むことはできるか？
いや、翻訳タグはできるだけ小さくすべきだ。パフォーマンスやサイズ制限を避けるためだ。

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
