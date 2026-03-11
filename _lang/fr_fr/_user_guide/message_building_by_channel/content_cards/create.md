---
nav_title: Créer une carte de contenu
article_title: Créer une carte de contenu
page_order: 0
description: "Cet article de référence explique comment créer, composer, configurer et envoyer des cartes de contenu à l'aide de campagnes et de canevas Braze."
tool:
  - Canvas
  - Campaigns
channel:
  - content cards
search_rank: 3.9

---

# Créer une carte de contenu

> Cet article explique comment créer une carte de contenu dans Braze lorsque vous créez des campagnes et des canevas. Nous allons vous aider à choisir un type de message, à composer votre carte et à planifier la réception/distribution de votre message.

## Étape 1 : Choisissez où créer votre message

Utilisez les campagnes de communication pour envoyer des messages simples et uniques (par exemple, informer les utilisateurs sur un produit à l'aide d'un seul message). Utilisez les canevas pour les parcours utilisateur en plusieurs étapes (tels que l'envoi de suggestions de produits personnalisées en fonction du comportement de l'utilisateur au fil du temps).

{% tabs %}
{% tab Campaign %}

1. Allez dans **Messagerie** > **Campagnes** et sélectionnez **Créer une campagne**.
2. Sélectionnez **Cartes de contenu** ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Multicanal**.
3. Donnez un nom clair et significatif à votre campagne.
4. Ajoutez des [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) et des [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) si nécessaire.
   * Les balises facilitent la recherche et l’identification des campagnes, et la création de rapports. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), vous pouvez filtrer par les étiquettes pertinentes.
