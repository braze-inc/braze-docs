---
nav_title: ランディングページ
article_title: ランディングページ
page_order: 31
guide_top_header: "ランディングページ"
description: "この記事には、Brazeランディングページの構築とカスタマイズに関するリソースが含まれている。"
alias: /landing_pages/
---

# ランディングページについて

> Braze のランディングページは、ユーザー獲得とエンゲージメント戦略を推進できる独立した Web ページです。

ランディングページを使用して、オーディエンスの拡大、ユーザーデータの収集、特別なオファーのプロモート、マルチチャネルキャンペーンの促進を行います。

{% alert note %}
ランディングページとカスタムドメインの利用可否は、Brazeの契約プランによって異なる。アカウントマネージャーか顧客サクセスマネージャーに連絡して始めよう。
{% endalert %}

{% multi_lang_include video.html id="eg4r7agod1" source="wistia" %}

## 前提条件

ランディングページにアクセス、作成、公開するには、管理者権限または次のすべての[権限]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions)が必要です。

- ランディングページを表示
- ランディングページの下書きを編集
- ランディングページを公開

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='dnd editors' %}

## プランの階層

利用できる公開ランディングページとカスタムドメインの数は、無料または有料（インクリメンタル）のプランタイプによって異なる。

| 機能                                                                                                   | 無料階層     | 有料ティア (増分)     |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| ランディングページの公開                                                                 | 1社につき5つ | 20追加 |
| カスタムドメイン          | 1社につき1つ | 5追加 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## ランディングページにGoogle Tag Managerを追加する

ランディングページにGoogle Tag Managerを追加するには、ドラッグ＆ドロップエディターでランディングページに**カスタムコード**ブロックを追加し、そのブロックにGoogle Tag Managerのコードを挿入する。タグマネージャーのコードの前に、必ずデータレイヤーを追加すること。例えば、この例のように：

```
<script>
window.dataLayer = window.dataLayer || [];
</script>
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-XXXXXX');</script>
<!-- End Google Tag Manager -->
```

Google Tag Manager の実装に関する詳細は、[Google のドキュメントを](https://developers.google.com/tag-platform/tag-manager/datalayer#installation)参照せよ。

## よくある質問

### ランディングページの最大サイズは何ですか?

ランディングページの本体サイズは最大500KBまでである。

### ランディングページを公開するための技術的な要件はありますか？

いいえ、技術的な要件はありません。

### ランディングページ用の HTML エディターはありますか？

はい。HTML を追加または編集するには、ドラッグ＆ドロップ・エディターで**カスタムコード**ブロックを使用します。

### ランディングページ内に Webhook を作成できるますか?

いいえ、これは現在サポートされていません。
