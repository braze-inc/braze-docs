---
nav_title: Création d’un SMS
article_title: Création d’un SMS
page_order: 5
description: "Cet article de référence couvre les étapes de génération et de création d’un SMS."
page_type: reference
tool:
  - Campagnes
channel:
  - SMS
search_rank: 3
---

# Création d’un SMS

> Les campagnes par SMS sont idéales pour atteindre directement vos clients et échanger avec eux par programmation. Vous pouvez utiliser Liquid et d’autres contenus dynamiques pour non seulement proposer une expérience originale à vos utilisateurs, mais aussi générer un environnement qui favorise et optimise une expérience utilisateur discrète avec votre marque. 

## Étape 1 : Choisissez où créer votre message

Vous ne savez pas si votre message doit être envoyé via une campagne ou un Canvas ? Les campagnes sont préférables pour des messages simples, tandis que les Canvas se prêtent davantage aux expériences utilisateur en plusieurs étapes.

{% tabs %}
{% tab Campagne %}

**Étapes :**

1. Dans la page **Campagnes**, cliquez sur <i class="fas fa-plus"></i>Create Campaign**Créer une campagne**.
2. Sélectionnez **SMS**, ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Campagne multicanaux**.
3. Nommez votre campagne de manière claire et pertinente.
4. Si nécessaire, ajoutez des [Équipes]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/) et des [Tags.]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)
   * Les tags facilitent la recherche et l’identification des campagnes, et la création de rapports. Par exemple, lorsque vous utilisez le [Créateur de rapports]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/report_builder/), vous pouvez filtrer les éléments en fonction de tags spécifiques.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez choisir différentes plates-formes, types de messages et mises en page pour chacune de vos variantes ajoutées. Pour plus d’informations sur cette rubrique, consultez [Tests a/b et multivariés]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
6. Sélectionnez un [groupe d’abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) pour vous assurer d’envoyer votre message aux utilisateurs appropriés. Lors de la sélection d’un groupe d’abonnement, Braze ajoute automatiquement un filtre de segmentation, garantissant que seuls les utilisateurs abonnés recevront la campagne. Seuls les codes longs et les codes courts appartenant à ce groupe d’abonnement seront utilisés pour envoyer des SMS aux utilisateurs cibles.

{% alert tip %}
Si tous les messages de votre campagne vont être similaires ou avoir le même contenu, composez votre message avant d’ajouter d’autres variantes. Vous pouvez ensuite choisir **Copier à partir de la variante** dans le menu déroulant **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Étapes :**

1. [Créez votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l’aide de l’Assistant Canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape dans le Créateur de Canvas. Donnez un nom clair et significatif à votre étape.
3. Choisissez une [planification des étapes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) et indiquez un délai si besoin est.
4. Filtrez votre audience pour cette étape si nécessaire. Vous pouvez affiner davantage les destinataires de cette étape en spécifiant des segments et en ajoutant plus de filtres. Les options d’audience seront vérifiées après le délai au moment de l’envoi des messages.
5. Choisissez votre [comportement d’avancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choisissez les autres canaux de messagerie que vous souhaitez associer à votre message.

{% endtab %}
{% endtabs %}

## Étape 2 : Composer votre SMS

Composer un SMS en toute facilité ! Vous n’avez qu’à rédiger votre message, et utilisez les langages et la personnalisation (Liquid, contenu connecté et émojis) de votre choix si nécessaire. Assurez-vous de respecter nos limites de texte des messages pour réduire vos risques de dépassements.

{% alert important %}
Avant de poursuivre, lisez nos directives sur les [segments de messages SMS et limites de texte]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/). Les segments de messages SMS sont les lots de caractères que les opérateurs en téléphonie utilisent pour mesurer les messages texte. Les messages étant facturés par segment de message, il est judicieux de comprendre les possibles divisions des messages.
{% endalert %}

![Éditeur de SMS dans Braze avec le message « Bonjour _prénom, nous apprécions votre soutien ! Pourquoi ne pas passer dans l’un de nos magasins et leur montrer ce SMS pour bénéficier d’une remise exclusive ? » Répondez STOP pour ne plus recevoir des messages de notre part."]({% image_buster /assets/img/sms_campaign_compose.png %})

{% alert tip %}
{% raw %}
Si vous prévoyez d’utiliser Liquid, assurez-vous d’inclure une valeur par défaut pour la personnalisation choisie. De cette façon, si le profil utilisateur de votre destinataire est incomplet, il ne recevra pas un simple « Bonjour   !» sans son prénom ou une phrase cohérente.
{% endraw %}
{% endalert %}

Besoin d’aide pour créer un texte d’exception ? Essayez d’utiliser l’[assistant de rédaction IA]({{site.baseurl}}/user_guide/intelligence/ai_copywriting/). Saisissez un nom ou une description du produit et l’IA générera un texte marketing semblant d’origine humaine pour une utilisation dans votre message.

![Bouton Lancer l’IA de rédaction, situé dans le champ Message de l’éditeur de SMS.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_sms.png %}){: style="max-width:60%"}

### Cartes de visite

Si vous le souhaitez, vous pouvez ajouter une carte de visite à votre SMS pour que vos clients puissent facilement ajouter votre entreprise et vos coordonnées à leurs contacts. Vous pouvez attribuer des propriétés communes à ces cartes, telles que le nom de votre entreprise, le numéro de téléphone, l’adresse, l’e-mail et une petite photo. Consultez [Cartes de visite]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/contact_card/) pour en savoir plus.

