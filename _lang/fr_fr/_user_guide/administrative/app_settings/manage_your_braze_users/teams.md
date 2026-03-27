---
nav_title: Équipes
article_title: Équipes
page_order: 4
page_type: reference
alias: /teams/
description: "Cet article de référence traite de l'utilisation des Teams Braze dans le tableau de bord. Vous y apprendrez à créer des Teams, à attribuer des rôles, ainsi que des étiquettes et des filtres."

---

# Équipes

> En tant qu'administrateur Braze, vous pouvez regrouper les utilisateurs de votre entreprise au sein de Teams avec différents rôles et autorisations. Cela permet à plusieurs groupes d'utilisateurs, sans lien entre eux, de collaborer au sein d'un même espace de travail tout en séparant les types de contenu pouvant être modifiés.

Les Teams peuvent être constituées en fonction de la localisation des clients, de la langue et d'attributs personnalisés, de sorte que les membres et les non-membres d'une équipe aient un accès différent aux fonctionnalités d'envoi de messages et aux données clients. Des filtres et des étiquettes d'équipe peuvent être attribués à différents outils d'engagement. Il n'y a aucune limite au nombre d'équipes que vous pouvez créer dans votre espace de travail.

L'option Teams n'est pas disponible sur tous les contrats Braze. Pour accéder à cette fonctionnalité, contactez votre Account Manager Braze ou [contactez-nous](mailto:success@braze.com) pour une consultation.

## En quoi les Teams diffèrent-elles des jeux d'autorisations et des rôles ?

{% multi_lang_include permissions.md content="Differences" %}

## Créer des Teams {#creating-teams}

Allez dans **Paramètres** > **Équipes internes** et sélectionnez <i class="fas fa-plus"></i> **Ajouter une équipe**.

