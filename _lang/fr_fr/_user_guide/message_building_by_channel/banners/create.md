---
nav_title: Créer une bannière
article_title: Créer une bannière
page_order: 1
description: "Cet article de référence explique comment créer, composer, configurer et envoyer des bannières à l'aide de campagnes et de canevas Braze."
tool:
  - Campaigns
channel:
  - banners
---

# Créer une bannière

> Apprenez à créer des bannières lorsque vous créez des campagnes et des canevas dans Braze. Pour plus d'informations générales, reportez-vous à la section [À propos des bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners).

{% alert important %}
La création d'un message de bannière dans Canvas est en accès anticipé. Si vous souhaitez participer à cet accès anticipé, contactez votre gestionnaire de la satisfaction client.
{% endalert %}

## Conditions préalables

Avant de pouvoir lancer votre Teams, votre équipe de développement doit [mettre en place des placements dans votre appli ou votre site web.]({{site.baseurl}}/developer_guide/banners/creating_placements/) Vous pouvez toujours rédiger votre campagne de bannières pendant ce temps, mais vous ne pourrez pas lancer la campagne tant que les placements n'auront pas été configurés.

## Créer un message de bannière

{% multi_lang_include banners/creating_placements.md section="user" %}

### Étape 2 : Choisissez où créer votre message

Vous ne savez pas si votre message doit être envoyé via une campagne ou un Canvas ? Les campagnes sont plus adaptées aux campagnes d'envoi de messages uniques et ciblés, tandis que les Canevas sont plus adaptés aux parcours utilisateurs en plusieurs étapes.

{% tabs %}
{% tab Campaign %}

1. Allez dans **Messagerie** > **Campagnes** et sélectionnez **Créer une campagne**.
2. Sélectionnez la **bannière**.
3. Donnez un nom clair et significatif à votre campagne.
4. Ajoutez des [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) et des [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) si nécessaire. Les balises facilitent la recherche et l’identification des campagnes, et la création de rapports. Par exemple, lorsque vous utilisez le générateur de rapports, vous pouvez filtrer par les étiquettes pertinentes.
5. Sélectionnez le placement que vous avez précédemment créé pour l'associer à votre campagne.
6. Ajoutez des variantes si nécessaire. Vous pouvez choisir un type de message et une mise en page différents pour chacun d'entre eux. Pour plus d'informations sur les variantes, reportez-vous au [test multivarié et au test A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing).
7. Choisissez une date et une heure de début pour votre campagne de bannières. Par défaut, les bannières durent indéfiniment. Vous pouvez modifier cela en sélectionnant **Heure de fin** et en spécifiant une date et une heure de fin.

{% alert tip %}
Si tous les messages de votre campagne vont être similaires ou avoir le même contenu, composez votre message avant d’ajouter des variantes supplémentaires. Vous pouvez ensuite sélectionner **Copier de la variante** dans le menu déroulant **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Créez votre canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l'aide du compositeur de canvas.
2. Après avoir configuré votre canvas, ajoutez une étape du message dans le générateur de canvas. Donnez un nom clair et significatif à votre étape.
3. Sélectionnez **Banner** comme canal d'envoi de messages.
4. Sélectionnez un emplacement pour la bannière.
5. Définissez la priorité de la bannière. La [priorité des bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) détermine l'ordre dans lequel les bannières sont affichées si elles partagent le même emplacement.
6. Fixez une date d'expiration pour la bannière. Il peut s'agir d'un délai après la mise à disposition de l'étape ou d'une date et d'une heure spécifiques.

{% endtab %}
{% endtabs %}

### Étape 3 : Composer une bannière {#compose-a-banner}

Pour composer votre bannière, vous pouvez choisir de.. :

- Commencer par un modèle vide
- Utilisez un modèle de bannière Braze
- Sélectionnez un modèle de bannière enregistré

![Possibilité de choisir une bannière vierge ou un modèle.]({% image_buster /assets/img/banners/choose_banner_composer.png %})

#### Étape 3.1 : Style de la bannière

Vous pouvez glisser-déposer des blocs et des lignes dans la zone du canvas pour commencer à créer votre message.

Pour personnaliser les propriétés de l'arrière-plan de votre message, les paramètres de la bordure, etc., sélectionnez **Styles**. Si vous souhaitez uniquement personnaliser le style d'un bloc ou d'une ligne spécifique, sélectionnez-le pour apporter des modifications.

![Panneau de style du compositeur de bannières.]({% image_buster /assets/img/banners/banner_card_styles.png %})

#### Étape 3.2 : Définir le comportement au clic (facultatif)

Lorsqu'un utilisateur clique sur un lien dans la bannière, vous pouvez choisir de le faire naviguer plus profondément dans votre application ou de le rediriger vers une autre page web. En outre, vous pouvez choisir d' [enregistrer un attribut ou un événement personnalisé]({{site.baseurl}}/developer_guide/analytics/), qui met à jour le profil de votre utilisateur avec des données personnalisées lorsqu'il clique sur la bannière.

