---
nav_title: Configuration des promotions Gmail
article_title: Configuration des promotions Gmail
page_order: 8
description: "Cet article de référence explique comment utiliser Braze pour vous aider à créer la carte de promotion mobile de Gmail à partir de votre campagne e-mail."
channel:
  - email

---

# Configuration de la promotion Gmail

> L'[onglet Promotions de Gmail mobile](https://developers.google.com/gmail/promotab/) permet aux marketeurs d'envoyer davantage d'informations via des annotations dans une "carte" plutôt que de se contenter de la ligne d'objet ou des informations de l'accroche. Braze dispose d'un outil intégré pour vous aider à créer la carte de votre campagne d'e-mail.

## Prérequis

Commencez par transmettre vos domaines et sous-domaines à l'équipe de sensibilisation de l'onglet Promotions de Google, à l'adresse suivante <a href="mailto:p-promo-outreach@google.com">p-promo-outreach@google.com</a> pour qu'ils soient ajoutés à la liste d'autorisation de Gmail. Cela vous permet d'utiliser n'importe quelle fonctionnalité qui présente des images riches, comme le carrousel de produits de l'onglet Promotions de Gmail.

## Créer la carte avec Braze

Suivez ces étapes pour créer une carte de promotion Gmail pour une campagne e-mail. Notez que si vous quittez la section **Contenu** dans l'éditeur, les champs et les informations de l'onglet **Promotion Gmail** seront réinitialisés. Terminez la configuration de votre carte de promotion et copiez le code HTML généré pour ne pas le perdre.

### Étape 1 : Créer une campagne d'e-mailing

Tout d'abord, [créez votre campagne d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) et sélectionnez l'**éditeur de code HTML** comme expérience d'édition.

### Étape 2 : Ajouter des détails à la carte de promotion Gmail

Ensuite, accédez à la section **Contenu de** l'éditeur HTML et sélectionnez l'onglet **Promotion Gmail**. Remplissez les champs sous **Informations de base**, puis sélectionnez **Générer un code HTML.** Cela vous aidera à générer le script pour votre carte Gmail Promo Tab dans la section **Copier et coller le code HTML dans `<Head>`**.

Un exemple de la façon de créer une carte.]({% image_buster /assets/img/create-gmail-promo.png %})

### Étape 3 : Personnalisez votre carte de promotion Gmail

Choisissez d'inclure une offre de réduction, une carte d'affaires, une carte de promotion ou toutes les options pour votre carte de promotion Gmail.

{% tabs %}
{% tab Discount offer %}

La mise en place d'une offre de réduction vous permet de spécifier les dates de validité d'une réduction. 

1. Basculer sur l'**offre de réduction**.
2. Dans le cas d'une **offre**, saisissez un bref résumé de la réduction. Un exemple est "20% de réduction".
3. Pour **Code**, ajoutez le code de promotion que l'utilisateur doit appliquer au moment du paiement.
4. Sélectionnez ensuite la date et l'heure de début de l'offre de réduction.
5. Déterminez si l'offre de réduction doit se terminer à une date précise ou ne jamais se terminer.

Options permettant de spécifier la valeur de l'offre, le code, ainsi que la date et l'heure de début d'une offre de réduction.]({% image_buster /assets/img/gmail_promo_discount_details.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Deal Cards %}

Utilisez les cartes d'offres pour fournir des informations clés sur les offres directement en haut du corps des e-mails. Cela permet aux destinataires de comprendre rapidement les détails de l'offre et de passer à l'action. Par exemple, vous pouvez utiliser les cartes de promotion pour promouvoir des offres à durée limitée et réduire la nécessité pour les utilisateurs de rechercher des détails dans les e-mails.

1. Basculer sur la **carte de donne**.
2. Dans le cas d'une **offre**, saisissez un bref résumé de la réduction. Par exemple, "20 % de réduction sur toutes les chaussures".
3. (facultatif) Pour **Code**, ajoutez le code de promotion que l'utilisateur doit appliquer au moment du paiement.
4. Saisissez au moins l'une des URL suivantes. 
-  **URL de la page de l'offre :** L'URL de la page d'atterrissage de l'offre spécifique. Cela permet de créer un bouton "Acheter maintenant" (ou un bouton similaire). Nous vous recommandons de fournir cette URL pour votre Deal Card. 
- **URL de la page d'accueil du commerçant :** L'URL de votre page d'accueil principale. N'utilisez ce champ que si l'URL d'une page d'offre spécifique n'est pas disponible.
5. (facultatif) Ajoutez une date de début pour l'offre.
6. Déterminez si l'offre doit se terminer à une heure précise ou si elle ne doit jamais se terminer.

