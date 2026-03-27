---
nav_title: Créer une carte de contenu
article_title: Créer une carte de contenu
page_order: 0
description: "Cet article de référence explique comment créer, composer, configurer et envoyer des cartes de contenu à l'aide de campagnes et de Canvas Braze."
tool:
  - Canvas
  - Campaigns
channel:
  - content cards
search_rank: 3.9

---

# Créer une carte de contenu

> Cet article explique comment créer une carte de contenu dans Braze lorsque vous créez des campagnes et des Canvas. Nous allons vous guider dans le choix d'un type de message, la composition de votre carte et la planification de la distribution de votre message.

## Étape 1 : Choisissez où créer votre message

Utilisez les campagnes pour des messages simples et uniques (par exemple, informer les utilisateurs d'un produit avec un seul message). Utilisez les Canvas pour des parcours utilisateur en plusieurs étapes (comme l'envoi de suggestions de produits personnalisées en fonction du comportement de l'utilisateur au fil du temps).

{% tabs %}
{% tab Campaign %}

1. Allez dans **Messagerie** > **Campagnes** et sélectionnez **Créer une campagne**.
2. Sélectionnez **Cartes de contenu** ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Multicanal**.
3. Donnez un nom clair et significatif à votre campagne.
4. Ajoutez des [équipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) et des [étiquettes]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) si nécessaire.
   * Les étiquettes facilitent la recherche de vos campagnes et la création de rapports. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), vous pouvez filtrer par les étiquettes pertinentes.
