---
nav\_title : Créer des pages d'atterrissage article\_title : Création de pages d'atterrissage (Landing Pages) description : "Cet article explique comment créer et personnaliser des pages d'atterrissage Braze à l'aide de l'éditeur glisser-déposer" page\_order : 0
---

# Créer des pages d'atterrissage

> Apprenez à créer et à personnaliser une page d'atterrissage à l'aide de l'éditeur par glisser-déposer, afin de développer votre audience et de recueillir vos préférences directement dans Braze.

## Création d'une page d'atterrissage

### Étape 1 : Créer un nouveau projet

Accédez à l'option **Messages** > **Pages d'atterrissage**, puis sélectionnez **Créer une page d'atterrissage**. Vous pouvez également cliquer sur le nom d'une page d'atterrissage existante pour la dupliquer ou la modifier.

\![La section des pages d'atterrissage dans le tableau de bord de Braze.\]({% image\_buster /assets/img/landing\_pages/landing-pages-homepage.png %})

### Étape 2 : Entrez les détails de la page

#### Informations générales

Le nom et la description de la page de destination sont utilisés pour rechercher la page dans votre espace de travail interne. Celles-ci ne seront pas visibles pour vos clients.

#### Détails du site

Mettez en place des métatags pour personnaliser l'affichage de votre page dans l'onglet du navigateur et l'optimiser pour les résultats des moteurs de recherche. Celles-ci seront visibles par vos clients.

Nous vous suggérons de suivre ces bonnes pratiques :

| Détail | Description | Recommandations | --- | | | Titre du site | Le titre qui s'affiche sur l'onglet du navigateur. | Utilisez jusqu'à 60 caractères. | Meta description | Extrait de code qui s'affiche dans les résultats de recherche. | Utilisez entre 140 et 160 caractères. | | Favicon | L'icône qui apparaît à côté du titre du site sur l'onglet du navigateur. | Utilisez un rapport hauteur/largeur de 1:1 et un type de fichier pris en charge (PNG, JPEG ou ICO). | L'URL est le lien sur lequel les utilisateurs cliqueront pour se rendre sur votre page de destination. Ce lien est également utilisé pour générer des [étiquettes Liquid de la page d'atterrissage]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users) que vous pouvez intégrer dans un message pour les identifier automatiquement lorsqu'ils soumettent votre formulaire.| Cette poignée doit être unique. Ce lien est également utilisé pour générer des balises liquides de page d'atterrissage qui sont incorporées dans le message afin d'identifier automatiquement les personnes qui soumettent votre formulaire.| { : .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Étape 3 : Personnaliser la page

Si vous ne l'avez pas encore fait, sélectionnez **Enregistrer comme brouillon**. Pour commencer à personnaliser votre page, sélectionnez **Modifier la page d'atterrissage**. L'éditeur par glisser-déposer est préchargé avec un modèle par défaut que vous pouvez personnaliser pour l'adapter à votre cas d'utilisation.

\![Un exemple de page d'atterrissage créée dans l'éditeur glisser-déposer\]({% image\_buster /assets/img/landing\_pages/template.png %})

