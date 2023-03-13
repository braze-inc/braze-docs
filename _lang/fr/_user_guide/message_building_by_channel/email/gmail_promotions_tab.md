---
nav_title: Onglet Promotions Gmail
article_title: Onglet Promotions Gmail
page_order: 8
description: "Cet article de référence couvre l’outil de promotions de Gmail et explique comment utiliser Braze pour vous aider à créer la carte à partir de notre produit."
channel:
  - e-mail

---

# Outil de promotion Gmail

Gmail a mis à jour l’[onglet Promotions mobiles][1] pour permettre aux marketeurs d’envoyer plus d’informations via des annotations dans une « carte », plutôt que de se limiter à la ligne Objet ou aux informations de l’accroche. Braze a conçu un outil pour vous aider à créer la carte à partir de notre produit.

## Créer la carte avec Braze

La création de la carte dans Braze est facile !

Commencez par créer votre campagne par e-mail comme vous le feriez normalement. Ensuite, lorsque vous modifiez le contenu de votre e-mail, sous **Content Library (Bibliothèque de contenu)**, cliquez sur l’onglet **Gmail Promotion Setup (Configuration des promotions Gmail)**. Ici, vous pourrez remplir les champs qui généreront le script pour votre carte de l’onglet Gmail Promo (Promotions Gmail).

![Exemple de création d’une carte.][2]

Après avoir terminé de remplir les champs, vous verrez un script rempli au bas de votre éditeur. Copiez-le et collez-le dans l’élément `<head>` du HTML de votre e-mail.

![Comment copier votre script pour le coller dans le corps HTML de l’e-mail ?][3]

{% alert warning %}

Le script Promotions ne s’affiche que si vos e-mails sont dans l’onglet **Gmail Promotions (Promotions Gmail)**. Actuellement, Gmail utilise des algorithmes pour déterminer la destination de votre e-mail. Cependant, si un utilisateur marque votre e-mail comme une promotion, l’algorithme Gmail sera ignoré, et votre e-mail arrivera automatiquement dans l’**onglet Promotions** à l’avenir.

{% endalert %}

### Personnalisez votre carte

Vous pouvez personnaliser de nombreuses variables de votre carte qui correspondront aux emplacements suivants, indiqués dans la mise en page de la carte.

![Mise en page de la carte qui définit les paramètres du logo de l’entreprise, de l’expéditeur, de la ligne d’objet, de l’offre de remise et du code de réduction, ainsi que des images associées.][4]

| Variable personnalisable | Description |
|---|---|
| Logo de la société | Les logos doivent avoir une forme carrée ou circulaire et être téléchargés en `https` et pas en `http`..|
| Image produit (aperçu d’image unique)| Il s’agit d’un Canvas vierge pour l’ajout d’images de produits ou de styles de vie. Dans l’aperçu de Gmail, ils affichent un exemple d’image de "`538x138` "avec un format de "`3.9` ". |
| Offre de réduction (badge de l’offre)| Un ou deux mots utilisés pour mettre rapidement en évidence une offre ou un appel à l’action, comme « Cadeau gratuit », « 2 pour 1 » ou « Offre limitée ». |
| Code de réduction (code de promotion)| Utilisez votre code de promotion habituel. Utilisez uniquement s’il existe un code de promotion. |
| Date d’expiration | La date de début doit être celle de l'envoi de l’e-mail ou du début de la promotion (si cette date est ultérieure, votre e-mail **ne s’affichera pas** dans un lot). La date de fin ne doit être utilisée que si vous avez une offre expirée et que la date doit être dans le futur. Si les dates d'expiration sont anciennes ou dépassées, notre système considérera l'offre comme périmée et ne prévisualisera pas votre courriel. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
Nous vous recommandons de télécharger votre logo et l’image du produit dans la bibliothèque multimédia de Braze, puis de copier et coller les URL dans les champs appropriés. Seuls les formats d’image statiques tels que `.png` et `.jpeg` sont acceptés. Certains formats d’images, comme `.gif`, se téléchargeront mais ne réagiront pas comme prévu.
{% endalert %}

### Bonnes pratiques

Au-delà de respecter les meilleures pratiques recommandées par Gmail, vous pouvez utiliser leur outil [Preview your annotations (Prévisualiser vos annotations)][5] pour voir à quoi leurs cartes ressemblent.

![Un exemple de ce à quoi votre aperçu peut ressembler lors du test sur le site Gmail.][6]

{% alert warning %}
Bien que vous puissiez utiliser Liquid dans ce script, nous vous conseillons fortement de le tester autant que possible pour éviter toute erreur.
{% endalert %}

#### Image du produit

Gmail a vu de meilleurs résultats avec des images fortes liées au courrier électronique. Gmail ne recommande pas d’utiliser une conception de texte uniquement, car cet espace a été conçu pour apporter à l’aperçu ce langage visuel essentiel au marketing par e-mail. N’utilisez pas d’images avec du texte tronqué ou des images répétées dans plusieurs campagnes.

#### Offre de réduction

Gmail ne conseille pas d’utiliser des phrases comme « 1 acheté, 1 gratuit » ou « Bénéficiez de réductions sur tous les shorts et chemises », car il peut être coupé, ne plus attirer le regard et rivaliser avec la ligne d’objet. Encore une fois, cet espace ne doit être utilisé que pour que votre communication engage vos clients avec votre e-mail. Évitez donc toutes les phrases comme « Ouvrez cet e-mail maintenant » ou « Cliquez ici pour accéder aux offres ». Ne répétez pas votre ligne d’objet.

[1]: https://developers.google.com/gmail/promotab/
[2]: {% image_buster /assets/img/create-gmail-promo.png %}
[3]: {% image_buster /assets/img/copy-gmail-promo-script.png %}
[4]: {% image_buster /assets/img/promocardmap.png %}
[5]: https://developers.google.com/gmail/promotab/overview#preview_your_annotations
[6]: {% image_buster /assets/img/gmail_preview.png %}
