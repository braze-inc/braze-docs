---
nav_title: Création d’une carte de contenu
article_title: Création d’une carte de contenu
page_order: 0
description: "Le présent article de référence explique comment créer, composer, configurer et envoyer des cartes de contenu via des campagnes Braze et des Canvas."
tool:
  - Canvas
  - Campagnes
channel:
  - cartes de contenu

---

# Création d’une carte de contenu

> Le présent article explique comment créer une carte de contenu dans Braze. Nous allons voir ici comment choisir un type de message, composer votre carte et planifier l’envoi de votre message.

Vous pouvez créer une carte de contenu avec la plateforme Braze en utilisant des campagnes et des Canvas.

## Étape 1 : Choisissez où créer votre message

Vous ne savez pas si votre message doit être envoyé à l’aide d’une campagne ou d’un Canvas ? Les campagnes sont mieux adaptées aux campagnes de communication simples et uniques, tandis que les Canvas sont mieux adaptés aux parcours client en plusieurs étapes.

{% tabs %}
{% tab Campaign %}

**Étapes :**

1. Sur la page **Campaign (Campagne)**, cliquez sur <i class="fas fa-plus"></i>**Create Campaign (Créer une campagne)**.
2. Sélectionnez **Content Cards (Cartes de contenu)**, ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Multichannel Campaign (Campagne multicanale)**.
3. Donnez un nom clair et significatif à votre campagne.
4. Si nécessaire, ajoutez des [Équipes]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/) et des [Tags.]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)
   * Les tags facilitent la recherche et l’identification des campagnes, et la création de rapports. Par exemple, lorsque vous utilisez le [Créateur de rapports]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/report_builder/), vous pouvez filtrer les éléments en fonction de tags spécifiques.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez sélectionner différentes plateformes, types de messages et mises en page pour chacune des variantes que vous ajoutez. Pour plus d’informations sur ce sujet, consultez [Tests A/B et Tests Multivariés.]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si tous les messages de votre campagne vont être similaires ou avoir le même contenu, composez votre message avant d’ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copy from Variant (Copier à partir de la variante)** dans le menu déroulant **Add Variant (Ajouter une variante)**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Étapes :**

1. [Créez votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l’aide de l’Assistant Canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape dans le Créateur de Canvas. Donnez un nom clair et significatif à votre étape.
3. Choisissez un [calendrier des étapes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) et spécifiez un délai si nécessaire. Les étapes contenant des cartes de contenu peuvent être programmées ou basées sur des actions.
4. Filtrez votre public pour cette étape, si nécessaire. Vous pouvez affiner davantage les destinataires de cette étape en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options de public seront vérifiées après le délai, au moment de l’envoi des messages.
5. Choisissez votre [comportement d’avancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/). Vous pouvez utiliser soit l’option **Advance when Message Sent (Progresser lorsque le message est envoyé)**, pour faire progresser vos utilisateurs vers les étapes suivantes lorsque la carte de contenu est envoyée, soit l’option **Immediately Advance Audience (Progresser immédiatement),** qui fait progresser les utilisateurs lorsque la carte de contenu est envoyée, ou si la carte de contenu est abandonnée pour quelque raison que ce soit.
6. Choisissez les autres canaux de messagerie que vous souhaitez associer à votre message.

{% endtab %}
{% endtabs %}

## Étape 2 : Spécifiez vos types de messages

Ensuite, sélectionnez un **Type de carte**. Braze propose trois types de carte de contenu prêts à l’emploi : Classique, Image avec légende et Bannière.

Pour en savoir plus sur le comportement attendu et l’apparence de chacun de ces types de messages, consultez [Détails créatifs]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/) ou consultez les liens du tableau suivant. Ces types de carte de contenu sont acceptés par les applications mobiles et les applications Web.

| Type de message | Exemple | Description |
|---|---|---|
|[Classique]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#classic)| ![Classic Content Card]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) |La carte classique a une mise en forme simple avec un titre gras, un texte de message et une image optionnelle située à gauche du titre et du texte. Il vaut mieux utiliser une image carrée ou une icône avec la Classic Card. |
|[Image avec légende]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#captioned-image)| ![Captioned Content Card]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | La carte Image avec légende vous permet de présenter votre contenu avec une image et un texte qui attirent l’attention. |
|[Bannière]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#banner)| ![Content Card bannière]{% image_buster/assets/img_archive/cc_steppington_banner.png %}) | La Carte Bannière vous permet d’être créatif et de retenir l’attention grâce aux images, aux GIFs et autres contenus non textuels. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Étape 3 : Composer une carte de contenu

Vous pouvez modifier tous les aspects du contenu et du comportement de votre message sur l'onglet Compose** (Composer)** de l’éditeur de messages.

![Exemple de détails de carte de contenu sur l’onglet Compose (Composer) de l’éditeur de messages][24]

Ici, le contenu varie en fonction du **Type de carte** choisi à l’étape précédente, mais peut inclure l’une des options suivantes :

#### Langue

