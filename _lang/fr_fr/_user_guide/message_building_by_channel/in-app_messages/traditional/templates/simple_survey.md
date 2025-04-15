---
nav_title: "Enquête simple"
article_title: Message in-app d’enquête simple
page_order: 1.5
page_type: reference
description: "Cet article de référence explique comment recueillir des attributs, des informations et des préférences utilisateur pour soutenir votre stratégie de campagne à l’aide des enquêtes de messages in-app."
channel:
  - in-app messages
tool:
  - Templates
---

# Enquête simple

> Utilisez le modèle de message in-app **Simple Survey** pour collecter les attributs, informations et préférences des utilisateurs qui alimentent votre stratégie de communication. 

Par exemple, demandez aux utilisateurs comment ils aimeraient utiliser votre application, découvrez leurs préférences personnelles, ou interrogez-les sur leur satisfaction par rapport à une fonctionnalité particulière.

![Trois messages d’enquête simple : préférences de notification, préférences alimentaires et enquête de satisfaction client. Les options sélectionnées dans les enquêtes correspondent aux attributs personnalisés qui seront enregistrés pour cet utilisateur.]({% image_buster /assets/img/iam/iam-survey.png %})

## Exigences du SDK {#supported-sdk-versions}

Ce message in-app ne sera livré que sur les appareils prenant en charge [Flex CSS](https://caniuse.com/flexbox) et au moins dotés des [versions SDK]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions) suivantes. 

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

{% alert note %}
Pour activer les messages in-app HTML via le SDK pour le Web, vous devez fournir l’option d’initialisation `allowUserSuppliedJavascript` à Braze.
{% endalert %}

## Création d’une enquête {#create}

Lorsque vous créez un [message in-app][1], sélectionnez **Enquête simple** pour votre **type de message.**

![]({% image_buster /assets/img/iam/survey-message-type.png %}){: style="max-width:80%"}

Ce modèle d’enquête est pris en charge pour les applications mobiles et les navigateurs Web. N’oubliez pas de vérifier que vous disposez des [versions SDK minimum](#supported-sdk-versions) requises pour cette fonctionnalité.

### Étape 1 : Ajouter votre question d’enquête

Pour commencer à élaborer votre enquête, ajoutez votre question dans le champ **En-tête** de l’enquête. Si vous le souhaitez, vous pouvez ajouter un **corps** de message facultatif qui apparaîtra sous la question.

![Onglet Composer de l’éditeur d’enquête simple, avec des champs pour un en-tête, un corps facultatif et un texte d’aide facultatif.]({% image_buster /assets/img/iam/iam-survey2.png %}){: style="max-width:80%"}

{% alert tip %}
Ces champs peuvent inclure à la fois Liquid et des émojis, alors laissez place à la fantaisie !
{% endalert %}

### Étape 2 : Choisir entre un ou plusieurs choix {#single-multiple-choice}

Utilisez l'option **Sélection à choix unique** ou **Sélection à choix multiple** pour déterminer si l'utilisateur ne peut sélectionner qu'un seul ou plusieurs choix. Vous pouvez ajouter jusqu’à 12 choix dans une enquête.

![Liste déroulante des choix avec "Sélection à choix multiples" sélectionnée.]({% image_buster /assets/img/iam/single-multiple-choice.png %}){: style="max-width:60%"}

{% alert tip %}
Votre **texte d'aide** sera automatiquement mis à jour lorsque vous passerez de la **sélection à choix unique** à la **sélection à choix multiple**, afin d'indiquer aux utilisateurs le nombre de choix qu'ils peuvent sélectionner.
{% endalert %}

### Étape 3 : Recueillir des attributs personnalisés {#custom-attributes}

Sélectionnez **Enregistrer les attributs lors de la soumission** pour collecter les attributs en fonction de la soumission de l'utilisateur. Vous pouvez utiliser cette option pour créer de nouveaux segments et des campagnes de reciblage. Par exemple, dans une enquête de satisfaction, vous pouvez envoyer un e-mail de suivi à tous les utilisateurs qui n’étaient pas satisfaits.

![Menu déroulant Choix avec l’option « Enregistrer les attributs lors de la soumission » sélectionnée.]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:60%"}

Pour ajouter un attribut personnalisé à chaque choix, sélectionnez un nom d’attribut personnalisé dans le menu déroulant (ou créez-en un), puis saisissez la valeur à définir lorsque ce choix est soumis. Vous pouvez créer un nouvel attribut personnalisé dans votre [page de configuration.][5]

Par exemple, dans une enquête de préférences de notification, vous pouvez convertir chaque choix en attribut booléen (vrai/faux) pour permettre aux utilisateurs de sélectionner les sujets qui leur intéressent. Si un utilisateur coche l'option "Promotions", son [profil utilisateur][3] sera mis à jour avec l'attribut personnalisé `Promotions Topic` fixé à `true`. S’il ne fait pas ce choix, ce même attribut reste inchangé.

![]({% image_buster /assets/img/iam/iam-survey3.png %}){: style="max-width:60%"}

Vous pouvez ensuite créer un segment pour les utilisateurs avec `Promotions Topic = true`, afin de vous assurer que seuls les utilisateurs intéressés par vos promotions recevront les campagnes pertinentes.

{% alert important %}
Lorsque la collecte d’attributs personnalisés est activée, les choix qui partagent le même nom d’attribut personnalisé sont regroupés.
{% endalert %}

#### Types de données des attributs personnalisés

Le type de données de vos attributs personnalisés dépend de la façon dont vous avez configuré votre enquête.

- **Sélection à choix multiples :** Le type de données de l'attribut personnalisé doit être un tableau. Si l'attribut personnalisé est défini sur un autre type de données, les réponses ne seront pas enregistrées.
- **Sélection à choix unique :** Le type de données de l'attribut personnalisé _ne doit pas être_ un tableau. Les réponses ne seront pas enregistrées si l'attribut est un tableau.

#### Enregistrement des réponses uniquement

Vous pouvez également choisir d'**enregistrer uniquement les réponses (pas d'attributs).** Lorsque cette option est sélectionnée, les réponses de l’enquête sont enregistrées en tant que clics de boutons, mais les attributs personnalisés ne sont pas consignés dans un profil d’utilisateur. Cela signifie que vous pouvez toujours consulter les indicateurs de clics pour chaque option d'enquête (voir [Analyse)](#analytics), mais que ce choix ne sera pas reflété dans leur profil utilisateur.

Ces indicateurs de clic ne sont pas disponibles pour le reciblage.

### Étape 4 : Choisir le comportement de soumission

Une fois qu’un utilisateur a envoyé sa réponse, vous pouvez éventuellement afficher une page de confirmation ou simplement fermer le message.

Une page de confirmation est l’endroit idéal pour remercier les utilisateurs du temps passé ou fournir des informations supplémentaires. Vous pouvez personnaliser l’appel à action dans cette page afin de diriger les utilisateurs vers une autre page de votre application ou site Web.

Modifiez le texte de votre bouton et le comportement au clic dans la section **Bouton de soumission** au bas de l'onglet **Enquête :** 

![Comportement en cas de clic défini sur « Envoyer les réponses et afficher la page de confirmation ».]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:60%"}

Si vous choisissez d'ajouter une page de confirmation, passez à l'onglet **Page de confirmation** pour personnaliser votre message :

![Onglet Confirmation page (Page de confirmation) de l’éditeur d’enquête simple. Les champs disponibles sont l’en-tête, le corps optionnel, le texte du bouton et le comportement en cas de clic de bouton.]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:80%"}

Si vous souhaitez guider les utilisateurs vers une autre page de votre application ou de votre site Web, modifiez le **comportement lors du clic** du bouton.

### Étape 5 : Styliser votre message (facultatif) {#styling}

Vous pouvez personnaliser la couleur de la police et la couleur d'accentuation du message à l'aide du sélecteur de **thème de couleur**.

![Onglet Composer de l'éditeur d'enquête simple avec le sélecteur de thème de couleur développé après que l'utilisateur ait cliqué sur la palette de couleurs.]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## Analyser les résultats {#analytics}

Une fois votre campagne lancée, vous pouvez analyser les résultats en temps réel pour voir la répartition de chaque choix sélectionné. Si vous avez activé la [collecte d'attributs personnalisés](#custom-attributes), vous pourrez également créer de nouveaux segments ou des campagnes de suivi pour les utilisateurs qui ont répondu à l'enquête.

{% alert note %}
Les choix d’enquête supprimés apparaîtront toujours dans l’analyse, mais ne sont pas affichés comme choix pour les nouveaux utilisateurs.
{% endalert %}

Pour connaître les définitions des indicateurs de l’enquête, reportez-vous au [glossaire des indicateurs de rapport][11] et filtrez par message in-app.

![Panneau de performance des messages in-app avec analyse des clics pour chaque choix et bouton dans l’enquête.]({% image_buster /assets/img/iam/iam-survey-analytics.png %}){: style="max-width:95%"}

Consultez les [rapports sur les messages in-app][4] pour connaître les indicateurs de votre campagne.

### Currents {#currents}

Les choix sélectionnés seront automatiquement transférés dans Currents, sous la rubrique [**Événements de clics du message in-app**][6] `button_id` dans le champ Chaque choix est envoyé avec son identifiant unique universel (UUID).

## Cas d’utilisation

### Satisfaction des utilisateurs

**Objectif :** Mesurer la satisfaction client et envoyer des campagnes de reconquête aux utilisateurs qui ont donné des notes faibles.

Pour ce cas d’utilisation, utilisez une sélection à choix unique, avec des choix allant de « Très insatisfait » à « Très satisfait ». Chaque choix a l’attribut personnalisé `customer_satisfaction` défini à un nombre compris entre 1 et 5, 1 étant le moins satisfait et 5 étant le plus satisfait.

Après avoir lancé votre enquête, vous pouvez cibler vos campagnes de reconquête sur les utilisateurs qui ont signalé être « Très insatisfait » ou « Insatisfait », avec `customer_satisfaction` défini à 1 ou 2.

![][7]

### Identifier les objectifs des clients

**Objectif :** Identifier les principales raisons pour lesquelles les utilisateurs visitent votre application.

Pour ce cas d’utilisation, utilisez une sélection à choix unique, chaque choix offrant une raison fréquente pour laquelle un utilisateur peut visiter votre application. Chaque choix a l’attribut personnalisé `product_goal` défini au sujet du cas d’utilisation. 

Par exemple, si l’utilisateur sélectionne « Mettre à niveau mon compte », `product_goal = upgrade` figure dans le profil de l’utilisateur.

![][8]

### Améliorer les taux de conversion

**Objectif :** Comprendre pourquoi les clients n’effectuent pas de mises à niveau ou d’achats.

Pour ce cas d’utilisation, utilisez une sélection à choix unique, chaque choix offrant une raison fréquente pour laquelle un utilisateur n’effectue pas de mise à niveau vers un compte premium. Chaque choix a l’attribut personnalisé `upgrade_reason` défini à la sélection de l’utilisateur. 

Par exemple, si l’utilisateur sélectionne « Trop cher », `upgrade_reason = expensive` figure dans le profil de l’utilisateur. Vous pouvez cibler ces utilisateurs pour des campagnes promotionnelles telles que des remises ou des essais gratuits.

![][9]

### Fonctionnalités préférées

**Objectif :** Comprendre les fonctionnalités que les clients aiment utiliser.

Pour ce cas d’utilisation, utilisez une sélection à choix multiple, chaque choix correspondant à une fonctionnalité de l’application. Chaque choix a l’attribut personnalisé `favorite_features` défini à la sélection de l’utilisateur. Comme ce cas d'utilisation implique un choix multiple, une fois que l'utilisateur a répondu à l'enquête, son profil est mis à jour avec l'attribut `favorite_features` défini comme un tableau de toutes les options sélectionnées.

![][10]

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[3]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/managing_custom_data
[6]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#api_fzzdoylmrtwe

[7]: {% image_buster /assets/img_archive/simple_survey_use_case_1.png %}
[8]: {% image_buster /assets/img_archive/simple_survey_use_case_2.png %}
[9]: {% image_buster /assets/img_archive/simple_survey_use_case_3.png %}
[10]: {% image_buster /assets/img_archive/simple_survey_use_case_4.png %}

[11]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
