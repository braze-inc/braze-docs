---
nav_title: "Sondage simple"
article_title: Message In-App de Sondage Simple
page_order: 1.5
page_type: Référence
description: "Cet article de référence couvre la façon de collecter les attributs, les idées et les préférences des utilisateurs pour activer la stratégie de votre campagne en utilisant les nouvelles enquêtes de messages intégrées à l'application."
channel:
  - messages intégrés à l'application
tool:
  - Modèles
---

# Message simple de l'enquête dans l'application

Utilisez le nouveau modèle de message **Sondage simple** dans l'application pour collecter les attributs, les aperçus et les préférences de l'utilisateur qui alimentent votre stratégie de campagne.

Par exemple, demandez aux utilisateurs comment ils aimeraient utiliser votre application, en savoir plus sur leurs préférences personnelles, ou même poser des questions sur leur satisfaction à l'égard d'une caractéristique particulière.

![Exemples d'enquête simples]({% image_buster /assets/img/iam/iam-survey.png %})

## Exigences du SDK {#supported-sdk-versions}

Ce message dans l'application ne sera livré qu'aux appareils qui prennent en charge [Flex CSS](https://caniuse.com/?search=flex), et doit avoir au moins les [versions SDK]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions) ci-dessous :

{% sdk_min_versions web:2.5.0 android:8.0.0 ios:3.23.0 %}

## Création d'une enquête {#create}

Lors de la création d'un message [dans l'application][1], sélectionnez **Sondage simple** pour votre **type de message**.

![Type de message de sondage simple]({% image_buster /assets/img/iam/survey-message-type.png %}){: style="largeur-max-80%"}

Ce modèle d'enquête est pris en charge pour les applications mobiles et les navigateurs Web. N'oubliez pas de vérifier que vos SDK sont sur les [versions minimales](#supported-sdk-versions) requises pour cette fonctionnalité.

### Étape 1 : Ajouter votre question de sondage

Pour commencer à construire votre enquête, ajoutez votre question au champ **Entête** de l'enquête. Si vous le souhaitez, vous pouvez ajouter un message facultatif **Body** qui apparaîtra sous votre question de sondage.

![Question de sondage simple]({% image_buster /assets/img/iam/iam-survey2.png %})

{% alert tip %}
Ces champs peuvent inclure à la fois des Liquides et des émoticônes, alors soyez fantaisie!
{% endalert %}

### Étape 2 : Choisissez entre un ou plusieurs choix {#single-multiple-choice}

Utilisez l'option Single vs. Choix multiple pour contrôler si un utilisateur peut sélectionner un seul choix ou plusieurs choix. Vous pouvez ajouter jusqu'à 12 choix dans un sondage.

![Choix multiple unique]({% image_buster /assets/img/iam/single-multiple-choice.png %}){: style="largeur-max-70%"}

{% alert tip %}
Votre **texte d'aide** sera automatiquement mis à jour lorsque vous basculez entre **sélection à choix unique** et **sélection à choix multiple** pour permettre aux utilisateurs de savoir combien de choix ils peuvent sélectionner.
{% endalert %}

### Étape 3 : Récupérer les attributs personnalisés {#custom-attributes}

Sélectionnez **Loguer les attributs lors de la soumission** pour collecter les attributs en fonction de la soumission de l'utilisateur. Vous pouvez utiliser cette option pour créer de nouveaux segments et campagnes de repositionnement. Par exemple, dans un sondage de satisfaction, vous pouvez envoyer un e-mail de suivi à tous les utilisateurs qui n'étaient pas satisfaits.

![Attributs personnalisés]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="largeur-max-70%"}

Pour ajouter un attribut personnalisé à chaque choix, sélectionnez un nom d'attribut personnalisé dans le menu déroulant (ou créez un nouveau), puis entrez la valeur à définir lorsque ce choix est soumis. Vous pouvez créer un nouvel attribut personnalisé dans votre [Page Paramètres][5].

Par exemple, dans une enquête sur les préférences de notification, vous pouvez faire de chaque choix un attribut booléen (vrai/faux) pour permettre aux utilisateurs de sélectionner les sujets qui les intéressent. Si un utilisateur coche le choix "Promotions", qui va mettre à jour leur [profil utilisateur][3] avec l'attribut personnalisé `Sujet de Promotions` défini à `true`. Si le choix n'est pas coché, ce même attribut restera inchangé.

![Attributs personnalisés de choix]({% image_buster /assets/img/iam/iam-survey3.png %}){: style="largeur-max-70%"}

Vous pouvez ensuite créer un segment pour les utilisateurs avec `Promotions Topic = true` pour vous assurer que seuls les utilisateurs intéressés par vos promotions recevront les campagnes appropriées.

{% alert important %}
Lorsque la collection d'attributs personnalisés est activée, les choix qui partagent le même nom d'attribut personnalisé seront combinés dans un tableau.
{% endalert %}

### Étape 4 : Choisissez le comportement de soumission

Une fois qu'un utilisateur soumet sa réponse, vous pouvez éventuellement afficher une page de confirmation, ou tout simplement fermer le message.

Une page de confirmation est un excellent endroit pour remercier les utilisateurs pour leur temps ou fournir des informations supplémentaires. Vous pouvez personnaliser l'appel à l'action sur cette page pour guider les utilisateurs vers une autre page de votre application ou site Web.

Modifier le texte de votre bouton et le comportement du clic dans la section **Soumettre le bouton** au bas de l’onglet **Enquête**:

![Option de confirmation]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="largeur-max-70%"}