Cliquez sur **Add Languages (Ajouter des langues)** et sélectionnez les langues souhaitées dans la liste affichée. Cela insérera [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) dans votre message. Nous vous recommandons de sélectionner vos langues avant d’écrire votre contenu pour pouvoir mettre votre texte au bon endroit dans le Liquid. Voir notre [liste complète des langues disponibles][18].

#### Titre et message

Écrivez ce que vous voulez. Il n’y a pas de limites, mais plus vite vous pouvez faire passer votre message et réussir à faire cliquer le client et mieux c’est ! Nous recommandons d’utiliser du contenu et des titres clairs et concis dans vos messages. Ces champs ne sont pas fournis pour les cartes de bannière.

#### Image

Pour ajouter une image à votre carte de contenu, cliquez sur **Add Image (Ajouter une Image)** ou entrez l’URL d’une image. Cliquer sur **Add Image (Ajouter une Image)** ouvre la **Médiathèque**, où vous pouvez sélectionner une image précédemment téléchargée ou en ajouter une nouvelle. Chaque type de message et plateforme peut avoir ses propres proportions suggérées et ses conditions, donc vérifiez-les avant de les mettre en œuvre ou de créer une image à partir de zéro ! La taille totale des champs de message de carte de contenu est limitée à 2 Ko

#### Épingler en haut

Une carte épinglée s’affiche en haut d’un flux d’un utilisateur et ne peut pas être rejetée par l’utilisateur. Si plus d’une carte est épinglée dans le flux d’un utilisateur, les cartes épinglées sont affichées dans l’ordre chronologique. Une fois qu’une carte a été envoyée, vous ne pouvez pas modifier rétroactivement l’option Épinglée. Modifier cette option après l’envoi d’une campagne n’affectera que les futurs envois.

#### Comportement on-click

Lorsque votre client clique sur un lien présenté dans la carte, votre lien peut les amener plus en profondeur dans votre application, ou vers un autre site. Si vous choisissez un comportement on-click pour votre carte de contenu, n’oubliez pas de mettre à jour votre **Texte de lien** en conséquence !

Les actions suivantes sont disponibles pour les liens de carte de contenu :

| Action | Description |
|---|---|
| Redirection vers URL Web | Ouverture d’un une page Web non native. |
| [Lien profond dans l’application]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | Lien profond vers un écran existant de votre appli. |
| Enregistrer un événement personnalisé | Choisissez un [événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) à déclencher. Peut être utilisé pour afficher une autre carte de contenu ou déclencher des messages supplémentaires. |
| Enregistrer un attribut personnalisé | Choisissez un [attribut personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) à définir pour l’utilisateur actuel. |
{: .reset-td-br-1 .reset-td-br-2}

**Note**: Les options  __Enregistrer événement personnalisé__  et  __Enregistrer Attribut personnalisé__  sont disponibles si vous avez la version suivante du SDK  :

{% sdk_min_versions ios:5.1.0 android:21.0.0 web:4.0.3 %}

{% alert warning %}
Les champs de message de carte de contenu sont limités à 2 Ko en taille totale, calculés en additionnant la longueur en octets des champs suivants : Titre, Message, URL de l’image, Texte du lien, URL du lien et Paires clés/valeurs (noms + valeurs). Les messages qui dépassent cette taille ne seront pas envoyés. Notez que cela ne concerne pas la taille de l’image mais plutôt la longueur de l’URL de l’image.
{% endalert %}

{% alert note %}
Chaque utilisateur peut recevoir jusqu’à 100 cartes de contenu non-expirées et non-rejetées. Si l’utilisateur devient éligible pour plus de 100 cartes, Braze commence à supprimer les anciennes cartes de son flux, même si elles n'ont pas été lues.
{% endalert %}

## Étape 4 : Configurer des paramètres supplémentaires (facultatif)

Vous pouvez utiliser des [paires clé-valeur][19] pour créer des catégories pour vos cartes, créer plusieurs flux de carte de contenu ([Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/multiple_feeds/), [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/multiple_feeds/), [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds/)) et personnaliser la façon de trier les cartes.

Pour ajouter des paires clé-valeur à votre message, allez sur l’onglet **Paramètres** et cliquez sur **Add New Pair (Ajouter une nouvelle paire)**.

## Étape 5 : Créez le reste de votre campagne ou de votre Canvas.

{% tabs %}
{% tab Campaign %}

Créez le reste de votre campagne ; consultez les sections suivantes pour plus de détails sur la façon optimale d’utiliser nos outils pour créer des cartes de contenu.

#### Choisir un calendrier ou un déclencheur pour la livraison

