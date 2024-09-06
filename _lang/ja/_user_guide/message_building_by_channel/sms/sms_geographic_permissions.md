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

> SMS 地理的許可は、SMS メッセージを送信できる国にコントロールを強制することにより、セキュリティを強化し、不正なSMS トラフィックから保護します。各国の許可リストを指定して、SMS メッセージがアプリの認証済みリージョンにのみ送信されるようにすることができます。管理者のみが、国の許可リストを変更できます。管理者以外のユーザーは、サブスクリプショングループがどの国に送信できるかを示す読込専用版の許可リストにアクセスできます。

!["Country allowlist" で選択された米国および英国の管理者以外のユーザーの参照のみのSMS 地理的権限セクション。][6]{: style="max-width:80%;"}

## SMS 国の許可リストの設定

管理者の場合は、allowlist にある国を設定できます。国の許可リストは、[サブスクリプショングループ]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) レベルで設定されます。**Audience** > **サブスクリプション s** に進み、SMS サブスクリプショングループを選択すると、アクセスできます。allowlist は**SMS Geographic Permissions** の下にあります。

![「"Country allowlist"」で選択した、オーストラリア、カナダ、および米国の管理者用の編集可能なSMS 地理的権限セクション。][1]{: style="max-width:80%;"}

### 国の選定

ドロップダウンでallowlist に国を追加します。最も一般的なSMS の国は上部に表示されますが、その他は次のとおりです。また、テキストフィールドに入力して国を検索することもできます。

!["Country allowlist"ドロップダウン。最も一般的な国が最上位に表示されます。][2]{: style="max-width:80%;"}

以前に選択した国の隣にあるそれぞれのボックスをクリアして、その国を削除します。

### 変更の保存

変更は、**Save**を選択すると有効になります。allowlist から国を削除すると、すべてのSMS およびMMS メッセージがそれらの国の番号に送信されなくなります。

![許可リストから削除される国を確認する警告 モーダル。][3]{: style="max-width:70%;"}

## ハイリスク国

一部の国では、SMSトラフィックポンプのリスクが高くなっています。これらの国は、国ドロップダウンの**High Risk** タグで示されます。

![アゼルバイジャンが" High Risk" タグを持っているため、ダウン・ダウン・カントリー。][4]{: style="max-width:80%;"}

これらの国での送信を許可する場合は、その国が許可リストに追加される前に、まずそのリスクを確認する必要があります。

{% alert note %}
許可リストの国を、ビジネスニーズをサポートするために必要な国に限定します。これにより、不正なトラフィックの可能性を最小限に抑えることができます。SMSトラフィックポンピングの防止に関する詳細なガイダンスについては、[SMSトラフィックポンピング詐欺FAQs]({{site.baseurl}}/sms_traffic_pumping_fraud/)を参照してください。
{% endalert %}

## ブロック送信の可視性

許可リストにない国への送信を試みると、中止されます。中止されたメッセージは、[Message Activity Log]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)と[SMS abort message エンゲージメント event]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/)に記録されます。 

ブロックの送信によってアボートされたメッセージは、`Abort_Type = "blocked_recipient_country"` と表示され、アボートログにはブロックの国名が記録されます。

![ブロックed_受信者_countryのabort_typeとブロックed電話番号の国名イニシャルを示す中止ログ。][5]{: style="max-width:80%;"}

[1]: {% image_buster /assets/img/sms/sms_geographic_permissions.png %}
[2]: {% image_buster /assets/img/sms/allowlist_dropdown.png %}
[3]: {% image_buster /assets/img/sms/delete_allowlist_warning.png %}
[4]: {% image_buster /assets/img/sms/high_risk.png %}
[5]: {% image_buster /assets/img/sms/abort_log.png %}
[6]: {% image_buster /assets/img/sms/sms_geographic_permissions_read_only.png %}