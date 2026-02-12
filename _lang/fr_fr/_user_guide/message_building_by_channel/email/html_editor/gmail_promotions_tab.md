---
nav_title: Configuration des promotions Gmail
article_title: Configuration des promotions Gmail
page_order: 8
description: "Cet article de référence explique comment utiliser Braze pour vous aider à créer la carte de promotions mobiles Gmail à partir de votre campagne par e-mail."
channel:
  - email
toc_headers: h2
---

# Configuration des promotions Gmail

> L'onglet Promotions [Gmail mobile](https://developers.google.com/gmail/promotab/) permet aux marketeurs d'envoyer plus d'informations via des annotations dans une « carte » plutôt que de se limiter à la ligne d'objet ou aux informations de pré-en-tête. Braze dispose d’un outil intégré pour vous aider à créer la carte à partir de votre campagne par e-mail.

## Prérequis

Tout d'abord, transférez vos domaines et sous-domaines à l'équipe en charge de l'onglet Promotions de Google, à l’adresse <a href="mailto:p-promo-outreach@google.com">p-promo-outreach@google.com</a> pour être ajouté à la liste d’autorisation de Gmail. Ceci vous permet d'utiliser toute fonctionnalité affichant des images riches, comme le carrousel de produits pour l'onglet Promotions de Gmail.

## Créer la carte avec Braze

Suivez ces étapes pour créer une carte de promotion Gmail pour une campagne par e-mail. Notez que la navigation hors de la section **Contenu** dans l'éditeur réinitialisera les champs et les informations dans l'onglet **Promotion Gmail**. Complétez la configuration de votre carte de promotion et copiez le HTML généré afin de ne pas perdre votre code HTML.

### Étape 1 : Créer une campagne d'e-mailing

Tout d'abord, [créez votre campagne e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) et sélectionnez l'**éditeur de code HTML** comme expérience d'édition.

### Étape 2 : Ajouter des détails à la carte de promotion Gmail

Ensuite, allez dans la section **Contenu de** l'éditeur HTML et sélectionnez l'onglet **Promotion Gmail**. Remplissez les champs sous **Informations de base**, puis sélectionnez **Générer un code HTML.** Cela aidera à générer le script pour votre carte d'onglet Promo Gmail dans la section **Copiez et collez le code HTML dans `<Head>`**.

![Exemple de création d’une carte.]({% image_buster /assets/img/create-gmail-promo.png %})

### Étape 3 : Personnalisez votre carte de promotion Gmail

Choisissez d'inclure une offre de réduction, une carte d'affaires, une carte de promotion ou toutes les options pour votre carte de promotion Gmail.

{% tabs %}
{% tab Discount offer %}

La mise en place d'une offre de réduction vous permet de spécifier les dates de validité d'une réduction. 

1. Basculer sur l'**offre de réduction**.
2. Dans le cas d'une **offre**, saisissez un bref résumé de la réduction. Un exemple est "20% de réduction".
3. Pour **Code**, ajoutez le code de promotion que l'utilisateur doit appliquer au moment du paiement.
4. Sélectionnez ensuite la date et l'heure de début de l'offre de réduction.
5. Déterminez si l'offre de réduction doit se terminer à une date précise ou ne jamais se terminer.

