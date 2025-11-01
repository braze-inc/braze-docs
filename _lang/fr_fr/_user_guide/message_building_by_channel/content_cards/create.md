---
nav_title: Créer une carte de contenu
article_title: "Création d'une carte de contenu"
page_order: 0
description: "Cet article de référence explique comment créer, composer, configurer et envoyer des cartes de contenu à l'aide de campagnes et de canevas Braze."
tool:
  - Canvas
  - Campaigns
channel:
  - content cards
search_rank: 3.9

---

# Création d'une carte de contenu

> Cet article explique comment créer une carte de contenu dans Braze lorsque vous créez des campagnes et des canevas. Nous allons vous aider à choisir un type de message, à composer votre carte et à planifier la réception/distribution de votre message.

## Étape 1 : Choisissez où créer votre message

Vous ne savez pas si votre message doit être envoyé par le biais d'une campagne ou d'un canvas ? Les campagnes conviennent mieux aux campagnes d'envoi de messages simples et uniques (par exemple, informer les utilisateurs d'un nouveau produit avec un seul message), tandis que les Canevas conviennent mieux aux parcours utilisateurs en plusieurs étapes (par exemple, envoyer des suggestions de produits sur mesure en fonction du comportement de l'utilisateur au fil du temps).

{% tabs %}
{% tab Campaign %}

1. Allez dans **Messagerie** > **Campagnes** et sélectionnez **Créer une campagne.**
2. Sélectionnez **Cartes de contenu** ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Multicanal**.
3. Donnez à votre campagne un nom clair et significatif.
4. Ajoutez des [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) et des [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) si nécessaire.
   * Les étiquettes facilitent la recherche de vos campagnes et permettent de créer des rapports. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), vous pouvez filtrer par les étiquettes pertinentes.
5. Ajoutez et nommez autant de variantes que vous le souhaitez pour votre campagne. Vous pouvez choisir des plateformes, des types de messages et des mises en page différents pour chacune de vos variantes ajoutées. Pour en savoir plus sur les variantes, reportez-vous au [test multivarié et au test A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si tous les messages de votre campagne seront similaires ou auront le même contenu, composez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite sélectionner **Copier de la variante** dans le menu déroulant **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Créez votre canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l'aide du compositeur de canvas.
2. Après avoir configuré votre canvas, ajoutez une étape du message dans le générateur de canvas. Donnez à votre démarche un nom clair et significatif.
3. Sélectionnez les **cartes de contenu** comme canal de communication.
4. Choisissez le moment où Braze calcule l'éligibilité de l'audience et la personnalisation de la carte de contenu. Cela peut se faire à l'entrée de l'étape ou à la première impression (recommandé). Les étapes contenant des cartes de contenu peuvent être planifiées ou basées sur des actions.
5. Choisissez de supprimer ou non les cartes de contenu lorsque les utilisateurs effectuent un achat ou un événement personnalisé.
6. Définissez une date d'expiration pour la carte de contenu (durée dans le flux). Cela peut se faire après un certain temps ou à un moment précis.
7. Filtrez votre audience, ou les destinataires, pour cette étape si nécessaire dans les **paramètres de réception/distribution**. Vous pouvez encore affiner votre audience en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d'audience seront vérifiées après le délai, au moment de l'envoi des messages.
8. Choisissez les autres canaux de communication que vous souhaitez associer à votre message.

{% endtab %}
{% endtabs %}

## Étape 2 : Spécifiez vos types de messages

Sélectionnez l'un des trois types de carte contenu essentiels : **Classique**, **Image légendée** et **Image seule**. 

Pour en savoir plus sur le comportement et l'aspect attendus de chaque type, reportez-vous à la section [Détails créatifs]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/) ou consultez les liens du tableau suivant. Ces types de cartes de contenu sont acceptés à la fois par les applications mobiles et les applications web.

| Type de message | Exemple | Description |
|---|---|---|
|[Classique]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#classic)| Une carte de contenu classique avec une petite icône et du texte pour encourager la réservation d'un cours d'entraînement.]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) |La carte classique présente une mise en page simple avec un titre en gras, le texte du message et une image facultative placée à gauche du titre et du texte. Il est préférable d'utiliser une image ou une icône carrée avec la carte classique. |
|[Image légendée]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#captioned-image)| Une carte de contenu légendée avec l'image d'une haltérophile et un texte encourageant à s'inscrire à un cours d'entraînement.]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | La carte de type image légendée met en valeur votre contenu avec un texte et une image qui attire l'attention. |
|[Image seulement]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#banner)| \![Une carte de contenu avec uniquement du texte.]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | La carte d'images seulement attire l'attention grâce à l'espace réservé aux images, aux GIF et à d'autres contenus créatifs non textuels. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Étape 3 : Composer une carte de contenu

Vous pouvez modifier tous les aspects du contenu et du comportement de votre message dans l'onglet **Composer de** l'éditeur de message.

!Détails de la carte de contenu dans l'onglet Composer de l'éditeur de message.]({% image_buster /assets/img/content_card_compose.png %})

