---
nav_title: "Gestion de l'identité des utilisateurs de Shopify"
article_title: "Gestion de l'identité des utilisateurs de Shopify"
description: "Cet article de référence présente la fonctionnalité de gestion des identités des utilisateurs de Shopify."
page_type: partner
search_tag: Partner
alias: "/shopify_user_identity/"
page_order: 3
---

# Gestion de l'identité des utilisateurs de Shopify

> Braze recevra des signaux de vos clients Shopify à travers leurs comportements sur site et en écoutant les webhooks de Shopify que vous avez configurés dans le cadre de votre intégration. Pour les sites Shopify non headless, Braze aidera à rapprocher les utilisateurs à partir de la page de paiement. Pour les sites Shopify headless, reportez-vous à nos conseils d'intégration sur la façon de [rapprocher les utilisateurs à partir de l’étape de paiement]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#headless-checkout).

## Saisie d'informations pour les profils utilisateurs 

### Suivi des utilisateurs de Shopify

Si les visiteurs de votre magasin sont des invités (c'est-à-dire anonymes), Braze saisira le site `device_id` pour les sessions de ces clients particuliers. Après avoir configuré la réconciliation des utilisateurs pour les formulaires Shopify lors de votre [mise en œuvre du SDK Web]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#implement-web-sdk), les e-mails des clients seront ajoutés aux profils utilisateurs anonymes chaque fois que les clients entreront leurs informations dans un formulaire. 

Lorsque les visiteurs d'un magasin saisissent leur e-mail dans une newsletter Shopify ou un formulaire de capture d'e-mail, Braze recevra un événement webhook de Shopify pour créer le profil utilisateur. Braze fusionne ensuite ce profil d'utilisateur avec le profil d'utilisateur anonyme suivi par le SDK Web et attribue l'identifiant du client Shopify comme alias d'utilisateur sur le profil d'utilisateur. 

Au fur et à mesure que les clients progressent vers le paiement et fournissent d'autres informations identifiables, comme des numéros de téléphone, Braze doit capturer les données utilisateur pertinentes à partir des webhooks de Shopify et les fusionner avec l'utilisateur anonyme à l'adresse `device_id`.
- Si vous avez mis en œuvre le SDK Web via Shopify ScriptTag, sur un site Shopify non headless, ou via Google Tag Manager, Braze veillera automatiquement à ce que les données utilisateur de la page de paiement et les données de session du profil d'utilisateur anonyme soient fusionnées au profil d'alias utilisateur avec l'identifiant client Shopify attribué.
- Si vous avez mis en œuvre le SDK Web sur un site Shopify headless, vous devez vous assurer que les données de l'utilisateur soumises dans la page de paiement sont correctement attribuées au bon profil utilisateur par le biais du SDK Web ou de l'API. Pour plus d'informations, consultez la page [Mettre en œuvre le SDK Web directement sur votre site Shopify headless]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/#headless-site).

Lorsque les clients poursuivent le processus de paiement, Braze vérifie si l'adresse e-mail, le numéro de téléphone ou l'ID client Shopify qu'ils ont saisi correspond à un profil utilisateur existant. En cas de correspondance, Braze synchronise les données de l'utilisateur de Shopify avec ce profil.

Si l'adresse e-mail ou le numéro de téléphone est associé à plusieurs profils utilisateurs identifiés, Braze synchronise les données Shopify avec le profil dont l'activité est la plus récente.

Si Braze ne trouve pas de correspondance pour l'adresse e-mail ou le numéro de téléphone, Braze crée un nouveau profil utilisateur avec les données Shopify prises en charge.

### Lorsque les clients de Shopify se synchronisent avec Braze

Braze met à jour les profils utilisateurs existants ou en crée de nouveaux pour les prospects, les inscriptions et les enregistrements de compte capturés dans votre boutique Shopify. Vous pouvez collecter des données de profil utilisateur à partir des méthodes suivantes dans Shopify et plus encore :
- Le client crée un compte
- L'adresse e-mail ou le numéro de téléphone du client est collecté dans un formulaire de capture Shopify
- L'adresse e-mail du client est collectée à partir d'un formulaire de bulletin d'information.
- L'adresse e-mail ou le numéro de téléphone du client est collecté par le biais d'un outil tiers connecté à Shopify, tel qu'EcomSend

Braze tentera d'abord de mapper les données Shopify prises en charge à tout profil utilisateur existant à l'aide de l'adresse e-mail ou du numéro de téléphone du client. 

Pour éviter de dupliquer les profils utilisateurs, il est essentiel que vous examiniez les instructions relatives à la réconciliation des utilisateurs pour Shopify Forms selon la méthode que vous avez utilisée pour [mettre en œuvre le SDK Web sur votre site Web Shopify]().

## Fusion des profils utilisateurs 

{% alert note %}
L'intégration par défaut de Shopify fournit des outils pour faciliter la fusion de votre profil d'utilisateur anonyme et du profil d'alias de Shopify. Si vous mettez en œuvre l'intégration sur un site Shopify headless, passez en revue la [mise en œuvre du SDK Web directement sur votre site Shopify headless]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/getting_started_shopify/?tab=headless%20shopify%20site#supported-features) pour confirmer que vous rapprochez correctement vos utilisateurs. <br><br> Si vous rencontrez des profils utilisateurs en double, vous pouvez utiliser notre [outil de fusion en bloc]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#bulk-merging/) pour vous aider à rationaliser vos données.
{% endalert %}

Braze fusionne les champs du profil de l'utilisateur anonyme avec ceux du profil de l'utilisateur identifié lorsque nous trouvons une correspondance avec l'un des éléments suivants :
- ID du client Shopify
- e-mail
- Numéro de téléphone

Braze fusionne les champs suivants du profil utilisateur anonyme au profil utilisateur identifié :
- Prénom
- Nom de famille
- e-mail
- Genre
- Date de naissance
- Numéro de téléphone
- Fuseau horaire
- Ville d'origine
- Pays
- Langue
- Attributs personnalisés
    - Données d'événements personnalisés et d'achats (à l'exclusion des propriétés d'événement, du décompte et des horodatages de la première et de la dernière date).
    - Propriétés d'événement personnalisé et d'achat pour la segmentation "X fois en Y jours" (où X<=50 et Y<=30)
- Jetons de notification push
- Historique des messages
- L'un des champs suivants figurant dans le profil de l'utilisateur anonyme ou dans le profil de l'utilisateur identifié, tels que l'événement personnalisé, le nombre d'événements d'achat et les horodatages de la première et de la dernière date.
    - Ces champs fusionnés mettront à jour les filtres "pour X événements dans Y jours". Pour les achats, ces filtres comprennent le "nombre d'achats en Y jours" et "l'argent dépensé dans les Y derniers jours".

{% alert important %}
Les données de session ne sont pas encore prises en charge dans le cadre du processus de fusion.
{% endalert %}

## Synchronisation des abonnés de Shopify

Au cours du processus de configuration de Shopify, Braze propose des contrôles personnalisés pour synchroniser les adresses e-mail de vos clients et les états d'abonnement par SMS avec les groupes d'abonnement et les états d'abonnement des profils utilisateurs de Braze. 

### Collecte d'abonnés par e-mail ou SMS

Lors de votre configuration de la boutique Shopify dans Braze, vous aurez la possibilité de synchroniser vos abonnés e-mail et SMS de Shopify vers Braze. 

#### Recueillir des abonnés aux e-mails

Pour activer la collecte d'abonnés aux e-mails, activez la fonctionnalité dans votre configuration Shopify. Nous vous recommandons d’attribuer au moins un [groupe d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#subscription-groups) Braze, par exemple les abonnés aux e-mails de Shopify. Braze ajoutera vos abonnés aux e-mails aux groupes d'abonnement spécifiés afin qu'ils soient inclus dans votre ciblage d'audience lorsque vous envoyez un message. 

![]({% image_buster /assets/img/Shopify/collect_email.png %})

Lorsque cette option est activée, Braze synchronise en temps réel les mises à jour de vos abonnés à l'e-mail de Shopify et les mises à jour des états de leurs abonnements à l'e-mail. Si vous n'activez pas l'option de remplacement, vos clients Shopify seront soit abonnés, soit désabonnés du groupe d'abonnement associé à votre boutique Shopify.

Si vous activez l'option d'annulation, Braze mettra à jour l'état de l'abonnement global sur le profil utilisateur. Cela signifie que si vos clients sont marqués comme désabonnés dans Shopify, Braze marquera l'état d'abonnement global comme désabonné sur le profil utilisateur et désabonnera le client de tous les groupes d'abonnement e-mail disponibles. Par conséquent, aucun message ne sera envoyé aux utilisateurs qui se sont globalement désabonnés de l'e-mail.

#### Recueillir des abonnés aux SMS

Pour collecter des abonnés SMS à partir de Shopify, vous devez créer des [groupes d'abonnement SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/) dans le cadre de votre [configuration SMS.]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup) 

Lorsque vous êtes prêt à collecter vos abonnés aux SMS Shopify, activez la collecte d'abonnés aux SMS dans la page de configuration de Shopify. Vous devez sélectionner au moins un groupe d'abonnement SMS afin de pouvoir cibler et envoyer des messages SMS de manière appropriée. 

![]({% image_buster /assets/img/Shopify/collect_sms.png %})

Lorsque cette option est activée, Braze synchronise en temps réel les mises à jour de vos abonnés SMS Shopify et l'état de leurs abonnements SMS. Si vous n'activez pas l'option de remplacement, vos clients Shopify seront soit abonnés, soit désabonnés du groupe d'abonnement associé à votre boutique Shopify.

Les abonnés SMS n'ont pas d'état d'abonnement global, vous n'avez donc pas besoin de les prendre en compte lorsque vous utilisez une option de remplacement. Un utilisateur ne peut être désabonné ou abonné qu'à un groupe d'abonnement SMS.

#### Attributs personnalisés hérités du passé

Les anciens clients de Shopify peuvent avoir l'ancienne méthode de collecte des abonnés par e-mail et SMS via les attributs personnalisés `shopify_accepts_marketing` et `shopify_sms_consent`. Si vous enregistrez les paramètres ci-dessus avec l'option Override activée, Braze supprimera les attributs personnalisés des profils utilisateurs et synchronisera ces valeurs avec leur groupe d'abonnement e-mail et leur groupe d'abonnement SMS respectifs.

Si des campagnes ou des plans d'action existants utilisent ces anciens attributs personnalisés, supprimez-les et vérifiez que les campagnes ou les plans d'action utilisent l'état ou le groupe d'abonnement approprié, ou les deux.
