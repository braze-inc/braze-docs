---
nav_title: Notes de version
article_title: Notes de version
page_order: 4
layout: dev_guide
guide_top_header: "Notes de version"
guide_top_text: "C’est là que vous trouverez toutes les mises à jour de la plateforme Braze, avec <a href='/docs/help/release_notes/#most-recent'>les dernières mises à jour de la plateforme</a> suivantes."
page_type: landing
search_rank: 1
description: "Cette page de destination est le foyer des notes de version de Braze. C’est là que vous trouverez toutes les mises à jour de notre plateforme et de nos SDK Braze ainsi que la liste des fonctionnalités retirées."

guide_featured_title: "Notes de version"
guide_featured_list:
  - name: 2025
    link: /docs/help/release_notes/2025/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2024
    link: /docs/help/release_notes/2024/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2023
    link: /docs/help/release_notes/2023/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2022
    link: /docs/help/release_notes/2022/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2021
    link: /docs/help/release_notes/2021/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2020
    link: /docs/help/release_notes/2020/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2019
    link: /docs/help/release_notes/2019/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2018
    link: /docs/help/release_notes/2018/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2017
    link: /docs/help/release_notes/2017/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2016
    link: /docs/help/release_notes/2016/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: Obsolescences
    link: /docs/help/release_notes/deprecations/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: Journaux de modifications SDK
    link: /docs/developer_guide/changelogs/
    image: /assets/img/braze_icons/file-code-01.svg

---

# Notes de version Braze les plus récentes {#most-recent}

> Braze publie des informations sur les mises à jour du produit à une cadence mensuelle, en s’alignant sur les versions majeures du produit, bien que le produit soit mis à jour avec des améliorations diverses sur une base hebdomadaire.
> <br>
> <br>

> Pour plus d'informations sur l'une des mises à jour répertoriées dans cette section, contactez votre gestionnaire de compte ou [ouvrez un ticket de support]({{site.baseurl}}/user_guide/administrative/access_braze/support/). Vous pouvez également consulter [nos journaux de modifications SDK]({{site.baseurl}}/developer_guide/changelogs) pour voir plus d'informations sur nos versions mensuelles de SDK, mises à jour et améliorations.
 
## Publication le 1er avril 2025

### Mises à jour de la navigation sur Braze

La navigation mise à jour dans Braze est conçue pour vous aider à accéder efficacement aux fonctionnalités et au contenu sur tous les appareils. Notez que l'option permettant de passer d'une version de navigation à l'autre n'est plus disponible. Pour en savoir plus, consultez notre article consacré à [la navigation dans la Braze]({{site.baseurl}}/user_guide/administrative/access_braze/navigation).

### Guide du développeur démêler

Auparavant, de nombreuses tâches au niveau de la plateforme étaient réparties sur plusieurs pages, l'intégration du SDK Swift étant par exemple répartie sur six pages. En outre, les fonctionnalités partagées étaient documentées individuellement pour chaque plateforme, ce qui signifie qu'une recherche sur un sujet tel que "Configuration des notifications push" aboutissait à 10 pages différentes.

**Avant :**

