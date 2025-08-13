---
nav_title: Utilisateurs et segmentations
article_title: "Pour commencer : Utilisateurs et segmentations"
page_order: 2
page_type: reference
description: "Cet article donne un aperçu des utilisateurs et des segments, en soulignant leur importance et la façon dont ils peuvent être exploités pour engager votre audience."

---

# Pour commencer : Utilisateurs et segmentations

Comprendre vos utilisateurs et les cibler efficacement est crucial pour envoyer des campagnes marketing personnalisées et ciblées. Cet article donne un aperçu des utilisateurs et des segments, en soulignant leur importance et la façon dont ils peuvent être exploités pour engager votre audience.

## Utilisateurs

Dans Braze, les informations relatives à votre audience sont stockées dans les profils utilisateurs. Un [profil utilisateur]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/) est un ensemble complet d'informations et d'attributs qui décrivent un consommateur individuel. Il sert de référentiel central pour le stockage et la gestion des données relatives à leur comportement, à leurs préférences et à leurs données démographiques.

### Parties d'un profil utilisateur

En comprenant les profils utilisateurs, vous pouvez obtenir des informations sur votre audience et vous engager avec elle à un niveau personnalisé et ciblé. Le profil utilisateur contient de nombreuses informations, dont voici les principales :

- **Identifiant de l'utilisateur :** Chaque profil utilisateur est identifié de manière unique par un ID utilisateur, appelé `external_id`. Cet identifiant permet à Braze de suivre et d'associer les données des utilisateurs sur différents canaux et appareils, offrant ainsi une vue unifiée des interactions de chaque utilisateur avec votre marque. Les [profils utilisateurs anonymes]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/) (les utilisateurs qui visitent votre site web ou votre application sans se connecter) n'ont pas de `external_id`, mais peuvent se voir attribuer des [alias d'utilisateur]({{site.baseurl}}/user_guide/data/user_data_collection/anonymous_users/#assigning-user-aliases) comme identifiant alternatif.
- [Attributs](#attributes)**:** Il s'agit d'informations spécifiques sur l'utilisateur, telles que son nom, son âge, son emplacement/localisation ou toute autre information démographique. Vous pouvez utiliser ces attributs pour segmenter votre audience et personnaliser vos messages.
- [Événements](#events)**:** Il s'agit des actions que l'utilisateur entreprend, comme effectuer un achat, cliquer sur un lien ou ouvrir une application. Braze suit ces événements pour vous aider à comprendre le comportement et l'engagement de l'utilisateur. À l'instar des attributs, vous pouvez également utiliser les événements pour segmenter et personnaliser.
- **Achats :** Cette section enregistre l'historique des achats de l'utilisateur. C'est essentiel pour comprendre les habitudes d'achat et les préférences de l'utilisateur.
- **Appareils :** Cette section répertorie les appareils que l'utilisateur a utilisés pour interagir avec votre marque. Il peut s'agir d'appareils mobiles, de navigateurs web et d'appareils connectés (tels que les wearables et les téléviseurs intelligents).
- **Engagement :** Cette section contient des informations sur les interactions de l'utilisateur avec les messages que vous lui envoyez, les segments auxquels il appartient, le statut de son abonnement, etc.
- **Historique des messages :** Il s'agit d'un enregistrement de tous les messages qui ont été envoyés à l'utilisateur à partir du canal de communication correspondant (comme l'e-mail ou le push).

{% alert tip %}
Les SDK de la plateforme Braze collectent automatiquement 27 attributs et événements différents. Grâce à ces événements et attributs standard, vous pouvez créer des segments dès l'intégration du SDK.
{% endalert %}

### Attributs

Les attributs sont des caractéristiques ou des propriétés spécifiques associées à un utilisateur. Ces attributs vous aident à segmenter et à cibler les utilisateurs en fonction de leurs caractéristiques uniques et de leurs centres d'intérêt. Il existe deux types d'attributs dans Braze : les attributs standard et les attributs personnalisés.

#### Attributs standard

Les attributs standard sont des attributs prédéfinis que vous pouvez suivre avec Braze après avoir intégré le SDK dans votre application. Il s'agit d'éléments communs d'information sur les utilisateurs que la plupart des apps trouveraient utiles, comme les données démographiques et les données sur les appareils. En voici quelques exemples :

- Prénom
- Nom
- E-mail
- Genre
- Date de naissance
- Pays
- Ville
- Dernière application utilisée
- Langue
- Fuseau horaire

#### Attributs personnalisés

Les [attributs personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) sont des attributs que vous définissez en fonction des besoins spécifiques de votre entreprise. Ils vous permettent de suivre des informations qui sont uniques à votre appli ou à votre entreprise. 

Par exemple, une application de streaming musical peut suivre des attributs personnalisés tels que :

- Genre préféré
- Nombre de chansons jouées
- Abonné Premium (Oui/Non)
- Artiste préféré

Une application de retailing, en revanche, pourrait suivre des attributs personnalisés comme :

- Taille de vêtement préférée
- Marque préférée
- Nombre d'achats
- Membre du programme de fidélisation (Oui/Non)

Les attributs personnalisés vous donnent la possibilité de collecter et d'analyser les données les plus pertinentes pour votre entreprise. Cependant, ils nécessitent une configuration supplémentaire.

Les attributs standard et personnalisés peuvent être utilisés pour segmenter votre audience et personnaliser vos messages marketing. Par exemple, vous pouvez envoyer une offre spéciale aux utilisateurs d'une certaine ville (attribut standard) qui ont effectué plus de 10 achats (attribut personnalisé).

### Événements

Les événements représentent des actions ou des comportements spécifiques effectués par les utilisateurs au sein de votre appli ou de votre site web. Parmi les exemples d'événements, on peut citer le lancement d'une application, un achat, la consultation d'un contenu ou toute autre action. En suivant et en analysant ces événements, vous pouvez obtenir des informations sur le comportement des utilisateurs et les modèles d'engagement.

#### Événements standard

Les [événements standard]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/events#standard-events) sont des événements prédéfinis que Braze suit automatiquement après l'intégration du SDK dans votre application ou votre site. Voici quelques exemples d'événements standard :

- **Début de la session :** Cet événement est déclenché lorsqu'un utilisateur ouvre l'application.
- **Fin de la session :** Cet événement est déclenché lorsqu'un utilisateur ferme l'application.
- **Achat :** Cet événement est déclenché lorsqu'un utilisateur effectue un achat dans l'appli.
- **Clic sur la notification push :** Cet événement est déclenché lorsqu'un utilisateur clique sur une notification push.

#### Événements personnalisés

Les [événements personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) sont des événements que vous définissez en fonction des actions spécifiques que vous souhaitez suivre au sein de votre app ou de votre site. Par exemple, une application de flux d'écoute de musique peut suivre des événements personnalisés tels que :

- Chanson jouée
- Liste de lecture créée
- Annonce sautée

Une application de fitness, en revanche, pourrait suivre des événements personnalisés tels que :

- Début de l'entraînement
- Séance d'entraînement terminée
- Record personnel établi

Les événements personnalisés vous donnent la possibilité de suivre les actions les plus pertinentes pour votre application et votre entreprise. Cependant, comme les attributs personnalisés, ils nécessitent une configuration supplémentaire.

### Points de données

Braze utilise des points de données pour vous aider à définir les informations les plus impactantes pour votre entreprise. Les points de données constituent une partie cruciale du fonctionnement de Braze et sont utilisés pour la facturation, la tarification et, surtout, la personnalisation et l'optimisation de vos campagnes marketing.

Les points de données sont consommés lorsque les données de profil d'un utilisateur sont mises à jour ou lorsqu'il effectue des actions spécifiques. Ces actions peuvent inclure le démarrage d'une session, la fin d'une session, l'enregistrement d'un événement personnalisé ou la réalisation d'un achat. Il est important de noter que toutes les données collectées par Braze ne comptent pas comme des points de données. Par exemple, les données et les événements collectés par défaut par les Services Braze, tels que les jetons push, les informations sur les appareils et tous les événements de suivi de l'engagement des campagnes, comme les ouvertures d'e-mail et les clics sur les notifications push, ne sont pas jetés en tant que points de données.

En réfléchissant bien aux informations à suivre en tant que points de données, vous ciblez les données ayant le plus d'impact sur l'expérience de vos utilisateurs. Votre gestionnaire de compte Braze vous aidera à recommander les meilleures pratiques en matière de données en fonction de vos besoins.

Consultez notre article dédié pour en savoir plus sur les [points de données]({{site.baseurl}}/user_guide/data/data_points/).

## Segments

La [segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments) vous permet de cibler les utilisateurs en fonction de leurs caractéristiques et actions démographiques, comportementales, sociales ou techniques (c'est-à-dire les attributs et les événements). L'utilisation créative et intelligente de la segmentation et de l'automatisation des messages vous permet de faire évoluer vos utilisateurs de façon fluide/sans heurts tout au long de leur parcours client.

Conseils pour travailler avec des segments :

- Dans Braze, les segments sont dynamiques : les utilisateurs entrent et sortent constamment des segments, car ils ne correspondent pas toujours aux critères. Les utilisateurs qui correspondent aux critères d'un segment au moment de l'envoi seront les destinataires de cette campagne ou de ce Canvas.
    - Si vous souhaitez que votre segment soit statique, vous pouvez utiliser les extensions de segments. Les extensions de segments (avec la [régénération désactivée]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#extension-regeneration)) représentent votre audience comme un instantané unique dans le temps.
- Vous n'êtes pas limité à l'utilisation d'un seul filtre à la fois. Créez des segments granulaires finement ajustés en superposant plusieurs filtres.
- Vous pouvez utiliser les actions ou les inactions de vos utilisateurs pour comprendre comment atteindre vos utilisateurs là où ils veulent s'engager avec vous. Ces actions peuvent être des événements personnalisés, un engagement lié à une campagne ou un Canvas existant, ou même un message spécifique au sein d'un Canvas.

### Cas d’utilisation

Supposons que vous dirigiez un magasin de vêtements en ligne et que vous ayez mis en place un flux d'envoi de messages pour envoyer une série d'e-mails aux utilisateurs qui ont ajouté un article à leur panier mais n'ont pas terminé leur achat. Ce flux de panier abandonné pourrait inclure un e-mail de rappel initial, un e-mail de suivi offrant une réduction et un e-mail de rappel final.

![]({% image_buster /assets/img/getting_started/segment_example.png %}){: style="max-width:70%" }

Vous pouvez créer un segment d'utilisateurs qui ont déclenché l'événement personnalisé "Ajout d'un article au panier" mais qui n'ont pas déclenché l'événement personnalisé "Achats effectués". Ensuite, dans ce segment, vous pourriez identifier davantage les utilisateurs qui ont ouvert l'e-mail de rappel initial (engagement avec un message spécifique) mais qui n'ont pas effectué d'achat.

![]({% image_buster /assets/img/getting_started/segment_example_breakdown.png %})

Ce segment pourrait être ciblé par une campagne plus agressive pour tenter de convertir ces utilisateurs en acheteurs. Par exemple, vous pouvez leur envoyer une offre spéciale ou une recommandation personnalisée en fonction des articles de leur panier.

Ce n'est qu'un exemple de la façon dont vous pouvez utiliser les actions et inactions des utilisateurs, les événements personnalisés et les données d'engagement pour créer des segments et adapter vos stratégies marketing dans Braze.

