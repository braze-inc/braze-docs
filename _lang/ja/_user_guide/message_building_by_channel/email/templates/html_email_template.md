---
nav_title: HTMLメールテンプレートをアップロードする
article_title: HTMLメールテンプレートをアップロードする
page_order: 2
description: "このリファレンス記事では、Brazeダッシュボードを使用したHTMLメールテンプレートの作成、管理、トラブルシューティングの方法について説明する。"
tool:
  - Templates
channel:
  - email

---

# HTMLメールテンプレートをアップロードする

> Brazeのダッシュボードでは、独自のHTMLメールテンプレートをアップロードし、後でキャンペーンに使用するために保存することができる。また、エディターを使って[Eメールテンプレートを作成する]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/)こともできる。

## 前提条件 {#upload-requirements}

まず、HTMLメールのテンプレートを作成する必要がある。これは、以下を含むZIPファイルでなければならない：

* 1つのHTMLファイル-メールの本文
* HTMLファイルで参照される画像のフォルダ
* 画像ファイル数50以下
* 5MB以下であること

## テンプレートをアップロードする

### ステップ 1:Eメールテンプレートエディターに移動する

**Templates**>**Email Templatesに**移動する。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合、このページは**エンゲージメント**>**テンプレートとメディア**>**Eメールテンプレートに**ある。
{% endalert %}

### ステップ 2:アップローダーを開く

**Template Type**セクションで**HTML Editorを**選択し、**Start from a Basic HTML Template**セクションまでスクロールダウンする。**ファイルから**」を選択する。

### ステップ 3:テンプレートをアップロードする

**ファイルからアップロードを**クリックし、コンピューターからテンプレートを選択する。[前提条件の](#upload-requirements)セクションを参照し、テンプレートがアップロード要件を満たしていることを確認する。

#### テンプレートのアップロードエラーのトラブルシューティング

HTMLテンプレートファイルをアップロードする際に、いくつかのエラーメッセージが表示されることがある。エラーが発生した場合、一般的な問題と推奨される修正方法については、以下の表を参照のこと：

| エラー | 修正する |
|------|---|
|.zip 5MB以上| ファイルサイズを小さくして、もう一度アップロードしてみよう。|
|.zip破損| ファイルを検査し、再度アップロードを試みる。 |
|HTMLの欠落| HTMLファイルをZIPファイルに追加し、再度アップロードを試みる。|
|複数のHTML| HTMLファイルの1つを削除し、再度アップロードを試みる。|
|5MB以上の画像| 画像の数を減らして、再度アップロードを試みる。 |
|おまけの画像| HTMLファイルで参照されていない画像がファイル内にあるかもしれない。これはフェイルエラーにはならないが、余分な画像は破棄される。もしこれらの画像がHTMLファイルで参照されることになっているのであれば、コンテンツをチェックし、エラーがあれば修正して、再度アップロードを試みる。|
|消えた画像| HTMLファイル内で参照されている画像があるにもかかわらず、それらの画像がZIPファイルのimageフォルダに含まれていない場合、ファイルエラーが発生する。ファイルを確認し、エラー（スペルミスなど）を修正するか、足りない画像をZIPファイルに追加し、再度アップロードを試みる。|
{: .reset-td-br-1 .reset-td-br-2}

### ステップ 4:テンプレートを完成させて保存する

**Save Template（テンプレートの保存）**」をクリックして、必ずテンプレートを保存すること。これで、このテンプレートを任意のキャンペーンやキャンバスで使用する準備が整った！

{% alert note %}
既存のテンプレートに編集を加えた場合、その変更はそのテンプレートの旧バージョンを使用して作成されたキャンペーンには反映されない。
{% endalert %}

## APIキャンペーンでテンプレートを使用する {#api_for_upload_email_templates}

APIキャンペーンにメールを使用するには、`email_template_id` 、Brazeで作成したメールテンプレートの一番下にある。

![HTMLメールテンプレートのAPI Identifierセクション。][4]

## メールテンプレートを管理する

メールテンプレートの[複製や]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) [アーカイブが]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/)できる！テンプレートとクリエイティブ・コンテンツの作成と管理については、[テンプレートで]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/)詳しく説明されている。

## よくある質問

Eメールテンプレートに関するよくある質問については、\[Eメール・リンクテンプレート FAQ][10] ]ページをご覧いただきたい。


[4]: {% image_buster /assets/img_archive/email_template_id.png %}
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/