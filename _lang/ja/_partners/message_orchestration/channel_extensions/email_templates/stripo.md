---
nav_title: Stripo
article_title:Stripo
alias: /partners/stripo
description:「この参考記事では、BrazeとStripoのパートナーシップについて概説しています。Stripoは、インタラクティブな要素を備えた洗練されたメールを簡単に作成できるドラッグアンドドロップ式のメールテンプレートビルダーです。「
page_type: partner
search_tag:Partner

---

# Stripo

> [Stripoは](https://stripo.email/)、インタラクティブな要素を備えたレスポンシブメールの作成とデザインに役立つドラッグアンドドロップのメールテンプレートビルダーです。Stripoユーザーは、HTMLで編集したり、Stripoエディターを使用してさまざまなデバイスで表示または非表示にする要素を決定したりすることもできます。

BrazeとStripoの統合により、カスタマイズしたStripoメールをエクスポートして、Braze内のテンプレートとしてアップロードできます。

## 前提条件

| 必要条件 | 説明 |
| ------------| ----------- |
| Stripo アカウント | このパートナーシップを利用するには、Stripoアカウントが必要です。 |
| Braze REST API キー | **完全なテンプレート権限を持つBraze** REST API キーです。<br><br> これは Braze ダッシュボードの **\[設定] > \[**API キー**]** から作成できます。 |
| クラスターインスタンス | Braze [クラスターインスタンスは]({{site.baseurl}}/api/basics/#endpoints) Braze ダッシュボードおよび REST エンドポイントと連携しています。  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合

### ステップ1:Stripoメールを作成

**Stripoプラットフォーム Stripoメールを作成し、「エクスポート」をクリックします。** 

![Stripo Export]({% image_buster /assets/img_archive/stripo_export.png %})

### ステップ2:テンプレートを Braze にエクスポート

表示されるダイアログで、**エクスポート方法としてBrazeを選択します** 

次に、**アカウント名** (ワークスペース名など)、**API キー**、**クラスターインスタンスを入力します**。

![Stripo Form]({% image_buster /assets/img_archive/stripo_form.png %})

{% alert important %}
これは 1 回限りの設定で、今後のエクスポートではこの API キーが自動的に使用されます。
{% endalert %}

## 使用

アップロードしたStripoテンプレートは、Brazeアカウントの「**テンプレートとメディア」>「メールテンプレート**」セクションにあります。これで、このメールテンプレートを使用して、顧客への魅力的なメールメッセージの送信を開始できます。

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
