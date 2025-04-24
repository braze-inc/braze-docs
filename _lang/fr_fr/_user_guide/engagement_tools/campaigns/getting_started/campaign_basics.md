---
nav_title: Notions de base des campagnes
article_title: Notions de base des campagnes
page_order: 1
page_type: reference
description: "Le présent article de référence aborde les fondamentaux des campagnes, notamment diverses questions que vous devez vous poser lorsque vous configurez votre première campagne."
tool: Campaigns

---

# Notions de base des campagnes

> Le présent article de référence aborde les fondamentaux des campagnes, notamment diverses questions que vous devez vous poser lorsque vous configurez votre première campagne.

## Comprendre la structure d’une campagne

Avant d’aborder les détails plus précis de l’implémentation des campagnes, nous allons identifier les détails clés permettant de comprendre comment les campagnes fonctionnent sur les différents canaux de communication.

Les campagnes sont une étape de message unique pour contacter vos utilisateurs sur les canaux, appelés généralement canaux de communication. Ces canaux de communication comprennent les cartes de contenu, les e-mails, les messages in-app, les notifications push, les SMS et MMS et les webhooks. En comprenant la localisation de vos consommateurs, vous pouvez tirer parti des canaux de communication appropriés pour communiquer.

## Création du parcours client

Étant donné que les campagnes peuvent être créées seulement en fonction du canal de communication, vous pouvez utiliser les cinq W de visualisation pour essayer d’identifier et de conceptualiser vos buts et vos stratégies d’engagement client.

### Le « quoi » : Nommez votre campagne

> Qu’essayez-vous de faire faire ou comprendre à votre utilisateur ?

Ne sous-estimez jamais le pouvoir du nom. Braze est conçu pour la collaboration, c’est donc le moment idéal pour évaluer la façon dont vous communiquez les objectifs à votre équipe. Pour en savoir plus sur les parcours clients, consultez notre cours d'apprentissage Braze sur [le mappage des cycles de vie des utilisateurs](https://learning.braze.com/mapping-customer-lifecycles)!

### Le « quand » : Créer des conditions de démarrage

> Quand un client sera-t-il confronté à cette campagne ? 

Les utilisateurs peuvent entrer dans votre campagne de trois manières : à une date et heure donnée (planifiée), lorsqu’ils effectuent une action donnée (par événement) ou lorsqu’ils effectuent une action déclenchant un appel API (déclenchée par API). 

La livraison planifiée implique d’ajuster vos campagnes pour qu’elles soient envoyées à un moment particulier et, optionnellement, à une cadence donnée. Les campagnes par événement répondent à des comportements des clients spécifiques, lorsqu’ils se produisent en temps réel. Ils peuvent comprendre : effectuer un achat ou interagir avec une autre campagne. Des campagnes déclenchées par l'API peuvent être mises en place pour déterminer les actions clés des clients sur votre plateforme qui, une fois réalisées, déclencheront un appel API vers Braze et enverront vos campagnes.

### Le « qui » : Sélectionnez une audience d’entrée

> Qui (Who) essayez-vous de joindre ? 

Vous pouvez utiliser des [segments]({{site.baseurl}}/user_guide/engagement_tools/segments) prédéfinis pour cibler les utilisateurs en fonction de leurs caractéristiques démographiques, comportementales ou techniques et de leurs actions. Ajoutez plus de filtres lorsque vous construisez votre campagne pour ajuster encore plus vos segments. Seuls les utilisateurs répondant à ces critères d’audience cible peuvent accéder au parcours. Consultez ce tableau pour obtenir un sommaire rapide des types de filtres disponibles.

| Filtre | Description |
|---|---|
| Données personnalisées | Segmentez les utilisateurs en fonction d’événements et d’attributs que vous définissez. Vous pouvez utiliser des fonctionnalités spécifiques pour votre produit. |
| Activité de l’utilisateur | Segmentez les clients sur la base de leurs actions et de leurs achats. |
| Reciblage | Segmentez des clients qui ont envoyé, reçu ou interagi avec des campagnes précédentes. |
| Activité de marketing | Segmentez les clients en fonction de comportements universels, tels que le dernier engagement ou les campagnes reçues. |
| Attributs utilisateur | Segmentez les clients en fonction de leurs caractéristiques et attributs constants. |
| Attribution d’installation | Segmenter les clients par leur première source, groupe d'annonces, campagne ou annonce. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Le « pourquoi » : Identifier des événements de conversion

> Pourquoi créez-vous cette campagne ? 

Il est toujours important d’avoir un objectif défini en tête et les campagnes vous permettent de comprendre comment vous vous situez par rapport aux KPI tels que l’engagement de session, les achats et les événements personnalisés. En sélectionnant au moins un [événement de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), vous aurez la possibilité de comprendre les performances de votre campagne.

### Le « où » : Trouver mon audience

> Où puis-je atteindre au mieux mon audience ?

C’est l’endroit où nous déterminons quels canaux de communication sont les plus pertinents pour votre parcours utilisateur. Dans l’absolu, nous souhaiterions atteindre vos utilisateurs là où ils sont les plus actifs.

### Le « comment » : Consolider l’expérience

> Comment puis-je créer ma campagne après avoir identifié les cinq W ?

Envisagez de mettre en place des variantes et des tests A/B alors que vous devenez plus averti dans le domaine de la création de campagnes. Considérez que les campagnes prennent en charge jusqu’à huit variantes avec un groupe de contrôle. Utilisez vos analyses de campagne pour effectuer des choix bien renseignés en construisant votre campagne, pour tout ajuster depuis votre audience segmentée à votre contenu de communication proprement dit.

