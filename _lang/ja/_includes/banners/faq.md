# バナー:よくある質問

> これらは、Braze のBanners に関するよくある質問に対する回答です。より一般的な情報については、[バナーについて]を]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners{% endif %})参照せよ。

## バナーの更新はいつユーザーに表示されるのか？

バナーはリフレッシュメソッドを呼び出すたびに最新のデータで更新される。バナーキャンペーンを再送信したり更新したりする必要はない。

## 1回のセッションで何件の配置をリクエストできるのか？

1回の更新リクエストで、最大10個のプレースメントをリクエストできる。Brazeが提供するサービスでは、ユーザーが対象となるバナーの中で、優先度が最も高いものを、リクエストごとに返す。追加のリクエストはエラーを返す。

詳細については、[配置リクエスト]を参照]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners#requests{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#requests{% endif %})せよ。

## 同時にアクティブにできるバナーキャンペーンはいくつあるか？

各ワークスペースは最大200のアクティブなバナーキャンペーンをサポートできる。この制限に達した場合、新しいキャンペーンを作成する前に、既存のキャンペーンを[アーカイブするか無効化する]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status)必要がある。

## 同じ掲載枠を共有するキャンペーンでは、どのバナーが最初に表示されるのか？

ユーザーが同じ掲載位置を共有する複数のバナー広告キャンペーンの対象となる場合、優先順位が最も高いバナーが表示される。詳細については、[バナー優先度]を参照]({% if include.section == "user" %}{{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority{% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/banners#priority{% endif %})せよ。

## 既存のコンテンツカードフィードでバナーを使えるか？

バナーはコンテンツカードとは異なる。つまり、同じフィード内でバナーとコンテンツカードを併用することはできない。既存のコンテンツカードフィードをバナーに置き換えるには、[アプリやWeb サイト内に配置場所を作成]({{site.baseurl}}/developer_guide/banners/placements/)する必要がある。

## ユーザーのアクションに基づいてバナーを表示させることはできるか？

バナーは[アクションベースの配信]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery)をサポートしていないが、セグメンテーションと優先度を活用すれば、ユーザーの過去の行動に基づいてターゲティングできる。

例えば、特定の`purchase`イベントを完了したユーザーだけに特別なバナーを表示するには：
1. **ターゲティング：**キャンペーンでは、カスタムイベントを`purchase`少なくとも一度実行したユーザーセグメントをターゲットに設定する。
2. **優先度:**すべてのユーザー向けの一般的なバナーと、購入者を対象とした特定のバナーが同じ配置をターゲットにしている場合、特定のバナーの優先度を**「高」**に設定し、一般的なバナーの優先度を**「中」**または**「低」**に設定する。

ユーザーが新しいセッションを開始するか、アクション実行後にバナーを更新すると、Brazeはその適格性を評価する。「購入」セグメントに一致する場合、優先度の高いバナーが表示される。


## ユーザーは手動でバナーを閉じることができるか？

いいえ。ユーザーは手動でバナーを閉じることはできない。ただし、ユーザーセグメントの適格性を管理することで、バナーの表示をコントロールできる。ユーザーがバナー広告キャンペーンのターゲティング条件を満たさなくなると、次のセッションではその広告が表示されなくなる。

例えば、ユーザーが購入するまでプロモーションバナーを表示する場合、購入といったイベントを記録すると、その`purchase_completed`ユーザーをターゲットセグメントから除外できる。結果として、その後のセッションではバナーが表示されなくなる。

## Braze APIを使ってバナーキャンペーンの分析データをエクスポートできるか？

はい。この[`/campaigns/data_series`エンドポイント]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)を使用すれば、バナー広告キャンペーンの表示回数、クリック数、コンバージョン数に関するデータを取得できる。

## ユーザーはいつセグメンテーションされるのか？

ユーザーはセッションの開始時にセグメントされる。キャンペーンのターゲティング対象セグメントがカスタム属性、カスタムイベント、その他のターゲティング属性に依存する場合、それらの属性はセッション開始時点でユーザーに存在していなければならない。

## 最低のレイテンシーを確保するために、どのようにバナーを構成すればよいのか？

バナーのメッセージングがシンプルであればあるほど、表示が速くなる。バナー広告キャンペーンは、想定されるレイテンシーに対してテストするのが最善だ。例えば、Liquidの属性（例：\`@attribute\`）を必ず`catalog_items`テストすること。

## すべてのLiquidタグはサポートされているのか？

いいえ。ただし、ほとんどのLiquidタグはバナーメッセージでサポートされている。ただし`catalog_items`、`[<LI>``:rerender`タグ]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid)を使用して再レンダリングされるものは除く。

## クリックイベントをキャプチャできるか？

はい。クリックイベントの捕捉方法は、バナーのレンダリング方法によって異なる。

- **標準エディタコンポーネント：**バナーが標準のエディターコンポーネント（画像, 写真、ボタン、テキスト）を使用している場合、SDKの挿入メソッドを使用するとクリックは自動的にトラッキングされる。
- **カスタムコードブロック：**カスタムコードエディタブロック内の要素のクリックをトラッキングしたい場合、カスタムHTML内から\`click\``brazeBridge.logClick()`イベントを呼び出してクリックをトラッキングしなければならない。これは、SDKメソッドを使用してバナーを挿入およびレンダリングする場合にも適用される。完全な参照については、[バナー用のカスタムコードとJavaScriptブリッジを]({{site.baseurl}}/user_guide/message_building_by_channel/banners/custom_code/#javascript-bridge)参照のこと。
- **カスタムUI（ヘッドレス）：**バナーのHTMLをレンダリングせずに、バナーのカスタムプロパティを使って完全にカスタムUIを構築する場合、アプリケーションコードからバナーオブジェクトに対して\`setCustomProperties`logClick()`()`を呼び出す。

詳細については、[クリックの記録を]({{site.baseurl}}/developer_guide/banners/placements/#logging-clicks)参照せよ。
