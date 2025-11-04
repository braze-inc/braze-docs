---
nav_title: "Création d'un message LINE"
article_title: "Création d'un message LINE"
page_order: 1
description: "Cet article explique comment créer une campagne de messages LINE ou Canvas."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/
---

# Création d'un message LINE

> Les campagnes LINE permettent d'atteindre directement vos clients et de dialoguer avec eux de manière programmatique. Vous pouvez utiliser Liquid et d'autres contenus dynamiques pour créer une expérience personnelle avec vos utilisateurs et créer un environnement qui favorise et améliore une expérience discrète de l'utilisateur avec votre marque.

## Conditions préalables

Avant de créer un message LINE, procédez comme suit :

1. Lisez l'aperçu de LINE.
2. Reconnaître les politiques, les limites et les règles de contenu.
3. [Établissez votre connexion LINE]({{site.basesurl}}/user_guide/message_building_by_channel/line/line_setup/).

L'envoi de messages LINE à partir de Braze est prélevé sur les crédits de messages de votre compte.

## Étape 1 : Choisissez où créer votre message

Vous ne savez pas si votre message doit être envoyé par le biais d'une campagne ou d'un canvas ? Les campagnes sont plus adaptées aux campagnes d'envoi de messages simples et uniques, tandis que les Canevas sont plus adaptés aux parcours utilisateurs en plusieurs étapes.

{% tabs %}
{% tab Campaign %}

**Les étapes :**

1. Allez dans **Messagerie** > **Campagnes** et sélectionnez **Créer une campagne.**
2. Sélectionnez **LIGNE** ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Campagne multicanal**.
3. Donnez à votre campagne un nom clair et significatif.
4. Ajoutez des [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) et des [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) si nécessaire.
   * Les étiquettes facilitent la recherche de vos campagnes et permettent de créer des rapports.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez choisir des plateformes, des types de messages et des mises en page différents pour chacune de vos variantes ajoutées. Pour en savoir plus sur ce sujet, reportez-vous aux [tests multivariés et aux tests A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si tous les messages de votre campagne seront similaires ou auront le même contenu, composez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copier à partir de la variante** dans la liste déroulante **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Les étapes :**

1. [Créez votre canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l'aide du compositeur de canvas.
2. Après avoir configuré votre canvas, ajoutez une étape dans le générateur de canvas. Donnez à votre démarche un nom clair et significatif.
3. Choisissez une [planification des étapes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) et spécifiez un délai si nécessaire.
4. Filtrez votre audience pour cette étape si nécessaire. Vous pouvez encore affiner les destinataires de cette étape en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d'audience seront vérifiées après le délai au moment de l'envoi des messages.
5. Choisissez votre [comportement en matière d'avancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choisissez les autres canaux de communication que vous souhaitez associer à votre message.

{% endtab %}
{% endtabs %}

## Étape 2 : Composez votre message LINE

Rédigez votre message en utilisant la personnalisation (comme le contenu liquide ou connecté) si nécessaire. LINE autorise jusqu'à cinq bulles de message dans chaque message, qui peuvent correspondre à l'une des mises en page de messages disponibles : texte, image, riche ou à base de cartes.

\![LINE composer avec un message affiché dans l'aperçu.]({% image_buster /assets/img/line/line_composer.png %})

### Conseils

#### Utilisation du liquide

Si vous prévoyez d'utiliser Liquid, veillez à inclure une valeur par défaut pour votre personnalisation. Vous éviterez ainsi que les destinataires dont le profil utilisateur est incomplet ne reçoivent un marque substitutive vide. Par exemple, au lieu qu'un utilisateur reçoive le message "Bonjour !", il pourrait recevoir le message "Bonjour, nouvel abonné !".

#### Création d'envois de droite à gauche

L'aspect final des messages de droite à gauche dépend largement de la manière dont les fournisseurs de services les restituent. Pour connaître les meilleures pratiques en matière d'élaboration de messages de droite à gauche qui s'affichent le plus précisément possible, reportez-vous à la section [Création de messages de droite à gauche.]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/)

## Étape 3 : Prévisualisez et testez votre message

Passez à l'onglet **Test** pour envoyer un message LINE de test à des groupes de test de contenu ou à des utilisateurs individuels, ou prévisualisez le message en tant qu'utilisateur directement dans Braze.

L'onglet "Tests" affiche un aperçu d'un message de test.]({% image_buster /assets/img/line/test_preview.png %})

## Étape 4 : Créez le reste de votre campagne ou Canvas

{% tabs %}
{% tab Campaign %}

Créez le reste de votre campagne. Vous trouverez dans les sections suivantes de plus amples informations sur la manière d'utiliser au mieux nos outils pour créer des messages LINE.

### Choisissez la planification ou le déclencheur de la réception/distribution

Les messages LINE peuvent être envoyés en fonction d'une heure planifiée, d'une action ou d'un déclencheur API. Pour en savoir plus sur les options de planification et de déclencheur, reportez-vous à la section [Planification de votre campagne.]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)

Vous pouvez spécifier des contrôles de réception/distribution, par exemple en autorisant les utilisateurs à se [réinscrire]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) pour recevoir la campagne ou en activant des règles de [limitation de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping). Pour la réception/distribution par événement, vous pouvez également définir la durée de la campagne et les heures calmes.

### Choisissez les utilisateurs à cibler

[Ciblez les utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) en choisissant des segments ou des filtres pour réduire votre audience. Vous devriez avoir déjà choisi le groupe d'abonnement, qui restreint les utilisateurs en fonction du niveau ou de la catégorie de communication qu'ils souhaitent avoir avec vous. 

Sélectionnez l'audience la plus large à partir de vos segments et, si vous le souhaitez, réduisez encore cette segmentation à l'aide de nos [filtres]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/). Vous obtiendrez automatiquement un aperçu de ce à quoi ressemble la population de ce segment approximatif à l'heure actuelle. N'oubliez pas que l'appartenance exacte à un segment est toujours calculée juste avant l'envoi du message.

### Choisissez des événements de conversion

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), après avoir reçu une campagne. Vous avez la possibilité d'autoriser une fenêtre de 30 jours maximum pendant laquelle une conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée.

Les événements de conversion vous aident à mesurer le succès de votre campagne. Par exemple :

- Si vous utilisez le géociblage pour déclencher un message LINE dont l'objectif final est que l'utilisateur effectue un achat, définissez l'événement de conversion sur `Purchase`.
- Si vous essayez de conduire l'utilisateur vers votre application, définissez l'événement de conversion sur `Starts Session`.

Vous pouvez également définir des événements de conversion personnalisés en fonction de votre cas d'utilisation spécifique. Faites preuve de créativité et réfléchissez à la manière dont vous souhaitez mesurer le succès de cette campagne.

{% endtab %}
{% tab Canvas %}

Si vous ne l'avez pas encore fait, complétez les sections restantes de votre Canvas. Pour plus de détails sur la manière de créer le reste de votre Canvas, d'utiliser les tests multivariés et la sélection intelligente, et plus encore, reportez-vous à la section [Créer un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).

{% endtab %}
{% endtabs %}

## Étape 5 : Examiner et déployer

Une fois que vous avez fini de créer la dernière partie de votre campagne ou de votre canvas, passez en revue ses détails, testez-le, puis envoyez-le !

Ensuite, consultez les [rapports LINE]({{site.baseurl}}/line/reporting/) pour savoir comment vous pouvez accéder aux résultats de vos campagnes LINE.


