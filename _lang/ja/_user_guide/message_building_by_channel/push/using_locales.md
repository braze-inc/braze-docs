---
nav_title: メッセージのロケール
article_title: メッセージのロケール
page_order: 9
description: "この記事では、プッシュ通知でロケールを使用する方法について説明します。"
---

# メッセージ内のロケール

> ロケールをワークスペースに追加した後、1 回のプッシュ通知内ですべてのユーザーを異なる言語でターゲットにすることができます。

## 前提条件

[多言語サポート]({{site.baseurl}}/multi_language_support/)の編集および管理を行うには、「多言語設定を管理」のユーザー権限が必要です。メッセージにロケールを追加するには、キャンペーンの編集権限が必要だ。

## ロケールの使用

メッセージングでロケールを使用するには、プッシュキャンペーンまたはキャンバスを作成し、次の手順を実行します。

1. 翻訳タグ{% raw %}`{% translation %}` と`{% endtranslation %}`{% endraw %} を追加して、翻訳するすべてのテキストと画像、リンクURLをラップする。<br><br>![プッシュ通知コンポーザーと、タイトルおよびメッセージフィールドに追加された翻訳タグ。]({% image_buster /assets/img/multi-language_support/push_translation_tags.png %})<br><br>
2. メッセージを下書きとして保存します。
3. **言語**を選択し、ドロップダウンを使用してメッセージのロケールを追加します。
4. **Download template**を選択し、CSVテンプレート内の翻訳を入力します。<br><br>![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})<br><br>
5. 完了したCSV テンプレートをアップロードするには、**Upload translations** を選択します。<br><br>!["多言語メッセージ"ウィンドウ。2つのロケールが選択され、テンプレートをダウンロードするか、翻訳をアップロードするボタンが表示されます。]({% image_buster /assets/img/multi-language_support/upload_translation.png %})

翻訳を更新するには、CSVを更新し、ファイルを再アップロードする。つまり、CSVのIDやロケールに変更があっても、メッセージは自動的に更新されない。

{% alert tip %}
キャンペーンとキャンバスの翻訳の管理および更新を行う方法については、[翻訳 API]({{site.baseurl}}/api/endpoints/translations) を参照してください。
{% endalert %}

## ロケールのプレビュー

**Preview message as user** ドロップダウンの**Test** タブで、**Custom user** を選択し、メッセージが期待どおりに翻訳されるかどうかを確認するために、メッセージをプレビューするために異なる言語を入力します。

{% multi_lang_include locales.md section="Frequently Asked Questions" %}
