---
nav_title: Onglet Promotions Gmail
article_title: Onglet Promotions Gmail
page_order: 8
description: "Gmail a mis à jour l'onglet Promotions mobiles pour permettre aux marketeurs d'envoyer plus d'informations via des annotations dans une \"carte\". Cet article explique comment utiliser Braze pour vous aider à construire la carte à partir de notre produit."
channel:
  - Email
---

# Outil de promotion Gmail

Gmail a mis à jour [l'onglet Promotions mobiles][1] pour permettre aux marketeurs d'envoyer plus d'informations via des annotations dans une "carte" plutôt que simplement la ligne de sujet ou des informations pré-en-tête. Braze a construit un outil pour vous aider à construire la carte à partir de notre produit.

## Construire la carte avec Braze

Construire la carte à Braze est facile!

Tout d'abord, créez votre campagne de courriel, comme vous le feriez normalement. Ensuite, lorsque vous éditez le contenu de votre e-mail, cliquez sur l'onglet **Gmail Promo**. Ici, vous serez en mesure de remplir les champs qui vont générer le script pour votre carte Gmail Promo Tab.

!\[Construisez votre carte\]\[2\]

Une fois que vous aurez rempli les champs, vous verrez un script terminé au bas de votre éditeur. Copiez et collez le dans la "`<head>` "section/élément de votre message `HTML`.

!\[Copiez votre script\]\[3\]

{% alert warning %}

The Promotions script will only appear if your email lands in the Gmail **Promotions Tab**. Actuellement, Gmail utilise des algorithmes pour déterminer la destination de votre courriel. Cependant, si un utilisateur marque un jour votre e-mail comme une promotion, l'algorithme de Gmail sera ignoré, et votre email sera automatiquement positionné dans l'onglet **Promotions** avancer.

{% endalert %}

### Personnaliser votre carte

Vous pouvez personnaliser de nombreuses variables pour votre carte, qui seront mappées aux emplacements indiqués dans la disposition de la carte ci-dessous.

!\[Carte promotionnelle\]\[4\]

| Variable personnalisable                        | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Logo de la société                              | Les logos doivent être une forme carrée ou circulaire et doivent être téléchargés dans "`https` ", et non "`http`".                                                                                                                                                                                                                                                                                                                              |
| Image du produit (aperçu de l'image)            | Il s'agit d'une toile vierge pour que vous puissiez apporter des images de produits ou de style de vie. Dans l'aperçu de Gmail, ils montrent un exemple d'image qui est "`538x138` "avec un "`3.9` "rapport d'aspect.                                                                                                                                                                                                                            |
| Offre de réduction (badge « Green Deal Badge ») | Un ou deux mots utilisés pour mettre rapidement en évidence une offre ou comme un appel à l'action, comme "Cadeau Gratuit", "2 pour 1", ou "Offre Limitée".                                                                                                                                                                                                                                                                                      |
| Code de réduction (code promo)                  | Utilisez votre code promo régulier. Utiliser uniquement s'il y a un code promotionnel.                                                                                                                                                                                                                                                                                                                                                           |
| Date d'expiration                               | La date de début doit être le moment où votre e-mail envoie ou la promotion commence (si cette date est dans le futur, votre adresse e-mail __ne remplira pas__ dans un bundle). La date de fin ne doit être utilisée que si vous avez une offre d'expiration, et la date doit être dans le futur. Les dates d'expiration antérieures ou antérieures entraîneront notre système de voir l'offre comme obsolète et n'afficheront pas votre email. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
Nous vous recommandons de télécharger votre logo et votre image de produit dans la médiathèque de Braze, puis copiez et collez les URLs à partir de là dans les champs appropriés. Seuls les formats d'images statiques comme `.png` et `.jpeg` sont acceptés. Certains formats d'image, comme `.gif`, seront téléchargés mais n'agiront pas comme prévu.
{% endalert %}

{% alert warning %}
Bien que vous puissiez utiliser Liquid dans ce script, nous vous recommandons fortement de tester autant que possible pour éviter une erreur.
{% endalert %}

### Meilleures pratiques

En plus de respecter les meilleures pratiques recommandées par Gmail, vous pouvez utiliser leur outil [Aperçu de vos annotations][5] pour voir à quoi ressemblent leurs cartes.

#### Image du produit

Gmail a vu de meilleurs résultats avec de fortes images liées au message électronique. Gmail ne recommande pas d'utiliser un design texte uniquement, car cet espace a été conçu pour apporter ce langage visuel, vital pour le marketing par courriel, à l'aperçu. N'utilisez pas d'images avec du texte coupé ou répétez des images dans plusieurs campagnes.

#### Offre de réduction

Gmail ne suggère pas d'utiliser des phrases ou des phrases, telles que "Vous pouvez acheter 1 Gratuit, 1 Gratuit ou des Remises sur tous les Shorts et Shirts", comme il peut clip, ne plus dessiner l'œil, et concurrencer avec la ligne du sujet. Encore une fois, cet espace ne devrait être utilisé que pour votre messagerie afin d'engager vos clients avec votre courriel. donc évitez toute langue autour de "Ouvrir cet e-mail maintenant" ou "Cliquez ici pour les affaires". Ne répétez pas votre ligne d'objet.
[2]: {% image_buster /assets/img/create-gmail-promo.gif %} [3]: {% image_buster /assets/img/copy-gmail-promo-script.gif %} [4]: {% image_buster /assets/img/promocardmap.png %}

[1]: https://developers.google.com/gmail/promotab/
[5]: https://developers.google.com/gmail/promotab/overview#preview_your_annotations
