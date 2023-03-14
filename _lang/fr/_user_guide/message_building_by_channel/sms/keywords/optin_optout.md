---
nav_title: Abonnement/Désabonnement
article_title: Mots-clés Abonnement/Désabonnement aux SMS
page_order: 0
description: "Cet article de référence explique comment Braze traite les mots-clés de base d’abonnement et de désabonnement pour l’envoi de messages SMS."
page_type: reference
tool:
  - Tableau de bord

channel:
  - SMS
---

# Mots-clés d’abonnement et de désabonnement

Les réglementations exigent qu’il y ait des réponses à toutes les questions sur l’abonnement, le désabonnement, l’aide/les informations et les réponses à des mots-clés. Braze traite automatiquement les messages suivants _exacts, uniques et non sensibles à la casse_, en mettant automatiquement à jour [l’état du groupe d’abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) pour l’utilisateur et le numéro de téléphone associé dans toutes les demandes entrantes.

## Aperçu du mot-clé

Braze traitera automatiquement les mots-clés suivants et mettra à jour l’état du groupe d’abonnement pour le numéro de téléphone dans toutes les demandes entrantes. Notez que ces mots-clés et réponses par défaut sont également personnalisables. 

| Type | Mot-clé | Changement |
|-|-------|---|
|Abonnement| `START`<br> `YES`<br> `UNSTOP` | Toute demande entrante avec l’un de ces mots-clés `Opt-In` entraînera un changement d’état du groupe d’abonnement `subscribed`. De plus, l’ensemble de numéros associés à ce groupe d’abonnement sera désormais en mesure d’envoyer un SMS à ce client. <br><br>L’utilisateur reçoit votre réponse automatique d’abonnement définie.  |
|Désabonnement| `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | Toute demande entrante avec l’un de ces mots-clés `Opt-Out` entraînera un changement d’état du groupe d’abonnement `unsubscribed`. De plus, l’ensemble de numéros associés à ce groupe d’abonnement ne sera plus en mesure d’envoyer un SMS à ce client.<br><br>L’utilisateur reçoit votre réponse automatique de désabonnement définie. |
| Aide | `HELP`<br> `INFO` | L’utilisateur reçoit votre réponse automatique d’aide définie. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Seul le **message avec exactement un mot** est traité (_non sensible_ à la casse). Les mots-clés tels que `ARRÊTEZ S’IL VOUS PLAIT` seront ignorés sauf si vous avez activé les [désinscriptions vagues][fuzzylink].

Si un destinataire utilise les mots-clés `HELP` ou `INFO`, une réponse est automatiquement déclenchée. Le modèle de SMS pour ces messages de réponse automatique est défini pendant votre [onboarding][oblink] et la période d’acquisition de numéros de téléphone. Notez que vous pouvez continuer à mettre à jour ces réponses après la période d’onboarding initiale.


{% alert tip %}
Vous souhaitez étendre votre traitement des opt-out ? Essayez le [désabonnement vague]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/fuzzy_opt_out/), une fonctionnalité qui tente de déterminer lorsqu’un message entrant ne correspond pas à un mot-clé de désabonnement, mais en indique l’intention.
{% endalert %}

[oblink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[fuzzylink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/fuzzy_opt_out/
