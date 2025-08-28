---
nav_title: Détails créatifs
article_title: Détails créatifs pour les cartes de contenu
page_order: 1
description: "Cet article traite de détails liés à la création, tels que les recommandations en matière de taille d'image et le comportement en matière de fermeture pour les trois types de cartes de contenu standard."
channel:
  - content cards
tool: Media

---

# Détails créatifs pour les cartes de contenu

> La personnalisation des cartes de contenu et de leur flux ne peut être effectuée lors de la création de la campagne. Vous devez travailler avec vos ingénieurs et développeurs pour créer et personnaliser vos cartes. Pour plus de détails techniques, consultez notre [documentation destinée aux développeurs]({{site.baseurl}}/developer_guide/getting_started/customization_overview).

## Types de carte de contenu

{% tabs %}
{% tab Classique %}

La carte classique est idéale pour les communications et les notifications standard, ou même pour catégoriser visuellement les messages avec des icônes. L’image est facultative, mais elle doit être au rapport 1 :1.

![Image d'une carte classique avec des détails recommandés et un exemple de carte classique]({% image_buster /assets/img/content_card_classic.png %}){: style="max-width:45%;border:0;"}

| Capacité de la carte | Détails |
| --- | ---|
| Texte de l’en-tête | 18 px ; Gras <br> Avec idéalement une seule ligne de texte. <br> Vous pouvez utiliser Liquid ici pour personnaliser votre message. |
| Texte du message | 13 px ; Normal <br> Avec idéalement deux à quatre lignes de texte. <br> Vous pouvez utiliser Liquid ici pour personnaliser votre message. |
| Texte du lien | Facultatif. <br> 13 px <br> Lien vers une page Web ou lien profond à l'intérieur de votre application. |
| Image | Facultatif. <br> Doit être au rapport 1:1. <br> Nous recommandons une qualité d'image de 60 x 60 px. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Image avec légende %}

La carte de type image légendée est un excellent moyen de mettre en valeur et d'attirer l'attention sur un contenu important, comme une grande vente ou une nouvelle fonctionnalité de l'application.

![Image d'une carte d'image légendée avec les détails recommandés et un exemple de carte d'image légendée]({% image_buster /assets/img/content_card_captioned.png %}){: style="max-width:90%;border:0;"}

| Capacité de la carte | Détails |
| --- | ---|
| Texte de l’en-tête | 18 px ; Gras <br> Avec idéalement une seule ligne de texte. <br> Vous pouvez utiliser Liquid ici pour personnaliser votre message. |
| Texte du message | 13 px ; Normal <br> Avec idéalement deux à quatre lignes de texte. <br> Vous pouvez utiliser Liquid ici pour personnaliser votre message. |
| Texte du lien | Facultatif. <br> 13 px <br> Lien vers une page Web ou lien profond à l'intérieur de votre application. |
| Image | Un rapport 4:3 est suggéré. <br> Largeur minimale de 600 px.  <br> Prend en charge les formats PNG, JPEG et GIF à haute résolution. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Image seulement %}

Si vous souhaitez un contrôle plus créatif, la carte image seule est faite pour vous. Créez votre image à l'aide de l'outil de votre choix et téléchargez-la sur ce type de carte.

![Image d'une carte de contenu avec détails recommandés et exemple d'image seulement]({% image_buster /assets/img/content_card_banner.png %}){: style="max-width:45%;border:0;"}

| Capacité de la carte | Détails |
| --- | ---|
| Carte liée | Facultatif. <br> 13 px <br> Comportement lors du clic avec lien vers une page Web ou lien profond dans votre application. |
| Image | Tous les rapports hauteur/largeur sont pris en charge. <br> Largeur minimale de 600 px.  <br> Prend en charge les formats PNG, JPEG et GIF à haute résolution. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Détails créatifs globaux {#general}

Les cartes de contenu sont dotées dès le départ d’excellentes fonctionnalités. Actuellement, la définition du style des cartes ne peut pas être effectuée nativement depuis votre compte Braze, mais vous pouvez définir le style de vos cartes de contenu en fonction de leur type et de leur flux au moment de l’intégration. Pour plus d'informations, reportez-vous à la section [Personnaliser les cartes de contenu]({{site.baseurl}}/developer_guide/content_cards/).

### Comportement de fermeture

Pour refuser une carte, l’utilisateur peut faire un swipe (balayage) sur son mobile ou utiliser une fonction `close X` comme illustré dans la capture d’écran suivante. Le `x` apparaîtra sur le curseur avec le SDK Web uniquement.

![Image montrant les comportements de fermeture de la carte de contenu]({% image_buster /assets/img/dismissal-cc.png %})

Si un utilisateur a fermé toutes ses cartes ou si vous n’avez pas envoyé de mises à jour, le flux de l’utilisateur ressemblera généralement à ceci :

![Image d'une carte de contenu vide]({% image_buster /assets/img/empty-cc.png %}){: style="max-width:45%"}

{% alert tip %}
Veillez à la pertinence des cartes de contenu en les configurant pour qu'elles soient fermées lorsque l'utilisateur effectue des actions pertinentes. Par exemple, configurez les cartes de contenu promotionnelles pour qu'elles soient fermées dès que les utilisateurs effectuent un achat, afin qu'ils ne continuent pas à voir une offre pour quelque chose qu'ils ont déjà acheté.
{% endalert %}

### Utilisation des GIF dans les cartes de contenu

| Cartes de contenu pour Android | Cartes de contenu pour iOS | Cartes de contenu pour Web |
| --- | --- |---|
| Par défaut, le SDK Android ne prend pas en charge les GIF animés. Pour plus de détails sur l'activation de la prise en charge des GIF, reportez-vous à [GIFs]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs/?sdktab=android). | Par défaut, le SDK Swift ne prend pas en charge les GIF animés. Pour plus de détails sur l'activation de la prise en charge du format GIF, reportez-vous au [didacticiel sur la prise en charge du format GIF](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support). | La prise en charge du format GIF est incluse par défaut dans l'intégration SDK Web. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

<br><br>

