# バナー:よくある質問

> これらは、Braze のBanners に関するよくある質問に対する回答です。一般的な情報については、[バナーについて]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %})] を参照してください。

## バナー・更新がアプリの耳元をユーザーsにするのはいつ？

バナーは、最新表示メソッドを呼び出すたびに最新のデータで更新されます。バナーキャンペーンを再送信または更新する必要はありません。

## 1セッションにいくつの打ち込みをリクエストできますか?

1 回の更新リクエストで、最大 10 個の配置をリクエストできます。Braze は、リクエストするたびに、ユーザーが適格である最も優先度の高いバナーを返します。追加のリクエストはエラーを返します。

詳細については、[Placement requests]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %})を参照してください。

## 同時に有効にできるバナーキャンペーンの数は?

それぞれのワークスペースは、最大200 の有効なバナーキャンペーンに対応できます。この制限に達した場合は、[アーカイブするか、既存のキャンペーンを非アクティブ化してから新しいものを作成する必要があります。

## プレイスメントを共有するキャンペーンで、最初に表示されるバナーは?

ユーザーが、同じ配置を共有する複数のバナーキャンペーンに適格である場合、最も高いプライオリティを持つバナーが表示されます。詳細については、[Banner priority]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %})を参照してください。

## 既存のコンテンツカードフィードでバナーを使用できますか?

バナーはコンテンツカードとは異なります。つまり、同じフィードでバナーとコンテンツカードを使用することはできません。既存のコンテンツカードフィードをバナーに置き換えるには、[アプリまたはWeb サイト]({{site.baseurl}}/developer_guide/banners/placements/)に配置を作成する必要があります。

## ユーザー アクション s に基づいてバナーをトリガーできますか?

バナーは[アクションベースの配信]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery)に対応していませんが、これまでのアクションsに基づいてユーザーsをセグメンテーションとプライオリティでターゲットできます。

たとえば、`purchase` イベントを完了したユーザーにのみ特殊なバナーを表示するには、次のようにします。
1. **ターゲット設定:**キャンペーンで、カスタムイベント`purchase` を少なくとも1 回実行したユーザーのSegmentを対象にします。
2. **優先度:**すべてのユーザーに汎用バナーがあり、同じ配置をターゲットとする購入者にこの固有のバナーがある場合は、特定のバナーのプライオリティを**High** に設定し、汎用バナーを**Medium** または**Low** に設定します。

ユーザーがアクションの実行後に新しいセッションを開始するか、バナーを更新すると、Braze はその適格性を評価します。"Purchase"Segmentと一致する場合、優先順位の高いバナーが表示されます。


## ユーザーが手作業でバナーを解任できるか。

いいえ。ユーザーは手動でバナーを削除することはできません。ただし、ユーザー Segmentの適格性を管理することで、バナーの可視性をコントロールできます。ユーザーがバナーキャンペーンのターゲット基準を満たさなくなると、次回のセッション時に再度表示されなくなります。

たとえば、ユーザーが購入するまでプロモーションバナーを表示する場合、`purchase_completed` などのイベントをログに記録すると、そのユーザーをターゲットSegmentから削除でき、バナーを後続のセッションs に事実上隠すことができます。

## Braze API を使用してバナーキャンペーン 分析をエクスポートできますか?

はい。[`/campaigns/data_series`エンドポイント]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)を使用して、表示、クリック、または変換されたバナーキャンペーンの数を取得できます。

## ユーザー s Segment はいつed ですか?

ユーザは、セッションの先頭でSegmented になります。キャンペーンのターゲットSegmentsがカスタム属性s、カスタムイベントs、または他のターゲット属性sに依存する場合、それらはセッションの最初のユーザーに存在しなければなりません。

## 最小のレイテンシーを確保するには、どうすればバナーを作成できますか?

バナーのメッセージングがシンプルであればあるほど、レンダリングが高速になります。バナーキャンペーンをユースケースの予想レイテンシーに照らしてテストすることをお勧めします。例えば、`catalog_items` のように、Liquid 属性 s をテストしてください。

## すべてのリキッドタグはサポートされていますか?

いいえ。ただし、[`:rerender` タグ]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid) を使用して再レンダリングされる`catalog_items` を除き、ほとんどのリキッドタグs はバナーメッセージでサポートされています。

## クリックイベントをキャプチャできますか?

クリックイベントは、クリックアクションが`logClick` 要素に設定され、[JS ブリッジ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#javascript-bridge) を使用して呼び出された場合にのみキャプチャされます。
