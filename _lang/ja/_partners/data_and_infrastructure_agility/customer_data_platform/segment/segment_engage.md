---
nav_title: Segment Engage
article_title:セグメントエンゲージ
page_order:3
alias: /partners/segment_personas/
alias: /partners/segment_engage/
alias: /partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_personas/

description:「この参考記事では、Braze と Segment のパートナーシップについて概説しています。Segment は、マーケティングスタック内のソース間で情報を収集およびルーティングするカスタマーデータプラットフォームです。」
page_type: partner
search_tag:Partner

---

# セグメントエンゲージ

> [セグメント](https://segment.com)は、顧客データを収集、クリーン、およびアクティブ化するのに役立つ顧客データプラットフォームです。この記事では、[BrazeとSegment Engage](https://segment.com/docs/destinations/braze/#Engage)の接続に関する概要を説明し、適切な実装と使用のための要件とプロセスについて説明します。

BrazeとSegmentの統合により、Segmentの組み込みオーディエンスビルダーである[Engage](https://segment.com/docs/engage/)を使用して、さまざまなソースから既に収集したデータに基づいてユーザーのセグメントを作成できます。これらのオーディエンスはコホートとしてBrazeに同期されるか、[カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/)または[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events)を通じてユーザープロファイルに示され、キャンペーンおよびCanvasリターゲティングで使用するためのBrazeセグメントを作成するために使用できます。

## 前提条件

| 要件 | 説明 |
| ----------- | ----------- |
| セグメントアカウント | [セグメントアカウント](https://app.segment.com/login)を利用するには、このパートナーシップを活用する必要があります。 |
| Braze Cloud 宛先 | セグメント統合でBrazeを送信先として[設定済みである必要があります]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/)。<br><br>これには、[接続設定]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings)で正しいBrazeデータセンターとREST APIキーを提供することが含まれます。 |
| Brazeデータインポートキー | BrazeにコホートとしてEngageオーディエンスを同期するには、データインポートキーを生成する必要があります。<br><br>コホートインポートは早期アクセス中です。この機能にアクセスするには、Brazeのカスタマーサクセスマネージャーに連絡してください。 |

{: .reset-td-br-1 .reset-td-br-2}

## コホート先統合

### ステップ1:エンゲージオーディエンスを作成する
1. セグメントで、Engageの**オーディエンス**タブに移動し、**新規**をクリックします。
2. オーディエンスを作成します。ページの隅にある稲妻のアイコンは、オーディエンスがリアルタイムで更新されるかどうかを示します。
3. 次に、Brazeを宛先として選択します。
4. オーディエンスをプレビューするには、**レビューと作成**をクリックします。デフォルトでは、セグメントは計算された特性とオーディエンスの現在の値を設定するためにすべての履歴データを照会します。このデータを省略するには、**履歴のバックフィル**のチェックを外します。

### ステップ2:コホートデータインポートキーをキャプチャする

Brazeで、**パートナー統合** > **テクノロジーパートナー** に移動し、**セグメント** を選択します。

{% alert note %}
古いナビゲーションを使用している場合は、テクノロジーパートナーを統合の下に見つけることができます。
{% endalert %}

ここでは、RESTエンドポイントを見つけて、Brazeデータインポートキーを生成します。キーが生成された後、新しいキーを作成するか、既存のキーを無効にすることができます。

### ステップ3:Brazeコホートの宛先に接続する
Segment の指示に従って、Cohorts Destination を設定し、Engage オーディエンスを Braze にコホートとして同期します。

### ステップ 4:エンゲージオーディエンスからBrazeセグメントを作成する
Brazeで、**セグメント**に移動し、新しいセグメントを作成して、フィルターとして**セグメントコホート**を選択します。ここから、含めたいセグメントコホートを選択できます。セグメントコホートセグメントが作成された後、キャンペーンやキャンバスを作成する際にオーディエンスフィルターとして選択できます。

![][1]

## クラウドモード統合

### ステップ1:セグメント計算特性またはオーディエンスを作成する

1. セグメントで、**計算された特性**または**オーディエンス**タブに移動し、**エンゲージ**で**新規**をクリックします。
2. 計算された特性またはオーディエンスを作成します。ページの隅にある稲妻のアイコンは、計算がリアルタイムで更新されるかどうかを示します。
3. 次に、**Braze**を目的地として選択します。 
4. **レビューと作成**をクリックして、オーディエンスをプレビューします。デフォルトでは、セグメントは計算された特性とオーディエンスの現在の値を設定するためにすべての履歴データを照会します。このデータを省略するには、**履歴のバックフィル**のチェックを外します。
5. 計算されたトレイトまたはオーディエンス設定で、データをBrazeに送信する方法に基づいて接続設定を調整します。

#### 計算された特性とオーディエンス

[計算された特性](https://segment.com/docs/engage/audiences/computed-traits/)と[オーディエンス](https://segment.com/docs/Engage/audiences/)は、カスタム属性またはカスタムイベントとしてBrazeに送信できます。
- `identify` コールを使用して送信された特性とオーディエンスは、Braze にカスタム属性として表示されます。
- `track`呼び出しを使用して送信された特性とオーディエンスは、カスタムイベントとしてBrazeに表示されます。

接続された計算済みの特性をBrazeの宛先に接続する際に、どの方法を使用するか（または両方を使用するか）を選択できます。

{% tabs %}
{% tab Identify %}

Brazeにカスタム属性を作成するために、計算された特性とオーディエンスを`identify`呼び出しとしてBrazeに送信できます。 

例えば、「最後に見た商品」のEngage計算属性がある場合、Brazeプロファイルの**カスタム属性**の下に`last_product_viewed_item`が表示されます。これが代わりにEngageオーディエンスであった場合、オーディエンスは**カスタム属性**に`true`としてリストされます。

| 計算された特性 | 観客 |
| -------------- | --------- |
| ![The custom attribute section within a user profile lists "last_product_viewed_item" as "Sweater".]({% image_buster /assets/img/segment/last_viewed-id-braze.png %}) | ![The custom attribute section within a user profile lists "dormant_shopper" as "true".]({% image_buster /assets/img/segment/dormant-identify-braze.png %}) |

{% endtab %}
{% tab Track %}

Brazeにカスタムイベントを作成するための`track`コールとして計算された特性とオーディエンスを送信できます。 

前の例を続けると、ユーザーが「最後に見た商品アイテム」の計算された特性を持っている場合、それはユーザーのBrazeプロファイルに`Trait Computed`として表示され、対応するカウントと最新のタイムスタンプが**カスタムイベント**の下に表示されます。これが代わりにEngageオーディエンスであった場合、オーディエンス、カウント、および最新のタイムスタンプが**カスタム属性**にリストされ、`true`として設定されます。

| 計算された特性 | 観客 |
| -------------- | --------- |
| ![The custom event section within a user profile lists "Trait Computed" "1" time, with the last time being "20 hours ago".]({% image_buster /assets/img/segment/last_viewed-track-braze.png %}) | ![The custom attribute section within a user profile lists "Audience Entered" "1" time, with the last time being "March 9 at 1:45 am".]({% image_buster /assets/img/segment/dormant-track-braze.png %}) |

{% endtab %}
{% endtabs %}

### ステップ2:Brazeでユーザーをセグメント化する

Brazeでは、これらのユーザーのセグメントを作成するには、**セグメント**の下の**エンゲージメント**に移動し、新しいセグメントを作成して、セグメントに名前を付けます。次に、使用した呼び出しに基づいて:
- **識別**:フィルターとして**カスタム属性**を選択し、カスタム属性を見つけます。次に、「一致する正規表現」オプション（特性）または「等しい」オプション（オーディエンス）を使用し、適切な変数を入力します。
- **トラック**:フィルターとして**カスタムイベント**を選択し、カスタムイベントを見つけます。次に、「より大きい」、「より小さい」、または「正確に」オプションを使用し、希望する値を入力します。これは、セグメントの定義方法によります。

保存すると、キャンバスやキャンペーンの作成時にターゲットユーザーのステップでこのセグメントを参照できます。

## 同期時間

BrazeからSegment Engageへの接続のデフォルト設定は`Realtime`ですが、リアルタイムでの同期を失格とするいくつかのフィルターがあり、メッセージ送信時にオーディエンスのサイズを制限する時間ベースのフィルターも含まれます。

## セグメントデバッガーテスト

セグメントのダッシュボードには、「デバッガー」機能があり、顧客が「ソース」から「デスティネーション」へのデータ転送が期待通りに行われているかどうかをテストできます。

この機能はBraze [`/users/track`エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)に接続するため、識別されたユーザー（すでにBrazeユーザープロファイルにユーザーIDを持っているユーザー）にのみ使用できます。

これはサイドバイサイドのBraze統合では機能しません。正しいBraze REST API情報を入力していない場合、サーバーデータは通過しません。

[1]: {% image_buster /assets/img/segment/segment3.png %}