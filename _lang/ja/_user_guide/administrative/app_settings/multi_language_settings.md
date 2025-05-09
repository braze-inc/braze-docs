---
nav_title: 多言語設定
article_title: 多言語設定
alias: "/multi_language_support/"
page_order: 5.5
description: "この記事では、Braze ダッシュボードの多言語設定の概要と、メッセージングでロケールを使用する方法について説明します。"
---

# 多言語設定

> 多言語設定を調整することで、1 通のメールメッセージの中で異なるメッセージを使用して、異なる言語や地域のユーザーをターゲットにすることができます。

## 前提条件

多言語サポートの編集および管理を行うには、「多言語設定を管理」のユーザー権限が必要です。メッセージにロケールを追加するには、キャンペーンの編集権限が必要だ。

## ロケールを追加する

1. [**設定**] > [**多言語設定**] ([**ワークスペース設定**] の下) に移動します。
2. [**ロケールを追加**] を選択し、[**デフォルトのロケール**] または [**カスタム属性**] を選択します。<br><br>![デフォルトのロケールまたはカスタム属性を選択するオプションがある [ロケールを追加] ドロップダウン。][1]{: style="max-width:40%;"}
3. ロケールの名前を入力する。
4. 選択したロケールオプションに対応するユーザー属性を選択します。

{% tabs %}
{% tab デフォルトのロケール %}

**デフォルトロケール**の場合、ドロップダウンを使用して、追加する言語、およびオプションで言語に関連付ける国を選択します。<br><br>![言語と国を指定するための「ロケールの追加 - デフォルトの言語と国」というウィンドウ。]({% image_buster /assets/img/multi-language_support/default_option.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab カスタム属性 %}

**Custom Attributes** の場合、ドロップダウンを使用して関連付けられたカスタム属性を選択し、テキストフィールドに値を入力します。<br><br>![カスタム属性と値を指定するための「ロケールの追加-カスタム属性」というウィンドウ。]({% image_buster /assets/img/multi-language_support/custom_attributes_option.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

{: start="5"}
5\.[**ロケールを追加**] を選択します。 

メールのキャンペーンおよびキャンバスでこれらのロケールを使用する手順については、[ロケールの使用]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/)を参照してください。

## 考慮事項

- ロケールを設定するときは、デフォルトのユーザー属性またはカスタム属性から言語を選択できます。両方から選択することはできません。
- 1つのロケールで最大2つのカスタム属性を選択できます。また、最大2つのデフォルトユーザー属性言語を選択できます。どちらの場合も、2番目の属性はオプションです。
- CSV ファイルで変換された値を編集する場合は、ファイルのデフォルト値を変更しないでください。
- アップロードしたファイルのロケールキーは、マルチ言語設定のロケールキーと一致する必要があります。

### 支援と優先順位付け

- カスタム属性ロケールに一致するユーザーは、デフォルトのユーザー属性に一致するユーザーよりも前に優先されます。
- カスタム属性のサポートは、文字列型と`equals` 比較キーに制限されます。
- カスタム属性が削除された場合、またはそのタイプが変更された場合、ユーザはそのロケールに属することができなくなり、該当するロケールの優先リストがダウンするか、デフォルトのマーケティング翻訳が受信されます。
- ロケールが無効な場合(カスタム属性が変更または削除された場合)、**Multi-Language Support** ページにエラーが表示されます。

## よくある質問

#### 追加できるロケールはいくつですか?

最大 200 か所のロケールを追加できます。

#### Brazeの翻訳ファイルはどこに保存されているのか？

翻訳ファイルはキャンペーンレベルで保存されるため、各メッセージのバリアントは翻訳をアップロードする必要がある。

#### ロケール名は特定のパターンやフォーマットに従わなければならないのか？

いいえ、お好きな命名規則を使うことができる。ロケール名はエディターでロケールを選択するときに使用され、翻訳 ID とともにダウンロードしたファイルの見出しに記載されます。

[1]: {% image_buster /assets/img/multi-language_support/add_locale_options.png %}