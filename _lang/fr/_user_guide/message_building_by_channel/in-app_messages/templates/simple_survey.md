---
nav_title: "Enquête simple"
article_title: Message In-App d’enquête simple
page_order: 1.5
page_type: reference
description: "Cet article de référence explique comment recueillir des attributs, des informations et des préférences utilisateur pour soutenir votre stratégie de campagne à l’aide des enquêtes de messages in-app."
channel:
  - messages In-App
tool:
  - Templates
---

# Enquête simple

> Utilisez le nouveau modèle de message In-App d’**enquête simple** pour recueillir des attributs, des informations et des préférences utilisateur afin d’alimenter votre stratégie de campagne. 

Par exemple, demandez aux utilisateurs comment ils aimeraient utiliser votre application, découvrez leurs préférences personnelles, ou interrogez-les sur leur satisfaction par rapport à une fonctionnalité particulière.

![Trois messages d’enquête simple : préférences de notification, préférences alimentaires et enquête de satisfaction client. Les options sélectionnées dans les enquêtes correspondent aux attributs personnalisés qui seront enregistrés pour cet utilisateur.]({% image_buster /assets/img/iam/iam-survey.png %})

## Exigences du SDK {#supported-sdk-versions}

Ce message In-App ne sera livré que sur les appareils prenant en charge [Flex CSS](https://caniuse.com/flexbox) et au moins dotés des [versions SDK]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions) suivantes. 

{% sdk_min_versions web:2.5.0 android:8.0.0 ios:3.23.0 %}

{% alert note %}
Pour activer les messages in-app HTML via le SDK pour le Web, vous devez fournir l’option d’initialisation `allowUserSuppliedJavascript` à Braze.
{% endalert %}

## Création d’une enquête {#create}

Lors de la création d’un [message In-App][1], sélectionnez **Simple Survey (Enquête simple)** comme **type de message**.

![]({% image_buster /assets/img/iam/survey-message-type.png %}){: style="max-width:80%"}

Ce modèle d’enquête est pris en charge pour les applications mobiles et les navigateurs Web. N’oubliez pas de vérifier que vous disposez des [versions SDK minimum](#supported-sdk-versions) requises pour cette fonctionnalité.

### Étape 1 : Ajouter votre question d’enquête

Pour commencer à élaborer votre enquête, ajoutez votre question dans le champ d’**en-tête** de l’enquête. Si vous le souhaitez, vous pouvez ajouter un **corps** de message facultatif qui apparaîtra sous la question.

![Onglet Composer de l’éditeur d’enquête simple, avec des champs pour un en-tête, un corps facultatif et un texte d’aide facultatif.]({% image_buster /assets/img/iam/iam-survey2.png %}){: style="max-width:80%"}

{% alert tip %} 
Ces champs peuvent inclure à la fois Liquid et des émojis, alors laissez place à la fantaisie ! 
{% endalert %}

### Étape 2 : Choisir entre un ou plusieurs choix {#single-multiple-choice}

Choisissez **Single-choice selection (Sélection à choix unique)** ou **Multiple-choice selection (Sélection à choix multiples)** pour décider si un utilisateur peut sélectionner un ou plusieurs choix. Vous pouvez ajouter jusqu’à 12 choix dans une enquête.

![Menu déroulant Choix avec l’option « Sélection à choix multiple » sélectionnée.]({% image_buster /assets/img/iam/single-multiple-choice.png %}){: style="max-width:60%"}

{% alert tip %} 
Votre **texte d’aide** est automatiquement actualisé quand vous basculez entre **Sélection à choix unique** et **Sélection à choix multiples** pour permettre aux utilisateurs de savoir combien de choix ils disposent. 
{% endalert %}

### Étape 3 : Recueillir des attributs personnalisés {#custom-attributes}

Sélectionner **Log attributes upon submission** (Consigner les attributs selon soumission) pour collecter des attributs en fonction de la soumission de l’utilisateur. Vous pouvez utiliser cette option pour créer de nouveaux segments et des campagnes de reciblage. Par exemple, dans une enquête de satisfaction, vous pouvez envoyer un e-mail de suivi à tous les utilisateurs qui n’étaient pas satisfaits.

![Menu déroulant Choix avec l’option « Consigner les attributs selon la soumission » sélectionnée.]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:60%"}

Pour ajouter un attribut personnalisé à chaque choix, sélectionnez un nom d’attribut personnalisé dans le menu déroulant (ou créez-en un), puis saisissez la valeur à définir lorsque ce choix est soumis. Vous pouvez créer un nouvel attribut personnalisé dans votre [page de paramètres][5].

Par exemple, dans une enquête de préférences de notification, vous pouvez convertir chaque choix en attribut booléen (true/false) pour permettre aux utilisateurs de sélectionner les sujets qui leur intéressent. Si un utilisateur choisit « Promotions », son [profil utilisateur][3] est mis à jour avec l’attribut personnalisé `Promotions Topic` défini à `true`. S’il ne fait pas ce choix, ce même attribut reste inchangé.

![]({% image_buster /assets/img/iam/iam-survey3.png %}){: style="max-width:60%"}

Vous pouvez ensuite créer un segment pour les utilisateurs avec `Promotions Topic = true`, afin de vous assurer que seuls les utilisateurs intéressés par vos promotions recevront les campagnes pertinentes.

{% alert important %} 
Lorsque la collecte d’attributs personnalisés est activée, les choix qui partagent le même nom d’attribut personnalisé sont regroupés.
{% endalert %}

#### Enregistrement des réponses uniquement

Vous pouvez également choisir **Log responses only (no attributes) (Consigner les réponses uniquement [pas d’attributs])**. Lorsque cette option est sélectionnée, les réponses de l’enquête sont enregistrées en tant que clics de boutons, mais les attributs personnalisés ne sont pas consignés dans un profil d’utilisateur. Par conséquent, vous pouvez toujours afficher les indicateurs de clics pour chaque option d’enquête (voir [Analytique](#analytics)), mais ce choix n’est pas reflété dans le profil utilisateur.

Ces métriques de clic ne sont pas disponibles pour le reciblage.

### Étape 4 : Choisir le comportement de soumission

Une fois qu’un utilisateur a envoyé sa réponse, vous pouvez éventuellement afficher une page de confirmation ou simplement fermer le message.

Une page de confirmation est l’endroit idéal pour remercier les utilisateurs du temps passé ou fournir des informations supplémentaires. Vous pouvez personnaliser l’appel à action dans cette page afin de diriger les utilisateurs vers une autre page de votre application ou site Web.

Modifiez votre texte de bouton et le comportement en cas de clic dans la section **Submit Button (Bouton Soumettre)** au bas de l’onglet **Enquête** :

![Comportement en cas de clic défini à « Envoyer les réponses et afficher la page de confirmation ».]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:60%"}

Si vous choisissez d’ajouter une page de confirmation, passez à l’onglet **Page de confirmation** pour personnaliser votre message :

![Onglet Confirmation page (Page de confirmation) de l’éditeur d’enquête simple. Les champs disponibles sont l’en-tête, le corps optionnel, le texte du bouton et le comportement en cas de clic de bouton.]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:80%"}

Si vous souhaitez diriger les utilisateurs vers une autre page de votre application ou site Web, modifiez le **comportement lors du clic** du bouton.

### Étape 5 : Styliser votre message (facultatif) {#styling}

Vous pouvez personnaliser la couleur de police et la couleur d’emphase du message à l’aide du sélecteur de **thème de couleur**.

![Onglet Composer de l’éditeur d’enquête simple avec le sélecteur de thème de couleur agrandi après avoir cliqué sur la palette de couleurs.]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## Analyser les résultats {#analytics}

Une fois votre campagne lancée, vous pouvez analyser les résultats en temps réel pour voir la répartition de chaque choix sélectionné. Si vous avez activé la [collecte d’attributs personnalisés](#custom-attributes), vous pouvez également créer des segments ou des campagnes de suivi pour les utilisateurs qui ont soumis l’enquête.

{% alert note %}
Les choix d’enquête supprimés apparaîtront toujours dans l’analyse, mais ne sont pas affichés comme choix pour les nouveaux utilisateurs.
{% endalert %}

Pour les définitions des indicateurs de l’enquête, reportez-vous au [glossaire des indicateurs de rapport][11] et filtrez par message In-App.

![Panneau de performance des messages In-App avec analyse des clics pour chaque choix et bouton dans l’enquête.]({% image_buster /assets/img/iam/iam-survey-analytics.png %}){: style="max-width:95%"}

Consultez les [rapports sur les messages In-App][4] pour voir la répartition des indicateurs de votre campagne.

### Currents {#currents}

Les choix sélectionnés circulent automatiquement vers Currents (Courants), sous le champ [**In-App Message Click Events**][6]`button_id` (Événements de clic de message In-App). Chaque choix est envoyé avec son identifiant unique universel (UUID).

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

Pour ce cas d’utilisation, utilisez une sélection à choix multiple, chaque choix correspondant à une fonctionnalité de l’application. Chaque choix a l’attribut personnalisé `favorite_features` défini à la sélection de l’utilisateur. Étant donné que ce cas d’utilisation implique un choix multiple, au terme de l’enquête, le profil de l’utilisateur est mis à jour avec l’attribut `favorite_features` défini à l’ensemble de toutes les options sélectionnées.

![][10]

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[3]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/
[5]: {{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/custom_event_and_attribute_management/
[6]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#api_fzzdoylmrtwe

[7]: {% image_buster /assets/img_archive/simple_survey_use_case_1.png %}
[8]: {% image_buster /assets/img_archive/simple_survey_use_case_2.png %}
[9]: {% image_buster /assets/img_archive/simple_survey_use_case_3.png %}
[10]: {% image_buster /assets/img_archive/simple_survey_use_case_4.png %}

[11]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