L'éditeur utilise deux types de composants pour la composition des pages d'atterrissage : les [blocs de base](#basic-blocks) et les [blocs de formulaire](#form-blocks). Tous les blocs doivent être placés dans une ligne.

\![La section 'Créer' contenant les 'Lignes' et les 'Blocs de formulaires'.\]({% image\_buster /assets/img/landing\_pages/dnd.png %}){ : style="max-width:35% ;"}

#### Blocs de base

Vous pouvez utiliser ces blocs pour ajouter du contenu et personnaliser la mise en page de votre page de destination.

| Type de bloc | Description | |-------------|-------------| | Titre | Un bloc de texte permettant d'ajouter un titre ou une rubrique à votre contenu. Utile pour structurer les sections et améliorer la lisibilité. | Paragraphe | Bloc de texte pour des descriptions plus longues ou un contexte supplémentaire. Prend en charge la mise en forme de texte riche. | Bouton - Un élément cliquable qui dirige les utilisateurs vers une action spécifique, telle que l'ouverture d'un lien ou la soumission d'un formulaire. | Image - Bloc permettant l'affichage d'images. Vous pouvez télécharger une image ou fournir une URL pour référencer une source externe. | Vous pouvez télécharger une image ou fournir une URL pour faire référence à une source externe. Il peut être incorporé dans un texte ou être autonome. | Bloc invisible qui ajoute un espacement vertical entre les éléments afin d'améliorer la mise en page et la lisibilité. | Code personnalisé - Un bloc qui vous permet d'insérer et d'exécuter des codes HTML, CSS ou JavaScript personnalisés pour une personnalisation avancée. | { : .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Blocs de formulaires

Vous pouvez utiliser ces blocs pour créer un formulaire qui relie les données soumises par l'utilisateur à son profil dans Braze. Gardez à l'esprit que si vous utilisez des blocs de formulaire, vous devrez également créer une page d'atterrissage supplémentaire pour l'état de confirmation.

\![Un bloc de formulaire qui enregistre un nouveau client et lui envoie un code de réduction par e-mail\]({% image\_buster /assets/img/landing\_pages/form.png %}){ : style="max-width:70% ;"}

| Capture d'e-mail | Un champ de formulaire pour les adresses e-mail. Une fois soumise, l'adresse e-mail est ajoutée au profil de l'utilisateur dans Braze. | Capture d'un numéro de téléphone | Un champ de formulaire pour les numéros de téléphone. Lorsqu'il est soumis, l'utilisateur est abonné à votre groupe d'abonnement SMS ou Whatsapp. | Champ de saisie - Un champ de formulaire qui prend en charge les attributs standard (tels que le prénom et le nom) ou une chaîne d'attributs personnalisée de votre choix. | Champ de saisie : champ de formulaire qui prend en charge les attributs standard (tels que le prénom et le nom de famille) ou une chaîne d'attributs personnalisée de votre choix. Vous pouvez ajouter toute chaîne d'attribut personnalisé à la liste. | Si un utilisateur coche la case, l'attribut du bloc est défini comme `vrai`. S'il n'est pas coché, son attribut est défini comme `faux`. | : .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %} Après avoir créé une page d'atterrissage avec un formulaire, veillez à intégrer son [étiquette Liquid de page d'atterrissage]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users) dans votre message. Grâce à cette étiquette, Braze peut automatiquement identifier et mettre à jour les profils utilisateurs existants lorsqu'ils soumettent le formulaire. {% endalert %}

#### Styles de conteneur de page

Vous pouvez définir des styles à appliquer à tous les blocs de composants pertinents de votre page d'atterrissage à partir de l'onglet **Conteneur de page.**  Ces styles seront utilisés partout sur votre page, sauf si vous les remplacez par un bloc spécifique.

Nous vous recommandons de définir les styles au niveau du conteneur de la page avant de personnaliser les styles au niveau du bloc. Vous pouvez également ajouter une image de fond pour l'ensemble de la page.

\![La section 'Conteneur de page' avec des options pour personnaliser les images d'arrière-plan, les couleurs, les détails de la bordure et le style du contenu.\]({% image\_buster /assets/img/landing\_pages/page\_container.png %}){ : style="max-width:30% ;"}

### Étape 4 : Créer une page de confirmation

Si vous avez ajouté un [formulaire](#form-block) à votre page de destination à l'étape précédente, créez une page de destination supplémentaire pour l'état de confirmation, puis ajoutez le lien **Open web URL** au bouton qui soumet le formulaire. Sinon, passez à l'étape suivante.

### Étape 5 : Prévisualiser la page

Vous pouvez prévisualiser votre page d'atterrissage dans l'onglet **Aperçu de** l'éditeur. Après avoir enregistré votre page d'atterrissage en tant que brouillon, vous pouvez visiter l'URL en allant dans **Pages d'atterrissage** et en sélectionnant **Copier l'URL** à côté de votre page d'atterrissage. Vous pouvez également partager l'URL avec des collaborateurs.

Une page d'atterrissage avec le menu ouvert pour montrer l'option "Copier l'URL"\]({% image\_buster /assets/img/landing\_pages/copy-url.png %})

Lorsque vous êtes prêt, sélectionnez **Publier la page d'atterrissage**.

## Traitement des erreurs de soumission de formulaire

Si un utilisateur saisit une valeur de formulaire non valide (comme des caractères spéciaux non acceptés), il verra un indicateur d'erreur générique qui n'est pas personnalisable et ne pourra pas soumettre le formulaire. Vous pouvez voir le comportement de l'erreur dans l'aperçu de la page d'atterrissage.

## Afficher les analyses

Pour analyser l'efficacité de votre page d'atterrissage, allez dans **Messagerie** > **Pages d'atterrissage**, puis sélectionnez une page d'atterrissage que vous avez publiée. Ici, vous pouvez suivre le nombre de pages vues, de clics sur les pages, de soumissions de pages et les taux de soumission pour votre page d'atterrissage.

\![La section analyse d'une page d'atterrissage.\]({% image\_buster /assets/img/landing\_pages/analytics.png %})
