---
nav_title: Codes de Promotion
article_title: Codes de Promotion
page_order: 5
alias: "/fr/promotion_codes/"
description: "Cet article de référence couvre la façon de créer des listes de codes promotionnels et de les ajouter à vos campagnes et à vos Canvases."
---

# Codes promotionnels

> Les codes promotionnels, également appelés codes promotionnels, sont un excellent moyen de maintenir les utilisateurs engagés en conduisant des interactions avec une grande importance pour les achats. <br><br>Avec la fonctionnalité Liquid de Braze, nous offrons un moyen de faire de l'utilisation généralisée du code promotionnel un instantané, permettant maintenant aux messages de tirer de la liste de promotion que vous avez fournie, automatiquement et intuitivement. La fonction de codes promotionnels offre des dates d'expiration allant jusqu'à six mois et supporte jusqu'à 20 MM de codes individuels par liste.

{% alert important %}
Les codes promotionnels ne peuvent pas être envoyés dans les messages de l'application.
{% endalert %}

## Création d'une liste de codes promotionnels

!\[Promo Codes 1\]\[1\]{: style="float:right;max-width:30%;margin-left:15px;"}

### Étape 1 : Accédez à la section Code de Promotion

À partir du tableau de bord, allez sur **Codes de Promotion**, situé dans la section **Intégrations** , puis sélectionnez **Créer une liste de code promotionnel**.

### Étape 2 : Nommer et créer votre code de promotion

Nommez votre liste de codes promotionnels et ajoutez une description facultative.

!\[Promo Codes 2\]\[2\]{: style="max-width:90%"}

Ensuite, créez un extrait de code pour le code promotionnel. Ce code snippet sera ce que vous allez référencer dans Liquid pour afficher cet ensemble spécifique de codes promotionnels. Assurez-vous qu'il s'agit d'un extrait de code qui n'est pas déjà utilisé dans une autre liste.

{% alert important %}
Les extraits sont sensibles à la casse, par exemple, « Birthday_promo» et « birthday_promo» seront reconnus comme deux extraits différents.
{% endalert %}

!\[Promo Codes 3\]\[3\]{: style="max-width:90%"}

{% alert warning %}
Vous ne pouvez pas changer le code snippet après la sauvegarde!
{% endalert %}

### Étape 3 : Options de code promotionnel

Chaque liste de codes promotionnels a une date et une heure d'expiration correspondantes qui seront définies lors de la création. La durée maximale d'expiration est de six mois dans le futur à partir du jour où vous créez ou éditez votre liste. Dans ce délai, vous pouvez modifier et mettre à jour la date d'expiration à plusieurs reprises. Cette date d'expiration s'appliquera à tous les codes ajoutés à cette liste. À l’expiration, les codes seront supprimés du système Braze et tous les messages appelant le code snippet de cette liste ne seront pas envoyés.

!\[Promo Codes 4\]\[4\]{: style="max-width:90%"}

Vous avez également la possibilité de mettre en place des alertes de seuil facultatives et personnalisables. Si configuré, ces alertes enverront un e-mail au destinataire désigné soit lorsque la liste est faible sur les codes de promotion disponibles dans cette liste, ou lorsque votre liste de codes promotionnels est proche de l'expiration. Le destinataire sera averti une fois par jour.

!\[Codes promo 5\]\[5\]

### Étape 4: Téléchargement de code promotionnel

Braze ne gère pas la création ou le rachat de code, donc en conséquence, vous devrez générer vos codes promotionnels dans un fichier CSV et les télécharger sur Braze. Vous pouvez utiliser notre intégration intégrée avec [Voucherify]({{site.baseurl}}/partners/channel_extensions/loyalty/voucherify/) ou [Talon.One]({{site.baseurl}}/partners/channel_extensions/loyalty/talonone/) pour créer et exporter des codes promotionnels. Assurez-vous qu'il n'y a qu'un seul code sur chaque ligne.

