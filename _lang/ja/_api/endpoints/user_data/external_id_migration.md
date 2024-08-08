---
nav_title: 外部IDマイグレーション
article_title: "外部IDマイグレーション"
search_tag: Endpoint
page_order: 7
layout: dev_guide

description: "このランディングページでは、Brazeの外部ID移行機能について説明し、一覧表示します。"
page_type: landing

guide_top_header: "外部IDマイグレーション"
guide_top_text: "外部 ID マイグレーション API を使用すると、既存の外部 ID の名前を変更したり (新しいプライマリ ID を作成し、既存の ID を非推奨にする)、非推奨の ID をマイグレーション後に削除したりできます。 <br><br> 私たちは、以前の外部 ID ネーミング スキーマを使用する古いバージョンのアプリが壊れないようなマイグレーション期間をサポートするために、複数の外部 ID を使用できるようにこのソリューションを設計しました。古い命名スキーマが使われなくなったら、非推奨の外部IDを削除することを強くお勧めします。"

guide_featured_title: "外部ID移行エンドポイント"
guide_featured_list:
  - name: "POST: Rename External IDs"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
    fa_icon: fas fa-user
  - name: "POST: Remove Deprecated External IDs"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
    fa_icon: fas fa-user-minus
---