5. Ajoutez et nommez autant de variantes que vous le souhaitez pour votre campagne. Vous pouvez choisir différentes plates-formes, types de messages et mises en page pour chacune de vos variantes ajoutées. Pour en savoir plus sur les variantes, reportez-vous au [test multivarié et au test A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si tous les messages de votre campagne vont être similaires ou avoir le même contenu, composez votre message avant d’ajouter des variantes supplémentaires. Vous pouvez ensuite sélectionner **Copier de la variante** dans le menu déroulant **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Créez votre canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l'aide du compositeur de canvas.
2. Après avoir configuré votre canvas, ajoutez une étape du message dans le générateur de canvas. Donnez un nom clair et significatif à votre étape.
3. Sélectionnez les **cartes de contenu** comme canal de communication.
4. Choisissez le moment où Braze calcule l'éligibilité de l'audience et la personnalisation de la carte de contenu. Ceci peut se faire à l'entrée de l'étape ou à la première impression (recommandé). Les étapes contenant des cartes de contenu peuvent être planifiées ou par événement.
5. Choisissez de supprimer ou non les cartes de contenu lorsque les utilisateurs effectuent un achat ou un événement personnalisé.
6. Définissez une date d'expiration pour la carte de contenu (durée dans le flux). Cela peut se faire après un certain temps ou à un moment précis.
7. Filtrez votre audience, ou les destinataires, pour cette étape si nécessaire dans les **paramètres de réception/distribution**. Vous pouvez encore affiner votre audience en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d’audience seront vérifiées après le délai, au moment de l’envoi des messages.
8. Choisissez les autres canaux de communication que vous souhaitez associer à votre message.

{% endtab %}
{% endtabs %}

## Étape 2 : Spécifiez vos types de messages

Sélectionnez l'un des trois types de carte contenu essentiels : **Classique**, **Image légendée** et **Image seule**. 

Pour en savoir plus sur le comportement et l'aspect attendus de chaque type, reportez-vous à la section [Détails créatifs]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/) ou consultez les liens du tableau suivant. Ces types de carte de contenu sont acceptés par les applications mobiles et les applications Web.

| Type de message | Exemple | Description |
|---|---|---|
|[Classique]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#classic)| ![Une carte de contenu classique avec une petite icône et un texte encourageant à réserver un cours de sport.]({% image_buster/assets/img_archive/cc_steppington_classic.png %}) |La carte classique présente une mise en page simple avec un titre en gras, un message et une image facultative placée à gauche du titre et du message. Il vaut mieux utiliser une image carrée ou une icône avec la Classic Card. |
|[Image avec légende]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#captioned-image)| ![Une carte de contenu de type image légendée avec l'image d'un haltérophile et un texte encourageant à réserver un cours de sport.]({% image_buster/assets/img_archive/cc_steppington_captioned.png %}) | La carte de type image légendée met en valeur votre contenu avec un texte et une image qui attire l'attention. |
|[Image uniquement]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#banner)| ![Carte de contenu contenant uniquement une image et du texte.]({% image_buster/assets/img_archive/cc_steppington_banner.png %}) | La carte d'images seulement attire l'attention grâce à l'espace réservé aux images, aux GIF et à d'autres contenus créatifs non textuels. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Étape 3 : Composer une carte de contenu

Vous pouvez modifier tous les aspects du contenu et du comportement de votre message dans l'onglet **Composer de** l'éditeur de message.

![Exemple de carte de contenu dans l'onglet Composer de l'éditeur de message.]({% image_buster /assets/img/content_card_compose.png %})

Le contenu de cette section varie en fonction du **Content-Type** choisi à l'étape précédente, mais peut inclure l'une des options suivantes :

#### Langue

Sélectionnez **Ajouter des langues** pour ajouter les langues de votre choix dans la liste proposée. Cela permettra d'insérer [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) dans votre message. Nous vous recommandons de sélectionner vos langues avant d’écrire votre contenu afin que vous puissiez remplir votre texte dans Liquid. Pour obtenir la liste complète des langues que vous pouvez utiliser, reportez-vous à la section [Langues prises en charge.]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported)

![Une fenêtre avec l'anglais, l'espagnol et le français sélectionnés pour les langues, et le titre, la description et le texte du lien sélectionnés pour les champs à internationaliser.]({% image_buster /assets/img/add_languages.png %}){: style="max-width:70%;"}

##### Création d'envois de messages de droite à gauche

L'aspect final des messages de droite à gauche dépend largement de la manière dont les fournisseurs de services les restituent. Pour connaître les meilleures pratiques en matière d'élaboration de messages de droite à gauche qui s'affichent le plus précisément possible, reportez-vous à la section [Création de messages de droite à gauche.]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/)

#### Titre et message

Écrivez ce que vous voulez. Il n'y a pas de limites, mais plus vite vous pouvez faire passer votre message et faire cliquer votre client, mieux c'est ! Nous recommandons d’utiliser du contenu et des titres clairs et concis dans vos messages. Notez que ces champs ne sont pas fournis pour les cartes à image seule.

#### Image

Ajoutez une image à votre carte de contenu en sélectionnant **Ajouter une image** ou en fournissant l'URL de l'image. En sélectionnant **Ajouter une image**, vous ouvrez la **bibliothèque multimédia**, où vous pouvez sélectionner une image déjà téléchargée ou en ajouter une nouvelle. Chaque type de message et de plateforme peut avoir ses propres proportions et exigences. Vérifiez-les avant de commander ou de créer une image à partir de zéro ! N'oubliez pas que la taille totale des champs des messages de la carte de contenu est limitée à 2 Ko.

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Épingler en haut

Braze affiche une carte épinglée en haut du fil d'actualité de l'utilisateur, et l'utilisateur ne peut pas la supprimer. Si le fil d'actualité d'un utilisateur contient plusieurs cartes épinglées, Braze les classe par ordre chronologique. Une fois que vous avez envoyé une carte, il n'est pas possible de modifier rétroactivement son option épinglée. La modification de cette option après l'envoi d'une campagne n'affecte que les envois futurs.

![Aperçu côte à côte de la carte de contenu dans Braze pour mobile et Web avec l’option « Épingler cette carte en haut du fil » sélectionnée.]({% image_buster /assets/img/cc_pin_to_top.png %}){:style="border:none"}

#### Comportement lors du clic

Lorsque votre client clique sur un lien présenté dans la carte, votre lien peut les amener plus en profondeur dans votre application, ou vers un autre site. Si vous choisissez un comportement "on-click" pour votre carte de contenu, n'oubliez pas de mettre à jour votre **texte de lien** en conséquence.

Les actions suivantes sont disponibles pour les liens de la carte de contenu :

| Action | Description |
|---|---|
| Rediriger vers une URL Web | Ouvrir une page Web non native. |
| [Lien profond dans l'application]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | Lien profond vers un écran existant de votre appli. |
| Enregistrer un événement personnalisé | Choisissez un [événement personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) à déclencher. Peut être utilisé pour afficher une autre carte de contenu ou déclencher des envois de messages supplémentaires. |
| Enregistrer un attribut personnalisé | Choisissez un [attribut personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) à définir pour l'utilisateur actuel. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Les options **Log Custom Event** et **Log Custom Attribute** nécessitent la compatibilité avec la version suivante du SDK :

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

## Étape 4 : Configurer des paramètres supplémentaires (facultatif)

Vous pouvez utiliser des [paires clé-valeur]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) pour créer des catégories pour vos cartes, créer [plusieurs flux de cartes de contenu]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds) et personnaliser la façon dont les cartes sont triées.