5. Ajoutez et nommez autant de variantes que vous le souhaitez pour votre campagne. Vous pouvez choisir différentes plateformes, types de messages et dispositions pour chacune de vos variantes. Pour en savoir plus sur les variantes, consultez [Test multivarié et test A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si tous les messages de votre campagne sont similaires ou ont le même contenu, composez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite sélectionner **Copier de la variante** dans le menu déroulant **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Créez votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l'aide du compositeur de Canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape Message dans le générateur de Canvas. Donnez un nom clair et significatif à votre étape.
3. Sélectionnez **Cartes de contenu** comme canal de communication.
4. Choisissez le moment où Braze calcule l'éligibilité de l'audience et la personnalisation de la carte de contenu. Cela peut se faire à l'entrée de l'étape ou à la première impression (recommandé). Les étapes contenant des cartes de contenu peuvent être planifiées ou déclenchées par événement.
5. Choisissez si les cartes de contenu doivent être supprimées lorsque les utilisateurs effectuent un achat ou un événement personnalisé.
6. Définissez une date d'expiration pour la carte de contenu (durée dans le flux). Cela peut être après une certaine durée ou à un moment précis.
7. Filtrez votre audience, ou les destinataires, pour cette étape si nécessaire dans les **Paramètres de distribution**. Vous pouvez affiner davantage votre audience en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d'audience sont vérifiées après le délai, au moment de l'envoi des messages.
8. Choisissez les autres canaux de communication que vous souhaitez associer à votre message.

{% endtab %}
{% endtabs %}

## Étape 2 : Spécifiez vos types de messages

Sélectionnez l'un des trois types essentiels de cartes de contenu : **Classique**, **Image légendée** et **Image seule**. 

Pour en savoir plus sur le comportement et l'apparence attendus de chaque type, consultez la section [Détails créatifs]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/) ou les liens dans le tableau suivant. Ces types de cartes de contenu sont acceptés par les applications mobiles et les applications Web.

| Type de message | Exemple | Description |
|---|---|---|
|[Classique]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#classic)| ![Une carte de contenu classique avec une petite icône et un texte encourageant à réserver un cours de sport.]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) |La carte classique présente une mise en page simple avec un titre en gras, un texte de message et une image facultative placée à gauche du titre et du texte. Il est préférable d'utiliser une image carrée ou une icône avec la carte classique. |
|[Image légendée]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#captioned-image)| ![Une carte de contenu de type image légendée avec l'image d'un haltérophile et un texte encourageant à réserver un cours de sport.]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | La carte de type image légendée met en valeur votre contenu avec un texte et une image accrocheuse. |
|[Image seule]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#banner)| ![Une carte de contenu de type image seule avec du texte uniquement.]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | La carte image seule attire l'attention grâce à l'espace réservé aux images, GIF et autres contenus créatifs non textuels. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Étape 3 : Composer une carte de contenu

Vous pouvez modifier tous les aspects du contenu et du comportement de votre message dans l'onglet **Rédiger** de l'éditeur de message.

![Exemple de détails d'une carte de contenu dans l'onglet Rédiger de l'éditeur de message.]({% image_buster /assets/img/content_card_compose.png %})

Le contenu varie en fonction du **type de carte** choisi à l'étape précédente, mais peut inclure l'une des options suivantes :

#### Langue

Sélectionnez **Ajouter des langues** pour ajouter les langues souhaitées à partir de la liste proposée. Cela insère du [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) dans votre message. Nous vous recommandons de sélectionner vos langues avant de rédiger votre contenu afin de pouvoir remplir votre texte aux emplacements appropriés dans le Liquid. Pour consulter la liste complète des langues disponibles, reportez-vous à la section [Langues prises en charge]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

![Une fenêtre avec l'anglais, l'espagnol et le français sélectionnés pour les langues, et le titre, la description et le texte du lien sélectionnés pour les champs à internationaliser.]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

##### Création de messages de droite à gauche

L'apparence finale des messages de droite à gauche dépend largement de la manière dont les fournisseurs de services les restituent. Pour connaître les bonnes pratiques de création de messages de droite à gauche qui s'affichent le plus fidèlement possible, consultez la section [Création de messages de droite à gauche]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

#### Titre et message

Écrivez ce que vous voulez. Il n'y a pas de limites, mais plus vite vous faites passer votre message et incitez votre client à cliquer, mieux c'est ! Nous recommandons des titres et un contenu de message clairs et concis. Notez que ces champs ne sont pas disponibles pour les cartes de type image seule.

#### Image

Ajoutez une image à votre carte de contenu en sélectionnant **Ajouter une image** ou en fournissant une URL d'image. En sélectionnant **Ajouter une image**, vous ouvrez la **bibliothèque multimédia**, où vous pouvez sélectionner une image déjà téléchargée ou en ajouter une nouvelle. Chaque type de message et chaque plateforme peut avoir ses propres proportions et exigences suggérées. Vérifiez-les avant de commander ou de créer une image de zéro ! N'oubliez pas que la taille totale des champs de message d'une carte de contenu est limitée à 2 Ko.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Épingler en haut

Braze affiche une carte épinglée en haut du flux de l'utilisateur, et celui-ci ne peut pas la supprimer. Si le flux d'un utilisateur contient plusieurs cartes épinglées, Braze les classe par ordre chronologique. Une fois que vous avez envoyé une carte, vous ne pouvez pas modifier rétroactivement son option d'épinglage. La modification de cette option après l'envoi d'une campagne n'affecte que les envois futurs.

![Aperçu côte à côte de la carte de contenu dans Braze pour mobile et Web avec l'option « Épingler cette carte en haut du flux » sélectionnée.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### Comportement au clic

Lorsque votre client clique sur un lien présenté dans la carte, votre lien peut l'amener plus en profondeur dans votre application ou vers un autre site. Si vous choisissez un comportement au clic pour votre carte de contenu, n'oubliez pas de mettre à jour votre **texte de lien** en conséquence.

Les actions suivantes sont disponibles pour les liens des cartes de contenu :

| Action | Description |
|---|---|
| Rediriger vers une URL Web | Ouvrir une page Web non native. |
| [Lien profond dans l'application]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | Lien profond vers un écran existant de votre application. |
| Enregistrer un événement personnalisé | Choisissez un [événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) à déclencher. Peut être utilisé pour afficher une autre carte de contenu ou déclencher des messages supplémentaires. |
| Enregistrer un attribut personnalisé | Choisissez un [attribut personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) à définir pour l'utilisateur actuel. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Les options **Enregistrer un événement personnalisé** et **Enregistrer un attribut personnalisé** nécessitent la compatibilité avec les versions de SDK suivantes :

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## Étape 4 : Configurer des paramètres supplémentaires (facultatif)

Vous pouvez utiliser des [paires clé-valeur]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) pour créer des catégories pour vos cartes, créer [plusieurs flux de cartes de contenu]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds) et personnaliser le tri des cartes.

Pour ajouter des paires clé-valeur à votre message, accédez à l'onglet **Paramètres** et sélectionnez **Ajouter une nouvelle paire**.

## Étape 5 : Créer le reste de votre campagne ou Canvas

{% tabs %}
{% tab Campaign %}

Construisez le reste de votre campagne. Consultez les sections suivantes pour plus de détails sur la meilleure façon d'utiliser nos outils pour créer des cartes de contenu.

#### Choisir une planification ou un déclencheur de distribution

Les cartes de contenu peuvent être distribuées en fonction d'une heure planifiée, d'une action ou d'un déclencheur API. Pour en savoir plus, consultez [Planification de votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Vous pouvez également définir la durée de la campagne et les [heures calmes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours), et déterminer l'expiration de la carte de contenu. Définissez une date d'expiration spécifique ou le nombre de jours avant l'expiration de la carte, jusqu'à 30 jours. Toutes les variantes ont la même date d'expiration.

Si vous choisissez de faire expirer une carte après une durée définie (par exemple, après deux semaines), l'expiration est calculée à partir de la date d'envoi de la carte. Pour les campagnes planifiées, il s'agit de l'heure de lancement planifiée. Pour les campagnes par événement, il s'agit du moment où l'utilisateur effectue l'action déclencheuse. Par exemple, si une carte par événement est envoyée à 14 h aujourd'hui avec une expiration d'un jour, elle expire à 14 h le lendemain.

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

Pour la livraison par événement, un court délai est attendu avant l'apparition de la carte de contenu. Par exemple, lorsqu'une campagne est déclenchée au démarrage de la session, cet événement déclencheur doit d'abord être transmis aux serveurs de Braze. Ensuite, l'éligibilité de l'utilisateur à la campagne est enregistrée. Lorsque le SDK se synchronise, la carte est créée et renvoyée dans la même réponse de synchronisation. Si la synchronisation du SDK a eu lieu avant l'enregistrement de l'éligibilité de l'utilisateur, celui-ci ne reçoit pas la carte. Pour les utilisateurs en première session, ce délai est inévitable. Pour les utilisateurs existants nécessitant une disponibilité immédiate, envisagez plutôt la distribution planifiée.

##### Distribution planifiée

Pour les campagnes de cartes de contenu avec distribution planifiée, vous pouvez choisir quand Braze évalue l'éligibilité de l'audience et la personnalisation pour les nouvelles campagnes de cartes de contenu en spécifiant quand la carte est créée. Pour en savoir plus, consultez [Création de cartes]({{site.baseurl}}/card_creation).

#### Choisir les utilisateurs à cibler

Ensuite, [ciblez les utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) en sélectionnant des segments ou des filtres pour affiner votre audience. Vous recevez automatiquement un aperçu de la population approximative de ce segment. N'oubliez pas que l'appartenance exacte au segment est toujours calculée avant l'envoi du message.

{% multi_lang_include target_audiences.md %}

#### Sélectionner des événements de conversion

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, les [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), après avoir reçu une campagne. Vous avez la possibilité d'autoriser une fenêtre allant jusqu'à 30 jours pendant laquelle une conversion est comptabilisée si l'utilisateur effectue l'action spécifiée.

{% endtab %}

{% tab Canvas %}

Si vous ne l'avez pas encore fait, complétez les sections restantes de votre composant Canvas. Pour plus de détails sur la création du reste de votre Canvas, la mise en œuvre des [tests multivariés]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) et de la [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/), et plus encore, consultez l'étape [Créer votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation Canvas.

{% endtab %}
{% endtabs %}

## Étape 6 : Vérifier et déployer

Après avoir terminé la création de votre campagne ou Canvas, vérifiez ses détails, [testez-la]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/), puis envoyez-la quand vous êtes prêt.

{% alert warning %}
Une fois qu'une carte de contenu est lancée, elle ne peut plus être modifiée. On peut seulement arrêter de l'envoyer à de nouveaux utilisateurs et la retirer des flux des utilisateurs. Consultez la section [Mise à jour des cartes lancées]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-launched-cards) pour comprendre comment aborder ce scénario.
{% endalert %}

Ensuite, consultez la section [Rapports sur les cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/) pour découvrir comment accéder aux résultats de vos campagnes de cartes de contenu.

## Choses à savoir

### Limites de PAYLOAD et de flux

Pour garantir les performances, les cartes de contenu sont soumises à deux contraintes principales : une limite de taille de PAYLOAD pour chaque carte et un nombre maximal de cartes pouvant apparaître dans un flux.

#### Limites de taille des cartes de contenu

La PAYLOAD totale des données pour une seule carte de contenu ne peut pas dépasser 2 Ko **après** le rendu de toute personnalisation Liquid. Cela inclut :

* Titre
* Message
* URL de l'image (la longueur de la chaîne de caractères de l'URL elle-même, pas la taille du fichier image)
* Texte du lien
* URL de lien pour toutes les plateformes spécifiées (les URL distinctes pour iOS, Android et le Web comptent toutes dans le total)
* Paires clé-valeur (les noms des clés et leurs valeurs)

L'utilisation de Liquid pour extraire de longues chaînes de caractères (provenant par exemple d'attributs personnalisés) peut entraîner un dépassement de la limite.

Le compositeur de campagne affiche un avertissement si votre contenu statique dépasse la limite. (Nous ne prédisons pas la taille du contenu dynamique utilisant Liquid.) **Si la taille du message dépasse 2 Ko, l'envoi est interrompu.** Vous pouvez consulter ces interruptions dans le journal d'activité des messages avec la raison `Content card maximum size exceeded`.

{% alert important %}
Lors des envois de test, les cartes de contenu dépassant 2 Ko peuvent tout de même être livrées et affichées correctement.
{% endalert %}

Voici quelques bonnes pratiques pour gérer la taille de la PAYLOAD des cartes de contenu :

* Utilisez des raccourcisseurs d'URL pour les liens longs. Les URL, en particulier celles comportant de nombreux paramètres de suivi, peuvent poser des problèmes de limite de taille. L'utilisation d'un service de raccourcissement d'URL peut réduire considérablement le nombre de caractères et libérer de l'espace dans la PAYLOAD.
* Tronquez le contenu dynamique avec Liquid. Lors de la personnalisation de cartes avec du texte dynamique provenant d'attributs utilisateur ou d'appels API, la longueur du contenu peut être imprévisible. Utilisez de manière proactive des filtres Liquid comme `truncate` pour limiter la longueur de tout texte dynamique.
* Soyez efficace avec les URL multiplateformes. La limite de 2 Ko inclut les URL de toutes les plateformes que vous définissez. L'utilisation d'URL longues et uniques pour chaque plateforme peut multiplier la taille de la PAYLOAD. Dans la mesure du possible, utilisez un lien unique fonctionnant sur toutes les plateformes, ou recourez à des raccourcisseurs d'URL si nécessaire.
* Envisagez les bannières pour du contenu plus riche. Pour les cas d'utilisation nécessitant systématiquement de grandes quantités de contenu, les cartes de contenu ne sont peut-être pas le canal approprié. Les bannières ne sont pas soumises à la même limitation de PAYLOAD de 2 Ko et sont mieux adaptées à l'intégration de contenus plus riches directement dans l'expérience d'une application ou d'un site Web.

