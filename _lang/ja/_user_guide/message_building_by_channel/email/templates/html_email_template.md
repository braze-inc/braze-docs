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

> Braze ダッシュボードでは、独自の HTML メールテンプレートをアップロードし、後でキャンペーンに使用するために保存することができます。また、エディターを使って[Eメールテンプレートを作成する]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/)こともできる。

## 前提条件 {#upload-requirements}

まず、HTMLメールのテンプレートを作成する必要がある。これは、以下を含むZIPファイルでなければならない：

* 1つのHTMLファイル-メールの本文
* HTMLファイルで参照される画像のフォルダ
* 画像ファイル数 50 未満
* 5 MB 未満であること

## テンプレートをアップロードする

### ステップ 1: Eメールテンプレートエディターに移動する

[**テンプレート**] > [**メールテンプレート**] に移動します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、このページは**Engagement**> **Templates & Media**> **Email Templates** にあります。
{% endalert %}

### ステップ 2: アップローダーを開く

**Template Type**セクションで**HTML Editorを**選択し、**Start from a Basic HTML Template**セクションまでスクロールダウンする。[**元のファイル**] を選択します。

### ステップ 3: テンプレートをアップロードする

[**ファイルからアップロード**] をクリックし、コンピューターからテンプレートを選択します。[前提条件](#upload-requirements)のセクションを参照し、テンプレートがアップロード要件を満たしていることを確認します。

#### テンプレートのアップロードエラーのトラブルシューティング

HTMLテンプレートファイルをアップロードする際に、いくつかのエラーメッセージが表示されることがある。エラーが発生した場合、一般的な問題と推奨される修正方法については、以下の表を参照のこと：

| エラー | 修正する |
|------|---|
|.zip 5MB以上| ファイルサイズを小さくして、もう一度アップロードしてみよう。|
|.zip破損| ファイルを検査し、再度アップロードを試みる。 |
|HTMLの欠落| HTMLファイルをZIPファイルに追加し、再度アップロードを試みる。|
|複数のHTML| HTMLファイルの1つを削除し、再度アップロードを試みる。|
|5MB以上の画像| 画像の数を減らして、再度アップロードを試みる。 |
|おまけの画像| HTMLファイルで参照されていない画像がファイル内にあるかもしれない。これはフェイルエラーにはなりませんが、余分な画像は破棄されます。もしこれらの画像がHTMLファイルで参照されることになっているのであれば、コンテンツをチェックし、エラーがあれば修正して、再度アップロードを試みる。|
|画像がありません| HTMLファイル内で参照されている画像があるにもかかわらず、それらの画像がZIPファイルのimageフォルダに含まれていない場合、ファイルエラーが発生する。ファイルを確認し、エラー（スペルミスなど）を修正するか、足りない画像をZIPファイルに追加し、再度アップロードを試みる。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### ステップ 4: テンプレートを完成させて保存する

**Save Template（テンプレートの保存）**」をクリックして、必ずテンプレートを保存すること。これで、このテンプレートを任意のキャンペーンやキャンバスで使用する準備が整った！

{% alert note %}
既存のテンプレートに編集を加えた場合、その変更はそのテンプレートの旧バージョンを使用して作成されたキャンペーンには反映されない。
{% endalert %}

## APIキャンペーンでテンプレートを使用する {#api_for_upload_email_templates}

API キャンペーンでメールを使用するには、`email_template_id` が必要です。これは、Braze で作成されたメールテンプレートの下部にあります。

![HTMLメールテンプレートのAPI Identifierセクション。][4]

## メールテンプレートを管理する

メールテンプレートの[複製や]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) [アーカイブが]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/archive/)できる！テンプレートとクリエイティブ・コンテンツの作成と管理については、[テンプレートで]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/)詳しく説明されている。

## よくある質問

Eメールテンプレートに関するよくある質問については、[Eメール・リンクテンプレート FAQ][10] ]ページをご覧いただきたい。


[4]: {% image_buster /assets/img_archive/email_template_id.png %}
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/