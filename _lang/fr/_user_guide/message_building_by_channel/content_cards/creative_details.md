---
nav_title: Détails créatifs
article_title: Détails créatifs
page_order: 1
layout: dev_guide
guide_top_header: "Détails créatifs"
guide_top_text: "Donnez libre cours à votre créativité avec les cartes de contenu ! Mais vous devez en premier lieu connaître certaines des recommandations ! Après tout, il faut connaître les règles pour les enfreindre ! Consultez les spécifications créatives ou les détails créatifs globaux suivants pour chaque type de message individuel."
description: "Cet article d’accueil couvre les détails créatifs tels que les recommandations de taille d’image et le comportement de fermeture pour les trois types de carte de contenu."

guide_featured_title: "Spécifications créatives pour les types message"
guide_featured_list:
- name: Classique
  link: /docs/user_guide/message_building_by_channel/content_cards/creative_details/#classic
  image: /assets/img/braze_icons/layout-top.svg
- name: Image avec légende
  link: /docs/user_guide/message_building_by_channel/content_cards/creative_details/#captioned-image
  image: /assets/img/braze_icons/layout-alt-03.svg
- name: Bannière
  link: /docs/user_guide/message_building_by_channel/content_cards/creative_details/#banner
  image: /assets/img/braze_icons/layout-bottom.svg

channel:
  - cartes de contenu
tool: Media

---

## Types de carte de contenu

### Classique

La carte classique est idéale pour les communications et les notifications standard, ou même pour catégoriser visuellement les messages avec des icônes. L’image est facultative, mais elle doit être au rapport 1 :1.  

![Image d’une carte classique avec des détails recommandés et un exemple de carte classique][1]{: height="50%" width="50%"}

| Capacité de la carte | Détails |
| --- | ---|
| Texte de l’en-tête | 18px; En gras <br> Avec idéalement une seule ligne de texte. <br> Vous pouvez utiliser Liquid ici pour personnaliser votre message. |
| Texte du message | 13px; Poids normal <br> Avec idéalement deux à quatre lignes de texte. <br> Vous pouvez utiliser Liquid ici pour personnaliser votre message. |
| Texte du lien | Facultatif. <br> 13 px <br> Lien vers la page Web ou lien profond vers votre application. |
| Image | Facultatif. <br> Doit être au rapport 1:1. <br> Nous recommandons une qualité d’image de 60 px par 60 px. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Image avec légende

La carte Image avec Légende est un excellent moyen de montrer et attirer l’attention sur un contenu important, comme une grosse vente ou une nouvelle fonctionnalité de l’application !

![Carte Image avec Légende avec les détails recommandés et un exemple de Carte Image avec Légende][2]{: height="50%" width="50%"}

| Capacité de la carte | Détails |
| --- | ---|
| Texte de l’en-tête | 18px; En gras <br> Avec idéalement une seule ligne de texte. <br> Vous pouvez utiliser Liquid ici pour personnaliser votre message. |
| Texte du message | 13px; Poids normal <br> Avec idéalement deux à quatre lignes de texte. <br> Vous pouvez utiliser Liquid ici pour personnaliser votre message. |
| Texte du lien | Facultatif. <br> 13 px <br> Lien vers la page Web ou lien profond vers votre application. |
| Image | Un rapport 4:3 est suggéré. <br> Largeur minimum de 600 px.  <br> Prend en charge les PNG, JPEG et GIF haute résolution. |
{: .reset-td-br-1 .reset-td-br-2}

### Bannière

Si vous voulez ajouter un peu de fantaisie, la carte de bannière est faite pour vous ! Elle est entièrement personnalisée pour correspondre à vos attentes. Créez simplement votre contenu ailleurs et chargez-le pour avoir une carte magnifique qui vous ressemble !

![Image d’une bannière avec des détails recommandés et un exemple de bannière][3]{: height="50%" width="50%"}

| Capacité de la carte | Détails |
| --- | ---|
| Carte liée | Facultatif. <br> 13 px <br> Comportement lors du clic avec lien vers une page Web ou lien profond dans votre application. |
| Image | Tous les rapports sont pris en charge. <br> Largeur minimum de 600 px.  <br> Prend en charge les PNG, JPEG et GIF haute résolution. |
{: .reset-td-br-1 .reset-td-br-2}

## Détails créatifs {#general}

Les cartes de contenu sont dotées dès le départ d’excellentes fonctionnalités. Actuellement, la définition du style des cartes ne peut pas être effectuée nativement depuis votre compte Braze, mais vous pouvez définir le style de vos cartes de contenu en fonction de leur type et de leur flux au moment de l’intégration. Reportez-vous à [Personnalisation des cartes de contenu][4] pour plus d’informations.

### Comportement de fermeture

Pour refuser une carte, l’utilisateur peut faire un swipe (balayage) sur son mobile ou utiliser une fonction `close X` comme illustré dans la capture d’écran suivante. Le `x` apparaîtra sur le curseur avec le SDK Web uniquement.

![Image montrant le swipe ou la fermeture d’une carte pour la refuser][5]{: height="70%" width="70%"}

Si un utilisateur a fermé toutes ses cartes ou si vous n’avez pas envoyé de mises à jour, le flux de l’utilisateur ressemblera généralement à ceci :

![Image d’un flux de cartes de contenu vide][6]{: height="50%" width="50%"}

### Utilisation des GIF dans les cartes de contenu

| Cartes de contenu pour Android | Cartes de contenu pour iOS | Cartes de contenu pour Web |
| --- | --- |---|
| [Installer la bibliothèque d’images personnalisées.]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/gifs/) | Inclus dans l’intégration. | Inclus dans Intégration. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

<br><br>

[1]: {% image_buster /assets/img/classic-cc.png %}
[2]: {% image_buster /assets/img/captioned-image-cc.png %}
[3]: {% image_buster /assets/img/banner-cc.png %}
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/customize/
[5]: {% image_buster /assets/img/dismissal-cc.png %}
[6]: {% image_buster /assets/img/empty-cc.png %}
