---
nav_title: Équipes
article_title: Équipes
page_order: 4
page_type: reference
description: "Cet article de référence traite de l'utilisation de Braze Teams dans le tableau de bord. Vous y apprendrez à créer des Teams, à leur attribuer des rôles et à leur attribuer des tags et des filtres."

---

# Équipes

> En tant qu'administrateur Braze, vous pouvez regrouper les utilisateurs de votre tableau de bord en Teams, avec différents rôles et autorisations. Cela vous permet de faire travailler ensemble dans un même espace de travail plusieurs groupes d'utilisateurs de tableaux de bord sans lien entre eux, en séparant les types de contenu qui peuvent être modifiés.

Les Teams peuvent être constituées en fonction de l'emplacement/localisation des clients, de la langue et d'attributs personnalisés, de sorte que les membres de l'équipe et les non-membres aient un accès différent aux fonctionnalités d'envoi des messages et aux données des clients. Des filtres et des balises d’équipes peuvent être attribués à différents outils d’engagement.

L’option Teams (Équipes) n’est pas disponible sur tous les contrats Braze. Si vous souhaitez accéder à cette fonctionnalité, adressez-vous à votre gestionnaire de compte Braze ou [contactez-nous](mailto:success@braze.com) pour une consultation.

## En quoi les Teams diffèrent-elles des jeux de permissions et des rôles ?

{% multi_lang_include permissions.md content="Différences" %}

## Créer des équipes

Allez dans **Paramètres** > **Équipes internes** et sélectionnez <i class="fas fa-plus"></i> **Ajouter une équipe**.

