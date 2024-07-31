---
nav_title: 1月
page_order: 12
noindex: true
page_type: update
description: "この記事には2018年1月のリリースノートが含まれている。"
---
# 2018年1月

## CSSインライン化

**メール**設定で、個々のメールメッセージの[CSSインラインの][84]オン・オフを切り替えられるようになった。

## 新しいセグメンテーションフィルター

以下のフィルターを使用して、セグメンテーションを作成できるようになった：
- キャンバスステップを受け取る
- 開封/クリック キャンバスステップ
- 最後に受け取った特定のキャンバスステップ

{% alert update %}
2019年3月現在、`Received Canvas Step` は`Received Message from Canvas Step` に、`Last Received Specific Canvas Step` は`Last Received Message from Specific Canvas Step` に名称が変更されている。
{% endalert %}

## デバイスIDを使ってユーザーをエクスポートする

このエンドポイントはパラメータとしてデバイス識別子を受け付けるようになり、[匿名ユーザープロファイルをエクスポート][82]できるようになった。

デバイスIDを使って、そのデバイス上のすべてのユーザープロファイルをエクスポートできる。

## エンゲージメントレポート更新

**プッシュ開封率や** **コンバージョン率などの**追加統計が、[エンゲージメントレポートで][81]利用できるようになった。

## アップルのプッシュ証明書：.p8ファイルを使う

Apple Push証明書をアップロードする際に[p8ファイルを][80]使用できるようになり、iOSプッシュ認証情報の有効期限が切れることがなくなった。


[80]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#recommended-option-using-a-p8-file-authentication-tokens
[81]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#engagement-reports
[82]: {{site.baseurl}}/developer_guide/rest_api/export/#users-by-identifier-endpoint
[84]: {{site.baseurl}}/user_guide/message_building_by_channel/email/css_inline/#css-inlining
