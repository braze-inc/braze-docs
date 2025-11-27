---
nav_title: "地理的許可"
article_title: 地理的許可
description: "この記事では、SMS、MMS、RCSを配信できる国を選択できる、Geographic Permissionsの国別許可リストについて説明する。"
page_order: 2
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
alias: /geographic_permissions/
  
---

# 地理的許可

> 地理的権限は、あなたがメッセージを送信することができる国のコントロールを強制することにより、セキュリティを強化し、不正なSMS、MMS、およびRCSトラフィックから保護する。国の許可リストを指定して、SMS、MMS、RCSメッセージが承認された地域にのみ送信されるようにすることができる。管理者のみが、国の許可リストを変更できます。管理者以外のユーザーは、サブスクリプショングループがどの国に送信できるかを示す読込専用版の許可リストにアクセスできます。

管理者は、許可リストに含まれている国を設定できます。国の許可リストは、[サブスクリプショングループ]({{site.baseurl}}/sms_rcs_subscription_groups/) レベルで設定されます。[**オーディエンス**] > [**サブスクリプション**] に移動して、SMS、MMS、または RCS サブスクリプショングループを選択すると、国の許可リストにアクセスできます。許可リストは [**地理的許可**] の下にあります。

![[国許可リスト] で複数の国が選択されている管理者用の編集可能な [SMS の地理的許可] セクション。]({% image_buster /assets/img/sms/sms_geographic_permissions.png %})({: style="max-width:80%;"})

### 国の選定

ドロップダウンを使用して、許可リストに国を追加します。最も一般的な SMS と RCSの国が上部に表示され、その他の国は下に表示されます。また、テキストフィールドに入力して国を検索することもできます。

!["Country allowlist"ドロップダウン。最も一般的な国が最上位に表示されます。]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

以前に選択した国の隣にあるそれぞれのボックスをクリアして、その国を削除します。

### 変更の保存

変更は、**Save**を選択すると有効になります。許可リストから国を削除すると、すべてのSMS、MMS、RCSメッセージがそれらの国の番号に送信されなくなる。

![許可リストから削除される国を確認する警告 モーダル。]({% image_buster /assets/img/sms/delete_allowlist_warning.png %}){: style="max-width:70%;"}

## ハイリスク国

一部の国では、SMS および RCS トラフィックポンピングのリスクが高くなっています。これらの国は、国ドロップダウンの**High Risk** タグで示されます。

![アゼルバイジャンの国名ドロップダウンには "高リスク "タグが付いている。]({% image_buster /assets/img/sms/high_risk.png %}){: style="max-width:80%;"}

これらの国での送信を許可する場合は、まずそのリスクを認識してから許可リストに国を追加する必要があります。

{% alert note %}
許可リストに含める国を、ビジネスニーズをサポートするために必要な国のみに限定してください。これにより、不正なトラフィックの可能性を最小限に抑えることができます。SMSトラフィックポンピングの防止に関する詳細なガイダンスについては、[SMSトラフィックポンピング詐欺FAQs]({{site.baseurl}}/sms_traffic_pumping_fraud/)を参照してください。
{% endalert %}

## ブロックされた送信の可視性

許可リストにない国への送信を試行すると、中止されます。中止されたメッセージは、[メッセージアクティビティログ]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/)と[SMS メッセージ中止エンゲージメントイベント]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/)に記録されます。 

ブロックされ送信が原因で発生した中止メッセージは、[**メッセージ中止のエラー**] として表示され、「受信者の電話番号はブロックされている国の番号です」というメッセージが表示されます。

![電話番号がブロックされている国の番号であるためにブロックされた SMS 送信を示す中止ログ。]({% image_buster /assets/img/sms/abort_log.png %})({: style="max-width:80%;"})