## Étape 3 : Prévisualiser et tester votre message

Braze recommande toujours de prévisualiser et de tester votre message avant de l’envoyer. Allez dans l’onglet **Test** pour envoyer un SMS test à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou des utilisateurs uniques, ou prévisualisez le message en tant qu’utilisateur directement dans Braze.

![Prévisualisation du texte du SMS dans l’onglet Test de l’éditeur Dans la section de profil, le champ « Prénom » comporte « James ». Dans la section d’aperçu, le SMS indique maintenant « Bonjour James, nous apprécions votre soutien ! »"]({% image_buster /assets/img/sms_campaign_test.png %})

{% alert tip %}
Si vous souhaitez tester le nombre de segments dans lequel votre SMS risque d’être divisé, testez la longueur de votre texte avec notre [calculatrice de segments SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-calculator).
{% endalert %}

## Étape 4 : Créer le reste de votre campagne ou Canvas

{% tabs %}
{% tab Campagne %}

Concevez ensuite le reste de votre campagne. Consultez les sections suivantes pour plus de détails sur la façon de mieux utiliser nos outils pour créer des messages SMS.

#### Choisir une planification de livraison ou un déclencheur

Les SMS peuvent être livrés selon une heure planifiée, une action ou un déclencheur API. Pour en savoir plus, consultez la section [Planification de votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Pour une livraison par événement, vous pouvez également définir la durée de la campagne et les [Heures calmes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

Cette étape permet également de spécifier les contrôles de livraison, comme permettre aux utilisateurs de devenir [rééligibles]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) pour recevoir la campagne ou activer les règles de [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Choisir les utilisateurs à cibler

Ensuite, vous devez [cibler des utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) en choisissant des segments ou des filtres pour limiter votre public. Vous devez avoir déjà choisi le groupe d’abonnement, qui restreint les utilisateurs par niveau ou la catégorie de communication qu’ils souhaitent avoir avec vous. Au cours de cette étape, vous allez sélectionner une audience plus importante dans vos segments et allez restreindre peut-être davantage ce segment à l’aide de nos filtres. Vous recevez automatiquement un aperçu de ce à quoi ressemble la population approximative du segment à ce moment-là. Gardez à l’esprit que l’appartenance à un segment exact est toujours calculée juste avant l’envoi du message.

{% alert tip %}
Vous êtes intéressé par le reciblage de SMS ? Consultez notre article [Reciblage des SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) pour en savoir plus. 
{% endalert %}

#### Choisir des événements de conversion

Braze vous permet de suivre à quelle fréquence les utilisateurs effectuent des actions spécifiques, des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), après avoir reçu une campagne. Vous avez la possibilité de définir une durée de 30 jours maximum pour qu’une conversion soit comptabilisée si l’utilisateur effectue l’action spécifiée.

Les événements de conversion vous aident à évaluer le succès de votre campagne. Par exemple :

- Si vous utilisez un géociblage pour déclencher un message SMS dont l’objectif final est un achat de la part de l’utilisateur, configurez l’événement de conversion sur `Purchase`.
- Si vous essayez de diriger l’utilisateur vers votre application, configurez l’événement de conversion sur `Starts Session`.

Vous pouvez également définir des événements de conversion personnalisés propre à votre cas d’utilisation spécifique. Soyez créatif et réfléchissez à la façon dont vous voulez vraiment évaluer la réussite de cette campagne.

{% endtab %}

{% tab Canvas %}

Si vous ne l’avez pas déjà fait, complétez les sections restantes de votre composant de Canvas. Pour plus d’informations sur la mise en place du reste de votre Canvas, la mise en œuvre d’un test multivarié et d’une sélection intelligente, etc. consultez la section [Construire votre Canvas Step]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation Canvas.

{% endtab %}
{% endtabs %}

## Étape 5 : Examiner et déployer

Après avoir terminé votre campagne ou votre Canvas, consultez-en les détails, faites un test et procédez à son envoi.

Ensuite, consultez [Rapports SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/) pour découvrir comment accéder aux résultats de vos campagnes par SMS.