![Options pour spécifier la valeur de l'offre, le code et la date et l'heure de début d'une offre de réduction.]({% image_buster /assets/img/gmail_promo_discount_details.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Deal Cards %}

Utilisez les cartes d'offres pour fournir des informations clés sur les offres directement en haut du corps des e-mails. Cela permet aux destinataires de comprendre rapidement les détails de l'offre et de passer à l'action. Par exemple, vous pouvez utiliser les cartes de promotion pour promouvoir des offres à durée limitée et réduire la nécessité pour les utilisateurs de rechercher des détails dans les e-mails.

1. Basculer sur la **carte de donne.** 
2. Dans le cas d'une **offre**, saisissez un bref résumé de la réduction. Par exemple, "20 % de réduction sur toutes les chaussures".
3. (facultatif) Pour **Code**, ajoutez le code de promotion que l'utilisateur doit appliquer au moment du paiement.
4. Saisissez au moins l'une des URL suivantes. 
-  **URL de la page de l'offre :** L'URL de la page d'atterrissage de l'offre spécifique. Cela permet de créer un bouton "Acheter maintenant" (ou un bouton similaire). Nous vous recommandons de fournir cette URL pour votre Deal Card. 
- **URL de la page d'accueil du commerçant :** L'URL de votre page d'accueil principale. N'utilisez ce champ que si l'URL d'une page d'offre spécifique n'est pas disponible.
5. (facultatif) Ajoutez une date de début pour l'offre.
6. Déterminez si l'offre doit se terminer à une heure précise ou si elle ne doit jamais se terminer.

![Options permettant de spécifier la valeur de l'offre, le code, ainsi que la date et l'heure de début d'une Deal Card.]({% image_buster /assets/img/gmail_promo_deal_cards.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Promotion cards %}

Les cartes de promotion dans votre carrousel de produits sont utiles pour ajouter des images à votre offre. Vous pouvez également personnaliser les variables dans votre carrousel de produits et inclure jusqu'à dix aperçus d'images, où chaque image est unique.

1. Basculer sur les **cartes de promotion**.
2. Sélectionnez **Ajouter une carte de promotion**. Chaque image dans votre carrousel de produits doit avoir une URL unique et utiliser le même ratio d'aspect (4:5, 1:1, 1.91:1).
3. Incluez l'URL de l'image.
4. Pour l'**URL cible**, ajoutez le lien de votre promotion.

{% alert tip %}
Nous vous recommandons de télécharger les images de vos produits dans la bibliothèque multimédia, puis de copier et coller les URL dans les champs appropriés. Seuls les formats d'images statiques (PNG et JPEG) sont acceptés. Certains formats d’images (GIF) se chargeront mais ne s’afficheront pas comme prévu.
{% endalert %}

{: start="5"}
5\. Personnalisez votre carte de promotion en ajoutant un titre, une devise, un prix et une valeur de réduction.

| Propriété personnalisable | Description |
|---|---|
| Titre | (facultatif) Une ou deux phrases de description pour la promotion. S'affiche sous l'image de prévisualisation. |
| Devise | (facultatif) La devise du prix. |
| Prix | Le prix de la promotion. |
| Valeur de la remise | Le montant réduit du prix d'origine. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Exemple de carrousel de produits d'une entreprise nommée Motto, dont l'e-mail s'intitule "Nos chaussettes les plus vendues sont en solde", avec trois images de chaussettes et leurs prix réduits.]({% image_buster /assets/img_archive/product_carousel.png %}){: style="max-width:40%;"}

{% endtab %}
{% endtabs %}

### Étape 4 : Générer et coller le code HTML

Après avoir créé votre carte de promotion Gmail, sélectionnez **Générer le code HTML.** Copiez et collez le script dans l’élément `<head>` du HTML de votre e-mail. 

{% alert tip %}
Pour l'éditeur par glisser-déposer, copiez et collez le code HTML généré dans la section des [tags d'en-tête personnalisés]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#custom-head-tags) sous **Paramètres d'envoi.**
{% endalert %}

{% alert warning %}
Le script Promotions apparaît uniquement si votre e-mail se trouve dans l'onglet Promotions de Gmail. Actuellement, Gmail utilise des algorithmes pour déterminer la destination de votre e-mail. Cependant, si un utilisateur marque un jour votre e-mail comme une promotion, l'algorithme de Gmail sera ignoré et votre e-mail atterrira automatiquement dans l'onglet Promotions à l'avenir.
{% endalert %}

## Bonnes pratiques

D'une manière générale, respectez les [bonnes pratiques recommandées par Gmail](https://developers.google.com/gmail/promotab/best-practices). 

{% alert tip %}
Bien que vous puissiez utiliser Liquid dans ce script, nous vous conseillons fortement de tester vos envois de messages autant que possible pour éviter toute erreur.
{% endalert %}

## Mesurer les cartes Gmail

