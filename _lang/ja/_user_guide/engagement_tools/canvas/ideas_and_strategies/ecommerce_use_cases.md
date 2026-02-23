---
nav_title: eコマースのユースケース
article_title: eコマースのユースケース
alias: /ecommerce_use_cases/
page_order: 4
description: "このリファレンス記事では、e コマースのマーケター向けにカスタマイズされた、事前構築済みのさまざまな Braze テンプレートについて説明し、必要な戦略を簡単に実施できるようにします。"
toc_headers: h2
---

# eコマースおすすめイベントの使い方

> このページでは、Braze eコマースキャンバステンプレートの使用方法など、プラットフォーム全体でeコマースの推奨イベントをどのように、どこで使用できるかについて説明します。

{% alert important %}
[e コマースの推奨イベント]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/)は現在、早期アクセス段階です。早期アクセスに参加したい場合は、Braze カスタマーサクセスマネージャーにお問い合わせください。<br><br>新しいShopifyコネクターを使用している場合、eCommerceの推奨イベントは統合によって自動的に利用可能になります。
{% endalert %}

## キャンバステンプレートの使用

キャンバステンプレートを使用するには:
1. [**メッセージング**] > [**キャンバス**] に進みます。
2. [**キャンバスを作成** > [**キャンバステンプレートを使用**] を選択します。
3. 使用するテンプレートの [**Braze テンプレート**] タブを参照します。テンプレートの名前を選択すると、テンプレートをプレビューできます。
4. 使用するテンプレートの [**テンプレートを適用**] を選択します。<br><br>!["Canvas テンプレート s" page 開封 to the " Braze テンプレート &s" tab と表示され、最近使用したテンプレートと選択可能なBraze テンプレートを表示します。]({% image_buster /assets/img_archive/apply_template.png %}){: style="max-width:80%;"}

## eコマースキャンバスのテンプレート

Brazeは4つのeコマースキャンバステンプレートを提供している。

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

eコマースフィルターとその定義の一覧については、[セグメントフィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/)を参照し、"eCommerce"検索カテゴリを選択してください。

![セグメントフィルターは"Ecommerce"フィルター sでドロップダウンします。]({% image_buster /assets/img_archive/ecommerce_filters.png %}){: style="max-width:50%"}

{% multi_lang_include alerts/important_alerts.md alert='Purchase event deprecation for eCommerce filters' %}

## ネストされたイベントプロパティ

階層化イベントプロパティでセグメンテーションを行うには、[セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#why-use-segment-extensions)を利用できます。たとえば、Segment Extensions を使用して、製品「SKU-123」を過去90 日間に購入したユーザーを検索できます。

## 分析

### カスタムイベントレポート

eコマースの推奨イベントボリュームは、[カスタムイベントレポート]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_events/#analytics)で追跡できます。**カスタムイベントを実行** でフィルタリングし、[eCommerce 推奨イベント名]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/#types-of-ecommerce-recommended-events) を指定して、そのパフォーマンスを経時的に表示します。

![選択した6 つのイベントの結果を表示するカスタムイベントチャート。]({% image_buster /assets/img/ecommerce/custom_events_chart.png %})

### 換算レポート 

### カスタムイベントレポート

統合でサポートされているイベントを誰が実行したかに基づいて[カスタムイベントレポート]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#analytics) を作成するには、特定の[イベント名]({{site.baseurl}}/shopify_data_features/) を指定します。

### ダッシュボード

#### コンバージョンダッシュボード

起動したキャンバスからの注文に関連するトレンドをインサイトするには、[コンバージョンダッシュボード]({{site.baseurl}}/user_guide/data_and_analytics/analytics/conversions_dashboard#conversions-dashboard)を設定し、キャンバスを指定します。

#### イーコマース収入ダッシュボード

インサイトを収益属性に取り込むには、d ユーザーが最後のキャンペーンまたはキャンバスに移動してから発注するには、[eCommerce revenue ダッシュボード]({{site.baseurl}}/ecommerce_revenue_dashboard/) を使用し、コンバージョンウィンドウを選択します。

### クエリビルダー

### 収益レポート 

これらの新しいイベントのデータを分析するには、[ ダッシュボード Builder]({{site.baseurl}}/user_guide/analytics/reporting/dashboard_builder/) に移動し、[**eCommerce Revenue - Last Touch Attribution** ダッシュボード]({{site.baseurl}}/ecommerce_revenue_dashboard/) を表示します。
