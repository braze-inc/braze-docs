---
nav_title: Étape Message
article_title: Étape Message
alias: "/message_step/"
page_order: 5
page_type: reference
description: "Cet article de référence aborde la façon de créer un message indépendant à l’aide de l’étape Messagerie Canvas."
tool: Canvas

---

# Étape Message

Les étapes Message vous permettent d’ajouter un message indépendant où vous voulez dans votre flux Canvas.

## Créer une étape Message

![][1]{: style="float:right;max-width:19%;margin-left:15px;"}

Pour créer une étape Message, ajoutez une étape à votre Canvas. Puis, utilisez le menu déroulant en haut de la nouvelle étape pour sélectionner **Message**.

Avec une étape Message, tous les utilisateurs ayant franchi l’étape progressent vers l’étape suivante lorsque l’une des conditions suivantes est remplie :
- Un message est envoyé
- Un message n’est pas envoyé, car l’utilisateur n’est pas joignable par un canal
- Un message n’est pas envoyé, car il est en limite de fréquence
- Un message n’est pas envoyé, car il est annulé

![Configurez des paramètres de messages pour une étape Message Canvas, incluant l’option permettant de sélectionner votre canal de message et de personnaliser des paramètres de livraison.][2]{: style="max-width:75%;"} 

L’étape Message comprend également des paramètres pour la livraison intelligente, les remplacements d’heures calmes et la validation de livraison.

L’étape Message vous permet d’activer [Timing Intelligent]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/) avec une option de recours lorsqu’un profil utilisateur n’a pas suffisamment de données pour calculer une heure optimale. Nous conseillons d’activer Timing Intelligent et [Limites de débit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-frequency-capping/) comme contrôle supplémentaire de tout délai entre le moment où les utilisateurs accèdent à l’étape Message et l’envoi réel du message.

Sélectionnez **Utilisation de Timing Intelligent** dans **Paramètres de livraison**. À ce niveau, vous pouvez sélectionner l’heure la plus classique ou une heure de base spécifique. Si l’option Heures calmes est activée, l’étape Message vous permet donc d’ignorer ce paramètre.

Les validations de livraison fournissent un contrôle supplémentaire pour confirmer que votre public répond aux critères de livraison pour l’envoi de message. Ce paramètre est recommandé si les options Heures calmes, Timing Intelligent ou Limitation du taux sont activées. Vous pouvez ajouter un segment ou des filtres supplémentaires pour valider l’heure d’envoi du message.

![Onglet Paramètres de livraison pour les paramètres de l’étape Message. Les heures calmes sont activées et la case pour l’utilisation de Timing Intelligent est cochée pour envoyer le message à une heure optimale. Les validations de livraison sont activées pour valider le public lors de l’envoi du message.][4]{: style="max-width:80%;"}

Pour les étapes Message Canvas, `event_properties` ne sont pas pris en charge. À la place, utilisez `canvas_entry_properties`. Les propriétés d’entrée Canvas sont des propriétés issues de l’événement qui a déclenché le Canvas. Ces propriétés peuvent être uniquement utilisées dans la première étape complète d’un Canvas. Inversement, les propriétés de l’événement proviennent d’un événement ou d’une action qui se produit lorsque l’utilisateur accède à son flux de travail.

## Analytique

Reportez-vous au tableau suivant pour les définitions des métriques de l’étape Message : 

| Métrique | Description |
| --- | --- |
| Entrées | Le nombre d’accès à l’étape. Si votre Canvas est rééligible et qu’un utilisateur accède deux fois à une étape Message, les deux entrées seront enregistrées. |
| Poursuivre vers l’étape suivante | Le nombre d’entrées pour accéder à l’étape suivante dans le Canvas. |
| Envois | Le nombre total de messages envoyés par l’étape. Si votre Canvas est rééligible et qu’un utilisateur accède deux fois à une étape Message, les deux entrées seront enregistrées. |
| Destinataires uniques | Le nombre d’utilisateurs ayant reçu des messages depuis cette étape. |
| Événement de conversion primaire | Le nombre de fois où un événement défini se produit après l’interaction ou la consultation d’un message reçu d’une campagne Braze. Vous définissez cet événement lors de la création de la campagne. |
| Revenue | Le revenu total en dollars de destinataires de campagne dans la fenêtre de conversion principale définie. |
{: .reset-td-br-1 .reset-td-br-2}

![][3]{: style="max-width:20%;"}


[1]: {% image_buster /assets/img/canvas_components/message_step1.png %}
[2]: {% image_buster /assets/img/canvas_components/message_step2.png %}
[3]: {% image_buster /assets/img/canvas_components/message_step3.png %}
[4]: {% image_buster /assets/img/canvas_components/message_step4.png %}