Options permettant de spécifier la valeur de l'offre, le code, ainsi que la date et l'heure de début d'une carte d'offre.]({% image_buster /assets/img/gmail_promo_deal_cards.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Promotion cards %}

Les cartes de promotion dans votre carrousel de produits sont utiles pour fournir des images à votre offre. Vous pouvez également personnaliser les variables de votre carrousel de produits et inclure jusqu'à dix aperçus d'images, où chaque image est unique.

1. Basculer sur les **cartes de promotion**.
2. Sélectionnez **Ajouter une carte de promotion**. Chaque image de votre carrousel de produits doit avoir une URL unique et utiliser le même rapport hauteur/largeur (4:5, 1:1, 1,91:1).
3. Incluez l'URL de l'image.
4. Pour l'**URL cible**, ajoutez le lien de votre promotion.

{% alert tip %}
Nous vous recommandons de télécharger les images de vos produits dans la bibliothèque multimédia, puis de copier et coller les URL dans les champs appropriés. Seuls les formats d'images statiques (PNG et JPEG) sont acceptés. Certains formats d'images (GIF) seront téléchargés mais ne s'afficheront pas comme prévu.
{% endalert %}

{: start="5"}
5\. Personnalisez votre carte de promotion en ajoutant un titre, une devise, un prix et une valeur de réduction.

| Propriété personnalisable | Description |
|---|---|
| À la une | (facultatif) Description en une ou deux phrases de la promotion. S'affiche sous l'image de prévisualisation. |
| Monnaie | (facultatif) La devise du prix. |
| Prix | Le prix de la promotion. |
| Valeur d'actualisation | Le montant actualisé par rapport au prix initial. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Un exemple de carrousel de produits d'une société nommée Motto avec l'e-mail "Nos chaussettes les plus vendues sont en solde", avec trois images de chaussettes et leurs prix réduits.]({% image_buster /assets/img_archive/product_carousel.png %}){: style="max-width:40%;"}

{% endtab %}
{% endtabs %}

### Étape 4 : Générer et coller le code HTML

Après avoir créé votre carte de promotion Gmail, sélectionnez **Générer le code HTML.** Copiez et collez le script dans l'élément `<head>` du code HTML de votre e-mail.

{% alert warning %}
Le script des promotions n'apparaît que si votre e-mail arrive dans l'onglet des promotions de Gmail. Actuellement, Gmail utilise des algorithmes pour déterminer l'emplacement de votre e-mail. Toutefois, si un utilisateur marque votre e-mail comme étant une promotion, l'algorithme de Gmail sera ignoré et votre e-mail atterrira automatiquement dans l'onglet "Promotions" à l'avenir.
{% endalert %}

## Meilleures pratiques

D'une manière générale, respectez les [bonnes pratiques recommandées par Gmail](https://developers.google.com/gmail/promotab/best-practices). 

{% alert tip %}
Bien que vous puissiez utiliser Liquid dans ce script, nous vous conseillons vivement de tester votre envoi de messages autant que possible afin d'éviter toute erreur.
{% endalert %}

### Incorporer des images

Gmail a obtenu de meilleurs résultats avec des images fortes en rapport avec le message de l'e-mail. Gmail déconseille l'utilisation d'une conception exclusivement textuelle, car cet espace a été conçu pour apporter un langage visuel, essentiel au marketing par e-mail, dans la prévisualisation. N'utilisez pas d'images dont le texte est coupé ou qui se répètent dans plusieurs campagnes.

### Décrivez les offres

Gmail ne suggère pas l'utilisation de phrases ou d'expressions telles que "Vous pouvez acheter 1 pour 1 gratuitement ou bénéficier de réductions sur tous les shorts et chemises", car elles risquent de s'écourter, de ne plus attirer l'attention et d'entrer en concurrence avec la ligne d'objet. Cet espace ne doit être utilisé que pour engager vos clients dans votre message. Évitez donc toute formulation du type "Ouvrez cet e-mail maintenant" ou "Cliquez ici pour des offres". Il est préférable d'éviter de répéter votre ligne d'objet.

## Questions fréquemment posées

### Pourquoi mon message promotionnel n'affiche-t-il pas la carte de promotion ou le carrousel de produits dans la boîte réception de l'utilisateur final ?

De nombreux facteurs déterminent l'affichage du carrousel de produits dans l'onglet Promotion de Gmail.

Toutes les images de l'annotation doivent encore passer un filtre de qualité. Pour que le carrousel de produits se remplisse, il est essentiel que toutes les images de l'annotation respectent le rapport hauteur/largeur recommandé, qu'elles soient de haute qualité ou qu'elles présentent des images de produits en gros plan et en haute résolution. Les images doivent contenir peu ou pas de texte (de préférence). Le filtre de qualité filtre également les contenus inappropriés. Les images doivent donc être adaptées aux familles, aux utilisateurs et aux enfants.

En outre, Gmail a fixé un plafond de densité pour le nombre de carrousels de produits apparaissant dans l'onglet Promotion de Gmail d'un utilisateur. Par exemple, si un utilisateur s'abonne à un grand nombre de marques qui utilisent des carrousels de produits dans leurs e-mails de promotion, Gmail finit par plafonner le nombre de carrousels de produits affichés.

En raison des règles de confidentialité et de sécurité de Google, les e-mails contenant des annotations doivent être envoyés à grande échelle pour que l'annotation fonctionne. Il est recommandé de lancer une campagne et de l'envoyer à au moins 100 destinataires pour que le système de Google la détecte comme un "envoi en masse". Les URL des images ne peuvent pas varier d'un destinataire à l'autre.

### Comment les clics sur une carte de promotion ou un carrousel de produits sont-ils suivis ?

Braze ou tout autre ESP n'est pas en mesure d'insérer le suivi des liens dans la section de l'en-tête. Cela signifie que les clics ne peuvent pas être suivis sur une carte de promotion ou un carrousel de produits.

### Existe-t-il un moyen de savoir combien d'utilisateurs ont reçu un carrousel de produits ?

Gmail détermine quand et à qui afficher la carte, il n'est donc pas garanti que tous les destinataires verront le carrousel de produits.

