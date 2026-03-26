---
nav_title: Aperçu de Shopify
article_title: "Aperçu de Shopify"
description: "Cet article de référence décrit le partenariat entre Braze et Shopify, une entreprise de commerce mondiale qui vous permet de connecter de façon fluide votre boutique Shopify à Braze pour transmettre certains webhooks Shopify dans Braze. Exploitez les stratégies cross-canal de Braze et Canvas pour inciter les clients à finaliser leurs achats ou recibler les utilisateurs en fonction de leurs achats précédents."
page_type: partner
search_tag: Partner
alias: /shopify_overview/
page_order: 0
---

# Aperçu de Shopify

> [Shopify](https://www.shopify.com/) est un leader mondial du commerce qui fournit des outils de confiance pour démarrer, développer, commercialiser et gérer une entreprise de toute taille. Shopify améliore le commerce pour tout le monde grâce à une plateforme et des services conçus pour la fiabilité, tout en offrant une meilleure expérience d'achat aux consommateurs partout dans le monde.

L'intégration de Braze à Shopify constitue une solution puissante pour les entreprises de commerce électronique qui cherchent à améliorer l'engagement de leurs clients et à mener des actions marketing personnalisées. Cette intégration connecte de façon fluide les fonctionnalités eCommerce robustes de Shopify avec notre plateforme avancée d'engagement client, ce qui vous permet d'envoyer des messages ciblés, pertinents et opportuns à vos utilisateurs en fonction de leurs comportements d'achat en temps réel et des données transactionnelles.

## Conditions

| Exigence | Description |
| --- | --- |
| Boutique Shopify | Vous avez une boutique Shopify active. |
| Autorisations pour le propriétaire ou l'employé de la boutique Shopify | {::nomarkdown}<ul><li>Accès à tous les paramètres généraux et de la boutique en ligne.</li><li> Autorisations administratives supplémentaires :</li><ul><li>Commandes : Afficher</li><li>Client : Lecture-écriture</li><li>Voir les événements client (pixels Web)</li><li>Gérer les paramètres</li><li>Voir les applications développées par le personnel/collaborateurs</li><li>Gérer/installer des applications et des canaux</li><li>Gérer/Ajouter des pixels personnalisés</li></ul></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Comment intégrer 

Braze propose aux marchands Shopify deux options d'intégration conçues pour répondre aux divers besoins des entreprises de commerce électronique : **Intégration standard** et **Intégration personnalisée**.

{% multi_lang_include shopify.md section='Integration Tabs' %}

## Comment fonctionne l'intégration

Si vous avez déjà configuré et activé le remplissage historique dans vos paramètres de configuration, la synchronisation initiale des données commencera immédiatement. Braze importera tous les clients et les événements de commandes passées au cours des 90 derniers jours précédant votre connexion à l'intégration Shopify. Lorsque Braze importe vos clients Shopify, nous leur attribuons le type d'`external_id` que vous avez choisi dans vos paramètres de configuration.

Si vous prévoyez d'intégrer un ID externe personnalisé (pour l'[intégration standard]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/#step-4-configure-how-you-manage-users) ou l'[intégration personnalisée]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/#step-6-configure-how-you-manage-users-optional)), vous devrez ajouter votre ID externe personnalisé en tant que méta-champ client Shopify à tous les profils clients Shopify existants, puis effectuer le [remplissage historique]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill). 

Après la synchronisation initiale des données, Braze suivra en permanence les nouvelles données et les mises à jour, directement depuis Shopify et les SDK de Braze.

{% alert note %}
Si vous êtes un client existant de Braze avec des campagnes ou des Canvas actifs, consultez le [remplissage historique de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill) pour obtenir des informations importantes. Pour savoir quelles données clients spécifiques sont renseignées, reportez-vous aux [fonctionnalités de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/).
{% endalert %}

### Synchronisation des utilisateurs et des données

Une fois l'intégration en production, Braze recueillera les données des utilisateurs à partir de deux sources clés grâce à l'intégration Shopify :
- **API du pixel Web Shopify et applications intégrées :** Cela alimente le SDK Web et le SDK Javascript de Braze pour prendre en charge le suivi sur site, la gestion des identités, les données comportementales eCommerce et alimenter les canaux de communication comme les messages in-app.
- **Webhooks Shopify :** données comportementales eCommerce, synchronisation des produits et collecte des abonnés

Lors de l'onboarding de l'intégration, vous devrez sélectionner le moment où les SDK de Braze s'initialisent et chargent votre site Shopify : 
- Lors de la visite du site (comme le début de la session)
    - **Ce que cela fait :** Suit les utilisateurs anonymes — tels que les acheteurs invités — afin d'accéder à davantage de données pour une personnalisation plus poussée 
- Lors de l'inscription à un compte (comme la connexion au compte) 
    - **Ce que cela fait :** Empêche le suivi des utilisateurs anonymes pour une approche plus conservatrice et axée sur la protection de la vie privée, de sorte que l'activité de l'utilisateur est suivie *après que* celui-ci s'est connecté à son compte

{% alert note %}
- Les visites du site web (sessions) comptent dans vos allocations d'utilisateurs actifs par mois (MAU).
- Les versions du SDK Web et du SDK JavaScript de Braze seront automatiquement définies sur v5.4.0.
{% endalert %}

Braze utilise l'intégration Shopify pour prendre en charge plusieurs identifiants qui suivent vos utilisateurs depuis leur expérience d'achat en tant qu'invité jusqu'à ce qu'ils deviennent des utilisateurs identifiés :

| Identifiant Braze | Description |
| --- | --- |
| `device_id` Braze | Un ID généré de manière aléatoire et stocké dans le navigateur qui permet de suivre l'activité des utilisateurs anonymes par le biais des SDK de Braze. |
| Alias d'utilisateur du jeton de panier | Un alias que Braze crée pour suivre les événements de mise à jour du panier. Ce jeton est créé à l'aide du jeton de panier Shopify. |
| Alias d'utilisateur du jeton de paiement | Un alias que Braze crée lorsque l'utilisateur lance le processus de paiement. Ce jeton est créé en utilisant le jeton de paiement Shopify.<br><br> Si un client utilise Shop Pay comme option de paiement accéléré, Shopify peut contourner certains événements de paiement standard et empêcher Braze de recevoir les données nécessaires pour ajouter l'alias du jeton de paiement. |
| Alias de l'ID client Shopify | L'ID client Shopify est attribué en tant qu'alias lorsque l'ID externe est attribué lors de la connexion au compte ou lorsqu'une commande est passée. |
| `external_id` Braze | Un identifiant unique qui permet de suivre les clients à travers les appareils et les plateformes. Cela permet de maintenir une expérience utilisateur cohérente et d'améliorer l'analytique en empêchant la création de profils multiples lorsque les utilisateurs changent d'appareil ou réinstallent l'application.<br><br>L'intégration Shopify prend en charge les types d'`external_id` suivants : <br><br>{::nomarkdown}<ul><li>ID client Shopify (par défaut)</li><li>ID externe personnalisé</li><li>E-mail haché (SHA-256)</li><li>E-mail haché (SHA-1)</li><li>E-mail haché (MD5)</li><li>E-mail</li></ul>{:/}Braze attribue un `external_id` à vos utilisateurs en appelant la méthode changeUser dans les SDK lorsque : <br><br>{::nomarkdown}<ul><li>Un utilisateur se connecte ou crée un compte</li><li>Une commande est passée</li></ul>{:/}<br> Pour plus d'informations sur ce qui se passe lorsque vous affectez un `external_id` à un profil anonyme, reportez-vous au [Cycle de vie du profil utilisateur]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users).<br><br>Braze s'appuiera également sur l'`external_id` pour attribuer en aval les données comportementales eCommerce provenant des webhooks Shopify.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

L'intégration nécessite que les SDK de Braze et les services Shopify travaillent ensemble pour suivre et attribuer de manière appropriée les données Shopify aux bons utilisateurs en quasi-temps réel. Pour plus de détails sur les données suivies grâce à l'intégration, consultez les [données Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/).

{% alert note %}
- Si vous testez l'intégration, nous vous conseillons d'utiliser le mode incognito ou d'effacer vos cookies pour réinitialiser le `device_id` de Braze et simuler le comportement d'un utilisateur anonyme.
- Même si un ID client Shopify est généré lorsqu'un e-mail est saisi dans le pied de page de la newsletter Shopify ou lors du processus de paiement avant qu'une commande ne soit passée, cet ID client n'est pas accessible via les pixels Web Shopify. Pour cette raison, Braze ne peut pas utiliser la méthode `changeUser` dans ces deux situations.
{% endalert %}

### Synchronisation des abonnements marketing par e-mail et par SMS de Shopify

Si vous activez la collecte d'abonnés dans vos paramètres de configuration, vous devez attribuer un groupe d'abonnement pour chaque boutique que vous connectez à Braze. Vos clients seront ainsi catégorisés comme « abonnés » ou « désabonnés » au groupe d'abonnement de votre boutique.

Le statut d'abonnement marketing Shopify pour le marketing par e-mail et par SMS peut être mis à jour de la manière suivante :
- **Mise à jour manuelle :** Vous pouvez modifier manuellement le statut d'abonnement au marketing par e-mail ou par SMS d'un utilisateur dans votre administration Shopify.
- **Pied de page de la newsletter Shopify :** Si un utilisateur saisit son e-mail dans le pied de page de la newsletter par défaut de Shopify, son statut d'abonnement sera mis à jour.
- **Processus de paiement :** Si un utilisateur met à jour son statut d'abonnement lors de la validation de sa commande.

{% alert note %}
Le statut d'abonnement au marketing par e-mail de Shopify ne modifiera pas l'[état de l'abonnement global à l'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) d'un utilisateur dans Braze. L'état de l'abonnement par défaut lors de la création d'un profil utilisateur est « abonné ». N'oubliez pas d'utiliser le groupe d'abonnement dans les critères d'entrée de votre campagne ou de votre Canvas.
{% endalert %}

Ce tableau montre quels états d'abonnement marketing Shopify correspondent aux statuts au sein de votre groupe d'abonnement Braze. 

| État d'abonnement marketing Shopify | État du groupe d'abonnement Braze |
| --- | --- |
| E-mail abonné | Abonné |
| E-mail désabonné | Désabonné |
| E-mail en attente de confirmation | Désabonné |
| E-mail non valide | Désabonné |
| SMS abonné | Abonné |
| SMS désabonné | Désabonné |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Formulaires d'inscription

#### Pied de page de la newsletter Shopify

Les utilisateurs qui saisissent leur adresse e-mail dans le pied de page de la newsletter Shopify suivront l'un de ces parcours :

##### Utilisateurs qui ne se sont pas connectés à leur compte

1. Braze reçoit un webhook Shopify entrant chaque fois qu'un client est créé ou mis à jour.
2. Braze crée un profil utilisateur contenant l'adresse e-mail et l'alias d'ID client Shopify associés à cet utilisateur.
3. Le SDK de Braze met à jour le profil anonyme avec l'adresse e-mail.

{% alert note %}
Il peut en résulter un profil en double jusqu'à ce que l'utilisateur s'identifie en créant son compte, en se connectant à son compte ou en passant une commande. Braze propose des outils de fusion en bloc pour vous aider à automatiser le rapprochement des profils en double. Pour plus de détails, reportez-vous à la section [Utilisateurs en double]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/).
{% endalert %}

##### Utilisateurs qui se sont déjà connectés à leur compte

Braze créera un profil utilisateur contenant l'adresse e-mail et l'alias d'ID client Shopify associés à cet utilisateur. Braze ne mettra pas à jour l'adresse e-mail de l'utilisateur connecté, car nous supposons que Shopify a déjà fourni cette information.

#### Formulaires d'inscription Braze

Braze propose deux types de modèles de formulaires d'inscription :
- **[Formulaires d'inscription par e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/email_capture/) :** Créez-les à l'aide de l'éditeur par glisser-déposer.
- **[Formulaire de capture d'e-mail de l'éditeur traditionnel]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/) :** Un formulaire plus simple pour capturer les adresses e-mail.

Lorsque vous utilisez ces modèles de formulaire d'inscription, Braze met automatiquement à jour l'état de l'abonnement global à l'e-mail sur le profil utilisateur. Pour plus de détails sur la gestion de l'état de l'abonnement global à l'e-mail, y compris des informations sur la validation de l'e-mail, reportez-vous à la documentation de chaque type de modèle de formulaire.

{% alert note %}
- Veillez à inclure des critères d'entrée dans votre campagne ou Canvas qui incluent à la fois le statut global de l'abonnement e-mail et le groupe d'abonnement connectés à votre boutique Shopify. Cela vous permettra de cibler la bonne audience. 
- Braze recueille des informations sur les visiteurs, telles que les adresses e-mail et les numéros de téléphone, par le biais de messages dans le navigateur. Ces informations sont ensuite envoyées à l'API Visitor de Shopify, mais ne créent pas de profil client dans Shopify. Pour plus de détails, reportez-vous à l'[API Visitor](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api).
{% endalert %}

#### Formulaires d'inscription tiers 

Si vous utilisez une plateforme tierce ou un plugin Shopify pour vos formulaires d'inscription, vous devez travailler avec vos développeurs pour intégrer le code SDK de Braze afin de capturer l'adresse e-mail et le statut d'abonnement global à l'e-mail à partir des soumissions de formulaire. Pour en savoir plus, consultez la [configuration de l'intégration standard de Shopify]({{site.baseurl}}/shopify_standard_integration/) et la [configuration de l'intégration personnalisée de Shopify]({{site.baseurl}}/shopify_custom_integration/).

### Synchronisation des produits 

Braze prend en charge la synchronisation des produits de votre boutique Shopify dans un catalogue Braze. Pour plus de détails, reportez-vous à la rubrique [Synchronisation des produits Shopify]({{site.baseurl}}/shopify_catalogs/).

## Demandes des personnes concernées

Dans le cadre de l'intégration de la plateforme Braze à Shopify, Braze reçoit automatiquement les [webhooks de conformité de Shopify](https://shopify.dev/docs/apps/build/privacy-law-compliance/). Toutefois, étant donné que les clients sont les responsables du traitement des données de leurs utilisateurs finaux, ils doivent effectuer toutes les actions nécessaires pour répondre aux demandes des personnes concernées reçues au sujet des données des utilisateurs finaux dans Braze (y compris les données des utilisateurs finaux reçues via l'intégration Shopify). Pour plus de détails, veuillez consulter notre documentation sur l'[assistance technique en matière de protection des données]({{site.baseurl}}/dp-technical-assistance).