Les cartes de contenu peuvent être livrées en fonction d’une heure planifiée, d’une action ou d’un déclencheur API. Pour en savoir plus, consultez la section [Planifier votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Vous pouvez également définir la durée de la campagne, des [Heures calmes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) et déterminer l’expiration de la carte de contenu. Définissez une date d’expiration spécifique ou le nombre de jours avant l’expiration de la carte (jusqu’à 30 jours). Toutes les variantes ont la même date d’expiration.

{% alert note %}
La Limite de Fréquence ne s’applique pas aux cartes de contenu.
{% endalert %}

#### Choisir les utilisateurs à cibler

Ensuite, vous devez [cibler vos utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) en choisissant des segments ou des filtres pour préciser votre public. Vous verrez automatiquement un aperçu de la population approximative de ce segment à ce moment-là. Gardez à l’esprit que l’appartenance précise à un segment est toujours calculée juste avant l’envoi du message.

#### Sélectionner des événements de conversion

Braze vous permet de suivre à quelle fréquence les utilisateurs effectuent des actions spécifiques ([événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/)) après avoir reçu une campagne. Vous avez la possibilité d’autoriser une fenêtre de 30 jours maximum pendant laquelle une conversion sera comptabilisée si l’utilisateur effectue l’action spécifiée.

{% endtab %}

{% tab Canvas %}

Si vous ne l’avez pas déjà fait, complétez les sections restantes de votre Canvas Step. Pour plus d’informations sur la façon de créer le reste de votre Canvas, de mettre en œuvre un test multivarié et une sélection intelligente, reportez-vous à la section [Construire votre Canvas Step]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation Canvas.

{% endtab %}
{% endtabs %}

## Étape 6 : Revue et déploiement

Quand vous avez fini de concevoir votre campagne ou votre Canvas, vérifiez ses détails, [testez-le ]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/testing/) et envoyez-le !

{% alert warning %}
Une fois qu’une carte de contenu est lancée, elle ne peut plus être modifiée. On peut seulement arrêter de l’envoyer à des nouveaux utilisateurs et la supprimer des flux des utilisateurs.
{% endalert %}

Ensuite, consultez la section [Rapports sur les cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/) pour voir comment accéder aux résultats de vos campagnes de carte de contenu.

## Choses à savoir

### Capacités non encore prises en charge

Les fonctionnalités suivantes ne sont pas encore prises en charge pour les cartes de contenu :

- Bons d’achat
- Limite de fréquence
- Réorganisation des cartes de contenu depuis l’interface utilisateur Braze
- Modifications post-lancement


### Comportement d’envoi

Comme les e-mails, une fois que les cartes de contenu ont été envoyées, elles attendent dans une « boîte de réception », prêtes à être livrées à l’utilisateur. Une fois que le contenu est extrait dans la carte de contenu (au moment de l’affichage), le contenu ne peut plus être modifié pendant toute sa durée de vie. Cela s’applique même si vous appelez une API via un Contenu connecté, et que les données de l’endpoint changent. Ces données ne seront pas mises à jour. On peut seulement arrêter de les envoyer à des nouveaux utilisateurs et les retirer des flux des utilisateurs. Si vous modifiez une campagne, seules les futures cartes envoyées auront la mise à jour.

Pour supprimer des anciennes cartes, vous devez arrêter la campagne. Pour arrêter une campagne, ouvrez votre campagne de carte de contenu et sélectionnez **Stop Campaign (Arrêter la campagne)**. Lors de l’arrêt de la campagne, vous serez invité(e) à décider comment gérer les utilisateurs qui ont déjà reçu votre carte. Si vous souhaitez supprimer la carte de contenu des flux de vos utilisateurs, sélectionnez **Remove card from feed (Retirer la carte du flux)**. La carte sera alors masquée par le SDK lors de la prochaine synchronisation.

![Boîte de dialogue pour confirmer la désactivation d’une carte de contenu][25]{: style="max-width:75%" }

### Événements de retrait de carte {#action-based-card-removal}

Certaines cartes de contenu sont pertinentes jusqu’à ce que l’utilisateur effectue une action. Par exemple, les cartes qui incitent les utilisateur à activer leur compte ne devraient plus apparaitre quand l’utilisateur achève la tâche d’onboarding.

Dans une campagne ou un message Canvas, vous pouvez éventuellement ajouter un **Événement de retrait** pour spécifier quels événements ou achats personnalisés entraineront la suppression des cartes précédemment envoyées dans le flux cet utilisateur ; déclenchés via le SDK ou l’API REST.

{% alert tip %}
Vous pouvez spécifier plusieurs événements personnalisés ou achats avant qu’une carte soit retirée du flux des utilisateurs. Dès que l’utilisateur effectue **une** de ces actions, toutes les cartes existantes envoyées dans le cadre de la campagne seront supprimées. Toutes les futures cartes éligibles continueront d’être envoyées conformément au calendrier du message.
{% endalert %}

![Panneau Conditions de retrait de carte de contenu avec option de retrait de carte de contenu]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

### Mise à jour des cartes envoyées

Si vous avez besoin d’apporter des modifications à des cartes qui ont déjà été envoyées :
1. Arrêtez votre campagne.
2. Supprimez les cartes de contenu actives des flux des utilisateurs.
3. Modifiez votre campagne si nécessaire.
4. Redémarrez votre campagne.

[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported
[19]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/
[24]: {% image_buster /assets/img/content_card_compose.png %}
[25]: {% image_buster /assets/img/cc_remove.png %}
