---
nav_title: Créer et gérer des espaces de travail
article_title: Créer et gérer des espaces de travail
page_order: 0
page_type: reference
description: "Cet article explique comment créer, configurer et gérer vos espaces de travail."

---

# Créer et gérer des espaces de travail

> Cet article explique comment créer, configurer et gérer vos espaces de travail. 

## Qu'est-ce qu'un espace de travail ?

Tout ce que vous faites dans Braze se passe dans un espace de travail. Les espaces de travail sont un environnement partagé qui vous permet de suivre et gérer l’engagement pour les applications mobiles ou les sites Internet qui lui sont liés. Les espaces de travail regroupent les mêmes applications ou des applications très similaires : par exemple, les versions Android et iOS de votre application mobile. 

## Créer un espace de travail

### Étape 1 : Préparez un plan

Avant de commencer, assurez-vous d'avoir travaillé avec votre équipe et votre gestionnaire onboarding de Braze pour déterminer la meilleure configuration d'espace de travail pour votre cas d'utilisation. Pour en savoir plus sur la planification de vos espaces de travail dans Braze, consultez notre site [Getting Started : Guide des espaces de travail]({{site.baseurl}}/user_guide/getting_started/workspaces/).

### Étape 2 : Ajoutez votre espace de travail

Vous pouvez créer de nouveaux espaces de travail ou passer d'un espace de travail à l'autre à partir de la liste déroulante de l'espace de travail dans l'en-tête global.

1. Sélectionnez la liste déroulante Espace de travail, puis <i class="fa-solid fa-square-plus" style="color: #0b8294;"></i> **Créer un espace de travail**.

