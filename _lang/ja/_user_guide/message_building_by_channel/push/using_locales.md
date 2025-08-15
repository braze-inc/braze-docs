---
nav_title: メッセージのロケール
article_title: メッセージのロケール
page_order: 9
description: "この記事では、プッシュ通知でロケールを使用する方法について説明します。"
---

# メッセージ内のロケール

> ワークスペースにロケールを追加すると、1通のプッシュ通知の中で、異なる言語のユーザーをすべてターゲットにすることができます。

{% multi_lang_include locales.md section="Prerequisites" %}

{% alert important %}
メッセージの多言語サポートは、現在早期アクセス段階です。早期アクセスに参加することに興味がある場合は、Brazeのアカウントマネージャーに連絡してください。
{% endalert %}

## ロケールの使用

メッセージングでロケールを使用するには、プッシュキャンペーンまたはキャンバスを作成し、次の手順を実行します。

1. 翻訳タグ{% raw %}`{% translation %}` と`{% endtranslation %}`{% endraw %} を追加して、翻訳するすべてのテキストと画像、リンクURLをラップする。

![プッシュ通知作成画面のタイトルフィールドとメッセージフィールドに翻訳タグが追加されている。]({% image_buster /assets/img/multi-language_support/push_translation_tags.png %})

{: start="2"}
2\.メッセージを下書きとして保存します。
3\.**言語**を選択し、ドロップダウンを使用してメッセージのロケールを追加します。
4\.[**テンプレートをダウンロード**] を選択し、CSV テンプレート内に翻訳を入力します。

![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})

{: start="5"}
5\.完成した CSV テンプレートをアップロードするには、[**翻訳をアップロード**] を選択します。 

![[多言語メッセージ] ウィンドウで2つのロケールが選択され、テンプレートをダウンロードするボタンと、翻訳をアップロードするボタンが表示されている。]({% image_buster /assets/img/multi-language_support/upload_translation.png %})

CSV ファイルの ID や ロケールに変更があっても、メッセージは自動的に更新されません。翻訳を更新するには、CSVファイルを更新し、ファイルを再アップロードする。

{% alert tip %}
キャンペーンとキャンバスの翻訳の管理および更新を行う方法については、[翻訳 API]({{site.baseurl}}/api/endpoints/translations) を参照してください。
{% endalert %}

{% multi_lang_include locales.md section="Preview" %}

{% multi_lang_include locales.md section="Frequently Asked Questions" %}
