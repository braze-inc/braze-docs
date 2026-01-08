---
nav_title: "Enquête simple"
article_title: "Message in-app de l'enquête simple"
page_order: 1.5
page_type: reference
description: "Cet article de référence explique comment collecter les attributs, informations et préférences des utilisateurs pour alimenter votre stratégie de campagne à l'aide des enquêtes sur les messages in-app."
channel:
  - in-app messages
tool:
  - Templates
---

# Enquête simple

> Utilisez le modèle de message in-app **Simple Survey** pour collecter les attributs, informations et préférences des utilisateurs qui alimentent votre stratégie de communication. 

Par exemple, demandez aux utilisateurs comment ils aimeraient utiliser votre appli, apprenez-en plus sur leurs préférences personnelles, ou même interrogez-les sur leur satisfaction à l'égard d'une fonctionnalité particulière.

Trois messages d'enquête simples : préférences en matière de notification, préférences alimentaires et enquête de satisfaction des clients. Les options sélectionnées dans les enquêtes correspondent aux attributs personnalisés qui seront enregistrés pour cet utilisateur.]({% image_buster /assets/img/iam/iam-survey.png %})

## Exigences du SDK {#supported-sdk-versions}

Ce message in-app ne sera envoyé qu'aux appareils qui prennent en charge [Flex CSS](https://caniuse.com/flexbox), et qui doivent disposer au minimum des [versions]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions) suivantes [du SDK]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions). 

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

{% alert note %}
Pour activer les messages in-app HTML via le SDK Web, vous devez fournir l'option d'initialisation `allowUserSuppliedJavascript` à Braze.
{% endalert %}

## Créer une enquête {#create}

Lorsque vous créez un [message in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/), sélectionnez **Enquête simple** pour votre **type de message.**

Ce modèle de sondage est pris en charge à la fois pour les applications mobiles et les navigateurs web. N'oubliez pas de vérifier que vos SDK sont dans les [versions minimales](#supported-sdk-versions) requises pour cette fonctionnalité.

### Étape 1 : Ajoutez votre question d'enquête

Pour commencer à créer votre enquête, ajoutez votre question dans le champ **En-tête de l'** enquête. Si vous le souhaitez, vous pouvez ajouter un **envoi** de messages facultatif qui apparaîtra sous votre question d'enquête.

Onglet Composer de l'éditeur d'enquête simple, avec des champs pour un en-tête, un corps et un texte d'aide facultatifs.]({% image_buster /assets/img/iam/iam-survey2.png %}){: style="max-width:90%"}

{% alert tip %}
Ces champs peuvent contenir à la fois des liquides et des émojis, alors faites preuve de fantaisie !
{% endalert %}

### Étape 2 : Configurer les choix {#single-multiple-choice}

Vous pouvez ajouter jusqu'à 12 choix dans une enquête.

Sélectionnez soit la **sélection à choix unique**, soit la **sélection à choix multiple.** Le **texte de l'aide** est automatiquement mis à jour lorsque vous passez d'une option à l'autre afin d'indiquer aux utilisateurs le nombre de choix possibles. 

