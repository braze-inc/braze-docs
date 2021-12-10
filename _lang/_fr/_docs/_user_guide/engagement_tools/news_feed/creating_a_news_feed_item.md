---
nav_title: Création d'un fil d'actualité
article_title: Création d'un fil d'actualité
page_order: 3
page_type: Référence
description: "Cet article de référence couvre la façon de créer un fil d'actualité. Les éléments Flux d'actualité vous permettent d'insérer du contenu permanent directement dans votre application à partir de notre tableau de bord web."
channel: fil d'actualité
---

# Création d'un fil d'actualités

Les fils d'actualité vous permettent d'insérer du contenu permanent directement dans votre application à partir de notre tableau de bord web. Mieux encore, le fil de nouvelles est également ciblable pour des segments individuels, comme tous nos autres types de messages. Cela signifie que ce que vous voyez dans le flux peut être complètement différent d'un autre individu. Les possibilités pour les nouveaux aliments sont presque illimitées.

Pour voir des exemples de flux d'actualités et des conseils utiles, consultez notre [Études de cas][13], et notre [cas d'utilisation][15] et [meilleures pratiques][16] docs.

## Étape 1 : Cliquez sur créer une carte

Tout d'abord, vous devez choisir le type d'élément du fil d'actualité que vous voulez envoyer à vos utilisateurs. À partir du menu déroulant, vous pouvez sélectionner l'un de nos quatre types de fiches d'actualité.

!\[Créer un fil d'actualité\]\[1\]

### Caractéristiques des fiches d'actualités

#### Cartes de flux d'actualités

<br>!\[Classic Card\]\[2\]{: style="max-width:40%;"}

Les cartes de flux d'actualités standard consistent en :

- Image 110x110
- Titre de la page
- Corps du texte
- Lien (In-App/Web)

#### Cartes d'images sous-titrées

<br>!\[Image sous-titrée\]\[3\]{: style="max-width:40%;"}

Les cartes d'image sous-titrées consistent en :

- Image 600x450
- Titre de la page
- Corps du texte
- Lien (In-App/Web)

#### Cartes de bannière

<br>!\[Bannière NewsFeed\]\[4\]{: style="max-width:40%;"}

Les cartes de bannière consistent en :

- Image 600x100
- Lien (In-App/Web)

#### Directives de l'image

|   Type de carte   |          Ratio d'aspect           | Taille de l'image recommandée | Taille maximale de l'image | Types de fichiers |
|:-----------------:|:---------------------------------:|:-----------------------------:|:--------------------------:| ----------------- |
|     Classique     | 1:1 (110 pixels de large minimum) |             500Ko             |            1 Mo            | PNG, JPG, GIF     |
| Image sous-titrée | 4:3 (600 pixels de large minimum) |             500Ko             |            1 Mo            | PNG, JPG, GIF     |
|     Bannière      | 6:1 (600 pixels de large minimum) |             500Ko             |            1 Mo            | PNG, JPG, GIF     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

- Les fichiers PNG sont recommandés.
- Une bibliothèque de chargement d'images personnalisée est nécessaire pour afficher les Gifs sur Android. Nous recommandons Glide.
- Des images plus petites et de haute qualité se chargeront plus rapidement. Il est donc recommandé d'utiliser le plus petit actif possible pour atteindre la sortie souhaitée.

## Étape 2 : Ajouter un titre, un résumé, une image et des liens

!\[Résumé du titre du fil d'actualité\]\[6\]

Il est temps de composer votre carte de flux d'actualités! Créez un titre et un résumé pour votre carte et téléchargez une image pour aller à côté de celle-ci. Vous pouvez également définir le comportement des liens sur cette page. Ce lien peut être un lien standard ou un ["Deep Link"][7] vers le contenu de l'application.

## Étape 3 : Sélectionnez un calendrier

!\[Calendrier des fils d'actualités\]\[8\]

En dessous de l'éditeur de la fiche d'actualité, vous trouverez les options pour publier cet article. Vous pouvez choisir de le publier immédiatement après la création ou définir une heure dans le futur pour le publier. Vous pouvez également choisir de livrer la carte de flux d'actualités à un moment particulier à l'heure locale de vos utilisateurs en cochant la case "Publier aux utilisateurs dans leur fuseau horaire local".

## Étape 4 : Sélectionnez un segment

Vous pouvez configurer votre carte de flux d'actualités pour cibler n'importe quel [segment][10] que vous avez défini dans le tableau de bord à n'importe quel horaire que vous souhaitez. Sélectionnez votre segment cible en cliquant sur le menu déroulant. Ici vous pouvez voir des statistiques de haut niveau, y compris la disponibilité des emails et la valeur à vie par utilisateur.

!\[Target Segment\]\[11\]

## Étape 5 : Examiner les détails et publier

Ensuite, vous serez redirigé vers une page qui affiche tous les détails sur votre carte (et le cas échéant un autre message dans l'application). Vous pouvez consulter les détails de ces éléments et les modifier si vous en avez besoin en cliquant sur l'icône crayon dans l'un des en-têtes.

!\[Aperçu du flux d'actualités\]\[12\]

Voilà! Vous avez terminé ! Vous avez publié votre première fiche d'actualité!

## Optionnel: Associer une carte de flux d'actualité à un message dans l'application

!\[Application Liée dans l'application\]\[14\]

Les campagnes multicanaux mènent souvent à de meilleurs taux de conversion et d'engagement globaux, ainsi Braze a rendu facile le lien entre un message dans l'application et une carte de News Feed spécifique. Après avoir lancé une carte de flux d'actualités, un bouton apparaîtra dans la nouvelle page de statistiques du flux vous permettant de "créer un message associé dans l'application". En cliquant dessus, vous serez dirigé vers le compositeur de campagne pour une nouvelle campagne de message dans l'application. Pendant que vous saisissez la copie, l'apparence et la sensation du message dans l'application, Braze copie automatiquement les règles de livraison et de ciblage de la carte de flux de nouvelles associée pour s'assurer que les campagnes se lancent ensemble.

## Organiser votre flux d'actualités

Vous pouvez réorganiser vos cartes à partir de la page Flux d'actualités de Braze.
- Les cartes dans le flux sont d'abord ordonnées par si elles ont été vues ou non par l'utilisateur, les éléments invisibles sont en haut du flux.
  - Une carte est considérée comme lue si elle a reçu une impression dans le flux.
  - Les impressions ne sont comptées que si la carte est visible dans le flux (c.-à-d. si un utilisateur ne fait pas défiler vers le bas pour lire une carte, une impression n'est pas comptée).
- Les cartes sont ensuite commandées par date et heure de création, où les éléments les plus récents sont en premier.
[1]: {% image_buster /assets/img_archive/newsfeed1_new.png %} [2]: {% image_buster /assets/img_archive/classiccard.png %} [3]: {% image_buster /assets/img_archive/captionedimage. ng %} [4]: {% image_buster /assets/img_archive/newsfeedbanner.png %} [6]: {% image_buster /assets/img_archive/news-feed-title-summary_new. ng %} [8]: {% image_buster /assets/img_archive/newsfeed2_new.png %} [11]: {% image_buster /assets/img_archive/targetsegment_new. ng %} [12]: {% image_buster /assets/img_archive/newsfeedpreview_new.png %} [14]: {% image_buster /assets/img_archive/linked-in-app_new.png %}

[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/advanced_use_cases/linking/#deep-linking-to-app-settings
[10]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[13]: https://www.braze.com/customers
[15]: {{site.baseurl}}/user_guide/engagement_tools/news_feed/news_feed_use_cases/
[16]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/
