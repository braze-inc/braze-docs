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
  link: /docs/user_guide/data/activation/catalogs/create/
  image: /assets/img/braze_icons/users-01.svg
- name: カタログを使う
  link: /docs/user_guide/data/activation/catalogs/use/
  image: /assets/img/braze_icons/users-01.svg
- name: 在庫切れのお知らせ
  link: /docs/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: 値下げ通知
  link: /docs/price_drop_notifications/
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: セレクション
  link: /docs/user_guide/data/activation/catalogs/selections/
  image: /assets/img/braze_icons/list.svg

guide_menu_title: "Other articles"
guide_menu_list:
- name: カタログ API エンドポイント
  link: /docs/api/endpoints/catalogs/
  image: /assets/img/braze_icons/server-01.svg
- name: 製品ドラッグ＆ドロップブロック
  link: /docs/dnd_product_blocks/
  image: /assets/img/braze_icons/columns-01.svg
---
<br><br>

## カタログ使用例

カタログには、任意のタイプのデータを取り込むことができます。通常、データは製品、割引、プロモーション、イベントなど、提供するアイテムに関するメタデータです。関連性の高いメッセージングでユーザーをターゲットにするために、このデータをどのように使用できるかのいくつかの例については、以下の使用例を参照のこと。

### 小売業と e コマース

- **季節のプロモーション:**季節の商品コレクションをインポートし、現在のトレンドを反映したメッセージをパーソナライズする。
- **メッセージのローカライズ:**お客様の物理的な住所、営業時間、およびサービスをインポートし、ユーザーの場所に基づいて通知をパーソナライズします。
- **再入荷通知:**在庫数量を含む製品情報をインポートし、[再入荷通知]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/)と Braze のカスタムイベントを使用して、製品が現在、在庫しているという通知をユーザーに送信するキャンペーンまたはキャンバスをトリガーします。
- **値下げ通知:**商品価格を含む商品情報をインポートし、[値下がり通知と]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/)Brazeカスタムイベントを使用して、商品の値下がり通知をユーザーに送信するCanvasをトリガーする。

### エンターテイメント

- **サブスクリプションプラン：**購読プランをインポートし、ユーザーの利用パターンや最もよく消費するコンテンツの種類に基づいてアドオンを宣伝します。
- **今後のイベント:**近日開催予定のイベントのリストとその場所、オーディエンスの年齢をインポートし、その地域にいるターゲット年齢のユーザーにパーソナライズされた通知を送信します。
- **メディアの嗜好:**映画や番組の情報をインポートし、ユーザーのお気に入りタイトルやよく見るジャンルに基づいてコンテンツを推薦する。

### 旅行とホスピタリティ

- **目的地:**旅行先と、その旅行先で最も人気のあるアトラクション、レストラン、アクティビティをインポートし、過去の旅行に基づいて、ユーザーにパーソナライズされたレコメンデーションを提供する。
- **宿泊施設:**ホテルの特徴とそのアメニティ、客室のタイプ、料金をインポートし、ユーザーの選択した好みに基づいてプロモーションをユーザーに送信します。
- **旅行手段**: 航空券、鉄道、レンタカーなど、旅行形態のお得なキャンペーン情報をインポートし、最近の検索履歴に基づいてユーザーに送信する。
- **食事の嗜好:**食事の提供に関する情報をインポートし、[セレクション]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/)を使用して、最近表示した食品カテゴリに基づき、特定の食事を嗜好するユーザーにパーソナライズされたメッセージを送信します。

## カタログと Liquid の連携の仕組み

カタログは、データ保存機能の 1 つです。カタログには大規模なデータセットが含まれており、パーソナライゼーションの目的でデータをメッセージ内で参照できます。実際にデータを参照するには、テンプレート言語として [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) を使用します。言い換えれば、カタログはデータが保管されているストレージであり、Liquidはストレージから関連データを引き出すための言語である。

Liquid を使用してカタログ情報を取得する方法の例については、[「カタログの作成」]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#additional-use-cases/)の追加のユースケースを参照してください。

#### データ保存の制限

カタログのデータストレージは、カタログアイテムのサイズに基づいて制限されており、アップロードされたCSVファイルのサイズとは異なる場合がある。

カタログの無料バージョンの場合、許可されるストレージ容量は最大100 MBです。保存ストレージが100MBを超えない限り、項目は無制限に持つことができます。

カタログ Proの場合、ストレージサイズのオプションは以下の通りです。5GB、10GB、15GB、または50GB。なお、無料版のストレージ (100 MB) はこれらの各プランに含まれています。
