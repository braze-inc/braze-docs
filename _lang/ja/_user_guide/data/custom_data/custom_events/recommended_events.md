---
nav_title: おすすめイベント
article_title: おすすめイベント
alias: /recommended_events/
page_type: reference
description: "この参考記事では、Brazeが提供するeコマースイベントの推奨イベント（recommended events）について説明する。"
---

# おすすめイベント

> 推奨されるイベントは、最も一般的なeコマースのユースケースに対応している。推奨イベントを使用することで、事前に作成されたキャンバステンプレート、カスタマーライフサイクルにマッピングされたレポートダッシュボードなどをアンロックすることができる。

例えば、"cart_updated "または "update_to_cart "というカスタムイベントを用意し、ユーザーがカート内の商品を追加、削除、または更新したときを捕捉することができる。推奨されるイベントについては、Brazeは、定義されたイベント名とこのイベントに関連するプロパティを含むイベントテンプレートを提供する。

{% alert important %}
推奨イベントは現在早期アクセス中である。早期アクセスにご興味のある方は、Brazeカスタマーサクセスマネージャーまでお問い合わせください。<br><br>新しい[Shopifyコネクタを]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/)活用している場合、これらの推奨イベントは統合によって自動的に利用できるようになる。
{% endalert %}

## CDI の仕組み

Brazeはすべての推奨イベントに特別なバリデーションを適用し、推奨イベントには特別な後処理アクションがあるものもある。特定の業界が推奨するイベントについては、BrazeはキャンペーンやCanvasの新しいアクションベースのトリガーなど、特別な処理をサポートする場合がある。

推奨イベントは[カスタムイベントと]({{site.baseurl}}/user_guide/data/custom_data/custom_events)同様の機能を持つ。カレントの推奨イベントをエクスポートし、ブロックリストに登録し、レポートに使用することができる。[Braze SDK]({{site.baseurl}}/developer_guide/getting_started/sdk_overview)または[`/users/track` エンドポイントを]({{site.baseurl}}/api/endpoints/user_data/post_user_track)使用して、これらのイベントをトラッキング追跡するためにBrazeにデータを送信することもできる。

### eコマース推奨イベント

[eコマースの推奨イベントは]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/)、推奨イベントに基づいている。これらのeコマース推奨イベントは、商品を見たり、カートを更新したり、チェックアウトを開始したりといった顧客のアクションを追跡する。 

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`

#### eコマースキャンバスのテンプレート

Braze Canvasの構築済みテンプレートを使って、重要な戦略を実現するアイデアについては、[eコマース]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/)専用の[ユースケースを]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/)ご覧ください。

## よくある質問

### 推奨イベントはカスタムイベントと同じか？

いや、Brazeは推奨されるイベントに対して、意見付きのデータスキーマを定義する。これには、Brazeで検証プロセスを経る必須およびオプションのイベントプロパティが含まれる。[カスタムイベントとは]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)、アプリやWebサイトでユーザーが行った特定のアクションや更新を追跡するものである。イベント名やトラッキングする内容はカスタムできる。

### おすすめイベントの名前をカスタムできるか？

推奨されるイベントは、標準化されたイベント名とプロパティを持っている。これらの標準化は、データ全体に一貫性を持たせるのに役立つ。

### 購入イベントを使用して購入履歴を記録することは可能か？

eコマース推奨イベントの開始に伴い、Brazeは将来的にレガシー購入イベントを段階的に廃止していく。現在、購入イベントを利用している場合は、非推奨プランに関する事前通知を受け取ることになる。その間は、正式な廃止日まで購入イベントを使い続けることができる。