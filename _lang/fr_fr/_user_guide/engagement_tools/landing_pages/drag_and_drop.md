---
nav_title: Editeur par glisser-déposer
article_title: "Créer des pages d'accueil au moyen du glisser-déposer"
description: "Cet article explique comment créer et personnaliser les pages d'atterrissage de Braze à l'aide de l'éditeur par glisser-déposer."
page_order: 0
alias: /landing_pages/drag_and_drop/
---

# Pages d’accueil par glisser-déposer

> Grâce à l'éditeur par glisser-déposer, vous pouvez créer et personnaliser une page d'atterrissage pour développer votre audience et recueillir vos préférences directement dans Braze.

{% alert important %}
Les pages d'atterrissage sont actuellement en accès anticipé. Le nombre de pages d'atterrissage est limité à cinq par entreprise. Les sessions d'utilisateurs finaux enregistrées sur les pages de renvoi comptent dans le calcul de vos Utilisateurs actifs mensuels / MAU.
{% endalert %}

## Création d’une page d'accueil (glisser-déposer)

### Étape 1 : Créez une page d'accueil

Accédez à l'option **Messages** > **Pages d'accueil** et sélectionnez **Créer une page d'accueil** ou sélectionnez le nom d'une page existante pour la dupliquer ou y apporter des modifications.

![Page d’accueil « Pages d’accueil ».][2]{: style="max-width:90%;"}

### Étape 2 : Définissez les détails de votre page d'accueil

#### Informations générales

Le nom et la description de la page de destination sont utilisés pour rechercher la page dans votre espace de travail interne. Celles-ci ne seront pas visibles pour vos clients.

#### Détails du site

Mettez en place des métatags pour personnaliser l'affichage de votre page dans l'onglet du navigateur et l'optimiser pour les résultats des moteurs de recherche. Celles-ci seront visibles par vos clients.

Nous vous suggérons de suivre ces bonnes pratiques :

| Détail | Description | Recommandations |
| --- | --- |
| Titre du site | Le titre qui s'affiche sur l'onglet du navigateur. | Utilisez jusqu'à 60 caractères. |
| Description du site | Un extrait de code qui s'affiche dans les résultats de recherche. | Utilisez entre 140 et 160 caractères.|
| Favicon | L'icône qui apparaît à côté du titre du site dans l'onglet du navigateur. | Utilisez un rapport hauteur/largeur de 1:1 et un type de fichier pris en charge (PNG, JPEG ou ICO). |
| Handle de l'URL | Il s'agit du lien sur lequel les utilisateurs cliqueront pour accéder à votre page d’accueil. | Celui-ci doit être unique. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Étape 3 : Personnalisez votre page d'accueil

Sélectionnez **Lancer l'éditeur** pour commencer à concevoir votre page d'atterrissage dans l'éditeur par glisser-déposer. L'éditeur sera préchargé avec un modèle par défaut que vous pouvez personnaliser pour l'adapter à votre cas d'utilisation.

![Modèle de page d'accueil avec un formulaire pour l'inscription des clients.][8]{: style="max-width:90%;"}

#### Glisser-déposer des blocs

L'éditeur utilise deux types de composants pour la composition des pages d'atterrissage : les lignes et les blocs. Tous les blocs doivent être placés dans une ligne.

![La section de l'éditeur "Créer" contenant les "Lignes" et les "Blocs de formulaires".][4]{: style="max-width:30%;"}

#### Bloc de formulaires

Utilisez divers composants de blocs de formulaires pour enregistrer des attributs personnalisés et des attributs de profil standard, ainsi que des événements personnalisés. Le bloc de formulaire du champ d'entrée peut enregistrer des attributs standard et personnalisés pour vos utilisateurs, et les blocs de formulaire de capture de téléphone et de capture d'e-mail peuvent capturer les champs de téléphone et d'e-mail pour les soumissions de formulaire de vos utilisateurs. Les actions des boutons peuvent être enregistrées en tant qu'attributs personnalisés, événements personnalisés ou les deux lors de la soumission du formulaire. 

Si vous incluez un bloc de formulaire, vous devez inclure au moins un bouton avec le basculement activé pour **Soumettre le formulaire lorsque le bouton est cliqué**. Vous devriez également créer une autre page d'accueil pour l'[état de confirmation](#confirmation-state).

![Un bloc de formulaire qui enregistre un nouveau client et lui envoie un code de réduction par e-mail.][5]{: style="max-width:70%;"}

#### Styles de conteneur de page

Vous pouvez définir des styles à appliquer à tous les blocs de composants pertinents de votre page d'atterrissage à partir de l'onglet **Conteneur de page.**  Ces styles seront utilisés partout sur votre page, sauf si vous les remplacez par un bloc spécifique.

Nous vous recommandons de définir les styles au niveau du conteneur de la page avant de personnaliser les styles au niveau du bloc. Vous pouvez également ajouter une image de fond pour l'ensemble de la page.

![Le conteneur de page avec des options permettant de personnaliser les images d'arrière-plan, les couleurs, les détails des bordures et le style personnalisé du contenu.][6]{: style="max-width:30%;"}

### Étape 4 : Prévisualisez votre page d'accueil

Vous pouvez prévisualiser votre page d'atterrissage dans l'onglet **Aperçu de** l'éditeur. Après avoir enregistré votre page d'atterrissage en tant que brouillon, vous pouvez visiter l'URL en allant dans **Pages d'atterrissage** et en sélectionnant **Copier l'URL** à côté de votre page d'atterrissage. Vous pouvez également partager l'URL avec des collaborateurs.

![Page d'accueil avec le menu ouvert affichant l'option « Copier l'URL ».][7]{: style="max-width:90%;"}

Une fois que vous êtes satisfait de la page d'accueil, sélectionnez **Publier la page d'accueil**.

{% alert important %}
Le handle d'URL ne peut plus être modifié après la publication de la page d'accueil.
{% endalert %}

## Créer une page de confirmation {#confirmation-state}

Si vous incluez un [formulaire](#form-block) sur votre page d'accueil, n'oubliez pas de créer une page d'accueil de confirmation. Créez une autre page d'atterrissage pour l'état de confirmation, puis ajoutez le lien dans le champ **Open web URL** du bouton qui soumet le formulaire.

## Lien vers votre page d'accueil

Vous pouvez inclure un lien vers la page de destination dans n'importe quel canal en copiant et en collant le lien dans un message Braze ou une campagne de réseaux sociaux.

## Traitement des erreurs de soumission de formulaire

Si un utilisateur saisit une valeur de formulaire non valide (comme des caractères spéciaux non acceptés), il verra un indicateur d'erreur générique qui n'est pas personnalisable et ne pourra pas soumettre le formulaire. Vous pouvez visualiser le comportement des erreurs sur la page d'accueil d’aperçu.

## Fusion des utilisateurs créés à partir de votre page d'accueil

Chaque soumission de formulaire sur une page de renvoi créera un nouveau profil utilisateur anonyme dans Braze. S'il existe déjà un utilisateur avec la même adresse e-mail, vous pouvez fusionner le nouveau profil utilisateur avec le profil existant à l'aide de l’endpoint [`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge#merging-unidentified-user). Pour en savoir plus sur les différentes façons de dédupliquer les utilisateurs dans Braze, consultez [Dupliquer les utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users).

La fusion des utilisateurs sera gérée automatiquement par une étiquette Liquid à l'avenir. 

## Considérations

La taille du corps de la page d'accueil peut aller jusqu'à 1 Mo.

## Autorisations

Vous devez disposer d'autorisations d'administrateur ou de toutes les autorisations suivantes pour accéder aux pages d'atterrissage, les créer et les publier :

- Accéder aux pages d’accueil
- Créer des ébauches de page d’accueil
- Publier les pages d’accueil

## Paliers de régime

Le nombre de pages de destination publiées et de domaines personnalisés que vous pouvez utiliser dépend de votre type de plan : gratuit ou payant (incrémental).

| Fonctionnalité                                                                                                   | Tiercé libre     | Niveau payant (incrémental)     |
| :---------------------------------------------------------------------------------------------------------------- | :--------------- | ----------------- |
| Pages d'atterrissage publiées                                                                 | Cinq par entreprise | 20 supplémentaires |
| Domaines personnalisés          | Un par entreprise | Cinq autres |

## Foire aux questions

### Que se passe-t-il lorsqu'un utilisateur soumet ses informations sur la page d'accueil ?

Lorsqu'un utilisateur soumet un formulaire, un nouveau profil utilisateur Braze est créé avec les données utilisateur soumises.

### Y a-t-il des exigences techniques pour publier une page d'accueil ?

Non, il n'y a pas d'exigences techniques.

### Existe-t-il un éditeur HTML pour les pages d'atterrissage ?

Vous pouvez modifier le code HTML d'une page de destination à l'aide du bloc Code personnalisé.

### Des rapports sont-ils disponibles pour les pages d'atterrissage ?

Non, ce service n'est pas disponible actuellement.

### Puis-je créer un webhook à l'intérieur d'une page d'atterrissage ?

Non, cela n'est pas possible actuellement.

### Quelles sont les fonctionnalités prévues pour les pages d'atterrissage ? {#roadmap}

Nous prévoyons de lancer des fonctionnalités supplémentaires pour les pages d’accueil, qui sont en cours de développement. Il peut s'agir de :

* Nouvelle étiquette Liquid pour lier une page d'atterrissage dans un canal de messages de Braze.
* Fusion automatique des utilisateurs lorsqu'une page de renvoi est envoyée via un canal Braze.
* Page de rapport de base
* Blocs de formulaire à glisser-déposer pour les cases à cocher et les listes déroulantes
* Événement standard pour le suivi et le reciblage basés sur les soumissions de formulaires.

Bien que ces fonctionnalités fassent partie de notre feuille de route, elles sont encore en cours de développement et Braze ne peut pas garantir qu'une partie ou la totalité de ces fonctionnalités sera mise à disposition de tous. L'accès à tout ou partie des fonctionnalités prévues pour les pages d'atterrissage peut être soumis à des frais supplémentaires.

[1]: {% image_buster /assets/img/landing_pages/homepage.gif %}
[2]: {% image_buster /assets/img/landing_pages/create.png %}
[3]: {% image_buster /assets/img/landing_pages/details.png %}
[4]: {% image_buster /assets/img/landing_pages/dnd.png %}
[5]: {% image_buster /assets/img/landing_pages/form.png %}
[6]: {% image_buster /assets/img/landing_pages/page_container.png %}
[7]: {% image_buster /assets/img/landing_pages/url_handle.png %}
[8]: {% image_buster /assets/img/landing_pages/template.png %}
