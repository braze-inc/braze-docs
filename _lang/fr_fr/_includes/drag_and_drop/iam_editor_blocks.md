## Utilisation des blocs éditeurs de messages in-app

Les blocs éditeurs se trouvent dans la section **Créer** pour les messages in-app. Pour les utiliser, faites glisser un bloc éditeur dans une colonne. Il s'ajuste automatiquement à la largeur de la colonne. Chaque bloc éditeur possède ses propres paramètres, comme le contrôle granulaire de la marge intérieure. Le panneau latéral droit bascule automatiquement vers un panneau de propriétés correspondant à l'élément de contenu sélectionné.

## Types

Le tableau suivant décrit comment exploiter chaque type de bloc éditeur.

| Nom | Description |
| --- | --- |
| Titre | Permet d'insérer un titre dans le message. |
| Paragraphe | Permet d'insérer un paragraphe dans le message. |
| Bouton | Ajoute un bouton standard. Les propriétés de ce bloc permettent de modifier le texte, de configurer les liens et d'enregistrer les analyses. |
| Bouton radio | Ajoute une liste d'options parmi lesquelles les utilisateurs peuvent en choisir une. Lors de l'envoi du formulaire, le profil utilisateur enregistre l'attribut personnalisé associé, qui doit être une chaîne de caractères pour être sauvegardé. Les attributs personnalisés avec d'autres types de données ne sont pas enregistrés dans le profil utilisateur. |
| Image | Insère une image provenant de la [bibliothèque multimédia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). |
| Lien | Insère un lien hypertexte sur lequel les utilisateurs peuvent cliquer pour accéder à une URL spécifiée. Il peut être intégré dans un texte ou utilisé de manière autonome. |
| Espaceur | Ajoute de l'espace ou une marge intérieure entre les autres blocs. |
| Code personnalisé | Insère et exécute du code HTML, CSS ou JavaScript personnalisé pour une personnalisation avancée.  |
| Capture de numéros de téléphone | Insère un champ de formulaire pour les numéros de téléphone. Une fois le formulaire envoyé, l'utilisateur est abonné au groupe d'abonnement [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) ou [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/). |
| Capture d'adresses e-mail | Insère un champ de formulaire pour les adresses e-mail. Une fois le formulaire envoyé, l'adresse e-mail est ajoutée au profil de l'utilisateur dans Braze. |
| Texte court    | Insère un champ de formulaire prenant en charge les attributs standard (tels que le prénom et le nom) ou une chaîne de caractères d'attribut personnalisé de votre choix. |
| Liste déroulante      | Insère une liste déroulante avec une liste prédéfinie d'éléments parmi lesquels les utilisateurs peuvent en sélectionner un. Vous pouvez ajouter à la liste des chaînes de caractères d'attributs personnalisés. |
| Case à cocher      | Insère une case à cocher. Si l'utilisateur coche la case, l'attribut du bloc est défini sur `true`. Si la case reste décochée, l'attribut est défini sur `false`. |
| Groupe de cases à cocher| Les utilisateurs peuvent choisir parmi plusieurs options proposées. Les valeurs sont soit définies, soit ajoutées à un attribut personnalisé de type tableau. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Propriétés

Les détails des propriétés de chaque bloc éditeur sont fournis dans les tableaux suivants.

### Titre et paragraphe

| Propriété | Description |
| --- | --- |
| Famille de polices | Le style de police du texte |
| Graisse de la police | Détermine l'épaisseur du texte |
| Taille de police | Détermine la taille du texte |
| Hauteur de ligne | Modifie l'espacement entre les lignes de texte |
| Espacement des lettres | Modifie l'espace entre chaque caractère |
| Alignement du texte | Aligne le texte à gauche, au centre, à droite ou en mode justifié |
| Couleur du texte | Modifie la couleur du texte |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Bouton

| Propriété | Description |
| --- | --- |
| Largeur du bouton | Définit la largeur du bouton en mode automatique ou manuel |
| Famille de polices | Le style de police du texte |
| Graisse de la police | Détermine l'épaisseur du texte |
| Taille de police | Détermine la taille du texte |
| Espacement des lettres | Modifie l'espace entre chaque caractère |
| Alignement du bouton | Positionne le bouton à gauche, au centre ou à droite |
| Couleur du texte du bouton | Modifie la couleur du texte sur le bouton |
| Couleur d'arrière-plan | Modifie la couleur de l'arrière-plan du bouton |
| Style de bordure | Détermine le style de la bordure du bouton | 
| Rayon de bordure | Détermine le degré d'arrondi des coins |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Image

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

| Propriété | Description |
| --- | --- |
| URL | L'adresse hébergée de l'image |
| Alignement | Positionne l'image à gauche, au centre ou à droite |
| Couleur d'arrière-plan | Modifie la couleur de l'arrière-plan de l'image |
| Style de bordure | Détermine le style de la bordure de l'image | 
| Rayon de bordure | Détermine le degré d'arrondi des coins de l'image |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Lien