Pour ajouter des paires clé-valeur à votre message, accédez à l'onglet **Paramètres** et sélectionnez **Ajouter une nouvelle paire.**

## Étape 5 : Créer le reste de votre campagne ou de votre Canvas

{% tabs %}
{% tab Campaign %}

Construisez le reste de votre campagne. Vous trouverez dans les sections suivantes des informations complémentaires sur la manière d'utiliser au mieux nos outils pour créer des cartes de contenu.

#### Choisir une planification ou un déclencheur pour la livraison

Les cartes de contenu peuvent être diffusées en fonction d'une heure planifiée, d'une action ou d'un déclencheur API. Pour en savoir plus, reportez-vous à la section [Planification de votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Vous pouvez également définir la durée de la campagne et les [heures calmes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) et déterminer l'expiration de la carte de contenu. Définissez une date d’expiration spécifique ou le nombre de jours avant l’expiration de la carte (jusqu’à 30 jours). Toutes les variantes ont la même date d’expiration.

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

##### Livraison planifiée

Pour les campagne de cartes de contenu avec une livraison planifiée, vous pouvez choisir quand Braze évalue l’éligibilité et la personnalisation de l’audience pour les nouvelles campagnes de cartes de contenu en spécifiant quand la carte est créée. Pour en savoir plus, reportez-vous à la rubrique [Création de cartes]({{site.baseurl}}/card_creation).

#### Choisir les utilisateurs à cibler

Ensuite, [ciblez les utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) en sélectionnant des segments ou des filtres afin de restreindre votre audience. Vous recevez automatiquement un aperçu de ce à quoi ressemble approximativement la population de ce segment. Veuillez noter que l'appartenance exacte à un segment est toujours calculée avant l'envoi du message.

{% multi_lang_include target_audiences.md %}

#### Sélectionner des événements de conversion

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, des [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), après avoir reçu une campagne. Vous avez la possibilité d’autoriser une fenêtre allant jusqu’à 30 jours pendant laquelle une conversion sera comptée si l’utilisateur entreprend l’action spécifiée.

{% endtab %}

{% tab Canvas %}

Si vous ne l’avez pas déjà fait, complétez les sections restantes de votre composant de Canvas. Pour plus de détails sur la manière de créer le reste de votre Canvas, de mettre en œuvre les [tests multivariés]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) et la [sélection intelligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/), etc., reportez-vous à l'étape [Créer votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de notre documentation sur le Canvas.

