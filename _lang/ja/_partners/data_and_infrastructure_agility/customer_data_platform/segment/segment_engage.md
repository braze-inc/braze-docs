---
nav_title: セグメント・エンゲージ
article_title: セグメント・エンゲージ
page_order: 3
alias: /partners/segment_personas/
alias: /partners/segment_engage/
alias: /partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_personas/

description: "この参考記事では、BrazeとSegmentのパートナーシップについて概説している。Segmentは、マーケティング・スタックのソース間で情報を収集し、ルーティングする顧客データ・プラットフォームである。"
page_type: partner
search_tag: Partner

---

# セグメント・エンゲージ

> [Segmentは](https://segment.com)、顧客データの収集、クリーニング、活性化を支援する顧客データ・プラットフォームである。この参考記事では、[BrazeとSegment Engageの](https://segment.com/docs/destinations/braze/#Engage)接続の概要を説明するとともに、適切な導入と利用のための要件とプロセスについて述べる。

BrazeとSegmentの統合により、Segmentに組み込まれたオーディエンス・ビルダーである[Engageを使って](https://segment.com/docs/engage/)、様々なソースから収集したデータを基にユーザーのセグメントを作成することができる。これらのオーディエンスは、コホートとしてBrazeに同期されるか、[カスタム属性や]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) [カスタムイベントを通じて]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events)ユーザープロファイルに示され、キャンペーンやキャンバスリターゲティングで使用するBrazeセグメントを作成するために使用できる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| セグメント・アカウント | このパートナーシップを利用するには、[セグメントアカウントが](https://app.segment.com/login)必要である。 |
| ブレイズクラウドの目的地 | Segmentとの統合で、[Brazeを配信先として設定]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/)済みであること。<br><br>これには、[接続]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings)設定で正しいBrazeデータセンターとREST APIキーを提供することが含まれる。 |
| Brazeデータインポートキー | EngageオーディエンスをコホートとしてBrazeに同期するには、データインポートキーを生成する必要がある。<br><br>Brazeのカスタマーサクセスマネージャーに連絡して、この機能にアクセスしよう。 |

{: .reset-td-br-1 .reset-td-br-2}

## コホート 目的地 統合

### ステップ1:エンゲージ・オーディエンスを作る
1. Segmentで、Engageの**Audiences**タブに移動し、**Newを**クリックする。
2. 観客を作る。ページ上部の稲妻は、観客がリアルタイムで更新しているかどうかを示す。
3. 次に、目的地としてブレーズを選択する。
4. **Review & Createを**クリックしてオーディエンスをプレビューする。デフォルトでは、Segmentはすべての履歴データを照会し、計算された特性と観客の現在値を設定する。このデータを省略するには、**ヒストリカル・バックフィルの**チェックを外す。

### ステップ2:コホート・データ・インポート・キーをキャプチャする

Brazeで、**Partner Integrations**>**Technology Partnersに**移動し、**Segmentを**選択する。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**統合」の**下に**テクノロジー・パートナーが**ある。
{% endalert %}

ここで、RESTエンドポイントを見つけ、Brazeデータインポートキーを生成する。鍵の生成後、新しい鍵を作成したり、既存の鍵を無効にしたりすることができる。