![La documentation Swift précédente se trouve dans la section Guides d'intégration de la plate-forme.]({% image_buster /assets/img/before_swift.png %})

Désormais, les tâches au niveau de la plateforme ont été fusionnées en une seule page et les fonctionnalités partagées du SDK existent désormais sur la même page (avec l'aide de notre nouvelle fonctionnalité de navigation vers le SDK). Par exemple, il n'y a plus qu'une seule page pour l'intégration du SDK Braze, où vous pouvez passer d'une plateforme à l'autre en sélectionnant un onglet en haut de la page. Lorsque vous le faites, même la table des matières de la page est mise à jour pour refléter l'onglet sélectionné.

**Après :**

![La documentation Swift mise à jour se trouve dans l'onglet Swift de l'article Intégration du SDK.]({% image_buster /assets/img/after_swift.png %})

![La documentation Android mise à jour se trouve dans l'onglet Android de l'article Intégration du SDK.]({% image_buster /assets/img/after_android.png %})

### Contribution aux documents de Braze

Si vous ne le saviez pas, notre documentation est entièrement open-source ! Pour en savoir plus, consultez notre [Guide de la contribution]({{site.baseurl}}/contributing/home). Ce mois-ci, nous avons documenté certaines fonctionnalités du site, comme le [développement automatique des sections]({{site.baseurl}}/contributing/content_management/sections#forcing-auto-expand) et le [rendu du contenu généré par l'API]({{site.baseurl}}/contributing/generating_a_preview#step-2-start-a-local-server).

### Flexibilité des données

#### Mise à jour des propriétés de l'entrée Canvas

Les propriétés d'entrée dans le canvas font désormais partie des [variables de contexte du canvas.]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) Chaque variable de contexte comprend un nom, un type de données et une valeur qui peut inclure Liquid. Pour plus d'informations, reportez-vous au [composant Contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context).

#### Mise à jour des filtres de segmentation pour les filtres de numéros de téléphone

Les filtres de segmentation ont été mis à jour pour refléter les modifications apportées à deux filtres de numéros de téléphone :

- [Numéro de téléphone non formaté]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#unformatted-phone-number) (anciennement **numéro de téléphone**) : Segmente vos utilisateurs en fonction de leur numéro de téléphone non formaté.
- [Numéro de téléphone]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#phone-number) (anciennement **numéro de téléphone de l'expéditeur**) : Segmente vos utilisateurs en fonction du champ de numéro de téléphone formaté E.164.

#### Supprimer les données personnalisées

Au fur et à mesure que vous créez des campagnes et des segments ciblés, vous constaterez peut-être que vous n'avez plus besoin d'un événement personnalisé ou d'un attribut personnalisé. Vous pouvez maintenant [supprimer ces données personnalisées]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data#deleting-custom-data) et retirer leurs références de votre app.

#### Importation d'utilisateurs avec des adresses e-mail et des numéros de téléphone

Vous pouvez désormais utiliser une adresse e-mail ou un numéro de téléphone pour [importer des utilisateurs]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#importing-with-email-addresses-and-phone-numbers) et omettre un ID externe ou un alias utilisateur.

#### Résolution des problèmes d'identifiant à l'initiative du fournisseur de services

L'identifiant initié par le fournisseur de services dispose désormais d'une [section de résolution des problèmes]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#troubleshooting) pour vous aider à résoudre les problèmes liés à SAML et à l'authentification unique.

#### Résolution des problèmes liés à l'importation d'utilisateurs

La [section "Résolution des problèmes liés à l'importation d'utilisateurs]({{site.baseurl}}/user_guide/data/user_data_collection/user_import#troubleshooting) " comporte des entrées nouvelles et mises à jour, notamment sur la manière de résoudre les problèmes liés aux lignes manquantes dans vos fichiers CSV importés.

#### Questions fréquemment posées sur les extensions de segments

Consultez notre [foire aux questions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#frequently-asked-questions) sur les extensions de segments, notamment sur la façon dont vous pouvez créer une extension de segments qui utilise plusieurs événements personnalisés.

#### Délais personnalisés et prolongés

{% multi_lang_include release_type.md release="Accès anticipé" %}

Vous pouvez définir un [délai personnalisé]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step#personalized-delays) pour vos utilisateurs et l'utiliser avec une étape Contexte pour sélectionner la variable contextuelle à retarder.

Vous pouvez également prolonger les délais jusqu'à deux ans. Par exemple, si vous intégrez de nouveaux utilisateurs à votre application, vous pouvez ajouter un délai prolongé de deux mois avant d'envoyer une étape Message pour inciter les utilisateurs qui n'ont pas encore démarré une session à le faire.

#### Attributs par défaut du profil utilisateur pour Snowflake

{% multi_lang_include release_type.md release="Beta" %}

Il y a maintenant trois [attributs de profil utilisateur par défaut]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/user_attributes) dans Snowflake. Chaque vue est conçue pour un cas d'utilisation spécifique, avec ses propres considérations en matière de performances. Par exemple, vous pouvez recevoir un snapchat périodique des attributs par défaut d'un profil utilisateur.

### Canaux robustes

#### Principes de base de l'envoi de messages

[Fondamentaux de l'envoi de messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals) est une nouvelle section des outils d'engagement qui abrite les concepts et les termes partagés pour les campagnes et les toiles, tels que l'archivage et la localisation des messages.

#### Domaines personnalisés WhatsApp

Vous pouvez désormais attribuer des [domaines personnalisés]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/custom_domains/) à un ou plusieurs groupes d'abonnement WhatsApp.

#### Messages in-app déclenchés pour Canvas

Vous pouvez désormais sélectionner un [déclencheur pour vos messages in-app]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas) au démarrage de la session, ou en fonction d'événements personnalisés et d'achats. Une fois les délais écoulés et les options d'audience cochées, les messages in-app sont mis en ligne/en production/instantané lorsque l'utilisateur atteint l'étape Message. Si un utilisateur démarre une session et effectue l'événement déclencheur pour le message in-app, l'utilisateur verra le message in-app. 

#### Limiter le volume d'entrée pour les canvas

Vous pouvez limiter le nombre de personnes susceptibles d'entrer dans ce Canvas en fonction d'une cadence choisie (quotidienne, pendant toute la durée du Canvas ou à chaque fois que le Canvas est planifié). Par exemple, vous pouvez [paramétrer les contrôles d'entrée de]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas?tab=action-based%20delivery#step-2c-set-your-target-entry-audience) manière à ce que la toile ne puisse être envoyée qu'à 5 000 utilisateurs par jour.

#### Nouveau cas d'utilisation : Système d'e-mail de rappel de réservation

Découvrez comment vous pouvez utiliser les fonctionnalités de Braze pour [créer un service d'envoi de messages e-mail de rappel de réservation]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/booking_use_case). Le service permettra aux utilisateurs de prendre des rendez-vous et leur enverra des messages pour leur rappeler leurs rendez-vous à venir. Bien que ce cas d'utilisation utilise des messages e-mail, vous pouvez envoyer des messages dans n'importe quel canal, ou dans plusieurs, sur la base d'une seule mise à jour d'un profil utilisateur.

#### Suivi des clics pour des liens spécifiques

Vous pouvez [désactiver le suivi des clics]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links#turning-off-click-tracking-on-a-link-to-link-basis) pour des liens spécifiques en ajoutant du code HTML à votre message e-mail dans l'éditeur HTML ou aux composants dans l'éditeur par glisser-déposer.

#### Gestion dynamique de la passerelle du service de notification push d'Apple

La [gestion dynamique des passerelles APN]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_dynamic-apns-gateway-management) améliore la fiabilité et l'efficacité des notifications push d'iOS en détectant automatiquement l'environnement APN adéquat. Auparavant, vous deviez sélectionner manuellement des environnements APN (développement ou production) pour vos notifications push, ce qui entraînait parfois des configurations de passerelle incorrectes, des échecs de réception/distribution et des erreurs BadDeviceToken.

#### Prise en charge de Flutter pour les cartes bannières

{% multi_lang_include release_type.md release="Accès anticipé" %}

Les cartes bannières sont désormais compatibles avec Flutter. De plus, toute la documentation de Banner Card a été revue pour faciliter son utilisation. Consultez les articles suivants pour commencer :

- [À propos de Banner Cards]({{site.baseurl}}/developer_guide/banner_cards)
- [Créer des campagnes de cartes bannières]({{site.baseurl}}/developer_guide/banner_cards/creating_campaigns)
- [Intégrer des cartes bannières dans votre application]({{site.baseurl}}/developer_guide/banner_cards/embedding_cards)

#### Suivi des clics sur WhatsApp

{% multi_lang_include release_type.md release="Accès anticipé" %}

Le [suivi des clics]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking/) vous permet de savoir quand quelqu'un clique sur un lien dans votre message WhatsApp, ce qui vous donne une vision claire du contenu qui suscite l'engagement. Braze raccourcit vos URL, ajoute un suivi en coulisses et enregistre les clics au fur et à mesure qu'ils se produisent.

#### Questions fréquemment posées pour push

Consultez notre nouvel article [Push FAQ]({{site.baseurl}}/user_guide/message_building_by_channel/push/faq) qui aborde certaines des questions les plus fréquemment posées lors de l'implémentation des campagnes push.

#### Résolution des problèmes de poussée

La [résolution des problèmes]({{site.baseurl}}/user_guide/message_building_by_channel/push/troubleshooting) liés aux notifications push propose un certain nombre d'étapes pour vous aider à relever les défis liés à la réception/distribution des notifications push. Par exemple, si vous rencontrez des problèmes de réception/distribution avec les notifications push, nous avons compilé les étapes à suivre pour résoudre le problème.

### Nouveaux partenariats Braze

#### Movable Ink Da Vinci - Contenu dynamique

L'intégration de Braze et Movable Ink [Da Vinci]({{site.baseurl}}/partners/movable_ink_da_vinci) permet aux marques de diffuser des messages hautement personnalisés en s'appuyant sur le moteur de décision de contenu piloté par l'intelligence artificielle de Da Vinci. Da Vinci sélectionne le contenu le plus pertinent pour chaque utilisateur et déploie les messages de façon fluide/sans heurts/de façon homogène, etc.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [Flutter SDK 13.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Mise à jour du pont natif Android du [SDK Android 33.0.0 vers 35.0.0.](https://github.com/braze-inc/braze-android-sdk/compare/v33.0.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
        - La version minimale requise du SDK Android est 25. Pour plus de détails [, cliquez ici.](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)
- [Swift SDK v11.8.0-11.9.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [SDK Web v5.8.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

## Publication le 4 mars 2025

### Reports

Braze a mis à jour notre définition de ce qu'est un échec provisoire d'envoi et envoie un nouvel événement appelé [reports à]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/#email-performance) partir du 25 février 2025 à 10h EST.

Pour les clients de Sendgrid, nous avons apporté une modification afin de séparer les événements d'ajournement de nos événements d'échec provisoire envoi. Nous considérons les événements différés comme un échec provisoire d'envoi. Cela concerne tous les clients de Sendgrid qui utilisent Currents, Query Builder, SQL Extension, Snowflake Data Sharing ou notre produit Transactional Email.

#### Comportement antérieur

Avant le 25 février 2025, un événement différé pour une adresse e-mail sur une campagne ou un Canvas enregistre un événement d'échec provisoire d'envoi à chaque fois. Par conséquent, les reports sont inclus dans les données relatives aux échecs provisoires d'envoi. Un utilisateur ou une campagne peut ainsi signaler plus d'événements d'échec provisoire d'envoi que prévu. 

#### Nouveau comportement

À partir du 25 février 2025, un événement différé n'enregistrera plus à chaque fois un événement d'échec provisoire d'envoi. Au lieu de cela, nous enregistrerons un événement d'échec provisoire d'envoi une fois par envoi pour l'adresse e-mail, quel que soit le nombre de fois que l'e-mail est retenté ou différé.

#### Ce que cela signifie

Vous constaterez une baisse sensible du volume des événements provisoires d'envoi à partir du 25 février 2025, ce qui entraînera les changements potentiels suivants :

- Diminution des échecs provisoires d'envoi pour tous les rapports créés à l'aide du générateur de requêtes.
- Réduction de la taille des segments à l'aide des extensions SQL si vous ciblez des utilisateurs ayant subi X échecs provisoires d'envoi sur une période de Y.
- Baisse du nombre d'échecs provisoires d'envois réalisés à l'aide de Currents et de l'une de nos fonctionnalités à l'aide de Snowflake.
- Baisse du nombre d'échecs provisoires d'envois pour le produit "Transactional Email".

Pour les clients de Sparkpost, il n'y a pas d'impact sur vos données d'événements d'échec provisoire, à la place vous commencerez à recevoir un nouvel événement e-mail, deferral, dans Currents et Snowflake.

### Guide du développeur démêler

Les contenus identiques partagés entre plusieurs SDK commencent à être fusionnés grâce à la nouvelle fonctionnalité d'onglet SDK du site de documentation. Ce mois-ci, l'[intégration SDK]({{site.baseurl}}/developer_guide/sdk_integration/), l'[initialisation SDK]({{site.baseurl}}/developer_guide/sdk_initialization/) et les [cartes de contenu]({{site.baseurl}}/developer_guide/content_cards/) ont été combinées. Restez à l'écoute pour d'autres mises à jour dans les mois à venir.

### Flexibilité des données
 
#### ID de Braze pour les profils utilisateurs

Le profil utilisateur comprend désormais un [ID Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles#user-profiles). Vous pouvez l'utiliser lors de la recherche de profils utilisateurs.

#### Reports

Braze a mis à jour sa définition de ce qu'est un échec provisoire (soft bounce) et envoie un nouvel événement appelé [report]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-performance), c'est-à-dire lorsqu'un e-mail n'a pas été livré immédiatement, mais que Braze relance l'e-mail jusqu'à 72 heures après cet échec provisoire de la réception/distribution afin de maximiser les chances de réussite avant que les tentatives pour cette campagne spécifique ne soient interrompues.

#### Relations entre entités Snowflake
 
Nous avons mappé les [schémas bruts des tables](https://www.braze.com/docs/assets/download_file/data-sharing-raw-table-schemas.txt) pour les relations entre entités de Snowflake et Braze dans une nouvelle [page de documentation conviviale](https://www.braze.com/docs/partners/data_and_infrastructure_agility/data_warehouses/snowflake/entity_relationships). Il comprend une ventilation des tables `USER_MESSAGES` appartenant à chaque canal, ainsi que des descriptions des clés primaires, étrangères et natives de chaque table.

#### Gestion des identités pour les ID externes

L'utilisation d'une adresse e-mail ou d'une adresse e-mail hachée comme ID externe Braze peut simplifier la gestion des identités dans l'ensemble de vos sources de données. Cependant, il est important de prendre en compte les [risques potentiels]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#identified-user-profiles) pour la confidentialité des utilisateurs et la sécurité des données.
 
### Libérer la créativité

#### Didacticiels sur les liquides

Ajout de trois [didacticiels Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/operators/#tutorials) sur l'utilisation des opérateurs dans les scénarios suivants.

<table border="1">
  <tr>
    <td>Choix d'un message avec un attribut personnalisé de type entier.</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/integer.png %}" alt="L&apos;étape de composition dans Braze affichant un message avec un attribut personnalisé de type entier." /></td>
  </tr>
  <tr>
    <td>Choix d'un message avec un attribut personnalisé de type chaîne de caractères.</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/string.png %}" alt="L&apos;étape de composition dans Braze affichant un message avec une chaîne de caractères en attribut personnalisé." /></td>
  </tr>
  <tr>
    <td>Abandon d'un message en fonction de l'emplacement/localisation.</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/location.png %}" alt="L&apos;étape de composition dans Braze montre l&apos;interruption d&apos;un message en fonction de l&apos;emplacement/localisation." /></td>
  </tr>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Étapes du contexte pour Canvas
 
{% multi_lang_include release_type.md release="Accès anticipé" %}
 
Utilisez les [étapes Contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) pour créer ou mettre à jour un ensemble de variables qui conseillent le contexte d'un utilisateur (ou des informations sur le comportement de cet utilisateur) au fur et à mesure qu'il se déplace dans un Canvas.

#### Délai personnalisé

{% multi_lang_include release_type.md release="Accès anticipé" %}

Vous pouvez définir un [délai personnalisé]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) pour vos utilisateurs en basculant la case Délai **personnalisé** dans votre étape Délai. Vous pouvez l'utiliser avec une étape Contexte pour sélectionner une variable de contexte à retarder.

Lorsque vous configurez une étape du canvas dans votre parcours utilisateur, vous pouvez désormais créer un délai allant jusqu'à 2 ans.

#### Annulation de la synchronisation automatique

Lors de la [rédaction d'un message e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-3-compose-your-email), vous pouvez revenir à la synchronisation automatique dans l'onglet Texte en clair en sélectionnant l'icône Régénérer à partir du HTML, qui n'apparaît que si le texte en clair n'est pas synchronisé.

![Le bouton de retour pour la synchronisation automatique dans Braze.]({% image_buster /assets/img/release_notes/2025_05_04/regenerate_from_html.png %})
 
### Canaux robustes

#### Mises à jour en ligne/en production/instantané d'Android

Bien que les mises à jour en ligne/instantanées ne soient pas officiellement disponibles avant le mois d'août, elles ne sont pas encore disponibles.
[Android 16](https://android-developers.googleblog.com/2025/01/first-beta-android16.html), notre page [Mises à jour en direct pour Android]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=android&tab=local) vous montre comment émuler leur comportement, afin que vous puissiez afficher des notifications interactives sur l'écran de verrouillage, similaires aux [activités en direct pour le SDK Braze de Swift]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift). Contrairement aux mises à jour en ligne/en production/instantanées officielles, cette fonctionnalité peut être mise en œuvre pour les anciennes versions d'Android.

#### Copier des campagnes avec des drapeaux de fonctionnalité dans plusieurs espaces de travail

Vous pouvez désormais [copier des campagnes avec des drapeaux de fonctionnalité dans les espaces de travail.]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/#copying-campaigns-with-feature-flags) Pour ce faire, assurez-vous que l'espace de travail de destination dispose d'une expérience d'indicateur de fonctionnalité configurée avec un ID correspondant à l'indicateur de fonctionnalité référencé dans la campagne d'origine.

#### Prise en charge de nouveaux types d'envoi de messages WhatsApp

Les messages WhatsApp prennent désormais en charge les [envois de vidéos, d'audio et de documents]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#outbound-messages). Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.

#### Envois de messages de droite à gauche

La [création de messages de droite à gauche]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) couvre les meilleures pratiques pour rédiger des messages dans des langues qui se lisent de droite à gauche, afin que vos messages s'affichent avec le plus de précision possible.
 
### L'intelligence artificielle et l'automatisation de l’apprentissage machine.
 
#### Recommandations de poste

L'[utilisation des recommandations d'éléments dans les messages]({{site.baseurl}}/user_guide/brazeai/recommendations/using_recommendations) couvre l'objet `product_recommendation` Liquid et comprend un tutoriel pour vous aider à mettre ces connaissances en pratique.

### Nouveaux partenariats Braze
 
#### Email Love - Extensions de canaux
 
Le partenariat entre Braze et [Email Love]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates) s'appuie sur la fonctionnalité Export to Braze d'Email Love et sur l'API de Braze pour télécharger vos modèles d'e-mails vers Braze de façon fluide/sans heurts/de façon façon homogène.

#### VWO - Test A/B
 
L'intégration de Braze et de [VWO]({{site.baseurl}}/partners/data_and_infrastructure_agility/ab_testing/vwo) vous permet d'exploiter les données d'expérience de VWO pour créer des segments ciblés et proposer des campagnes personnalisées.
 
### Mises à jour SDK
 
Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.
 
- [React Native](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Fait passer la version minimale requise de React native à [0.71.0.](https://reactnative.dev/blog/2023/01/12/version-071) Pour plus d'informations, reportez-vous à la [politique de soutien aux versions du](https://github.com/reactwg/react-native-releases#releases-support-policy) groupe de travail React.
    - La version minimale requise d'iOS passe à 12.0.
    - Met à jour les liaisons de la version native d'iOS du [SDK Swift de Braze 7.5.0 à 8.1.0.](https://github.com/braze-inc/braze-swift-sdk/compare/7.5.0...8.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Mise à jour des liens de la version native d'Android du [SDK Android de Braze 29.0.1 vers 30.1.1.](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.1.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)

## Publication le 4 février 2025

### Améliorations apportées à la documentation de Braze

#### Guide du contributeur
Nos récentes mises à jour du [Guide de contribution]({{site.baseurl}}/contributing/your_first_contribution) permettent aux utilisateurs non techniques de contribuer plus facilement à la documentation de Braze.

#### Refonte des données et de l'analyse/analytique (si utilisé comme adjectif)
Pour vous permettre de trouver plus facilement ce que vous cherchez, nous avons séparé les articles qui se trouvaient auparavant sous "Data & Analytics" en " [Data]({{site.baseurl}}/user_guide/data) and [Analytics]({{site.baseurl}}/user_guide/analytics)". 

#### Guide du développeur
Nous avons fait un grand ménage dans toute la documentation du [Guide du développeur Braze]({{site.baseurl}}/developer_guide/home), notamment en fusionnant les "comment faire" répartis sur plusieurs pages en une seule.

Vous trouverez également une nouvelle [page de référence SDK]({{site.baseurl}}/developer_guide/references) qui répertorie l'ensemble de la documentation de référence et des référentiels pour chaque SDK Braze.

##### SDK Unreal Engine Braze
Nous avons migré et réécrit tout le contenu du README du dépôt GitHub du SDK d'Unreal Engine Braze dans sa [section dédiée sur Braze Docs]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=unreal%20engine).

### Flexibilité des données

#### Tableau de bord de l'utilisation de l'API

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Le [tableau de bord de l'utilisation de l'API]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_dashboard) vous permet de surveiller le trafic de votre API REST entrant dans Braze afin de comprendre les tendances de votre utilisation de nos API REST et de résoudre les problèmes éventuels.

#### Ajout d'étiquettes aux attributs personnalisés

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Vous pouvez [ajouter des étiquettes à un attribut personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes#adding-tags) après sa création si vous disposez de l'autorisation "Gérer les événements et les attributs, les clients". Les étiquettes peuvent ensuite être utilisées pour filtrer la liste des attributs.

#### Sélections de catalogue et endpoints de champs de catalogue asynchrones 

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Les endpoints suivants sont désormais généralement disponibles :
* [POST : Créer des champs de catalogue]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields)
* [DELETE : Supprimer un champ du catalogue]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field)
* [DELETE : Supprimer la sélection du catalogue]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection)
* [POST : Créer une sélection de catalogue]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections)

#### Utilisation d'une adresse e-mail pour déclencher des campagnes ou des canevas

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Vous pouvez désormais spécifier un destinataire par adresse e-mail pour déclencher vos [campagnes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users) et [Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=target%20audience#step-2c-set-your-target-entry-audience).

#### Utilisation d'un numéro de téléphone pour identifier un utilisateur via l'API

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Vous pouvez désormais utiliser un numéro de téléphone, en plus d'un alias et d'une adresse e-mail, pour identifier un utilisateur via l'[endpoint de l'API`/users/identify` ]({{site.baseurl}}/api/endpoints/user_data/post_user_identify).

#### Obtenir une trace SAML
Nous avons ajouté des [étapes sur la façon d'obtenir une trace SAML]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up#obtaining-a-saml-trace), ce qui vous aide à résoudre plus efficacement les problèmes liés à l'authentification unique (SSO) SAML avec le support.
 
#### Centres de données spécifiques à une région
Comme Braze se développe pour desservir de nouvelles régions, nous avons ajouté un [article sur les centres de données de Braze]({{site.baseurl}}/user_guide/data/data_centers) afin de clarifier notre approche opérationnelle.
 
### Libérer la créativité
 
#### Notifications de baisse de prix et de retour en stock

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Vous pouvez désormais avertir les clients lorsqu'un article est de nouveau en stock en configurant des [notifications de retour en stock]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications) par le biais d'un Canvas et d'un catalogue.

Vous pouvez également créer des [notifications de baisse de]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/price_drop_notifications) prix pour informer les clients lorsque le prix d'un article a baissé en configurant des notifications de baisse de prix dans un catalogue et dans Canvas.

#### Aperçu de la sélection 

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Après avoir créé une sélection, vous pouvez [voir ce qu'elle donnerait]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/#test-and-preview) pour un utilisateur aléatoire ou pour un utilisateur spécifique.

#### Modélisation de produits de catalogue comprenant des étiquettes Liquid 

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Vous pouvez [créer des modèles d'articles de catalogue qui incluent le liquide]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/#using-liquid).

#### Modèles de canvas
Nous avons ajouté de nouveaux modèles Canvas pour l'[onboarding des utilisateurs avec une enquête de préférences]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/preference_survey) et la [création d'une inscription par e-mail avec double abonnement.]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/email_signup)

#### Gérer les prospects avec Salesforce Sales Cloud pour le B2B
Les marketeurs B2B peuvent notamment utiliser Braze par le biais d'une intégration avec Salesforce Sales Cloud. Pour en savoir plus sur la mise en œuvre de ce [cas d'utilisation]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_salesforce_sales_cloud), cliquez ici.
 
### Canaux robustes

#### Listes de suppression

{% multi_lang_include release_type.md release="Beta" %}
 
[Les listes de suppression]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists) spécifient les groupes d'utilisateurs qui ne recevront jamais de messages. Les administrateurs peuvent créer des listes de suppression avec des filtres de segmentation pour restreindre un groupe d'utilisateurs de la même manière que vous le feriez pour la segmentation.

### Nouveaux partenariats Braze

#### Constructeur - Contenu dynamique
[Constructor]({{site.baseurl}}/partners/message_personalization/dynamic_content/constructor) est une plateforme de recherche et de découverte de produits qui utilise l'intelligence artificielle et le machine learning pour offrir des recherches, des recommandations et des expériences de navigation personnalisées pour les sites web de ecommerce et de retailing.
 
#### Trustpilot - Contenu dynamique
[Trustpilot]({{site.baseurl}}/partners/message_personalization/dynamic_content/trustpilot) est une plateforme d'évaluation en ligne qui permet à vos clients de partager leurs commentaires et vous permet de gérer les évaluations et d'y répondre.

### Mises à jour SDK
 
Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.
 
- [Braze Android SDK 34.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3400)
    - Mise à jour de la version minimale du SDK, qui passe de 21 (Lollipop) à 25 (Nougat).

## Publication le 7 janvier 2025

### Libérer la créativité

#### Modèles de messages in-app

Nous avons ajouté des [modèles]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/) pour les messages in-app à glisser-déposer.