{% endtab %}
{% endtabs %}

## Étape 6 : Revue et déploiement

Une fois que vous avez fini de créer la dernière partie de votre campagne ou de votre Canvas, passez en revue ses détails, [testez-la]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/), puis envoyez-la lorsque vous êtes prêt.

{% alert warning %}
Une fois qu’une carte de contenu est lancée, elle ne peut plus être modifiée. On peut seulement arrêter de les envoyer à des nouveaux utilisateurs et les retirer des flux des utilisateurs. Reportez-vous à la section [Mise à jour des cartes d'envoi]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-launched-cards) pour comprendre comment vous pouvez aborder ce scénario.
{% endalert %}

Ensuite, consultez la section [Rapports sur les cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/) pour voir comment accéder aux résultats de vos campagnes de carte de contenu.

## Choses à savoir

### Limites de charge utile et d'alimentation

Afin d'optimiser les performances, les cartes de contenu sont soumises à deux contraintes principales : une limite de taille pour chaque carte et un nombre maximal de cartes pouvant apparaître dans un flux.

#### Limites de taille pour les cartes de contenu

La charge utile totale des données pour une seule carte de contenu ne doit pas dépasser 2 Ko **après** le rendu de toute personnalisation Liquid. Ceci comprend :

* Titre
* Message
* URL de l'image (longueur de la chaîne de caractères URL elle-même, et non taille du fichier image)
* Texte du lien
* URL de lien pour toutes les plateformes spécifiées (les URL distinctes pour iOS, Android et le Web sont toutes prises en compte dans le total)
* Paires clé-valeur (les noms des clés et leurs valeurs)

L'utilisation de Liquid pour extraire de longues chaînes de caractères (provenant par exemple d'attributs personnalisés) peut entraîner un dépassement de la limite. 

