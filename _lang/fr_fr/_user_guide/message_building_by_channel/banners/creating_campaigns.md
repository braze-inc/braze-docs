---
nav_title: Création de campagnes
article_title: Créer des campagnes de bannières dans Braze
page_order: 1
description: "Cet article de référence explique comment créer, composer, configurer et envoyer des bannières à l'aide des campagnes Braze."
tool:
  - Campaigns
channel:
  - banners
---

# Création de campagnes de bannières

> Découvrez comment créer des bannières lorsque vous créez une campagne dans Braze. Pour plus d'informations générales, reportez-vous à la section [À propos des bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners).

## Conditions préalables

Avant de pouvoir lancer votre campagne Banner, votre équipe de développement devra implémenter [des campagnes dans votre application ou votre site web]({{site.baseurl}}/developer_guide/banners/creating_placements/). Dans l'intervalle, vous pouvez toujours rédiger votre campagne Banner, mais vous ne pourrez pas la lancer.

## Créer une campagne de bannières

{% multi_lang_include banners/creating_placements.md section="user" %}

### Étape 2 : Créer une campagne

1. Allez dans **Messagerie** > **Campagnes** et sélectionnez **Créer une campagne**.
2. Sélectionnez la **bannière**.
3. Donnez un nom clair et significatif à votre campagne.
4. Ajoutez des Teams et des tags si nécessaire. Les balises facilitent la recherche et l’identification des campagnes, et la création de rapports. Par exemple, lorsque vous utilisez le générateur de rapports, vous pouvez filtrer par les étiquettes pertinentes.
5. Sélectionnez le placement que vous avez précédemment créé pour l'associer à votre campagne.
6. Ajoutez des variantes si nécessaire. Vous pouvez choisir un type de message et une mise en page différents pour chacun d'entre eux. Pour plus d'informations sur les variantes, reportez-vous au [test multivarié et au test A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing).

### Étape 3 : Composer une bannière {#compose-a-banner}

Pour composer votre bannière, sélectionnez **Modifier le message.** Ici, vous pouvez créer la bannière et définir le comportement au clic. 

#### Étape 3.1 : Style de la bannière

Vous pouvez glisser-déposer des blocs et des lignes dans la zone du canvas pour commencer à créer votre message.

Pour personnaliser les propriétés de l'arrière-plan de votre message, les paramètres de la bordure, etc., sélectionnez **Styles**. Si vous souhaitez uniquement personnaliser le style d'un bloc ou d'une ligne spécifique, sélectionnez-le pour apporter des modifications.

![Panneau de style du compositeur de bannières.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### Étape 3.2 : Définir le comportement au clic

Lorsqu'un utilisateur clique sur un lien dans la bannière, vous pouvez choisir de le faire naviguer plus profondément dans votre application ou de le rediriger vers une autre page web. En outre, vous pouvez choisir d' [enregistrer un attribut ou un événement personnalisé]({{site.baseurl}}/developer_guide/analytics/), qui mettra à jour le profil de votre utilisateur avec des données personnalisées lorsqu'il cliquera sur la bannière.

{% alert important %}
{::nomarkdown}
Le comportement au clic peut être remplacé si un élément spécifique (tel qu'un bouton, un lien ou une image, de la bannière) a son propre comportement au clic. Par exemple, compte tenu des comportements suivants lors du clic :<br><br><ul><li>Une bannière a un comportement au clic qui redirige vers la page d'accueil d'un site web.</li><li>Une image dans la bannière a un comportement de clic qui redirige vers la page produit d'un site web.</li></ul>Si un utilisateur clique sur l'image, il sera redirigé vers la page du produit. Toutefois, si vous cliquez sur la zone environnante de la bannière, vous serez redirigé vers la page d'accueil.
{:/}
{% endalert %}

### Étape 4 : Définir la durée de la campagne

Choisissez une date et une heure de début pour votre campagne de bannières. Par défaut, les bannières durent indéfiniment. Vous pouvez modifier cela en sélectionnant **Heure de fin** et en spécifiant une date et une heure de fin.

### Étape 5 : Définir la priorité de la bannière (facultatif)

La [priorité des bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) détermine l'ordre dans lequel les bannières sont affichées si elles partagent le même emplacement. Pour définir manuellement la priorité :

1. Sélectionnez **Définir la priorité exacte.**
2. Glissez-déposez les campagnes pour les ordonner avec la bonne priorité.
3. Sélectionnez **Appliquer le tri**.

{% alert tip %}
Si vous avez plusieurs campagnes Banner utilisant le même ID de placement, nous vous recommandons d'utiliser la fonction de tri des priorités par glisser-déposer pour définir la priorité exacte.
{% endalert %}

### Étape 6 : Testez votre message (facultatif)

{% multi_lang_include banners/testing.md page="campagnes" %}

### Étape 7 : Finir de créer la campagne

Terminez de créer votre campagne en complétant les éléments suivants :

| Option | Description |
| --- | --- |
| **Cibler des utilisateurs** | Ciblez les utilisateurs en choisissant des segments ou des filtres pour réduire votre audience. Vous obtiendrez automatiquement un aperçu de la population approximative du segmentation. L'appartenance exacte à un segment est calculée juste avant l'envoi du message. |
| **Événements de conversion** | Suivez la fréquence à laquelle les utilisateurs effectuent des actions spécifiques après avoir reçu une campagne. Vous pouvez définir des événements de conversion avec une fenêtre de 30 jours maximum pour compter l'action comme une conversion. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Étape 8 : Lancez votre campagne

Après avoir créé et testé votre campagne Banner, vous êtes prêt à la lancer !
