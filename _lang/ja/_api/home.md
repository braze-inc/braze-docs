---
page_order: 0
nav_title: ホーム
article_title: Braze API ガイド
layout: api_glossary
glossary_top_header: "Braze API ガイド"
glossary_top_text: "Braze は、ユーザーの追跡、メッセージの送信、データのエクスポートなどを可能にする高性能の REST API を提供します。このページでは、利用可能な Braze API エンドポイントとその用途を示します。"
page_type: glossary
description: "このランディング ページには、利用可能な Braze API エンドポイントとその用途がリストされています。"
glossary_tag_name: Endpoint Type

glossary_filter_text: "Select endpoint type to narrow the glossary:"

glossary_mid_text: "Endpoint Search"
guide_featured_list:
  - name: API の概要
    fa_icon: fa-solid fa-info
    link: /docs/api/basics/
  - name: API 識別子の種類
    link: /docs/api/identifier_types/
    fa_icon: fa-solid fa-clipboard-list
  - name: オブジェクト＆フィルター
    link: /docs/api/objects_filters/
    fa_icon: fa-solid fa-gear
  - name: エラー＆回答
    link: /docs/api/errors/
    fa_icon: fa-solid fa-list-check
  - name: データ保持
    link: /docs/api/data_retention/
    fa_icon: fa-solid fa-laptop-code
  - name: 料金制限
    link: /docs/api/api_limits/
    fa_icon: fa-solid fa-hand

# channel to icon/fa or image mapping
glossary_tags:
  - name: キャンペーン
  - name: キャンバス
  - name: カタログ
  - name: コンテンツブロック
  - name: カスタムイベント
  - name: メールリスト
  - name: メールテンプレート
  - name: KPI
  - name: ニュースフィード
  - name: 購入
  - name: ユーザー設定センター
  - name: スケジュールメッセージ
  - name: SCIM
  - name: セグメント
  - name: メッセージの送信
  - name: SMS
  - name: サブスクリプショングループ
  - name: ユーザーデータ
  - name: ライブアクティビティ
  - name: クラウドデータ取り込み