Le contenu de cette section varie en fonction du **Content-Type** choisi à l'étape précédente, mais peut inclure l'une des options suivantes :

#### Langue

Sélectionnez **Ajouter des langues** pour ajouter les langues de votre choix dans la liste proposée. Cela permettra d'insérer [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) dans votre message. Nous vous recommandons de sélectionner vos langues avant de rédiger votre contenu afin de pouvoir remplir votre texte à l'endroit voulu dans le Liquid. Pour obtenir la liste complète des langues que vous pouvez utiliser, reportez-vous à la section [Langues prises en charge.]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported)

Une fenêtre avec l'anglais, l'espagnol et le français sélectionnés pour les langues, et le titre, la description et le texte du lien sélectionnés pour les champs à internationaliser.]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

##### Création d'envois de droite à gauche

L'aspect final des messages de droite à gauche dépend largement de la manière dont les fournisseurs de services les restituent. Pour connaître les meilleures pratiques en matière d'élaboration de messages de droite à gauche qui s'affichent le plus précisément possible, reportez-vous à la section [Création de messages de droite à gauche.]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/)

#### Titre et message

Écrivez ce que vous voulez. Il n'y a pas de limites, mais plus vite vous pouvez faire passer votre message et faire cliquer votre client, mieux c'est ! Nous recommandons des titres et des messages clairs et concis. Notez que ces champs ne sont pas fournis pour les cartes à image seule.

#### Image

Ajoutez une image à votre carte de contenu en sélectionnant **Ajouter une image** ou en fournissant l'URL de l'image. En sélectionnant **Ajouter une image**, vous ouvrez la **bibliothèque multimédia**, où vous pouvez sélectionner une image déjà téléchargée ou en ajouter une nouvelle. Chaque type de message et chaque plateforme peuvent avoir leurs propres proportions et exigences. Vérifiez-les avant de commander ou de créer une image à partir de zéro ! N'oubliez pas que la taille totale des champs des messages de la carte de contenu est limitée à 2 Ko.

#### Épingler en haut de page

Une carte épinglée s'affiche en haut du fil d'actualité de l'utilisateur et ne peut pas être fermée par ce dernier. Si plusieurs cartes sont épinglées dans le flux d'un utilisateur, les cartes épinglées s'affichent dans l'ordre chronologique. Une fois qu'une carte a été envoyée, vous ne pouvez pas mettre à jour rétroactivement son option épinglée. La modification de cette option après l'envoi d'une campagne n'affectera que les envois futurs.

L'aperçu de la carte de contenu est présenté côte à côte dans Braze pour mobile et Web avec l'option "Épingler cette carte en haut du flux" sélectionnée.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### Comportement au clic

Lorsque votre client clique sur un lien présenté dans la carte, votre lien peut soit le conduire plus profondément dans votre appli, soit vers un autre site. Si vous choisissez un comportement "on-click" pour votre carte de contenu, n'oubliez pas de mettre à jour votre **texte de lien** en conséquence.

Les actions suivantes sont disponibles pour les liens de la carte de contenu :

| Action | Description |
|---|---|
| Redirection vers l'URL | Ouvrez une page web non native. |
| [Lien profond dans l'application]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | Lien profond vers un écran existant dans votre application. |
| Enregistrer un événement personnalisé | Choisissez un [événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) à déclencher. Peut être utilisé pour afficher une autre carte de contenu ou déclencher des messages supplémentaires. |
| Attribut personnalisé du journal | Choisissez un [attribut personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) à définir pour l'utilisateur actuel. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Les options **Log Custom Event** et **Log Custom Attribute** nécessitent la compatibilité avec la version suivante du SDK :

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## Étape 4 : Configurer des paramètres supplémentaires (en option)

Vous pouvez utiliser des [paires clé-valeur]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) pour créer des catégories pour vos cartes, créer [plusieurs flux de cartes de contenu]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds) et personnaliser la façon dont les cartes sont triées.

