---
nav_title: Créer des codes
article_title: Créer des codes de promotion
page_order: 0.1
description: "Découvrez comment créer des codes de promotion dans vos campagnes et vos canevas."
---

# Créer des codes de promotion

> Découvrez comment créer des codes de promotion dans vos campagnes et vos canevas.

## Création d'une liste de codes de promotion {#create}

### Étape 1 : Veuillez créer une nouvelle liste.

Dans le tableau de bord, veuillez vous rendre dans **Paramètres des données** > **Codes de promotion**, puis sélectionner **Créer une liste de codes de promotion**.

![Bouton permettant de créer un code de promotion.]({% image_buster /assets/img/promocodes/promocode1.png %})

### Étape 2 : Saisissez les détails

1. Nommez votre liste de codes de promotion et ajoutez une description facultative.
2. Ensuite, créez un extrait de code pour le code de promotion. 

Voici quelques détails à prendre en compte lors de la création d'un extrait de code :

- Il n'est pas possible de modifier un extrait de code après l'avoir enregistré.
- Les extraits de code sont sensibles à la casse. Par exemple, le système identifie"Birthday_promo"et"birthday_promo"comme deux extraits de code distincts.
- Utilisez le nom de l'extrait dans Liquid pour référencer cet ensemble de codes de promotion.
- Assurez-vous que l'extrait de code n'est pas déjà utilisé dans une autre liste.

![Une liste de codes de promotion intitulée « SpringSale2025 » avec l'extrait de code « spring25 ».]({% image_buster /assets/img/promocodes/promocode3.png %}){: style="max-width:80%"}

### Étape 3 : Choisissez les options du code de promotion

Chaque liste de codes de promotion est assortie d'une date et d'une heure d'expiration qui sont définies lors de la création. La durée maximale d'expiration est de six mois à compter de la date à laquelle vous créez ou modifiez votre liste.

Dans ce délai, vous pouvez modifier et mettre à jour la date d’expiration à plusieurs reprises. Cette date d'expiration s'applique à tous les codes ajoutés à cette liste. À leur expiration, les codes sont supprimés du système Braze, et aucun message faisant appel à l'extrait de code de cette liste n'est envoyé.

![Veuillez indiquer dans les paramètres d'expiration que tous les codes restants expireront le 30 avril 2025 à minuit.]({% image_buster /assets/img/promocodes/promocode4.png %}){: style="max-width:80%"}

Vous avez également la possibilité de mettre en place des alertes de seuil facultatives et personnalisées. Une fois configurées, ces alertes sont envoyées par e-mail au destinataire désigné lorsque la liste commence à manquer de codes de promotion disponibles ou lorsque votre liste de codes de promotion arrive à expiration. Le destinataire est informé une fois par jour.

![Exemple d'alerte seuil pour informer « marketing@ abc.com» lorsque la liste des codes de promotion expire dans 5 jours.]({% image_buster /assets/img/promocodes/promocode5.png %}){: style="max-width:80%"}

### Étape 4 : Télécharger des codes de promotion

Braze ne gère pas la création ou l'échange de codes, ce qui signifie que vous devez générer vos codes de promotion dans un fichier CSV et les télécharger dans Braze. 

Veillez à ce que votre fichier CSV respecte ces directives :

- Comprend une colonne pour les codes de promotion.
- Il y a un code de promotion par ligne.

Vous pouvez utiliser notre intégration intégrée avec [Voucherify]({{site.baseurl}}/partners/ecommerce/loyalty/voucherify/) ou [Talon.One]({{site.baseurl}}/partners/ecommerce/loyalty/talonone/) pour créer et exporter des codes de promotion.

{% alert important %}
La taille maximale des fichiers est de 100 Mo et la taille maximale des listes est de 20 millions de codes inutilisés. Si vous constatez qu'un fichier incorrect a été téléchargé, veuillez télécharger un nouveau fichier pour remplacer le fichier précédent.
{% endalert %}

1. Une fois le téléchargement terminé, sélectionnez **Enregistrer la liste** pour enregistrer tous les détails et codes que vous venez de saisir.

![Fichier CSV intitulé « springsale » qui a été téléchargé avec succès.]({% image_buster /assets/img/promocodes/promocode7.png %})

{:start="2"}
2\. Après avoir sélectionné « Enregistrer », une nouvelle ligne apparaît dans l'**historique** **des importations**.
3\. Pour actualiser le tableau afin de savoir si votre importation est terminée, sélectionnez <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Sync** en haut du tableau.

![Les codes de promotion sont en cours de téléchargement.]({% image_buster /assets/img/promocodes/promocode8.png %})

{% alert note %}
L'importation de fichiers volumineux peut prendre plusieurs minutes. Pendant que vous attendez, vous pouvez quitter la page et travailler sur autre chose pendant que l'importation est en cours. Une fois l'importation terminée, le statut passe à **Terminé** dans le tableau.
{% endalert %}

## Mettre à jour une liste de codes de promotion

Pour mettre à jour une liste, sélectionnez l'une de vos listes existantes. Vous pouvez modifier le nom, la description, l'expiration de la liste et les seuils d'alerte. Vous pouvez également ajouter d'autres codes à la liste en téléchargeant de nouveaux fichiers et en sélectionnant **Mettre à jour la liste.** Tous les codes figurant dans la liste ont la même date d'expiration, quelle que soit la date d'importation.

{% alert important %}
Les codes de promotion ne peuvent pas être supprimés.
{% endalert %}

### Modification d'une liste de codes de promotion incorrects 

Si vous avez téléchargé un fichier CSV contenant des codes de promotion incorrects et sélectionné **Enregistrer la liste**, vous pouvez résoudre ce problème de deux manières :

- Déprécier l'ensemble de la liste : Veuillez cesser d'utiliser la liste actuelle des codes de promotion dans toutes les campagnes, canevas ou modèles. Veuillez ensuite télécharger le fichier CSV contenant les codes appropriés et les utiliser pour l'envoi de messages.
- Veuillez utiliser les codes incorrects : Veuillez créer une campagne qui envoie les codes de promotion de la liste des codes de promotion incorrects à une marque substitutive jusqu'à ce que tous les codes incorrects soient utilisés. Veuillez ensuite télécharger les codes de promotion appropriés dans la même liste.