#### B2B Salesforce Sales Cloud Gestion des prospects

[Gérer les leads avec Salesforce Sales]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_salesforce_sales_cloud/) Cloud montre comment utiliser les webhooks de Braze pour créer et mettre à jour des leads dans Salesforce Sales Cloud via une intégration soumise par la communauté.

### Canaux robustes

#### Modèles de canvas

Nous avons ajouté des modèles Braze Canvas pour l'[inscription par e-mail avec double abonnement]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/email_signup/) et l'[onboarding avec enquête sur les préférences.]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/preference_survey/)

#### Modifications de la politique d'abonnement de WhatsApp

Meta a récemment mis à jour sa [politique d'abonnement](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Pour plus d'informations, consultez les [mises à jour des produits WhatsApp.]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/meta_resources/)

#### Outil de largeur pour les blocs de contenu dans l'éditeur par glisser-déposer de l'e-mail

Vous pouvez [ajuster la largeur]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/#using-the-editor-to-add-a-content-block) de votre bloc de contenu dans l'éditeur par glisser-déposer de l'e-mail. La largeur par défaut est de 100 %.

### Flexibilité des données

#### Filtre de segmentation provisoire d'envoi

Segmentez vos utilisateurs en fonction du nombre d'échecs provisoires d'envoi X fois en Y jours. Pour plus d'informations, reportez-vous au [glossaire des filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced).

