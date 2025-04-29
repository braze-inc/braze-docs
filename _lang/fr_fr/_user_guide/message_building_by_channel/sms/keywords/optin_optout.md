---
nav_title: Mots-clés d’abonnement et de désabonnement
article_title: Mots-clés Abonnement/Désabonnement aux SMS
page_order: 0
description: "Cet article de référence explique comment Braze traite les mots-clés de base d’abonnement et de désabonnement pour l’envoi de messages SMS."
page_type: reference
tool:
  - Dashboard

channel:
  - SMS
---

# Mots-clés d’abonnement et de désabonnement

> Les réglementations exigent qu’il y ait des réponses à toutes les questions sur l’abonnement, le désabonnement, l’aide/les informations et les réponses à des mots-clés. Braze traite automatiquement les messages suivants _exacts, uniques et non sensibles à la casse_, en mettant automatiquement à jour [l’état du groupe d’abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) pour l’utilisateur et le numéro de téléphone associé dans toutes les demandes entrantes.

## Aperçu du mot-clé

Braze traitera automatiquement les mots-clés suivants et mettra à jour l'état du groupe d'abonnement pour le numéro de téléphone sur toutes les demandes entrantes. Notez que ces mots-clés et réponses par défaut sont également personnalisables. 

| Type | Mot-clé | Changement |
\|-|-------|---|
|Abonnement| `START`<br> `YES`<br> `UNSTOP` | Toute demande entrante avec l'un de ces `Opt-In` mots-clés entraînera un changement d'état du groupe d'abonnement à `subscribed`. De plus, l’ensemble de numéros associés à ce groupe d’abonnement sera désormais en mesure d’envoyer un SMS à ce client. <br><br>L’utilisateur reçoit votre réponse automatique d’abonnement définie.  |
|Se désinscrire| `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | Toute demande entrante avec l'un de ces `Opt-Out` mots-clés entraînera un changement d'état du groupe d'abonnement à `unsubscribed`. De plus, le pool de numéros associé à ce groupe d'abonnement ne pourra plus envoyer de message SMS à ce client.<br><br>L’utilisateur reçoit votre réponse automatique de désabonnement définie. |
| Aide | `HELP`<br> `INFO` | L'utilisateur recevra votre réponse automatique d'aide définie. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Seul le **message exact, d'un seul mot** est traité (non sensible à la casse). Les mots-clés tels que `STOP PLEASE` seront ignorés sauf si [l'option de désactivation vague][fuzzylink] est activée.

Si un destinataire utilise les mots-clés `HELP` ou `INFO`, une réponse est automatiquement déclenchée. Le modèle de SMS pour ces messages de réponse automatique sera défini pendant votre [intégration][oblink] et la période d'acquisition de numéro de téléphone. Notez que vous pouvez continuer à mettre à jour ces réponses après la période d’onboarding initiale.

{% alert tip %}
Vous souhaitez étendre votre traitement des opt-out ? Essayez [l'option de désinscription floue]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/fuzzy_opt_out/), une fonctionnalité qui tente de reconnaître quand un message entrant ne correspond pas à un mot-clé de désinscription, mais indique une intention de désinscription.
{% endalert %}

[oblink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[fuzzylink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/fuzzy_opt_out/
