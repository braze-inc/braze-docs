---
nav_title: Aperçu de Braze
article_title: "Pour commencer : Aperçu de Braze"
page_order: 1
page_type: reference
description: "Familiarisez-vous avec les concepts de base que vous devrez connaître lorsque vous travaillerez dans Braze."

---

# Pour commencer : Aperçu de Braze

Bienvenue à Braze ! Cette collection d'articles vous aidera à démarrer avec notre plateforme et vous présentera les termes clés, les fonctionnalités et les caractéristiques de Braze. Cette page présente les concepts fondamentaux que vous devrez connaître lorsque vous travaillerez dans Braze.

{% alert tip %}
Nous vous recommandons vivement de consulter notre cours gratuit sur [les fondements de Braze pour tous](https://learning.braze.com/page/braze-foundations-for-everyone), ainsi que ces articles. Aucun identifiant ou compte spécial n'est nécessaire pour ce cours. Si vous êtes un développeur à la recherche d'une présentation technique de Braze, consultez également la rubrique [Démarrage pour les développeurs]({{site.baseurl}}/developer_guide/getting_started/platform_overview/).
{% endalert %}

Dans les sections Prise en main, nous nous concentrons sur les implémentations courantes de Braze. Cependant, Braze est incroyablement flexible et peut être personnalisé pour apporter de la valeur à votre organisation de différentes manières. Par souci de clarté et de concision, nous avons fourni un aperçu descriptif de la configuration par défaut au lieu de proposer des instructions rigoureuses. Nous sommes conscients que chaque organisation a ses propres besoins, et Braze est créé pour répondre à une gamme variée d'options de personnalisation qui peuvent être adaptées à vos exigences spécifiques.

Explorons ensemble la puissance de Braze.

## Comment fonctionne Braze ?

Braze est une plateforme d'engagement client qui aide les marques de toutes tailles à créer des campagnes personnalisées et ciblées sur différents canaux. Braze vous donne la possibilité d'écouter vos clients, de comprendre ce que leur comportement signale, puis d'agir en envoyant aux clients le bon message, par le bon canal, au bon moment.

{% alert tip %}
N'oubliez pas d'[ajouter vos collègues à Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/adding_users_to_your_dashboard/#adding-braze-users) pour qu'ils puissent explorer la plateforme avec vous.
{% endalert %}

## Utilisateurs et segmentations

Les utilisateurs sont vos personnalisés - les personnes qui reçoivent les messages que vous envoyez à l'aide de Braze. Toutes les données que vous recueillez sur un utilisateur et que vous ingérez dans Braze sont stockées dans son profil utilisateur, comme ses données démographiques, ses informations personnelles, ses préférences et ses comportements. Ces informations alimentent votre envoi de messages et vous permettent d'adapter vos messages au bon utilisateur.

\![]({% image_buster /assets/img/getting_started/user_profile.png %})

Les segments divisent votre base de clients en groupes plus petits que vous pouvez ensuite cibler avec des envois de messages spécifiques. Vous pouvez utiliser différentes variables pour créer des segments, allant de caractéristiques telles que le sexe, l'emplacement/localisation et l'âge à des comportements tels que les schémas d'interaction avec les campagnes précédentes ou l'endroit où ils se trouvent dans le parcours client.

Les segments sont dynamiques : les utilisateurs peuvent entrer et sortir des segments en temps réel en fonction de leur comportement et de leur position par rapport à votre marque. Ainsi, vos clients reçoivent les messages les plus pertinents pour eux à tout moment. Vous pouvez créer autant de segments que nécessaire pour vos objectifs de ciblage et d'envoi de messages.

\![]({% image_buster /assets/img/getting_started/segment.png %})

Pour en savoir plus, consultez le site : [Pour commencer : Utilisateurs et segments]({{site.baseurl}}/user_guide/getting_started/users_segments/).

## Campagnes et toiles

Les campagnes et les canevas vous permettent d'envoyer des messages à vos utilisateurs.

Les campagnes sont idéales pour les messages uniques envoyés à un segment d'audience spécifique sur différents canaux. Vous pouvez exploiter tous les canaux de messages pris en charge dans votre campagne (e-mail, push, messages in-app, SMS, et plus encore).

Les canevas sont des flux de campagne avancés qui vous permettent d'automatiser et d'orchestrer des parcours clients personnalisés sur plusieurs canaux. Dans un Canvas, vous pouvez mettre en place une logique de branchement, des délais, des points de décision et des événements de conversion pour guider les clients à travers une série d'interactions. Les toiles permettent d'assurer une communication cohérente et fluide sur différents points de contact, augmentant ainsi les chances d'engagement et de conversion des clients. 

Pour en savoir plus, consultez le site : [Pour commencer : Campagnes et toiles]({{site.baseurl}}/user_guide/getting_started/campaigns_canvases/).

## Espaces de travail

Les espaces de travail regroupent vos données (utilisateurs, segments, campagnes et toiles) en un seul emplacement/localisation. Les informations ne sont pas partagées entre les espaces de travail. Gardez cela à l'esprit lorsque vous ajoutez des sites web et des applications à vos espaces de travail. Nous vous conseillons de ne regrouper que les différentes versions d'une même application ou d'applications très similaires au sein d'un même espace de travail.

Voici quelques exemples d'utilisation des espaces de travail :

- Différentes lignes de produits ou applications
- Différentes audiences (par exemple, les chauffeurs de réception/distribution par rapport aux clients)
- Entreprises distinctes
- Environnement de test

Pour en savoir plus, consultez le site : [Pour commencer : Espaces de travail]({{site.baseurl}}/user_guide/getting_started/workspaces/).

## Intégration de Braze

Braze est conçu pour être rapidement et facilement opérationnel. Notre délai moyen de rentabilisation est de six semaines pour notre clientèle composée de centaines de marques.

\![]({% image_buster /assets/img/getting_started/timetovalue.png %})

Voici le cadre de Braze pour estimer la durée de votre intégration sur la base de quatre composants sur lesquels vous pouvez travailler en parallèle. La fourchette habituelle est de 30 à 180 jours, la plupart des comptes achevant leur intégration dans un délai de 45 à 60 jours.

- **Niveau de complexité de la migration de la campagne :** Le temps nécessaire à la migration des campagnes dépend de leur nombre, de leur degré de personnalisation et de vos ressources. Si vous avez moins de dix campagnes à migrer, cela prendra moins de 60 jours. Mais si vous avez plus de 100 campagnes, ce sera plus compliqué. Si une seule personne migre 100 campagnes, c'est différent de 10 personnes qui en migrent 100.

{% alert tip %}
Besoin d'aide pour votre migration ? Nos [partenaires certifiés Braze](https://www.braze.com/partners/solutions-partners) peuvent vous aider !
{% endalert %}

- **Volume d'e-mail :** Pour envoyer des e-mails, vous devez réchauffer vos adresses IP. Le [réchauffement d'adresses IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) consiste à créer une réputation d'expéditeur avec vos nouvelles adresses IP. Si vous envoyez moins de 2 à 3 millions d'e-mails par jour, le réchauffement d'IP devrait prendre 30 jours ou moins. Gardez à l'esprit vos pics d'envoi. Si vous envoyez normalement 2 millions d'e-mails par jour mais que vous prévoyez d'en envoyer 7 millions pendant une période saisonnière, c'est à ce "pic" d'envoi que vous devez vous préparer. Les expéditeurs de gros volumes peuvent utiliser plusieurs adresses IP pour accélérer le processus de réchauffement.
- **La complexité organisationnelle :** Notre processus d'onboarding peut s'adapter aux besoins de votre entreprise. Que vous soyez une seule unité commerciale, que vous ayez un centre d'excellence, plusieurs unités indépendantes ou que vous fassiez appel à des agences pour renforcer vos équipes, Braze a de l'expérience dans tous les cas de figure.
- **La sophistication de l'infrastructure de données :** Si vous ne mettez en œuvre que le SDK de Braze ou si vous disposez déjà d'une plateforme de données client (CDP), il est possible de tout mettre en place en seulement 30 jours. L'utilisation d'un CDP moderne peut accélérer le processus. Mais si vous avez de nombreux systèmes dorsaux, outils ou bases de données à connecter à Braze, cela peut prendre plus de temps et nécessiter plus de ressources dédiées pour terminer la configuration.

Pour en savoir plus, consultez le site : [Pour commencer : Aperçu de l'intégration]({{site.baseurl}}/user_guide/getting_started/integration/).

