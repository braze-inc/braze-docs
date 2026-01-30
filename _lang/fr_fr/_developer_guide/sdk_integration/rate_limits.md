---
page_order: 2.0
nav_title: Limites de débit
article_title: Limites de débit du SDK Braze
description: "Découvrez la limite de débit intelligente côté client du SDK Braze qui optimise l'autonomie de la batterie, réduit l'utilisation de la bande passante et garantit une réception/distribution fiable des données."
---

# Limites de débit du SDK Braze

> Découvrez la limite de débit intelligente côté client du SDK Braze qui optimise l'autonomie de la batterie, réduit l'utilisation de la bande passante et garantit une réception/distribution fiable des données.

## Comprendre les limites de débit du SDK

La limitation du débit du SDK de Braze utilise les fonctionnalités suivantes pour optimiser les performances, minimiser l'épuisement de la batterie, réduire l'utilisation des données et assurer une réception/distribution fiable des données :

### Traitement asynchrone

Le SDK de Braze utilise un algorithme de compartiment à jetons pour la limite de débit. Cette approche permet des rafales d'activité tout en maintenant un contrôle des taux à long terme. Au lieu de traiter les demandes dans une file d'attente stricte, le compartiment à jetons fonctionne de manière asynchrone :

- **Génération de jetons**: Les jetons sont réapprovisionnés à un rythme régulier dans le compartiment.
- **Traitement des demandes**: Tout appel au SDK qui arrive lorsqu'un jeton est disponible est traité immédiatement, indépendamment de l'arrivée des autres appels.
- **Pas de commande stricte**: Les demandes ne font pas la queue ; plusieurs appels peuvent se disputer le prochain jeton disponible.
- **Traitement des rafales**: De courtes périodes d'activité sont autorisées si suffisamment de jetons sont disponibles au moment des demandes.
- **Contrôle des taux**: Le débit à long terme est limité par le taux de réapprovisionnement des jetons.

Ce flux asynchrone permet au SDK de répondre rapidement à la capacité disponible du réseau tout en maintenant des niveaux de trafic globaux prévisibles.

### Limite de débit adaptative

Le SDK de Braze peut ajuster les limites de débit en temps réel pour protéger l'infrastructure du réseau et maintenir des performances optimales. Cette approche :

- **Prévient la surcharge**: Ajuste les limites pour éviter la congestion du réseau.
- **Optimise les performances**: Assurer le bon fonctionnement du SDK dans des conditions variables.
- **Répond aux conditions**: S'adapte en fonction du réseau actuel et des habitudes d'utilisation.

{% alert note %}
Les limites s'adaptant en temps réel, la taille exacte des compartiments et les valeurs statiques ne sont pas fournies. Elles peuvent varier en fonction des conditions du réseau et de l'utilisation.
{% endalert %}

### Optimisation des réseaux

Le SDK de Braze crée plusieurs comportements intégrés pour améliorer l'efficacité, réduire l'utilisation de la batterie et gérer des conditions de réseau variables :

- **Dosage automatique**: Met les événements en file d'attente et les envoie par lots efficaces.
- **Comportement conscient du réseau**: Ajuste les taux de rinçage en fonction de la qualité de la connectivité.
- **Optimisation de la batterie**: Minimise les réveils radio et les appels réseau.
- **Dégradation progressive**: Maintien de la fonctionnalité en cas de mauvaises conditions de réseau.
- **Connaissance de l'arrière-plan et du premier plan**: Optimise le comportement au fur et à mesure que le cycle de vie de l'application évolue.

## Bonnes pratiques

Suivez ces bonnes pratiques pour éviter les problèmes de limite de débit :

| Faites ceci | Pas ceci |
| --- | --- |
| Suivre les actions et les jalons significatifs de l'utilisateur | Suivez chaque interaction mineure ou événement de l'interface utilisateur |
| N'actualisez le contenu qu'en cas de nécessité | Actualiser le contenu à chaque événement utilisateur (comme les événements de défilement) |
| Laissez le SDK gérer automatiquement la mise en lots | Forcer la transmission immédiate des données (sauf en cas d'absolue nécessité) |
| Concentrez-vous sur les événements qui apportent une valeur ajoutée à l'analyse/analytique. | Appeler les méthodes du SDK en succession rapide sans tenir compte de la fréquence |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Obtenir de l'aide

Si vous rencontrez des problèmes de limite de débit du SDK, examinez les méthodes de mise en réseau suivantes :

- `requestImmediateDataFlush()`
- `requestContentCardsRefresh()`
- `refreshFeatureFlags()`
- `logCustomEvent()`
- `logPurchase()`

Lorsque vous contactez [support@braze.com](mailto:support@braze.com), veuillez inclure les détails suivants pour chacune des méthodes du SDK de mise en réseau que vous utilisez :

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
