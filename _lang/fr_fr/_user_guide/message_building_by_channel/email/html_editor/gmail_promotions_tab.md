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

> L'[onglet Promotions de Gmail mobile](https://developers.google.com/gmail/promotab/) permet aux marketeurs d'envoyer plus d'informations via des annotations dans une « carte », plutôt que de se limiter à la ligne d'objet ou aux informations d'accroche. Braze dispose d'un outil intégré pour vous aider à créer la carte à partir de votre campagne par e-mail.

## Prérequis

Tout d'abord, transférez vos domaines et sous-domaines à l'équipe en charge de l'onglet Promotions de Google, à l'adresse <a href="mailto:p-promo-outreach@google.com">p-promo-outreach@google.com</a>, pour être ajouté à la liste d'autorisation de Gmail. Ceci vous permet d'utiliser toute fonctionnalité affichant des images riches, comme le carrousel de produits pour l'onglet Promotions de Gmail.

## Créer la carte avec Braze

Suivez ces étapes pour créer une carte de promotion Gmail pour une campagne par e-mail. Notez que quitter la section **Contenu** dans l'éditeur réinitialisera les champs et les informations de l'onglet **Promotion Gmail**. Finalisez la configuration de votre carte de promotion et copiez le HTML généré afin de ne pas perdre votre code HTML.

### Étape 1 : Créer une campagne par e-mail

Tout d'abord, [créez votre campagne par e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) et sélectionnez l'**éditeur de code HTML** comme expérience d'édition.

### Étape 2 : Ajouter des détails à la carte de promotion Gmail

Ensuite, rendez-vous dans la section **Contenu** de l'éditeur HTML et sélectionnez l'onglet **Promotion Gmail**. Remplissez les champs sous **Informations de base**, puis sélectionnez **Générer un code HTML**. Le script de votre carte d'onglet Promo Gmail sera alors généré dans la section **Copiez et collez le code HTML dans `<Head>`**.

