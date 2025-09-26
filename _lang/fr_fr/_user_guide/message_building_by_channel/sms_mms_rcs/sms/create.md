---
nav_title: Création d’un SMS
article_title: Création d’un SMS
page_order: 5
description: "Cet article de référence couvre les étapes de génération et de création d’un SMS."
page_type: reference
alias: /create_sms_message/
tool:
  - Campaigns
channel:
  - SMS
search_rank: 1
---

# Création d’un SMS

> Les campagnes par SMS sont idéales pour atteindre directement vos clients et échanger avec eux par programmation. Vous pouvez utiliser Liquid et d’autres contenus dynamiques pour non seulement proposer une expérience originale à vos utilisateurs, mais aussi générer un environnement qui favorise et optimise une expérience utilisateur discrète avec votre marque. 

## Étape 1 : Choisissez où créer votre message

Vous ne savez pas si votre message doit être envoyé via une campagne ou un Canvas ? Les campagnes sont mieux adaptées aux campagnes de communication simples et uniques, tandis que les Canvas sont mieux adaptés aux parcours client en plusieurs étapes.

{% tabs %}
{% tab Campagne %}

**Étapes :**

1. Allez dans **Messagerie** > **Campagnes** et sélectionnez **Créer une campagne**.
2. Sélectionnez **SMS** ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Multicanal**.
3. Donnez un nom clair et significatif à votre campagne.
4. Ajoutez des [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) et des [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) si nécessaire.
   * Les balises facilitent la recherche et l’identification des campagnes, et la création de rapports. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), vous pouvez filtrer les éléments en fonction de certaines étiquettes spécifiques.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez choisir différentes plates-formes, types de messages et mises en page pour chacune de vos variantes ajoutées. Pour plus d'informations sur ce sujet, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
