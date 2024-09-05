---
nav_title: プッシュ・アンサブスクライブのトラッキング
article_title: プッシュ・アンサブスクライブのトラッキング
page_type: solution
description: "このヘルプでは、プッシュ配信停止を追跡するためのヒントをいくつか紹介します。"
channel: push
---

# プッシュ配信停止の追跡

プッシュ配信停止sは、アップルやグーグルなどのプロバイダからのユーザーのプッシュステータスへの更新に依存します。これらの更新s は、頻度が低く、予測不可能な場合があります。そのため、プッシュ配信停止sはプッシュキャンペーン 分析のメトリクスとして含まれません。 

ただし、手動でプッシュ配信停止を"トラッキングすると、通知頻度と内容の関連性に対するユーザーレスポンスに貴重なインサイトを提供することができます。"トラッキングプッシュ配信停止sには、次の2つの方法があります。

## オプション 1: Segment フィルターsを使用

回避策として、Segmentを作成して、プッシュが有効になっていないユーザーを識別できます。つまり、サブスクライブまたはオプトインされておらず、[フォアグラウンドプッシュトークン]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens)がありません。たとえば、Android アプリ内の配信停止の個数を表示するには、次のSegments の組合せを使用します。 

- `Background or Foreground Push Enabled for App "TEST (Android)" is false`
- `Has Uninstalled`

![フィルター "Background またはForeground Push Enabled for アプリ"TEST (Android) アプリがfalse で、フィルター "Has Uninstalled"が選択され、2393 の到達可能なユーザーs.]({% image_buster /assets/img/push_unsub_segment_example.png %})が表示されます。

セグメンテーション フィルターs はアプリ近接であり、特に日付とキャンペーンに結びつけることはできません。

## オプション 2: カスタムイベントの使用

{% alert important %}
サブスクリプション変更のカスタムイベントを記録すると、[データポイント s]({{site.baseurl}}/user_guide/data_and_analytics/data_points#consumption-count) が消費されることに注意してください。または、Segment フィルターs を使用して、プッシュが有効になっていないユーザーを識別し、対象にします。
{% endalert %}

別の回避策では、このメトリクスを追跡するために、ユーザーのプッシュ有効ステータスが`true` または`false` のいずれであるかに基づいてプッシュ配信停止s のカスタムイベントを作成することもお勧めします。

_2024更新6月13日昨日_
