---
nav_title: Créer un élément de Fil d’actualité
article_title: Créer un élément de Fil d’actualité
page_order: 3
page_type: reference
description: "Cet article de référence explique comment créer un élément pour votre Fil d’actualité. Les éléments du Fil d’actualité vous permettent d’insérer du contenu permanent directement dans votre application depuis notre tableau de bord Web."
channel: news feed
hidden: true


---

# Créer un élément de Fil d’actualité

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

> Les éléments du Fil d’actualité vous permettent d’insérer du contenu permanent directement dans votre application depuis notre tableau de bord Web. Mieux encore, le Fil d’actualité peut également cibler des segments individuels comme tous nos autres types de messages. Cela signifie que ce que vous voyez dans le fil peut être complètement différent de ce que verrait une autre personne. Les possibilités offertes par le Fil d’actualité sont quasiment illimitées.

Consultez nos [études de cas][13], [cas d'utilisation][15], et [meilleures pratiques][16] pour voir des exemples et des conseils utiles pour les fils d'actualité.

## Étape 1 : Créer une carte

Tout d’abord, vous devez choisir le type d’élément que vous souhaitez envoyer à vos utilisateurs dans votre Fil d’actualité. Dans le menu déroulant, vous pouvez choisir parmi quatre types de cartes de fil d’actualité.

![Le bouton Create Card (Créer une carte) sur le tableau de bord de Braze. Liste des options disponibles pour créer une carte : Classic (Classique), Captioned Image (Image avec légende) et Banner (Bannière).][1]

### Spécifications des cartes de fil d’actualité

#### Cartes de fil d’actualité

<br>![Aperçu d’une carte classique avec l’icône Facebook, un en-tête qui indique « Laissez-nous un j’aime sur Facebook ! », avec deux lignes de texte : "Cliquez ici" et "www.facebook.com".][2]{: style="max-width:40%;"}

Les cartes de fil d’actualité standard comprennent :

- Une image de 110 x 110
- Titre
- Un corps de texte
- Un lien (dans l’application ou Web)

#### Des cartes d’images avec légende

<br>![Aperçu d’une carte d’image avec légende sur laquelle figure une tarte aux pommes entourée de pommes. Sous l’image, un en-tête indique « Les soldes des vacances sont arrivées ! Économisez près de 50 dollars !" avec le texte suivant : « Quatre délicieuses tartes aux pommes pour le prix de 3\. Offre disponible pour une durée limitée. Dépêchez-vous ! Cette offre ne durera pas longtemps. Cliquez ici pour l'utiliser. www.example.com".][3]{: style="max-width:40%;"}

Les cartes d’images avec légende comprennent :

- Une image de 600 x 450
- Titre
- Un corps de texte
- Un lien (dans l’application ou Web)

#### Des cartes-bannières

<br>![Un aperçu de la carte bannière avec une image indiquant "Ceci est une bannière".][4]{: style="max-width:40%;"}

Les cartes-bannières comprennent :

- Une image de 600 x 100
- Un lien (dans l’application ou Web)

#### Directives concernant l’image

|          Type de carte         |          Rapport hauteur/largeur         | Taille d’image recommandée | Taille d’image maximale |   Types de fichiers  |
|:-----------------------------:|:----------------------:|:------------------:|:-------------:|
|          Classique         | 1:1 (110 pixels de large au minimum) |          500 KB         |         1 MB        | PNG, JPEG, GIF |
|          Image avec légende         | 4:3 (600 pixels de large au minimum) |          500 KB         |         1 MB        | PNG, JPEG, GIF |
|          Bannière         | 6:1 (600 pixels de large au minimum) |          500 KB         |         1 MB        | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

- Des fichiers PNG sont recommandés.
- Une bibliothèque de chargement d’images personnalisée est requise pour lire les GIF sur Android. Nous recommandons Glide.
- Les images de petite taille et de haute qualité se chargeront plus rapidement, il est donc recommandé d’utiliser le plus petit format possible pour obtenir le résultat souhaité.

## Étape 2 : Ajouter un titre, un résumé, une image et des liens

Il est temps de composer votre carte de fil d’actualité ! Créez un titre et un résumé pour votre carte et téléchargez une image pour accompagner le texte. Vous pouvez également ajouter un lien sur cette page. Il peut s’agir d’un lien standard ou d’un [lien profond][7] vers du contenu in-app.

![Éditeur d’éléments de fil d’actualité qui affiche le nom de la carte, un aperçu de la carte et les détails de personnalisation pour la langue.][6]

## Étape 3 : Définir une planification

Sous l’éditeur de cartes de fil d’actualité, vous trouverez des options pour choisir quand publier cet élément. Vous pouvez choisir de le publier immédiatement après sa création ou de définir une heure pour le publier ultérieurement. Vous pouvez également choisir de diffuser la carte fil d'actualité à une heure particulière dans l'heure locale de vos utilisateurs en cochant la case **Publier pour les utilisateurs dans leur fuseau horaire local**.

![][8]

## Étape 4 : Sélectionner un segment

Vous pouvez configurer votre carte de fil d'actualité pour qu'elle cible n'importe quel [segment][10] que vous avez défini dans le tableau de bord, selon la planification de votre choix. Sélectionnez votre segment cible en cliquant sur le menu déroulant. Ici, vous pouvez voir des statistiques avancées, y compris la disponibilité des e-mails et la valeur à vie par utilisateur.

![][11]

## Étape 5 : Vérifier les détails et publier

Ensuite, vous serez redirigé(e) vers une page affichant toutes les informations de votre carte (et le message in-app qui l’accompagne, le cas échéant). Vous pouvez vérifier les informations de ces éléments et les modifier au besoin en cliquant sur l’icône en forme de crayon dans n’importe quel en-tête.

![][12]

Et voilà ! Vous avez terminé ! Vous venez de publier votre première carte de fil d’actualité !

## Facultatif : Créer un lien entre une carte de fil d’actualité et un message in-app

Les campagnes multicanaux génèrent souvent de meilleurs taux de conversion et d’engagement, c’est pourquoi Braze vous permet de créer facilement un lien entre un message in-app et une carte de fil d’actualité spécifique. 

Après avoir lancé une carte de fil d’actualité, un bouton apparaîtra sur la page des statistiques du fil d’actualité pour vous permettre de créer un message in-app associé au fil. Cliquez sur ce bouton pour accéder à l’éditeur de campagne et créer une nouvelle campagne de communication dans l’application. Pendant que vous saisissez le texte et concevez la mise en page du message in-app, Braze copie automatiquement les règles de livraison et de ciblage de la carte de fil d’actualité associé à votre message afin que les campagnes soient lancées ensemble.

## Organiser votre fil d’actualité

Vous pouvez réorganiser vos cartes dans la page du fil d'actualité.
- Les cartes du fil d’actualité sont classées dans l’ordre, selon si elles ont été vues ou non par l’utilisateur (les éléments non vus se trouvent en haut du fil).
  - Une carte est considérée comme vue si elle a reçu une impression dans le fil d’actualité.
  - Les impressions ne sont comptabilisées que si la carte est visible dans le flux (autrement dit, si un utilisateur ne fait pas défiler la page pour lire une carte, l'impression n'est pas comptabilisée).
- Les cartes sont ensuite classées par date et heure de création, avec les éléments plus récents en premier.

[1]: {% image_buster /assets/img_archive/newsfeed1_new.png %}
[2]: {% image_buster /assets/img_archive/classiccard.png %}
[3]: {% image_buster /assets/img_archive/captionedimage.png %}
[4]: {% image_buster /assets/img_archive/newsfeedbanner.png %}
[6]: {% image_buster /assets/img_archive/news-feed-title-summary_new.png %}
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/linking/
[8]: {% image_buster /assets/img_archive/newsfeed2_new.png %}
[10]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[11]: {% image_buster /assets/img_archive/targetsegment_new.png %}
[12]: {% image_buster /assets/img_archive/newsfeedpreview_new.png %}
Il y a [13]: https://www.braze.com/customers
[14]: {% image_buster /assets/img_archive/linked-in-app_new.png %}
[15]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/news_feed_use_cases/
[16]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/
