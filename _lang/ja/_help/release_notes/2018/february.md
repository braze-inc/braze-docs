---
nav_title: 2月
page_order: 11
noindex: true
page_type: update
description: "この記事は、2018年2月のリリースノートを含んでいます。"
---
# 2018年2月

## iOSプッシュバッジ数

これで、Braze からのプッシュコンポーザー内で[バッジ数][89] を更新できます。
プッシュメッセージごとに、通知がトリガーするバッジ数を指定できます。

## メールアドレスを使用したAPI 経由のユーザーのエクスポート

メールアドレスを指定することで、API 経由でユーザプロファイルデータをエクスポートできるようになりました[。
このエクスポートには、そのメールアドレスに関連付けられたすべてのプロファイルが含まれます。

## メールテンプレートAPI

これで、API 経由で[メールテンプレートを作成および更新できるようになりました。各テンプレートには、他のAPI 呼び出しで参照できる**email\_template\_id** があります。

## REST API キーの権限

[複数のREST APIキー][86]を作成し、それぞれのアクセス権限を設定できるようになりました。各キーは、特定のエンドポイントへのアクセスを許可するように設定できます。

また、[ IP アドレスのホワイトリスト][85] と、指定されたREST API キーに対してREST API リクエストを実行できるサブネットを指定できます。

[85]: {{site.baseurl}}/developer_guide/rest_api/basics/#api-ip-whitelisting
[86]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[87]: {{site.baseurl}}/developer_guide/rest_api/email_templates/#email-templates
[88]: {{site.baseurl}}/developer_guide/rest_api/export/#user-export
[89]: {{site.baseurl}}/help/best_practices/utilizing_badge_count/#utilizing-badge-count
