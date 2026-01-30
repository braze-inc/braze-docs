---
nav_title: Le tableau de bord
article_title: Le tableau de bord de Braze
page_order: 2
page_type: reference
description: "Le tableau de bord de Braze est votre espace de travail central pour créer, gérer et analyser l'engagement client. Il rassemble en un seul endroit des outils de messages, des informations sur l'audience, la segmentation et des données en temps réel sur les performances."

---

# Le tableau de bord de Braze

> Le tableau de bord de Braze est notre interface web à l'adresse suivante [dashboard.braze.com](https://dashboard.braze.com/) ou [dashboard.braze.eu](https://dashboard.braze.eu/)

Utilisez le tableau de bord de Braze pour planifier des campagnes, lancer et gérer des messages, explorer les informations sur l'audience, ajuster la segmentation et examiner les indicateurs de performance et d'engagement en temps réel à partir d'une interface unique.

## Accédez à votre tableau de bord

Pour commencer, [connectez-vous à votre compte Braze]({{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account). Votre accès aux pages du tableau de bord et la permission d'effectuer certaines actions sont basés sur les [autorisations d'utilisateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) qui vous ont été attribuées. Si vous avez besoin d'aide concernant vos autorisations, contactez vos administrateurs Braze.

## Naviguer dans Braze

La navigation dans Braze est conçue pour vous aider à accéder efficacement aux fonctionnalités et au contenu sur tous les appareils. Le tableau de bord de Braze comporte deux niveaux de navigation : l'en-tête global et la navigation latérale.

L'en-tête global est presque toujours visible en haut de l'écran. Il permet d'accéder rapidement aux outils et paramètres essentiels, notamment

- Rechercher
- Soutien et liens avec la communauté
- [Langue du tableau de bord]({{site.baseurl}}/user_guide/administrative/access_braze/language/)
- Notifications
- Paramètres du compte
- [BrazeAI Operator™]({{site.baseurl}}/user_guide/brazeai/operator/)

### Utiliser la navigation latérale

Le menu vertical de gauche organise les outils Braze par fonction et permet de garder à portée de main vos articles les plus utilisés. Sélectionnez un élément du menu principal pour faire apparaître ses options dans une présentation verticale empilée. 

![Changement d'espace de travail dans le tableau de bord de Braze]({% image_buster /assets/img/workspace_switcher.png %}){: style="max-width:35%;float:right;margin-left:15px"}

#### Commutateur d'espace de travail

Situé en haut de la navigation latérale, le sélecteur d'espace de travail vous permet de passer d'un espace de travail à l'autre dans votre instance Braze. L'espace de travail actif est mis en évidence.

Les [espaces de travail]({{site.baseurl}}/user_guide/getting_started/workspaces) permettent d'organiser le contenu par marque, région, ligne de produits ou équipe. Chaque espace de travail comprend ses propres données, campagnes et paramètres. Votre accès peut varier d'un espace de travail à l'autre. Par exemple, vous pouvez avoir un accès en modification dans un espace de travail et un accès en consultation seule dans un autre.

#### Minimiser la navigation latérale

Pour réduire l'encombrement visuel, notamment lors de tâches telles que la conception d'un canvas, vous pouvez réduire le panneau de navigation latéral. Appuyez sur le **menu Minimiser** pour la réduire. Même lorsqu'elle est réduite, survolez n'importe quelle icône pour afficher des infobulles avec les noms des éléments du menu. Cela vous permet de passer rapidement d'un outil à l'autre tout en gardant votre espace de travail propre.

![Minimiser et maximiser les icônes de menu]({% image_buster /assets/img/minimize_expand_menu.png %}){: style="max-width:60%;border:none"}

#### Navigation réactive

La navigation s'adapte de façon fluide/sans heurts à différentes tailles d'écran. Sur les petits écrans, la navigation latérale se réduit automatiquement. Appuyez sur <i class="fa-solid fa-bars" aria-label="Ouvrir le menu de navigation"></i> pour ouvrir le menu en cas de besoin. 

![Sur les petits écrans, la navigation latérale se réduit automatiquement. Le fait d'appuyer sur l'icône de menu ouvre les options de navigation.]({% image_buster /assets/img/navigation/navigation_small_screens.png %}){: style="max-width: 80%;border:none"}

## Recherche dans votre tableau de bord

La barre de recherche globale, située dans l'emplacement/localisation, est le moyen le plus rapide de trouver du contenu dans l'ensemble de votre tableau de bord Braze. Sélectionnez cette option pour ouvrir l'interface de recherche et accéder directement à ce dont vous avez besoin. 

![Recherche globale ouverte sans aucun terme de recherche, affichant les pages récemment ouvertes.]({% image_buster /assets/img/navigation/search_recently_opened.png %})

Votre contenu récemment ouvert apparaît sous la barre de recherche. Cela inclut toutes les campagnes, Canvas, modèles ou pages avec lesquels vous avez récemment interagi, ce qui vous permet de revenir facilement à votre travail.

### Que pouvez-vous rechercher ?

Vous pouvez rechercher les éléments et actions suivants :

- Noms de campagne
- Noms de toiles
- Blocs de contenu
- Noms de segments
- Noms de modèles d'e-mails
- Pages au sein de Braze (y compris les synonymes)

{% alert tip %}
Pour rechercher un texte exact, placez votre terme de recherche entre guillemets (« »). Par exemple, la recherche de ["tous les utilisateurs"] renverra tous les éléments contenant l'expression exacte "tous les utilisateurs" dans leur nom.
{% endalert %}

### Balises de type de contenu et de statut

Chaque résultat est étiqueté avec une étiquette indiquant son type de contenu (campagne, Canvas ou segment) et son statut (actif, archivé, arrêté).

### Filtrer le contenu actif et brouillon

Par défaut, la recherche inclut les éléments actifs, les brouillons et les éléments archivés. Utilisez la bascule **Afficher les actifs et les brouillons uniquement** pour affiner vos résultats.

![Le bouton bascule « Afficher uniquement les actifs et les brouillons ».]({% image_buster /assets/img/navigation/show_active_draft_new.png %})

### Raccourcis clavier

Vous pouvez vous déplacer dans les résultats de la recherche à l'aide de votre clavier.

<style>
  div.small_table + table {
    max-width: 60%;
  }
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2), {
    width:20%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

| Action                      | Raccourci clavier                                                             |
| --------------------------- | ----------------------------------------------------------------------------- |
| Ouvrir le menu de recherche        | {::nomarkdown} <ul> <li> Mac : <kbd>⌘</kbd> + <kbd>K</kbd> </li> <li>Windows : <kbd>Ctrl</kbd> + <kbd>K</kbd> </li> </ul> {:/}  |
| Déplacer entre les résultats de recherche | <kbd>⬆</kbd> / <kbd>⬇</kbd>  |
| Sélectionnez un résultat de recherche      | <kbd>Entrer</kbd>    |
| Fermez le menu de recherche       | <kbd>Éch</kbd>  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


## L'accessibilité dans le tableau de bord

Le tableau de bord de Braze utilise des couleurs de marque qui répondent aux normes WCAG AA en matière de contraste des couleurs. Cela favorise une expérience inclusive pour tous les utilisateurs et s'aligne sur les meilleures pratiques en matière d'accessibilité.

## Partager le retour d'expérience

Vous voulez nous dire ce que vous en pensez ? Vous pouvez faire part de vos commentaires sur la navigation, l'accessibilité, la convivialité, la conception visuelle, etc. Ouvrez le menu **Support** dans l'en-tête global et sélectionnez **Partager le feedback.** Nous examinons tous les commentaires afin d'améliorer votre expérience de Braze.