#### Nombre de cartes dans le flux

Chaque utilisateur peut avoir jusqu'à 250 cartes de contenu non expirées dans son flux à un moment donné. Lorsque cette limite est dépassée, Braze cesse de renvoyer les cartes les plus anciennes, même si elles n'ont pas été lues. Les cartes rejetées comptent également dans cette limite, ce qui signifie qu'un nombre élevé de cartes rejetées peut réduire l'espace disponible pour les cartes plus anciennes.

Pour éviter les problèmes liés à la limite de cartes, nous recommandons les bonnes pratiques suivantes :

- **Utilisez des dates d'expiration plus courtes :** Pour les campagnes sensibles au temps (comme les soldes du week-end), définissez une date d'expiration spécifique. Ainsi, les cartes sont automatiquement supprimées du flux et ne comptent plus dans la limite une fois qu'elles ne sont plus pertinentes.
- **Exploitez la suppression basée sur l'action :** Configurez des événements de suppression pour les cartes transactionnelles ou basées sur des objectifs. Par exemple, une carte invitant un utilisateur à compléter son profil devrait être supprimée dès qu'un événement `profile_completed` est enregistré.
- **Auditez les campagnes de longue durée :** Examinez les campagnes récurrentes ou en cours pour vous assurer qu'elles ne nuisent pas à l'expérience de vos utilisateurs en surchargeant le flux avec trop de cartes au fil du temps.

### Comprendre la rééligibilité pour les cartes de contenu

La rééligibilité détermine si et quand un utilisateur peut recevoir un message de la même campagne plus d'une fois. Pour les cartes de contenu, comprendre ce fonctionnement est essentiel pour gérer les campagnes récurrentes et garantir que les utilisateurs ne reçoivent pas de messages en double ou obsolètes.

{% alert tip %}
Vous souhaitez que votre contenu reste accessible au-delà de 30 jours ? Essayez les [bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners).
{% endalert %}

#### Comment la rééligibilité est-elle calculée ?

