---
nav_title: Création de campagnes
article_title: Créer des campagnes de cartes bannières
alias: "/create_banner_card/"
description: "Cet article de référence explique comment créer et envoyer des cartes bannières à l'aide des campagnes Braze."
page_type: reference
---

# Créer des campagnes de cartes bannières

> Découvrez comment créer des cartes bannières lorsque vous créez une campagne dans Braze. Pour plus d'informations générales, voir [À propos des cartes bannières]({{site.baseurl}}/developer_guide/banner_cards/).

{% alert important %}
Les cartes bannières sont actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé.
{% endalert %}

## Conditions préalables {#prerequisite-determine-placement}

Il s'agit des versions minimales du SDK pour commencer à utiliser les Banner Cards :

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Création d'une campagne de cartes bannières

{% multi_lang_include banner_cards/creating_placements.md %}

### Étape 2 : Créer une campagne

1. Allez dans **Messagerie** > **Campagnes** et sélectionnez **Créer une campagne**.
2. Sélectionnez **Banner Card**.
3. Donnez un nom clair et significatif à votre campagne.
4. Ajoutez des Teams et des tags si nécessaire. Les balises facilitent la recherche et l’identification des campagnes, et la création de rapports. Par exemple, lorsque vous utilisez le générateur de rapports, vous pouvez filtrer par les étiquettes pertinentes.
5. Sélectionnez le placement que vous avez précédemment créé pour l'associer à votre campagne.
6. Ajoutez des variantes si nécessaire. Vous pouvez choisir un type de message et une mise en page différents pour chacun d'entre eux. Pour plus d'informations sur les variantes, reportez-vous au [test multivarié et au test A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

### Étape 2 : Composer un message

Pour composer votre carte bannière, sélectionnez **Modifier le message.** Ici, vous pouvez donner un style à la carte et définir le comportement au clic.

#### Étape 2.1 : Style de la carte {#styles}

Vous pouvez glisser-déposer des blocs et des lignes dans la zone du canvas pour commencer à créer votre message. Pour personnaliser les propriétés de l'arrière-plan de votre message, les paramètres de la bordure, etc., sélectionnez **Styles**. Si vous souhaitez uniquement personnaliser le style d'un bloc ou d'une ligne spécifique, sélectionnez-le pour apporter des modifications.

![Panneau de style du compositeur Banner Card.]({% image_buster /assets/img/banner_cards/banner_card_styles.png %})

#### Étape 2.2 : Définir le comportement au clic

Lorsqu'un client clique sur un lien dans la carte-bannière, vous pouvez choisir de le faire naviguer plus profondément dans votre appli ou de le rediriger vers une autre page web. En outre, vous pouvez choisir d'[enregistrer un attribut ou un événement personnalisé]({{site.baseurl}}/developer_guide/analytics/), qui mettra à jour le profil de votre client avec des données personnalisées lorsqu'il cliquera sur la carte-bannière.

### Étape 3 : Définir la priorité de la carte {#set-card-priority}

Lorsque plusieurs campagnes font référence au même ID de placement, les cartes sont affichées par ordre de priorité. Par défaut, les cartes bannières nouvellement créées sont réglées sur une priorité moyenne, mais vous pouvez régler manuellement la priorité sur élevée, moyenne ou faible. Si plusieurs cartes ont le même niveau de priorité, la carte la plus récente sera affichée en premier.

Pour définir la priorité d'une carte :

1. Sélectionnez **Trieur de priorités**.
2. Glissez-déposez les campagnes pour les ordonner avec la bonne priorité.
3. Sélectionnez **Appliquer le tri.**

### Étape 3 : Finir de créer la campagne

Terminez de créer votre campagne en complétant les éléments suivants :

| Option                    | Description |
|---------------------------|-------------|
| **Durée de la campagne** | Choisissez une date et une heure de début pour votre campagne de cartes bannières. Par défaut, les cartes bannières durent indéfiniment. Vous pouvez modifier cela en sélectionnant **Heure de fin** et en spécifiant une date et une heure de fin. |
| **Cibler des utilisateurs** | Ciblez les utilisateurs en choisissant des segments ou des filtres pour réduire votre audience. Vous obtiendrez automatiquement un aperçu de la population approximative du segmentation. L'appartenance exacte à un segment est calculée juste avant l'envoi du message. |
| **Événements de conversion** | Suivez la fréquence à laquelle les utilisateurs effectuent des actions spécifiques après avoir reçu une campagne. Vous pouvez définir des événements de conversion avec une fenêtre de 30 jours maximum pour compter l'action comme une conversion. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Étape 4 : Test et lancement

Après avoir créé votre campagne, testez-la et examinez-la pour vous assurer qu'elle fonctionne comme prévu. Lorsque vous êtes prêt, lancez votre campagne de cartes bannières !
