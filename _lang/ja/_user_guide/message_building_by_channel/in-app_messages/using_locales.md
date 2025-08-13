---
nav_title: メッセージのロケール
article_title: メッセージのロケール
page_order: 4
alias: /iam_locales/
description: "この記事では、アプリ内メッセージでロケールを使用する方法について説明します。"
---

# メッセージ内のロケール

> ワークスペースにローカライゼーションを追加すると、1つのアプリ内メッセージで異なる言語のユーザーをターゲットにすることができる。

{% multi_lang_include locales.md section="Prerequisites" %}

## ロケールの使用

メッセージングでロケールを使用するには、アプリ内メッセージキャンペーンまたはキャンバスを作成します。ドラッグアンドドロップエディタまたは従来のエディタのいずれかを選択し、エディタに基づいて手順を実行します。

{% tabs %}
{% tab 従来のエディター %}

1. 翻訳タグ{% raw %}`{% translation %}` と`{% endtranslation %}`{% endraw %} を追加して、翻訳するすべてのテキストと画像、リンクURLをラップする。 
2. 各翻訳タグに ID タグを追加します。例を挙げよう： {% raw %}`{% translation id_1 %}`{% endraw %}

![翻訳 ID が表示されている従来のエディター。]({% image_buster /assets/img/multi-language_support/html_iam_editor_translation_tags.png %}){: style="max-width:60%;"}

{: start="3"}
3\.タグを追加したら、メッセージを下書きとして保存する。
4\.**言語の管理**を選択し、ドロップダウンを使用してメッセージのロケールを追加します。

![1つのロケールが選択されている [言語を管理] モーダル。]({% image_buster /assets/img/multi-language_support/manage_languages_modal.png %})

{: start="5"}
5\.[**テンプレートをダウンロード**] を選択して、翻訳テンプレートを CSV ファイルとしてダウンロードします。次に、CSVファイルに翻訳を記入する。

![翻訳 CSV ファイルの例。]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %}) 

{: start="6"}
6. **Upload translationsを**選択し、翻訳が完了したCSVファイルをアップロードする。

{% endtab %}
{% tab ドラッグ＆ドロップ・エディター %}

1. 翻訳タグ{% raw %}`{% translation %}` と`{% endtranslation %}`{% endraw %} を追加して、翻訳するすべてのテキストと画像、リンクURLをラップする。 
2. 各翻訳タグに ID タグを追加します。例を挙げよう： {% raw %}`{% translation id_1 %}`{% endraw %} 

![2つの翻訳 ID が表示されているドラッグ＆ドロップエディター。]({% image_buster /assets/img/multi-language_support/dnd_iam_editor_translation_tags.png %}){: style="max-width:70%;"}

{: start="3"}
3\.タグを追加したら、メッセージを下書きとして保存してから、エディタを再度開きます。
4\.[**作成**] パネルで [**多言語サポート**] を選択し、そのドロップダウンを使用してメッセージのロケールを追加します。
5\.[**テンプレートをダウンロード**] を選択して、翻訳テンプレートを CSV ファイルとしてダウンロードします。 

![テンプレートをダウンロードするボタンがある [多言語] パネル。]({% image_buster /assets/img/multi-language_support/dnd_iam_download_template.png %}){: style="max-width:40%;"}

{: start="6"}
6. CSVファイルに翻訳を記入する。ステップ1から翻訳タグを直接コピー＆ペーストした場合は、CSVファイルの**翻訳タグ**欄から`<code>` 。
7. **Upload translationsを**選択し、翻訳が完了したCSVファイルをアップロードする。

![テンプレートをダウンロードするボタンと翻訳をアップロードするボタンがある [多言語] パネル。]({% image_buster /assets/img/multi-language_support/dnd_iam_upload_translations.png %}){: style="max-width:40%;"}

{% endtab %}
{% endtabs %}

CSV ファイルの ID や ロケールに変更があっても、メッセージは自動的に更新されません。翻訳を更新するには、CSVファイルを更新し、ファイルを再アップロードする。

{% alert tip %}
キャンペーンとキャンバスの翻訳の管理および更新を行う方法については、[翻訳 API]({{site.baseurl}}/api/endpoints/translations) を参照してください。
{% endalert %}

{% multi_lang_include locales.md section="Preview" %}

{% multi_lang_include locales.md section="Frequently Asked Questions" %}
