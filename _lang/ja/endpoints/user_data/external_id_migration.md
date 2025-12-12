---
nav_title: 外部IDの移行
article_title: "外部ID の移行"
search_tag: Endpoint
page_order: 7
layout: dev_guide

description: "このランディングページでは、Brazeの外部ID マイグレーション機能について説明し、一覧を示します。"
page_type: landing

guide_top_header: "外部ID の移行"
guide_top_text: "外部 ID 移行 API を使用すると、既存の外部 ID の名前を変更したり (新しいプライマリ ID を作成し、既存の ID を廃止)、移行後に廃止された ID を削除したりできます。<br><br> このソリューションは、以前の外部ID 命名スキーマを使用するワイルド内にあるアプリの古いバージョンが壊れないように、マイグレーション期間をサポートするために複数の外部ID を許可するように設計されています。古い命名スキーマが使用されなくなった場合は、非推奨の外部 ID を削除することを強く推奨します。"

guide_featured_title: "外部ID 移行エンドポイント"
guide_featured_list:
  - name: "POST:外部ID の名前変更"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
    image: /assets/img/braze_icons/users-01.svg
  - name: "POST:非推奨の外部ID の削除"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
    image: /assets/img/braze_icons/user-minus-01.svg
---
