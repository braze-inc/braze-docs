---
nav_title: Infillion
article_title: Infillion
alias: /partners/infillion/
description: "Cet article de référence présente le partenariat entre Braze et Infillion, qui vous permet de perfectionner la pertinence de votre marketing grâce aux données d'emplacement/localisation."
page_type: partner
search_tag: Partner

---

# Infillion

> [Infillion](https://infillion.com/) vous permet de perfectionner la pertinence de votre marketing grâce aux données d'emplacement/localisation. Leur SDK d'emplacement/localisation, associé à un logiciel de géorepérage et à des balises, permet d'offrir des expériences mobiles pertinentes, personnalisées et sensibles à la proximité.

Combinez votre prise en charge des balises ou du géorepérage avec les fonctionnalités de ciblage et d'envoi de messages de Braze pour en savoir plus sur les actions physiques de vos utilisateurs et leur envoyer des messages en conséquence. Cette intégration de partenariat ouvre de nombreux cas d'utilisation pour :

- **Marketing :** Envoyez des messages contextuels pertinents et créez des parcours consommateurs expérientiels.
- **Analyse concurrentielle :** Configurez des déclencheurs autour d'emplacements concurrents pour comprendre les tendances et les habitudes de consommation.
- **Informations sur l’audience :** Comprenez les comportements de visite de vos utilisateurs et segmentez davantage en fonction de ces connaissances.

{% alert note %}
Cette intégration fonctionne de la même manière pour les balises Infillion et les solutions de géorepérage Infillion.
{% endalert %}

## Conditions préalables

| Condition| Description|
| ---| ---|
|  | Un compte gestionnaire d'Infillion est nécessaire pour profiter de ce partenariat. |
|[SDK d'emplacement/localisation d'Infillion](https://docs.gimbal.com/index.html) | Le SDK Infillion Location alimente des expériences mobiles macro et micro emplacement/localisation en utilisant des balises de proximité et des géorepérages qui vous permettent de communiquer plus efficacement avec les utilisateurs de votre application. Le SDK doit être mis en œuvre et les géorepérages (ou balises) configurés. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration SDK

Pour intégrer Braze et Infillion, vous devez mettre en œuvre le SDK d'emplacement/localisation d'Infillion et créer un compte de gestionnaire compte. Les intégrations suivantes pour Android, FireOS et iOS créeront un événement personnalisé unique pour chaque nouvel endroit qu'un utilisateur accède. Ces événements pourront ensuite être utilisés pour le déclenchement et le reciblage de vos campagnes et de vos Canvases.

Si vous prévoyez de créer plus de 50 lieux, nous vous recommandons de créer un événement `Places Entered` personnalisé générique et d'ajouter le nom du lieu en tant que propriété de l'événement. 

1. 
2. 
3. 
4.  
5. Consignez les propriétés de ces événements (nom du lieu, durée du séjour).
6. Utilisez ces propriétés et ces événements pour déclencher des campagnes et des Canvases in Braze. 