![Ajout d'un nouveau Teams]({% image_buster /assets/img_archive/adding_a_team.png %})

Saisissez le **nom de l'équipe**. Si vous le souhaitez, utilisez le champ **Définir l'équipe** pour sélectionner un attribut personnalisé, un emplacement ou une langue afin de définir plus précisément les données utilisateur auxquelles l'équipe a accès. Par exemple, un cas d'utilisation possible consiste à effectuer [des tests avec des Teams](#testing-with-Teams) en créant une équipe de développement qui n'a accès qu'aux utilisateurs test, identifiés par un attribut personnalisé. Un autre cas d'utilisation consiste à restreindre la communication avec les utilisateurs en fonction du produit.

Si une équipe est définie par un attribut personnalisé, une langue ou un pays, vous pouvez alors utiliser l'équipe pour filtrer les utilisateurs finaux pour des fonctionnalités telles que les campagnes, les Canvas, les cartes de contenu, les segments, etc. Pour en savoir plus, consultez la section [Attribution de tags d'équipe](#tags-and-filters).

## Affectation d'utilisateurs à des Teams

Les administrateurs de Braze et les utilisateurs limités disposant de l'autorisation au niveau de l'entreprise "Peut gérer les paramètres de l'entreprise" peuvent attribuer des autorisations au niveau de l'équipe à un utilisateur du tableau de bord disposant d'un accès limité. Lorsqu'ils sont affectés à une équipe, les utilisateurs du tableau de bord sont limités à la lecture ou à l'écriture des données disponibles pour leur équipe particulière, telles que la langue de l'utilisateur, l'emplacement ou un attribut personnalisé, comme défini lors de la création de l'équipe.

Pour affecter un utilisateur à une équipe, accédez à **Paramètres** > **Utilisateurs de l'entreprise** et sélectionnez l'utilisateur que vous souhaitez ajouter à votre équipe.

Effectuez ensuite les étapes suivantes :

1. Sélectionnez **Modifier**.
2. Définissez leur rôle d'utilisateur comme étant **limité**.
3. Ajoutez-les à l'espace de travail approprié. 
4. Sélectionnez l' **équipe** à laquelle vous souhaitez ajouter cet utilisateur et attribuez des autorisations spécifiques dans la colonne Autorisations de **l'équipe.** 

![]({% image_buster /assets/img/teams.png %})

### Autorisations disponibles au niveau de l'équipe

Vous trouverez ci-dessous toutes les autorisations disponibles que vous pouvez attribuer au niveau de l'équipe. Toutes les autorisations qui ne figurent pas dans cette liste ne sont accordées qu'au niveau de l'espace de travail, et ces autorisations apparaissent sous la forme "--" dans la colonne des autorisations de **Teams.** 

- Accédez aux campagnes, aux toiles, aux cartes, aux blocs de contenu, aux drapeaux de fonctionnalité, aux segments, à la bibliothèque multimédia et aux centres de préférences.
- Envoyer des campagnes, des canvas
- Publier des cartes
- Modifier les segments
- Exporter les données utilisateur
- Voir les profils utilisateur respectueux des données d'identification
- Gérer les utilisateurs du tableau de bord
- Gérer les ressources de la bibliothèque multimédia

Pour obtenir une description de chaque autorisation d'utilisateur et savoir comment l'utiliser, consultez notre section [Autorisations d'utilisateur.]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions) 

## Attribution de tags aux équipes {#tags-and-filters}

Vous pouvez affecter une équipe à des toiles, des campagnes, des cartes, des segments, des modèles e-mail et des ressources de la bibliothèque multimédia à l'aide du filtre **Ajouter une équipe**.
 
![Ajouter une étiquette d'équipe à une campagne]({% image_buster /assets/img/teams1.png %}){: style="max-width:70%;"}

- En fonction des *définitions* appliquées lors de la création de l'équipe, lorsqu'un filtre d'équipe est attribué, l'audience de cet outil d'engagement est limitée aux profils utilisateurs qui correspondent à la définition.
- En fonction des *autorisations* qui leur ont été attribuées, les membres de l'équipe ne pourront accéder qu'aux outils d'engagement du tableau de bord pour lesquels le filtre de l'équipe a été défini. S'ils disposent d'autorisations limitées ou inexistantes sur l'espace de travail, ils doivent ajouter un filtre Teams à certains objets avant de pouvoir les enregistrer ou les lancer. Les membres de l'équipe sont également en mesure de filtrer les Canvas, les campagnes, les cartes et les segments par équipe afin d'identifier le contenu qui leur est pertinent.

### Cas d’utilisation

Envisagez les deux scénarios suivants pour Michelle, une spécialiste du marketing chez Braze. Michelle est membre d'une Teams appelée "Développement". Elle a accès à toutes les autorisations au niveau de l'équipe pour l'équipe de développement.

{% tabs %}
{% tab Scénario 1 - Autorisations pour l'équipe uniquement %}

Dans ce scénario, Michelle est un utilisateur limité qui ne dispose d'aucune autorisation au niveau de l'espace de travail. Ses autorisations ressemblent à peu près à ceci :

![]({% image_buster /assets/img_archive/scenario1.png %})

Sur la base des autorisations attribuées à Michelle, chaque fois qu'elle crée une campagne, elle ne peut y affecter que l'équipe "Développement". Elle ne peut pas lancer la campagne si l'équipe n'est pas assignée, et elle ne peut pas voir ou accéder aux autres tags de l'équipe.

![]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab Scénario 2 - Permissions d'équipe et d'espace de travail %}

Dans ce scénario, Michelle est toujours membre de l'équipe de développement, mais elle dispose également d'une autorisation supplémentaire au niveau de l'espace de travail.

![]({% image_buster /assets/img_archive/scenario2.png %})

Comme Michelle dispose de l'autorisation de niveau espace de travail "Accéder aux campagnes, aux canevas, aux cartes, aux blocs de contenu, aux drapeaux de fonctionnalité, aux segments, à la bibliothèque multimédia et aux centres de préférences", elle peut afficher et attribuer d'autres filtres d'équipe à la campagne qu'elle crée.

![]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

Comme dans le premier scénario, Michelle doit ajouter l'étiquette de l'équipe de développement à la campagne avant de pouvoir la lancer.

{% endtab %}
{% endtabs %}

## Tester avec des Teams

L'un des cas d'utilisation possibles de Teams est la création d'un système d'approbation basé sur Teams pour tester et lancer du contenu dans un environnement de production.

Pour ce faire, créez une Teams "Développement" qui n'a accès qu'aux utilisateurs test. Vous pouvez limiter l'accès d'une équipe aux seuls utilisateurs test si vos utilisateurs test sont identifiables par un attribut personnalisé. Ensuite, ajoutez l'attribut personnalisé en tant que définition lorsque vous créez ou modifiez l'équipe (voir la section précédente [Création d'équipes](#creating-Teams)). Vos approbateurs doivent avoir accès à tous les utilisateurs.

La procédure générale serait la suivante :

1. L'équipe de développement crée une campagne et y ajoute l'étiquette "Développement".
2. L'équipe de développement lance la campagne auprès des utilisateurs tests.
3. L'équipe d'approbateurs valide la conception de la campagne locale, la promeut et la lance. Pour lancer la campagne, l'équipe d'approbateurs change l'étiquette de l'équipe de "Développement" en "[Toutes les équipes]]" et relance la campagne.

Pour les modifications apportées aux campagnes actives :

1. L'équipe de développement clone la campagne en cours, ajoute l'étiquette "Développement" et enregistre.
2. L'équipe de développement modifie et partage avec l'équipe d'approbation.
3. L'équipe d'approbateurs supprime l'étiquette de l'équipe de développement, met en pause la campagne précédente et lance la nouvelle campagne.

## Archivage d’une Team existante

Vous pouvez archiver des Teams à partir de la page **Teams internes**.

Sélectionnez un ou plusieurs Teams à archiver. Si la Team n’est pas associée à un objet au sein de Braze, la Team sera archivée immédiatement. Si la Team est associée à un objet, vous aurez le choix entre supprimer la Team après le processus d’archivage et remplacer la Team.

![Archivage d'une équipe associée à un objet dans Braze]({% image_buster /assets/img_archive/archive_a_team.png %}){: style="max-width:70%;"}

Les administrateurs de Braze peuvent désarchiver une équipe en sélectionnant l'équipe archivée et en choisissant **Désarchiver**.