Si vous choisissez d'ajouter une page de confirmation, passez à l'onglet **Page de confirmation** pour personnaliser votre message :

![Page de confirmation]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="largeur-max-70%"}

Si vous voulez guider les utilisateurs vers une autre page de votre application ou de votre site web, modifiez le **comportement en clic** du bouton.

### Étape 5 : Styliser votre message (facultatif) {#styling}

Vous pouvez personnaliser la couleur de la police et la couleur d'accentuation du message en utilisant le sélecteur **Color Theme**.

![Sélecteur de thème de couleur]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="largeur-max-80%"}

## Analyser les résultats {#analytics}

Une fois votre campagne lancée, vous pouvez analyser les résultats en temps réel pour voir la répartition de chaque choix sélectionné. Si vous avez activé [collection d'attributs personnalisés](#custom-attributes), vous pourrez également créer de nouveaux segments ou des campagnes de suivi pour les utilisateurs qui ont soumis l'enquête.

{% alert note %}
Les choix d’enquête supprimés apparaîtront toujours dans les analytiques mais ne seront pas affichés comme un choix pour les nouveaux utilisateurs.
{% endalert %}

Pour les définitions des métriques d'enquête, reportez-vous au [Glossaire des métriques de rapport][11] et filtrez par "Message In-App.

![Analyses]({% image_buster /assets/img/iam/iam-survey-analytics.png %}){: style="largeur-max:90%"}

Consultez [Reporting & Analytics][4] pour une répartition des métriques de votre campagne.

### Courants {#currents}

Les choix sélectionnés passeront automatiquement à travers les courants, sous le champ [__Message dans l'application Cliquez sur Événements__][6] `button_id`. Chaque choix sera envoyé avec son identifiant universellement unique (UUID).

## Cas d'utilisation

### Satisfaction de l'utilisateur

**Objectif:** Mesurer la satisfaction du client et envoyer des campagnes de retour aux utilisateurs qui ont laissé de faibles scores.

Ici, nous utilisons une sélection à choix unique, avec des choix allant de "très insatisfait" à "très satisfait". Chaque choix a l'attribut personnalisé `customer_satisfaction` défini à un nombre de 1 à 5, 1 étant le moins satisfait et 5 le plus satisfait.

Après avoir lancé votre enquête, vous pouvez ensuite cibler vos campagnes de retour aux utilisateurs qui ont déclaré être "très mécontents " ou "déçus", qui sont des utilisateurs avec `customer_satisfaction` à 1 ou 2.

!\[Satisfaction de l'utilisateur\]\[7\]

### Identifier les objectifs du client

**Objectif:** Identifiez les principales raisons pour lesquelles les utilisateurs visitent votre application.

Ici, nous utilisons une sélection à choix unique, chaque choix étant une raison courante qu'un utilisateur peut visiter votre application. Chaque choix a l'attribut personnalisé `product_goal` défini sur le sujet de la casse.

Par exemple, si l'utilisateur sélectionne "Mettre à jour mon compte", cela définira `product_goal = upgrade` sur le profil de l'utilisateur.

!\[Identifier les objectifs clients\]\[8\]

### Améliorer les taux de conversion

**Objectif :** Comprendre pourquoi les clients ne sont pas en train de mettre à niveau ou d’acheter.

Ici, nous utilisons la sélection à choix unique, chaque choix étant une raison courante pour laquelle un utilisateur ne peut pas passer à un compte Premium. Chaque choix a l'attribut personnalisé `upgrade_reason` défini à la sélection de l'utilisateur.

Par exemple, si l'utilisateur sélectionne "Too Expensive", cela définira `upgrade_reason = expensive` sur le profil de l'utilisateur. Vous pouvez cibler ces utilisateurs sur des campagnes promotionnelles telles que des remises ou des essais gratuits.

!\[Améliore les taux de conversion\]\[9\]

### Fonctionnalités favorites

**Objectif:** Comprendre qui permet aux clients de profiter de l'utilisation.

Ici, nous utilisons la sélection à choix multiple et chaque choix est une fonctionnalité de l'application. Chaque choix a l'attribut personnalisé `favite_features` défini à la sélection de l'utilisateur. Parce que ce cas d'utilisation implique plusieurs choix, une fois que l'utilisateur a répondu à l'enquête, leur profil sera mis à jour avec l'attribut `favite_features` défini sur un tableau de toutes les options sélectionnées.

!\[Fonctionnalités favorites\]\[10\]
[7]: {% image_buster /assets/img_archive/simple_survey_use_case_1.png %} [8]: {% image_buster /assets/img_archive/simple_survey_use_case_2. ng %} [9]: {% image_buster /assets/img_archive/simple_survey_use_case_3.png %} [10]: {% image_buster /assets/img_archive/simple_survey_use_case_4.png %}

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[3]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/
[5]: {{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/custom_event_and_attribute_management/
[6]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#api_fzzdoylmrtwe

[11]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
