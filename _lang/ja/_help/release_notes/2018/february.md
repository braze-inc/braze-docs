---
nav_title: 2月
page_order: 11
noindex: true
page_type: update
description: "この記事には2018年2月のリリースノートが含まれている。"
---
# 2018年2月

## iOSプッシュバッジ数

Brazeからプッシュコンポーザー内で[バッジ数を更新][89]できるようになった。
各プッシュメッセージに対して、その通知がトリガーするバッジカウントを指定することができる。

## メールアドレスを使用してAPI経由でユーザーをエクスポートする

[ユーザープロファイルのデータを][88]、メールアドレスを指定して[API経由でエクスポート][88]できるようになった。
このエクスポートには、そのメール・アドレスに関連するすべてのプロファイルが含まれる。

## メールテンプレートAPI

[API経由でメールテンプレートを][87]作成・更新できるようになった。各テンプレートは、他のAPIコールで参照できる**email_template_idを**持つ。

## REST APIキーの権限

[複数のREST APIキーを][86]作成し、それぞれにアクセス権限を設定できるようになった。各キーは、特定のエンドポイントへのアクセスを許可するように設定できる。

また、指定したREST APIキーに対してREST APIリクエストを許可する[IPアドレスと][85]サブネット[のホワイトリストを][85]指定することもできる。

[85]: {{site.baseurl}}/developer_guide/rest_api/basics/#api-ip-whitelisting
[86]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[87]: {{site.baseurl}}/developer_guide/rest_api/email_templates/#email-templates
[88]: {{site.baseurl}}/developer_guide/rest_api/export/#user-export
[89]: {{site.baseurl}}/help/best_practices/utilizing_badge_count/#utilizing-badge-count