Pour ajouter des paires clé-valeur à votre message, accédez à l'onglet **Paramètres** et sélectionnez **Ajouter une nouvelle paire.**

## Étape 5 : Créez le reste de votre campagne ou Canvas

{% tabs %}
{% tab Campaign %}

Créez le reste de votre campagne. Vous trouverez dans les sections suivantes des informations complémentaires sur la manière d'utiliser au mieux nos outils pour créer des cartes de contenu.

#### Choisissez une planification ou un déclencheur de réception/distribution

Les cartes de contenu peuvent être diffusées en fonction d'une heure planifiée, d'une action ou d'un déclencheur API. Pour en savoir plus, reportez-vous à la section [Planification de votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Vous pouvez également définir la durée de la campagne et les [heures calmes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) et déterminer l'expiration de la carte de contenu. Définissez une date d'expiration spécifique ou le nombre de jours avant l'expiration d'une carte, jusqu'à 30 jours. Toutes les variantes ont des dates de péremption identiques.

{% alert note %}
La limite de fréquence ne s'applique pas aux cartes de contenu.
{% endalert %}

##### Réception/distribution planifiée

Pour les campagnes de cartes de contenu avec réception/distribution planifiée, vous pouvez choisir le moment où Braze évalue l'éligibilité de l'audience et la personnalisation pour les nouvelles campagnes de cartes de contenu en spécifiant le moment où la carte est créée. Pour en savoir plus, reportez-vous à la rubrique [Création de cartes]({{site.baseurl}}/card_creation).

#### Choisissez les utilisateurs à cibler

Ensuite, [ciblez les utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) en choisissant des segments ou des filtres pour réduire votre audience. Vous obtiendrez automatiquement un aperçu de ce à quoi ressemble actuellement cette segmentation approximative de la population. N'oubliez pas que l'appartenance exacte à un segment est toujours calculée juste avant l'envoi du message.

{% multi_lang_include target_audiences.md %}

#### Choisissez des événements de conversion

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), après avoir reçu une campagne. Vous avez la possibilité d'autoriser une fenêtre de 30 jours maximum pendant laquelle une conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée.

{% endtab %}

{% tab Canvas %}

Si vous ne l'avez pas encore fait, complétez les sections restantes de votre composante Canvas. Pour plus de détails sur la manière de créer le reste de votre Canvas, de mettre en œuvre les [tests multivariés]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) et la [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/), et plus encore, reportez-vous à l'étape [Créer votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation sur le Canvas.

{% endtab %}
{% endtabs %}

## Étape 6 : Examiner et déployer

Une fois que vous avez fini de créer la dernière partie de votre campagne ou de votre Canvas, passez en revue ses détails, [testez-la]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/testing/), puis envoyez-la lorsque vous êtes prêt.

{% alert warning %}
Une fois qu'une carte de contenu est lancée, elle ne peut plus être modifiée. Il est seulement possible d'empêcher l'envoi de messages à de nouveaux utilisateurs et de les supprimer des fils d'actualité des utilisateurs. Reportez-vous à la section [Mise à jour des cartes d'envoi]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-launched-cards) pour comprendre comment vous pouvez aborder ce scénario.
{% endalert %}

Ensuite, consultez [les rapports sur les cartes de]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/) contenu pour savoir comment vous pouvez accéder aux résultats de vos campagnes de cartes de contenu.

## Ce qu'il faut savoir

### Limitation de la taille des cartes de contenu

La taille de la charge utile d'une carte de contenu peut atteindre 2 Ko après le rendu liquide. Il s'agit du **titre**, du **message**, de l'**URL de l'image**, du **texte du lien**, de l'**URL du ou des liens** et des **paires clé-valeur** (noms et valeurs). Toutefois, cette limite n'inclut pas la taille de l'image, mais seulement la longueur de l'URL de l'image.

{% alert important %}
Les messages de plus de 2 Ko ne seront pas envoyés. Lors des envois de test, les cartes de contenu qui dépassent 2 Ko peuvent encore être livrées et s'afficher correctement.
{% endalert %}

