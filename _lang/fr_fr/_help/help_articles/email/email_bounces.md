---
nav_title: E-mails renvoyés
article_title: E-mails renvoyés
page_order: 0
page_type: solution
description: "Cet article explique quelle est la différence entre les échecs d'envoi et les échecs d'envoi définitifs."
channel: email
---

# E-mails renvoyés

Que faites-vous lorsqu'un message de votre campagne par e-mail est renvoyé par les adresses e-mail de vos utilisateurs ? Tout d'abord, définissons et résolvons les deux types de rebonds d'e-mails : les rebonds durs et les rebonds doux. 

## Échecs d'envoi définitifs

{% multi_lang_include metrics.md metric='Hard Bounce' %}

Pour plus d'informations, voir l'[échec d'envoi définitif]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics/#hard-bounce).

## Soft bounces

{% multi_lang_include metrics.md metric='Soft Bounce' %} 

Si un e-mail reçoit un rebond temporaire, nous réessayerons généralement dans les 72 heures, mais le nombre de tentatives de réessai varie d'un destinataire à l'autre.

Bien que les rebonds doux ne soient pas suivis dans vos analyses de campagne, vous pouvez surveiller les rebonds doux dans le [Journal d'activité des messages][3]. Ici, vous pouvez également voir la raison du soft bounce et comprendre les éventuelles divergences entre les « envois » et les « livraisons » dans vos campagnes e-mail.

Pour en savoir plus sur la gestion de vos abonnements et campagnes par e-mail, consultez [Les meilleures pratiques pour les e-mails][2].

Vous avez toujours besoin d’aide ? Ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 2 mai 2024_

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices
[3]: {{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/