| Propriété | Description |
| --- | --- |
| Famille de polices | Le style de police du texte |
| Graisse de la police | Détermine l'épaisseur du texte |
| Espacement des lettres | Modifie l'espace entre chaque caractère |
| Couleur du texte | Modifie la couleur du texte |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Espaceur

| Propriété | Description |
| --- | --- |
| Couleur d'arrière-plan | Modifie la couleur d'arrière-plan de l'espaceur |
| Hauteur | Modifie la hauteur de l'espaceur. Vous pouvez également ajuster cette valeur à l'aide des poignées de redimensionnement de l'espaceur. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Code personnalisé

| Propriété | Description |
| --- | --- |
| Code personnalisé | Permet d'ajouter, de modifier ou de supprimer du code HTML, CSS et JavaScript pour un message in-app. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Capture de numéros de téléphone

| Propriété | Description |
| --- | --- |
| Groupe d'abonnement | Le groupe d'abonnement [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) ou [WhatsApp]({{site.baseurl}}/whatsapp_subscription_groups/) auquel l'utilisateur sera abonné en fournissant son numéro de téléphone, avec la possibilité de collecter des numéros de tous les pays. |
| Alignement du texte | Aligne le texte à gauche, au centre, à droite ou en mode justifié |
| Texte de la marque substitutive | Un numéro de téléphone de marque substitutive à afficher |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Capture d'adresses e-mail

| Propriété | Description |
| --- | --- |
| Famille de polices | Le style de police du texte |
| Graisse de la police | Détermine l'épaisseur du texte |
| Taille de police | Détermine la taille du texte |
| Hauteur de ligne | Modifie l'espacement entre les lignes de texte |
| Couleur du texte | Modifie la couleur du texte |
| Espacement des lettres | Modifie l'espace entre chaque caractère |
| Alignement du texte | Aligne le texte à gauche, au centre, à droite ou en mode justifié |
| Texte de la marque substitutive | Une adresse e-mail de marque substitutive à afficher |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Actions

Vous pouvez affecter une action qui se déclenche lorsqu'un utilisateur appuie sur un bouton, un lien ou une image dans le message. Vous pouvez également utiliser [Liquid]({{site.baseurl}}/liquid/) pour personnaliser les actions. Les tableaux suivants détaillent les actions disponibles pour chaque bloc éditeur.

### Bouton

| Action | Description |
| --- | --- |
| Envoyer le formulaire lors du clic sur le bouton | Envoie le formulaire et exécute le comportement sélectionné au clic. Désactivez cette option pour exécuter uniquement l'action associée au clic. |
| Définir des comportements distincts pour chaque plateforme | Personnalise le comportement du bouton pour chaque plateforme séparément. |
| Comportement au clic | Détermine l'action effectuée lorsque l'utilisateur clique sur le bouton : fermer le message, ouvrir une URL Web, accéder à une page spécifique de l'application via un lien profond, naviguer vers une autre page ou [demander l'autorisation d'envoyer des notifications push]({{site.baseurl}}/push_primer/). |
| Enregistrer des attributs ou événements personnalisés | Détermine si un clic sur le bouton met à jour le profil de l'utilisateur avec des données personnalisées. Vous pouvez également sélectionner l'identifiant pour le rapport. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Image

Pour les spécifications relatives aux images, consultez nos [spécifications relatives aux images des messages in-app]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/image_specs/#in-app-messages).

| Action | Description |
| --- | --- |
| Texte alternatif | Le texte qui apparaît à la place d'une image si celle-ci ne se charge pas. Les lecteurs d'écran annoncent le texte alternatif pour décrire les images : utilisez donc un langage simple pour fournir les informations clés sur l'image. |
| Envoyer le formulaire lors du clic sur l'image | Envoie le formulaire et exécute le comportement sélectionné au clic. Désactivez cette option pour exécuter uniquement l'action associée au clic. |
| Définir des comportements distincts pour chaque plateforme | Personnalise le comportement de l'image pour chaque plateforme séparément. |
| Comportement au clic | Détermine l'action effectuée lorsque l'utilisateur clique sur l'image : fermer le message, ouvrir une URL Web, accéder à une page spécifique de l'application via un lien profond, naviguer vers une autre page ou [demander l'autorisation d'envoyer des notifications push]({{site.baseurl}}/push_primer/). |
| Enregistrer des attributs ou événements personnalisés | Détermine si un clic sur l'image met à jour le profil de l'utilisateur avec des données personnalisées. Vous pouvez également sélectionner l'identifiant pour le rapport. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Lien

| Action | Description |
| --- | --- |
| URL | Le lien hypertexte vers lequel naviguer |
| Identifiant pour le rapport | Détermine quel identifiant est utilisé pour le rapport |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }