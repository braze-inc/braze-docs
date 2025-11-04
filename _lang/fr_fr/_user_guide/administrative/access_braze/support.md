---
nav_title: Soutien à Braze
article_title: Soutien
description: "Cette page vous aidera à localiser le portail d'assistance de Braze pour soumettre vos commentaires sur les produits Braze. Cette page ne sera accessible qu'aux clients de Braze."
alias: /braze_support/
page_type: reference
search_rank: 7
---

# ![cours d'apprentissage de Bra](https://learning.braze.com/the-braze-support-portal/)ze []({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/the-braze-support-portal/){: style="float:right;width:120px;border:0;" class="noimgborder"} Braze Support

## Accéder au portail d'assistance

Pour contacter l'équipe d'assistance de Braze, accédez au tableau de bord de Braze. Dans le tableau de bord, sélectionnez **Support** > **Obtenir de l'aide.**

Le menu déroulant "Support" avec la possibilité d'obtenir de l'aide.]({% image_buster /assets/img_archive/get_help.png %}){: style="max-width:60%;"}

En fonction de vos autorisations Braze et si vous êtes un contact d'assistance désigné, vous serez dirigé soit vers le portail d'assistance Braze, où vous pouvez soumettre et suivre des cas, soit vers notre formulaire d'assistance standard. Si vous n'êtes pas sûr d'être un contact d'assistance Braze, contactez l'administrateur Braze, le gestionnaire de succès Braze ou le propriétaire du compte de votre entreprise.

## Ajouter des contacts d'assistance désignés

Les contacts d'assistance désignés peuvent accéder à tous les cas d'assistance de votre entreprise, quel que soit leur auteur. Vous pouvez définir des utilisateurs comme contacts d'assistance désignés directement à partir de la page **Modifier l'utilisateur**. 

1. Allez dans **Paramètres** > **Utilisateurs de l'entreprise**, puis recherchez l'utilisateur par son nom ou son adresse e-mail.
2. Sélectionnez le nom de l'utilisateur ou survolez la ligne du nom de l'utilisateur pour afficher un menu. 
3. Dans le menu, sélectionnez **Modifier** pour être redirigé vers la page **Modifier l'utilisateur**.
4. Cochez la case pour **Définir cet utilisateur comme contact d'assistance désigné pour le portail d'assistance de Braze**.

\![Case à cocher permettant de définir un utilisateur comme contact d'assistance désigné.]({% image_buster /assets/img_archive/designated_support_contact.png %}){: style="max-width:70%;"}

### Obtenir l'accès

Lorsqu'un utilisateur est désigné comme contact d'assistance, le portail d'assistance de Braze lui envoie un e-mail de bienvenue contenant des instructions pour configurer son accès.

## Fournir des captures d'écran de la console de développement

Lorsque vous communiquez avec l'assistance, il se peut que vous ayez besoin d'accéder à votre console de développement pour fournir des informations supplémentaires :
- Chrome
  1. Cliquez avec le bouton droit de la souris sur la page web et sélectionnez **Inspecter**.
  2. Sélectionnez l'onglet **Console** dans la fenêtre qui s'ouvre.
  3. Faites une capture d'écran de l'onglet de la console.<br><br>
- Firefox
  1. Cliquez avec le bouton droit de la souris sur la page web et sélectionnez **Inspecter l'élément**.
  2. Sélectionnez l'onglet **Console** dans la fenêtre qui s'ouvre.
  3. Faites une capture d'écran de l'onglet de la console.<br><br>
- Safari
  1. Allez dans Safari dans la barre de menu en haut de votre écran et sélectionnez **Préférences**.
  2. Sélectionnez **Avancé**, puis cochez la case en regard de **Afficher le menu Développer dans la barre de menus.** Vous pouvez ensuite quitter la fenêtre.
  3. Cliquez avec le bouton droit de la souris sur la page web et sélectionnez **Inspecter l'élément**.
  4. Sélectionnez l'onglet **Console** dans la fenêtre qui s'ouvre.
  5. Faites une capture d'écran de l'onglet de la console.

## Meilleures pratiques pour soumettre une demande d'assistance

### Fournir autant d'informations que possible

Plus vous pouvez apporter d'informations, mieux c'est. Incluez des informations spécifiques telles que l'espace de travail, l'URL de la campagne ou du segment, ainsi que tout ID externe pertinent. Cela peut nous aider à résoudre vos problèmes plus efficacement.

### Fournir un échantillon d'utilisateurs

Partagez un échantillon d'utilisateurs plutôt que l'ensemble du segment concerné. Le fait de fournir un nombre réduit d'utilisateurs nous permet de restreindre notre champ d'action et d'accélérer nos enquêtes.

### Joindre les journaux du réseau (journaux HAR)

Si vous contactez le service d'assistance, il sera utile de demander à l'utilisateur concerné de collecter des journaux de réseau (journaux HAR) à partir de son navigateur pendant que le problème se produit. Il affiche les requêtes réseau entre le navigateur et le serveur pour les différents composants d'une page web, ainsi que le tableau de bord de Braze que l'utilisateur tente d'ouvrir.

Demandez à l'utilisateur concerné de faire ce qui suit :

1. Ouvrez leurs outils de développement. Si vous utilisez Chrome, vous pouvez le faire en utilisant le raccourci clavier `option` + `⌘` + `J` (sur macOS). Si vous utilisez Windows ou Linux, vous pouvez le faire en utilisant le raccourci `shift` + `CTRL` + `J`.
2. Sélectionnez **Réseau** > **Fetch/XHR** ou **XHR**.
3. Effectuez un enregistrement ou une capture d'écran montrant le **nom**, l'**état**, la **taille** et l'**heure des** éléments.<br><br>L'onglet "Fetch/XHR" dans un navigateur Chrome.]({% image_buster /assets/img/network_xhr.png %}){: style="max-width:60%;"}

Ensuite, joignez l'enregistrement ou la capture d'écran de l'utilisateur au ticket d'assistance. Ces informations peuvent aider l'enquête de Support.

### Clarifier le comportement attendu par rapport au comportement réel

Faites-nous savoir ce que vous attendiez et ce qui s'est réellement passé. Cela peut nous aider à réduire les causes possibles du problème.

### Joignez des images pertinentes

Pensez à joindre une capture d'écran pour illustrer le problème. La fourniture de ces images peut nous aider considérablement à comprendre le problème et à accélérer le processus de résolution.

### Évaluer l'impact

Sélectionnez le niveau de gravité approprié pour nous aider à affecter les ressources adéquates à la résolution du problème. 

{% alert important %}
Marquer un problème comme "critique" signifie que votre instance de production est hors service et que tout le travail au sein de Braze est arrêté.
{% endalert %}

## Résolution des problèmes d'accès

Si vous recevez une erreur lors de la connexion au portail d'assistance de Braze, telle que `Check your entry`, assurez-vous que vous avez suivi le lien dans votre e-mail de bienvenue pour définir un mot de passe pour le portail. Si vous l'avez fait ou si vous avez pu vous connecter au portail, créez un ticket d'assistance.