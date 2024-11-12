---
nav_title: 2月
page_order: 11
noindex: true
page_type: update
description: "この記事には2018年2月のリリースノートが含まれている。"
---
# 2018年2月

## iOSプッシュバッジ数

Brazeからのプッシュコンポーザー内で[更新バッジ数][89]が可能になりました。
プッシュメッセージごとに、通知 トリガーするバッジ数を指定できます。

## メールアドレスを使用してAPI経由でユーザーをエクスポートする

メールアドレスを指定して、[API経由でユーザー・プロフィール・データをエクスポート][88]できるようになった。
このエクスポートには、そのメールアドレスに関連するすべてのプロファイルが含まれる。

## メールテンプレートAPI

[メールテンプレートを API を介して][87]作成および更新できるようになりました。それぞれのテンプレートには、他のAPI 呼び出しで参照できる**メール_テンプレート_id** があります。

## REST APIキーのパーミッション

[複数のREST APIキーを][86]作成し、それぞれにアクセス許可を設定できるようになった。各キーは、特定のエンドポイントへのアクセスを許可するように設定できる。

また、特定のREST APIキーに対してREST APIリクエストを許可するIPアドレスとサブネットの[ホワイトリスト][85]を指定することもできます。

[85]: {{site.baseurl}}/developer_guide/rest_api/basics/#api-ip-whitelisting
[86]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[87]: {{site.baseurl}}/developer_guide/rest_api/email_templates/#email-templates
[88]: {{site.baseurl}}/developer_guide/rest_api/export/#user-export
[89]: {{site.baseurl}}/help/best_practices/utilizing_badge_count/#utilizing-badge-count