![Fenêtre permettant d'ajouter une nouvelle équipe.]({% image_buster /assets/img_archive/adding_a_team.png %})

Saisissez le **nom de l'équipe**. Si vous le souhaitez, utilisez le champ **Définir l'équipe (facultatif)** pour sélectionner un attribut personnalisé, un emplacement ou une langue afin de définir plus précisément les données utilisateur auxquelles l'équipe a accès. Par exemple, un cas d'utilisation possible consiste à effectuer [des tests avec des Teams](#test-with-teams) en créant une équipe de développement qui n'a accès qu'aux utilisateurs test, identifiés par un attribut personnalisé. Un autre cas d'utilisation consiste à restreindre la communication avec les utilisateurs en fonction du produit.

Si une équipe est définie par un attribut personnalisé, une langue ou un pays, vous pouvez alors l'utiliser pour filtrer les utilisateurs finaux dans des fonctionnalités telles que les campagnes, les Canvas, les cartes de contenu, les segments, etc. Pour en savoir plus, consultez la section [Attribution d'étiquettes d'équipe](#tags-and-filters).

## Affecter des utilisateurs à des Teams

Les administrateurs Braze et les utilisateurs limités disposant de l'autorisation au niveau de l'entreprise « Peut gérer les paramètres de l'entreprise » peuvent attribuer des autorisations au niveau des Teams à un utilisateur de l'entreprise disposant d'un accès limité. Lorsqu'ils sont affectés à une équipe, les utilisateurs sont limités à la lecture ou à l'écriture des données disponibles pour leurs équipes respectives, telles que la langue de l'utilisateur, la localisation ou les attributs personnalisés, tels que définis lors de la création de l'équipe.

Pour affecter un utilisateur à une équipe, accédez à **Paramètres** > **Utilisateurs de l'entreprise** et sélectionnez l'utilisateur que vous souhaitez ajouter à votre équipe.

Effectuez ensuite les étapes suivantes :

1. Dans la section **Autorisations au niveau de l'espace de travail**, ajoutez l'utilisateur à l'espace de travail approprié s'il n'y figure pas déjà.

![Autorisations au niveau de l'espace de travail avec le jeu d'autorisations Modèle de bannière.]({% image_buster /assets/img/team_level_permissions.png %})

{: start="2"}
2. Sélectionnez **+ Ajouter des autorisations au niveau des Teams**, puis choisissez la **Team** à laquelle vous souhaitez ajouter cet utilisateur.
3. Attribuez des autorisations spécifiques depuis la section des autorisations **Teams**.

![Autorisations relatives aux modèles de page d'accueil au niveau des Teams.]({% image_buster /assets/img/teams.png %})

### Autorisations disponibles au niveau de l'équipe

Voici l'ensemble des autorisations que vous pouvez attribuer au niveau de l'équipe. Toutes les autorisations qui ne figurent pas dans cette liste ne sont accordées qu'au niveau de l'espace de travail et apparaissent sous la forme « -- » dans la colonne des autorisations **Teams**.

{% tabs %}
{% tab Granular permissions %}

{% multi_lang_include alerts/important_alerts.md alert="granular permissions ea" %}

- Afficher les campagnes
- Modifier les campagnes
- Archiver les campagnes
- Afficher les Canvas
- Modifier les Canvas
- Archiver les Canvas
- Afficher les blocs de contenu
- Modifier les blocs de contenu
- Archiver les blocs de contenu
- Lancer des blocs de contenu
- Voir les indicateurs de fonctionnalité
- Modifier les indicateurs de fonctionnalité
- Archiver les indicateurs de fonctionnalité
- Afficher les segments
- Modifier les segments
- Afficher les modèles d'e-mail
- Modifier les modèles d'e-mail
- Archiver les modèles d'e-mail
- Afficher les modèles de webhook
- Modifier les modèles de webhook
- Archiver les modèles de webhook
- Afficher les modèles de lien e-mail
- Modifier les modèles de lien e-mail
- Voir les ressources de la bibliothèque multimédia
- Modifier les ressources de la bibliothèque multimédia
- Supprimer les ressources de la bibliothèque multimédia
- Lancer des campagnes
- Lancer des Canvas
- Exporter les données utilisateur
- Voir les profils utilisateurs (données personnelles masquées)
- Modifier les utilisateurs du tableau de bord
- Approuver les campagnes
- Approuver les Canvas
- Modifier les modèles Canvas
- Afficher les modèles Canvas
- Archiver les modèles Canvas
- Consulter les rapports du tableau de bord
- Modifier les rapports du tableau de bord
- Supprimer les rapports du tableau de bord
- Voir les données personnelles

{% endtab %}
{% tab Legacy permissions %}

- Accéder aux campagnes, Canvas, cartes, blocs de contenu, indicateurs de fonctionnalité, segments, bibliothèque multimédia et centres de préférences
- Envoyer des campagnes, des Canvas
- Lancer et gérer les cartes de contenu
- Modifier les segments
- Exporter les données utilisateur
- Voir les profils utilisateurs conformes aux données personnelles
- Gérer les utilisateurs du tableau de bord
- Gérer les ressources de la bibliothèque multimédia
- Approuver et refuser des campagnes
- Approuver et refuser des Canvas
- Créer et modifier des modèles Canvas
- Afficher les modèles Canvas
- Archiver les modèles Canvas
- Modifier les modèles de page d'accueil
- Voir les modèles de page d'accueil
- Archiver les modèles de page d'accueil

{% endtab %}
{% endtabs %}

Pour obtenir une description de chaque autorisation utilisateur et savoir comment l'utiliser, consultez notre section [Autorisations utilisateur]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/user_permissions/#editing-user-permissions).

## Attribuer des étiquettes d'équipe {#tags-and-filters}

Vous pouvez affecter une équipe à des Canvas, des campagnes, des cartes de contenu, des segments, des modèles d'e-mail, des modèles de webhook, des blocs de contenu et des ressources de la bibliothèque multimédia à l'aide du filtre **Ajouter une équipe**.
 
![Ajouter une étiquette d'équipe à une campagne.]({% image_buster /assets/img/teams1.png %}){: style="max-width:70%;"}

- En fonction des *définitions* appliquées lors de la création de l'équipe, lorsqu'un filtre d'équipe est attribué, l'audience de cet outil d'engagement est limitée aux profils utilisateurs correspondant à la définition.
- En fonction des *autorisations* attribuées, les membres de l'équipe ne pourront accéder qu'aux outils d'engagement du tableau de bord pour lesquels le filtre de leur équipe est défini. S'ils disposent d'autorisations limitées ou inexistantes sur l'espace de travail, ils doivent ajouter un filtre d'équipe à certains objets avant de pouvoir les enregistrer ou les lancer. Les membres de l'équipe peuvent également filtrer les Canvas, les campagnes, les cartes de contenu et les segments par équipe afin d'identifier le contenu qui les concerne.

### Cas d'utilisation

Prenons les deux scénarios suivants pour Michelle, une marketeur utilisant Braze. Michelle est membre d'une Team appelée « Development ». Elle a accès à toutes les autorisations au niveau de l'équipe pour la Team Development.

{% tabs %}
{% tab Scenario 1 - Only Team permissions %}

Dans ce scénario, Michelle est une utilisatrice restreinte qui ne dispose d'aucune autorisation au niveau de l'espace de travail. Ses autorisations ressemblent à ceci :

![Autorisations personnalisées sans autorisations au niveau de l'espace de travail et 16 autorisations basées sur l'équipe.]({% image_buster /assets/img_archive/scenario1.png %})

Avec les autorisations qui lui sont attribuées, chaque fois que Michelle crée une campagne, elle ne peut y affecter que l'équipe « Development ». Elle ne peut pas lancer la campagne si l'équipe n'est pas assignée, et elle ne peut ni voir ni accéder aux autres étiquettes d'équipe.

![Menu déroulant des étiquettes d'équipe de campagne qui n'affiche que l'étiquette « Development ».]({% image_buster /assets/img_archive/team_permissions_scenario1.gif %})

{% endtab %}
{% tab Scenario 2 - Team permissions and workspace permissions %}

Dans ce scénario, Michelle est toujours membre de l'équipe Development, mais elle dispose également d'une autorisation supplémentaire au niveau de l'espace de travail.

![Autorisations personnalisées avec une autorisation au niveau de l'espace de travail et 15 autorisations au niveau de l'équipe.]({% image_buster /assets/img_archive/scenario2.png %})

Comme Michelle dispose de l'autorisation au niveau de l'espace de travail « Accéder aux campagnes, Canvas, cartes, blocs de contenu, indicateurs de fonctionnalité, segments, bibliothèque multimédia et centres de préférences », elle peut afficher et attribuer d'autres filtres d'équipe à la campagne qu'elle crée.

![Menu déroulant des étiquettes d'équipe de campagne avec plusieurs étiquettes d'équipe]({% image_buster /assets/img_archive/team_permissions_scenario2.gif %})

Comme dans le premier scénario, Michelle doit ajouter l'étiquette de l'équipe Development à la campagne avant de pouvoir la lancer.

{% endtab %}
{% endtabs %}

## Tester avec des Teams

L'un des cas d'utilisation possibles des Teams est la création d'un système d'approbation basé sur les équipes pour tester et lancer du contenu dans un environnement de production.

Pour ce faire, créez une Team « Development » qui n'a accès qu'aux utilisateurs test. Vous pouvez limiter l'accès d'une équipe aux seuls utilisateurs test si ceux-ci sont identifiables par un attribut personnalisé. Ensuite, ajoutez cet attribut personnalisé en tant que définition lors de la création ou de la modification de l'équipe (voir la section précédente [Créer des Teams](#creating-Teams)). Vos approbateurs doivent avoir accès à tous les utilisateurs.

La procédure générale est la suivante :

1. L'équipe de développement crée une campagne et y ajoute l'étiquette « Development ».
2. L'équipe de développement lance la campagne auprès des utilisateurs test.
3. L'équipe d'approbation valide la conception de la campagne locale, la promeut et la lance. Pour ce faire, l'équipe d'approbation modifie l'étiquette d'équipe de « Development » à « [All Teams] » et relance la campagne.

Pour les modifications apportées aux campagnes actives :

1. L'équipe de développement clone la campagne en cours, ajoute l'étiquette « Development » et enregistre.
2. L'équipe de développement effectue les modifications et les partage avec l'équipe d'approbation.
3. L'équipe d'approbation supprime l'étiquette de l'équipe Development, met en pause la campagne précédente et lance la nouvelle campagne.

## Archiver une équipe existante

Vous pouvez archiver des Teams à partir de la page **Équipes internes**.

Sélectionnez une ou plusieurs Teams à archiver. Si la Team n'est associée à aucun objet dans Braze, elle sera archivée immédiatement. Si la Team est associée à un objet, vous aurez le choix entre supprimer la Team après le processus d'archivage ou la remplacer.

![Archivage d'une équipe associée à un objet dans Braze]({% image_buster /assets/img_archive/archive_a_team.png %}){: style="max-width:70%;"}

Les administrateurs Braze peuvent désarchiver une équipe en sélectionnant l'équipe archivée puis en cliquant sur **Désarchiver**.