#### Aperçu des utilisateurs anonymes

[Utilisateurs anonymes]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/) donne un aperçu des utilisateurs anonymes et des alias d'utilisateurs, en soulignant leur importance et la manière dont ils peuvent être exploités dans vos messages.

#### Composition du groupe de contrôle global

Vous pouvez [consulter l'appartenance à un groupe de contrôle global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#view-whether-a-user-is-in-a-global-control-group) en accédant à l'onglet **Engagement** du profil d'un utilisateur et en faisant défiler la page jusqu'à la section **Divers.** 

### Nouveaux partenariats Braze

#### Justuno - Capture de prospects

[Justuno]({{site.baseurl}}/partners/data_and_infrastructure_agility/leads_capture/justuno/) vous permet de créer des expériences visiteurs entièrement optimisées pour toutes vos audiences avec des segments dynamiques, offrant le ciblage le plus avancé disponible - le tout sans impacter la vitesse du site ou augmenter le travail de développement.

#### Odicci - plateforme de données client

Intégrez Braze à [Odicci]({{site.baseurl}}/partners/message_personalization/dynamic_content/odicci/), une plateforme qui donne aux entreprises les moyens d'acquérir, d'engager et de fidéliser leurs clients grâce à des expériences omnicanales axées sur la fidélisation.

#### Optimizely - Test A/B

L'intégration entre Braze et [Optimizely]({{site.baseurl}}/partners/data_and_infrastructure_agility/ab_testing/optimizely/) est une intégration bidirectionnelle qui vous permet de :

- Synchronisez chaque nuit vos segments et événements personnalisés de Braze vers Optimizely Data Platform (ODP) afin d'enrichir les profils, rapports et segmentations des clients d'Optimizely.
- Envoyez les événements de Braze Currents depuis Braze vers l'outil de reporting d'Optimizely.
- Synchronisez les données et événements personnalisés de l'ODP vers Braze pour enrichir vos données clients et déclencher l'envoi de messages Braze en fonction des événements clients dans l'ODP.

## 10 décembre 2024 libération

### Emplacement/localisation des utilisateurs du SDK par adresse IP

À partir du 26 novembre 2024, Braze détectera les emplacements/localisations des utilisateurs à partir du pays géolocalisé en utilisant l'adresse IP du début de la première session SDK. Braze utilisera l'adresse IP pour définir la valeur du pays sur les profils utilisateurs créés via le SDK, et ce paramètre de pays basé sur l'IP sera disponible pendant et après la première session. Pour plus d'informations, reportez-vous à la section [Emplacement/localisation]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/location_tracking/).

