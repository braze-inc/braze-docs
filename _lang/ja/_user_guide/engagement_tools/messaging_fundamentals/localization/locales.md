---
nav_title: メッセージ内のロケール
article_title: ロケールの変換
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "ここでは、ロケールを使用する方法に関するステップについて説明します。"
---

# ロケールの変換

> ロケールをワークスペースに追加した後、単一のプッシュ、メール、バナー、またはアプリ内メッセージ内のすべてのユーザーをさまざまな言語で対象にすることができます。

{% multi_lang_include locales.md section="Prerequisites" %}

## ロケールの使用

### ステップ 1: ワークスペースでロケールを設定する {#workspace-setup}

ロケールと変換タグs を使用するには、まず[ロケールをワークスペース]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings)に追加する必要があります。

### ステップ 2:メールに変換Liquid タグsを追加する {#add-translation-tags}

翻訳タグs {% raw %}`{% translation your_id_here %}` および`{% endtranslation %}`{% endraw %} を追加して、翻訳するすべての文字、"画像、またはリンクURL をラップします。

各変換には一意の`id` が必要です。たとえば、単純なグリーティングを変換する場合、ID "greeting" という名前を付けることができます。

{% raw %}`{% translation greeting %}Hello!{% endtranslation}`{% endraw %}

#### HTML ブロックのローカライズ

より複雑な段落には、複数の変換タグs ("offer_text" が含まれる場合があります "offer_amount"):

{% raw %}
```
{% translation offer_text %}Sign up now to save{% endtranslation %}
<b>{% translation offer_amount %}50% Off{% endtranslation %}</b>
```
{% endraw %}

{% alert important %}
変換タグで大きなHTML ブロックs をアプリすると、スタイルシートまたはスタイルの問題が発生する可能性があります。最小のテキストセクションをできるだけ折り返します。
{% endalert %}

#### リンクのローカライズ

アンカータグリンクをローカライズするには、** は言語固有の部分** のみをラップし、`href` URL 属性全体をローカライズしないようにします。URL 全体をラップすると、リンクテンプレートが正しく機能しない場合があります。

##### 正しい使い方

{% raw %}
```
<a href="https://www.braze.com/{% translation link_href %}en{% endtranslation %}/page"></a>
```
{% endraw %}

##### 誤った使用方法

{% raw %}
```
<a href="{% translation link_href %}https://www.braze.com/en/page{% endtranslation %}"></a>
```
{% endraw %}

### ステップ 3:メッセージロケールの選択 {#choose-locales}

変換タグがメッセージに表示されたら、メッセージの多言語設定に移動し、このメッセージに変換する1つ以上のロケールを選択します。

![ロケールを選択するドロップダウン・フィールドを含む多言語設定。]({% image_buster /assets/img/multi-language_support/manage_language_dropdown.png %}){: style="max-width:80%;"}

{% tabs %}
{% tab Email %}
メッセージを編集するときは、コンテンツメニューから**Multi-Language**を選択します。

![メール用の多言語設定。]({% image_buster /assets/img/multi-language_support/email_multi_language.png %}){: style="max-width:45%;"}

{% endtab %}

{% tab Push %}
メッセージを編集するときは、**言語の管理**を選択します。

![プッシュ用多言語設定。]({% image_buster /assets/img/multi-language_support/push_manage_languages.png %})

{% endtab %}

{% tab In-app message %}
{% subtabs %}
{% subtab Drag-and-Drop Editor %}
**Build**セクションの下部にある**Manage Languages**を選択します。

![アプリ内ドラッグアンドドロップメッセージ用の多言語設定s。]({% image_buster /assets/img/multi-language_support/iam_dnd_manage_languages.png %}){: style="max-width:45%;"}

{% endsubtab %}
{% subtab Traditional editor %}

メッセージを編集するときは、**言語の管理**を選択します。

![アプリ HTML内通信の多言語設定s。]({% image_buster /assets/img/multi-language_support/iam_html_manage_languages.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Banner %}
メッセージを編集するときは、**言語の管理**を選択します。

![バナー用の多言語設定。]({% image_buster /assets/img/multi-language_support/banner_manage_languages.png %})

{% endtab %}
{% endtabs %}

### ステップ 4: 下読み込むCSV テンプレート {#download-csv}

ロケールを選択したら、**Down 読み込む テンプレート**を選択して、選択した変換IDとロケールの行列を含むCSV テンプレートを読み込むします。

![en、fr、およびロケールのCSV の例。]({% image_buster /assets/img/multi-language_support/example_translation_csv.png %}){: style="max-width:70%;"}

### ステップ 5: 完了したCSVを読み込むする {#upload-csv}

{% alert important %}
CSV ファイルの ID や ロケールに変更があっても、メッセージは自動的に更新されません。翻訳を更新するには、CSVファイルを更新し、ファイルを再アップロードする。
{% endalert %}

次に、完成したCSV の形式の例を示します。

```
Variant1,,,,
,Translation tags,en,es,fr
title,We noticed you've left something behind,We noticed you've left something behind,Notamos que has dejado algo atrás,Nous avons remarqué que vous avez oublié quelque chose derrière vous
offer_text,Check out now and receive,Check out now and receive,Paga ahora y recibe,Payez maintenant et recevez
offer_amount,10% Off,10% Off,10% de Descuento,10 % de réduction
cta,CHECK OUT NOW,CHECK OUT NOW,VERIFICAR AHORA,VÉRIFIER MAINTENANT
```

### ステップ 6: ロケールのプレビュー {#preview-locales}

メッセージをプレビューするときは、**Multi-Language User**を**プレビューからUser**ドロップダウンから選択します。これにより、さまざまなロケール定義を切り替えるして、すべての翻訳をプレビューできます。

![ロケールプレビュー]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %})

{% alert tip %}
キャンペーンとキャンバスの翻訳の管理および更新を行う方法については、[翻訳 API]({{site.baseurl}}/api/endpoints/translations) を参照してください。
{% endalert %}

## 右から左に読むメッセージ

右から左に記述された言語の翻訳ファイルを入力する場合(アラビア語のように)、翻訳を`span` でラップし、適切にフォーマットされます。

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

翻訳は、キャンバス ステップ、キャンペーン、またはキャンペーンのバリエーションとともにコピーされます。これは、ロケールがその送信先 ワークスペースで定義されている限り、ワークスペースs 間でコピーする場合にも当てはまります。キャンバスやキャンペーンに修正を加える際には、必ず翻訳を確認し、適宜更新してください。

### Canvases での多言語API の使用

[Multi-Language API をCanvases]({{site.baseurl}}/api/endpoints/translations/) で使用するには、`workflow_id`、`step_id`、および`message_variation_id` をパラメータリストに含める必要があります。

#### 開始後の下書きに追加されたキャンバスステップ

キャンバスの起動後に作成されたキャンバスステップで多言語API を使用する場合、API に渡す`message_variation_id` は空または空白になります。

## よくある質問

#### 自分のいずれかのロケールで翻訳文を変更できますか?
はい。まず、CSV で編集を行ってから、ファイルを再度アップロードすることで、翻訳文を変更します。

#### 翻訳タグをネストできますか?
いいえ。

#### 翻訳はスタイリングのHTMLに対応していますか?
はい。ただし、HTML のスタイル設定がコンテンツと一緒に翻訳されていないことを確認してください。

#### HTMLメール全体を翻訳タグにまとめることはできますか?
いいえ、変換タグは、パフォーマンスやサイズ制限を避けるためにできるだけ小さくする必要があります。

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