![Exemple de création d'une carte.]({% image_buster /assets/img/create-gmail-promo.png %})

### Étape 3 : Personnaliser votre carte de promotion Gmail

Choisissez d'inclure une offre de réduction, une carte d'offre, une carte de promotion ou toutes les options pour votre carte de promotion Gmail.

{% tabs %}
{% tab Discount offer %}

La mise en place d'une offre de réduction vous permet de spécifier les dates de validité d'une réduction. 

1. Activez le bouton **Offre de réduction**.
2. Dans le champ **Offre**, saisissez un bref résumé de la réduction. Par exemple : « 20 % de réduction ».
3. Dans le champ **Code**, ajoutez le code de promotion que l'utilisateur doit appliquer au moment du paiement.
4. Sélectionnez ensuite la date et l'heure de début de l'offre de réduction.
5. Déterminez si l'offre de réduction doit se terminer à une date précise ou ne jamais se terminer.

![Options pour spécifier la valeur de l'offre, le code et la date et l'heure de début d'une offre de réduction.]({% image_buster /assets/img/gmail_promo_discount_details.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Deal Cards %}

Les cartes d'offres permettent de présenter les informations clés d'une offre directement en haut du corps de l'e-mail. Les destinataires peuvent ainsi comprendre rapidement les détails de l'offre et passer à l'action. Par exemple, vous pouvez utiliser les cartes d'offres pour promouvoir des offres à durée limitée et éviter aux utilisateurs de chercher les détails dans l'e-mail.

1. Activez le bouton **Carte d'offre**.
2. Dans le champ **Offre**, saisissez un bref résumé de la réduction. Par exemple : « 20 % de réduction sur toutes les chaussures ».
3. (facultatif) Dans le champ **Code**, ajoutez le code de promotion que l'utilisateur doit appliquer au moment du paiement.
4. Saisissez au moins l'une des URL suivantes. 
-  **URL de la page de l'offre :** L'URL de la page d'atterrissage de l'offre spécifique. Cela crée un bouton « Acheter maintenant » (ou similaire). Nous vous recommandons de fournir cette URL pour votre Deal Card. 
- **URL de la page d'accueil du commerçant :** L'URL de votre page d'accueil principale. N'utilisez ce champ que si l'URL d'une page d'offre spécifique n'est pas disponible.
5. (facultatif) Ajoutez une date de début pour l'offre.
6. Déterminez si l'offre doit se terminer à une heure précise ou ne jamais se terminer.

![Options permettant de spécifier la valeur de l'offre, le code, ainsi que la date et l'heure de début d'une Deal Card.]({% image_buster /assets/img/gmail_promo_deal_cards.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Promotion cards %}

Les cartes de promotion dans votre carrousel de produits permettent d'ajouter des images à votre offre. Vous pouvez également personnaliser les variables de votre carrousel de produits et inclure jusqu'à dix aperçus d'images, chacune étant unique.

1. Activez le bouton **Cartes de promotion**.
2. Sélectionnez **Ajouter une carte de promotion**. Chaque image de votre carrousel de produits doit avoir une URL unique et utiliser le même rapport hauteur/largeur (4:5, 1:1, 1.91:1).
3. Incluez l'URL de l'image.
4. Dans le champ **URL cible**, ajoutez le lien de votre promotion.

{% alert tip %}
Nous vous recommandons de télécharger les images de vos produits dans la bibliothèque multimédia, puis de copier et coller les URL dans les champs appropriés. Seuls les formats d'images statiques (PNG et JPEG) sont acceptés. Certains formats d'images (GIF) se chargeront mais ne s'afficheront pas comme prévu.
{% endalert %}

{: start="5"}
5. Personnalisez votre carte de promotion en ajoutant un titre, une devise, un prix et une valeur de réduction.

| Propriété personnalisable | Description |
|---|---|
| Titre | (facultatif) Une ou deux phrases de description pour la promotion. S'affiche sous l'image de prévisualisation. |
| Devise | (facultatif) La devise du prix. |
| Prix | Le prix de la promotion. |
| Valeur de la remise | Le montant déduit du prix d'origine. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Exemple de carrousel de produits d'une entreprise nommée Motto, dont l'e-mail s'intitule « Nos chaussettes les plus vendues sont en solde », avec trois images de chaussettes et leurs prix réduits.]({% image_buster /assets/img_archive/product_carousel.png %}){: style="max-width:40%;"}

{% endtab %}
{% endtabs %}

### Étape 4 : Générer et coller le code HTML

Après avoir créé votre carte de promotion Gmail, sélectionnez **Générer le code HTML**. Copiez et collez le script dans l'élément `<head>` du HTML de votre e-mail. 

{% alert tip %}
Pour l'éditeur par glisser-déposer, copiez et collez le code HTML généré dans la section des [balises d'en-tête personnalisées]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#custom-head-tags) sous **Paramètres d'envoi**.
{% endalert %}

{% alert warning %}
Le script Promotions n'apparaît que si votre e-mail arrive dans l'onglet Promotions de Gmail. Actuellement, Gmail utilise des algorithmes pour déterminer la destination de votre e-mail. Cependant, si un utilisateur marque un jour votre e-mail comme promotion, l'algorithme de Gmail sera ignoré et votre e-mail atterrira automatiquement dans l'onglet Promotions à l'avenir.
{% endalert %}

## Mesurer les cartes Gmail

Gmail ne renvoie pas de données analytiques sur ces cartes, et les fournisseurs de services d'e-mailing (ESP) comme Braze ne peuvent pas insérer leur propre suivi de lien sur les liens de la section d'en-tête (y compris les cartes de promotion et les carrousels de produits). Toutefois, vous pouvez ajouter des paramètres UTM ou des codes uniques aux URL lors de la configuration. Ces paramètres vous permettent de suivre l'engagement via l'analytique de votre propre site web ou le suivi des conversions, car le suivi fait partie intégrante de l'URL — il n'est pas inséré par l'ESP. Le suivi des clics au niveau de l'ESP n'est pas disponible pour ces liens.

### Incorporer des images

Gmail a constaté de meilleurs résultats avec des images percutantes en lien avec le contenu de l'e-mail. Gmail déconseille les conceptions uniquement textuelles, car cet espace a été conçu pour apporter à l'aperçu un langage visuel essentiel au marketing par e-mail. N'utilisez pas d'images avec du texte tronqué et ne réutilisez pas les mêmes images dans plusieurs campagnes.

### Décrire les offres

Gmail déconseille d'utiliser des phrases comme « 1 acheté, 1 gratuit » ou « Réductions sur tous les shorts et chemises », car elles risquent d'être tronquées, de ne plus attirer le regard et de rivaliser avec la ligne d'objet. Cet espace ne doit servir qu'à engager vos clients avec votre message. Évitez donc toute formulation comme « Ouvrez cet e-mail maintenant » ou « Cliquez ici pour accéder aux offres ». Il est également préférable de ne pas répéter votre ligne d'objet.

## Bonnes pratiques

D'une manière générale, respectez les [bonnes pratiques recommandées par Gmail](https://developers.google.com/gmail/promotab/best-practices). 

{% alert tip %}
Bien que vous puissiez utiliser Liquid dans ce script, nous vous conseillons fortement de tester vos envois de messages autant que possible pour éviter toute erreur.
{% endalert %}

### Prévisualiser votre annotation

Utilisez l'[outil de prévisualisation](https://developers.google.com/workspace/gmail/promotab/preview) pour prévisualiser votre annotation. Notez que l'envoi d'un e-mail de test à vous-même ne fonctionnera pas pour les annotations, car celles-ci ne s'affichent que si l'e-mail est envoyé à un nombre significatif de destinataires. Assurez-vous d'envoyer l'e-mail final (avec ses URL d'images) à au moins 100 destinataires Gmail.