### ステップ3:ブレイズ・コホーツの目的地をつなぐ
[Segmentの指示に従って](https://segment.com/docs/connections/destinations/catalog/actions-braze-cohorts/#getting-started)Cohorts Destinationを設定し、EngageオーディエンスをコホートとしてBrazeに同期する。

### ステップ4:EngageのオーディエンスからBrazeセグメントを作成する。
Brazeで**Segmentsに**移動し、新しいセグメントを作成し、フィルターとして**Segment Cohortsを**選択する。ここから、どのセグメントのコホートを含めるかを選択できる。セグメントコホートセグメントを作成した後、キャンペーンまたはキャンバスを作成する際に、オーディエンスフィルターとして選択することができる。

![][1]

## クラウドモードの統合

### ステップ1:セグメントで計算された特性または聴衆を作成する

1. Segmentで、**Engageの** **Computed Traits**または**Audiences**タブに移動し、**Newを**クリックする。
2. 競合の特徴やオーディエンスを作る。ページの上隅にある稲妻は、計算がリアルタイムで更新されているかどうかを示す。
3. 次に、目的地として**ブレーズを**選択する。 
4. **Review & Createを**クリックしてオーディエンスをプレビューする。デフォルトでは、Segmentはすべての履歴データを照会し、計算された特性と観客の現在値を設定する。このデータを省略するには、**ヒストリカル・バックフィルの**チェックを外す。
5. 計算された特性または視聴者設定で、Brazeへのデータ送信方法に基づいて接続設定を調整する。

#### 計算された特徴とオーディエンス

[計算された特性や](https://segment.com/docs/engage/audiences/computed-traits/) [オーディエンスは](https://segment.com/docs/Engage/audiences/)、カスタム属性やカスタムイベントとしてBrazeに送ることができる。
- `identify` 、カスタム属性としてBrazeに表示される。
- `track` 、カスタムイベントとしてBrazeに表示される。

計算された形質をBrazeのデスティネーションに接続する際に、どちらの方法を使うか（あるいは両方を使うか）を選択できる。

{% tabs %}
{% tab 特定する %}

Brazeでカスタム属性を作成するために、計算された形質とオーディエンスを`identify` 呼び出しとしてBrazeに送ることができる。 

例えば、"Last Product Viewed Item"（最後に見た商品）に対してEngageが計算した特質がある場合、ユーザーのBrazeプロフィールの**Custom Attributes（カスタム属性**）に`last_product_viewed_item` 。これがエンゲージオーディエンスであった場合、**カスタム属性の**下に`true` として設定されたオーディエンスが表示される。

| 計算された形質 | 観客 |
| -------------- | --------- |
| ![ユーザー・プロフィール内のカスタム属性セクションに、"last_product_viewed_item" が "Sweater" としてリストされている。]({% image_buster /assets/img/segment/last_viewed-id-braze.png %}) | ![] （{% image_buster /assets/img/segment/dormant-identify-braze.png %} ）。 |

{% endtab %}
{% tab トラック %}

計算された特性やオーディエンスを`track` 呼び出しとしてBrazeに送信し、Brazeでカスタムイベントを作成することができる。 

前の例の続きで、もしユーザーが "Last Product Viewed Item "の計算された特徴を持っている場合、それはユーザーのBrazeプロフィールに`Trait Computed` 、対応するカウントと最新のタイムスタンプと共に**Custom Eventsの**下に表示される。これがEngageオーディエンスであった場合、オーディエンス、カウント、および最新のタイムスタンプは、`true` として設定された**カスタム属性の**下に表示される。

| 計算された形質 | 観客 |
| -------------- | --------- |
| ![ユーザープロファイル内のカスタムイベントセクションには、"Trait Computed "が "1 "回表示され、最後に表示されたのは "20時間前 "である。]({% image_buster /assets/img/segment/last_viewed-track-braze.png %}) | ![ユーザー・プロフィール内のカスタム属性セクションには、"観客動員数 "の "1 "時間が表示され、最終時間は "3月9日午前1時45分 "である。]({% image_buster /assets/img/segment/dormant-track-braze.png %}) |

{% endtab %}
{% endtabs %}

### ステップ2:Brazeのセグメントユーザー

Brazeで、これらのユーザーのセグメントを作成するには、**Engagementの**下の**Segmentsに**移動し、新しいセグメントを作成し、セグメントに名前を付ける。次に、どのコールを使用したかによる：
- **特定する**：フィルターとして**カスタム属性を**選択し、カスタム属性を探す。次に、"matches regex "オプション（特徴）または "equals "オプション（観客）を使い、適切な変数を入力する。
- **トラック**フィルターとして**カスタムイベントを**選択し、カスタムイベントを探す。次に、"more than"、"less than"、"justly "のオプションを使い、希望の値を入れる。これは、セグメントをどのように定義したいかによる。

一度保存すれば、キャンバスやキャンペーン作成時に、ユーザーをターゲティングするステップでこのセグメントを参照することができる。

## 同期時間

BrazeからSegment Engageへの接続のデフォルト設定は`Realtime` 、ペルソナをリアルタイム同期から除外するフィルターがいくつかある。これには、メッセージ送信時のオーディエンスのサイズを制限する時間ベースのフィルターも含まれる。

## セグメント・デバッガのテスト

セグメントのダッシュボードには「デバッガー」機能があり、「ソース」からのデータが期待通りに「デスティネーション」に転送されているかどうかをテストすることができる。

この機能は、Braze[`/users/track` エンドポイントに]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)接続する。つまり、識別されたユーザー（BrazeユーザープロファイルのユーザーIDをすでに持っているユーザー）にのみ使用できる。

これはサイドバイサイドのBrazeとの統合には使えない。正しいBraze REST API情報が入力されていない場合、サーバーデータは通過しない。

[1]: {% image_buster /assets/img/segment/segment3.png %}