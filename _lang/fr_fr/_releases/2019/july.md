---
nav_title: juillet
page_order: 6
noindex: true
page_type: update
description: "Cet article contient les notes de version de juillet 2019."
---

# Juillet 2019

{% alert update %}
Braze a eu deux (vous avez bien lu - **deux**) cycles de lancement de produits ce mois-ci ! La dernière version est indiquée en haut de page, la version précédente [commence plus bas sur cette page](#earlier-this-month)!
{% endalert %}

## Authentification unique (SSO) SAML

L'[authentification unique]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/) (SSO) offre aux entreprises un moyen sécurisé et centralisé de contrôler l'accès au tableau de bord de Braze. Pour faire court, elle permet d’utiliser un seul identifiant/mot de passe pour se connecter à différentes applications, y compris Braze.

En plus de [Google Sign-In avec la prise en charge d'OAuth 2.0](https://developers.google.com/identity/protocols/OAuth2), les entreprises souhaiteraient un SSO avec la prise en charge de SAML (Security Assertion Markup Language). Ils peuvent ainsi s'intégrer de façon fluide aux grands fournisseurs d'identité (IdP), notamment [Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/) et [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/), qui prennent en charge les dernières normes du secteur (SAML 2.0).

Braze prend en charge :
- [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)
- [Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/)
- [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)

## Affichage de la clé API Événement d’Adjust

Nous avons mis à jour la page partenaire d’Adjust pour rendre cette clé API accessible aux clients.

## Nouveaux partenaires

Certains nouveaux partenaires ont rejoint notre programme Alloys et ont été ajoutés à notre documentation ! Dites bonjour à :
- [Fivetran]({{site.baseurl}}/partners/fivetran/)
- [Talon.One]({{site.baseurl}}/partners/talonone/)
- [Voucherify]({{site.baseurl}}/partners/voucherify/)

## Amélioration des détails de la campagne

Les détails de la campagne sont désormais affichés dans la section ...attendez..**.Détails de la campagne** de la page de la **campagne**!

## Afficher uniquement les miennes dans Segments et Canvas

Le filtre "Afficher uniquement les miens" sur la page des **campagnes** s'est avéré très populaire. Par conséquent, nous ajoutons également cette option aux listes Canvas et Segment !

### Comportement d’avancement

Vous pouvez désormais choisir le [moment où un utilisateur passe]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) d'une étape du canvas à l'autre. Ces options comprennent « Message Sent » (Message envoyé) et « Entire Audience After Delay » (Toute l’audience après un délai).

### Messages in-app de Canvas

Les [messages in-app]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/) sont désormais disponibles dans Canvas ! Ajoutez une étape de Canvas et parcourez les canaux disponibles pour ajouter un message in-app.

# Plus tôt ce mois-ci

## Suppression de l’image du profil utilisateur

Nous avons supprimé les images de profil utilisateur affichées dans les profils utilisateur de Braze et les recherches d’utilisateurs.

## Contenu connecté dans les Cartes de contenu

Vous pouvez désormais utiliser les chaînes de caractères et les fonctionnalités du [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) dans les [cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/).

Les appels de contenu connectés vers des serveurs externes se produisent lorsqu’une carte est réellement envoyée, et non lorsque la carte est vue par l’utilisateur. Comme pour l’e-mail, le contenu dynamique sera calculé et déterminé au moment de l’envoi, et non pas au moment où la carte est visualisée.

## Adresse « reply-to » (répondre à) nulle

Les clients peuvent désormais définir une valeur `null` pour l'adresse "reply-to" d'un message e-mail à partir de la page **Paramètres de l'e-mail** dans Braze ou en utilisant l ['API]({{site.baseurl}}/api/endpoints/messaging/#email-object-specification).  Quand cette option est utilisée, les réponses seront envoyées à l’adresse « De » indiquée.  Vous pouvez maintenant personnaliser le champ d’adresse « De » en tant que `dan@emailaddress.com`, et vos clients auront la possibilité de répondre directement à Dan.

Pour définir une valeur `null` pour l'adresse "reply-to-" d'un message e-mail provenant de Braze, allez dans la navigation sous **Gérer les paramètres**, puis sous l'onglet **Paramètres de l'e-mail.**  Faites défiler jusqu'à la section **Paramètres des e-mails sortants** et sélectionnez **Exclure "Répondre à" et envoyer les réponses à "De"** comme adresse par défaut.

## Comparaisons de campagne

Examinez [plusieurs campagnes en même temps pour comparer leurs performances relatives]({{site.baseurl}}/report_builder/), côte à côte dans Braze - dans une seule fenêtre !

## Templater le dispatch_ID dans les messages avec Liquid

{% alert note %}
Le comportement de `dispatch_id` diffère entre Canvas et les campagnes car Braze traite les étapes de Canvas (à l'exception des étapes d'entrée, qui peuvent être planifiées) comme des événements déclenchés, même lorsqu'elles sont "planifiées". En savoir plus sur le [comportement de`dispatch_id` ]({{site.baseurl}}/help/help_articles/data/dispatch_id/) dans les canevas et les campagnes.
{% endalert %}

Si vous souhaitez suivre l’envoi d’un message à partir du message (dans une URL, par exemple), vous pouvez intégrer le `dispatch_id`. Vous trouverez le formatage correspondant dans notre liste des tags de personnalisation pris en charge, sous [Attributs du canevas.]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/)

Le comportement est exactement identique à `api_id`, c.-à-d. que lorsque `api_id` n’est pas disponible lors de la création de campagnes, il est affiché sous forme de marque substitutive et il sera prévisualisé comme `dispatch_id_for_unsent_campaign`. L’ID est généré avant l’envoi du message et sera ajouté au moment de l’envoi.

{% alert warning %}
Le templating Liquid de `dispatch_id_for_unsent_campaign` ne fonctionne pas avec les messages in-app, car les messages n’ont pas de `dispatch_id`.
{% endalert %}

## Le paramètre « Show Only Mine » (Afficher uniquement les miennes) est persistant

Le filtre "Afficher uniquement les miens" de la grille de campagne restera activé chaque fois que vous visiterez la page **Campagnes.** 

## Mises à jour des tests A/B

Vous pouvez envoyer un [test A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) unique comprenant jusqu'à huit variantes (et un contrôle facultatif) à un pourcentage spécifié par l'utilisateur de l'audience d'une campagne, puis envoyer la meilleure variante à l'audience restante à une date planifiée à l'avance.