### Nombre de cartes dans le flux

Chaque utilisateur peut avoir jusqu'à 250 cartes de contenu non expirées dans son flux à un moment donné. Lorsque cette limite est dépassée, Braze cesse de renvoyer les cartes les plus anciennes, même si elles ne sont pas lues. Les cartes retirées sont également prises en compte dans cette limite, ce qui signifie qu'un nombre élevé de cartes retirées peut réduire l'espace disponible pour les nouvelles cartes.

### Comportement d'envoi

Une fois que les cartes de contenu ont été envoyées, elles attendent dans une "boîte de réception", prêtes à être remises à l'utilisateur (comme c'est le cas pour les e-mails). Une fois que le contenu a été introduit dans la carte de contenu (au moment de l'affichage), il ne peut plus être modifié pendant sa durée de vie. Cela s'applique même si vous appelez une API par l'intermédiaire du contenu connecté et que les données de l'endpoint changent. Ces données ne seront pas mises à jour. Il est seulement possible d'empêcher l'envoi de messages à de nouveaux utilisateurs et de les supprimer des fils d'actualité des utilisateurs. Si vous modifiez une campagne, seules les cartes envoyées ultérieurement seront mises à jour.

Si vous devez retirer d'anciennes cartes, vous devez d'abord arrêter la campagne. Pour arrêter une campagne, ouvrez votre campagne cartes de contenu et sélectionnez **Arrêter la campagne.** En arrêtant la campagne, vous devrez décider comment traiter les utilisateurs qui ont déjà reçu votre carte. 

Si vous souhaitez supprimer la carte de contenu des flux de vos utilisateurs, sélectionnez **Supprimer la carte du flux.** La carte sera ensuite masquée par le SDK lors de la prochaine synchronisation.

Dialogues de confirmation de la désactivation de la carte de contenu]({% image_buster /assets/img/cc_remove.png %}){: style="max-width:75%" }

{% alert tip %}
Vous souhaitez que votre contenu dure plus de 30 jours ? Essayez les [bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners).
{% endalert %}

### Evénements liés au retrait de la carte {#action-based-card-removal}

Certaines cartes de contenu ne sont pertinentes que jusqu'à ce que l'utilisateur effectue une action. Par exemple, une carte incitant les utilisateurs à activer leur compte ne doit pas être affichée une fois que l'utilisateur a terminé cette tâche d'onboarding.

Dans une campagne ou un message Canvas, vous pouvez éventuellement ajouter un **événement de retrait** pour spécifier les événements personnalisés ou les achats qui doivent entraîner le retrait des cartes précédemment envoyées du flux de cet utilisateur, déclenché par le SDK ou l'API REST.

Les cartes seront supprimées lors des actualisations suivantes, une fois que Braze aura traité l'événement spécifié.

{% alert tip %}
Vous pouvez spécifier plusieurs événements personnalisés et achats qui doivent supprimer une carte du flux d'un utilisateur. Lorsque l'utilisateur effectue l' **une de** ces actions, toutes les cartes existantes envoyées par les cartes de la campagne sont supprimées. Les cartes éligibles ultérieures continueront d'être envoyées conformément à la planification du message.
{% endalert %}

!Panneau Conditions de retrait de la carte de contenu avec l'option Événement de retrait de la carte de contenu.]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

### Mise à jour des cartes lancées

Les cartes de contenu ne peuvent pas être modifiées après leur envoi. Si vous constatez que vous devez apporter des modifications à des cartes déjà envoyées, envisagez de recourir à la [réadmissibilité de la campagne]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/), comme indiqué dans les options suivantes.

{% alert note %}
Lorsqu'une carte de contenu devient rééligible, elle peut être envoyée à nouveau lorsque la carte originale se trouve encore dans l'appli d'un utilisateur. Pour éviter les cartes en double dans l'application d'un utilisateur, vous pouvez désactiver la rééligibilité ou prolonger la fenêtre de rééligibilité de sorte que les utilisateurs ne reçoivent pas de nouvelle carte tant que la première n'a pas expiré.
{% endalert %}

Notez également que les cartes de contenu utilisant la [première impression]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression) utilisent le temps d'impression pour calculer la réadmissibilité. Toutefois, les cartes de contenu créées au moment du lancement de la campagne ou de l'étape du canvas utilisent l'heure d'envoi ou d'impression la plus tardive.