### Cadre d'accès surélevé

L['accès élevé]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#elevated-access) ajoute une couche de sécurité supplémentaire pour les actions sensibles dans votre tableau de bord de Braze. Lorsqu'il est actif, l'utilisateur doit revérifier son compte avant d'exporter un segment ou de consulter une clé API. Pour utiliser l'accès élevé, accédez à **Paramètres** > **Paramètres d'administration** > **Paramètres de sécurité** et basculez sur cette option.

### Autorisation de consulter des informations personnelles identifiables (IPI)

Pour les administrateurs, vous pouvez [autoriser les utilisateurs à afficher les IIP]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) définies par votre entreprise dans le tableau de bord, dans des aperçus de messages qui utilisent des variables Liquid pour accéder aux propriétés de l'utilisateur. 

Pour les espaces de travail, vous pouvez autoriser les utilisateurs à afficher les IIP définies par votre entreprise dans le tableau de bord, ou afficher les profils utilisateurs mais expurger les champs que votre entreprise a identifiés comme étant des IIP.

### Flexibilité des données

#### Schémas de lac de données

Les schémas suivants ont été ajoutés aux schémas des tables brutes :
- `USERS_CANVASSTEP_PROGRESSION_SHARED` : Événements de progression d'un utilisateur dans un canvas
- `CHANGELOGS_GLOBALCONTROLGROUP_SHARED` : Identifier les numéros de compartiment aléatoires présents dans le groupe de contrôle global actuel et dans le précédent.
- `USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED` : Événements d'impression lorsqu'un utilisateur consulte un indicateur de fonctionnalité

#### Segmentation basée sur les comptes

Vous pouvez effectuer une [segmentation interentreprises (B2B) basée sur les comptes de]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/account_based_segmentation/) deux manières, en fonction de la façon dont vous avez configuré votre modèle de données B2B :

- Lorsque vous utilisez des catalogues pour vos objets de gestion
- Lorsque vous utilisez des sources connectées pour vos objets de gestion

#### Filtres de segmentation