{% alert important %}
{::nomarkdown}
Le comportement au clic peut être remplacé si un élément spécifique (tel qu'un bouton, un lien ou une image, de la bannière) a son propre comportement au clic. Par exemple, compte tenu des comportements suivants lors du clic :<br><ul><li>Une bannière a un comportement au clic qui redirige vers la page d'accueil d'un site web.</li><li>Une image dans la bannière a un comportement de clic qui redirige vers la page produit d'un site web.</li></ul>Si un utilisateur clique sur l'image, il est redirigé vers la page du produit. Cependant, en cliquant sur la zone environnante de la bannière, ils sont redirigés vers la page d'accueil.
{:/}
{% endalert %}

#### Étape 3.3 : Ajouter des propriétés personnalisées (facultatif) {#custom-properties}

Vous pouvez ajouter des objets personnalisés à une bannière pour y attacher des métadonnées structurées, telles que des chaînes de caractères ou des objets JSON. Ces propriétés n'affectent pas l'affichage de la bannière mais sont [accessibles via le SDK de Braze]({{site.baseurl}}/developer_guide/banners/placements/) pour modifier le comportement ou l'apparence de votre application. Par exemple, vous pourriez :

- Envoyez des métadonnées pour vos analyses/analytiques tierces (si utilisées comme adjectifs).
- Utilisez des métadonnées telles qu'un objet `timestamp` ou JSON pour déclencher une logique conditionnelle.
- Contrôlez le comportement d'une bannière en fonction des métadonnées incluses telles que `ratio` ou `format`.

Pour ajouter une propriété personnalisée, sélectionnez **Paramètres** > **Propriétés** > **Ajouter une propriété.**

![La page des propriétés montrant l'option d'ajouter la première propriété personnalisée à une campagne Banner.]({% image_buster /assets/img/banners/add_property.png %})

Pour chaque bien que vous souhaitez ajouter, remplissez le formulaire suivant :

| Champ | Description | Exemple |
|-------|-------------|---------|
| Type de propriété | Le type de données pour la propriété. Les types pris en charge sont les suivants : chaîne de caractères, booléen, nombre, horodatage, URL d'image et objet JSON. | Chaîne de caractères |
| Clé de propriété | L'identifiant unique du bien. Cette clé est utilisée dans le SDK pour accéder à la propriété. | `color` |
| Valeur | La valeur attribuée à la propriété. Doit correspondre au type de propriété sélectionné. | `#FF0000` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Lorsque vous avez terminé, sélectionnez **Terminé**.

![La page des propriétés contient une chaîne de caractères dont la clé est color et la valeur #FF0000.]({% image_buster /assets/img/banners/example_property.png %})

### Étape 4 : Créer le reste de votre campagne ou de votre Canvas

{% tabs %}
{% tab Campaign %}

#### Définir la priorité de la bannière (facultatif)

La [priorité des bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners/#priority) détermine l'ordre dans lequel les bannières sont affichées si elles partagent le même emplacement. Pour définir manuellement la priorité :

1. Sélectionnez **Définir la priorité exacte.**
2. Glissez-déposez les campagnes pour les ordonner avec la bonne priorité.
3. Sélectionnez **Appliquer le tri**.

{% alert tip %}
Si vous avez plusieurs campagnes Banner utilisant le même ID de placement, nous vous recommandons d'utiliser la fonction de tri des priorités par glisser-déposer pour définir la priorité exacte.
{% endalert %}

#### Choisissez votre audience

1. Dans **Audiences cibles**, choisissez des segments ou des filtres pour restreindre votre audience. Vous recevez automatiquement un aperçu de la population approximative de la segmentation. L'appartenance exacte à un segment est calculée avant l'envoi du message.

{% multi_lang_include target_audiences.md %}

{:start="2"}
2\. Dans **Attribuer des conversions**, suivez la fréquence à laquelle les utilisateurs effectuent des actions spécifiques après avoir reçu une campagne en définissant des événements de conversion avec une fenêtre allant jusqu'à 30 jours pour compter l'action comme une conversion.

{% multi_lang_include target_audiences.md %}

#### Sélectionner des événements de conversion

Braze vous permet de suivre les [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), c'est-à-dire la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, après avoir reçu une campagne. Vous avez la possibilité d'autoriser une fenêtre de 30 jours maximum pendant laquelle une conversion est comptabilisée si l'utilisateur effectue l'action spécifiée.

{% endtab %}

{% tab Canvas %}

Si vous ne l’avez pas déjà fait, complétez les sections restantes de votre composant de Canvas. Pour plus de détails sur la manière de créer le reste de votre Canvas, de mettre en œuvre les [tests multivariés]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) et la [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/), etc., reportez-vous à l'étape [Créer votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation sur le Canvas.

{% endtab %}
{% endtabs %}

### Étape 5 : Testez votre message (facultatif)

{% multi_lang_include banners/testing.md page="campaigns" %}

### Étape 6 : Revue et déploiement

Une fois que vous avez fini de créer votre campagne ou votre Canvas, passez en revue ses détails, [testez-le]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/), puis envoyez-le lorsque vous êtes prêt.
