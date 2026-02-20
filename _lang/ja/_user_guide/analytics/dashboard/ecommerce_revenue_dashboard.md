---
nav_title: イーコマース収入ダッシュボード
article_title: イーコマース収入ダッシュボード
alias: "/ecommerce_revenue_dashboard/"
page_order: 6
description: "本稿では、イーコマースレベニュー-ラストタッチアトリビューションダッシュボードの概略を紹介する。"
---

# イーコマース収入ダッシュボード

> **eCommerce Revenue - Last Touch Attribution**ダッシュボードは、[eCommerce推奨イベント]({{site.baseurl}}/ecommerce_events/)を使用して、キャンペーンsとキャンバスのラストタッチ属性d収益を追跡します。このダッシュボードを使用して、どのメッセージが収益を促進するかを理解し、eコマースパフォーマンス全体を経時的に監視します。

{% alert note %}
e コマースの推奨イベントは現在、早期アクセス段階です。早期アクセスにご興味のある方は、Brazeカスタマーサクセスマネージャーまでお問い合わせください。<br><br>新しい[Shopify コネクター]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector) を使用している場合、これらの推奨されるイベントは、インテグレーションによって自動的に利用可能になります。それ以外の場合、これらのイベントは、データアプリがこのダッシュボードで耳に入る前に実装する必要があります。
{% endalert %}

eコマースの収益ダッシュボードを表示するには、**Analytics** > **ダッシュボード Builder**に移動し、**eCommerce Revenue - Last Touch Attribution**を選択します。このダッシュボード レポートでは、選択したコンバージョンウィンドウ内で、収益属性d を最後のキャンペーンまたはキャンバスに表示してから、ユーザーを操作してから発注します。

## 使用可能なメトリック

| 指標 | 定義 |
| --- | --- |
| e コマース収益 | 選択した日付範囲とコンバージョンウィンドウに基づいた最後のタッチ属性の総収益。 |
| 1 日あたりの注文数 | 1 日あたりの個別注文の平均数。 |
| 1 日あたりの e コマース収益平均 | 選択した期間の1 日あたりの平均属性d 収益。 |
| 時間経過に伴う e コマース収益 | 選択した日付範囲の属性d 収益の時系列。 |
| キャンペーン別 e コマース収益 | キャンペーン別の売上高構成比 | 
| キャンバス別 e コマース収益 | キャンバス別の属性付き収益。 |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## 属性モデル

**eCommerce Revenue - Last Touch アトリビューション** ダッシュボードはラストタッチアトリビューションを使用します。つまり、収益は、発注前に関与したユーザーの最新のBraze キャンペーンまたはキャンバスに属性されます。

{% alert important %}
メッセージインターアクションs は、選択したコンバージョンウィンドウ内で発生している必要があります。コンバージョンウィンドウ内にメッセージインターアクションがない注文は、属性dではありません。
{% endalert %}

## 対象データ

**eCommerce Revenue - Last Touch Attribution** ダッシュボードは、eCommerce 推奨イベントからデータを取得します。

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

収益と発注数は、Braze標準化された計算を使用します。

| 指標 | 計算 |
| --- | --- |
| 総収益 | 発注値の合計- 返金値の合計 |
| 注文数の合計 | 個別受注-個別受注キャンセル主導 |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

### 除外データ

レガシー購入イベントを使用してログに記録された購入は含まれません。**eCommerce Revenue - Last Touch Attribution** ダッシュボードは、現在、キャンペーン s またはCanvase 内の生涯価値や収益レポートなど、レガシー購入イベントに関連付けられた機能に対応していません。 


## 通貨処理

すべての収益はUSDで表示されます。米ドル以外の通貨は、事象がレポートされた日の為替レートを使用して米ドルに換算されます。コンバージョンを防止するには、イベント送信時に通貨を`USD` にハードコードします。
