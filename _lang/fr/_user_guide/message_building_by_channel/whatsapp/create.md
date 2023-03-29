---
nav_title: Créer un message WhatsApp
article_title: Créer un message WhatsApp
page_order: 4
description: "Cet article de référence couvre les étapes de génération et de création d’un message WhatsApp."
page_type: reference
tool:
  - Campagnes
channel:
  - WhatsApp
hidden: true
---

# Créer un message WhatsApp

> Les campagnes WhatsApp sont idéales pour atteindre directement vos clients et échanger avec eux par programmation. Vous pouvez utiliser Liquid et d’autres contenus dynamiques pour non seulement proposer une expérience originale à vos utilisateurs, mais aussi générer un environnement qui favorise et optimise une expérience utilisateur discrète avec votre marque. 

{% alert important %}
La prise en charge du canal WhatsApp est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Conditions préalables

Pour créer un message WhatsApp et tirer parti du canal WhatsApp, vous devez d’abord lire la [présentation]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/) WhatsApp et effectuer les actions suivantes :
  - Acceptez les politiques, les limites et les règles relatives au contenu
  - Paramétrez votre connexion WhatsApp
  - Construisez vos modèles initiaux dans Meta pour utiliser vos messages

## Étape 1 : Choisissez où créer votre message

Vous ne savez pas si votre message doit être envoyé via une campagne ou un Canvas ? Les campagnes sont mieux adaptées aux campagnes de communication simples et uniques, tandis que les Canvas sont mieux adaptés aux parcours client en plusieurs étapes.

{% tabs %}
{% tab Campaign %}

**Étapes :**

