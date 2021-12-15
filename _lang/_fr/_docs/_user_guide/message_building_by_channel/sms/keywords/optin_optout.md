---
nav_title: Opt-In / Opt-Out
article_title: Mots clés "Opt-In/Opt-out" SMS
page_order: 0
description: "Cet article de référence décrit comment Braze traite les mots clés de base opt-in et opt-out pour la messagerie SMS."
page_type: Référence
tool:
  - Tableau de bord
channel:
  - SMS
---

# Mots clés opt-in et opt-out

Le règlement exige qu'il y ait des réponses à toutes les réponses aux mots clés opt-in, opt-out et help/info. Braze traite automatiquement les messages _exacts, mot unique et insensible à la casse_ suivants mise à jour automatique du [statut du groupe d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) pour l'utilisateur et son numéro de téléphone associé sur toutes les demandes entrantes.

## Aperçu des mots clés

Braze traitera automatiquement les mots-clés suivants et mettra à jour l'état du groupe d'abonnement pour le numéro de téléphone sur toutes les demandes entrantes. Notez que ces mots-clés et réponses par défaut peuvent également être personnalisés.

| Type de texte  | Keyword                                                                                              | Changement                                                                                                                                                                                                                                                                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Opt-in         | `COMMENCER`<br> `OUI`<br> `INSTALLER`                                                    | Toute requête entrante avec l'un de ces mots-clés `Opt-In` entraînera un changement d'état du groupe d'abonnement à `inscrit`. De plus, le groupement de numéros associés à ce groupe d'abonnement pourra maintenant envoyer un message SMS à ce client. <br><br>L'utilisateur recevra votre réponse automatique d'opt-in.        |
| Désinscription | `STOP`<br> `STOPALL`<br> `DEBONNER`<br> `ANNULER`<br> `END`<br> `QUIT` | Toute requête entrante avec l'un de ces mots-clés `Opt-In` entraînera un changement d'état du groupe d'abonnement à `désabonné`. De plus, le groupement de numéros associés à ce groupe d'abonnement ne pourra plus envoyer de SMS à ce client.<br><br>L'utilisateur recevra votre réponse automatique de désinscription définie. |
| Aide           | `AIDEZ`<br> `INFOS`                                                                            | L'utilisateur recevra votre réponse automatique d'aide définie.                                                                                                                                                                                                                                                                               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Seul le message __exact, un mot simple__ sera traité (cas _insensible_). Les mots-clés tels que `STOP VEUILLEZ` seront ignorés.

Si un destinataire utilise les mots-clés `AIDE` ou `INFO`, une réponse sera déclenchée automatiquement. Le modèle de SMS pour ces messages de réponse automatique sera défini pendant votre [période d'intégration][oblink] et de numéro de téléphone de la période d'achat. Notez que vous pouvez continuer à mettre à jour ces réponses après la période d’intégration initiale.

[oblink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
