---
nav_title: Juillet
page_order: 6
noindex: true
page_type: update
description: "Cet article contient les notes de version de juillet 2019."
---

# Juillet 2019

{% alert update %}
Braze a publié deux (oui, vous avez bien lu - **deux**) nouvelles versions ce mois-ci ! La dernière version est affichée en haut, la première [commence en bas de page](#earlier-this-month) !
{% endalert %}

## Authentification unique (SSO) SAML

L’[Authentification unique]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/) (SSO) offre aux entreprises une façon sécurisée et centralisée de contrôler l’accès au tableau de bord de Braze. Pour faire court, elle permet d’utiliser un seul identifiant/mot de passe pour se connecter à différentes applications, y compris Braze.

En plus de [Connexion Google à l’aide du support OAuth 2.0](https://developers.google.com/identity/protocols/OAuth2), les entreprises souhaiteraient que SSO soit compatible avec l’assistance Security Assertion Markup Language (SAML). Cela permet, en effet, de s’intégrer de manière transparente avec des fournisseurs d’identité (IdP) importants, notamment [Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/azure_ad/) et [Okaa]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/) qui prennent en charge les dernières normes de l’industrie (SAML 2.0).

Braze prend en charge :
- [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)
- [Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/azure_ad/)
- [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)

## Affichage de la clé API Événement d’Adjust

Nous avons mis à jour la page partenaire d’Adjust pour rendre cette clé API accessible aux clients.

## Nouveaux partenaires

Certains nouveaux partenaires ont rejoint notre programme Alloys et ont été ajoutés à nos Documents ! Dites bonjour à :
- [FiveTran]({{site.baseurl}}/partners/fivetran/)
- [Talon.One]({{site.baseurl}}/partners/talonone/)
- [Voucherify]({{site.baseurl}}/partners/voucherify/)

## Amélioration des détails de la campagne

Les détails supplémentaires de la campagne sont affichés dans… tenez-vous bien… la section **Campaign Details** (Détails de la campagne) de la page **Campaign** (Campagne) !

## Afficher uniquement les miennes dans Segments et Canvas

Le filtre de vérification « Only Show Mine » (Afficher uniquement les miennes) sur la page **Campaigns** (Campagnes) s’est avéré très populaire. Par conséquent, nous ajoutons également cette option aux listes Canvas et Segment !

### Comportement d’avancement

Vous pouvez maintenant choisir [quand un utilisateur avance]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) d’une Canvas Step à la suivante. Ces options comprennent « Message Sent » (Message envoyé) et « Entire Audience After Delay » (Toute l’audience après un délai).

### Messages in-app de Canvas

Les [messages in-app]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/) sont maintenant disponibles dans Canvas ! Ajoutez une Canvas Step et parcourez les canaux disponibles pour ajouter un message in-app.

# Plus tôt ce mois-ci

## Suppression de l’image du profil utilisateur

Nous avons supprimé les images de profil utilisateur affichées dans les profils utilisateur de Braze et les recherches d’utilisateurs.

## Contenu connecté dans les Cartes de contenu

Vous pouvez maintenant utiliser les strings et fonctionnalités de [Contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) dans vos [Cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/overview/).

Les appels de contenu connectés vers des serveurs externes se produisent lorsqu’une carte est réellement envoyée, et non lorsque la carte est vue par l’utilisateur. Comme pour l’e-mail, le contenu dynamique sera calculé et déterminé au moment de l’envoi, et non pas au moment où la carte est visualisée.

## Adresse « reply-to » (répondre à) nulle

Les clients peuvent désormais définir la valeur `null` de l’adresse « reply-to (répondre à) » sur la page **Email Settings (Paramètres e-mail)** dans Braze ou à l’aide de l’[API]({{site.baseurl}}/api/endpoints/messaging/#email-object-specification).  Quand cette option est utilisée, les réponses seront envoyées à l’adresse « De » indiquée.  Vous pouvez maintenant personnaliser le champ d’adresse « De » en tant que `dan@emailaddress.com`, et vos clients auront la possibilité de répondre directement à Dan.

Pour définir une valeur `null` pour l’adresse « reply-to » (répondre à) de l’e-mail dans Braze, allez sur **Manage Settings (Gérer les paramètres)**, puis sur l’onglet **Email Settings (Paramètres de messagerie)**. Faites défiler jusqu’à la section **Outbound Email Settings (Paramètres d’e-mail sortant)** et sélectionnez **Exclude « Reply-To » and « Send Replies to From » (Exclure « Répondre à » et « Envoyer les réponses à De »)** comme adresse par défaut.

## Comparaisons de campagne

Regardez [plusieurs campagnes à la fois pour comparer leurs performances relatives]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/comparing_campaigns/), côte à côte dans Braze - dans une seule fenêtre !

## Templater le dispatch_ID dans les messages avec Liquid

{% alert update %}
Le comportement par rapport au `dispatch_id` diffère entre Canvas et les campagnes, car Braze traite les Canvas Steps (à l’exception des étapes d’entrée, qui peuvent être programmées) en tant qu’événements déclenchés, et ce même lorsqu’elles sont « programmées ». En savoir plus sur le[ comportement de `dispatch_id`]({{site.baseurl}}/help/help_articles/data/dispatch_id/) dans Canvas et les campagnes.

_Mis à jour en août 2019._
{% endalert %}

Si vous souhaitez suivre l’envoi d’un message à partir du message (dans une URL, par exemple), vous pouvez intégrer le `dispatch_id`. Vous pouvez trouver le formatage dans notre liste de tags de personnalisation pris en charge, sous [Attributs Canvas]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

Le comportement est exactement identique à `api_id`, c.-à-d. que lorsque `api_id` n’est pas disponible lors de la création de campagnes, il est affiché sous forme de marque substitutive et il sera prévisualisé comme `dispatch_id_for_unsent_campaign`. L’ID est généré avant l’envoi du message et sera ajouté au moment de l’envoi.

{% alert warning %}
Le templating Liquid de `dispatch_id_for_unsent_campaign` ne fonctionne pas avec les messages in-app, car les messages n’ont pas de `dispatch_id`.
{% endalert %}

## Le paramètre « Show Only Mine » (Afficher uniquement les miennes) est persistant

Le filtre « Show Only Mine » (Afficher uniquement les miennes) sur la grille de campagne restera « activé » à chaque fois que vous irez sur la page **Campaigns** (Campagnes).

## Mises à jour des tests A/B

Vous pouvez envoyer un [Test A/B]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/) ponctuel avec jusqu’à huit variantes (et contrôle optionnel) pour un pourcentage spécifié par l’utilisateur de l’audience d’une campagne, puis envoyer la meilleure variante au public restant à un moment préprogrammé.