Le compositeur de campagne affichera un avertissement si votre contenu statique dépasse la limite. (Nous ne prévoyons pas la taille du contenu dynamique à l'aide de Liquid.) **Si la taille du message dépasse 2 Ko, l'envoi de messages sera interrompu.** Vous pouvez consulter ces interruptions dans le journal des activités des messages avec la raison indiquée`Content card maximum size exceeded`.

{% alert important %}
Lors des envois tests, les cartes de contenu dépassant 2 Ko peuvent toujours être livrées et affichées correctement.
{% endalert %}

Voici quelques bonnes pratiques pour la gestion de la taille de la charge utile des cartes de contenu :

* Veuillez utiliser des raccourcisseurs d'URL pour les liens longs. Les URL, en particulier celles qui contiennent de nombreux paramètres de suivi, peuvent rencontrer des problèmes de limite de taille. L'utilisation d'un service de raccourcissement d'URL peut considérablement réduire le nombre de caractères et libérer de l'espace dans la charge utile.
* Tronquer le contenu dynamique avec Liquid. Lors de la personnalisation de cartes à l'aide de texte dynamique provenant d'attributs utilisateur ou d'appels API, la longueur du contenu peut être imprévisible. Veuillez utiliser de manière proactive des filtres Liquid tels que`truncate`pour limiter la longueur de tout texte dynamique.
* Soyez efficace grâce aux URL multiplateformes. La limite de 2 Ko inclut les URL de toutes les plateformes que vous définissez. L'utilisation d'URL longues et uniques pour chaque plateforme peut augmenter considérablement la taille de la charge utile. Dans la mesure du possible, veuillez utiliser un lien unique compatible avec toutes les plateformes ou recourir à des raccourcisseurs d'URL si nécessaire.
* Envisagez l'utilisation de bannières pour enrichir votre contenu. Pour les cas d'utilisation qui nécessitent systématiquement de grandes quantités de contenu, les cartes de contenu peuvent ne pas constituer le canal approprié. Les bannières ne sont pas soumises à la même limitation de charge utile de 2 Ko et sont plus adaptées à l'intégration de contenus plus riches directement dans l'expérience sur l'application ou le site Web.

#### Nombre de cartes dans le flux

Chaque utilisateur peut avoir jusqu'à 250 cartes de contenu non expirées dans son flux à un moment donné. Lorsque cette limite est dépassée, Braze cesse de renvoyer les cartes les plus anciennes, même si elles ne sont pas lues. Les cartes rejetées sont également prises en compte dans cette limite, ce qui signifie qu'un nombre élevé de cartes rejetées peut réduire l'espace disponible pour les cartes plus anciennes.

Afin d'éviter tout problème lié à la limite de la carte, nous vous recommandons de suivre les meilleures pratiques suivantes :

- **Veuillez utiliser des dates d'expiration plus courtes :** Pour les campagnes soumises à des contraintes de temps (telles que les soldes du week-end), veuillez définir une date d'expiration précise. De cette manière, les cartes sont automatiquement supprimées du flux et ne sont plus prises en compte dans la limite lorsqu'elles ne sont plus pertinentes.
- **Utilisation de la suppression basée sur l'action :** Configurez des événements de suppression pour les cartes liées aux transactions ou basées sur des objectifs. Par exemple, une carte invitant un utilisateur à compléter son profil devrait être supprimée dès qu'un`profile_completed`événement utilisateur est enregistré.
- **Vérifier les campagnes de longue durée :** Veuillez examiner les campagnes récurrentes ou en cours afin de vous assurer qu'elles ne nuisent pas à l'expérience de vos utilisateurs en surchargeant le flux avec un nombre excessif de cartes au fil du temps.

### Comprendre la rééligibilité pour les cartes de contenu

La rééligibilité détermine si et quand un utilisateur peut recevoir un message provenant de la même campagne plus d'une fois. Pour les cartes de contenu, il est essentiel de comprendre ce fonctionnement afin de gérer les campagnes récurrentes et de garantir que les utilisateurs ne reçoivent pas de messages en double ou obsolètes.

{% alert tip %}
Souhaitez-vous que votre contenu reste accessible au-delà de 30 jours ? Veuillez essayer [les bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners).
{% endalert %}

#### Comment la rééligibilité est-elle calculée ?

Si vous activez la rééligibilité, le compte à rebours permettant à un utilisateur de « réintégrer » une campagne commence après l'envoi du message. Le moment précis où ce compte à rebours commence dépend des paramètres de création de votre carte :

* Les cartes de contenu utilisant [la première impression]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/#differences-between-creating-cards-at-launch-or-entry-versus-at-first-impression) se basent sur le temps d'impression pour calculer la rééligibilité.
* Les cartes de contenu créées lors du lancement de la campagne ou lors de l'entrée dans l'étape du canvas utilisent la date d'envoi ou l'heure d'impression la plus récente.

#### L'expiration au bout de 30 jours et la réadmissibilité

Une source fréquente de confusion réside dans l'interaction entre la rééligibilité à la campagne et l'expiration automatique de toutes les cartes de contenu après 30 jours. 

Toutes les cartes de contenu sont automatiquement supprimées des systèmes Braze 30 jours après leur envoi ou leur suppression. Si vous avez une campagne récurrente de longue durée avec la rééligibilité désactivée, un utilisateur peut toujours recevoir la même carte après 30 jours. Lorsque la carte d'origine est supprimée, le système ne voit plus que cet utilisateur a reçu la campagne, ce qui le rend à nouveau éligible lors de sa prochaine session. 

Pour que les utilisateurs ne reçoivent qu'une seule fois un message provenant d'une campagne spécifique, veuillez ajouter un filtre d'audience à votre campagne ou à votre étape du canvas pour les utilisateurs qui n'ont pas encore reçu de message provenant de cette campagne. Ce filtre constitue le moyen le plus fiable d'éviter les envois en double dans le cadre de campagnes de longue durée.

### Gestion des cartes de contenu en ligne/en production/instantanées

Une fois que les cartes de contenu ont été envoyées, elles attendent dans une "boîte de réception", prêtes à être remises à l'utilisateur (comme c'est le cas pour les e-mails). Une fois que le contenu a été introduit dans la carte de contenu (au moment de l'affichage), il ne peut plus être modifié pendant sa durée de vie. Cela s'applique même si vous appelez une API par l'intermédiaire du contenu connecté et que les données de l'endpoint changent. Ces données ne seront pas mises à jour. On peut seulement arrêter de les envoyer à des nouveaux utilisateurs et les retirer des flux des utilisateurs. Si vous modifiez une campagne, seules les futures cartes envoyées auront la mise à jour.

#### Mise à jour des cartes lancées

Pour remplacer une carte destinée à des utilisateurs qui l'ont déjà reçue, veuillez utiliser l'une des méthodes suivantes :

##### Option 1 : Veuillez dupliquer la campagne (recommandé pour les modifications immédiates).

{% alert tip %}
Nous recommandons cette option pour les messages dans lesquels vous affichez le contenu le plus récent dans la carte de contenu, lorsque les modifications doivent être affichées immédiatement ou lorsque la rééligibilité est désactivée.
{% endalert %}

La première approche consiste à archiver la campagne et à lancer une nouvelle campagne identique :

1. Veuillez interrompre la campagne initiale et, lorsque vous y êtes invité, sélectionner `Remove card after the next sync`.
2. Veuillez dupliquer la campagne, modifier vos éléments et lancer la nouvelle version.

Lorsque vous dupliquez la campagne, il est nécessaire de définir l’audience cible pour la nouvelle version. Veuillez utiliser les filtres de segmentation pour déterminer qui recevra la carte mise à jour :
* Si les utilisateurs ne doivent jamais être rééligibles pour une carte de contenu, vous pouvez filtrer les utilisateurs qui n'ont pas reçu la version précédente de la carte de contenu en réglant le filtre `Received Message from Campaign` sur la condition `Has Not`.
* Si les utilisateurs qui ont reçu la carte précédente doivent être rééligibles dans X jours, vous pouvez définir le filtre pour `Last Received Message from specific campaign` à plus de X jours **OU** `Received Message from Campaign` avec la condition `Has Not`.

###### Impact

* **Destinataires actuels :** Les nouveaux destinataires et les destinataires actuels verront la carte mise à jour lors de la prochaine actualisation du flux, s'ils sont éligibles.
* **Rapport :** Chaque version de la carte ferait l'objet d'une analyse/analytique distincte.

Supposons que vous ayez configuré une campagne pour qu'elle soit déclenchée par le début d'une session et que la rééligibilité soit fixée à 30 jours. Un utilisateur a reçu la campagne il y a deux jours et vous souhaitez modifier la copie. Tout d'abord, vous archivez la campagne et retirez les cartes du flux. Ensuite, vous reproduisez la campagne et la lancez à nouveau avec le nouveau texte. Si l'utilisateur a une autre session, il recevra immédiatement la nouvelle carte.

##### Option 2 : Veuillez interrompre et relancer la même campagne.

{% alert tip %}
Nous vous recommandons d'utiliser cette option pour les messages uniques dans un centre de notification ou une boîte de réception (comme les promotions), lorsqu'il est important que les analyses/analytiques soient unifiées, ou lorsque l'actualité du message n'est pas un problème (par exemple, les destinataires existants peuvent attendre la fenêtre d'éligibilité avant de voir les cartes mises à jour).
{% endalert %}

Cette approche permet de regrouper toutes vos analyses dans une seule campagne. Les nouveaux utilisateurs éligibles recevront la nouvelle carte, mais cela retardera la mise à jour pour les destinataires existants jusqu'à ce qu'ils redeviennent éligibles :

1. Veuillez interrompre votre campagne et, lorsque vous y êtes invité, sélectionnez **Supprimer la carte après la prochaine synchronisation**.
2. Modifier votre campagne si nécessaire.
3. Redémarrer votre campagne.

###### Impact

* **Destinataires actuels :** Les utilisateurs qui ont déjà reçu la carte ne recevront pas les cartes mises à jour tant qu'ils ne seront pas rééligibles. Si la rééligibilité est désactivée, ils ne recevront jamais la nouvelle carte.
* **Rapport :** Une campagne contiendra toutes les analyses de rapports pour les versions de cartes lancées. Braze ne fera pas la différence entre les versions lancées.

Imaginons que vous ayez une campagne déclenchée par le démarrage d'une session et dont la rééligibilité est fixée à 30 jours. Un utilisateur a reçu la campagne il y a deux jours et vous souhaitez modifier la copie. Tout d'abord, arrêtez la campagne et supprimez la carte du flux. Ensuite, republiez la campagne avec le nouveau texte. Si l'utilisateur a une autre session, il recevra la nouvelle carte dans 28 jours.

#### Suppression et expiration des cartes

##### Retrait manuel de la carte

Vous pouvez supprimer manuellement les cartes pour les flux de tous les utilisateurs à tout moment en interrompant la campagne.

1. Veuillez ouvrir la campagne de cartes de contenu et sélectionner Arrêter la campagne.
2. Lorsque vous y êtes invité, veuillez sélectionner **« Supprimer la carte après la prochaine synchronisation** ». La carte sera supprimée lors de la prochaine actualisation du flux.

##### Retrait automatisé des cartes {#action-based-card-removal}

Vous pouvez supprimer automatiquement une carte lorsqu'un utilisateur effectue une action spécifique, telle que finaliser un achat ou activer une fonctionnalité.

Dans votre campagne ou votre étape du canvas, veuillez définir un événement de suppression. Lorsqu'un utilisateur effectue cet événement, la carte sera supprimée de son flux lors de l'actualisation suivante, après que Braze aura traité l'événement. 

{% alert note %}
Cette suppression n'est pas immédiate. Il existe un délai de traitement, donc cela peut prendre plusieurs minutes et nécessiter plusieurs fois le fait d’actualiser le flux avant que la carte ne disparaisse.
{% endalert %}

{% alert tip %}
Vous pouvez spécifier plusieurs événements personnalisés ou achats avant qu’une carte soit retirée du flux des utilisateurs. Lorsque l'utilisateur effectue l' **une de** ces actions, toutes les cartes existantes envoyées par les cartes de la campagne sont supprimées. Toutes les futures cartes éligibles continueront d’être envoyées conformément au calendrier du message.
{% endalert %}

![Panneau Conditions de suppression des cartes de contenu avec l'option Événement de suppression des cartes de contenu.]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

##### Expiration de la carte

Les cartes de contenu restent disponibles pendant 30 jours à compter de leur envoi. Passé ce délai, Braze les supprime des flux des utilisateurs et les efface de ses systèmes.

#### Faire en sorte que les cartes durent plus de 30 jours

{% alert tip %}
Pour les cas d'utilisation nécessitant que les messages soient conservés plus longtemps que la limite de 30 jours imposée aux cartes de contenu de type bannière, il est recommandé d'utiliser des bannières. Les bannières sont conçues pour être continuelles et n'ont pas de date d'expiration obligatoire, ce qui leur permet de rester visibles aussi longtemps que nécessaire.
{% endalert %}

Si vous souhaitez qu'une carte semble toujours disponible (i.ec'est-à-dire qu'elle dure plus longtemps que la durée maximale de 30 jours), vous pouvez créer une campagne récurrente qui remplace efficacement la carte tous les 30 jours :

1. Fixez la durée de la carte de contenu à 30 jours.
2. Fixez la rééligibilité de la campagne à 30 jours.
3. Réglez la campagne pour qu'elle se déclenche au "début de la session".
