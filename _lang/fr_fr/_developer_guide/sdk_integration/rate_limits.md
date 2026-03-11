---
page_order: 2.0
nav_title: Limites de débit
article_title: Limites de débit du SDK Braze
description: "Découvrez la limite de débit intelligente côté client du SDK Braze, qui optimise l'autonomie de la batterie, réduit l'utilisation de la bande passante et garantit une réception/distribution fiable des données."
---

# Limites de débit du SDK Braze

> Découvrez la limite de débit intelligente côté client du SDK Braze, qui optimise l'autonomie de la batterie, réduit l'utilisation de la bande passante et garantit une réception/distribution fiable des données.

## Comprendre les limites de débit du SDK

La limite de débit du SDK Braze utilise les fonctionnalités suivantes pour optimiser les performances, minimiser la consommation de batterie, réduire l'utilisation des données et garantir une réception/distribution fiable des données :

### Traitement asynchrone

Le SDK Braze utilise un algorithme de type « token bucket » pour établir la limite de débit. Cette approche permet des pics d'activité tout en maintenant un contrôle à long terme du rythme cardiaque. Au lieu de traiter les requêtes dans une file d'attente stricte, le token bucket fonctionne de manière asynchrone :

- **Génération de jetons** : Les jetons sont réapprovisionnés à un rythme régulier dans le compartiment.
- **Traitement des demandes** : Tout appel SDK qui arrive lorsqu'un jeton est disponible est traité immédiatement, indépendamment du moment où les autres appels sont arrivés.
- **Aucun ordre strict** : Les requêtes ne sont pas mises en attente ; plusieurs appels peuvent entrer en concurrence pour le prochain jeton disponible.
- **Gestion des rafales** : De courtes périodes d'activité sont autorisées si un nombre suffisant de jetons est disponible au moment de la demande.
- **Contrôle du taux** : Le débit à long terme est limité par le taux de réapprovisionnement régulier des jetons.

Ce flux asynchrone permet au SDK de réagir rapidement à la capacité réseau disponible tout en maintenant des niveaux de trafic globaux prévisibles.

### Limitation adaptative du débit

Le SDK Braze peut ajuster les limites de débit en temps réel afin de protéger l'infrastructure réseau et de maintenir des performances optimales. Cette approche :

- **Empêche la surcharge** : Adjust les limites afin d'éviter la congestion du réseau.
- **Optimise les performances** : Assure le bon fonctionnement du SDK dans diverses conditions.
- **Répond aux conditions** suivantes : S'adapte en fonction du réseau actuel et des habitudes d'utilisation.

{% alert note %}
Étant donné que les limites s'adaptent en temps réel, les tailles exactes des compartiments et les valeurs statiques ne sont pas fournies. Ils peuvent varier en fonction des conditions du réseau et de l'utilisation.
{% endalert %}

### Optimisations du réseau

Le SDK Braze intègre plusieurs fonctionnalités visant à améliorer l'efficacité, réduire la consommation de batterie et gérer les conditions réseau variables :

- **Dosage automatique** : Met les événements de la file d'attente et les envoie par lots de manière efficace.
- **Comportement conscient du réseau** : Adjust les débits de chasse en fonction de la qualité de la connexion.
- **Optimisation de la batterie** : Réduit au minimum les réveils radio et les appels réseau.
- **Dégradation gracieuse** : Maintient la fonctionnalité même lorsque les conditions réseau sont défavorables.
- **Conscience de l'arrière-plan/du premier plan** : Optimise le comportement à mesure que le cycle de vie de l'application évolue.

## Bonnes pratiques

Veuillez suivre ces bonnes pratiques afin d'éviter les problèmes liés aux limites de débit :

| Veuillez procéder de la manière suivante | Pas ceci |
| --- | --- |
| Suivez les actions significatives des utilisateurs et les jalons importants. | Suivez chaque interaction mineure ou événement de l'interface utilisateur. |
| Veuillez actualiser le contenu uniquement lorsque cela est nécessaire. | Actualiser le contenu à chaque action de l'utilisateur (comme les événements de défilement) |
| Veuillez laisser le SDK gérer automatiquement le traitement par lots. | Forcer la transmission immédiate des données (sauf en cas d'absolue nécessité) |
| Concentrez-vous sur les événements qui apportent une valeur ajoutée à l'analyse/analytique. | Appelez les méthodes SDK rapidement les unes après les autres sans tenir compte de la fréquence. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Obtenir de l'aide

Si vous rencontrez des problèmes liés à la limite de débit du SDK, veuillez examiner les méthodes de mise en réseau suivantes :

- `requestImmediateDataFlush()`
- `requestContentCardsRefresh()`
- `refreshFeatureFlags()`
- `logCustomEvent()`
- `logPurchase()`

Lorsque vous contactez [support@braze.com](mailto:support@braze.com), veuillez inclure les informations suivantes pour chacune des méthodes SDK réseau que vous utilisez :

```plaintext
Method name:

Frequency:
[Describe how often this is called, e.g., at every app launch, once per session]

Trigger/context:
[Describe what causes it to be called, e.g., button click, scroll event]

Code snippet:  
[Paste the exact code where this method is called, one snippet for each time it is called]

Patterns in user flow that may cause bursts or excessive calls:
[Describe here]
```