Gmail ne renvoie pas d'analyse/analytique sur ces cartes, et les fournisseurs de services d'e-mailing (ESP) comme Braze ne peuvent pas insérer leur propre suivi des liens dans la section d'en-tête (y compris les cartes de promotion et les carrousels de produits). Toutefois, vous pouvez ajouter des paramètres UTM ou des codes uniques aux URL lors de la configuration. Ces paramètres vous permettent de suivre l'engagement à l'aide de votre propre analyse/analytique de site web ou du suivi des conversions, car le suivi fait partie de l'URL elle-même - il n'est pas inséré par l'ESP. Le suivi des clics au niveau ESP n'est pas disponible pour ces liens.

### Incorporer des images

Gmail a vu de meilleurs résultats avec des images fortes liées au courrier électronique. Gmail ne recommande pas d’utiliser une conception de texte uniquement, car cet espace a été conçu pour apporter à l’aperçu ce langage visuel essentiel au marketing par e-mail. N’utilisez pas d’images avec du texte tronqué ou des images répétées dans plusieurs campagnes.

### Décrivez les offres

Gmail ne conseille pas d’utiliser des phrases comme « 1 acheté, 1 gratuit » ou « Bénéficiez de réductions sur tous les shorts et chemises », car il peut être coupé, ne plus attirer le regard et rivaliser avec la ligne d’objet. Cet espace ne doit être utilisé que pour engager vos clients avec votre envoi de messages. Évitez donc toutes les phrases comme « Ouvrez cet e-mail maintenant » ou « Cliquez ici pour accéder aux offres ». Il est préférable d’éviter de répéter votre ligne d’objet.

## Foire aux questions

### Pourquoi mon message promotionnel n’affiche-t-il pas la carte de promotion ou le carrousel de produits dans la boîte de réception de l’utilisateur final ?

De nombreux facteurs déterminent l'affichage du carrousel de produits dans l'onglet Promotions de Gmail.

Toutes les images de l'annotation doivent encore passer un filtre de qualité. Pour que le carrousel de produits s'affiche, toutes les images de l'annotation doivent respecter le rapport hauteur/largeur recommandé et être des images de produits en gros plan, de haute qualité et à haute résolution. Les images doivent contenir peu ou pas de texte. Le filtre de qualité filtre également le contenu inapproprié, de sorte que les images doivent être adaptées aux familles, aux utilisateurs et aux enfants.

En outre, Gmail limite la densité des carrousels de produits qui apparaissent dans l'onglet "Promotions" de Gmail. Par exemple, si un utilisateur est abonné à un grand nombre de marques qui utilisent des carrousels de produits dans leurs e-mails de promotion, Gmail finit par plafonner le nombre de carrousels de produits affichés.

En raison des réglementations de confidentialité et de sécurité de Google, les e-mails avec des annotations doivent être largement envoyés pour que l'annotation fonctionne. Il est recommandé de lancer une campagne et de l'envoyer à au moins 100 destinataires pour que le système de Google la détecte comme un "envoi en masse". Les URL d'image peuvent ne pas varier selon les destinataires.

### Comment les clics sur une carte de promotion ou un carrousel de produits sont-ils suivis ?

Braze ou tout autre ESP ne sont pas en mesure d'insérer le suivi des liens sur les liens dans la section d'en-tête. Cela signifie que les clics ne peuvent pas être suivis sur une carte promotionnelle ou un carrousel de produits.

### Y a-t-il un moyen de voir combien d'utilisateurs ont reçu un carrousel de produits ?

Gmail détermine quand et à qui afficher la carte, il n'y a donc aucune garantie que chaque destinataire verra le carrousel de produits.

### Pourquoi les annotations ne s'affichent-elles pas dans l'onglet "Promotions" de Gmail ?

Les annotations ne sont pas prises en charge par Google Workspace. Pour prévisualiser les personnalisations, vous pouvez créer une adresse e-mail personnelle avec Gmail.

Notez que les annotations ne s'affichent pas dans l'onglet **principal** ni dans aucun autre onglet de l'application mobile Gmail. Les annotations ne s'affichent pas après l'ouverture d'un e-mail par un utilisateur ou si vous utilisez le type d'annotation `DiscountOffer` et que l'heure et la date ont déjà expiré.
