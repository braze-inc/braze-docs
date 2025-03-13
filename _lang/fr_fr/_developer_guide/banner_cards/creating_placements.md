---
nav_title: Création de placements
article_title: Création de placements de cartes-bannières pour le SDK de Braze
hidden: true
description: "Cet article de référence traite des cartes bannières et de l'intégration de cette fonctionnalité dans le SDK de Braze."
platform:
  - iOS
  - Android
  - Web
  
---

# Créer des emplacements pour les cartes bannières

> Avant de lancer une campagne Banner Card dans votre application, vous devrez créer un placement dans le tableau de bord Braze. Les emplacements/localisations sont des emplacements que vous définissez dans votre application et qui peuvent afficher des cartes bannières.

{% alert important %}
Les cartes bannières sont actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé.
{% endalert %}

## Conditions préalables

Il s'agit des versions minimales du SDK pour commencer à utiliser les Banner Cards :

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.6.0 %}

## Création d'un placement

### Étape 1 : Créer un nouveau placement

Allez dans **Settings** > **Banner Cards Placements**, puis sélectionnez **Create Placement**.

![Section Placement des cartes bannières pour créer des ID de placement.]({% image_buster /assets/img/banner_cards/create_placement.png %})

### Étape 2 : Complétez les détails

Donnez un nom à votre placement et attribuez-lui un **ID de placement**. En option, vous pouvez ajouter une description de votre placement.

Travaillez avec votre équipe de marketeurs pour créer cet ID. C'est l'ID auquel vous ferez référence dans le code de votre application, et votre équipe marketing l'utilisera pour attribuer une campagne à l'emplacement/localisation dans votre application. 

{% alert important %}
Évitez de modifier votre ID de placement après le lancement, car cela peut rompre l'intégration avec votre app ou votre site web.
{% endalert %}

![Les détails de placement qui désignent une carte de promotion s'afficheront dans la barre latérale gauche pour les campagnes de promotion des soldes de printemps.]({% image_buster /assets/img/banner_cards/placement_details_example.png %})

Pour savoir comment lancer une campagne de cartes bannières, reportez-vous à la section [Créer une carte bannière]({{site.baseurl}}/create_banner_card/).

## Étapes suivantes

Maintenant que vous avez créé vos emplacements de cartes bannières, vous pouvez :

- [Intégrer les cartes bannières]({{site.baseurl}}/developer_guide/banner_cards/integration/)
- [Créer des cartes bannières]({{site.baseurl}}/create_banner_card/)
