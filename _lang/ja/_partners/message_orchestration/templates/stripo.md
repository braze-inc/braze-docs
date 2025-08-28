---
nav_title: Stripo
article_title: Stripo
alias: /partners/stripo
description: "この参考記事では、BrazeとStripoの提携について概説している。Stripoは、ドラッグ＆ドロップでメールテンプレートを作成でき、インタラクティブな要素を含む洗練されたメールを簡単に作成できる。"
page_type: partner
search_tag: Partner

---

# Stripo

> [Stripoは](https://stripo.email/)ドラッグ＆ドロップで使えるメールテンプレートビルダーで、インタラクティブな要素を盛り込んだレスポンシブメールの作成・デザインを支援する。StripoユーザーはHTMLで編集することもでき、Stripoエディターを通じて、様々なデバイスで表示・非表示する要素を決めることができる。

_この統合は Stripo によって管理されます。_

## 統合について

BrazeとStripoの統合により、カスタマイズしたStripoメールをエクスポートし、Braze内でテンプレートとしてアップロードできる。

## 前提条件

| 必要条件 | 説明 |
| ------------| ----------- |
| Stripo アカウント | このパートナーシップを利用するには、Stripoアカウントが必要である。 |
| Braze REST API キー | 完全な**テンプレート**権限を持つBraze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| クラスタインスタンス | Braze [クラスターインスタンス]({{site.baseurl}}/api/basics/#endpoints)は、Braze ダッシュボードと REST エンドポイントに対応しています。  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 統合

### ステップ1:StripoのEメールを作成する

Stripo プラットフォームで Stripo メールを作成し、[**Export**] をクリックします。 

![Stripo エクスポート]({% image_buster /assets/img_archive/stripo_export.png %})

### ステップ2:テンプレートをBrazeにエクスポートする

表示されるダイアログで、エクスポート方法として [**Braze**] を選択します。 

次に、**アカウント名** (ワークスペース名など)、**API キー**、**クラスタインスタンス**を入力します。

![Stripo Form]({% image_buster /assets/img_archive/stripo_form.png %})

{% alert important %}
これは1回限りのセットアップであり、今後のエクスポートは自動的にこのAPIキーを利用することになる。
{% endalert %}

## 使用

アップロードしたStripoテンプレートをBrazeアカウントの**Templates & Media > Email Templates**セクションから探す。これで、このメールテンプレートを使用して、顧客に魅力的なメールメッセージを送信できます。


