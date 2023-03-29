---
nav_title: Abonnement/Désabonnement
article_title: Mots-clés Abonnement/Désabonnement aux SMS
page_order: 0
description: "Cet article de référence explique comment Braze traite les mots-clés de base d’abonnement et de désabonnement pour la messagerie SMS."
page_type: reference
tool:
  - Dashboard

channel:
  - SMS
---

# Mots-clés d’abonnement et de désabonnement

Les réglementations exigent qu’il y ait des réponses à toutes les questions sur l’abonnement, le désabonnement, l’aide/les informations et les réponses à des mots-clés. Braze traite automatiquement les messages suivants _exacts, uniques et sensibles à la casse_ , en mettant automatiquement à jour [l’état du groupe d’abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) pour l’utilisateur et le numéro de téléphone associé dans toutes les demandes entrantes.

## Aperçu du mot-clé

Braze traitera automatiquement les mots-clés suivants et mettra à jour l’état du groupe d’abonnement pour le numéro de téléphone dans toutes les demandes entrantes. Notez que ces mots-clés et réponses par défaut sont également personnalisables. 

| Type | Mot-clé | Changement |
|-|-------|---|
|Abonnement| `START`<br> `YES`<br> `UNSTOP` | Toute demande entrante avec l’un de ces mots-clés `Opt-In` entraînera un changement d’état du groupe d’abonnement `subscribed`. De plus, l’ensemble de numéros associés à ce groupe d’abonnement sera désormais en mesure d’envoyer un SMS à ce client. <br><br>L’utilisateur reçoit votre réponse automatique d’abonnement définie.  |
|Désabonnement| `STOP`<br> `STOPALL`<br> `UNSUBSCRIBE`<br> `CANCEL`<br> `END`<br> `QUIT` | Toute demande entrante avec l’un de ces mots-clés `Opt-Out` entraînera un changement d’état du groupe d’abonnement `unsubscribed`. De plus, l’ensemble de numéros associés à ce groupe d’abonnement ne sera plus en mesure d’envoyer un SMS à ce client.<br><br>L’utilisateur reçoit votre réponse automatique de désabonnement définie. |
| Aide | `HELP`<br> `INFO` | L’utilisateur reçoit votre réponse automatique d’aide définie. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Seul le **message avec exactement un mot** est traité (_non sensible_ à la casse). Les mots-clés tels que `STOP PLEASE` seront ignorés sauf si vous avez activé les [désinscriptions vagues][fuzzylink].

Si un destinataire utilise les mots-clés `HELP` ou `INFO`, une réponse est automatiquement déclenchée. Le modèle de SMS pour ces messages de réponse automatique est défini pendant votre [onboarding][oblink] et la période d’acquisition de numéros de téléphone. Notez que vous pouvez continuer à mettre à jour ces réponses après la période d’onboarding initiale.

<!---
{% alert tip %}
<<<<<<< HEAD
Vous souhaitez étendre votre traitement des opt-out ? Essayez [fuzzy opt-out]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/fuzzy_opt_out/), une fonction qui essaye de reconnaitre quand un message entrant indique une intention de opt-out sans contenir un mot-clé de opt-out (désabonnement).
=======
Interested in expanding your opt-out processing? Try [fuzzy opt-out]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/fuzzy_opt_out/), a feature that attempts to recognize when an inbound message does not match an opt-out keyword, but indicates opt-out intent.
>>>>>>> e54fcef14 (1177662|i18n_30_Dec_2022_08_00_01_270_32|1672408832912-GlobalLink Translation)
{% endalert %}
--->

[oblink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[fuzzylink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/fuzzy_opt_out/
