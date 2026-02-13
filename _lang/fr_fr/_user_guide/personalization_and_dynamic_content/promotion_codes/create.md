---
nav_title: Créer des codes
article_title: Créer des codes de promotion
page_order: 0.1
description: "Apprenez à créer des codes de promotion dans vos campagnes et Canvas."
---

# Créer des codes de promotion

> Apprenez à créer des codes de promotion dans vos campagnes et Canvas.

## Création d'une liste de codes de promotion {#create}

### Étape 1 : Créer une nouvelle liste

Dans le tableau de bord, allez dans **Paramètres des données** > **Codes promotionnels**, puis sélectionnez **Créer une liste de codes promotionnels**.

![Bouton permettant de créer un code de promotion.]({% image_buster /assets/img/promocodes/promocode1.png %})

### Étape 2 : Saisissez les détails

1. Nommez votre liste de codes de promotion et ajoutez une description facultative.
2. Ensuite, créez un extrait de code pour le code de promotion. 

Voici quelques détails à prendre en compte lors de la création d'un extrait de code :

- Vous ne pouvez pas modifier un extrait de code après l'avoir enregistré.
- Les extraits de code sont sensibles à la casse. Par exemple, le système reconnaît "Birthday_promo" et "birthday_promo" comme deux extraits de code différents.
- Utilisez le nom de l'extrait dans Liquid pour référencer cet ensemble de codes de promotion.
- Assurez-vous que l'extrait de code n'est pas déjà utilisé dans une autre liste.

![Une liste de codes de promotion nommée "SpringSale2025" avec l'extrait de code "spring25".]({% image_buster /assets/img/promocodes/promocode3.png %}){: style="max-width:80%"}

### Étape 3 : Choisissez les options du code de promotion

Chaque liste de codes de promotion est assortie d'une date et d'une heure d'expiration qui sont définies lors de la création. La durée maximale d'expiration est de six mois à compter du jour où vous créez ou modifiez votre liste.

Dans ce délai, vous pouvez modifier et mettre à jour la date d’expiration à plusieurs reprises. Cette date d'expiration s'applique à tous les codes ajoutés à cette liste. À l'expiration, les codes sont supprimés du système Braze et tout message appelant l'extrait de code de cette liste n'est pas envoyé.

![Les paramètres d'expiration de la liste indiquent que tous les codes restants expireront le 30 avril 2025 à 12 heures.]({% image_buster /assets/img/promocodes/promocode4.png %}){: style="max-width:80%"}

Vous avez également la possibilité de mettre en place des alertes de seuil facultatives et personnalisées. Si elles sont paramétrées, ces alertes envoient un e-mail au destinataire désigné soit lorsque le nombre de codes de promotion disponibles dans cette liste est faible, soit lorsque votre liste de codes de promotion est proche de l'expiration. Le destinataire est informé une fois par jour.

![Exemple de seuil d'alerte permettant d'avertir "marketeur@abc.com" lorsque la liste des codes promotionnels expire dans 5 jours.]({% image_buster /assets/img/promocodes/promocode5.png %}){: style="max-width:80%"}

### Étape 4 : Télécharger des codes de promotion

Braze ne gère pas la création ou l'échange de codes, ce qui signifie que vous devez générer vos codes de promotion dans un fichier CSV et les télécharger dans Braze. 

Veillez à ce que votre fichier CSV respecte ces directives :

- Comprend une colonne pour les codes de promotion.
- Chaque ligne contient un code de promotion.

Vous pouvez utiliser notre intégration intégrée avec [Voucherify]({{site.baseurl}}/partners/ecommerce/loyalty/voucherify/) ou [Talon.One]({{site.baseurl}}/partners/ecommerce/loyalty/talonone/) pour créer et exporter des codes de promotion.

{% alert important %}
La taille maximale du fichier est de 100 Mo et la taille maximale de la liste est de 20 MM de codes non utilisés. Si vous constatez que le fichier téléchargé n'est pas le bon, téléchargez-en un nouveau pour remplacer le précédent.
{% endalert %}

1. Une fois le téléchargement terminé, sélectionnez **Enregistrer la liste** pour enregistrer tous les détails et codes que vous venez de saisir.

![Fichier CSV nommé "springsale" qui a été téléchargé avec succès.]({% image_buster /assets/img/promocodes/promocode7.png %})

{:start="2"}
2\. Après avoir choisi d'enregistrer, une nouvelle ligne apparaît dans l'**historique des importations.**
3\. Pour actualiser le tableau afin de savoir si votre importation est terminée, sélectionnez <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Sync** en haut du tableau.

![Les codes de promotion sont en cours de téléchargement.]({% image_buster /assets/img/promocodes/promocode8.png %})

{% alert note %}
L'importation de fichiers plus volumineux prend plusieurs minutes. Pendant que vous attendez, vous pouvez quitter la page et travailler sur autre chose pendant que l'importation est en cours. Lorsque l'importation est terminée, le statut devient **Complet** dans le tableau.
{% endalert %}

## Mettre à jour une liste de codes de promotion

Pour mettre à jour une liste, sélectionnez l'une de vos listes existantes. Vous pouvez modifier le nom, la description, l'expiration de la liste et les seuils d'alerte. Vous pouvez également ajouter d'autres codes à la liste en téléchargeant de nouveaux fichiers et en sélectionnant **Mettre à jour la liste.** Tous les codes de la liste ont la même date d'expiration, quelle que soit la date d'importation.

{% alert important %}
Les codes de promotion ne peuvent pas être supprimés.
{% endalert %}

### Modification d'une liste de codes de promotion incorrecte 

Si vous avez téléchargé un fichier CSV contenant des codes de promotion incorrects et sélectionné **Enregistrer la liste**, vous pouvez résoudre le problème par l'une ou l'autre méthode :

- Déprécier la liste entière : N'utilisez plus la liste actuelle des codes de promotion dans les campagnes, les canevas ou les modèles. Ensuite, téléchargez le fichier CSV avec les codes corrects et utilisez-les dans votre envoi de messages.
- Utilisez les codes incorrects : Créez une campagne qui envoie les codes de promotion de la liste des codes de promotion incorrects à un marque substitutive jusqu'à ce que tous les codes incorrects soient utilisés. Ensuite, téléchargez les codes de promotion corrects dans la même liste.