{% alert note %}
La taille maximale du fichier est de 100 Mo et la taille maximale de la liste est de 20 MM de codes inutilisés. Si vous trouvez que le mauvais fichier a été téléchargé, téléchargez simplement un nouveau fichier et le fichier précédent sera remplacé.
{% endalert %}

!\[Codes promo 6\]\[6\]

Une fois le téléchargement terminé, cliquez sur **Enregistrer la liste** pour enregistrer tous les détails et codes que vous venez de saisir.

!\[Codes promo 7\]\[7\]

En cliquant sur Enregistrer, vous verrez qu'une nouvelle ligne apparaît dans l' **Historique d'Importation** ci-dessous. Pour actualiser la table pour voir si votre importation est terminée, cliquez sur <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Synchroniser** en haut de la table.

!\[Codes promo 8\]\[8\]

{% alert note %}
Les fichiers plus volumineux prendront quelques minutes à importer. Pendant que vous attendez, vous êtes libre de quitter la page et de travailler sur quelque chose pendant que l'importation est en cours. Une fois l'import terminé, vous verrez le changement de statut à **Compléter** dans le tableau.
{% endalert %}

#### Mise à jour d'une liste de codes promotionnels

Pour mettre à jour une liste, ouvrez simplement une de vos listes existantes. Vous pouvez changer le nom, la description, l'expiration de la liste, les alertes de seuil, et ajoutez plus de codes à la liste en téléchargeant de nouveaux fichiers et en cliquant sur **Liste de mise à jour**. Tous les codes de la liste auront la même expiration, quelle que soit la date d'importation.

### Étape 5 : Utilisez des codes promotionnels

Pour envoyer des codes promotionnels dans des messages, cliquez sur **Copier le snippet** pour copier le snippet de code que vous avez défini lors de la création de votre liste de codes promotionnels.

!\[Promo Codes 9\]\[9\]{: style="max-width:70%"}

À partir de là, tu peux coller ce code dans un message dans le tableau de bord.

!\[Promo Codes 10\]\[10\]{: style="max-width:70%"}

Maintenant, en utilisant [Liquid][11], vous pouvez insérer un des codes de promotion uniques du fichier CSV téléchargé dans un message. Ce code sera marqué comme envoyé sur le backend de Braze pour s'assurer qu'aucun autre message n'envoie ce même code. Lorsqu'un extrait de code est utilisé pour une campagne multicanal ou l'étape Canvas , le même code unique sera envoyé à chaque utilisateur à travers les canaux. Les codes promotionnels ne peuvent pas être envoyés dans les messages de l'application.

{% alert important %}
S'il n'y a pas de code promotionnel disponible lors de l'envoi de tests ou de messages en direct d'une campagne qui tire dans les codes promotionnels, le message ne sera pas envoyé.
{% endalert %}

## Déterminer combien de codes ont été utilisés

Vous pouvez trouver le nombre de codes restants dans la colonne **Restant** de la liste des codes promotionnels, situé sur la page **Codes de Promotion**.

!\[Promo Codes 12\]\[12\]{: style="max-width:90%"}

Ce nombre de codes peut également être trouvé lors de la révision d'une liste de codes promotionnels préexistants.

!\[Promo Codes 13\]\[13\]{: style="max-width:50%"}
[1]:{% image_buster /assets/img/promocodes/promocode1.png %} [2]:{% image_buster /assets/img/promocodes/promocode2.png %} [3]:{% image_buster /assets/img/promocodes/promocode3. ng %} [4]:{% image_buster /assets/img/promocodes/promocode4.png %} [5]:{% image_buster /assets/img/promocodes/promocode5.png %} [6]:{% image_buster /assets/img/promocodes/promocode6. ng %} [7]:{% image_buster /assets/img/promocodes/promocode7.png %} [8]:{% image_buster /assets/img/promocodes/promocode8.png %} [9]:{% image_buster /assets/img/promocodes/promocode9. ng %} [10]:{% image_buster /assets/img/promocodes/promocode10.png %} [12]: {% image_buster /assets/img/promocodes/promocode11.png %} [13]: {% image_buster /assets/img/promocodes/promocode12.png %}

[11]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/





