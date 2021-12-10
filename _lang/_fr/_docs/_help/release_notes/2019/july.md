---
nav_title: Juillet
page_order: 6
noindex: vrai
page_type: Mettre à jour
description: "Cet article contient des notes de mise à jour pour juillet 2019."
---

# Juillet 2019

{% alert update %}
Braze a eu deux cycles de publication de produits (vous avez lu ce droit - **deux**) ce mois-ci ! La dernière version est notée en haut, la précédente [commence plus loin cette page](#earlier-this-month)!
{% endalert %}

## SAML/SSO

[Single Sign On (SSO)]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/) fournit aux entreprises une manière sécurisée et centralisée de contrôler l'accès au tableau de bord de Braze. En bref, un seul ensemble d’identifiants peut être utilisé pour accéder à différentes applications, y compris le Brésil.

En plus de [Google Sign-In en utilisant le support OAuth 2.0](https://developers.google.com/identity/protocols/OAuth2), les entreprises aimeraient bénéficier du support SSO avec Security Assertion Markup Language (SAML). Cela leur permet de s'intégrer de manière transparente avec les grands fournisseurs d'identité (IdP), y compris [Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/azure_ad/) et [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/), qui prennent en charge les dernières normes de l'industrie (SAML 2.0).

Braze prend en charge :
- [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)
- [Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/azure_ad/)
- [Octa]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)

## Ajuster les séries de clés API de l'événement

Nous avons mis à jour la page partenaire d'Adjust pour rendre cette clé API accessible aux clients.

## Nouveaux partenaires

Quelques nouveaux partenaires ont rejoint notre programme d'alliages et ont été ajoutés à nos Docs ! Dites bonjour à...
- [FiveTran]({{site.baseurl}}/partners/fivetran/)
- [Un]({{site.baseurl}}/partners/talonone/)
- [Bon de réduction]({{site.baseurl}}/partners/voucherify/)

## Amélioration des détails de la campagne

Les détails étendus de la campagne sont maintenant affichés dans la ... attendez ... **la section des Détails de la campagne** de la page **Campagne**!

## Afficher la mine uniquement dans les segments & Canvas

Le filtre "Afficher la mienne" sur la page des **Campagnes** s'est avéré très populaire ! En conséquence, nous ajoutons également cette option aux listes Canvas and Segment !

### Comportement d'avancement

Vous pouvez maintenant choisir [quand un utilisateur avance]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) d'une étape de Canvas à l'autre - les options sont "Message Envoyé" et "Toute l'audience après retard".

### Messages intégrés dans Canvas

[Les messages intégrés sont maintenant disponibles avec Canvas !]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/) Ajoutez une étape de Canvas et naviguez sur les canaux disponibles pour ajouter un message dans l'application.

# Plus tôt ce mois-ci

## Suppression de l'image du profil utilisateur

Nous sommes en train de supprimer les photos de profil de l'utilisateur affichées dans Braze profils d'utilisateurs et les recherches d'utilisateurs.

## Contenu connecté dans les cartes de contenu

Vous pouvez maintenant utiliser les chaînes et les fonctionnalités [Contenus connectés]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) dans [Cartes de Contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/overview/).

Les appels de contenu connectés à des serveurs externes se produiront lorsqu'une carte est effectivement envoyée, __pas__ lorsque la carte est visualisée par l'utilisateur. Similaire à l'Email, le contenu dynamique sera calculé et déterminé au moment de l'envoi, plutôt que quand une carte est effectivement consultée.

## Adresse 'reply-to' nulle

Les clients peuvent maintenant définir une valeur `null` pour l'adresse "Répondre à" d'un message électronique à partir de la page des paramètres de messagerie de Braze ou en utilisant [l'API]({{site.baseurl}}/api/endpoints/messaging/#email-object-specification).  Lorsqu'il est utilisé, les réponses seront envoyées à l'adresse "De" listée.  Vous pouvez maintenant personnaliser le champ "De" comme `dan@emailaddress.com` et vos clients auront la possibilité de répondre directement à Dan.

Pour définir une valeur de `null` pour l'adresse "Répondre à" d'un e-mail provenant de Braze, allez dans `Gérer les paramètres` dans la navigation, puis dans l'onglet `Paramètres de messagerie`. Faites défiler jusqu'à la section `Paramètres de messagerie sortante` et sélectionnez `Exclure "Répondre à" et envoyer les réponses à "De"` comme adresse par défaut.

## Comparaisons de campagne

Regardez [campagnes multiples à la fois pour comparer leurs performances relatives]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/comparing_campaigns/), côte à côte dans Braze - dans une seule fenêtre !

## Modèle d'ID d'envoi dans les messages avec Liquid

{% alert update %}
Le comportement de `dispatch_id` diffère entre Canvas et les campagnes car Braze traite les pas de Canvas (à l'exception des pas d'entrée, qui peuvent être programmés) en tant qu'événements déclenchés, même lorsqu'ils sont "programmés". [En savoir plus sur le comportement de `dispatch_id` dans Canvas et les campagnes ici]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

_Mise à jour notée en août 2019._
{% endalert %}

Si vous voulez suivre l'envoi d'un message depuis l'intérieur du message (dans une URL, par exemple), vous pouvez modéliser dans le `dispatch_id`. Vous pouvez trouver le formatage pour cela dans notre liste de balises de personnalisation supportées, sous [Attributs de canvas]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

Cela se comporte comme `api_id`, car l'api_id `api_id` n'est pas disponible lors de la création de la campagne, elle est tempérée en tant que placeholder et sera prévisualisée comme `dispatch_id_for_unsent_campaign`. L'identifiant est généré avant l'envoi du message, et sera inclus dans l'heure d'envoi.

{% alert warning %}
Les modèles liquides de `dispatch_id_for_unsent_campaign` ne fonctionnent pas avec les messages dans l'application, car les messages dans l'application n'ont pas de `dispatch_id`.
{% endalert %}

## Le paramètre "Afficher la mienne" persiste

Le filtre "Show Only Mine" sur la grille de campagne restera "on" chaque fois que vous visitez la page des **Campagnes**.

## Mises à jour A/B test

Vous pouvez envoyer un [test A/B ponctuel]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/) avec jusqu'à huit variantes (et un contrôle facultatif) à un pourcentage spécifié par l'utilisateur de l'auditoire de la campagne, puis envoyer la meilleure variante au public qui reste à un moment préprogrammé.
