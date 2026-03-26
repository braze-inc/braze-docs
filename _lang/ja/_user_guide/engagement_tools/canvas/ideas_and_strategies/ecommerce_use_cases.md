---
nav_title: eコマースのユースケース
article_title: eコマースのユースケース
alias: /ecommerce_use_cases/
page_order: 4
description: "このリファレンス記事では、e コマースのマーケター向けにカスタマイズされた、事前構築済みのさまざまな Braze テンプレートについて説明し、必要な戦略を簡単に実施できるようにします。"
toc_headers: h2
---

# e コマース推奨イベントの使い方

> このページでは、プラットフォーム全体でe コマース推奨イベントをどのように、どこで使用できるかを説明する。これにはBraze e コマースキャンバステンプレートの使用方法も含まれる。

{% alert important %}
[e コマースの推奨イベント]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/)は現在、早期アクセス段階です。早期アクセスに参加したい場合は、Braze カスタマーサクセスマネージャーにお問い合わせください。<br><br>新しいShopifyコネクターを使用している場合、eCommerceの推奨イベントは統合によって自動的に利用可能になります。
{% endalert %}

## キャンバステンプレートの使用

キャンバステンプレートを使用するには:
1. [**メッセージング**] > [**キャンバス**] に進みます。
2. [**キャンバスを作成** > [**キャンバステンプレートを使用**] を選択します。
3. 使用するテンプレートの [**Braze テンプレート**] タブを参照します。テンプレートの名前を選択すると、テンプレートをプレビューできます。
4. 使用するテンプレートの [**テンプレートを適用**] を選択します。<br><br>![「Braze キャンバステンプレート」ページが開き、「Brazeテンプレート」タブが表示されている。最近使用したテンプレートのリストと、選択可能なBrazeテンプレートが表示されている。]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## eコマースキャンバスのテンプレート

Brazeは4つのe コマースキャンバステンプレートを提供している。

{% multi_lang_include canvas/ecommerce_templates.md %}

## メッセージのパーソナライズ

[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) は、Braze が使用する強力なテンプレート言語で、お客様のために動的でパーソナライズされたコンテンツを作成できます。Liquidタグを使用することで、顧客データ、製品情報、その他の変数に基づいてメッセージをカスタマイズすることができ、ショッピング体験や運転エンゲージメントを向上させることができます。

### Liquidの主な特徴

- **ダイナミックコンテンツ:**名前、注文の詳細、設定などの顧客固有の情報をメッセージに挿入します。
- **条件付きロジック:**if/else 文を使用して、特定の条件(顧客の場所や購入履歴など) に基づいて異なるコンテンツを表示します。
- **ループ:**製品または顧客データのコレクションを反復処理して、アイテムのリストまたはグリッドを表示します。

### Liquid を使い始める

Liquid タグを使用してメッセージのパーソナライズを開始するには、次のリソースを参照します。

- 事前定義の Liquid タグを使用した [Shopify データ]({{site.baseurl}}/shopify_features/#shopify-data)参照
- [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)

## セグメンテーション

Braze セグメントを使用して、特定の属性と動作に基づいてターゲットを絞った顧客セグメントを作成し、カスタマイズされたメッセージングとキャンペーンを提供します。この強力な機能により、適切なタイミングで適切なメッセージを使って適切なオーディエンスにリーチし、顧客に効果的にエンゲージできます。

セグメントの使用開始の詳細については、「[Braze のセグメントについて]({{site.baseurl}}/user_guide/engagement_tools/segments#about-braze-segments)」を参照してください。

### 推奨イベント

e コマースイベントは、[推奨イベント]({{site.baseurl}}/recommended_events/)に基づいています。
推奨されるイベントはオピニオン化されたカスタムイベントであるため、[カスタムイベントフィルタ]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#segmentation-filters)を選択することで、推奨されるeCommerceイベント名を検索できます。

### eコマースのフィルター

**Ecommerce Source** および**Total Revenue** などのeCommerce フィルタを使用して、セグメンテータ内の**Ecommerce** セクションに移動して、ユーザをeCommerce フィルタでセグメント化します。 

e コマースフィルターのリストとその定義については、[セグメントフィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/)を参照し、「e コマース」検索カテゴリを選択せよ。

![「e コマース」フィルター付きのセグメントフィルタードロップダウン。]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:50%"}

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation for eCommerce filters' %}

## ネストされたイベントプロパティ

階層化イベントプロパティでセグメンテーションを行うには、[セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#why-use-segment-extensions)を利用できます。たとえば、Segment Extensions を使用して、製品「SKU-123」を過去90 日間に購入したユーザーを検索できます。

## 分析

### カスタムイベントレポート

[カスタム]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/#analytics)イベント[レポート]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/#analytics)で、e コマース推奨イベントの発生件数を追跡できる。**カスタムイベント**でフィルターをかけ、[e コマース推奨イベント]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/#types-of-ecommerce-recommended-events)名を指定すると、そのイベントの経時的なパフォーマンスを確認できる。

![カスタムイベントのチャートで、選択した6つのイベントの結果を表示している。]({% image_buster /assets/img/ecommerce/custom_events_chart.png %})

### ダッシュボード

#### コンバージョンダッシュボード

「注文を確定」コンバージョンイベントを使用してキャンペーンやキャンバスを起動した後、対応する[コンバージョンレポート]({{site.baseurl}}/user_guide/analytics/dashboard/conversions_dashboard/#setting-up-your-report)を作成してパフォーマンスをトラッキングできる。

![コンバージョン詳細テーブルには、キャンペーンとキャンバス、および関連するコンバージョン統計が含まれる。]({% image_buster /assets/img_archive/conversion_details_table.png %})

#### e コマース収益ダッシュボード

注文前にユーザーが最後に接触したキャンペーンまたはキャンバスに起因する収益のインサイトを把握するには、[e コマース収益ダ]({{site.baseurl}}/ecommerce_revenue_dashboard/)ッシュ[ボード]({{site.baseurl}}/ecommerce_revenue_dashboard/)を使用し、コンバージョン期間を選択する。

### 収益レポート 

これらの新しいイベントのデータを分析するには、[ダッシュボード]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/)ビルダーに移動し、「[**e コマース収益 - ラストタッチアトリビューション**」ダッシュボード]({{site.baseurl}}/ecommerce_revenue_dashboard/)を表示する。
