---
nav_title: Configuration des promotions Gmail
article_title: Configuration des promotions Gmail
page_order: 8
description: "Cet article de référence explique comment utiliser Braze pour vous aider à créer la carte de promotions mobiles Gmail à partir de votre campagne par e-mail."
channel:
  - e-mail

---

# Configuration des promotions Gmail

> L’[onglet Promotions mobiles Gmail][1] permet aux marketeurs d’envoyer plus d’informations via des annotations dans une « carte », plutôt que de se limiter à la ligne Objet ou aux informations de l’accroche. Braze dispose d’un outil intégré pour vous aider à créer la carte à partir de votre campagne par e-mail.

## Créer la carte avec Braze

1. [Créez votre campagne par e-mail][7] comme vous le feriez habituellement. 
2. Accédez à la section **Content Library (Bibliothèque de contenu)** et sélectionnez l'onglet **Gmail Promotion Setup (Configuration de la promotion Gmail)**.
3. Remplissez les champs sous **Basic Information (Informations de base)**. Cela vous aidera à générer le script de votre carte de l’onglet Promo Gmail dans la section **Copy and Paste HTML code into `<Head>` (Copier et coller le code HTML dans ‘<Head>’)**. <br> ![Exemple de création d’une carte.][2]
4. Choisissez d’inclure ou non des offres de réduction ou des cartes de promotion pour votre carte de promotion Gmail.
5. Copiez et collez le script dans l’élément `<head>` du HTML de votre e-mail.

{% alert warning %}
Le script Promotions ne s’affiche que si vos e-mails sont dans l’onglet **Gmail Promotions (Promotions Gmail)**. Actuellement, Gmail utilise des algorithmes pour déterminer la destination de votre e-mail. Cependant, si un utilisateur marque votre e-mail comme une promotion, l’algorithme Gmail sera ignoré, et votre e-mail arrivera automatiquement dans l’**onglet Promotions** à l’avenir.
{% endalert %}

### Personnalisez votre carte

Vous pouvez personnaliser de nombreuses variables de votre carte qui correspondront aux emplacements suivants, indiqués dans la mise en page de la carte.

![Mise en page de la carte qui définit les paramètres du logo de l’entreprise, de l’expéditeur, de la ligne d’objet, de l’offre de remise et du code de réduction, ainsi que des images associées.][4]

| Variable personnalisable | Description |
|---|---|
| Logo de la société | Les logos doivent avoir une forme carrée ou circulaire et être téléchargés en `https` et pas en `http`..|
| Image produit (aperçu d’image unique) | Il s’agit d’un Canvas vierge pour l’ajout d’images de produits ou de styles de vie. Dans l’aperçu de Gmail, ils affichent un exemple d’image de "`538x138` "avec un format de "`3.9` ". |
| Offre de réduction (badge de l’offre) | Un ou deux mots utilisés pour mettre rapidement en évidence une offre ou un appel à l’action, comme « Cadeau gratuit », « 2 pour 1 » ou « Offre limitée ». |
| Code de réduction (code de promotion) | Utilisez votre code de promotion habituel. Utilisez uniquement s’il existe un code de promotion. |
| Date d’expiration | La date de début doit être celle de l'envoi de l’e-mail ou du début de la promotion (si cette date est ultérieure, votre e-mail **ne s’affichera pas** dans un lot). La date de fin ne doit être utilisée que si vous avez une offre expirée et que la date doit être dans le futur. Si les dates d'expiration sont anciennes ou dépassées, notre système considérera l'offre comme périmée et ne prévisualisera pas votre courriel. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
Nous vous recommandons de charger votre logo et l’image du produit dans la bibliothèque multimédia de Braze, puis de copier et coller les URL dans les champs appropriés. Seuls les formats d’image statiques (PNG et JPEG) sont acceptés. Certains formats d’images (GIF) se chargeront mais ne s’afficheront pas comme prévu.
{% endalert %}

### Bonnes pratiques

Au-delà de respecter ces bonnes pratiques recommandées par Gmail, vous pouvez également voir à quoi leurs cartes ressemblent à l’aide de [leur outil Preview your annotations (Prévisualiser vos annotations)][5].

{% alert important %}
Bien que vous puissiez utiliser Liquid dans ce script, nous vous conseillons fortement de tester vos envois de messages autant que possible pour éviter toute erreur.
{% endalert %}

![Un exemple de ce à quoi votre aperçu peut ressembler lors du test sur le site Gmail.][6]

#### Intégrer des images

Gmail a vu de meilleurs résultats avec des images fortes liées au courrier électronique. Gmail ne recommande pas d’utiliser une conception de texte uniquement, car cet espace a été conçu pour apporter à l’aperçu ce langage visuel essentiel au marketing par e-mail. N’utilisez pas d’images avec du texte tronqué ou des images répétées dans plusieurs campagnes.

#### Décrire des offres

Gmail ne conseille pas d’utiliser des phrases comme « 1 acheté, 1 gratuit » ou « Bénéficiez de réductions sur tous les shorts et chemises », car il peut être coupé, ne plus attirer le regard et rivaliser avec la ligne d’objet. Cet espace ne doit être utilisé que pour engager vos clients avec votre envoi de messages. Évitez donc toutes les phrases comme « Ouvrez cet e-mail maintenant » ou « Cliquez ici pour accéder aux offres ». Il est préférable d’éviter de répéter votre ligne d’objet.

## Foire aux questions

### Pourquoi mon message promotionnel n’affiche-t-il pas la carte de promotion ou le carrousel de produits dans la boîte de réception de l’utilisateur final ?

De nombreux facteurs déterminent si le carrousel de produits sera affiché dans l'onglet Promotion Gmail.

Toutes les images de l'annotation doivent encore passer un filtre de qualité. Pour que le carrousel de produits se remplisse, il est essentiel que toutes les images de l'annotation soient dans le rapport d'aspect recommandé, avec des images de produit en gros plan de haute qualité ou haute résolution. Les images doivent contenir peu ou pas de texte (de préférence). Le filtre de qualité filtre également le contenu inapproprié, de sorte que les images doivent être adaptées aux familles, aux utilisateurs et aux enfants.

En outre, Gmail a un plafond de densité sur le nombre de carrousels de produits qui apparaissent dans l’onglet Promotion Gmail d’un utilisateur. Par exemple, si un utilisateur s’abonne à un grand nombre de marques qui utilisent le carrousel de produits dans leur e-mail promotionnel, Gmail finit par plafonner le nombre de carrousels de produits affichés. 

[1]: https://developers.google.com/gmail/promotab/
[2]: {% image_buster /assets/img/create-gmail-promo.png %}
[3]: {% image_buster /assets/img/copy-gmail-promo-script.png %}
[4]: {% image_buster /assets/img/promocardmap.png %}
[5]: https://developers.google.com/gmail/promotab/overview#preview_your_annotations
[6]: {% image_buster /assets/img/gmail_preview.png %}
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_campaign/
