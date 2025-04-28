---
nav_title: "Créer des pages d'atterrissage"
article_title: "Créer des pages d'atterrissage"
description: "Cet article explique comment créer et personnaliser les pages d'atterrissage de Braze à l'aide de l'éditeur par glisser-déposer."
page_order: 0
---

# Créer des pages d'atterrissage

> Apprenez à créer et à personnaliser une page d'atterrissage à l'aide de l'éditeur par glisser-déposer, afin de développer votre audience et de recueillir vos préférences directement dans Braze.

## Création d'une page d'atterrissage

### Étape 1 : Créer un nouveau projet

Accédez à l'option **Messages** > **Pages d'atterrissage**, puis sélectionnez **Créer une page d'atterrissage**. Vous pouvez également cliquer sur le nom d'une page d'atterrissage existante pour la dupliquer ou la modifier.

![La section des pages d'atterrissage dans le bord de Braze.]({% image_buster /assets/img/landing_pages/landing-pages-homepage.png %})

### Étape 2 : Entrez les détails de la page

#### Informations générales

Le nom et la description de la page de destination sont utilisés pour rechercher la page dans votre espace de travail interne. Celles-ci ne seront pas visibles pour vos clients.

#### Détails du site

Mettez en place des métatags pour personnaliser l'affichage de votre page dans l'onglet du navigateur et l'optimiser pour les résultats des moteurs de recherche. Celles-ci seront visibles par vos clients.

Nous vous suggérons de suivre ces bonnes pratiques :

| Détail | Description | Recommandations |
| --- | --- |
| Titre du site | Le titre qui s'affiche sur l'onglet du navigateur. | Utilisez jusqu'à 60 caractères. |
| Meta description | Un extrait de code qui s'affiche dans les résultats de recherche. | Utilisez entre 140 et 160 caractères.|
| Favicon | L'icône qui apparaît à côté du titre du site dans l'onglet du navigateur. | Utilisez un rapport hauteur/largeur de 1:1 et un type de fichier pris en charge (PNG, JPEG ou ICO). |
| URL de la page | Il s'agit du chemin URL vers votre page d'atterrissage. Cette valeur est également référencée lors de l'utilisation des [étiquettes Liquid de la page d'atterrissage]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users) que vous pouvez intégrer dans un message afin de les identifier automatiquement lorsqu'ils soumettent votre formulaire.| Cette valeur doit être unique dans votre espace de travail. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Étape 3 : Personnaliser la page

Si vous ne l'avez pas encore fait, sélectionnez **Enregistrer comme brouillon**. Pour commencer à personnaliser votre page, sélectionnez **Modifier la page d'atterrissage**. L'éditeur par glisser-déposer est préchargé avec un modèle par défaut que vous pouvez personnaliser pour l'adapter à votre cas d'utilisation.

![Exemple de page d'atterrissage créée dans l'éditeur par glisser-déposer.]({% image_buster /assets/img/landing_pages/template.png %})

