## Utilisation des blocs éditeurs de messages in-app

Les blocs éditeurs sont situés sous la section **Créer** pour les messages in-app. Pour les utiliser, faites glisser un bloc éditeur dans une colonne. Il s’ajuste automatiquement à la largeur de la colonne. Chaque bloc éditeur possède ses propres paramètres, tels que le contrôle granulaire sur la marge intérieure. Le panneau latéral droit passe automatiquement à un panneau de propriétés pour l’élément de contenu sélectionné.

## Types

Le tableau suivant décrit comment vous pouvez exploiter chaque type de bloc éditeur.

| Nom | Description |
| --- | --- |
| Titre | Permet d'insérer un titre dans le message. |
| Paragraphe | Permet d'insérer un paragraphe dans le message. |
| Bouton | Ajoute un bouton standard. Les propriétés de ce bloc permettent de modifier, de configurer les liens et enregistrer les analyses. |
| Bouton radio | Ajoute une liste d'options parmi lesquelles les utilisateurs peuvent choisir. Lorsqu'il est soumis, le profil utilisateur enregistre l'attribut personnalisé associé. |
| Image | Insère une image de la [bibliothèque multimédia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). |
| Lien | Insère un lien hypertexte sur lequel les utilisateurs peuvent cliquer pour naviguer vers une URL spécifiée. Ils peuvent être intégrés dans un texte ou être autonomes. |
| Espaceur | Ajoute de l’espace ou une marge intérieure entre les autres blocs. |
| Code personnalisé | Insère et exécute des fichiers HTML, CSS ou JavaScript personnalisés pour une personnalisation avancée.  |
| Capture de numéros de téléphone | Insère un champ de formulaire pour les numéros de téléphone. Lorsqu'il est soumis, l'utilisateur est abonné au [groupe d'abonnement]({{site.baseurl}}/whatsapp_subscription_groups/) [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) ou [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/). |
| Capture d’adresses e-mail | Insère un champ de formulaire pour les adresses e-mail. Une fois soumise, l'adresse e-mail est ajoutée au profil de l'utilisateur dans Braze. |
| Liste déroulante      | Insère une liste déroulante avec une liste prédéfinie d'éléments parmi lesquels les utilisateurs peuvent en sélectionner un. Vous pouvez ajouter à la liste des chaînes d'attributs personnalisés. |
| Case à cocher      | Insère une case à cocher. Si l'utilisateur coche la case, l'attribut du bloc est fixé à `true`. S'il n'est pas coché, son attribut est fixé à `false`. |
| Groupe de cases à cocher| Les utilisateurs peuvent choisir parmi plusieurs options présentées. Les valeurs sont soit définies, soit ajoutées à un tableau défini d'attributs personnalisés. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Propriétés

Les détails des propriétés de chaque bloc éditeur sont fournis dans les tableaux suivants.

### Titre et paragraphe

| Propriété | Description |
| --- | --- |
| Famille de polices | Le style de police du texte |
| Poids de la police | Détermine l'épaisseur du texte |
| Taille de police | Détermine la taille du texte |
| Hauteur de ligne | Modifie l’espace entre les lignes de texte |
| Espacement des lettres | Modifie l’espace entre chaque caractère |
| Alignement du texte | Déplace le texte pour l’aligner à gauche, au centre, à droite ou le justifier |
| Couleur du texte | Modifie la couleur du texte |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Bouton

| Propriété | Description |
| --- | --- |
| Largeur du bouton | Modifie la largeur du bouton pour qu'il soit automatique ou manuel |
| Famille de polices | Il s'agit du style de police du texte |
| Poids de la police | Détermine l'épaisseur du texte |
| Taille de police | Détermine la taille du texte |
| Espacement des lettres | Modifie l’espace entre chaque caractère |
| Alignement du bouton | Déplace le bouton vers la gauche, le centre ou la droite. |
| Couleur de texte de bouton | Modifie la couleur du texte sur le bouton |
| Couleur d’arrière-plan | Modifie la couleur de l'arrière-plan du bouton |
| Style de bordure | Détermine le style de la bordure du bouton | 
| Rayon de bordure | Détermine à quel point vous désirez que vos coins soient arrondis |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Image

| Propriété | Description |
| --- | --- |
| URL | L'adresse hébergée de l'image |
| Alignement | Déplace l'image vers la gauche, le centre ou la droite. |
| Couleur d’arrière-plan | Modifie la couleur de l'arrière-plan de l'image |
| Style de bordure | Détermine le style de la bordure de l'image | 
| Rayon de bordure | Détermine le degré d'arrondi des coins de l'image. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Lien

| Propriété | Description |
| --- | --- |
| Famille de polices | Il s'agit du style de police du texte |
| Poids de la police | Détermine l'épaisseur du texte |
| Espacement des lettres | Modifie l’espace entre chaque caractère |
| Couleur du texte | Modifie la couleur du texte |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Espaceur

| Propriété | Description |
| --- | --- |
| Couleur d’arrière-plan | Modifie la couleur d’arrière-plan de l’espaceur |
| Hauteur | Modifie la hauteur de l’espaceur. Vous pouvez également modifier cela à l’aide des poignées de redimensionnement de l’espaceur. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Code personnalisé

| Propriété | Description |
| --- | --- |
| Code personnalisé | Permet d'ajouter, de modifier ou de supprimer des éléments HTML, CSS et JavaScript pour un message in-app. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Capture du téléphone

| Propriété | Description |
| --- | --- |
| Groupe d’abonnement | Le [groupe d']({{site.baseurl}}/whatsapp_subscription_groups/) abonnement [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) ou [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/) auquel l'utilisateur sera abonné en collectant son numéro de téléphone, avec une option permettant de collecter les numéros de tous les pays. |
| Alignement du texte | Déplace le texte pour l’aligner à gauche, au centre, à droite ou le justifier |
| Texte de la marque substitutive | Un numéro de téléphone marque substitutive à afficher |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Capture d’adresses e-mail

| Propriété | Description |
| --- | --- |
| Famille de polices | Le style de police du texte |
| Poids de la police | Détermine l'épaisseur du texte |
| Taille de police | Détermine la taille du texte |
| Hauteur de ligne | Modifie l’espace entre les lignes de texte |
| Couleur du texte | Modifie la couleur du texte |
| Espacement des lettres | Modifie l’espace entre chaque caractère |
| Alignement du texte | Déplace le texte pour l’aligner à gauche, au centre, à droite ou le justifier |
| Texte de la marque substitutive | Une adresse e-mail marque substitutive à afficher |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Actions

Vous pouvez assigner une action qui se produit lorsque l'utilisateur appuie sur un bouton, un lien ou une image dans le message. Vous pouvez également utiliser [Liquid]({{site.baseurl}}/liquid/) pour personnaliser les actions. Les tableaux suivants détaillent les actions de chaque bloc éditeur.

### Bouton

| Action | Description |
| --- | --- |
| Envoyer le formulaire lors d’un clic sur le bouton | Soumet le formulaire et exécute le comportement sélectionné lors du clic. Désactivez cette option pour uniquement réaliser l’action associée au clic. |
| Définissez des comportements distincts pour chaque plateforme | Personnalise le comportement des clients pour chaque plateforme séparément. |
| Comportement lors du clic | Détermine l'action lorsque l'utilisateur clique sur le bouton, comme la fermeture du message, l'ouverture de l'URL web, le lien profond vers une page spécifique de l'appli, l'accès à une autre page ou la [demande d'une autorisation push]({{site.baseurl}}/push_primer/). |
| Enregistrer des attributs ou événements personnalisés | Détermine si le fait de cliquer sur le bouton mettra à jour le profil de l'utilisateur avec des données personnalisées. Vous pouvez également sélectionner l'identifiant pour le rapport. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Image

Pour les [spécifications des images]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/image_specs/#in-app-messages), reportez-vous à nos [spécifications des images des messages in-app]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/image_specs/#in-app-messages).

| Action | Description |
| --- | --- |
| Texte alternatif | La copie écrite qui apparaît à la place d’une image si l’image ne se charge pas. Les lecteurs d'écran annoncent un texte alt pour expliquer les images. Utilisez donc un langage simple pour fournir des informations clés sur une image. |
| Envoyer le formulaire lors d’un clic sur l’image | Soumet le formulaire et exécute le comportement sélectionné lors du clic. Désactivez cette option pour uniquement réaliser l’action associée au clic. |
| Définissez des comportements distincts pour chaque plateforme | Personnalise le comportement des clients pour chaque plateforme séparément. |
| Comportement lors du clic | Détermine l'action lorsque l'utilisateur clique sur l'image, comme la fermeture du message, l'ouverture de l'URL web, le lien profond vers une page spécifique de l'appli, l'accès à une autre page ou la [demande d'autorisation push.]({{site.baseurl}}/push_primer/) |
| Enregistrer des attributs ou événements personnalisés | Détermine si le fait de cliquer sur l'image mettra à jour le profil de l'utilisateur avec des données personnalisées. Vous pouvez également sélectionner l'identifiant pour le rapport. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Lien

| Action | Description |
| --- | --- |
| URL | Le lien hypertexte vers lequel naviguer |
| Identifiant de signalement | Détermine l'identifiant utilisé pour les rapports |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

