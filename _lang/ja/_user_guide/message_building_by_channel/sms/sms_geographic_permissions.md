---
nav_title: "SMSの地理的権限"
article_title: SMSの地理的権限
description: "この記事では、SMS Geographic Permissions の国の許可者について説明します。これにより、SMS を配信できる国を選択できます。"
page_order: 4.5
page_type: reference
channel:
  - SMS
alias: "/sms_geographic_permissions/"
  
---

# SMSの地理的権限

> SMS 地理的許可は、SMS メッセージを送信できる国にコントロールを強制することにより、セキュリティを強化し、不正なSMS トラフィックから保護します。国の許可リストを指定して、承認済みの地域にのみ SMS メッセージを送信することができます。管理者のみが、国の許可リストを変更できます。管理者以外のユーザーは、サブスクリプショングループがどの国に送信できるかを示す読込専用版の許可リストにアクセスできます。

![[国の許可リスト] で選択された米国および英国の管理者以外のユーザーに表示される、読み取り専用の [SMS 地理的許可] セクション。][6]{: style="max-width:80%;"}

## SMS 国の許可リストの設定

管理者は、許可リストに含まれている国を設定できます。国の許可リストは、[サブスクリプショングループ]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) レベルで設定されます。[**オーディエンス**] > [**サブスクリプション**] に移動して、SMS サブスクリプショングループを選択すると、国の許可リストにアクセスできます。allowlist は**SMS Geographic Permissions** の下にあります。

![「"Country allowlist"」で選択した、オーストラリア、カナダ、および米国の管理者用の編集可能なSMS 地理的権限セクション。][1]{: style="max-width:80%;"}

### 国の選定

ドロップダウンを使用して、許可リストに国を追加します。最も一般的なSMS の国は上部に表示されますが、その他は次のとおりです。また、テキストフィールドに入力して国を検索することもできます。

!["Country allowlist"ドロップダウン。最も一般的な国が最上位に表示されます。][2]{: style="max-width:80%;"}

以前に選択した国の隣にあるそれぞれのボックスをクリアして、その国を削除します。

### 変更の保存

変更は、**Save**を選択すると有効になります。allowlist から国を削除すると、すべてのSMS およびMMS メッセージがそれらの国の番号に送信されなくなります。

![許可リストから削除される国を確認する警告 モーダル。][3]{: style="max-width:70%;"}

## ハイリスク国

一部の国では、SMSトラフィックポンプのリスクが高くなっています。これらの国は、国ドロップダウンの**High Risk** タグで示されます。

![アゼルバイジャンの国名ドロップダウンには "高リスク "タグが付いている。][4]{: style="max-width:80%;"}

これらの国での送信を許可する場合は、まずそのリスクを認識してから許可リストに国を追加する必要があります。

{% alert note %}
許可リストに含める国を、ビジネスニーズをサポートするために必要な国のみに限定してください。これにより、不正なトラフィックの可能性を最小限に抑えることができます。SMSトラフィックポンピングの防止に関する詳細なガイダンスについては、[SMSトラフィックポンピング詐欺FAQs]({{site.baseurl}}/sms_traffic_pumping_fraud/)を参照してください。
{% endalert %}

## ブロックされた送信の可視性

許可リストにない国への送信を試行すると、中止されます。中止されたメッセージは、[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)と[SMS メッセージ中止エンゲージメントイベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/)に記録されます。 

送信のブロックによって中止されたメッセージは `Abort_Type = "blocked_recipient_country"` と表示され、ブロックされた国の詳細を示す中止ログもともに表示されます。

![blocked_recipient_country の abort_type、およびブロックされた電話番号が属する国のイニシャルを示す中止ログ。][5]{: style="max-width:80%;"}

[1]: {% image_buster /assets/img/sms/sms_geographic_permissions.png %}
[2]: {% image_buster /assets/img/sms/allowlist_dropdown.png %}
[3]: {% image_buster /assets/img/sms/delete_allowlist_warning.png %}
[4]: {% image_buster /assets/img/sms/high_risk.png %}
[5]: {% image_buster /assets/img/sms/abort_log.png %}
[6]: {% image_buster /assets/img/sms/sms_geographic_permissions_read_only.png %}