L'éditeur utilise deux types de composants pour la composition des pages d'atterrissage : les [blocs de base](#basic-blocks) et les [blocs de formulaire](#form-blocks). Tous les blocs doivent être placés dans une ligne.

![La section "Créer" contient des "rangées" et des "blocs de formulaires".]({% image_buster /assets/img/landing_pages/dnd.png %}){: style="max-width:35%;"}

#### Blocs de base

Vous pouvez utiliser ces blocs pour ajouter du contenu et personnaliser la mise en page de votre page de destination.

| Type de bloc   | Description |
|-------------|-------------|
| Titre       | Bloc de contenu permettant d'ajouter un titre ou une rubrique à votre contenu. Utile pour structurer les sections et améliorer la lisibilité. |
| Paragraphe   | Un bloc de texte pour des descriptions plus longues ou un contexte supplémentaire. Prise en charge de la mise en forme de texte enrichi. |
| Bouton      | Un élément cliquable qui dirige les utilisateurs vers une action spécifique, telle que l'ouverture d'un lien ou la soumission d'un formulaire. |
| Image       | Un bloc pour afficher des images. Vous pouvez télécharger une image ou fournir une URL pour faire référence à une source externe. |
| Lien        | Lien hypertexte sur lequel les utilisateurs peuvent cliquer pour se rendre à une URL spécifiée. Ils peuvent être intégrés dans un texte ou être autonomes. |
| Espaceur      | Un bloc invisible qui ajoute un espacement vertical entre les éléments pour améliorer la mise en page et la lisibilité. |
| Code personnalisé | Un bloc qui vous permet d'insérer et d'exécuter du HTML, du CSS ou du JavaScript personnalisés pour une personnalisation avancée. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Blocs de formulaires

Vous pouvez utiliser ces blocs pour créer un formulaire qui relie les données soumises par l'utilisateur à son profil dans Braze. Gardez à l'esprit que si vous utilisez des blocs de formulaire, vous devrez également créer une page d'atterrissage supplémentaire pour l'état de confirmation.

![Un bloc de formulaire qui enregistre un nouveau client et lui envoie un code de réduction par e-mail.]({% image_buster /assets/img/landing_pages/form.png %}){: style="max-width:70%;"}

| Type de bloc     | Description |
|---------------|-------------|
| Capture d’adresses e-mail | Un champ de formulaire pour les adresses e-mail. Une fois soumise, l'adresse e-mail est ajoutée au profil de l'utilisateur dans Braze. |
| Capture de numéros de téléphone | Un champ de formulaire pour les numéros de téléphone. Une fois soumis, l'utilisateur est abonné à votre groupe d'abonnement SMS ou WhatsApp. |
| Champ de saisie   | Un champ de formulaire qui prend en charge les attributs standard (tels que le prénom et le nom) ou une chaîne de caractères personnalisée de votre choix. |
| Liste déroulante      | Les utilisateurs peuvent sélectionner un élément dans une liste prédéfinie. Vous pouvez ajouter à la liste des chaînes d'attributs personnalisés. |
| Case à cocher      | Si l'utilisateur coche la case, l'attribut du bloc est fixé à `true`. S'il n'est pas coché, son attribut est fixé à `false`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Après avoir créé une page d'atterrissage avec un formulaire, veillez à intégrer son [étiquette Liquid de page d'atterrissage]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users) dans votre message. Grâce à cette étiquette, Braze peut automatiquement identifier et mettre à jour les profils utilisateurs existants lorsqu'ils soumettent le formulaire.
{% endalert %}

#### Styles de conteneur de page

Vous pouvez définir des styles à appliquer à tous les blocs de composants pertinents de votre page d'atterrissage à partir de l'onglet **Conteneur de page**. Ces styles seront utilisés partout sur votre page, sauf si vous les remplacez par un bloc spécifique.

Nous vous recommandons de définir les styles au niveau du conteneur de la page avant de personnaliser les styles au niveau du bloc. Vous pouvez également ajouter une image de fond pour l'ensemble de la page.

![La section "Conteneur de page" contient des options permettant de personnaliser les images d'arrière-plan, les couleurs, les détails des bordures et le style personnalisé du contenu.]({% image_buster /assets/img/landing_pages/page_container.png %}){: style="max-width:30%;"}

### Étape 4 : Créer une page de confirmation

Si vous avez ajouté un [formulaire](#form-block) à votre page de destination à l'étape précédente, créez une page de destination supplémentaire pour l'état de confirmation, puis ajoutez le lien **Open web URL** au bouton qui soumet le formulaire. Sinon, passez à l'étape suivante.

### Étape 5 : Prévisualiser la page

Vous pouvez prévisualiser votre page d'atterrissage dans l'onglet **Aperçu de** l'éditeur. Après avoir enregistré votre page d'atterrissage en tant que brouillon, vous pouvez visiter l'URL en allant dans **Pages d'atterrissage** et en sélectionnant **Copier l'URL** à côté de votre page d'atterrissage. Vous pouvez également partager l'URL avec des collaborateurs.

![Une page d'atterrissage avec le menu ouvert pour montrer l'option "Copier l'URL".]({% image_buster /assets/img/landing_pages/copy-url.png %})

Lorsque vous êtes prêt, sélectionnez **Publier la page d'atterrissage**.

## Traitement des erreurs de soumission de formulaire

Si un utilisateur saisit une valeur de formulaire non valide (comme des caractères spéciaux non acceptés), il verra un indicateur d'erreur générique qui n'est pas personnalisable et ne pourra pas soumettre le formulaire. Vous pouvez voir le comportement de l'erreur dans l'aperçu de la page d'atterrissage.

## Afficher les analyses

Pour analyser l'efficacité de votre page d'atterrissage, allez dans **Messagerie** > **Pages d'atterrissage**, puis sélectionnez une page d'atterrissage que vous avez publiée. Ici, vous pouvez suivre le nombre de pages vues, de clics sur les pages, de soumissions de pages et les taux de soumission pour votre page d'atterrissage.

![La section analyse/analytique d'une page d'atterrissage.]({% image_buster /assets/img/landing_pages/analytics.png %})
