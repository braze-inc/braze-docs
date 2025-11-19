# バナー:よくある質問

> これらは、Braze のBanners に関するよくある質問に対する回答です。より一般的な情報については、[バナーについて]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %})]を参照のこと。

## バナーの更新はユーザーにいつ表示されるのか？

バナーは、リフレッシュメソッドを呼び出すたびに最新のデータでリフレッシュされるため、バナーキャンペーンを再送信したり更新したりする必要はない。

## 1セッションに何人の選手を起用できるか？

1回のリフレッシュ・リクエストで、最大10個のプレースメントをリクエストできる。Brazeは、ユーザーがリクエストするごとに、最も優先順位の高いBannerを返す。追加のリクエストはエラーを返す。

詳しくは、[配置リクエスト]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %})を参照のこと。

## いくつのバナーキャンペーンを同時にアクティブにできるか？

各ワークスペースは、最大200のアクティブなバナーキャンペーンをサポートすることができる。この制限に達した場合、新しいキャンペーンを作成する前に、既存のキャンペーンを[アーカイブするか非アクティブにする]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status)必要がある。

## プレースメントを共有するキャンペーンでは、どちらのバナーが最初に表示されるのか？

ユーザーが同じプレースメントを共有する複数のバナーキャンペーンにクオリファイした場合、最も優先順位の高いバナーが表示される。詳しくは[バナーの優先順位]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %})を参照のこと。

## 既存のコンテンツカードフィードでバナーを使用できるか？

つまり、バナーとコンテンツカードを同じフィードで使用することはできない。既存のコンテンツカードフィードをバナーに置き換えるには、[アプリやWebサイトにプレースメントを作成する]({{site.baseurl}}/developer_guide/banners/placements/)必要がある。

## ユーザーはバナーを手動で解除できるか？

ユーザーはバナーを手動で削除することはできない。しかし、ユーザーセグメンテーションの適格性を管理することで、バナーの可視性をコントロールすることができる。ユーザーがバナーキャンペーンのターゲティング基準を満たさなくなった場合、次回のセッションで再びバナーキャンペーンが表示されることはない。

例えば、ユーザーが購入するまでプロモーションバナーを表示する場合、`purchase_completed` のようなイベントを記録することで、そのユーザーをターゲットセグメントから外し、その後のセッションで効果的にバナーを非表示にすることができる。

## Braze APIを使ってバナーキャンペーンの分析をエクスポートできるか？

はい。[`/campaigns/data_series` エンドポイントを]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)使用して、いくつのバナーキャンペーンが閲覧されたか、クリックされたか、またはコンバージョンしたかに関するデータを得ることができる。

## ユーザーはいつセグメンテーションされるのか？

ユーザーはセッションの最初にセグメンテーションされる。キャンペーンのターゲットセグメントがカスタム属性、カスタムイベント、またはその他のターゲティング属性に依存する場合、セッションの開始時にユーザーにそれらが存在する必要がある。

## 最低のレイテンシーを確保するために、どのようにバナーを構成すればよいか？

バナーのメッセージングがシンプルであればあるほど、レンダリングは速くなる。あなたのユースケースで予想されるレイテンシーに対して、バナーキャンペーンをテストするのがベストだ。例えば、`catalog_items` のようなアトリビューション属性は必ずテストすること。

## すべてのLiquidタグに対応しているか？

しかし、[`:rerender` タグを使って]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid)再レンダリングされる`catalog_items` を除いて、ほとんどの Liquid タグはバナーメッセージでサポートされている。

## クリックイベントをキャプチャできるか？

クリックイベントは、`logClick` 要素にon-clickアクションが設定され、[JSブリッジを]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#javascript-bridge)使用して呼び出された場合にのみキャプチャされる。