Ensuite, déterminez si vous allez [collecter des attributs personnalisés](#custom-attributes) ou [uniquement les réponses du journal.](#no-attributes)

\![Liste déroulante de choix avec "Log attributes upon submission" sélectionné.]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:60%"}

#### Collecte d'attributs personnalisés {#custom-attributes}

Sélectionnez **Enregistrer les attributs lors de la soumission** pour collecter les attributs en fonction de la soumission de l'utilisateur. Vous pouvez utiliser cette option pour créer de nouveaux segments et des campagnes de reciblage. Par exemple, dans le cadre d'une [enquête de satisfaction](#user-satisfaction), vous pourriez envoyer un e-mail de suivi à tous les utilisateurs qui n'étaient pas satisfaits.

Pour ajouter un attribut personnalisé à chaque choix, sélectionnez un nom d'attribut personnalisé dans le menu déroulant (ou créez-en un nouveau), puis saisissez la valeur à définir lorsque ce choix est soumis. Vous pouvez également créer un nouvel attribut personnalisé dans votre [page de paramètres.]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/)

Le type de données de vos attributs personnalisés dépend de la façon dont vous avez configuré votre enquête.

- **Sélection à choix multiples :** Le type de données de l'attribut personnalisé doit être un tableau. Si l'attribut personnalisé est défini sur un autre type de données, les réponses ne seront pas enregistrées.
- **Sélection à choix unique :** Le type de données de l'attribut personnalisé _ne doit pas être_ un tableau. Les réponses ne seront pas enregistrées si l'attribut est un tableau.

{% alert important %}
Lorsque la collecte d'attributs personnalisés est activée, les choix qui partagent le même nom d'attribut personnalisé sont regroupés dans un tableau.
{% endalert %}

##### Exemple 

Par exemple, dans une [enquête sur les préférences en matière de notification](#notification-preferences), vous pouvez faire de chaque choix un attribut booléen (vrai/faux) pour permettre aux utilisateurs de sélectionner les sujets qui les intéressent. Si un utilisateur coche l'option "Promotions", son [profil utilisateur]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) sera mis à jour avec l'attribut personnalisé `Promotions Topic` fixé à `true`. Si le choix n'est pas coché, ce même attribut restera inchangé.

Vous pouvez ensuite utiliser le filtre `Custom Attribute` pour créer un segment pour les utilisateurs ayant l'attribut personnalisé `Promotions Topic` `is` `true` afin de vous assurer que seuls les utilisateurs intéressés par vos promotions recevront les campagnes correspondantes.

#### Enregistrement des réponses uniquement {#no-attributes}

Vous pouvez également choisir d'**enregistrer uniquement les réponses (pas d'attributs)**. Lorsque cette option est sélectionnée, les réponses à l'enquête sont enregistrées comme des clics sur des boutons, mais les attributs personnalisés ne sont pas enregistrés dans le profil de l'utilisateur. Cela signifie que vous pouvez toujours consulter les indicateurs de clics pour chaque option d'enquête (voir [Analyse)](#analytics), mais que ce choix ne sera pas reflété dans leur profil utilisateur.

Ces indicateurs de clics ne sont pas disponibles pour le reciblage.

### Étape 4 : Choisissez un comportement de soumission

Une fois que l'utilisateur a envoyé sa réponse, vous pouvez afficher une page de confirmation ou simplement fermer le message.

La page de confirmation est l'endroit idéal pour remercier les utilisateurs de leur temps ou pour leur fournir des informations supplémentaires. Vous pouvez personnaliser l'appel à l'action sur cette page pour guider les utilisateurs vers une autre page de votre appli ou de votre site web.

Modifiez le texte de votre bouton et le comportement au clic dans la section **Bouton de soumission** au bas de l'onglet **Enquête :** 

\![Le comportement au clic est défini sur "Soumettre les réponses et afficher la page de confirmation".]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:60%"}

Si vous choisissez d'ajouter une page de confirmation, passez à l'onglet **Page de confirmation** pour personnaliser votre message :

!onglet Page de confirmation de l'éditeur d'enquête simple. Les champs disponibles sont l'en-tête, le corps optionnel, le texte du bouton et le comportement du bouton au clic.]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:90%"}

Si vous souhaitez guider les utilisateurs vers une autre page de votre application ou de votre site web, modifiez le **comportement Au clic du** bouton.

### Étape 5 : Styliser votre message (facultatif) {#styling}

Vous pouvez personnaliser la couleur de la police et la couleur d'accentuation du message à l'aide du sélecteur de **thème de couleur**.

L'onglet Composer de l'éditeur d'enquêtes simples avec le sélecteur de thème de couleur développé après qu'un utilisateur ait cliqué sur la palette de couleurs.]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## Analyser les résultats {#analytics}

Une fois votre campagne lancée, vous pouvez analyser les résultats en temps réel pour connaître la répartition de chaque choix sélectionné. Si vous avez activé la [collecte d'attributs personnalisés](#custom-attributes), vous pourrez également créer de nouveaux segments ou des campagnes de suivi pour les utilisateurs qui ont répondu à l'enquête.

{% alert note %}
Les choix d'enquête supprimés apparaîtront toujours dans l'analyse/analytique, mais ne seront pas proposés aux nouveaux utilisateurs.
{% endalert %}

Vous pouvez trouver les indicateurs de performance de votre sondage en développant le menu déroulant **Résultats** pour une variante spécifique dans la section **Performance des messages in-app** des indicateurs. Voici un aperçu de ce que vous verrez :

- La **participation à l'enquête** montre comment les utilisateurs ont interagi avec l'enquête dans son ensemble, y compris le nombre total d'envois, de rejets et de clics dans le corps du message.
- **Les résultats de l'enquête** indiquent le nombre d'utilisateurs qui ont choisi chaque option de réponse, ainsi que le pourcentage de soumissions totales que chaque choix représente.
- Les **indicateurs de la page de confirmation** (s'ils sont activés) indiquent le nombre d'utilisateurs qui ont vu l'écran de confirmation, qui ont cliqué sur son bouton ou qui l'ont quitté sans interaction.

Pour connaître les définitions des indicateurs d'enquête, consultez le [glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data/report_metrics/) et filtrez par " Message in-app ".

Consultez les [rapports sur les messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) pour connaître les indicateurs de votre campagne.

### Courants {#currents}

Les choix sélectionnés seront automatiquement transférés dans Currents, sous la rubrique [**Événements de clics du message in-app**]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#api_fzzdoylmrtwe) `button_id` dans le champ Chaque choix sera envoyé avec son identifiant universel unique (UUID).

## Cas d'utilisation

{% tabs %}
{% tab User satisfaction %}

### Satisfaction des utilisateurs

**Objectif :** Mesurez la satisfaction des clients et envoyez des campagnes de reconquête aux utilisateurs qui ont laissé de mauvaises notes.

Pour ce faire, utilisez une enquête à choix unique comportant cinq options allant de "😡 Très insatisfait" à "😍 Très satisfait". Chaque choix est mappé à l'attribut personnalisé `customer_satisfaction`, avec une valeur numérique de 1 à 5 - où 1 indique le moins satisfait et 5 le plus satisfait.

| Choix                                | Attribut              | Valeur |
|---------------------------------------|------------------------|-------|
| 😡 Très insatisfait                  | `customer_satisfaction` | 1     |
| 😟 Insatisfait                       | `customer_satisfaction` | 2     |
| 🙂 Ni satisfait ni insatisfait | `customer_satisfaction` | 3     |
| 😊 Satisfait                          | `customer_satisfaction` | 4     |
| 😍 Très satisfait                     | `customer_satisfaction` | 5     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Lorsqu'un utilisateur répond à l'enquête, la valeur qu'il a sélectionnée est enregistrée en tant qu'attribut personnalisé. Vous pouvez ensuite créer des campagnes de suivi à l'aide de filtres d'audience. Par exemple, ciblez les messages de reconquête sur les utilisateurs dont l'attribut `customer_satisfaction` est 1 ou 2.

{% endtab %}
{% tab Notification preferences %}

### Préférences de notification

**Objectif :** Permettez aux utilisateurs d'opter pour des types de notifications spécifiques.

Pour ce faire, utilisez une enquête de sélection à choix multiples où chaque choix représente un sujet de notification. Au lieu d'attribuer des valeurs différentes au même attribut, chaque choix est mappé à un attribut booléen distinct qui reflète l'intérêt de l'utilisateur pour ce sujet. Si un utilisateur fait un choix, l'attribut correspondant est fixé à `true`. S'il n'est pas sélectionné, l'attribut reste inchangé.

| Choix             | Attribut              | Valeur  |
|--------------------|------------------------|--------|
| Mises à jour des produits    | `wants_product_updates`| `true` |
| Promotions         | `wants_promotions`     | `true` |
| Invitations aux événements      | `wants_event_invites`  | `true` |
| Enquêtes & Retour d'information | `wants_surveys`        | `true` |
| Conseils & Tutoriels   | `wants_tips`           | `true` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Identify customer goals %}

### Identifier les objectifs des clients

**Objectif :** Identifiez les principales raisons pour lesquelles les utilisateurs visitent votre application.

Pour ce faire, utilisez une enquête de sélection à choix unique, chaque option conseillant un objectif ou une intention commune. Chaque choix est mappé à l'attribut personnalisé `product_goal` avec une valeur correspondant à l'intention de l'utilisateur sélectionnée.

| Choix                     | Attribut       | Valeur     |
|----------------------------|------------------|-----------|
| Vérification du statut            | `product_goal`   | `status`  |
| Mise à niveau de mon compte       | `product_goal`   | `upgrade` |
| Planification d'un rendez-vous  | `product_goal`   | `schedule`|
| Soutien à la clientèle           | `product_goal`   | `support` |
| Juste pour naviguer              | `product_goal`   | `browse`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Lorsqu'un utilisateur répond à l'enquête, la valeur sélectionnée est enregistrée en tant qu'attribut personnalisé sur son profil. Vous pouvez ensuite utiliser ces données pour personnaliser les expériences futures ou segmenter les utilisateurs en fonction de leur objectif principal.

{% endtab %}
{% tab Improve conversion rates %}

### Améliorer les taux de conversion

**Objectif :** Comprenez pourquoi les clients ne passent pas à la vitesse supérieure ou n'achètent pas.

Pour ce faire, utilisez une enquête de sélection à choix unique, chaque option conseillant un obstacle courant à la mise à niveau. Chaque choix est mappé à l'attribut personnalisé `upgrade_reason` avec une valeur correspondante qui reflète la sélection de l'utilisateur.

| Choix              | Attribut        | Valeur       |
|---------------------|------------------|-------------|
| Trop cher       | `upgrade_reason` | `expensive` |
| Sans valeur        | `upgrade_reason` | `value`     |
| Difficile à utiliser    | `upgrade_reason` | `difficult` |
| Utilisation d'un concurrent  | `upgrade_reason` | `competitor`|
| Autre raison        | `upgrade_reason` | `other`     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Lorsqu'un utilisateur répond à l'enquête, la valeur sélectionnée est enregistrée dans son profil. Vous pouvez ensuite cibler ces utilisateurs avec des campagnes adaptées à leur objection spécifique, comme des offres de réduction ou des améliorations de la convivialité.

{% endtab %}
{% tab Favorite features %}

### Fonctionnalités préférées

**Objectif :** Comprenez quelles sont les fonctionnalités que les clients aiment utiliser.

Pour mettre cela en place, utilisez un sondage de sélection à choix multiples où chaque option représente une fonctionnalité de votre appli. Chaque choix est mappé à l'attribut personnalisé `favorite_features`, et lorsque l'utilisateur soumet l'enquête, l'attribut est défini comme un tableau des valeurs sélectionnées.

| Choix            | Attribut          | Valeur        |
|-------------------|--------------------|--------------|
| Signets         | `favorite_features`| `bookmarks`  |
| Application mobile        | `favorite_features`| `mobile`     |
| Partage des postes     | `favorite_features`| `sharing`    |
| Soutien à la clientèle  | `favorite_features`| `support`    |
| Personnalisation     | `favorite_features`| `custom`     |
| Prix / Valeur     | `favorite_features`| `value`      |
| Communauté         | `favorite_features`| `community`  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Comme cette enquête utilise une sélection à choix multiples, le profil de l'utilisateur sera mis à jour avec une liste de toutes les valeurs de fonctionnalité sélectionnées.

{% endtab %}
{% endtabs %}
