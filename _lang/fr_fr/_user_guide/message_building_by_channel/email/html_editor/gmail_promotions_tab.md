---
nav_title: Configuration des promotions Gmail
article_title: Configuration des promotions Gmail
page_order: 8
description: "Cet article de référence explique comment utiliser Braze pour vous aider à créer la carte de promotions mobiles Gmail à partir de votre campagne par e-mail."
channel:
  - email

---

# Configuration des promotions Gmail

> L'onglet Promotions [Gmail mobile](https://developers.google.com/gmail/promotab/) permet aux marketeurs d'envoyer plus d'informations via des annotations dans une « carte » plutôt que de se limiter à la ligne d'objet ou aux informations de pré-en-tête. Braze dispose d’un outil intégré pour vous aider à créer la carte à partir de votre campagne par e-mail.

## Prérequis

Tout d'abord, transférez vos domaines et sous-domaines à l'équipe en charge de l'onglet Promotions de Google, à l’adresse <a href="mailto:p-promo-outreach@google.com">p-promo-outreach@google.com</a> pour être ajouté à la liste d’autorisation de Gmail. Ceci vous permet d'utiliser toute fonctionnalité affichant des images riches, comme le carrousel de produits pour l'onglet Promotions de Gmail.

## Créer la carte avec Braze

Suivez ces étapes pour créer une carte de promotion Gmail pour une campagne par e-mail. Notez que la navigation hors de la section **Contenu** dans l'éditeur réinitialisera les champs et les informations dans l'onglet **Promotion Gmail**. Complétez la configuration de votre carte de promotion et copiez le HTML généré afin de ne pas perdre votre code HTML.

1. [Créez votre campagne d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) et sélectionnez l'**éditeur HTML** comme outil d'édition.
2. Allez dans la section **Contenu** de l'éditeur HTML et sélectionnez l'onglet **Promotion Gmail**.
3. Remplissez les champs sous **Information de base**, puis cliquez sur **Générer le code HTML**. Cela aidera à générer le script pour votre carte d'onglet Promo Gmail dans la section **Copiez et collez le code HTML dans `<Head>`**. <br> ![Un exemple de la façon de créer une carte.]({% image_buster /assets/img/create-gmail-promo.png %})
4. Choisissez d'inclure ou non une offre de réduction, des cartes de promotion ou les deux pour votre carte de promotion Gmail. <br> ![Options permettant d'inclure une offre de réduction et des cartes de promotion.]({% image_buster /assets/img_archive/gmail_promo_discount.png %}){: style="max-width:70%;"}
5. Copiez et collez le script dans l’élément `<head>` du HTML de votre e-mail.

{% alert warning %}
Le script Promotions apparaît uniquement si votre e-mail se trouve dans l'onglet Promotions de Gmail. Actuellement, Gmail utilise des algorithmes pour déterminer la destination de votre e-mail. Cependant, si un utilisateur marque un jour votre e-mail comme une promotion, l'algorithme de Gmail sera ignoré et votre e-mail atterrira automatiquement dans l'onglet Promotions à l'avenir.
{% endalert %}

### Inclure une offre de réduction

La mise en place d'une offre de réduction vous permet de spécifier les dates de validité d'une réduction. Après avoir déterminé votre offre de réduction, sélectionnez une date et une heure de début. Vous avez la possibilité de mettre fin à votre offre de réduction à un moment précis, ou de choisir de ne jamais y mettre fin.