![La liste déroulante de l'espace de travail avec le bouton "Créer un espace de travail".]({% image_buster /assets/img/workspaces/workspace_create.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Donnez un nom à votre espace de travail.

{% alert tip %}
Vous pouvez adopter une convention de dénomination afin que les autres membres de votre entreprise puissent facilement trouver votre espace de travail. Par exemple : « Upon Voyage US - Production » et « Upon Voyage US - Organisation ».
{% endalert %}

{:start="3"}
3\. Sélectionnez **Créer**. La création de votre espace de travail par Braze peut prendre quelques secondes.

![Fenêtre modale "Create Workspace" avec le nom "Upon Voyage US - Staging".]({% image_buster /assets/img/workspaces/workspace_name.png %}){: style="max-width:60%" }

Vous accéderez à la page **Paramètres de l'application** pour commencer à ajouter vos instances d'application. Vous pouvez accéder à cette page à tout moment à partir de **Réglages** > **Réglages de l'application.**

![Page "App Settings" pour le Upon Voyage US - Espace de travail avec un bouton pour ajouter une application.]({% image_buster /assets/img/workspaces/workspace_empty_state.png %})

### Étape 3 : Ajoutez vos instances d'application

Les différents sites et applications rassemblés au sein d'un espace de travail sont appelés des « instances d’applications ».

1. Dans la page **Paramètres de l'application**, sélectionnez **\+ Ajouter une application.**
2. Donnez un nom à votre instance d'application et sélectionnez la ou les plateformes sur lesquelles cette instance d'application est utilisée. Si vous sélectionnez plusieurs plateformes, Braze créera une instance d'application pour chaque plateforme.

![Fenêtre modale "Add New App to Upon Voyage US - Staging" avec des options pour sélectionner les détails de l'application.]({% image_buster /assets/img/workspaces/workspace_add_app.png %}){: style="max-width:60%" }

{:start="3"}
3\. Sélectionnez **Ajouter une application** pour confirmer.

#### Clés API de l'application

Après avoir ajouté votre instance d'application, vous aurez accès à sa clé API. La clé API est utilisée lors des requêtes entre votre instance d'application et l'API de Braze. La clé API est également importante pour l'intégration du SDK Braze à votre application ou à votre site Web.

![Page de réglages pour l'application iOS Upon Voyage avec des champs pour la clé API et l'endpoint SDK.]({% image_buster /assets/img/workspaces/app_api_key.png %})

{% alert note %}
Vous devez créer des instances d’application distinctes pour chaque version de votre application sur chaque plateforme. Par exemple, si vous avez des versions gratuite et pro de votre app sur iOS et Android, créez quatre instances d'app au sein de votre espace de travail (app iOS gratuite, app Android gratuite, app iOS pro et app Android pro). Cela vous donnera quatre clés API à utiliser, une pour chaque instance d’application.
{% endalert %}

#### Version du SDK en ligne/en production/instantané

La version du SDK affichée sur la page Paramètres des applications pour une application spécifique correspond à la version la plus élevée de l'application avec au moins 5 % de vos sessions quotidiennes totales et compte au moins 500 sessions au cours de la journée écoulée.

Ce champ apparaît une fois que vous avez intégré le SDK de Braze à votre application ou site web. Si une version plus récente du SDK Braze est disponible pour votre plateforme, elle sera notée ici avec l'étiquette « Une version plus récente est disponible ».

![La section "Version du SDK en ligne" contient la valeur "5.4.0" et une icône indiquant qu'une nouvelle version est disponible.]({% image_buster /assets/img/workspaces/app_live_sdk_version.png %})

### Étape 4 : Répétez l'opération si nécessaire

Répétez les étapes 2 et 3 pour configurer autant d'espaces de travail que votre plan le requiert. Comme meilleure pratique, nous vous recommandons de créer un espace de travail de test pour les tests d'intégration et de campagne.

{% alert tip %}
**Ajouter un espace de travail de test**<br>Vous pouvez également réaliser des tests d’applications mettant complètement en « sandbox » certains utilisateurs de votre instance de production. Créez un nouvel espace de travail et, lorsque vous publiez votre application, veillez à modifier la clé API utilisée par Braze pour qu'elle corresponde à celle de votre espace de travail de production plutôt qu'à celle de votre espace de travail de test.
{% endalert %}

## Gérer les espaces de travail

### Ajouter des favoris

Vous pouvez ajouter des espaces de travail favoris pour accéder encore plus rapidement aux espaces de travail que vous utilisez le plus.

![Espace de travail déroulant avec l'onglet "Espaces de travail favoris".]({% image_buster /assets/img/workspaces/workspace_favorites.png %}){: style="max-width:50%;"}

Pour ajouter des espaces de travail favoris :

1. Sélectionnez le menu déroulant de votre profil, puis sélectionnez **Gérer votre compte**.
2. Dans la section **Profil du compte**, localisez le champ **Espaces de travail favoris**.
3. Sélectionnez vos espaces de travail dans la liste.
4. Sélectionnez **Enregistrer les modifications**.

Il n'y a pas de limite au nombre d'espaces de travail que vous pouvez privilégier, mais nous vous recommandons de limiter cette liste pour plus de commodité.

### Renommer les espaces de travail

Pour renommer votre espace de travail :

1. Allez dans **Réglages** > **Réglages de l'application**.
2. Survolez le nom de votre espace de travail et sélectionnez <i class="image: /assets/img/braze_icons/pencil-01.svg" style="color: #0b8294;"></i>.
3. Donnez un nouveau nom à votre espace de travail, puis sélectionnez <i class="fa-solid fa-square-check" style="color: #0b8294;"></i> **Enregistrer**.

![L'icône du crayon apparaît à côté du nom de l'espace de travail.]({% image_buster /assets/img/workspaces/workspace_rename.gif %}){: style="max-width:50%;"}

### Suppression d'espaces de travail et d'instances d'applications

Pour supprimer votre espace de travail ou votre instance d'application :

1. Allez dans **Réglages** > **Réglages de l'application**.
2. Sélectionnez **Supprimer l'** espace de travail pour supprimer l'espace de travail correspondant, ou sélectionnez l'icône de la corbeille à côté de l'instance de l'application concernée.

Vous ne pouvez pas supprimer les instances d'app ou les espaces de travail qui sont actuellement utilisés pour le ciblage des utilisateurs ou qui comptent plus de 1 000 utilisateurs. Si vous essayez de le faire, vous recevrez un message d'erreur. Pour procéder et les supprimer, [créez un cas d'assistance]({{site.baseurl}}/user_guide/administrative/access_braze/support/) qui inclut un lien vers le tableau de bord et le nom de l'instance d'app ou de l'espace de travail à supprimer.

{% alert warning %}
Soyez prudent lorsque vous supprimez des espaces de travail ! Lorsqu'un espace de travail est supprimé, il ne peut plus être restauré.
{% endalert %}

![La page Paramètres de l'application avec un bouton pour supprimer un espace de travail et une icône de corbeille pour supprimer une application.]({% image_buster /assets/img/workspaces/workspace_delete.png %})

## Foire aux questions

### Dois-je créer un nouvel espace de travail lorsque je lance une nouvelle application ?

Cela dépend si vous mettez à jour votre application ou si vous en créez une entièrement nouvelle.

#### Mise à jour de votre application

Si vous mettez à jour votre application, vous devez séparer l'ancienne et la nouvelle version en créant une nouvelle instance d'application dans le même espace de travail. De cette façon, vous pouvez cibler uniquement les utilisateurs sur la nouvelle version en sélectionnant cette application au cours de la segmentation. Si vous souhaitez envoyer des messages aux utilisateurs qui sont sur l'ancienne version, vous pouvez utiliser des filtres pour [cibler la version précédente de l'application]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features#filtering-by-most-recent-app-versions).

Si vous créez un nouvel espace de travail, vos utilisateurs existeront à deux endroits : l'ancien espace de travail et le nouveau. Ils pourraient également avoir le même jeton de poussée. Les utilisateurs peuvent ainsi recevoir un message marketing destiné uniquement aux anciens utilisateurs de l'espace de travail, même s'ils ont déjà effectué une mise à niveau.

#### Lancement d'une nouvelle application

Si vous lancez une application entièrement nouvelle sur l'app store, vous devez créer un nouvel espace de travail. En créant un nouvel espace de travail, toutes les données historiques et les profils utilisateurs de l'ancienne version de l'application n'existeront pas dans ce nouvel espace de travail. Ainsi, lorsque les utilisateurs existants passeront à la nouvelle version de l'application, ils auront un nouveau profil créé sans aucune des données comportementales de l'ancienne application.

### J'ai plusieurs instances d'applications au sein d’un même espace de travail. Comment puis-je m'assurer que mon message ne cible qu'une seule application ? {#singular-app}

Pour vous assurer que votre message ne cible qu'une application spécifique, ajoutez un segment qui ne cible que les utilisateurs des instances de l'application que vous avez choisie. Ceci est particulièrement important si un utilisateur peut avoir deux jetons push pour différentes instances d'applications dans le même espace de travail. Dans ce cas, les utilisateurs peuvent recevoir une notification pour une application différente de celle sur laquelle ils se trouvent. Ce n'est pas une expérience idéale !

Par défaut, un segment cible toutes les applications et tous les sites Web de l'espace de travail. Pour mettre en place une segmentation qui ne cible qu'une appli ou un site web :

1. Créez un segment avec un nom significatif. Chez Braze, nous utilisons le format "Tous les utilisateurs ({Nom} {Plateforme})". Par exemple, "All Users (Upon Voyage iOS)".
2. Pour les **Apps et sites web ciblés**, sélectionnez les **utilisateurs d'apps spécifiques.**
3. Dans le menu déroulant **Applications spécifiques**, sélectionnez votre application ou votre site.

![Segmentation ciblant les utilisateurs d'applications spécifiques.]({% image_buster /assets/img/workspaces/users_from_specific_apps_filter.png %})

Vous pouvez ensuite ajouter ce segment à votre message et commencer à affiner votre audience avec d'autres segments et filtres si nécessaire.

#### Campagnes

Pour les campagnes, ajoutez votre segmentation à l'étape **Audiences cibles** du compositeur.

#### Canvas

Dans Canvas, ajoutez votre segment à vos étapes du message, dans la section **Validations de l'envoi**. Les validations des envois vérifient que votre audience répond à vos critères de réception au moment de l’envoi du message. N'oubliez pas de spécifier des validations de réception/distribution pour chaque étape du message afin de vous assurer qu'il sera livré à la bonne application. Il n'est pas nécessaire de segmenter au niveau de l'entrée.

{% details Développez les étapes du flux de travail Canvas d’origine %}

{% alert important %}
Depuis le 28 février 2023, vous ne pouvez plus créer ou dupliquer de Canvas à l’aide de l’éditeur Canvas d’origine. Ce contenu est disponible à titre de référence pour comprendre les segments et le ciblage dans l'éditeur d'origine.<br><br>Braze recommande aux clients qui utilisent l'expérience Canvas originale de cloner leurs Canvas vers l'éditeur mis à jour afin de mieux créer et gérer les Canvas. En savoir plus sur le [clonage de vos toiles]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

Dans le flux de travail original de Canvas, ajoutez votre segmentation au niveau du composant Canvas dans la section **Audience**. Il n'est pas nécessaire de segmenter au niveau de l'entrée.
{% enddetails %}


