---
nav_title: メールバウンス
article_title: メールバウンス
page_order: 0
page_type: solution
description: "このヘルプ記事では、ハードバウンスとソフトバウンスの違いを明確に説明します。"
channel: email
---

# メールバウンス

メール キャンペーンからのメッセージがユーザーのメールの住所から跳ね返った場合、どうしますか?まず、ハードバウンスとソフトバウンスの2種類のメールバウンスを定義してトラブルシューティングしましょう。 

## ハードバウンス

{% multi_lang_include metrics.md metric='Hard Bounce' %}

詳細については、[ハードバウンス]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#hard-bounce)を参照してください。

## ソフトバウンス数

{% multi_lang_include metrics.md metric='Soft Bounce' %} 

メールがソフトバウンスを受信した場合、通常は72時間以内に再試行されますが、再試行回数は受信側ごとに異なります。

ソフトバウンスはキャンペーン分析では追跡されませんが、[メッセージアクティビティログ][3]で監視できます。ここでは、ソフトバウンスの理由を確認し、メールキャンペーンの「送信数」と「配信数」の間で発生しうる不一致を把握することもできます。

メール購読とキャンペーンの管理の詳細については、「[メールのベストプラクティス][2]」を参照してください。

それでもサポートが必要な場合は、[サポートチケットを]({{site.baseurl}}/braze_support/)を登録してください。

_最終更新日: 2024年5月2日_

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices
[3]: {{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/