Reportez-vous à la section [Filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) pour obtenir la liste complète des filtres de segmentation et leur description.

##### Profil utilisateur créé à

Segmentez vos utilisateurs en fonction de la date de création de leur profil. Si un utilisateur a été ajouté par CSV ou API, ce filtre reflète la date à laquelle il a été ajouté. Si l'utilisateur n'est pas ajouté par CSV ou API et que sa première session est suivie par le SDK, ce filtre reflète la date de cette première session.

##### Envoi du numéro de téléphone

Segmentez vos utilisateurs en fonction du champ du numéro de téléphone e.164. Vous pouvez utiliser des expressions régulières avec ce filtre pour segmenter les numéros de téléphone avec un code pays spécifique.

### Nouveaux partenariats Braze

#### Narvar - Commerce électronique

L'intégration de Braze et [Narvar](https://corp.narvar.com/) permet aux marques d'exploiter les événements de notification de Narvar pour déclencher des messages directement depuis Braze, en tenant les clients informés grâce à des mises à jour opportunes.

#### Zeotap pour Currents - plateforme de données client

L'intégration de Braze et [Zeotap](https://zeotap.com/) vous permet d'étendre l'échelle et la portée de vos campagnes en synchronisant les segments de clients de Zeotap avec les profils d'utilisateurs de Braze. Avec [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), vous pouvez également connecter les données à Zeotap pour les rendre exploitables dans l'ensemble des outils de croissance.

#### Notify - Contenu dynamique

L'intégration de Braze et [Notify](https://notifyai.io/) permet aux marketeurs de stimuler efficacement l'engagement sur différentes plateformes. Au lieu de s'appuyer sur les méthodes de marketing traditionnelles, une campagne déclenchée par l'API de Braze peut exploiter les capacités de Notify pour diffuser des messages personnalisés par le biais de plusieurs canaux, notamment les e-mails, les SMS, les notifications push et bien plus encore.

#### Contentful - Contenu dynamique

L'intégration entre Braze et [Contentful](https://www.contentful.com/) vous permet d'utiliser dynamiquement le contenu connecté pour tirer du contenu de Contentful dans vos campagnes Braze.

#### Dépassement - Capture de prospects 

