---
nav_title: Segment Engage
article_title: Segment Engage
page_order: 3
alias: /partners/segment_personas/
alias: /partners/segment_engage/
alias: /partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_personas/

description: "この参考記事では、BrazeとSegmentのパートナーシップについて概説している。Segmentは、マーケティング・スタックのソース間で情報を収集し、ルーティングする顧客データ・プラットフォームである。"
page_type: partner
search_tag: Partner

---

# Segment Engage

> [Segment](https://segment.com) は、顧客データの収集、クリーンアップ、およびアクティブ化を支援する顧客データプラットフォームです。このリファレンス記事では、[Braze と Segment Engage](https://segment.com/docs/destinations/braze/#Engage) の接続について概説し、適切な実装と利用のための要件とプロセスを説明します。

BrazeとSegmentの統合により、Segmentに組み込まれたオーディエンス・ビルダーである[Engageを使って](https://segment.com/docs/engage/)、様々なソースから収集したデータを基にユーザーのセグメントを作成することができる。これらのオーディエンスは、コホートとしてBrazeに同期されるか、[カスタム属性や]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) [カスタムイベントを通じて]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events)ユーザープロファイルに示され、キャンペーンやキャンバスリターゲティングで使用するBrazeセグメントを作成するために使用できる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Segment アカウント | このパートナーシップを活用するには、[Segment アカウント](https://app.segment.com/login)が必要です。 |
| Braze Cloud の宛先 | Segment 統合で [Braze を宛先として設定]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/)している必要があります。<br><br>これには、[接続]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings)設定で正しいBrazeデータセンターとREST APIキーを提供することが含まれる。 |
| Brazeデータインポートキー | Engage オーディエンスをコホートとして Braze に同期するには、データインポートキーを生成する必要があります。<br><br>コホートのインポート機能は早期アクセスの段階であるため、この機能を利用するには Braze のカスタマーサクセスマネージャーにお問い合わせください。 |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## コホート宛先の統合

### ステップ1:Engage オーディエンスを作成する
1. Segment で、Engage の [**Audiences**] タブに移動し、[**New**] をクリックします。
2. オーディエンスを作成します。ページ上部の稲妻は、オーディエンスがリアルタイムで更新されているかどうかを示します。
3. 次に、宛先として Braze を選択します。
4. [**Review & Create**] をクリックしてオーディエンスをプレビューします。デフォルトでは、Segment は計算済み特性とオーディエンスの現在の値を設定するため、すべての履歴データをクエリします。このデータを省略するには、[**Historical Backfill**] をオフにします。

### ステップ2:コホートデータインポートキーをキャプチャする

Brazeで、[**パートナー連携**] > [**テクノロジーパートナー**] に移動し、[**Segment**] を選択します。

ここで、RESTエンドポイントを見つけて、Brazeデータインポートキーを生成します。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。

