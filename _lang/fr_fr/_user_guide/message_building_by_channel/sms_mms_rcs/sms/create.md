---
nav_title: "Création d'un message SMS"
article_title: "Création d'un message SMS"
page_order: 5
description: "Cet article de référence présente les étapes à suivre pour créer un message SMS."
page_type: reference
alias: /create_sms_message/
tool:
  - Campaigns
channel:
  - SMS
search_rank: 1
---

# Création d'un message SMS

> Les campagnes SMS sont idéales pour atteindre directement vos clients et dialoguer avec eux de manière programmatique. Vous pouvez utiliser Liquid et d'autres contenus dynamiques pour créer une expérience personnelle avec vos utilisateurs et créer un environnement qui favorise et améliore une expérience discrète de l'utilisateur avec votre marque. 

## Étape 1 : Choisissez où créer votre message

Vous ne savez pas si votre message doit être envoyé par le biais d'une campagne ou d'un canvas ? Les campagnes sont plus adaptées aux campagnes d'envoi de messages simples et uniques, tandis que les Canevas sont plus adaptés aux parcours utilisateurs en plusieurs étapes.

{% tabs %}
{% tab Campaign %}

**Les étapes :**

1. Allez dans **Messagerie** > **Campagnes** et sélectionnez **Créer une campagne.**
2. Sélectionnez **SMS** ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Multicanal**.
3. Donnez à votre campagne un nom clair et significatif.
4. Ajoutez des [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) et des [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) si nécessaire.
   * Les étiquettes facilitent la recherche de vos campagnes et permettent de créer des rapports. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), vous pouvez filtrer par des étiquettes particulières.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez choisir des plateformes, des types de messages et des mises en page différents pour chacune de vos variantes ajoutées. Pour en savoir plus sur ce sujet, reportez-vous aux [tests multivariés et aux tests A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
6. Sélectionnez un [groupe d'abonnement]({{site.baseurl}}/sms_rcs_subscription_groups/) pour vous assurer que vous envoyez votre message aux utilisateurs appropriés. Lors de la sélection d'un groupe d'abonnement, Braze ajoutera automatiquement un filtre de segmentation, garantissant que seuls les utilisateurs abonnés recevront la campagne. Seuls les codes longs et les codes courts appartenant à ce groupe d'abonnement seront utilisés pour envoyer des SMS aux utilisateurs ciblés.

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

## Étape 2 : Composez votre message SMS

Rédigez votre message en utilisant les langues et la personnalisation (Liquid, contenu connecté et emojis) selon vos besoins. Veillez à respecter les limites fixées pour les messages afin de réduire les risques de frais supplémentaires.

{% alert important %}
Avant de poursuivre, lisez nos lignes directrices concernant les [segments de messages et les limites d'envoi par SMS.]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/) Les segments de messages SMS sont les lots de caractères que les opérateurs téléphoniques utilisent pour mesurer les messages texte. Les messages sont facturés par segment de message, il est donc utile de comprendre les nuances de la répartition des messages.
{% endalert %}

SMS au compositeur dans Braze avec le message "Salut first_name, nous apprécions votre soutien ! Pourquoi ne pas vous rendre dans l'un de nos magasins et leur montrer ce SMS pour bénéficier d'une réduction exclusive ? Répondez STOP pour ne plus recevoir de messages de notre part."]({% image_buster /assets/img/sms_campaign_compose.png %})

### Ajouter une carte de contact

Vous pouvez ajouter une carte de contact à votre message SMS pour permettre à vos clients d'ajouter facilement votre entreprise et vos coordonnées à leurs contacts. Vous pouvez attribuer des propriétés communes à ces cartes, telles que le nom de votre entreprise, votre numéro de téléphone, votre adresse, votre e-mail et une petite photo. Consultez les [cartes de contact]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/) pour en savoir plus.

### Conseils

#### Utilisation du liquide

{% raw %}
Si vous envisagez d'utiliser Liquid, veillez à inclure une valeur par défaut pour la personnalisation que vous avez choisie. Ainsi, si le profil utilisateur du destinataire est incomplet, il ne recevra pas un marque substitutive vide `Hi, !`, au lieu de son nom ou d'une phrase cohérente.
{% endraw %}

#### Générer des copies d'intelligence artificielle

Vous avez besoin d'aide pour créer un texte percutant ? Essayez d'utiliser l'[assistant de rédaction de l'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Saisissez le nom ou la description d'un produit et l'intelligence artificielle générera un texte marketing de type humain à utiliser dans vos messages.

!Lancez le bouton du Copywriter de l'intelligence artificielle, situé/localisé dans le champ Message du compositeur de SMS.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_sms.png %}){: style="max-width:60%"}

#### Création d'envois de droite à gauche

L'aspect final des messages de droite à gauche dépend largement de la manière dont les fournisseurs de services les restituent. Pour connaître les meilleures pratiques en matière d'élaboration de messages de droite à gauche qui s'affichent le plus précisément possible, reportez-vous à la section [Création de messages de droite à gauche.]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/)

## Étape 3 : Prévisualisez et testez votre message

Braze recommande toujours de prévisualiser et de tester votre message avant de l'envoyer. Passez à l'onglet **Test** pour envoyer un SMS de test à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou à des utilisateurs individuels, ou prévisualiser le message en tant qu'utilisateur directement dans Braze.

\![Prévisualisation de la copie du SMS à partir de l'onglet Test du compositeur. Dans la section profil, le champ Prénom est défini sur "James". Dans la section de prévisualisation, le SMS indique désormais "Bonjour James, nous apprécions votre soutien !".]({% image_buster /assets/img/sms_campaign_test.png %})

{% alert tip %}
Si vous souhaitez tester le nombre de segments dans lesquels votre SMS peut être divisé, testez la longueur de votre texte à l'aide de notre [calculateur de segments SMS.]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-calculator)
{% endalert %}

## Étape 4 : Créez le reste de votre campagne ou Canvas

{% tabs %}
{% tab Campaign %}

Ensuite, créez le reste de votre campagne. Vous trouverez dans les sections suivantes de plus amples informations sur la manière d'utiliser au mieux nos outils pour créer des messages SMS.

#### Choisissez la planification ou le déclencheur de la réception/distribution

Les messages SMS peuvent être envoyés en fonction d'une heure planifiée, d'une action ou d'un déclencheur API. Pour en savoir plus, reportez-vous à la section [Planification de votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Pour la réception/distribution par événement, vous pouvez également définir la durée de la campagne et les heures calmes.

C'est également à cette étape que vous pouvez spécifier les contrôles de réception/distribution, par exemple en autorisant les utilisateurs à se [réinscrire]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) pour recevoir la campagne ou en activant les règles de [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Choisissez les utilisateurs à cibler

Ensuite, vous devez [cibler les utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) en choisissant des segments ou des filtres pour réduire votre audience. Vous devriez avoir déjà choisi le groupe d'abonnement, qui restreint les utilisateurs en fonction du niveau ou de la catégorie de communication qu'ils souhaitent avoir avec vous. 

{% multi_lang_include target_audiences.md %}

Au cours de cette étape, vous sélectionnerez l'audience la plus large à partir de vos segments, et vous restreindrez davantage ce segment à l'aide de nos filtres, si vous le souhaitez. Vous obtiendrez automatiquement un aperçu de ce à quoi ressemble actuellement cette segmentation approximative de la population. N'oubliez pas que l'appartenance exacte à un segment est toujours calculée juste avant l'envoi du message.

{% alert tip %}
Intéressé par le reciblage par SMS ? Consultez notre [article sur le reciblage par]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) SMS pour en savoir plus.
{% endalert %}

#### Choisissez des événements de conversion

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), après avoir reçu une campagne. Vous avez la possibilité d'autoriser une fenêtre de 30 jours maximum pendant laquelle une conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée.

Les événements de conversion vous aident à mesurer le succès de votre campagne. Par exemple :

- Si vous utilisez le géociblage pour déclencher un message SMS dont l'objectif final est que l'utilisateur effectue un achat, définissez l'événement de conversion sur `Purchase`.
- Si vous essayez de conduire l'utilisateur vers votre application, définissez l'événement de conversion sur `Starts Session`.

Vous pouvez également définir des événements de conversion personnalisés en fonction de votre cas d'utilisation spécifique. Faites preuve de créativité et réfléchissez à la manière dont vous souhaitez réellement mesurer le succès de cette campagne.

{% endtab %}

{% tab Canvas %}

Si vous ne l'avez pas encore fait, complétez les sections restantes de votre composante Canvas. Pour plus de détails sur la manière de créer le reste de votre Canvas, de mettre en œuvre les tests multivariés et la sélection intelligente, et plus encore, reportez-vous à l'étape [Créer votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation sur le Canvas.

{% endtab %}
{% endtabs %}

## Étape 5 : Examiner et déployer

Une fois que vous avez fini de créer la dernière partie de votre campagne ou de votre canvas, passez en revue ses détails, testez-le, puis envoyez-le !

Ensuite, consultez les [rapports sur les SMS]({{site.baseurl}}/sms_mms_rcs_reporting/) pour savoir comment vous pouvez accéder aux résultats de vos campagnes SMS.
