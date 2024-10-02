---
nav_title: 2月
page_order: 11
noindex: true
page_type: update
description: "この記事には2018年2月のリリースノートが含まれている。"
---
# 2018年2月

## iOSプッシュバッジ数

Brazeのプッシュコンポーザーで[バッジ数を更新][89]できるようになった。
各プッシュ・メッセージに対して、その通知がトリガーするバッジ・カウントを指定できる。

## メールアドレスを使用してAPI経由でユーザーをエクスポートする

メールアドレスを指定して、[API経由でユーザー・プロフィール・データをエクスポート][88]できるようになった。
このエクスポートには、そのメールアドレスに関連するすべてのプロファイルが含まれる。

## メールテンプレートAPI

[API経由でメールテンプレートを][87]作成・更新できるようになった。各テンプレートは、他のAPIコールで参照できる**email_template_idを**持つ。

## REST APIキーのパーミッション

[複数のREST APIキーを][86]作成し、それぞれにアクセス許可を設定できるようになった。各キーは、特定のエンドポイントへのアクセスを許可するように設定できる。

また、特定のREST APIキーに対してREST APIリクエストを許可するIPアドレスとサブネットの[ホワイトリスト][85]を指定することもできます。

[85]: {{site.baseurl}}/developer_guide/rest_api/basics/#api-ip-whitelisting
[86]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[87]: {{site.baseurl}}/developer_guide/rest_api/email_templates/#email-templates
[88]: {{site.baseurl}}/developer_guide/rest_api/export/#user-export
[89]: {{site.baseurl}}/help/best_practices/utilizing_badge_count/#utilizing-badge-count
