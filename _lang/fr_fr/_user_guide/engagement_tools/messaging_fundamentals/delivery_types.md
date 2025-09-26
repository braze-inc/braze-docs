---
nav_title: Types de réception/distribution
article_title: Types de réception/distribution
page_order: 5
page_type: reference
description: "Cet article de référence décrit les types de réception/distribution des campagnes, les types d'entrée des Canevas et les fonctionnalités basées sur le temps lors de la configuration d'une campagne ou d'un Canvas."
tool:
    - Campaigns
    - Canvas
---

# Planification de votre message

> Dans Braze, vous pouvez planifier votre message de trois manières différentes : programmée, basée sur une action et déclenchée par l'API. Le choix du moment et de la manière dont votre message est transmis est crucial pour l'élaboration d'un message efficace. 

## Types de réception/distribution

Pour les campagnes, le type de réception/distribution détermine le moment où vos utilisateurs entreront dans votre campagne et le moment où elle sera envoyée. Étant donné qu'un canvas est créé comme un parcours continu de l'utilisateur, le concept d'envoi de messages d'une planification est désigné comme un type d'entrée.

| Réception/distribution<nobr> et types d'entrée | Description                                                                                                                                                                                                                                                                                                                                      |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Planification**       | Ce type de planification est conçu pour des messages ponctuels que vous souhaitez envoyer immédiatement, tels que des campagnes sur un événement d'actualité. <br><br>Lorsque vous envoyez des messages de test destinés uniquement à vous-même ou à votre équipe, cette option vous permet de les délivrer immédiatement.                                                                                   |
| **Par événement**    | Les messages de réception/distribution basés sur l'action, ou les campagnes déclenchées par un événement et les Canvases, sont très efficaces pour les messages transactionnels ou basés sur l'accomplissement. Vous pouvez les déclencher pour qu'ils soient envoyés après qu'un utilisateur a accompli un certain événement au lieu d'envoyer votre message certains jours.                                                                                           |
| **Déclenchement par API**   | Les messages déclenchés par l'API vous permettent de gérer le texte des messages, les tests multivariés et les règles de rééligibilité dans le tableau de bord de Braze, tout en déclenchant la réception/distribution de ce contenu à partir de vos propres serveurs et systèmes. <br><br>La demande API pour déclencher le message peut également inclure des données supplémentaires à modéliser dans le message en temps réel. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Options basées sur le temps

{% tabs %}
{% tab campagne %}
Vous pouvez choisir parmi les options suivantes lorsque vous utilisez la réception/distribution :

- Envoyer dès que la campagne est lancée
- Envoyer à un moment spécifié
- [Timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/)
{% endtab %}

{% tab canvas %}
Avec une livraison planifiée, les utilisateurs accéderont selon un calendrier, de la même façon que vous planifieriez une campagne. Vous pouvez inscrire des utilisateurs à un Canvas dès son lancement ou à un moment précis.

#### Périodes désignées

Vous pouvez choisir d'envoyer votre Canvas à une fréquence d'entrée spécifique, notamment une seule fois, tous les jours, toutes les semaines ou tous les mois. Pour les toiles dont la réception/distribution est planifiée de manière récurrente, vous pouvez définir la récurrence de manière à permettre aux utilisateurs d'entrer dans la toile jusqu'à 30 fois.
{% endtab %}
{% endtabs %}

### Options basées sur l'action

{% tabs %}
{% tab campagne %}
La réception/distribution par événement permet d'envoyer des campagnes aux utilisateurs qui effectuent une action spécifique. Après cette action, vous pouvez décider du moment où la campagne sera envoyée : immédiatement, après un certain temps, à un moment précis ou à un moment ultérieur.
{% endtab %}

{% tab canvas %}
Les options basées sur l'action déterminent les actions (ou déclencheurs) qu'un utilisateur doit effectuer pour entrer dans un canvas et à quel moment précis il est autorisé à commencer à entrer. Par exemple, vous pouvez évaluer vos utilisateurs en fonction des actions suivantes :

- Ouvrir votre application
- Ajouter une adresse e-mail
- Saisir une localisation

#### Fenêtre d'entrée

La fenêtre d'entrée de votre Canvas détermine quels utilisateurs peuvent entrer dans le Canvas à l'heure de début désignée (et à l'heure de fin facultative). Comme pour les campagnes basées sur l'action, vous pouvez choisir d'inscrire les utilisateurs dans leur fuseau horaire local.
{% endtab %}
{% endtabs %}

### Options de déclencheur API

{% tabs %}
{% tab campagne %}
Lorsque vous sélectionnez l'option de réception/distribution déclenchée par l'API, vous recevez un ID de campagne qui vous permet d'identifier la campagne à envoyer à l'aide de l' [endpoint`/campaigns/trigger/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#prerequisites).
{% endtab %}

{% tab canvas %}
Lorsque vous sélectionnez le type d'entrée déclenchée par l'API, vous recevez un ID Canvas qui vous permet d'identifier la campagne à envoyer à l'aide de l' [endpoint`/canvas/trigger/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).
{% endtab %}
{% endtabs %}