Si vous activez la rééligibilité, le compte à rebours permettant à un utilisateur de « réintégrer » une campagne commence après l'envoi du message. Le moment précis où ce compte à rebours démarre dépend des paramètres de création de votre carte :

* Les cartes de contenu utilisant [la première impression]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression) se basent sur le moment de l'impression pour calculer la rééligibilité.
* Les cartes de contenu créées au lancement de la campagne ou à l'entrée dans l'étape du canvas utilisent la date d'envoi ou le moment de l'impression, selon le plus récent.

#### L'expiration à 30 jours et la rééligibilité

Une source fréquente de confusion est l'interaction entre la rééligibilité de la campagne et l'expiration automatique de toutes les cartes de contenu après 30 jours.

Toutes les cartes de contenu sont automatiquement purgées des systèmes de Braze 30 jours après leur envoi ou leur suppression. Si vous avez une campagne récurrente de longue durée avec la rééligibilité **désactivée**, un utilisateur peut tout de même recevoir la même carte après 30 jours. Lorsque la carte d'origine est purgée, le système ne voit plus que cet utilisateur a reçu la campagne, ce qui le rend à nouveau éligible lors de sa prochaine session.

Pour que les utilisateurs ne reçoivent qu'une seule fois un message d'une campagne spécifique, ajoutez un filtre d'audience à votre campagne ou étape du canvas pour les utilisateurs qui n'ont pas reçu de message de cette campagne. Ce filtre est le moyen le plus fiable d'éviter les envois en double dans le cadre de campagnes de longue durée.

### Gestion des cartes de contenu en production

Une fois envoyées, les cartes de contenu attendent dans une « boîte de réception », prêtes à être remises à l'utilisateur (de manière similaire aux e-mails). Une fois que le contenu est intégré dans la carte de contenu (au moment de l'affichage), il ne peut plus être modifié pendant sa durée de vie. Cela s'applique même si vous appelez une API via du contenu connecté et que les données de l'endpoint changent. Ces données ne seront pas mises à jour. On peut seulement arrêter l'envoi à de nouveaux utilisateurs et retirer la carte des flux des utilisateurs. Si vous modifiez une campagne, seules les futures cartes envoyées intégreront la mise à jour.

#### Mise à jour des cartes lancées

Pour modifier une carte destinée à des utilisateurs qui l'ont déjà reçue, vous devez utiliser l'une des méthodes suivantes :

##### Option 1 : Dupliquer la campagne (recommandé pour les modifications immédiates)

{% alert tip %}
Nous recommandons cette option pour les messages où vous affichez le contenu le plus récent dans la carte, lorsque les modifications doivent être visibles immédiatement, ou lorsque la rééligibilité est désactivée.
{% endalert %}

La première approche consiste à archiver la campagne et à lancer une nouvelle campagne dupliquée :

1. Arrêtez la campagne d'origine et, lorsque vous y êtes invité, sélectionnez `Remove card after the next sync`.
2. Dupliquez la campagne, effectuez vos modifications et lancez la nouvelle version.

Lorsque vous dupliquez la campagne, vous devez définir l'audience de la nouvelle version. Utilisez les filtres de segmentation pour contrôler qui reçoit la carte mise à jour :
* Si les utilisateurs ne doivent jamais être rééligibles pour une carte de contenu, vous pouvez filtrer les utilisateurs qui n'ont pas reçu la version précédente de la carte de contenu en définissant le filtre `Received Message from Campaign` avec la condition `Has Not`.
* Si les utilisateurs ayant reçu la carte précédente doivent être rééligibles dans X jours, vous pouvez définir le filtre `Last Received Message from specific campaign` à plus de X jours **OU** `Received Message from Campaign` avec la condition `Has Not`.

###### Impact

* **Destinataires existants :** Les nouveaux destinataires et les destinataires existants verront la carte mise à jour lors de la prochaine actualisation du flux, s'ils sont éligibles.
* **Rapports :** Chaque version de la carte disposera d'analyses distinctes.

Supposons que vous ayez configuré une campagne déclenchée au démarrage de la session, avec une rééligibilité fixée à 30 jours. Un utilisateur a reçu la campagne il y a deux jours et vous souhaitez modifier le texte. Tout d'abord, archivez la campagne et retirez les cartes du flux. Ensuite, dupliquez la campagne et relancez-la avec le nouveau texte. Si l'utilisateur démarre une autre session, il recevra immédiatement la nouvelle carte.

##### Option 2 : Arrêter et relancer la même campagne

