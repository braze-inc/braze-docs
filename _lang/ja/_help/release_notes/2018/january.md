---
nav_title: 1 月
page_order: 12
noindex: true
page_type: update
description: "この記事には、2018 年 1 月のリリース ノートが含まれています。"
---
# 2018年1月号

## CSS のインライン化

メール**設定**に移動して、個々のメールメッセージの[CSSインライン化][84]のオンとオフを切り替えられるようになりました。

## 新しいセグメント フィルター

次のフィルターを使用してセグメントを作成できるようになりました。
\- 受信キャンバスステップ
\- Opened/Clicked Canvas ステップ
\- Last Received Specific Canvas Step (最後に受信した特定のキャンバス ステップ)

{% alert update %}
2019 年 3 月現在、 `Received Canvas Step` は に `Received Message from Canvas Step`改名され、 `Last Received Specific Canvas Step` に改名 `Last Received Message from Specific Canvas Step`されました。
{% endalert %}

## デバイス ID を使用したユーザーのエクスポート

このエンドポイントは、デバイス識別子をパラメーターとして受け入れるようになり、 [匿名ユーザープロファイルをエクスポート][82]できるようになりました。

デバイス ID を使用して、そのデバイス上のすべてのユーザー プロファイルをエクスポートできます。

## エンゲージメントレポートの更新

**プッシュ開封率**や**コンバージョン率**などの追加統計が[エンゲージメントレポート][81]で利用できるようになりました。

## Apple プッシュ証明書:.p8 ファイルの使用

Apple プッシュ証明書のアップロード時に [p8 ファイルを][80] 使用できるようになり、iOS プッシュ資格情報が期限切れにならないようにできるようになりました。


[80]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#recommended-option-using-a-p8-file-authentication-tokens
[81]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#engagement-reports
[82]: {{site.baseurl}}/developer_guide/rest_api/export/#users-by-identifier-endpoint
[84]: {{site.baseurl}}/user_guide/message_building_by_channel/email/css_inline/#css-inlining
