---
nav_title: セグメント
article_title: セグメント
page_order: 1
layout: dev_guide
guide_top_header: "セグメント"
guide_top_text: "オーディエンスセグメンテーションは戦略的マーケティングの鍵です。オーディエンスセグメンテーションは、ターゲットの絞りすぎや、過剰なメッセージング、顧客との潜在的なつながりの喪失を防ぐことができます。次の記事を参照し、自他双方の最大の利益になるようにフィルターでオーディエンスをセグメント化する方法を学びましょう。"
descriptions: "オーディエンスセグメンテーションは戦略的マーケティングの鍵です。オーディエンスセグメンテーションは、ターゲットの絞りすぎや、過剰なメッセージング、顧客との潜在的なつながりの喪失を防ぐことができます。このランディングページを参照し、自他双方の最大の利益になるようにフィルターでオーディエンスをセグメント化する方法を学びましょう。"
search_rank: 4
tool: Segments
page_type: landing
description: "このランディングページは、ダッシュボードキャンペーン内のセグメンテーションに関する記事を対象としています。ここでは、セグメント、フィルター、ファネル、インサイト、エクステンション などの設定方法について説明します。"

guide_featured_title: "よく読まれている記事"
guide_featured_list:
  - name: セグメントの作成
    link: /docs/user_guide/engagement_tools/segments/creating_a_segment/
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: セグメントの管理
    link: /docs/user_guide/engagement_tools/segments/managing_segments/
    image: /assets/img/braze_icons/edit-05.svg
  - name: セグメンテーションフィルター
    link: /docs/user_guide/engagement_tools/segments/segmentation_filters/
    image: /assets/img/braze_icons/flag-02.svg
  - name: セグメントファンネル
    link: /docs/user_guide/engagement_tools/segments/segment_funnels/
    image: /assets/img/braze_icons/users-right.svg

guide_menu_title: "More articles"
guide_menu_list:
  - name: セグメントインサイト
    link: /docs/user_guide/engagement_tools/segments/segment_insights/
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: セグメント拡張
    link: /docs/user_guide/engagement_tools/segments/segment_extension/
    image: /assets/img/braze_icons/users-01.svg
  - name: SQL セグメント
    link: /docs/sql_segments/
    image: /assets/img/braze_icons/users-01.svg
  - name: カタログセグメント
    link: /docs/catalog_segments/
    image: /assets/img/braze_icons/users-01.svg
  - name: ユーザープロファイル
    link: /docs/user_guide/engagement_tools/segments/using_user_search/
    image: /assets/img/braze_icons/users-01.svg
  - name: ロケーションターゲティング
    link: /docs/user_guide/engagement_tools/segments/location_targeting/
    image: /assets/img/braze_icons/marker-pin-06.svg
  - name: ビーコンとジオフェンスのサポート
    link: /docs/user_guide/engagement_tools/segments/beacon_support/
    image: /assets/img/braze_icons/marker-pin-01.svg
  - name: 正規表現
    link: /docs/user_guide/engagement_tools/segments/regex/
    image: /assets/img/braze_icons/search-sm.svg
  - name: トラブルシューティング
    link: /docs/user_guide/engagement_tools/segments/troubleshooting/
    image: /assets/img/braze_icons/annotation-question.svg

guide_menu_title2: "Other"
guide_menu_list2:
  - name: カスタム属性
    link: /docs/user_guide/data_and_analytics/custom_data/custom_attributes/
    image: /assets/img/braze_icons/table.svg

---

## Braze Segmentについて

Braze では、Segment s はダイナミックなのユーザー s の集まりで、ユーザー 属性 s、ユーザー ビヘイビア、カスタムイベント s など、定義した条件に適合します。他のSegment s 内にSegment s をネストし、追加機能をアプリして、オーディエンスの範囲を狭め、高度なパーソナライズされたと魅力的な内容を適切なユーザーs に送信できるようにすることで、条件を細かく設定できます。

ユーザー s を対象とするSegment s を好きなだけ作成できます。Segment機能とセグメンテーション フィルターのさまざまな組合せを探索して、ユーザーデータを活用する創造的な方法を発見し、関連するメッセージをユーザーやエンゲージメント向上に送信するための新しい方法を解き放ちます。

Braze Segment s がどのようにユーザー s を目標にするのに役立つかについての小さなプレビューについては、以下のユースケース s をご覧ください。

### ユースケース

- **ようこそメッセージ:**新しいユーザーs を分割して、アプリに紹介するオンボーディング メールs またはアプリ内メッセージs を送信できます。
- **ロイヤリティ報酬:**セグメントユーザーは、その購買頻度、会員記念日、または他のマイルストーンに基づいて、あなたの最も忠実なユーザーに排他的なオファーまたは報酬を送る。
- **動作トリガーs:**ユーザーは、sまたはsをトリガー アプリ内メッセージするために、チェックアウト時にカートを放棄するなど、sのユーザー アクションに基づいて分割します。
- **項目の推奨事項:**セグメントユーザーは、特定の製品を購入し、それらを補完的な製品または上位の製品の推奨事項として送信します。
- **A/B テスト:**A/B のセグメントユーザーでは、さまざまなメッセージ、件名、またはコンテンツをテストして、特定の年代、性別、および他の属性s のユーザーに最も影響するものを判断します。

#### セグメント拡張ユースケースs

[Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)を使用して、ユーザープロファイルの存続期間中に保存されたカスタムイベントまたは購買行動に基づいてユーザーs を対象にすることで、Segments をさらに絞り込むことができます。

- **過去の購入実績:**特定の商品の特定のカラーを、過去2年間に少なくとも2回購入したかどうかによってユーザーする。
- **イベントメッセージインターアクションs:**過去30日間に購買を行ったかどうか、また、特定のアプリ内メッセージと相互作用したかどうかによって、sをユーザーする。
- **クエリデータ:** 
  - **照会Snowflake:**[SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)を使用してSnowflakeを照会することにより、BrazeおよびCRMやデータウェアハウスなどの外部ソースから結合されたデータを含むセグメントユーザーs。
  - **データウェアハウスからのシンク:**[CDI Segment s]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/) を使用して、データウェアハウスまたはファイルストレージシステムからBrazeに直接同期されたデータでs をSegment ユーザーします。

