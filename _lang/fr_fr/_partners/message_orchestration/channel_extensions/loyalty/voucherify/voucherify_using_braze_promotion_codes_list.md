---
nav_title: Voucherify et liste des codes de promotion
article_title: Liste des codes de promotion Voucherify et Braze
page_order: 4
alias: /partners/voucherify/promotion/
description: "Cet article de référence explique comment vous pouvez partager des codes Voucherify en utilisant l'extrait de code promo de Braze."
page_type: partner
search_tag: Partner
---

# Liste des codes de promotion Voucherify et Braze

> Outre le contenu connecté et les attributs personnalisés, vous pouvez partager des codes Voucherify à l'aide de l'extrait de code promo Braze. Tout d'abord, exportez les codes de Voucherify, importez les codes dans Braze et ajoutez un extrait de code e-mail pour extraire les codes de la liste des promotions. 

_Cette intégration est gérée par Voucherify._

## Étape 1 : Exporter des codes uniques de Voucherify

Dans Voucherify, accédez à votre campagne Voucherify. Ensuite, sélectionnez **Exporter vers CSV** et modifiez le fichier CSV en supprimant le nom de la colonne pour ne laisser que la liste des codes.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_export_codes.png %}){: style="margin-top:15px;"}

## Étape 2 : Créez une liste de codes de promotion

Allez dans **Data Settings** > **Promotion Codes** et cliquez sur **Create Promotion Code List**.

Vous pouvez utiliser le nom de la campagne Voucherify pour nommer la liste et vérifier la cohérence des données.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_code_list.png %}){: style="max-width:50%;"}

Ensuite, ajoutez l'extrait de code qui fait référence aux codes de la liste ; il sera complété par un code unique lors de l'envoi du message.

### Paramètres supplémentaires

Vous pouvez également définir des attributs pour les codes tels que l'expiration de la liste et les alertes de seuil ; notez toutefois que Voucherify gère la logique derrière vos codes indépendamment des paramètres de la liste.

![Expiration de la liste]({% image_buster /assets/img/voucherify/voucherify_promotion_list_expiration.png %})

## Étape 3 : Télécharger le fichier CSV

Téléchargez le fichier CSV contenant les codes Voucherify.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_import_codes.png %})

Confirmez que la liste ne contient que des codes (pas d'en-tête de colonne) et cliquez sur **Start Upload**. Lorsque l'importation est terminée, cliquez sur **Enregistrer la liste** pour confirmer les détails de la liste.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_upload_csv.png %}){: style="max-width:50%;"}

## Étape 4 : Utilisez l'extrait de code dans les campagnes de Braze

Pour utiliser les codes de la liste dans une campagne Braze, copiez l'extrait et ajoutez-le au corps de l'e-mail.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_code_snippet.png %}){: style="max-width:50%;"}

Ajoutez l'extrait de code pour afficher un code de la liste.

![]({% image_buster /assets/img/voucherify/voucherify_promotion_liquid_email.png %})

Une fois que le message contenant le code est envoyé, le même code ne sera plus utilisé.