6. Sélectionnez un [groupe d'abonnement]({{site.baseurl}}/sms_rcs_subscription_groups/) pour vous assurer que vous envoyez votre message aux utilisateurs appropriés. Lors de la sélection d’un groupe d’abonnement, Braze ajoute automatiquement un filtre de segmentation, garantissant que seuls les utilisateurs abonnés recevront la campagne. Seuls les codes longs et les codes courts appartenant à ce groupe d’abonnement seront utilisés pour envoyer des SMS aux utilisateurs cibles.

{% alert tip %}
Si tous les messages de votre campagne vont être similaires ou avoir le même contenu, composez votre message avant d’ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copier à partir de la variante** dans la liste déroulante **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Étapes :**

1. [Créez votre canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l'aide du compositeur de canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape dans le Créateur de Canvas. Donnez un nom clair et significatif à votre étape.
3. Choisissez un [calendrier par étapes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) et spécifiez un délai si nécessaire.
4. Filtrez votre audience pour cette étape si nécessaire. Vous pouvez affiner davantage les destinataires de cette étape en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d’audience seront vérifiées après le délai au moment de l’envoi des messages.
5. Choisissez votre [comportement d'avancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choisissez les autres canaux de communication que vous souhaitez associer à votre message.

{% endtab %}
{% endtabs %}

## Étape 2 : Composez votre message SMS

Rédigez votre message en utilisant des langues et des personnalisations (Liquid, Contenu Connecté et emojis) selon les besoins. Assurez-vous de respecter nos limites de texte des messages pour réduire vos risques de dépassements.

{% alert important %}
Avant de continuer, lisez nos directives concernant les [segments de message SMS et les limites de copie]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/). Les segments de messages SMS sont les lots de caractères que les opérateurs de téléphonie utilisent pour mesurer les messages texte. Les messages étant facturés par segment de message, il est judicieux de comprendre les possibles divisions des messages.
{% endalert %}

![Éditeur de SMS dans Braze avec le message « Bonjour prénom, nous apprécions votre soutien ! Pourquoi ne pas passer dans l’un de nos magasins et leur montrer ce SMS pour bénéficier d’une remise exclusive ? Répondez STOP pour arrêter de recevoir des messages de notre part."]({% image_buster /assets/img/sms_campaign_compose.png %})

### Ajouter une carte de contact

Vous pouvez ajouter une carte de contact à votre message SMS pour permettre à vos clients d'ajouter facilement votre entreprise et vos coordonnées à leurs contacts. Vous pouvez attribuer des propriétés communes à ces cartes, telles que le nom de votre entreprise, le numéro de téléphone, l’adresse, l’e-mail et une petite photo. Consultez les [cartes de contact]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/) pour en savoir plus.

### Conseils

#### Utilisation de Liquid

{% raw %}
Si vous prévoyez d’utiliser Liquid, assurez-vous d’inclure une valeur par défaut pour la personnalisation choisie. De cette façon, si le profil utilisateur de votre destinataire est incomplet, il ne recevra pas de marque substitutive vide `Hi, !`, au lieu de son nom ou d’une phrase cohérente.
{% endraw %}

#### Générer une copie d'intelligence artificielle

Besoin d’aide pour créer un texte d’exception ? Essayez d'utiliser l'[assistant de rédaction de l'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Saisissez un nom ou une description du produit et l’IA générera un texte marketing semblant d’origine humaine pour une utilisation dans votre envoi de messages.

![Bouton Lancer le rédacteur IA, situé dans le champ Message de l’éditeur de SMS.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_sms.png %}){: style="max-width:60%"}

#### Création d'envois de messages de droite à gauche

L'aspect final des messages de droite à gauche dépend largement de la manière dont les fournisseurs de services les restituent. Pour connaître les meilleures pratiques en matière d'élaboration de messages de droite à gauche qui s'affichent le plus précisément possible, reportez-vous à la section [Création de messages de droite à gauche.]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/)

## Étape 3 : Prévisualiser et tester votre message

Braze recommande toujours de prévisualiser et de tester votre message avant de l’envoyer. Passez à l'onglet **Test** pour envoyer un SMS de test aux [groupes de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou à des utilisateurs individuels, ou prévisualisez le message en tant qu'utilisateur directement dans Braze.

![Prévisualisation du texte du SMS dans l’onglet Test de l’éditeur Dans la section de profil, le champ « Prénom » comporte « James ». Dans la section d’aperçu, le SMS indique maintenant « Bonjour James, nous apprécions votre soutien ! »]({% image_buster /assets/img/sms_campaign_test.png %})

{% alert tip %}
Si vous souhaitez tester le nombre de segments dans lesquels votre SMS peut être divisé, testez la longueur de votre texte avec notre [calculateur de segments SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-calculator).
{% endalert %}

## Étape 4 : Créer le reste de votre campagne ou de votre Canvas

{% tabs %}
{% tab Campagne %}

Concevez ensuite le reste de votre campagne. Voir les sections suivantes pour plus de détails sur la meilleure façon d'utiliser nos outils pour créer des messages SMS.

#### Choisir un calendrier ou un déclencheur pour la livraison

Les SMS peuvent être livrés selon une heure planifiée, une action ou un déclencheur API. Pour plus d'informations, consultez [Planifier votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Pour une livraison basée sur l'action, vous pouvez également définir la durée de la campagne et les [Heures de silence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

C'est également à cette étape que vous pouvez spécifier les contrôles de réception/distribution, par exemple en autorisant les utilisateurs à se [réinscrire]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) pour recevoir la campagne ou en activant les règles de [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Choisir les utilisateurs à cibler

Ensuite, vous devez [cibler les utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) en choisissant des segments ou des filtres pour réduire votre audience. Vous devriez déjà avoir choisi le groupe d'abonnement, ce qui restreint les utilisateurs par le niveau ou la catégorie de communication qu'ils souhaitent avoir avec vous. Au cours de cette étape, vous allez sélectionner une audience plus importante dans vos segments et allez restreindre peut-être davantage ce segment à l’aide de nos filtres. Vous recevez automatiquement un aperçu de ce à quoi ressemble la population approximative du segment à ce moment-là. Gardez à l’esprit que l’appartenance à un segment exact est toujours calculée juste avant l’envoi du message.

{% alert tip %}
Vous êtes intéressé par le reciblage de SMS ? Pour en savoir plus, consultez notre [article sur le reciblage]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) par SMS.
{% endalert %}

#### Sélectionner des événements de conversion

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), après avoir reçu une campagne. Vous avez la possibilité d’autoriser une fenêtre allant jusqu’à 30 jours pendant laquelle une conversion sera comptée si l’utilisateur entreprend l’action spécifiée.

Les événements de conversion vous aident à évaluer le succès de votre campagne. Par exemple :

- Si vous utilisez un géociblage pour déclencher un message SMS dont l’objectif final est un achat de la part de l’utilisateur, configurez l’événement de conversion sur `Purchase`.
- Si vous essayez de diriger l’utilisateur vers votre application, configurez l’événement de conversion sur `Starts Session`.

Vous pouvez également définir des événements de conversion personnalisés propre à votre cas d’utilisation spécifique. Soyez créatif et réfléchissez à la façon dont vous voulez vraiment évaluer la réussite de cette campagne.

{% endtab %}

{% tab Canvas %}

Si vous ne l’avez pas déjà fait, complétez les sections restantes de votre composant de Canvas. Pour plus de détails sur la manière de créer le reste de votre Canvas, de mettre en œuvre les tests multivariés et la sélection intelligente, et plus encore, reportez-vous à l'étape [Créer votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation sur le Canvas.

{% endtab %}
{% endtabs %}

## Étape 5 : Revue et déploiement

Quand vous avez fini de concevoir votre campagne ou votre Canvas, vérifiez ses détails, testez-le et envoyez-le !

Ensuite, consultez [le rapport SMS]({{site.baseurl}}/sms_mms_rcs_reporting/) pour savoir comment vous pouvez accéder aux résultats de vos campagnes SMS.
