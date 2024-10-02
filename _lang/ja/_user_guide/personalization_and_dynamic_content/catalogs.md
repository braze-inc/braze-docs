---
nav_title: カタログ
article_title: カタログ
page_order: 6
layout: dev_guide

guide_top_header: "カタログ"
guide_top_text: "カタログは、Liquidを通してカスタム属性やカスタムイベントプロパティにアクセスするのと同じように、インポートしたCSVファイルやAPIエンドポイントからデータにアクセスし、メッセージを豊かにする。"

description: "このランディングページにはカタログが掲載されている。カタログとフィルターセットを使用して、Brazeキャンペーンで非ユーザーデータを活用し、パーソナライズされたメッセージを送信する。"

guide_featured_title: "セクションの記事"
guide_featured_list:
- name: カタログを作成する
  link: /docs/user_guide/personalization_and_dynamic_content/catalogs/catalog/
  image: /assets/img/braze_icons/users-01.svg
- name: カタログを使う
  link: /docs/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/
  image: /assets/img/braze_icons/users-01.svg
- name: 在庫切れのお知らせ
  link: /docs/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications/
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: 値下げ通知
  link: /docs/price_drop_notifications/
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: セレクション
  link: /docs/user_guide/personalization_and_dynamic_content/catalogs/selections/
  image: /assets/img/braze_icons/list.svg
- name: カタログ API エンドポイント
  link: /docs/api/endpoints/catalogs/
  image: /assets/img/braze_icons/server-01.svg
---
<br><br>

## カタログ使用例

カタログにはどんな種類のデータでも持ち込むことができる。通常、データは商品、割引、プロモーション、イベントなど、提供物に関するメタデータである。関連性の高いメッセージングでユーザーをターゲットにするために、このデータをどのように使用できるかのいくつかの例については、以下の使用例を参照のこと。

### 小売とeコマース

- **シーズンプロモーション：**季節の商品コレクションをインポートし、現在のトレンドを反映したメッセージをパーソナライズする。
- **ローカライズされたメッセージ：**物理的な場所の住所、営業時間、サービスをインポートし、ユーザーの場所に基づいて通知をパーソナライズする。
- **在庫切れ通知：**在庫数を含む商品情報をインポートし、[在庫切れ通知や]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications/)Brazeカスタムイベントを使用して、キャンペーンやCanvasをトリガーし、ユーザーに商品が入荷したことを通知する。
- **値下げ通知：**商品価格を含む商品情報をインポートし、[値下がり通知と]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/price_drop_notifications/)Brazeカスタムイベントを使用して、商品の値下がり通知をユーザーに送信するCanvasをトリガーする。

### エンターテイメント

- **サブスクリプションプラン：**サブスクリプションプランをインポートし、ユーザーの利用パターンや最もよく消費するコンテンツの種類に基づいてアドオンを促進する。
- **今後のイベント**近日開催予定のイベントリストとその場所、視聴者の年齢をインポートし、エリア内にいるターゲット年齢のユーザーにパーソナライズされた通知を送信する。
- **メディアの好みだ：**映画や番組の情報をインポートし、ユーザーのお気に入りタイトルやよく見るジャンルに基づいてコンテンツを推薦する。

### 旅行とホスピタリティ

- **目的地だ：**旅行先と、その旅行先で最も人気のあるアトラクション、レストラン、アクティビティをインポートし、過去の旅行に基づいて、ユーザーにパーソナライズされたレコメンデーションを提供する。
- **宿泊施設：**ホテルとそのアメニティ、ルームタイプ、価格をインポートし、選択した嗜好に基づいてユーザーにプロモーションを送信する。
- **旅の方法**：航空券、鉄道、レンタカーなど、旅行形態のお得なキャンペーン情報をインポートし、最近の検索履歴に基づいてユーザーに送信する。
- **食事の好み：**食事の提供に関する情報をインポートし、直近に閲覧した食品カテゴリーに基づいて、特定の食事の好みを持つユーザーにパーソナライズされたメッセージを送信するために[選択項目を]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/)使用する。

## カタログとリキッドの連携

カタログはデータ保存機能である。これらのデータには、パーソナライゼーションのためにメッセージで参照できる大規模なデータセットが含まれている。実際にデータを参照するには、テンプレート言語として[Liquidを]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)使う。言い換えれば、カタログはデータが保管されているストレージであり、リキッドはストレージから関連するデータを引き出す言語である。

カタログ情報をプルするためにLiquidを使用する方法の例については、[カタログを作成するでの]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#additional-use-cases/)追加の使用例を参照のこと。