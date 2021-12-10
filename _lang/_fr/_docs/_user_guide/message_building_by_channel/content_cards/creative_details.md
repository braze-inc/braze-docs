---
nav_title: Détails de la création
article_title: Détails de la création
page_order: 1
layout: en vedette
guide_top_header: "Détails de la création"
guide_top_text: "Soyez créatif avec les cartes de contenu ! Mais vous devriez d'abord connaître certaines lignes directrices! Après tout, vous devez connaître les règles pour les enfreindre! Consultez les spécifications créatives de chaque type de message ou les détails créatifs globaux ci-dessous."
description: "Soyez créatif avec les cartes de contenu ! Cet article de référence couvre des détails créatifs tels que les recommandations de taille d’image et le comportement de rejet dans les trois types de Cartes de Contenu."
guide_featured_title: "Caractéristiques de type de message"
guide_featured_list:
  - 
    name: Classique
    link: '/docs/user_guide/message_building_by_channel/content_cards/creative_details/#classic'
    image: /assets/img/icon-classic-cc.png
  - 
    name: Image sous-titrée
    link: '/docs/user_guide/message_building_by_channel/content_cards/creative_details/#captioned-image'
    image: /assets/img/captioned-cc.png
  - 
    name: Bannière
    link: '/docs/user_guide/message_building_by_channel/content_cards/creative_details/#banner'
    image: /assets/img/icon-banner-cc.png
channel:
  - cartes de contenu
tool: Médias
---

## Types de carte de contenu

### Classique

La carte classique est idéale pour la messagerie standard et les notifications ou même pour catégoriser visuellement les messages avec des icônes. L'image est optionnelle, mais elle doit être à un ratio 1:1.

!\[Classic\]\[1\]{: height="50%" width="50%"}

| Capacité de la carte | Détails du produit                                                                                                                                   |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Texte de l'en-tête   | 18px ; Bolded <br> Une ligne de texte est idéale. <br> Vous pouvez utiliser Liquid ici pour personnaliser votre message.                 |
| Texte du message     | 13px ; Poids normal <br> Deux à quatre lignes de texte est idéal. <br> Vous pouvez utiliser Liquid ici pour personnaliser votre message. |
| Texte du lien        | Optionnel. <br> 13px <br> Lien vers une page Web ou un lien profond vers votre application.                                              |
| Image                | Optionnel. <br> Doit être un ratio 1:1. <br> Nous recommandons une qualité d'image de 60px par 60px.                                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Image sous-titrée

La carte d'image sous-titrée est un excellent moyen de montrer et d'attirer l'attention sur un contenu important, comme une grosse vente ou une nouvelle fonctionnalité d'application!

!\[Image captionnée\]\[2\]{: height="50%" width="50%"}

| Capacité de la carte | Détails du produit                                                                                                                                   |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| Texte de l'en-tête   | 18px ; Bolded <br> Une ligne de texte est idéale. <br> Vous pouvez utiliser Liquid ici pour personnaliser votre message.                 |
| Texte du message     | 13px ; Poids normal <br> Deux à quatre lignes de texte est idéal. <br> Vous pouvez utiliser Liquid ici pour personnaliser votre message. |
| Texte du lien        | Optionnel. <br> 13px <br> Lien vers une page Web ou un lien profond vers votre application.                                              |
| Image                | Le rapport suggéré est de 4:3. <br> Largeur minimale de 600px.  <br> Prise en charge du PNG, du JPEG et du GIF.                          |
{: .reset-td-br-1 .reset-td-br-2}

### Bannière

Si vous voulez de la fantaisie, la carte de bannière est pour vous ! est complètement coutume à ce que vous voulez qu'il soit. Il vous suffit de créer votre contenu ailleurs et de le télécharger pour une belle carte qui est la vôtre.

!\[Banner\]\[3\]{: height="50%" width="50%"}

| Capacité de la carte | Détails du produit                                                                                                                         |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Carte associée       | Optionnel. <br> 13px <br> En cliquant sur le lien de comportement vers une page Web ou un lien profond vers votre application. |
| Image                | Tout rapport d'aspect supporté. <br> Largeur minimale de 600px.  <br> Prise en charge du PNG, du JPEG et du GIF.               |
{: .reset-td-br-1 .reset-td-br-2}

## Détails de la création {#general}

Les cartes de contenu sont fournies avec une excellente fonctionnalité « Out-of-the-box». Pour le moment, le style de la carte ne peut pas être fait nativement dans votre compte Braze, mais vous pouvez styliser votre Carte de Contenu par type et le flux de la Carte de Contenu pendant l'intégration. Plus d'informations sur les Cartes de Contenu peuvent être trouvées sur notre [page de Personnalisation][4].

### Comportement de rejet

Pour qu'un utilisateur rejette une carte, il peut soit la balayer sur mobile, ou utilisez une fonction `fermer X` , comme indiqué ci-dessous. Le `x` apparaîtra au survol pour le SDK Web uniquement.

!\[Comportement de Remise\]\[5\]{: height="70%" width="70%"}

Si un utilisateur a rejeté toutes ses cartes ou si vous n'avez pas poussé de nouvelles mises à jour, le flux de l'utilisateur ressemblera généralement à ceci :

!\[Fil vide\]\[6\]{: height="50%" width="50%"}

### Utiliser les GIFs dans les Cartes de Contenu

| Cartes de contenu pour Android                                                                                                                                                 | Cartes de contenu pour iOS | Cartes de contenu pour le Web |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- | ----------------------------- |
| [Installer la bibliothèque d'images personnalisée.]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/#gifs-news-content-cards) | Inclus dans l'intégration. | Inclus dans l'intégration.    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
[1]: {% image_buster /assets/img/classic-cc.png %} [2]: {% image_buster /assets/img/captioned-image-cc.png %} [3]: {% image_buster /assets/img/banner-cc. ng %} [5]: {% image_buster /assets/img/dismissal-cc.png %} [6]: {% image_buster /assets/img/empty-cc.png %}

[4]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize/
