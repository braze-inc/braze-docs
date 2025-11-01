---
nav_title: "Utilisateurs de l'envoi de messages"
article_title: Envoi de messages aux utilisateurs LINE
page_order: 2
description: "Cet article de référence explique comment chatter avec les utilisateurs en utilisant des campagnes modélisées et des Canvases."
page_type: reference
channel:
 - LINE
alias: /line/messaging_users/
---

# Envoi de messages aux utilisateurs de LINE

> LINE est un canal de communication bidirectionnelle. Vous pouvez aller au-delà de l'envoi de messages aux utilisateurs et engager des conversations avec eux en utilisant des campagnes modélisées et des Canevas. Cet article aborde les détails de l'envoi de messages aux utilisateurs, tels que la définition de mots déclencheurs pour les messages entrants et les réponses non reconnues.

Il existe plusieurs méthodes pour converser avec les utilisateurs par le biais de LINE, comme l'utilisation des mots déclencheurs de LINE. Vous pouvez également utiliser des appels à l'action (CTA) pour encourager l'engagement de l'utilisateur avec votre envoi de messages LINE.

## Déclencheurs basés sur l'action

Vous pouvez créer des campagnes et des canevas qui démarrent, se ramifient et sont modifiés en cours de route lorsque vous recevez un message LINE entrant (un message envoyé par un utilisateur) qui contient un mot déclencheur. Veillez à choisir des mots déclencheurs qui correspondent à ce que vous attendez des utilisateurs.

### Campagne

Définissez vos mots déclencheurs lors de la planification d'une campagne de réception/distribution basée sur des actions.

\![Déclencheur basé sur l'action "Envoyer cette campagne aux utilisateurs qui ont envoyé une LINE entrante au groupe d'abonnement où se trouve le corps du message" et un champ vide.]({% image_buster /assets/img/line/trigger_word_campaign.png %})

### Canevas

Placez vos mots déclencheurs dans les [parcours d'action de]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths) votre Canvas.

\![Parcours d'action avec un déclencheur de "Envoyer cette campagne aux utilisateurs qui ont envoyé une LINE entrante au groupe d'abonnement où se trouve le corps du message" et un champ vide.]({% image_buster /assets/img/line/trigger_word_canvas.png %})

### Exigences

Chaque lettre de votre mot déclencheur doit être mise en majuscule lorsque vous créez votre campagne ou votre Canvas, même si Braze n'exige pas que les mots déclencheurs entrants soient mis en majuscules. Par exemple, si votre mot déclencheur est "JOIN2023", un message entrant de "jOin2023" déclenchera toujours le Canvas ou la campagne.

Si aucun mot déclencheur n'est spécifié, la campagne ou le canvas sera exécuté pour *tous les* messages LINE entrants. Il s'agit notamment des messages dont les phrases correspondent à celles des campagnes et des Phrasese actives, auquel cas l'utilisateur recevra deux messages LINE.

## Réponses non reconnues

Vous devez inclure une option de déclencheur pour les réponses non reconnues sur les toiles interactives. Cela permet d'informer les utilisateurs des messages-guides disponibles (ou mots déclencheurs) et de définir leurs attentes à l'égard du canal.

### Création d'un déclencheur pour les réponses non reconnues

Après avoir créé des groupes d'action pour les phrases de filtrage personnalisées, ajoutez un autre groupe d'action au parcours d'action pour **Envoyer un message LINE**, et ne vérifiez pas **Où se trouve le corps du message.** Cela permet d'enregistrer toutes les réponses non reconnues de l'utilisateur, à l'instar d'une clause "else".

Pour ce message, vous devez envoyer un message LINE informant l'utilisateur que ce canal n'est pas surveillé par un humain et, si nécessaire, le guider vers un canal d'assistance.

