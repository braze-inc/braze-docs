---
nav_title: "メールリストとアドレス"
article_title: メールリストとアドレスのエンドポイント
search_tag: Endpoint
page_order: 1
layout: dev_guide

description: "このランディングページでは、Braze のメールリストとアドレスのエンドポイントについて説明し、一覧を掲載しています。"
page_type: landing

guide_top_header: "メールリストとアドレスのエンドポイント"
guide_top_text: "このエンドポイントセットを使用すると、ユーザーのメールサブスクリプションステータスを更新したり、Braze API を使用して Braze と他のメールシステムまたは独自のデータベースとの間で双方向同期を設定したりできます。"

guide_featured_title: ""
guide_featured_list:
  - name: "GET: ハードバウンスの一覧取得"
    link: /docs/api/endpoints/email/get_list_hard_bounces/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "GET: 配信停止メールアドレスの照会"
    link: /docs/api/endpoints/email/get_query_unsubscribed_email_addresses/
    image: /assets/img/braze_icons/mail-01.svg
  - name: "POST: メールサブスクリプションステータスの変更"
    link: /docs/api/endpoints/email/post_email_subscription_status/
    image: /assets/img/braze_icons/at-sign.svg
  - name: "POST: ハードバウンスの削除"
    link: /docs/api/endpoints/email/post_remove_hard_bounces/
    image: /assets/img/braze_icons/message-plus-square.svg
  - name: "POST: スパムの削除"
    link: /docs/api/endpoints/email/post_remove_spam/
    image: /assets/img/braze_icons/mail-04.svg
  - name: "POST: メールのブロックリスト登録"
    link: /docs/api/endpoints/email/post_blocklist/
    image: /assets/img/braze_icons/mail-04.svg
---
{% comment %}
redirect from email_sync.md
{% endcomment %}