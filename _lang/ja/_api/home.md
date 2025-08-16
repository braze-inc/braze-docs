---
page_order: 0
nav_title: ホーム
article_title: Braze API ガイド
layout: api_glossary
glossary_top_header: "Braze API Guide"
glossary_top_text: "Braze provides a high-performance REST API to allow you to track users, send messages, export data, and more. This page lists available Braze API endpoints and their uses."
page_type: glossary
description: "このランディングページには、利用可能なBraze APIエンドポイントとその用途が掲載されている。"
glossary_tag_name: Endpoint Type

glossary_filter_text: "Select endpoint type to narrow the glossary:"

glossary_mid_text: "Endpoint Search"
guide_featured_list:
  - name: APIの概要
    image: /assets/img/braze_icons/annotation-info.svg
    link: /docs/api/basics/
  - name: API識別子の種類
    link: /docs/api/identifier_types/
    image: /assets/img/braze_icons/clipboard-check.svg
  - name: オブジェクトとフィルター
    link: /docs/api/objects_filters/
    image: /assets/img/braze_icons/settings-01.svg
  - name: エラーとレスポンス
    link: /docs/api/errors/
    image: /assets/img/braze_icons/list.svg
  - name: データ保持
    link: /docs/api/data_retention/
    image: /assets/img/braze_icons/laptop-02.svg
  - name: レート制限
    link: /docs/api/api_limits/
    image: /assets/img/braze_icons/hand.svg

# channel to icon/fa or image mapping
glossary_tags:
  - name: キャンペーン
  - name: キャンバス
  - name: カタログ
  - name: コンテンツブロック
  - name: カスタムイベント
  - name: Eメールリスト
  - name: メールテンプレート
  - name: KPI
  - name: 購入
  - name: 環境設定センター
  - name: メッセージをスケジュール
  - name: SCIM
  - name: SDK認証
  - name: セグメント
  - name: メッセージを送る
  - name: SMS
  - name: サブスクリプショングループ
  - name: ユーザーデータ
  - name: ライブアクティビティ
  - name: クラウドデータ取り込み

