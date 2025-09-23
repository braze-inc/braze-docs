---
nav_title: Narvar
article_title: Narvar
description: "Découvrez comment intégrer Narvar à Braze."
alias: /partners/narvar/
page_type: partner
search_tag: Partner
---

# Narvar

> Narvar est une plateforme post-achat qui renforce la fidélité des clients grâce au suivi des commandes, aux mises à jour des livraisons et à la gestion des retours. L'intégration de Braze et Narvar permet aux marques d'exploiter les événements de notification de Narvar pour déclencher des messages directement depuis Braze, en tenant les clients informés grâce à des mises à jour opportunes.

## Conditions préalables

| Condition           | Descriptif                                                                                   |
|-----------------------|-----------------------------------------------------------------------------------------------|
| Compte Narvar        | Un compte Narvar est nécessaire pour bénéficier de ce partenariat.                           |
| Clé d'API REST Braze    | Une clé API REST Braze avec l'autorisation `messages.send`. Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**.                                            |
| Endpoint REST Braze   | L’[URL de votre endpoint REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), qui dépend de l'URL de votre instance Braze.         |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Fonctionnalités prises en charge

|Type|Fonctionnalités prises en charge|
|-------|----------|
| Notifications | \- Anticipation de la réception/distribution<br>\- Retard de la porteuse<br>\- Livré standard |
| Canaux | Notifications push |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Si vous êtes intéressé par d'autres types ou canaux de notification, veuillez contacter votre CSM Braze et Narvar.
{% endalert %}

## Détails de l'intégration

Pour chaque événement de notification, Narvar envoie une demande au point d'extrémité de Braze [`/messaging/send`]({{site.baseurl}}/api/endpoints/messaging) afin d'envoyer un message push à chaque consommateur abonné.

Narvar est responsable de la configuration des charges utiles de notification push pour chaque message. Actuellement, Teams ne dispose pas d'une interface de conception intégrée pour les notifications push. Son équipe collaborera donc avec la vôtre pour déterminer et définir les exigences en matière de charge utile. Ces données utiles peuvent être personnalisées dans la même mesure que celles envoyées par votre propre système, y compris la prise en charge de marqueurs substitutifs à contenu variable, tels que les données relatives aux commandes et les détails concernant les consommateurs.

## Démarrer avec l'intégration Braze-Narvar

1. **Contactez votre CSM Narvar** pour exprimer votre intérêt pour l'intégration.
2. **Désignez des environnements Braze** pour la mise en place et la production.
3. **Générer une clé API** dans Braze pour l'usage de Narvar.
4. **Générer des clés de campagne** dans Braze si nécessaire.
5. **Fournir les clés d'API et de campagne** à Narvar par le biais d'un lien unique sécurisé.
6. **Partagez les détails de la charge utile de la notification push** pour finaliser la configuration.
