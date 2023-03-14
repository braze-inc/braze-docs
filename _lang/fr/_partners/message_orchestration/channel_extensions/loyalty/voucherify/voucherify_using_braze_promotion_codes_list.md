---
nav_title: Liste des Promotion Codes et Voucherify
article_title: Liste des Promotion Codes Braze et Voucherify
page_order: 4
alias: /partners/voucherify/promotion/
description: "Cet article explique comment vous pouvez partager des codes Voucherify en utilisant l’extrait de code promo de Braze."
page_type: partner
search_tag: Partenaire
---

# Liste des codes de promotion Voucherify et Braze

> En plus du Contenu connecté et des attributs personnalisés, vous pouvez partager les codes de Voucherify en utilisant l’extrait de code de promotion de Braze. Tout d'abord, exportez les codes de Voucherify, importez les codes dans Braze, et ajoutez un extrait de code d'e-mail pour extraire les codes de la liste des promotions. 

## Étape 1 : Exporter des codes uniques depuis Voucherify

Dans Voucherify, naviguez vers votre campagne Voucherify. Puis, sélectionnez **Exporter vers CSV** et éditez le fichier CSV en supprimant le nom de la colonne pour ne laisser que la liste des codes.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_export_codes.png %}){: style="margin-top:15px;"}

## Étape 2 : Créer une liste de codes de promotion

Allez sur **Codes de promotion** dans la section **Intégrations Braze** et cliquez sur **Créer une liste de codes de promotion**.

Vous pouvez utiliser le nom de la campagne Voucherify pour nommer la liste et assurer la cohérence des données.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_code_list.png %}){: style="max-width:50%;"}

Ensuite, ajoutez l'extrait de code qui fait référence aux codes de la liste ; il sera complété par un code unique une fois le message envoyé.

### Paramètres supplémentaires

Vous pouvez également définir des attributs pour les codes comme l'expiration de la liste et les alertes de seuil ; cependant, notez que Voucherify gère la logique derrière vos codes indépendamment des paramètres de la liste.

![Expiration de la liste]({% image_buster /assets/img/voucherify/voucherify_promotion_list_expiration.png %})

## Étape 3 : Upload du fichier CSV

Uploadez le fichier CSV avec les codes de Voucherify.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_import_codes.png %})

Confirmez que la liste ne contient que des codes (pas d'en-tête de colonne) et cliquez sur **Start Upload (Commencer l’upload)**. Lorsque l'importation est terminée, cliquez sur **Save List (Enregistrer la liste)** pour confirmer les détails de la liste.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_upload_csv.png %}){: style="max-width:50%;"}

## Étape 4 : Utiliser l’extrait de code dans une campagne Braze

Pour utiliser des codes dans la liste dans une campagne Braze, copiez l’extrait de code et ajoutez-le au corps de l’e-mail.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_code_snippet.png %}){: style="max-width:50%;"}

Ajoutez l'extrait de code pour afficher un code de la liste.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_liquid_email.png %})

Une fois le message envoyé, le même code ne sera pas réutilisé.
