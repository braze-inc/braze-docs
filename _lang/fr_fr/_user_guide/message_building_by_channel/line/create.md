---
nav_title: Créer un message LINE
article_title: Créer un message LINE
page_order: 1
description: "Cet article explique comment créer une campagne de messages LINE ou un Canvas."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/
---

# Créer un message LINE

> Les campagnes LINE peuvent atteindre directement et discuter de manière programmatique avec vos clients. Vous pouvez utiliser Liquid et d’autres contenus dynamiques pour non seulement proposer une expérience originale à vos utilisateurs, mais aussi générer un environnement qui favorise et optimise une expérience utilisateur discrète avec votre marque.

## Conditions préalables

Avant de créer un message LINE, faites ce qui suit :

1. Lisez l'aperçu de LINE.
2. Reconnaître les politiques, les limites et les règles de contenu.
3. [Configurez votre connexion LINE]({{site.basesurl}}/user_guide/message_building_by_channel/line/line_setup/).

L'envoi de messages LINE à partir de Braze est prélevé sur les crédits de messages de votre compte.

## Étape 1 : Choisissez où créer votre message

Vous ne savez pas si votre message doit être envoyé via une campagne ou un Canvas ? Les campagnes sont mieux adaptées aux campagnes de communication simples et uniques, tandis que les Canvas sont mieux adaptés aux parcours client en plusieurs étapes.

{% tabs %}
{% tab Campagne %}

**Étapes :**

1. Allez dans **Messagerie** > **Campagnes** et sélectionnez **Créer une campagne**.
2. Sélectionnez **LINE** ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Campagne multicanale**.
3. Donnez un nom clair et significatif à votre campagne.
4. Ajoutez [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) et [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) au besoin.
   * Les balises facilitent la recherche et l’identification des campagnes, et la création de rapports.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez choisir différentes plates-formes, types de messages et mises en page pour chacune de vos variantes ajoutées. Pour plus d'informations sur ce sujet, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

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

## Étape 2 : Rédigez votre message LINE

Rédigez votre message en utilisant la personnalisation (comme le contenu Liquid ou connecté) si nécessaire. LINE autorise jusqu'à cinq bulles de message dans chaque message, qui peuvent correspondre à l'une des mises en page de messages disponibles : texte, image, riche ou à base de cartes.

![Composez LINE avec un message affiché dans l'aperçu.]({% image_buster /assets/img/line/line_composer.png %})

### Conseils

#### Utilisation de Liquid

Si vous prévoyez d'utiliser Liquid, assurez-vous d'inclure une valeur par défaut pour votre personnalisation. Cela empêchera les destinataires ayant des profils utilisateur incomplets de recevoir un espace réservé vide. Par exemple, au lieu de recevoir le message « Salut ! », l’utilisateur pourrait recevoir le message « Salut, nouvel abonné ! ».

#### Création d'envois de messages de droite à gauche

L'aspect final des messages de droite à gauche dépend largement de la manière dont les fournisseurs de services les restituent. Pour connaître les meilleures pratiques en matière d'élaboration de messages de droite à gauche qui s'affichent le plus précisément possible, reportez-vous à la section [Création de messages de droite à gauche.]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/)

## Étape 3 : Prévisualiser et tester votre message

Passez à l'onglet **Test** pour envoyer un message LINE de test aux groupes de test de contenu ou aux utilisateurs individuels, ou prévisualisez le message en tant qu'utilisateur directement dans Braze.

![L'onglet "Tests" affiche un aperçu d'un message de test.]({% image_buster /assets/img/line/test_preview.png %})

## Étape 4 : Créer le reste de votre campagne ou de votre Canvas

{% tabs %}
{% tab Campagne %}

Construisez le reste de votre campagne. Voir les sections suivantes pour plus de détails sur la meilleure façon d'utiliser nos outils pour créer des messages LINE.

### Choisir un calendrier ou un déclencheur pour la livraison

Les messages LINE peuvent être livrés en fonction d'une heure programmée, d'une action ou d'un déclencheur d'API. Pour plus d'informations sur les options de planification et de déclencheurs, consultez [Planifier votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Vous pouvez spécifier des contrôles de livraison, tels que permettre aux utilisateurs de redevenir [éligibles]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) pour recevoir la campagne, ou activer les règles de [limitation de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping). Pour une livraison basée sur l'action, vous pouvez également définir la durée de la campagne et les [Heures de silence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

### Choisir les utilisateurs à cibler

[Utilisez des segments ou des filtres pour cibler vos utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/). Vous devriez déjà avoir choisi le groupe d'abonnement, ce qui restreint les utilisateurs par le niveau ou la catégorie de communication qu'ils souhaitent avoir avec vous. 

Sélectionnez le plus grand public parmi vos segments, et réduisez éventuellement ce segment davantage avec nos [filtres]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/). Vous recevez automatiquement un aperçu de ce à quoi ressemble la population approximative du segment à ce moment-là. Gardez à l’esprit que l’appartenance à un segment exact est toujours calculée juste avant l’envoi du message.

### Sélectionner des événements de conversion

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), après avoir reçu une campagne. Vous avez la possibilité d’autoriser une fenêtre allant jusqu’à 30 jours pendant laquelle une conversion sera comptée si l’utilisateur entreprend l’action spécifiée.

Les événements de conversion vous aident à évaluer le succès de votre campagne. Par exemple :

- Si vous utilisez le géociblage pour déclencher un message LINE dont l'objectif final est que l'utilisateur effectue un achat, définissez l'événement de conversion sur un `Purchase`.
- Si vous essayez de diriger l'utilisateur vers votre application, configurez l'événement de conversion sur `Starts Session`.

Vous pouvez également définir des événements de conversion personnalisés propre à votre cas d’utilisation spécifique. Soyez créatif et réfléchissez à la manière dont vous souhaitez mesurer le succès de cette campagne.

{% endtab %}
{% tab Canvas %}

Si vous ne l'avez pas encore fait, complétez les sections restantes de votre canvas. Pour plus de détails sur la façon de construire le reste de votre Canvas, utilisez les tests multivariés et la Sélection Intelligente, et plus encore, consultez [Créer un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).

{% endtab %}
{% endtabs %}

## Étape 5 : Revue et déploiement

Lorsque vous avez terminé de concevoir votre campagne ou votre canvas, vérifiez-en les détails, testez et envoyez !

Ensuite, consultez [le reporting LINE]({{site.baseurl}}/line/reporting/) pour savoir comment vous pouvez accéder aux résultats de vos campagnes LINE.


