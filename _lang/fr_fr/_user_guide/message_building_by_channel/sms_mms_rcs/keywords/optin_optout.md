---
nav_title: "Mots clés pour l'abonnement et l'exclusion"
article_title: "Mots clés pour l'abonnement et l'exclusion par SMS"
page_order: 0
description: "Cet article de référence explique comment Braze traite les mots-clés opt-in et opt-out de base pour l'envoi de messages par SMS."
page_type: reference
alias: /optin_optout/
tool:
  - Dashboard

channel:
  - SMS
---

# Mots clés d'abonnement et d'exclusion

> La réglementation exige qu'il y ait des réponses à toutes les réponses de type "opt-in", "opt-out" et "help/info" par mot-clé. Braze traite automatiquement les messages _exacts_ suivants _, composés d'un seul mot et insensibles à la casse_, en mettant automatiquement à jour l'[état du groupe d'abonnement]({{site.baseurl}}/sms_rcs_subscription_groups/) pour l'utilisateur et son numéro de téléphone associé sur toutes les demandes entrantes.

## Aperçu des mots-clés

Braze traitera automatiquement les mots-clés suivants et mettra à jour l'état du groupe d'abonnement pour le numéro de téléphone sur toutes les demandes entrantes. Notez que ces mots-clés et réponses par défaut peuvent également être personnalisés. 

| Type | Mot-clé | Modifier |
\|-|-------|---|
|Abonnement| `START`<br> `YES`<br> `UNSTOP` | Toute demande entrante contenant l'un de ces mots-clés `Opt-In` entraînera un changement d'état du groupe d'abonnement à `subscribed`. En outre, les expéditeurs associés à ce groupe d'abonnement pourront désormais envoyer un message SMS, MMS ou RCS à ce client (en fonction du type d'envoi de messages pris en charge par les expéditeurs). <br><br>L'utilisateur recevra la réponse automatique Opt-In que vous avez définie.  |
|Opt-out| `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | Toute demande entrante contenant l'un de ces mots-clés `Opt-Out` entraînera un changement d'état du groupe d'abonnement à `unsubscribed`. En outre, le pool de numéros associé à ce groupe d'abonnement ne pourra plus envoyer de messages à ce client.<br><br>L'utilisateur recevra la réponse automatique d'exclusion que vous avez définie. |
| Aide `HELP`<br> `INFO` | L'utilisateur recevra la réponse automatique d'aide que vous avez définie. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Seul le **message exact, composé d'un seul mot,** sera traité (insensible à la casse). Les mots clés tels que `STOP PLEASE` seront ignorés à moins que l'[option fuzzy opt-out]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/fuzzy_opt_out/) ne soit activée.

Si un destinataire utilise les mots-clés `HELP` ou `INFO`, une réponse sera déclenchée automatiquement. La réponse par défaut pour ces messages de réponse automatique sera définie au cours de votre période d'[onboarding]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process) et d'obtention du numéro de téléphone. Notez que vous pouvez continuer à mettre à jour ces réponses après la période initiale d'onboarding.

{% alert tip %}
Vous souhaitez étendre votre traitement de l'opt-out ? Essayez le [fuzzy opt-out]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/fuzzy_opt_out/), une fonctionnalité qui tente de reconnaître lorsqu'un message entrant ne correspond pas à un mot-clé d'opt-out, mais indique une intention d'opt-out.
{% endalert %}