glossaries:
  - name: <a href='/docs/api/endpoints/user_data/post_user_alias/'>/users/alias/new</a>
    description: 既存の識別されたユーザーのために新しいユーザーエイリアスを追加するか、または新しい識別されていないユーザーを作成します。
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_users_alias_update/'>/users/alias/update</a>
    description: 既存のユーザーエイリアス名を新しいユーザーエイリアス名に更新します。
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_user_delete/'>/users/delete</a>
    description: 既知のユーザー識別子を指定して、任意の顧客プロファイルを削除します。
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/export/user_data/post_users_global_control_group/'>/users/export/global_control_group</a>
    description: グローバルコントロールグループ内のすべてのユーザーをエクスポートします。
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/export/user_data/post_users_identifier/'>/users/export/ids</a>
    description: ユーザー識別子を指定して、任意の顧客プロファイルからデータをエクスポートします。
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/export/user_data/post_users_segment/'>/users/export/segment</a>
    description: セグメント内のすべてのユーザーをエクスポートします。
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/'>/users/external_ids/rename</a>
    description: ユーザーの外部 ID の名前を変更します。
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/'>/users/external_ids/remove</a>
    description: ユーザーの古い非推奨外部 ID を削除してください。
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_user_identify/'>/users/identify</a>
    description: 識別されていない（エイリアスのみの）ユーザーを識別します。
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_user_track/'>/users/track</a>
    description: カスタムイベント、購入を記録し、顧客プロファイル属性を更新します。
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/user_data/post_users_merge/'>/users/merge</a>
    description: 顧客プロファイルを別のユーザーにマージします。
    tags:
      - User Data
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/'>/campaigns/trigger/send</a>
    description: API トリガー配信により、指定したユーザーに即座に単発のメッセージを送信します。
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/'>/canvas/trigger/send</a>
    description: API トリガー配信でキャンバスメッセージを送信します。
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_messages/'>/messages/send</a>
    description: Braze API を使用して、指定したユーザーに即座に単発のメッセージを送信します。
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_create_send_ids/'>/sends/id/create</a>
    description: 送信ごとにキャンペーンを作成することなく、プログラムでメッセージを送信し、メッセージのパフォーマンスを追跡するために使用できる送信 ID を作成します。
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/send_messages/post_send_transactional_message/'>/transactional/v1/campaigns/{CAMPAIGN_ID}/send</a>
    description: 指定されたユーザーに、即座に単発のトランザクションメッセージを送信します。
    tags:
      - Send Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/'>/campaigns/trigger/schedule/create</a>
    description: Send dashboard created campaign messages via API-triggered delivery.
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/'>/campaigns/trigger/schedule/delete</a>
    description: 以前にスケジューリングした API トリガーキャンペーンメッセージを、送信前にキャンセルできます。
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/'>/campaigns/trigger/schedule/update</a>
    description: ダッシュボードに作成されたスケジュールされた API トリガーキャンペーンを更新します。
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/'>/canvas/trigger/schedule/delete</a>
    description: API トリガーで以前にスケジューリングしたキャンバスメッセージを送信前にキャンセルします。
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/'>/canvas/trigger/schedule/create</a>
    description: API トリガー配信でキャンバスメッセージをスケジュールします。
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/'>/messages/schedule/update</a>
    description: スケジュールされたメッセージを更新します。このエンドポイントは、<code>schedule</code> か <code>messages</code> パラメータのどちらか、または両方の更新を受け付けます。
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/'>/messages/schedule/delete</a>
    description: 以前に予約したメッセージを送信前にキャンセルします。
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/'>/messages/schedule/create</a>
    description: キャンペーン、キャンバス、その他のメッセージを指定時間に送信するようスケジュールします。
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/'>/canvas/trigger/schedule/update</a>
    description: ダッシュボードで作成されたスケジュールされた API トリガーキャンバスを更新します。
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/'>/messages/scheduled_broadcasts</a>
    description: 現在からリクエストで指定された <code>end_time</code> までの間にスケジュールされたキャンペーンとエントリーキャンバスに関する情報の JSON リストを返します。
    tags:
      - Schedule Messages
  - name: <a href='/docs/api/endpoints/messaging/live_activity/update/'>/messages/live_activity/update</a>
    description: iOS のライブアクティビティを更新します。
    tags:
      - Live Activity
  - name: <a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/'>/subscription/status/set</a>
    description: Braze ダッシュボード上で最大 50 ユーザーのサブスクリプション状態を一括更新します。
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/'>/v2/subscription/status/set</a>
    description: Braze ダッシュボード上で最大 50 ユーザーのサブスクリプション状態を一括更新します。
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status/'>/subscription/status/get</a>
    description: サブスクリプショングループ内のユーザーのサブスクリプション状態を取得します。
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_groups/'>/subscription/user/status</a>
    description: 特定のユーザーのサブスクリプショングループをリストアップして取得します。
    tags:
      - Subscription Groups
  - name: <a href='/docs/api/endpoints/email/post_blacklist/'>/email/blacklist</a>
    description: ユーザーのメール配信を停止し、ハードバウンスとしてマークします。
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/post_remove_hard_bounces/'>/email/bounce/remove</a>
    description: Braze のバウンスリストからメールアドレスを削除します。
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/post_remove_spam/'>/email/spam/remove</a>
    description: Braze のスパムリストからメールアドレスを削除します。
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/post_email_subscription_status/'>/email/status</a>
    description: ユーザーのメールサブスクリプション状態を設定します。
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/templates/email_templates/post_create_email_template/'>/templates/email/create</a>
    description: Braze ダッシュボードでメールテンプレートを作成します。
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/templates/email_templates/post_update_email_template/'>/templates/email/update</a>
    description: Braze ダッシュボードでメールテンプレートを更新します。
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/email/get_list_hard_bounces/'>/email/hard_bounces</a>
    description: 一定期間内にメールメッセージを「ハードバウンス」したメールアドレスのリストを取得します。
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/email/get_query_unsubscribed_email_addresses/'>/email/unsubscribes</a>
    description: <code>start_date</code> から <code>end_date</code> までの期間に配信停止したメールを返します。
    tags:
      - Email List
  - name: <a href='/docs/api/endpoints/templates/email_templates/get_see_email_template_information/'>/templates/email/info</a>
    description: メールテンプレートの情報を取得します。
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/templates/email_templates/get_list_email_templates/'>/templates/email/list</a>
    description: Braze アカウントで利用可能なメールテンプレートのリストを取得します。
    tags:
      - Email Templates
  - name: <a href='/docs/api/endpoints/export/campaigns/get_campaign_analytics/'>/campaigns/data_series</a>
    description: 一定期間にわたるキャンペーンのさまざまな統計の日次系列を取得します。
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/campaigns/get_campaign_details/'>/campaigns/details</a>
    description: 指定したキャンペーンの関連情報を取得します。
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/campaigns/get_campaigns/'>/campaigns/list</a>
    description: キャンペーンのリストをエクスポートします。各キャンペーンには、名前、キャンペーン API 識別子、API キャンペーンかどうか、キャンペーンに関連するタグが含まれます。
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/campaigns/get_send_analytics/'>/sends/data_series</a>
    description: 追跡している <code>send_id</code> の各種統計情報を毎日取得します。
    tags:
      - Campaigns
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvas_analytics/'>/canvas/data_series</a>
    description: キャンバスの時系列データをエクスポートします。
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvas_analytics_summary/'>/canvas/data_summary</a>
    description: キャンバスの時系列データのロールアップをエクスポートして、キャンバスの結果を簡潔に要約できます。
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvas_details/'>/canvas/details</a>
    description: キャンバスの名前、作成時間、現在のステータスなど、キャンバスに関するメタデータをエクスポートします。
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/canvas/get_canvases/'>/canvas/list</a>
    description: キャンバス名、キャンバス API 識別子、関連タグを含むキャンバスのリストをエクスポートします。
    tags:
      - Canvas
  - name: <a href='/docs/api/endpoints/export/segments/get_segment_analytics/'>/segments/data_series</a>
    description: セグメントの推定サイズの日次系列を経時的に取得します。
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/segments/get_segment_details/'>/segments/details</a>
    description: セグメントの関連情報を取得します。
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/segments/get_segment/'>/segments/list</a>
    description: セグメントのリストをエクスポートします。各セグメントには、セグメントの名前、セグメント API 識別子、アナリティクスのトラッキングが有効かどうかが含まれます。
    tags:
      - Segments
  - name: <a href='/docs/api/endpoints/export/sessions/get_sessions_analytics/'>/sessions/data_series</a>
    description: 指定した期間におけるアプリのセッション数を取得します。
    tags:
      - Sessions
  - name: <a href='/docs/api/endpoints/export/custom_events/get_custom_events_analytics/'>/events/data_series</a>
    description: 指定した期間にアプリ内で発生したカスタムイベントの回数を取得します。
    tags:
      - Custom Events
  - name: <a href='/docs/api/endpoints/export/custom_events/get_custom_events/'>/events/list</a>
    description: アプリに記録されたカスタムイベントのリストをエクスポートします。
    tags:
      - Custom Events
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/'>/content_blocks/create</a>
    description: メールコンテンツブロックを作成します。
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/post_update_content_block/'>/content_blocks/update</a>
    description: メールのコンテンツブロックを更新します。
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/'>/content_blocks/info</a>
    description: 既存のメールコンテンツブロックの情報を呼び出します。
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/'>/content_blocks/list</a>
    description: 既存のコンテンツブロックの情報を一覧表示します。
    tags:
      - Content Blocks
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_dau_date/'>/kpi/dau/data_series</a>
    description: 各日付の一意のアクティブユーザーの総数の日次系列を取得します。
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_mau_30_days/'>/kpi/mau/data_series</a>
    description: 30日間にわたる一意のアクティブユーザーの総数の日次系列を取得します。
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date/'>/kpi/new_users/data_series</a>
    description: 各日付の新規ユーザー総数の日次系列を取得します。
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/export/kpi/get_kpi_uninstalls_date/'>/kpi/uninstalls/data_series</a>
    description: 各日付のアンインストール総数の日次系列を取得します。
    tags:
      - KPI
  - name: <a href='/docs/api/endpoints/export/news_feed/get_news_feed_card_analytics/'>/feed/data_series</a>
    description: 経時的なカードのエンゲージメント統計情報の日次系列を取得します。
    tags:
      - News Feed
  - name: <a href='/docs/api/endpoints/export/news_feed/get_news_feed_card_details/'>/feed/details</a>
    description: カードの関連情報を取得します。
    tags:
      - News Feed
  - name: <a href='/docs/api/endpoints/export/news_feed/get_news_feed_cards/'>/feed/list</a>
    description: ニュースフィードカードのリストをエクスポートします。各カードには名前とカード API 識別子が含まれます。
    tags:
      - News Feed
  - name: <a href='/docs/api/endpoints/sms/post_remove_invalid_numbers/'>/sms/invalid_phone_numbers/remove</a>
    description: Braze の無効リストから「無効」な電話番号を削除します。これは、無効とマークされた電話番号を再度検証するために使用できます。
    tags:
      - SMS
  - name: <a href='/docs/api/endpoints/sms/get_query_invalid_numbers/'>/sms/invalid_phone_numbers</a>
    description: 一定期間内に「無効」と判断された電話番号のリストを引き出します。
    tags:
      - SMS
  - name: <a href='/docs/api/endpoints/export/purchases/get_list_product_id/'>/purchases/product_list</a>
    description: 製品 ID のページ分割されたリストを返します。
    tags:
      - Purchases
  - name: <a href='/docs/api/endpoints/export/purchases/get_number_of_purchases/'>/purchases/quantity_series</a>
    description: 特定の時間範囲におけるアプリでの購入数の合計を返します。
    tags:
      - Purchases
  - name: <a href='/docs/api/endpoints/export/purchases/get_revenue_series/'>/purchases/revenue_series</a>
    description: 特定の時間範囲にわたってアプリで使用された合計金額を返します。
    tags:
      - Purchases    
  - name: <a href='/docs/api/endpoints/preference_center/get_create_url_preference_center'>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}</a>
    description: ユーザー設定センターの URL を作成します。
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/get_list_preference_center/'>/preference_center/v1/list</a>
    description: 利用可能なユーザー設定センターをリストアップしてください。
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/get_view_details_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>
    description: 作成日や更新日などユーザー設定センターの詳細を表示します。
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/post_create_preference_center'>/preference_center/v1</a>
    description: ユーザー設定センターを作成し、ユーザーがメールキャンペーンの通知設定を管理できるようにします。
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/preference_center/put_update_preference_center'>/preference_center/v1/{preferenceCenterExternalId}</a>
    description: ユーザー設定センターを更新します。
    tags:
      - Preference Center
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk'>/catalogs/{catalog_name}/items</a>
    description: カタログ内の複数のアイテムを削除します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: カタログ項目とその詳細を一覧表示します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/'>/catalogs/{catalog_name}/items</a>
    description: カタログの複数の項目を編集します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/'>/catalogs/{catalog_name}/items</a>
    description: カタログに複数のアイテムを作成します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/'>/catalogs/{catalog_name}</a>
    description: カタログを削除します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/'>/catalogs</a>
    description: カタログを作成します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/'>/catalogs</a>
    description: ワークスペース内のカタログを一覧表示します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: カタログに項目を作成します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: カタログの項目を編集します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/'>/catalogs/{catalog_name}/items</a>
    description: 複数のカタログ項目とその内容を返します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: カタログの項目を削除します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>
    description: カタログの項目を更新します。
    tags:
      - Catalogs
  - name: <a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/'>/catalogs/{catalog_name}/items/</a>
    description: カタログの複数の項目を更新します。
    tags:
      - Catalogs
  - name: <a href='/docs/post_create_user_account/'>/scim/v2/Users</a>
    description: メールアドレス、姓名、権限（会社、ワークスペース、およびチームレベルでの権限設定）を指定して、新しいダッシュボードユーザーアカウントを作成します。
    tags:
      - SCIM
  - name: <a href='/docs/get_see_user_account_information/'>/scim/v2/Users/{id}</a>
    description: メールアドレスを指定して、既存のダッシュボードユーザーアカウントを検索します。
    tags:
      - SCIM
  - name: <a href='/docs/post_update_existing_user_account/'>/scim/v2/Users/{id}</a>
    description: メール、姓名、権限（会社、ワークスペース、およびチームレベルでの権限設定）を指定して、既存のダッシュボードユーザーアカウントを更新します。
    tags:
      - SCIM
  - name: <a href='/docs/delete_existing_dashboard_user/'>/scim/v2/Users/{id}</a>
    description: 既存のダッシュボードユーザーを完全に削除します。
    tags:
      - SCIM
  - name: <a href='/docs/get_search_existing_dashboard_user_email/'>/scim/v2/Users?filter={userName@example.com}</a>
    description: メールアドレスを指定して、既存のダッシュボードユーザーアカウントを検索します。
    tags:
      - SCIM
  - name: <a href='/docs/api/endpoints/cdi/get_integration_list/'>/cdi/integrations</a>
    description: 既存の統合のリストを返します。
    tags:
      - Cloud Data Ingestion
  - name: <a href='/docs/api/endpoints/cdi/post_job_sync/'>/cdi/integrations/{integration_id}/sync</a>
    description: 指定した統合の同期をトリガーします。
    tags:
      - Cloud Data Ingestion
  - name: <a href='/docs/api/endpoints/cdi/get_job_sync_status/'>/cdi/integrations/{integration_id}/job_sync_status</a>
    description: 同期ステータスのリストを返します。
    tags:
      - Cloud Data Ingestion
---