L'intégration de Braze et [Outgrow](https://outgrow.co/) vous permet de transférer automatiquement les données des utilisateurs d'Outgrow vers Braze, ce qui permet de réaliser des campagnes hautement personnalisées et ciblées.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Web 5.6.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 12.0.0](https://github.com/braze-inc/braze-flutter-sdk/releases/tag/12.0.0)
    - Mise à jour du pont natif iOS [du SDK Swift de Braze 10.3.1 vers 11.3.0.](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.1...11.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Mise à jour du pont natif Android de Braze [Android SDK 32.1.0 à 33.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v33.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [SDK Swift 11.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/11.0.1/CHANGELOG.md)

## Libération le 12 novembre 2024
 
### Flexibilité des données
 
#### Limite de vitesse pour `/users/track`

La limite de vitesse pour l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) a été mise à jour à 3 000 par 3 secondes.
 
### Libérer la créativité

#### Cas d'utilisation de Canvas

Nous avons rassemblé quelques cas d'utilisation illustrant les différentes façons dont vous pouvez tirer parti d'un Braze Canvas. Si vous êtes en quête d'inspiration, choisissez un cas d'utilisation ci-dessous pour commencer.

- [Panier abandonné]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/abandoned_cart/)
- [En stock]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/back_in_stock/)
- [Fonctionnalité Adoption]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/feature_adoption/)
- [Utilisateur déchu]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/lapsed_user/)
- [Onboarding]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/onboarding/)
- [Rétroaction après l'achat]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/post_purchase_feedback/)

### Canaux robustes

#### LINE

{% multi_lang_include release_type.md release="Disponibilité générale" %}

L'intégration de LINE dans Braze est désormais disponible ! LINE est l'application de messages la plus populaire au Japon, avec plus de 95 millions d'utilisateurs actifs par mois. En plus de la messagerie, LINE offre à ses utilisateurs une plateforme « tout-en-un » pour les réseaux sociaux, les jeux, les achats et les paiements.

Pour commencer, consultez notre [documentation LINE.]({{site.baseurl}}/user_guide/message_building_by_channel/line/)
 
#### Synchronisation de l'audience LinkedIn

{% multi_lang_include release_type.md release="Beta" %}

Vous pouvez désormais utiliser LinkedIn avec Braze [Audience Sync]({{site.baseurl}}/partners/canvas_steps/), un outil qui vous aide à étendre la portée de vos campagnes à de nombreuses technologies sociales et publicitaires de premier plan. Pour participer à la version bêta, contactez votre gestionnaire de succès Braze.
 
### Améliorer le guide du développeur
 
Nous sommes en train d'apporter des améliorations majeures au [guide du développeur de Braze]({{site.baseurl}}/developer_guide/home/). Dans un premier temps, nous avons simplifié la navigation et réduit le nombre de sections imbriquées. 

|Avant|Après|
|------|-----|
|!["L'ancienne navigation pour le guide du développeur de Braze."]({% image_buster /assets/img/release_notes/developer_guide_improvements/old_navigation.png %})|!["La nouvelle navigation pour le guide du développeur de Braze"]({% image_buster /assets/img/release_notes/developer_guide_improvements/new_navigation.png %})|

### Nouveaux partenariats Braze
 
#### MyPostcard

[MyPostcard](https://www.mypostcard.com/), une application mondiale de cartes postales de premier plan, vous permet d'exécuter des campagnes de publipostage en toute simplicité, offrant un moyen fluide et rentable d'entrer en contact avec vos clients. Pour commencer, consultez la section [Intégration de MyPostcard à Braze]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/mypostcard/).
 
### Mises à jour SDK
 
Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.
 
- [Expo Plugin 3.0.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
    - Cette version nécessite la version 13.1.0 du SDK React native de Braze.
    - Remplace l'appel à la méthode BrazeAppDelegate iOS de BrazeReactUtils.populateInitialUrl par BrazeReactUtils.populateInitialPayload.
        - Cette mise à jour résout un problème où les événements push ouverts ne se déclenchaient pas lors d'un clic sur une notification alors que l'application est dans un état terminé.
        - Pour tirer pleinement parti de cette mise à jour, remplacez tous les appels de Braze.getInitialURL par Braze.getInitialPushPayload dans votre code JavaScript. L'URL initiale est désormais accessible via la propriété url de la charge utile initiale du push.
- [Braze Segmentation Swift Plugin 5.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
    - Met à jour les bindings du SDK Swift de Braze afin qu'ils requièrent les versions 11.1.1+ SemVer.
    - Cela permet d'assurer la compatibilité avec toutes les versions du SDK de Braze, de la 11.1.1 à la 12.0.0 incluse.
    - Consultez le journal des modifications de la version 11.1.1 pour plus d'informations sur les ruptures potentielles.

## Libération le 15 octobre 2024

### Flexibilité des données

#### Campagnes et canvas

Lors de la création de campagnes et de canevas, vous pouvez calculer le nombre exact d'utilisateurs atteignables dans votre audience cible au lieu de l'estimation par défaut en sélectionnant [Calculer les statistiques exactes.]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#statistics-for-segment-size)

#### Objets de l'API Android

Le [paramètre`android_priority` ]({{site.baseurl}}/api/objects_filters/messaging/android_object/#additional-parameter-details) accepte les valeurs "normal" ou "élevé" pour spécifier la priorité de l'expéditeur FCM. Par défaut, les messages de notification sont envoyés avec une priorité élevée et les messages de données avec une priorité normale.

Pour plus d'informations sur l'impact des différentes valeurs sur la réception/distribution, voir [Priorité des messages Android](https://firebase.google.com/docs/cloud-messaging/android/message-priority/).

#### SDK

Utilisez [le débogueur intégré au SDK de Braze]({{site.baseurl}}/developer_guide/debugging/) pour résoudre les problèmes de vos canaux alimentés par le SDK sans avoir à activer la journalisation verbeuse dans votre application.

#### Activités en direct

Nous avons mis à jour la [foire aux questions]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/faq/) sur les activités en ligne/instantanées de Swift avec quelques nouvelles questions et réponses.

#### Événements personnalisés

Les [objets de propriété d'événement]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) qui contiennent des valeurs de tableau ou d'objet peuvent désormais avoir une charge utile de propriété d'événement pouvant aller jusqu'à 100 Ko.

#### Numéros de compartiment aléatoire

Utilisez la [réinscription aléatoire de l'audience avec des numéros de compartiment aléatoire]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/#random-audience-re-entry-using-random-bucket-numbers) pour les tests A/B ou le ciblage de groupes d'utilisateurs spécifiques dans vos campagnes.

#### Extensions de segments

Vous pouvez [actualiser les extensions de segments selon une planification récurrente]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#setting-up-a-recurring-refresh) en sélectionnant la fréquence à laquelle les extensions seront actualisées (quotidienne, hebdomadaire ou mensuelle) et l'heure spécifique à laquelle l'actualisation aura lieu.

### Canaux robustes

#### SMS

Nous avons ajouté [Ajouter des paramètres U]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#using-link-shortening) TM pour montrer comment vous pouvez utiliser des paramètres UTM dans un message SMS, afin que vous puissiez suivre les performances des campagnes dans des outils d'analyse/analytique tiers, tels que Google Analytics.

#### Landing pages

[Connectez votre propre domaine]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/customizing_urls/) à votre espace de travail Braze pour personnaliser les URL de vos pages de destination avec votre marque.

#### LINE et Braze

{% multi_lang_include release_type.md release="Beta" %}

Nous avons ajouté une nouvelle documentation :

- [Types de messages LINE]({{site.baseurl}}/line/create/message_types/) couvre les types de messages LINE que vous pouvez composer, y compris les aspects et les limitations, et fait partie de la collection LINE beta.
- Le [lien avec le compte utilisateur]({{site.baseurl}}/line/line_setup/#user-account-linking) permet aux utilisateurs de relier leur compte LINE au compte utilisateur de votre application. Vous pouvez ensuite utiliser Liquid dans Braze, comme {% raw %}`{{line_id}}`{% endraw %}, pour créer une URL personnalisée pour l'utilisateur qui transmet son LINE ID à votre site Web ou à votre application, qui peut alors être associée à un utilisateur connu.

#### WhatsApp et Braze

Les [comptes WhatsApp Business (WABA)]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-2-whatsapp-setup) peuvent désormais être partagés avec plusieurs fournisseurs de solutions professionnelles.

### Nouveaux partenariats Braze

#### Future Anthem - Contenu dynamique

Le partenariat entre Braze et [Future Anthem]({{site.baseurl}}/partners/message_personalization/dynamic_content/future_anthem/) s'appuie sur l'intelligence artificielle Amplifier pour offrir une personnalisation du contenu, des expériences en temps réel et des audiences dynamiques. L'intelligence artificielle Amplifier fonctionne dans les sports, les casinos et les loteries, vous permettant d'améliorer les profils de joueurs de Braze avec des attributs de joueurs spécifiques à l'industrie, tels qu'un jeu favori, un score d'engagement, le prochain pari attendu, et plus encore.

### Paramètres

#### Cryptage au niveau du champ d'identification

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Grâce au [chiffrement au niveau du champ d'identification]({{site.baseurl}}/user_guide/analytics/field_level_encryption/), vous pouvez chiffrer de façon fluide/sans heurts les adresses e-mail avec AWS Key Management Service (KMS) afin de minimiser les informations personnelles identifiables (PII) partagées dans Braze. Le chiffrement remplace les données sensibles par du texte chiffré, c'est-à-dire des informations cryptées et non lisibles.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Swift 10.3.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [SDK Swift 11.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
    - Ajout de la prise en charge de la [vérification stricte de la concurrence dans Swift 6](https://developer.apple.com/documentation/swift/adoptingswift6)
        - Les classes et types de données publics pertinents de Braze sont désormais conformes au protocole `Sendable` et peuvent être utilisés en toute sécurité dans tous les contextes de concurrence.
        - Les API réservées aux threads principaux sont désormais marquées par l'attribut `@MainActor`.
        - Nous vous recommandons d'utiliser Xcode 16.0 ou une version ultérieure pour profiter de ces fonctionnalités tout en minimisant le nombre d'avertissements générés par le compilateur. Les versions précédentes de Xcode peuvent toujours être utilisées, mais certaines fonctionnalités peuvent générer des avertissements.
    - Lors de l'intégration manuelle de la prise en charge des notifications push, il se peut que vous deviez mettre à jour la conformité `UNUserNotificationCenterDelegate` pour utiliser l'attribut `@preconcurrency` afin d'éviter les avertissements.
        - L'application de l'attribut `@preconcurrency` sur la conformité du protocole n'est disponible que dans Xcode 16.0 ou une version ultérieure. Consultez notre exemple de code d'intégration [ici.](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/PushNotifications-Manual)
- [React Native SDK 13.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1300)
    - Mise à jour des liens de la version native d'Android du [SDK Android de Braze 31.1.0 à 32.1.0.](https://github.com/braze-inc/braze-android-sdk/compare/v31.1.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Met à jour les liaisons de la version native d'iOS du [SDK Swift de Braze 10.3.0 vers 11.0.0.](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.0...11.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [Flutter SDK 11.1.0](https://pub.dev/packages/braze_plugin/changelog#1110)
- [SDK Swift 11.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [SDK Android 33.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3300)
    - Mise à jour de Kotlin de 1.8 à Kotlin 2.0.
- [SDK Web 5.5.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#550)

## Libération le 17 septembre 2024

### Flexibilité des données

#### Braze Cloud Data Ingestion pour S3

Vous pouvez utiliser [Cloud Data Ingestion (CDI) for S3]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/file_storage_integrations/#aws-definitions) pour intégrer directement un ou plusieurs compartiments S3 de votre compte AWS à Braze. Lorsque de nouveaux fichiers sont publiés sur S3, un message est envoyé à SQS et Braze Cloud Data Ingestion prend en charge ces nouveaux fichiers.

#### Utilisateurs actifs par mois CY 24-25

Pour les clients qui ont acheté Utilisateurs actifs par mois - CY 24-25, Braze gère différentes limites de débit sur son endpoint `/users/track`. Pour plus de détails, reportez-vous à [POST : Suivre les utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25). 

### Libérer la créativité

#### Modélisation de produits de catalogue comprenant des étiquettes Liquid

{% multi_lang_include release_type.md release="Accès anticipé" %}

Utilisez l'indicateur `:rerender` dans une balise Liquid pour [afficher le contenu Liquid d'un article de catalogue]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#using-liquid). Par exemple, si vous rendez le contenu Liquid suivant :

{% raw %}
```liquid
Hi ${first_name}
{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

L'affichage est le suivant :

{% raw %}
```
Hi Peter,
Welcome to our store, Peter!
```
{% endraw %}

### Canaux robustes

#### Messages de réponse WhatsApp

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Vous pouvez utiliser les [messages de réponse]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) pour répondre aux messages WhatsApp entrants de vos utilisateurs. Ces messages sont créés in-app sur Braze pendant votre expérience sur la composition et peuvent être modifiés à tout moment. Vous pouvez utiliser Liquid pour faire correspondre la langue du message de réponse aux utilisateurs appropriés.

#### Modèles de canvas

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Créez des [modèles de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/) pour affiner votre envoi de messages en créant un cadre cohérent qui peut être facilement personnalisé pour s'adapter à vos objectifs spécifiques sur l'ensemble de vos Canvas.

#### Landing pages

{% multi_lang_include release_type.md release="Beta" %}

Les [pages d'atterrissage de Braze]({{site.baseurl}}/user_guide/engagement_tools/landing_pages) sont des pages web autonomes qui peuvent piloter votre stratégie d'acquisition et d'engagement des utilisateurs.

#### Changements depuis la dernière consultation

Vous pouvez consulter le nombre de mises à jour de vos [Teams]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/#changes-since-last-viewed), campagnes et [segments]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#changes-since-last-viewed) par d'autres membres de votre équipe en vous référant à l'indicateur *Changements depuis le dernier affichage* sur les pages d'aperçu respectives (comme la page d'aperçu d'une [campagne d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#changes-since-last-viewed)). 

#### Résolution des problèmes liés aux demandes de webhook et de contenu connecté 

[Cet article]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors) explique comment résoudre les codes d'erreur de webhook et de contenu connecté, notamment la nature des erreurs et les étapes pour les résoudre.

### Nouveaux partenariats Braze

#### Boîte de réception Monster - Analyse/analytique (si utilisé comme adjectif)

[Inbox Monster]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/inbox_monster/) est une plateforme de signaux de boîte de réception qui aide les marques d'entreprise à faire atterrir chaque envoi. Il s'agit d'une suite intégrée de solutions pour la livrabilité, le rendu créatif et le contrôle des SMS, qui permet aux équipes modernes de gestion de la relation client (CRM) d'être plus efficaces et de mettre fin aux angoisses liées à l'envoi de messages.

#### SessionM - Loyauté

[SessionM]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/sessionm/) est une plateforme d'engagement et de fidélisation des clients qui offre des fonctionnalités de gestion de campagne et des solutions de gestion de la fidélisation pour aider les marketeurs à mener un ciblage de proximité afin d'augmenter l'engagement et le bénéfice.

### L'intelligence artificielle et l'automatisation de l’apprentissage machine.

#### Recommandations d'articles à la mode

Outre le modèle "AI Personalized", la fonctionnalité de [recommandations d'articles par l'intelligence artificielle]({{site.baseurl}}/user_guide/sage_ai/recommendations/about_item_recommendations/#trending) comprend également un modèle de recommandation pour "Trending", qui présente les articles qui ont eu l'élan le plus positif en ce qui concerne les interactions récentes avec les utilisateurs.

### Paramètres

#### Rôles

{% multi_lang_include release_type.md release="Disponibilité générale" %}

[Les rôles]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) permettent une meilleure structuration en regroupant vos autorisations personnalisées individuelles avec les contrôles d'accès à l'espace de travail. Ceci est particulièrement utile si vous avez plusieurs marques ou espaces de travail régionaux dans un seul tableau de bord. Grâce aux rôles, vous pouvez ajouter les utilisateurs du tableau de bord aux bons espaces de travail et leur accorder directement les autorisations associées. 

#### Rapport sur les événements de sécurité

Nous avons ajouté une liste complète des [événements de sécurité]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#downloading-a-security-event-report) qui peuvent apparaître dans votre rapport de sécurité téléchargé.

#### Rapport sur l'utilisation des messages

{% multi_lang_include release_type.md release="Accès anticipé" %}

Le [tableau de bord de l'utilisation des messages]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/message_usage/) fournit en libre-service des informations sur votre utilisation des crédits SMS et WhatsApp pour une vue d'ensemble de l'utilisation historique et actuelle par rapport aux attributions contractuelles. Ces informations peuvent réduire votre confusion et vous aider à faire des ajustements pour prévenir les risques de dépassement.

### SDK

#### Initialisation retardée pour le SDK Braze Swift

Configurez l'[initialisation différée]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=swift) pour initialiser votre SDK Braze Swift de manière asynchrone tout en veillant à ce que la gestion des notifications push soit préservée. Cela peut être utile lorsque vous devez configurer d'autres services avant d'initialiser le SDK, par exemple pour récupérer des données de configuration sur un serveur ou attendre le consentement de l'utilisateur.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Android 32.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3210)
- [Segment Kotlin SDK 2.0.0](https://github.com/braze-inc/braze-segment-kotlin/blob/main/CHANGELOG.md#200)
- [SDK Swift 10.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1010)
- [React Native SDK 12.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1210)
- [Cordova SDK 10.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1000)
    - Cette version nécessite désormais Cordova Android 13.0.0.
    - Reportez-vous à l'[annonce de la version de Cordova](https://cordova.apache.org/announcements/2024/05/23/cordova-android-13.0.0.html) pour une liste complète des exigences en matière de dépendances du projet.- Mise à jour du pont Android natif de Braze [Android SDK 30.3.0 à 32.1.0.](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Mise à jour du pont natif iOS [du SDK Swift de Braze 9.2.0 vers 10.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.2.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [SDK Swift 10.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1020)
- [Unity 7.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#700)
    - Mise à jour du pont natif Android [du SDK Android de Braze 30.3.0 vers 32.1.0.](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Mise à jour du pont natif iOS [du SDK Swift de Braze 9.0.0 vers 10.1.0.](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [Braze Segmentation Swift Plugin 4.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#400)
    - Met à jour les bindings du SDK Swift de Braze pour exiger les versions de la dénomination `10.2.0+` SemVer.
        - Cela permet la compatibilité avec n'importe quelle version du SDK de Braze, de `10.2.0` jusqu'à, mais sans inclure, `11.0.0`.
        - Reportez-vous au journal des modifications de [`10.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1000) pour plus d'informations sur les ruptures potentielles.
- [Flutter SDK 11.0.0](https://pub.dev/packages/braze_plugin/changelog#1100)
    - Mise à jour du pont natif Android [du SDK Android de Braze 30.4.0 vers 32.1.0.](https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
        - Modifie le comportement de `wipeData()` sur Android pour conserver les abonnements externes (comme `subscribeToContentCards()`) après avoir été appelé.
    - Met à jour le pont natif iOS [du SDK Swift de Braze 9.0.0 vers 10.2.0.](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [SDK Swift 10.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1030)
- [Unity 7.1.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#710)
- [React Native SDK 12.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1220)
