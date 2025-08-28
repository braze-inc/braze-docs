---
nav_title: 推奨イベント
article_title: 推奨イベント
alias: /recommended_events/
page_type: reference
description: "この参考記事では、Brazeが提供するeコマースイベントの推奨イベント（recommended events）について説明する。"
---

# 推奨イベント

> 推奨イベントは、最も一般的な e コマースのユースケースに対応しています。推奨イベントを使用することで、事前に作成されたキャンバステンプレート、カスタマーライフサイクルにマッピングされたレポートダッシュボードなどをアンロックすることができる。

例えば、「cart_updated」または「update_to_cart」というカスタムイベントを用意し、ユーザーがカートで製品を追加、削除、または更新した時点をキャプチャできます。Braze は推奨イベントのイベントテンプレートを提供する予定です。イベントテンプレートには、このイベントの定義済みの名前と関連プロパティが含まれています。

{% alert important %}
推奨イベントは現在早期アクセス段階です。早期アクセスに参加したい場合は、Braze カスタマーサクセスマネージャーにお問い合わせください。<br><br>新しい[Shopifyコネクタを]({{site.baseurl}}/partners/ecommerce/shopify/multiple_stores/?tab=shopify%20connector)活用している場合、これらの推奨イベントは統合によって自動的に利用できるようになる。
{% endalert %}

## CDI の仕組み

Braze はすべての推奨イベントに特別な検証を適用します。一部の推奨イベントには、特別な後処理アクションがあります。特定の業界の推奨イベントについては、Braze は特別な処理 (キャンペーンやキャンバスの新しいアクションベースのトリガーなど) をサポートすることがあります。

推奨イベントは[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events)と同様に機能します。Currents から推奨イベントをエクスポートし、ブロックリストに登録し、レポートに使用することができます。[Braze SDK]({{site.baseurl}}/developer_guide/getting_started/sdk_overview) または[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track)を使用して、これらのイベントを追跡するために Braze にデータを送信することもできます。

### e コマースの推奨イベント

[e コマースの推奨イベント]({{site.baseurl}}/ecommerce_events/)は、推奨イベントに基づいています。e コマースの推奨イベントは、顧客のアクション (製品の閲覧、カートの更新、購入手続きの開始) を追跡します。 

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_refunded`
- `ecommerce.order_cancelled`

#### eコマースキャンバスのテンプレート

Braze キャンバスの事前作成済みテンプレートを使用して必要な戦略を実施する方法に関するアイデアについては、Braze の [e コマースユースケース]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/)を参照してください。

## よくある質問

### 推奨イベントはカスタムイベントと同じか？

いいえ。Braze は推奨イベントについて制約の強い (opinionated) データスキーマを定義します。これには、Braze で検証プロセスを経る必須のイベントプロパティとオプションのイベントプロパティが含まれます。[カスタムイベントとは]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)、アプリやWebサイトでユーザーが行った特定のアクションや更新を追跡するものである。イベント名や追跡する内容はカスタマイズできます。

### おすすめイベントの名前をカスタムできるか？

推奨イベントには、標準化されたイベント名とプロパティがあります。これらの標準化は、データ全体での一貫性を実現するうえで役立ちます。

### 購入イベントを使用して購入履歴を記録することは可能か？

e コマースの推奨イベントの導入に伴い、Braze は今後、従来の購入イベントを段階的に廃止していく予定です。現在、購入イベントを利用している場合は、非推奨プランに関する事前通知を受け取ることになる。正式な廃止日までは購入イベントを使い続けることができます。