N'utilisez pas Google Workspace pour envoyer des e-mails avec des annotations. Utilisez uniquement des domaines d'e-mail autorisés pour envoyer des annotations à un grand groupe de destinataires.

### Respecter les consignes relatives aux images

Vérifiez que vos images respectent les consignes suivantes :
- Utilisez des images de haute qualité et haute résolution.
- Toutes les images annotées doivent utiliser le même rapport hauteur/largeur. Les rapports pris en charge sont : 4:5, 1:1, 1.91:1.
- Utilisez des tailles d'images correctes. Le minimum est de 256x256 ; le maximum est de 4096x4096 pixels.

Gmail recommande d'éviter :
- L'utilisation excessive de texte dans vos images
- L'utilisation d'images qui ne sont que des icônes
- L'utilisation d'images avec des masques arrondis
- L'utilisation d'URL d'images personnalisées

### S'enregistrer avec DMARC

Pour que vos annotations s'affichent correctement, vérifiez que les domaines soumis sont enregistrés avec DMARC et que toutes les politiques sont activées.


## Foire aux questions

### Pourquoi mon message promotionnel n'affiche-t-il pas la carte de promotion ou le carrousel de produits dans la boîte de réception de l'utilisateur final ?

De nombreux facteurs déterminent l'affichage du carrousel de produits dans l'onglet Promotions de Gmail.

Toutes les images de l'annotation doivent passer un filtre de qualité. Pour que le carrousel de produits s'affiche, toutes les images de l'annotation doivent respecter le rapport hauteur/largeur recommandé et être des images de produits en gros plan, de haute qualité et haute résolution. Les images doivent contenir peu ou pas de texte. Le filtre de qualité exclut également le contenu inapproprié : les images doivent donc être adaptées à tous les publics, y compris les enfants.

Par ailleurs, Gmail limite le nombre de carrousels de produits affichés dans l'onglet Promotions d'un utilisateur. Par exemple, si un utilisateur est abonné à de nombreuses marques qui utilisent des carrousels de produits dans leurs e-mails promotionnels, Gmail finit par plafonner le nombre de carrousels affichés.

En raison des réglementations de confidentialité et de sécurité de Google, les e-mails avec des annotations doivent être envoyés à grande échelle pour que l'annotation fonctionne. Il est recommandé de lancer une campagne et de l'envoyer à au moins 100 destinataires pour que le système de Google la détecte comme un « envoi en masse ». Les URL d'images ne doivent pas varier selon les destinataires.

### Comment les clics sur une carte de promotion ou un carrousel de produits sont-ils suivis ?

Ni Braze ni aucun autre ESP ne sont en mesure d'insérer un suivi de lien sur les liens de la section d'en-tête. Les clics ne peuvent donc pas être suivis sur une carte de promotion ou un carrousel de produits.

### Existe-t-il un moyen de savoir combien d'utilisateurs ont reçu un carrousel de produits ?

Gmail détermine quand et à qui afficher la carte. Il n'y a donc aucune garantie que chaque destinataire verra le carrousel de produits.

### Pourquoi les annotations ne s'affichent-elles pas dans l'onglet Promotions de Gmail ?

Les annotations ne sont pas prises en charge par Google Workspace. Pour prévisualiser les annotations, vous pouvez créer une adresse e-mail personnelle avec Gmail.

Notez que les annotations ne s'affichent pas dans l'onglet **Principal** ni dans aucun autre onglet de l'application mobile Gmail. Les annotations ne s'affichent pas non plus après qu'un utilisateur a ouvert un e-mail, ou si vous utilisez le type d'annotation `DiscountOffer` et que la date et l'heure ont déjà expiré.