![Options permettant de spécifier la valeur de l'offre, le code, ainsi que la date et l'heure de début d'une offre de réduction.]({% image_buster /assets/img/gmail_promo_discount_details.png %}){: style="max-width:70%;"}

### Personnalisation de votre carrousel de produits

Les cartes de promotion dans votre carrousel de produits sont utiles pour ajouter des images à votre offre. Vous pouvez également personnaliser les variables dans votre carrousel de produits et inclure jusqu'à dix aperçus d'images, où chaque image est unique.

![Exemple de carrousel de produits d'une société nommée Motto dont l'e-mail s'intitule "Nos chaussettes les plus vendues sont en solde", avec trois images de chaussettes et leurs prix réduits.]({% image_buster /assets/img_archive/product_carousel.png %}){: style="max-width:40%;"}

| Variable personnalisable | Description |
|---|---|
| URL de l’image | L'URL de votre image. Chaque image dans votre carrousel de produits doit avoir une URL unique et utiliser le même ratio d'aspect (4:5, 1:1, 1.91:1). |
| URL cible | Le lien pour votre promotion. |
| Titre | (facultatif) Une ou deux phrases de description pour la promotion. S'affiche sous l'image de prévisualisation. |
| Devise | (facultatif) La devise du prix. |
| Prix | Le prix de la promotion. |
| Valeur de la remise | Le montant réduit du prix d'origine. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Nous recommandons de télécharger vos images de produit dans la bibliothèque multimédia, puis de copier et coller les URL dans les champs appropriés. Seuls les formats d’image statiques (PNG et JPEG) sont acceptés. Certains formats d’images (GIF) se chargeront mais ne s’afficheront pas comme prévu.
{% endalert %}

### Bonnes pratiques

D'une manière générale, respectez les [bonnes pratiques recommandées par Gmail](https://developers.google.com/gmail/promotab/best-practices). 

{% alert tip %}
Bien que vous puissiez utiliser Liquid dans ce script, nous vous conseillons fortement de tester vos envois de messages autant que possible pour éviter toute erreur.
{% endalert %}

#### Intégrer des images

Gmail a vu de meilleurs résultats avec des images fortes liées au courrier électronique. Gmail ne recommande pas d’utiliser une conception de texte uniquement, car cet espace a été conçu pour apporter à l’aperçu ce langage visuel essentiel au marketing par e-mail. N’utilisez pas d’images avec du texte tronqué ou des images répétées dans plusieurs campagnes.

#### Décrire des offres

Gmail ne conseille pas d’utiliser des phrases comme « 1 acheté, 1 gratuit » ou « Bénéficiez de réductions sur tous les shorts et chemises », car il peut être coupé, ne plus attirer le regard et rivaliser avec la ligne d’objet. Cet espace ne doit être utilisé que pour engager vos clients avec votre envoi de messages. Évitez donc toutes les phrases comme « Ouvrez cet e-mail maintenant » ou « Cliquez ici pour accéder aux offres ». Il est préférable d’éviter de répéter votre ligne d’objet.

## Foire aux questions

### Pourquoi mon message promotionnel n’affiche-t-il pas la carte de promotion ou le carrousel de produits dans la boîte de réception de l’utilisateur final ?

De nombreux facteurs déterminent si le carrousel de produits sera affiché dans l'onglet Promotion Gmail.

Toutes les images de l'annotation doivent encore passer un filtre de qualité. Pour que le carrousel de produits se remplisse, il est essentiel que toutes les images de l'annotation aient le rapport hauteur/largeur recommandé, avec des images de produit en gros plan de haute qualité ou haute résolution. Les images doivent contenir peu ou pas de texte (de préférence). Le filtre de qualité filtre également le contenu inapproprié, de sorte que les images doivent être adaptées aux familles, aux utilisateurs et aux enfants.

En outre, Gmail a un plafond de densité sur le nombre de carrousels de produits qui apparaissent dans l’onglet Promotion Gmail d’un utilisateur. Par exemple, si un utilisateur s’abonne à un grand nombre de marques qui utilisent le carrousel de produits dans leur e-mail promotionnel, Gmail finit par plafonner le nombre de carrousels de produits affichés.

En raison des réglementations de confidentialité et de sécurité de Google, les e-mails avec des annotations doivent être largement envoyés pour que l'annotation fonctionne. Il est recommandé de lancer une campagne et de l'envoyer à au moins 100 destinataires pour que le système de Google le détecte comme un « envoi de masse ». Les URL d'image peuvent ne pas varier selon les destinataires.

### Comment les clics sur une carte de promotion ou un carrousel de produits sont-ils suivis ?

Braze ou tout autre ESP ne sont pas en mesure d'insérer le suivi des liens sur les liens dans la section d'en-tête. Cela signifie que les clics ne peuvent pas être suivis sur une carte promotionnelle ou un carrousel de produits.

### Y a-t-il un moyen de voir combien d'utilisateurs ont reçu un carrousel de produits ?

Gmail détermine quand et à qui afficher la carte, il n'y a donc aucune garantie que chaque destinataire verra le carrousel de produits.