{% alert tip %}
Nous recommandons cette option pour les messages uniques dans un centre de notifications ou une boîte de réception (comme les promotions), lorsqu'il est important que les analyses soient unifiées, ou lorsque l'actualité du message n'est pas une préoccupation (par exemple, les destinataires existants peuvent attendre la fenêtre d'éligibilité avant de voir les cartes mises à jour).
{% endalert %}

Cette approche permet de regrouper toutes vos analyses dans une seule campagne. Les nouveaux utilisateurs éligibles recevront la nouvelle carte, mais la mise à jour sera retardée pour les destinataires existants jusqu'à ce qu'ils redeviennent éligibles :

1. Arrêtez votre campagne et, lorsque vous y êtes invité, sélectionnez **Supprimer la carte après la prochaine synchronisation**.
2. Modifiez votre campagne selon vos besoins.
3. Redémarrez votre campagne.

###### Impact

* **Destinataires existants :** Les utilisateurs ayant déjà reçu la carte ne recevront pas les cartes mises à jour tant qu'ils ne seront pas rééligibles. Si la rééligibilité est désactivée, ils ne recevront jamais la nouvelle carte.
* **Rapports :** Une seule campagne contient toutes les analyses de rapports pour les versions de cartes lancées. Braze ne différencie pas les versions lancées.

Supposons que vous ayez une campagne déclenchée au démarrage de la session avec une rééligibilité fixée à 30 jours. Un utilisateur a reçu la campagne il y a deux jours et vous souhaitez modifier le texte. Tout d'abord, arrêtez la campagne et supprimez la carte du flux. Ensuite, republiez la campagne avec le nouveau texte. Si l'utilisateur démarre une autre session, il recevra la nouvelle carte dans 28 jours.

#### Suppression et expiration des cartes

##### Suppression manuelle des cartes

Vous pouvez supprimer manuellement les cartes des flux de tous les utilisateurs à tout moment en arrêtant la campagne.

1. Ouvrez la campagne de cartes de contenu et sélectionnez Arrêter la campagne.
2. Lorsque vous y êtes invité, sélectionnez **Supprimer la carte après la prochaine synchronisation**. La carte sera supprimée lors de la prochaine actualisation du flux.

##### Suppression automatique des cartes {#action-based-card-removal}

Vous pouvez supprimer automatiquement une carte lorsqu'un utilisateur effectue une action spécifique, comme finaliser un achat ou activer une fonctionnalité.

Dans votre campagne ou étape du canvas, définissez un événement de suppression. Lorsqu'un utilisateur effectue cet événement, la carte est supprimée de son flux lors d'une actualisation ultérieure, après que Braze a traité l'événement.

{% alert note %}
Cette suppression n'est pas instantanée. Il y a un délai de traitement, et il peut falloir plusieurs minutes et plus d'une actualisation du flux avant que la carte ne disparaisse.
{% endalert %}

{% alert tip %}
Vous pouvez spécifier plusieurs événements personnalisés et achats qui doivent entraîner la suppression d'une carte du flux d'un utilisateur. Lorsque l'utilisateur effectue **l'une** de ces actions, toutes les cartes existantes envoyées par la campagne sont supprimées. Les futures cartes éligibles continueront d'être envoyées conformément à la planification du message.
{% endalert %}

![Panneau Conditions de suppression des cartes de contenu avec l'option Événement de suppression des cartes de contenu.]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

##### Expiration des cartes

Les cartes de contenu restent disponibles pendant 30 jours maximum à compter de leur envoi ; passé ce délai, Braze les supprime des flux des utilisateurs et les purge de ses systèmes.

#### Faire durer les cartes plus de 30 jours

{% alert tip %}
Pour les cas d'utilisation nécessitant que les messages persistent au-delà de la limite de 30 jours des cartes de contenu, envisagez d'utiliser les bannières. Les bannières sont conçues pour la persistance et n'ont pas de date d'expiration obligatoire, ce qui leur permet de rester visibles aussi longtemps que nécessaire.
{% endalert %}

Si vous souhaitez qu'une carte semble toujours disponible (c'est-à-dire qu'elle dure plus longtemps que le maximum de 30 jours), vous pouvez créer une campagne récurrente qui remplace efficacement la carte tous les 30 jours :

1. Fixez la durée de la carte de contenu à 30 jours.
2. Fixez la rééligibilité de la campagne à 30 jours.
3. Configurez la campagne pour qu'elle se déclenche au « démarrage de la session ».