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
  - name: セグメントデータ
    link: /docs/viewing_and_understanding_segment_data/
    image: /assets/img/braze_icons/pie-chart-01.svg

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
  - name: ユーザープロフィール
    link: /docs/user_guide/engagement_tools/segments/user_profiles/
    image: /assets/img/braze_icons/users-01.svg
  - name: ロケーションターゲティング
    link: /docs/user_guide/engagement_tools/segments/location_targeting/
    image: /assets/img/braze_icons/marker-pin-06.svg
  - name: 正規表現
    link: /docs/user_guide/engagement_tools/segments/regex/
    image: /assets/img/braze_icons/search-sm.svg
  - name: 抑制リスト
    link: /docs/user_guide/engagement_tools/segments/suppression_lists/
    image: /assets/img/braze_icons/list.svg 
  - name: 測定セグメントサイズ
    link: /docs/user_guide/engagement_tools/segments/measuring_segment_size/
    image: /assets/img/braze_icons/pie-chart-02.svg
  - name: トラブルシューティング
    link: /docs/user_guide/engagement_tools/segments/troubleshooting/
    image: /assets/img/braze_icons/annotation-question.svg

guide_menu_title2: "Other"
guide_menu_list2:
  - name: カスタム属性
    link: /docs/user_guide/data/custom_data/custom_attributes/
    image: /assets/img/braze_icons/table.svg

---

## Braze のセグメントについて

Braze のセグメントとは、ユーザー 属性、ユーザーの行動、 カスタムイベントなど、定義した特定の条件に合致するダイナミックなユーザーグループです。セグメント内に他のセグメントを階層化し、追加の機能を適用して条件を細かく設定することで、オーディエンスの範囲を絞り込んで、高度にパーソナライズされ魅力的なコンテンツを適切なユーザーに送信できます。

ターゲットにするユーザーを設定するために必要な数だけセグメントを作成できます。Segment機能とセグメンテーション フィルターのさまざまな組合せを探索して、ユーザーデータを活用する創造的な方法を発見し、関連するメッセージをユーザーやエンゲージメント向上に送信するための新しい方法を解き放ちます。

Braze のセグメントがユーザーのターゲット設定にどのように役立つかの概要については、以下のユースケースを参照してください。

### ユースケース

- **ウエルカムメッセージ:**新規ユーザーをセグメント化すると、アプリを紹介するオンボーディングメールまたはアプリ内メッセージを送信できます。
- **ロイヤルティ報酬:**購入頻度、登録記念日、その他のマイルストーンに基づいてユーザーをセグメント化して、最も忠実なユーザーに限定的なオファーまたは報酬を送ります。
- **行動トリガー:**チェックアウト時のカート放棄など、ユーザーのアクションに基づいてユーザーをセグメント化し、アプリ内メッセージまたはプッシュ通知をトリガーします。
- **アイテムのおすすめ:**セグメントユーザーは、特定の製品を購入し、それらを補完的な製品または上位の製品の推奨事項として送信します。
- **AB テスト:**A/B のセグメントユーザーでは、さまざまなメッセージ、件名、またはコンテンツをテストして、特定の年代、性別、および他の属性s のユーザーに最も影響するものを判断します。

#### セグメント拡張ユースケースs

[Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)を使用して、ユーザープロファイルの存続期間中に保存されたカスタムイベントまたは購買行動に基づいてユーザーを対象にすることで、Segments をさらに絞り込むことができます。

- **過去の購入:**過去 2 年間に特定の色の特定製品を 2 回以上購入したかどうかによって、ユーザーをセグメント化します。
- **イベントとメッセージのインタラクション:**過去 30 日間に購入を行ったかどうか、また特定のアプリ内メッセージと対話したかどうかによって、ユーザーをセグメント化します。
- **データのクエリ:** 
  - **Snowflake のクエリ:**[SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/)を使用してSnowflakeを照会することにより、BrazeおよびCRMやデータウェアハウスなどの外部ソースから結合されたデータを含むセグメントユーザー。
  - **データウェアハウスとの同期:**セグメントユーザーは、[CDI Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/) を使用して、データウェアハウスまたはファイルストレージシステムからBrazeに直接同期されたデータを使用します。

