---
nav_title: おすすめイベント
article_title: おすすめイベント
alias: /recommended_events/
page_type: reference
description: "この参考記事では、Brazeが提供するeコマースイベントの推奨イベント（recommended events）について説明する。"
---

# おすすめイベント

> 推奨されるイベントは、最も一般的なeコマースのユースケースに対応している。推奨イベントを使用することで、事前に作成されたキャンバステンプレート、カスタマーライフサイクルにマッピングされたレポートダッシュボードなどをアンロックすることができる。

例えば、“cart_updated” または“update_to_cart” というカスタムイベントを用意して、ユーザーがカート内の商品を追加、削除、更新したタイミングを捕捉することができる。推奨されるイベントについては、Brazeは、定義されたイベント名とこのイベントに関連するプロパティを含むイベントテンプレートを提供する。

{% alert important %}
推奨イベントは現在早期アクセス段階です。早期アクセスにご興味のある方は、Brazeカスタマーサクセスマネージャーまでお問い合わせください。<br><br>新しい[Shopifyコネクタを]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector)活用している場合、これらの推奨イベントは統合によって自動的に利用できるようになる。
{% endalert %}

## CDI の仕組み

Brazeはすべての推奨イベントに特別なバリデーションを適用し、推奨イベントには特別な後処理アクションがあるものもある。特定の業界の推奨イベントについては、Braze は特別な処理 (キャンペーンやキャンバスの新しいアクションベースのトリガーなど) をサポートすることがあります。

推奨イベントは[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events)と同様に機能します。Currents から推奨イベントをエクスポートし、ブロックリストに登録し、レポートに使用することができます。[Braze SDK]({{site.baseurl}}/developer_guide/getting_started/sdk_overview) または[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を使用して、これらのイベントを追跡するために Braze にデータを送信することもできます。

### eコマース推奨イベント

[e コマースの推奨イベント]({{site.baseurl}}/ecommerce_events/)は、推奨イベントに基づいています。e コマースの推奨イベントは、顧客のアクション (製品の閲覧、カートの更新、購入手続きの開始) を追跡します。 

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

#### eコマースキャンバスのテンプレート

Braze Canvasの構築済みテンプレートを使って、重要な戦略を実現するアイデアについては、[eコマース専用のユースケースを]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/)ご覧ください。

## よくある質問

### 推奨イベントはカスタムイベントと同じか？

いいえ。Braze は推奨イベントについて制約の強い (opinionated) データスキーマを定義します。これには、Brazeで検証プロセスを経る必須およびオプションのイベントプロパティが含まれる。[カスタムイベントとは]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)、アプリやWebサイトでユーザーが行った特定のアクションや更新を追跡するものである。イベント名やトラッキングする内容はカスタムできる。

### おすすめイベントの名前をカスタムできるか？

推奨イベントには、標準化されたイベント名とプロパティがあります。これらの標準化は、データ全体に一貫性を持たせるのに役立つ。

### 購入イベントを使用して購入履歴を記録することは可能か？

e コマースの推奨イベントの導入に伴い、Braze は今後、従来の購入イベントを段階的に廃止していく予定です。現在、購入イベントを利用している場合は、非推奨プランに関する事前通知を受け取ることになる。正式な廃止日までは購入イベントを使い続けることができます。