---
nav_title: リンク短縮
article_title: リンク短縮
page_order: 3
description: "この参照記事では、SMSメッセージでリンク短縮をオンにする方法と、よくある質問について説明します。"
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
---

# リンク短縮

> このページでは、SMS および RCS メッセージでリンク短縮を有効にする方法、短縮リンクをテストする方法、短縮リンクでカスタムドメインを使用する方法などについて説明します。

{% alert important %}
Braze は[統合リンク短縮]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/?sdktab=unified)を段階的にロールアウトしています。これにより、すべての SMS および RCS の短縮リンクが単一のパーソナライズ済みリンク形式（例: `brz.ai/abcdefgh`）に統合されます。
{% endalert %}

{% sdktabs %}
{% sdktab Legacy %}

{% multi_lang_include link_shortening_temp/legacy_link_shortening.md %}

{% endsdktab %}
{% sdktab Unified %}

{% multi_lang_include link_shortening_temp/unified_link_shortening.md %}

{% endsdktab %}
{% endsdktabs %}