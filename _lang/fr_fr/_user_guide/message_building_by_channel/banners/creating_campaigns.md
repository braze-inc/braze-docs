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

### Étape 2 : Créer une campagne

1. Allez dans **Messagerie** > **Campagnes** et sélectionnez **Créer une campagne.**
2. Sélectionnez la **bannière**.
3. Donnez à votre campagne un nom clair et significatif.
4. Ajoutez des Teams et des tags si nécessaire. Les étiquettes facilitent la recherche de vos campagnes et permettent de créer des rapports. Par exemple, lorsque vous utilisez le générateur de rapports, vous pouvez filtrer par les étiquettes pertinentes.
5. Sélectionnez le placement que vous avez précédemment créé pour l'associer à votre campagne.
6. Ajoutez des variantes si nécessaire. Vous pouvez choisir un type de message et une mise en page différents pour chacun d'entre eux. Pour plus d'informations sur les variantes, reportez-vous au [test multivarié et au test A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing).

### Étape 3 : Composer une bannière {#compose-a-banner}

Pour composer votre Bannière, vous pouvez choisir de.. :

- Commencez par un modèle vierge
- Utilisez un modèle de bannière Braze
- Sélectionnez un modèle de bannière enregistré

Vous pouvez choisir une bannière vierge ou un modèle.]({% image_buster /assets/img/banners/choose_banner_composer.png %})

#### Étape 3.1 : Style de la bannière

Vous pouvez glisser-déposer des blocs et des lignes dans la zone du canvas pour commencer à créer votre message.

Pour personnaliser les propriétés de l'arrière-plan de votre message, les paramètres de la bordure, etc., sélectionnez **Styles**. Si vous souhaitez uniquement personnaliser le style d'un bloc ou d'une ligne spécifique, sélectionnez-le pour effectuer les modifications.

\![Panneau de style du compositeur de la bannière.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### Étape 3.2 : Définir le comportement au clic (facultatif)

Lorsqu'un utilisateur clique sur un lien dans la bannière, vous pouvez choisir de le faire naviguer plus profondément dans votre application ou de le rediriger vers une autre page web. En outre, vous pouvez choisir d' [enregistrer un attribut ou un événement personnalisé]({{site.baseurl}}/developer_guide/analytics/), qui mettra à jour le profil de votre utilisateur avec des données personnalisées lorsqu'il cliquera sur la bannière.

{% alert important %}
{::nomarkdown}
Le comportement au clic peut être remplacé si un élément spécifique (tel qu'un bouton, un lien ou une image, de la bannière) a son propre comportement au clic. Par exemple, compte tenu des comportements suivants lors du clic :<br><ul><li>Une bannière a un comportement au clic qui redirige vers la page d'accueil d'un site web.</li><li>Une image dans la bannière a un comportement de clic qui redirige vers la page produit d'un site web.</li></ul>Si un utilisateur clique sur l'image, il sera redirigé vers la page du produit. Toutefois, si vous cliquez sur la zone environnante de la bannière, vous serez redirigé vers la page d'accueil.
{:/}
{% endalert %}

#### Étape 3.3 : Ajouter des propriétés personnalisées (facultatif) {#custom-properties}

Vous pouvez ajouter des objets personnalisés à une bannière pour y attacher des métadonnées structurées, telles que des chaînes de caractères ou des objets JSON. Ces propriétés n'affectent pas l'affichage de la bannière mais sont [accessibles via le SDK de Braze]({{site.baseurl}}/developer_guide/banners/placements/) pour modifier le comportement ou l'apparence de votre application. Par exemple, vous pourriez :

- Envoyez des métadonnées pour vos analyses/analytiques tierces (si utilisées comme adjectifs).
- Utilisez des métadonnées telles qu'un objet `timestamp` ou JSON pour déclencher une logique conditionnelle.
- Contrôlez le comportement d'une bannière en fonction des métadonnées incluses telles que `ratio` ou `format`.

Pour ajouter une propriété personnalisée, sélectionnez **Paramètres** > **Propriétés** > **Ajouter une propriété.**

La page des propriétés montre l'option d'ajouter la première propriété personnalisée à une campagne Banner.]({% image_buster /assets/img/banners/add_property.png %})

Pour chaque bien que vous souhaitez ajouter, remplissez le formulaire suivant :

| Champ d'application | Description | Exemple |
|-------|-------------|---------|
| Type de propriété | Le type de données pour la propriété. Les types pris en charge sont les suivants : chaîne de caractères, booléen, nombre, horodatage, URL d'image et objet JSON. | Chaîne de caractères |
| Clé de propriété | L'identifiant unique du bien. Cette clé est utilisée dans le SDK pour accéder à la propriété. | `color` |
| Valeur | La valeur attribuée à la propriété. Doit correspondre au type de propriété sélectionné. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Lorsque vous avez terminé, sélectionnez **Terminé**.

\![La page des propriétés avec une chaîne de caractères dont la clé est color et la valeur #FF0000.]({% image_buster /assets/img/banners/example_property.png %})

### Étape 4 : Définir la durée de la campagne

Choisissez une date et une heure de début pour votre campagne de bannières. Par défaut, les bannières durent indéfiniment. Vous pouvez modifier cela en sélectionnant **Heure de fin** et en spécifiant une date et une heure de fin.

### Étape 5 : Définir la priorité de la bannière (facultatif)

La [priorité des bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) détermine l'ordre dans lequel les bannières sont affichées si elles partagent le même emplacement. Pour définir manuellement la priorité :

1. Sélectionnez **Définir la priorité exacte.**
2. Glissez-déposez les campagnes pour les ordonner avec la bonne priorité.
3. Sélectionnez **Appliquer le tri**.

{% alert tip %}
Si vous avez plusieurs campagnes Banner utilisant le même ID de placement, nous vous recommandons d'utiliser la fonction de tri des priorités par glisser-déposer pour définir la priorité exacte.
{% endalert %}

### Étape 6 : Testez votre message (facultatif)

{% multi_lang_include banners/testing.md page="campaigns" %}

### Étape 7 : Finir de créer la campagne

Terminez de créer votre campagne en complétant les éléments suivants :

1. Dans **Audiences cibles**, choisissez des segments ou des filtres pour restreindre votre audience. Vous obtiendrez automatiquement un aperçu de la population approximative du segmentation. L'appartenance exacte à un segment est calculée juste avant l'envoi du message.

{% multi_lang_include target_audiences.md %}

{:start="2"}
2\. Dans **Attribuer des conversions**, suivez la fréquence à laquelle les utilisateurs effectuent des actions spécifiques après avoir reçu une campagne en définissant des événements de conversion avec une fenêtre allant jusqu'à 30 jours pour compter l'action comme une conversion.

### Étape 8 : Lancez votre campagne

Après avoir créé et testé votre campagne Banner, vous êtes prêt à la lancer !