### ステップ3:Braze コホートの宛先を接続する
Cohorts Destination の設定に関する[Segment の手順](https://segment.com/docs/connections/destinations/catalog/actions-braze-cohorts/#getting-started)に従って、Engage オーディエンスをコホートとして Braze に同期します。

### ステップ4:EngageのオーディエンスからBrazeセグメントを作成する。
Braze で [**セグメント**] に移動し、新しいセグメントを作成し、フィルターとして [**セグメントコホート**] を選択します。ここから、どの Segment コホートを含めるかを選択できます。セグメントコホートセグメントを作成した後、キャンペーンまたはキャンバスを作成する際に、オーディエンスフィルターとして選択することができる。

![][1]

## クラウドモードの統合

### ステップ1:Segment の計算済み特性またはオーディエンスを作成する

1. Segmentで、[**Engage**] の [**Computed Traits**] タブまたは [**Audiences**] タブに移動し、[**New**] をクリックします。
2. 計算済み特性またはオーディエンスを作成します。ページの上隅にある稲妻は、計算がリアルタイムで更新されているかどうかを示す。
3. 次に、宛先として **Braze** を選択します。 
4. [**Review & Create**] をクリックしてオーディエンスをプレビューします。デフォルトでは、Segment は計算済み特性とオーディエンスの現在の値を設定するため、すべての履歴データをクエリします。このデータを省略するには、[**Historical Backfill**] をオフにします。
5. 計算された特性または視聴者設定で、Brazeへのデータ送信方法に基づいて接続設定を調整する。

#### 計算された特徴とオーディエンス

[計算された特性や](https://segment.com/docs/engage/audiences/computed-traits/) [オーディエンスは](https://segment.com/docs/Engage/audiences/)、カスタム属性やカスタムイベントとしてBrazeに送ることができる。
- `identify` 呼び出しを使用して送信された特性とオーディエンスは、Braze ではカスタム属性として表示されます。
- `track` 呼び出しを使用して送信された特性とオーディエンスは、Braze ではカスタムイベントとして表示されます。

計算された形質をBrazeのデスティネーションに接続する際に、どちらの方法を使うか（あるいは両方を使うか）を選択できる。

{% tabs %}
{% tab Identify %}

Braze でカスタム属性を作成するために、計算済み特性とオーディエンスを `identify` 呼び出しとして Braze に送信できます。 

例えば、"Last Product Viewed Item"（最後に見た商品）に対してEngageが計算した特質がある場合、ユーザーのBrazeプロフィールの**Custom Attributes（カスタム属性**）に`last_product_viewed_item` 。これが Engage のオーディエンスであった場合、[**カスタム属性**] の下に `true` として設定されたオーディエンスが表示されます。

| 計算済み特性 | オーディエンス |
| -------------- | --------- |
| ![ユーザープロファイル内のカスタム属性セクションに、「last_product_viewed_item」 が「Sweater」としてリストされている。]({% image_buster /assets/img/segment/last_viewed-id-braze.png %}) | ![ユーザープロファイル内のカスタム属性セクションに、「dormant_shopper」が「tru」としてリストされている。]({% image_buster /assets/img/segment/dormant-identify-braze.png %}) |

{% endtab %}
{% tab Track %}

Braze でカスタムイベントを作成するために、計算済み特性とオーディエンスを `track` 呼び出しとして Braze に送信できます。 

前の例の続きで、もしユーザーが "Last Product Viewed Item "の計算された特徴を持っている場合、それはユーザーのBrazeプロフィールに`Trait Computed` 、対応するカウントと最新のタイムスタンプと共に**Custom Eventsの**下に表示される。これがEngageオーディエンスであった場合、オーディエンス、カウント、および最新のタイムスタンプは、`true` として設定された**カスタム属性の**下に表示される。

| 計算済み特性 | オーディエンス |
| -------------- | --------- |
| ![ユーザープロファイル内のカスタムイベントセクションに、「Trait Computed」「1」回、「Last time」として「20 hours ago」が表示されている。]({% image_buster /assets/img/segment/last_viewed-track-braze.png %}) | ![ユーザープロファイル内のカスタム属性セクションに、「Audience Entered」、「1」回、Last time」として「March 9 at 1:45 am」が表示されている。]({% image_buster /assets/img/segment/dormant-track-braze.png %}) |

{% endtab %}
{% endtabs %}

### ステップ2:Brazeのセグメントユーザー

Braze でこれらのユーザーのセグメントを作成するには、[**エンゲージメント**] の下の [**セグメント**] に移動し、新しいセグメントを作成し、セグメントに名前を付けます。次に、使用した呼び出しに基づいて作業を行います。
- **Identify**:フィルターとして**カスタム属性を**選択し、カスタム属性を探す。次に、"matches regex "オプション（特徴）または "equals "オプション（観客）を使い、適切な変数を入力する。
- **Track**:フィルターとして**カスタムイベントを**選択し、カスタムイベントを探す。次に、[より大きい]、[より小さい]、[完全一致] オプションのいずれかを使用して必要な値を挿入します。これは、セグメントをどのように定義したいかによる。

一度保存すれば、キャンバスやキャンペーン作成時に、ユーザーをターゲティングするステップでこのセグメントを参照することができる。

## 同期時間

Braze から Segment Engage への接続のデフォルト設定は `Realtime` ですが、ペルソナがリアルタイム同期を実行できないようにするいくつかのフィルターがあります。これには、メッセージ送信時のオーディエンスのサイズを制限する時間ベースのフィルターが含まれます。

## Segment デバッガーのテスト

Segment のダッシュボードにある「Debugger」機能により、顧客は「ソース」からのデータが予期されているとおりに「宛先」に転送されているかどうかをテストできます。

この機能は Braze [`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)に接続します。つまり、この機能は識別されたユーザー (Braze ユーザープロファイルのユーザー ID がすでに設定されているユーザー) のみに使用できます。

これはサイドバイサイドの Braze 統合では機能しません。正しい Braze REST API 情報が入力されていない場合、サーバーデータは転送されません。

[1]: {% image_buster /assets/img/segment/segment3.png %}