glossaries:
  - name: "<a href='/docs/api/endpoints/user_data/post_user_alias/'>/users/alias/new</a>"
    description: 識別された既存のユーザーのために新しいユーザーエイリアスを追加するか、識別されていないユーザーを新規作成します。
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_users_alias_update/'>/users/alias/update</a>"
    description: 既存のユーザーエイリアス名を新しいユーザーエイリアス名に更新する。
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_user_delete/'>/users/delete</a>"
    description: 既知のユーザー識別子を指定して、任意のユーザープロファイルを削除する。
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/export/user_data/post_users_global_control_group/'>/users/export/global_control_group</a>"
    description: グローバルコントロールグループ内のすべてのユーザーをエクスポートする。
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/export/user_data/post_users_identifier/'>/users/export/ids</a>"
    description: ユーザー識別子を指定して、任意のユーザープロファイルからデータをエクスポートする。
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/export/user_data/post_users_segment/'>/users/export/segment</a>"
    description: セグメント内のすべてのユーザーをエクスポートする。
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_rename/'>/users/external_ids/rename</a>"
    description: ユーザーの外部IDの名前を変更する。
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/external_id_migration/post_external_ids_remove/'>/users/external_ids/remove</a>"
    description: ユーザーの古い非推奨外部 ID を削除します。
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_user_identify/'>/users/identify</a>"
    description: 識別されていない（エイリアスのみの）ユーザーを識別する。
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_user_track/'>/users/track</a>"
    description: カスタムイベント、購入、ユーザープロファイル属性の更新を記録します。
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/user_data/post_users_merge/'>/users/merge</a>"
    description: ユーザープロファイルを別のユーザーにマージする。
    tags:
      - User Data
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/'>/campaigns/trigger/send</a>"
    description: API トリガー配信を介して、指定したユーザーに即時の1回限りのメッセージを送信します。 - メッセージを送信
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_triggered_canvases/'>/canvas/trigger/send</a>"
    description: APIトリガー配信でCanvasメッセージを送る。- メッセージを送信する
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_messages/'>/messages/send</a>"
    description: Braze API を介して、指定したユーザーに即座に単発のメッセージを送信します。
    tags:
      - Send Messages
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_create_send_ids/'>/sends/id/create</a>"
    description: 送信ごとにキャンペーンを作成することなく、プログラムでメッセージを送信し、メッセージのパフォーマンスを追跡するために使用できる送信IDを作成する。
    tags:
      - Send Messages
  - name: "<a href='/docs/api/endpoints/messaging/send_messages/post_send_transactional_message/'>/transactional/v1/campaigns/{CAMPAIGN_ID}/send</a>"
    description: 指定されたユーザーに、即時、単発のトランザクションメッセージを送信します。
    tags:
      - Send Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/'>/campaigns/trigger/schedule/create</a>"
    description: ダッシュボードで作成したキャンペーンメッセージをAPIトリガー配信で送信する。
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_messages/'>/campaigns/trigger/schedule/delete</a>"
    description: 以前にスケジュールした API でトリガーされるキャンペーンメッセージを、送信前にキャンセルします。
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_campaigns/'>/campaigns/trigger/schedule/update</a>"
    description: ダッシュボードに作成されたスケジュールされたAPIトリガーキャンペーンを更新する。
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_triggered_canvases/'>/canvas/trigger/schedule/delete</a>"
    description: 以前にスケジュールした、API でトリガーされるキャンバスメッセージを、送信前にキャンセルします。
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/'>/canvas/trigger/schedule/create</a>"
    description: APIトリガー配信でCanvasメッセージをスケジュールする。
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_messages/'>/messages/schedule/update</a>"
    description: スケジュールされたメッセージを更新する。このエンドポイントは <code>schedule</code> または <code>messages</code> パラメータ、またはその両方です。
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_delete_scheduled_messages/'>/messages/schedule/delete</a>"
    description: 以前にスケジュールしたメッセージを、送信前にキャンセルします。
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_schedule_messages/'>/messages/schedule/create</a>"
    description: キャンペーン、キャンバス、その他のメッセージを指定時間に送信するようスケジュールする。
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/'>/canvas/trigger/schedule/update</a>"
    description: ダッシュボードで作成された、スケジュールされたAPIトリガーキャンバスを更新する。
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/schedule_messages/get_messages_scheduled/'>/messages/scheduled_broadcasts</a>"
    description: 現在から指定された期間内に予定されているキャンペーンとエントリーキャンバスに関する情報のJSONリストを返す。 <code>end_time</code> リクエストで指定されました。
    tags:
      - Schedule Messages
  - name: "<a href='/docs/api/endpoints/messaging/live_activity/update/'>/messages/live_activity/update</a>"
    description: iOSのライブアクティビティを更新する。
    tags:
      - Live Activity
  - name: "<a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status/'>/subscription/status/set</a>"
    description: Brazeダッシュボード上で最大50ユーザーのサブスクリプション状態を一括更新。
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/'>/v2/subscription/status/set</a>"
    description: Brazeダッシュボード上で最大50ユーザーのサブスクリプション状態を一括更新。
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_group_status/'>/subscription/status/get</a>"
    description: サブスクリプショングループ内のユーザーのサブスクリプションステートを取得する。
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/subscription_groups/get_list_user_subscription_groups/'>/subscription/user/status</a>"
    description: 特定のユーザーの購読グループをリストアップし、取得する。
    tags:
      - Subscription Groups
  - name: "<a href='/docs/api/endpoints/email/post_blacklist/'>/email/blacklist</a>"
    description: ユーザーのメール配信を停止し、ハードバウンスとしてマークします。
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/post_remove_hard_bounces/'>/email/bounce/remove</a>"
    description: Braze のバウンスリストからメールアドレスを削除します。
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/post_remove_spam/'>/email/spam/remove</a>"
    description: Brazeのスパムリストからメールアドレスを削除する。
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/post_email_subscription_status/'>/email/status</a>"
    description: ユーザーのメールサブスクリプションの状態を設定します。
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/templates/email_templates/post_create_email_template/'>/templates/email/create</a>"
    description: BrazeダッシュボードでEメールテンプレートを作成する。
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/templates/email_templates/post_update_email_template/'>/templates/email/update</a>"
    description: BrazeダッシュボードでEメールテンプレートを更新する。
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/email/get_list_hard_bounces/'>/email/hard_bounces</a>"
    description: 一定期間内にメールメッセージを「ハードバウンス」したメールアドレスのリストを取得します。
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/email/get_query_unsubscribed_email_addresses/'>/email/unsubscribes</a>"
    description: 以下の期間中に購読を解除したメールを返す。 <code>start_date</code> への <code>end_date</code>.
    tags:
      - Email List
  - name: "<a href='/docs/api/endpoints/templates/email_templates/get_see_email_template_information/'>/templates/email/info</a>"
    description: Eメールテンプレートの情報を入手する。
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/templates/email_templates/get_list_email_templates/'>/templates/email/list</a>"
    description: Brazeアカウントで利用可能なEメールテンプレートのリストを取得する。
    tags:
      - Email Templates
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_campaign_analytics/'>/campaigns/data_series</a>"
    description: キャンペーンに関する様々な統計情報を日次で取得する。
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_campaign_details/'>/campaigns/details</a>"
    description: 指定したキャンペーンの関連情報を取得する。
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_campaigns/'>/campaigns/list</a>"
    description: キャンペーンのリストをエクスポートする。各キャンペーンには、名前、キャンペーンAPI識別子、APIキャンペーンかどうか、キャンペーンに関連するタグが含まれる。
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/campaigns/get_send_analytics/'>/sends/data_series</a>"
    description: 追跡対象のさまざまな統計の日次情報を取得します <code>send_id</code>.
    tags:
      - Campaigns
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvas_analytics/'>/canvas/data_series</a>"
    description: キャンバスの時系列データをエクスポートする。
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvas_analytics_summary/'>/canvas/data_summary</a>"
    description: キャンバスの時系列データのロールアップをエクスポートし、キャンバスの結果の簡潔な要約を提供する。
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvas_details/'>/canvas/details</a>"
    description: 名前、作成時間、現在のステータスなど、キャンバスに関するメタデータをエクスポートします。
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/canvas/get_canvases/'>/canvas/list</a>"
    description: 名前、キャンバスの API 識別子、関連タグを含むキャンバスのリストをエクスポートします。
    tags:
      - Canvas
  - name: "<a href='/docs/api/endpoints/export/segments/get_segment_analytics/'>/segments/data_series</a>"
    description: 時間の経過に伴うセグメントの推定サイズの日次情報を取得します。
    tags:
      - Segments
  - name: "<a href='/docs/api/endpoints/export/segments/get_segment_details/'>/segments/details</a>"
    description: セグメントの関連情報を取得する。
    tags:
      - Segments
  - name: "<a href='/docs/api/endpoints/export/segments/get_segment/'>/segments/list</a>"
    description: セグメントのリストをエクスポートする。各セグメントには、名前、セグメントAPI識別子、アナリティクスのトラッキングが有効かどうかが含まれる。
    tags:
      - Segments
  - name: "<a href='/docs/api/endpoints/export/sessions/get_sessions_analytics/'>/sessions/data_series</a>"
    description: 指定した期間におけるアプリの一連のセッション数を取得します。
    tags:
      - Sessions
  - name: "<a href='/docs/api/endpoints/export/custom_attributes/get_custom_attributes/'>/custom_attributes</a>"
    description: 名前、説明、データタイプ、配列長（該当する場合）、ステータス、関連タグを含むカスタム属性のリストをエクスポートする。
    tags:
      - Custom Attributes
  - name: "<a href='/docs/api/endpoints/export/custom_events/get_custom_events_analytics/'>/events/data_series</a>"
    description: 指定された期間にわたり、アプリ内でカスタムイベントが発生した回数を取得します。
    tags:
      - Custom Events
  - name: "<a href='/docs/api/endpoints/export/custom_events/get_custom_events_data/'>/events</a>"
    description: 名前、説明、ステータス、関連タグ、分析レポートを含むカスタムイベントのリストをエクスポートします。
    tags:
      - Custom Events
  - name: "<a href='/docs/api/endpoints/export/custom_events/get_custom_events/'>/events/list</a>"
    description: アプリに記録されたカスタムイベントの名前のリストをエクスポートする。
    tags:
      - Custom Events
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/'>/content_blocks/create</a>"
    description: Eメールのコンテンツブロックを作成する。
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/post_update_content_block/'>/content_blocks/update</a>"
    description: Eメールのコンテンツブロックを更新する。
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/'>/content_blocks/info</a>"
    description: 既存のEメール・コンテンツ・ブロックの情報を呼び出す。
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/'>/content_blocks/list</a>"
    description: 既存のコンテンツブロックの情報をリストアップする。
    tags:
      - Content Blocks
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_dau_date/'>/kpi/dau/data_series</a>"
    description: 各日付のアクティブユーザーの総数を日次で取得します。
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_mau_30_days/'>/kpi/mau/data_series</a>"
    description: 30日間にわたり固有のアクティブユーザーの総数を日次で取得します。
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_daily_new_users_date/'>/kpi/new_users/data_series</a>"
    description: 各日付の新規ユーザーの総数を日次で取得します。
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/export/kpi/get_kpi_uninstalls_date/'>/kpi/uninstalls/data_series</a>"
    description: 各日付のアンインストールの総数を日次で取得します。
    tags:
      - KPI
  - name: "<a href='/docs/api/endpoints/sms/post_remove_invalid_numbers/'>/sms/invalid_phone_numbers/remove</a>"
    description: Brazeの無効リストから「無効」な電話番号を削除する。これを使用して、電話番号が無効とマークされた後、それらの電話番号を再検証できます。
    tags:
      - SMS
  - name: "<a href='/docs/api/endpoints/sms/get_query_invalid_numbers/'>/sms/invalid_phone_numbers</a>"
    description: 一定期間内に「無効」と判断された電話番号のリストを引き出す。
    tags:
      - SMS
  - name: "<a href='/docs/api/endpoints/export/purchases/get_list_product_id/'>/purchases/product_list</a>"
    description: 製品 ID のページ分割されたリストを返す。
    tags:
      - Purchases
  - name: "<a href='/docs/api/endpoints/export/purchases/get_number_of_purchases/'>/purchases/quantity_series</a>"
    description: 時間範囲内のアプリでの購入総数を返す。
    tags:
      - Purchases
  - name: "<a href='/docs/api/endpoints/export/purchases/get_revenue_series/'>/purchases/revenue_series</a>"
    description: 特定の期間内のアプリ内支出額の合計を返します。
    tags:
      - Purchases    
  - name: "<a href='/docs/api/endpoints/preference_center/get_create_url_preference_center'>/preference_center/v1/{preferenceCenterExternalId}/url/{userId}。</a>"
    description: ユーザー設定センターの URL を作成します。
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/get_list_preference_center/'>/preference_center/v1/list</a>"
    description: 利用可能なユーザー設定センターをリストアップします。
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/get_view_details_preference_center'>/preference_center/v1/{preferenceCenterExternalId}.</a>"
    description: ユーザー設定センターの詳細 (作成日時や更新日時など) を表示します。
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/post_create_preference_center'>/preference_center/v1</a>"
    description: ユーザー設定センターを作成し、ユーザーがメールキャンペーンの通知設定を管理できるようにします。
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/preference_center/put_update_preference_center'>/preference_center/v1/{preferenceCenterExternalId}.</a>"
    description: ユーザー設定センターを更新します。
    tags:
      - Preference Center
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk'>/catalogs/{catalog_name}/items</a>"
    description: カタログ内の複数の項目を削除します。
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_item_details/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: カタログ項目とその詳細をリストアップする。
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk/'>/catalogs/{catalog_name}/items</a>"
    description: カタログ内の複数の項目を編集します。
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk/'>/catalogs/{catalog_name}/items</a>"
    description: カタログ内に複数の項目を作成します。
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/delete_catalog/'>/catalogs/{catalog_name}</a>"
    description: カタログを削除する。
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog/'>/catalogs</a>"
    description: カタログを作成する。
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_management/synchronous/get_list_catalogs/'>/catalogs</a>"
    description: ワークスペース内のカタログを一覧表示する。
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: カタログに項目を作成する。
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: カタログの項目を編集する。
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/get_catalog_items_details_bulk/'>/catalogs/{catalog_name}/items</a>"
    description: 複数のカタログ項目とその内容を返す。
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/delete_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: カタログの項目を削除する。
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/'>/catalogs/{catalog_name}/items/{item_id}</a>"
    description: カタログの項目を置換します。
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/'>/catalogs/{catalog_name}/items/</a>"
    description: カタログの複数の項目を置換します。
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields/'>/catalogs/{catalog_name}/fields/</a>"
    description: カタログに複数のフィールドを作成する。
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field/'>/catalogs/{catalog_name}/fields/{field_name}とする。</a>"
    description: カタログからフィールドを削除する。
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections/'>/catalogs/{catalog_name}/selections</a>"
    description: カタログにセレクションを作成する。
    tags:
      - Catalogs
  - name: "<a href='/docs/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection/'>/catalogs/{catalog_name}/selections/{selection_name}</a>"
    description: カタログセレクションを削除します。
    tags:
      - Catalogs
  - name: "<a href='/docs/post_create_user_account/'>/scim/v2/Users</a>"
    description: メール、姓名、権限 (会社、ワークスペース、チームレベルでの権限設定) を指定して、新しいダッシュボードのユーザーアカウントを作成します。
    tags:
      - SCIM
  - name: "<a href='/docs/get_see_user_account_information/'>/scim/v2/Users/{id}</a>"
    description: リソース ID を指定して、既存のダッシュボードユーザーアカウントを検索する。
    tags:
      - SCIM
  - name: "<a href='/docs/post_update_existing_user_account/'>/scim/v2/Users/{id}</a>"
    description: メール、姓名、権限 (会社、ワークスペース、チームレベルでの権限設定) を指定して、既存ダッシュボードのユーザーアカウントを更新します。
    tags:
      - SCIM
  - name: "<a href='/docs/delete_existing_dashboard_user/'>/scim/v2/Users/{id}</a>"
    description: 既存のダッシュボードユーザーを完全に削除する。
    tags:
      - SCIM
  - name: "<a href='/docs/get_search_existing_dashboard_user_email/'>/scim/v2/Users?filter={userName@example.com}</a>"
    description: Eメールを指定して既存のダッシュボード・ユーザー・アカウントを検索する。
    tags:
      - SCIM
  - name: "<a href='/docs/api/endpoints/cdi/get_integration_list/'>/cdi/integrations</a>"
    description: 既存の統合のリストを返す。
    tags:
      - Cloud Data Ingestion
  - name: "<a href='/docs/api/endpoints/cdi/post_job_sync/'>/cdi/integrations/{integration_id}/sync</a>"
    description: 指定した統合の同期をトリガーする。
    tags:
      - Cloud Data Ingestion
  - name: "<a href='/docs/api/endpoints/cdi/get_job_sync_status/'>/cdi/integrations/{integration_id}/job_sync_status</a>"
    description: 同期ステータスのリストを返す。
    tags:
      - Cloud Data Ingestion
  - name: "<a href='/docs/api/endpoints/sdk_authentication/post_create_sdk_authentication_key/'>/app_group/sdk_authentication/create</a>"
    description: アプリ用に新しい SDK 認証キーを作成する。
    tags:
      - SDK Authentication
  - name: "<a href='/docs/api/endpoints/sdk_authentication/get_sdk_authentication_keys/'>/app_group/sdk_authentication/keys</a>"
    description: アプリの SDK 認証キーをリストアップする。
    tags:
      - SDK Authentication
  - name: "<a href='/docs/api/endpoints/sdk_authentication/put_primary_sdk_authentication_key/'>/app_group/sdk_authentication/primary</a>"
    description: SDK 認証キーをアプリのプライマリキーとして設定します。
    tags:
      - SDK Authentication
  - name: "<a href='/docs/api/endpoints/sdk_authentication/delete_sdk_authentication_key/'>/app_group/sdk_authentication/delete</a>"
    description: アプリの SDK 認証キーを削除する。
    tags:
      - SDK Authentication  
---