1. Sur la page **Campaign (Campagne)**, cliquez sur <i class="fas fa-plus"></i>**Create Campaign (Créer une campagne)**.
2. Sélectionnez **WhatsApp**, ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Campagne multicanale**.
3. Donnez un nom clair et significatif à votre campagne.
4. Si nécessaire, ajoutez des [Équipes]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/) et des [Tags.]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)
   * Les tags facilitent la recherche et l’identification des campagnes, et la création de rapports. Par exemple, lorsque vous utilisez le [Créateur de rapports]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/), vous pouvez filtrer les éléments en fonction de tags spécifiques.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez choisir différentes plates-formes, types de messages et mises en page pour chacune de vos variantes ajoutées. Pour plus d’informations sur ce sujet, consultez les [Tests multivariés et A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
6. Sélectionnez un [groupe d’abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription) pour vous assurer d’envoyer votre message aux utilisateurs appropriés. Lors de la sélection d’un groupe d’abonnement, Braze ajoute automatiquement un filtre de segmentation, garantissant que seuls les utilisateurs abonnés recevront la campagne.

{% alert tip %}
Si tous les messages de votre campagne sont similaires ou ont le même contenu, composez votre message avant d’ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copy from Variant (Copier à partir de la variante)** dans le menu déroulant **Add Variant (Ajouter une variante)**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Étapes :**

1. [Créez votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l’aide de l’Assistant Canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape dans le Créateur de Canvas. Donnez un nom clair et significatif à votre étape.
3. Choisissez un [calendrier des étapes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) et spécifiez un délai si nécessaire.
4. Filtrez votre audience pour cette étape si nécessaire. Vous pouvez affiner davantage les destinataires de cette étape en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d’audience seront vérifiées après le délai au moment de l’envoi des messages.
5. Choisissez votre [comportement d’avancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choisissez les autres canaux de communication que vous souhaitez associer à votre message.

{% endtab %}
{% endtabs %}

## Étape 2 : Composer votre message WhatsApp

Pour composer votre message, sélectionnez un [modèle WhatsApp approuvé]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-3-create-whatsapp-templates). 

![][1]

Si vous avez ajouté des variables en créant votre modèle WhatsApp dans le gestionnaire Meta Business, ces variables s’afficheront comme des espaces blancs dans le composeur de message. Remplacez ces espaces blancs avec du Liquid. Si vous avez choisi d’intégrer des images lors de la création de votre modèle, chargez ou ajoutez des images depuis la bibliothèque média. 

![][2]

Prenez en compte le fait que les champs texte désactivés (surlignés en gris) ne peuvent pas être édités étant donné qu’ils font partie du modèle WhatsApp approuvé. Si vous désirez effectuer des mises à jour sur le texte désactivé, vous devez éditer votre modèle et le faire approuver à nouveau. 

{% alert tip %}
{% raw %}
Si vous prévoyez d’utiliser Liquid, assurez-vous d’inclure une valeur par défaut pour la personnalisation choisie. De cette façon, si le profil utilisateur de votre destinataire est incomplet, il ne recevra pas de message. Tout message comportant des variables Liquid manquantes ne sera pas envoyé via WhatsApp.
{% endraw %}
{% endalert %}

## Étape 3 : Prévisualiser et tester votre message

Braze recommande toujours de prévisualiser et de tester votre message avant de l’envoyer. Allez dans l’onglet **Test** pour envoyer un message WhatsApp test à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou des utilisateurs uniques, ou prévisualisez le message en tant qu’utilisateur directement dans Braze.

![][3]

## Étape 4 : Créez le reste de votre campagne ou de votre Canvas.

{% tabs %}
{% tab Campaign %}

Concevez ensuite le reste de votre campagne. Consultez les sections suivantes pour plus de détails sur la façon de mieux utiliser nos outils pour créer des messages WhatsApp.

#### Choisir une planification ou un déclencheur pour la livraison

Les messages WhatsApp peuvent être livrés sur la base d’une heure planifiée, d’une action ou d’un déclencheur API. Pour en savoir plus, consultez la section [Planifier votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Pour une livraison par événement, vous pouvez également définir la durée de la campagne et les [Heures calmes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

Cette étape permet également de spécifier les contrôles de livraison, comme permettre aux utilisateurs de devenir [rééligibles]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) pour recevoir la campagne ou activer les règles de [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Choisir les utilisateurs à cibler

Ensuite, vous devez [cibler des utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) en choisissant des segments ou des filtres pour limiter votre audience. Vous devez avoir déjà choisi le groupe d’abonnement, qui restreint les utilisateurs par niveau ou la catégorie de communication qu’ils souhaitent avoir avec vous. Au cours de cette étape, vous allez sélectionner une audience plus importante dans vos segments et allez restreindre davantage ce segment à l’aide de nos filtres. Vous recevez automatiquement un aperçu de ce à quoi ressemble la population approximative du segment à ce moment-là. Souvenez-vous que l’appartenance à un segment exact est toujours calculée juste avant l’envoi du message.

#### Sélectionner des événements de conversion

Braze vous permet de suivre à quelle fréquence les utilisateurs effectuent des actions spécifiques, des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), après avoir reçu une campagne. Vous pouvez autoriser une fenêtre de 30 jours maximum pendant laquelle une conversion sera comptabilisée si l’utilisateur effectue l’action spécifiée.

Vous pouvez également définir des événements de conversion personnalisés propre à votre cas d’utilisation spécifique. Soyez créatif et réfléchissez à la façon dont vous voulez vraiment évaluer la réussite de cette campagne.

{% endtab %}

{% tab Canvas %}

Si vous ne l’avez pas déjà fait, complétez les sections restantes de votre composant de Canvas. Pour plus d’informations sur la manière de mettre en place le reste de votre Canvas, d’implémenter un test multivarié et une sélection intelligente, référez-vous à l’étape [Construire votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation Canvas.

{% endtab %}
{% endtabs %}

## Étape 5 : Revue et déploiement

Quand vous avez fini de concevoir votre campagne ou votre Canvas, vérifiez ses détails, testez-le  et envoyez-le !

Ensuite, consultez [Rapports WhatsApp]() pour découvrir comment accéder aux résultats de vos campagnes WhatsApp.

[1]: {% image_buster /assets/img/whatsapp/whatsapp6.png %} 
[2]: {% image_buster /assets/img/whatsapp/whatsapp7.png %} 
[3]: {% image_buster /assets/img/whatsapp/whatsapp8.png %} 