---
nav_title: ユーザーデータ
article_title: ユーザーデータエンドポイント
search_tag: Endpoint
page_order: 9

local_redirect: #event-object-specification #purchase-object-specification
  event-object-specification: '/docs/api/objects_filters/event_object/'
  purchase-object-specification: '/docs/api/objects_filters/purchase_object/'

layout: dev_guide

#Required
description: "このランディングページには、Braze ユーザーデータエンドポイントが一覧表示されます。"
page_type: landing

guide_top_header: "ユーザーデータエンドポイント"
guide_top_text: "Braze User Data エンドポイントでは、モバイルアプリ外からのユーザーに関するデータをログに記録することで、ユーザーに関する情報を追跡できます。この API を使用して、テストやその他の目的でユーザーを削除することもできます。<br><br>すべての API エンドポイントのデータペイロード制限は 4 MB です。4 MB を超えるデータを投稿しようとすると、HTTP 413 リクエストエンティティが大きすぎるため失敗します。<br><br>このセクションの例には https://rest.iad-01.braze.com というURLが含まれていますが、別のエンドポイント URL を使用する必要がある場合があります（たとえば、Braze EU データセンターでホストされている場合や、専用の Braze をインストールしている場合）。別のエンドポイント URL を使用するかどうかは、Braze カスタマーサクセスマネージャーから通知されます。"

guide_featured_title: "ユーザーデータエンドポイント"
guide_featured_list:
  - name: "POST: Create a New User Alias"
    link: /docs/api/endpoints/user_data/post_user_alias/
    fa_icon: fas fa-user
  - name: "POST: Update a User Alias"
    link: /docs/api/endpoints/user_data/post_users_alias_update/
    fa_icon: fas fa-user-edit
  - name: "POST: Delete User Data"
    link: /docs/api/endpoints/user_data/post_user_delete/
    fa_icon: fas fa-user-minus
  - name: "POST: Identify a User"
    link: /docs/api/endpoints/user_data/post_user_identify/
    fa_icon: fas fa-user-circle
  - name: "POST: Track Users"
    link: /docs/api/endpoints/user_data/post_user_track/
    fa_icon: fas fa-database
  - name: "POST: Merge Users"
    link: /docs/api/endpoints/user_data/post_users_merge/
    fa_icon: fas fa-users

guide_menu_title: "External ID migration endpoints"
guide_menu_list:
  - name: "POST: Rename External IDs"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/
    fa_icon: fas fa-user
  - name: "POST: Remove Deprecated External IDs"
    link: /docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/
    fa_icon: fas fa-user-minus
---