#### Option 1 : Duplication de la campagne

Une approche consiste à archiver la campagne et à retirer les cartes actives du flux. Vous pouvez ensuite dupliquer la campagne et la lancer avec des mises à jour afin que tous les utilisateurs éligibles reçoivent les cartes actualisées.

* Si les utilisateurs ne doivent jamais être rééligibles pour une carte de contenu, vous pouvez filtrer les utilisateurs qui n'ont pas reçu la version précédente de la carte de contenu en réglant le filtre `Received Message from Campaign` sur la condition `Has Not`.
* Si les utilisateurs qui ont reçu la carte précédente doivent être rééligibles dans X jours, vous pouvez définir le filtre pour `Last Received Message from specific campaign` à plus de X jours **OU** `Received Message from Campaign` avec la condition `Has Not`.

##### Cas d'utilisation

Supposons que vous ayez configuré une campagne pour qu'elle soit déclenchée par le début d'une session et que la rééligibilité soit fixée à 30 jours. Un utilisateur a reçu la campagne il y a deux jours et vous souhaitez modifier la copie. Tout d'abord, vous archivez la campagne et retirez les cartes du flux. Ensuite, vous reproduisez la campagne et la lancez à nouveau avec le nouveau texte. Si l'utilisateur a une autre session, il recevra immédiatement la nouvelle carte.

##### Impact

* **Rapport :** Chaque version de la carte ferait l'objet d'une analyse/analytique distincte.
* **Destinataires actuels :** Les nouveaux destinataires et les destinataires actuels verront la carte mise à jour lors de la prochaine actualisation du flux, s'ils sont éligibles.

{% alert tip %}
Nous recommandons cette option pour les messages dans lesquels vous affichez le contenu le plus récent de la carte (comme les bannières de la page d'accueil), lorsque les changements doivent être affichés immédiatement ou lorsque la rééligibilité est désactivée.
{% endalert %}

#### Option 2 : Arrêter et relancer

Si la rééligibilité d'une carte est activée, vous pouvez choisir de.. :

1. Arrêtez votre campagne.
2. Supprimez les cartes de contenu actives des fils d'actualité des utilisateurs.
3. Modifiez votre campagne si nécessaire.
4. Redémarrez votre campagne.

Selon cette approche, les utilisateurs nouvellement éligibles recevront la nouvelle carte, et les anciens destinataires recevront la nouvelle carte lorsqu'ils seront à nouveau éligibles.

##### Cas d'utilisation

Imaginons que vous ayez une campagne déclenchée par le démarrage d'une session et dont la rééligibilité est fixée à 30 jours. Un utilisateur a reçu la campagne il y a deux jours et vous souhaitez modifier la copie. Tout d'abord, arrêtez la campagne et retirez la carte du flux. Ensuite, republiez la campagne avec le nouveau texte. Si l'utilisateur a une autre session, il recevra la nouvelle carte dans 28 jours.

##### Impact

* **Rapport :** Une campagne contiendra toutes les analyses/analytiques des cartes lancées. Braze ne fera pas la différence entre les versions lancées.
* **Destinataires actuels :** Les utilisateurs qui ont déjà reçu la carte ne recevront pas les cartes mises à jour tant qu'ils ne seront pas rééligibles. Si la rééligibilité est désactivée, ils ne recevront jamais la nouvelle carte.

{% alert tip %}
Nous vous recommandons d'utiliser cette option pour les messages uniques dans un centre de notification ou une boîte de réception (comme les promotions), lorsqu'il est important que les analyses/analytiques soient unifiées, ou lorsque l'actualité du message n'est pas un problème (par exemple, les destinataires existants peuvent attendre la fenêtre d'éligibilité avant de voir les cartes mises à jour).
{% endalert %}

#### Garder les cartes dans les fils d'actualité des utilisateurs

Si vous le souhaitez, vous pouvez conserver une campagne cartes de contenu active dans le flux des utilisateurs et ne pas la supprimer. Lorsque la campagne en ligne est modifiée, la version précédente non modifiée de la fiche de campagne reste en ligne, et seuls les utilisateurs qui répondent aux critères après les modifications verront la nouvelle version. Cependant, les utilisateurs déjà exposés à la campagne peuvent voir deux versions de la carte.

