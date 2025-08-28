---
nav_title: 1月
page_order: 12
noindex: true
page_type: update
description: "この記事は、2018年1月のリリースノートを含んでいます。"
---
# 2018年1月

## CSSインライン展開

[ CSS インライン化]({{site.baseurl}}/user_guide/message_building_by_channel/email/css_inline/#css-inlining) を個別のメールメッセージに対してオンまたはオフに切り替えるには、** メール設定** を選択します。

## 新規セグメントフィルター

次のフィルターs を使用してSegments を作成できるようになりました。
- キャンバスステップを受信しました
- 開いた/クリックしたキャンバスステップ
- 最後に受信した特定のキャンバスステップ

{% alert update %}
2019年3月より、`Received Canvas Step` は `Received Message from Canvas Step` に、`Last Received Specific Canvas Step` は `Last Received Message from Specific Canvas Step` に名称変更されています。
{% endalert %}

## デバイス ID を使用してユーザーをエクスポートする

このエンドポイントでは、パラメータとして装置識別子を受け入れるようになりました。これにより、[匿名ユーザープロファイルs]({{site.baseurl}}/developer_guide/rest_api/export/#users-by-identifier-endpoint)をエクスポートできます。

デバイスID を使用して、そのデバイス上のすべてのユーザープロファイルをエクスポートできます。

## エンゲージメントレポートの更新

**プッシュ開封率**や**コンバージョン率**などの追加統計が[エンゲージメントレポート]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports/#engagement-reports)で利用できるようになりました。

## アップルプッシュ証明書s:.p8 ファイルの使用

Apple プッシュ証明書をアップロードするときに[p8 ファイル]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#recommended-option-using-a-p8-file-authentication-tokens) を使用して、iOS プッシュ認証情報s が期限切れにならないようにすることができます。


