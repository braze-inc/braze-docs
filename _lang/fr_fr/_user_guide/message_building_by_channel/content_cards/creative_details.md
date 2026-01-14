---
nav_title: Détails créatifs
article_title: Détails créatifs pour les cartes de contenu
page_order: 1
description: "Cet article traite de détails créatifs tels que les recommandations en matière de taille d'image et le comportement en matière de fermeture pour les trois types de cartes de contenu standard."
channel:
  - content cards
tool: Media

---

# Détails créatifs pour les cartes de contenu

> La personnalisation des cartes de contenu et du flux dans lequel elles se trouvent ne peut pas se faire pendant le processus de création de la campagne. Vous devez travailler avec vos ingénieurs et vos développeurs pour créer et personnaliser vos cartes. Pour plus de détails techniques, consultez notre [documentation destinée aux développeurs]({{site.baseurl}}/developer_guide/getting_started/customization_overview).

## Types de cartes de contenu

{% tabs %}
{% tab Classic %}

La carte classique est idéale pour l'envoi de messages et de notifications standard ou même pour classer visuellement les messages à l'aide d'icônes. L'image est facultative, mais elle doit avoir un rapport de 1:1.

Image d'une carte classique avec les détails recommandés et un exemple de carte classique]({% image_buster /assets/img/content_card_classic.png %}){: style="max-width:45%;border:0;"}

| Capacité de la carte | Détails |
| --- | ---|
| Texte de l'en-tête | 18px ; Gras <br> Une ligne de texte est idéale. <br> Vous pouvez utiliser ici Liquid pour personnaliser votre message. |
| Texte du message | 13px ; Poids normal <br> Un texte de deux à quatre lignes est idéal. <br> Vous pouvez utiliser ici Liquid pour personnaliser votre message. |
| Texte du lien | En option. <br> 13 px <br> Lien vers une page web ou lien profond à l'intérieur de votre application. |
| Image | En option. <br> Le rapport doit être de 1:1. <br> Nous recommandons une qualité d'image de 60 x 60 px. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Captioned Image %}

La carte de type image légendée est un excellent moyen de mettre en valeur et d'attirer l'attention sur un contenu important, comme une grande vente ou une nouvelle fonctionnalité de l'application.

Image d'une carte d'image légendée avec les détails recommandés et un exemple de carte d'image légendée]({% image_buster /assets/img/content_card_captioned.png %}){: style="max-width:90%;border:0;"}

| Capacité de la carte | Détails |
| --- | ---|
| Texte de l'en-tête | 18px ; Gras <br> Une ligne de texte est idéale. <br> Vous pouvez utiliser ici Liquid pour personnaliser votre message. |
| Texte du message | 13px ; Poids normal <br> Un texte de deux à quatre lignes est idéal. <br> Vous pouvez utiliser ici Liquid pour personnaliser votre message. |
| Texte du lien | En option. <br> 13 px <br> Lien vers une page web ou lien profond à l'intérieur de votre application. |
| Image | Le rapport suggéré est de 4:3. <br> Largeur minimale de 600 px.  <br> Prend en charge les formats PNG, JPEG et GIF à haute résolution. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Image-only %}

Si vous souhaitez un contrôle plus créatif, la carte image seule est faite pour vous. Créez votre image à l'aide de l'outil de votre choix et téléchargez-la sur ce type de carte.

Image d'une carte de contenu avec des détails recommandés et un exemple d'image.]({% image_buster /assets/img/content_card_banner.png %}){: style="max-width:45%;border:0;"}

| Capacité de la carte | Détails |
| --- | ---|
| Carte liée | En option. <br> 13 px <br> Le comportement au clic renvoie à une page web ou à un lien profond à l'intérieur de votre application. |
| Image | Tous les rapports hauteur/largeur sont pris en charge. <br> Largeur minimale de 600 px.  <br> Prend en charge les formats PNG, JPEG et GIF à haute résolution. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Détails créatifs globaux {#general}

Les cartes de contenu sont dotées d'une grande fonctionnalité dès le départ. Pour l'instant, le stylisme des cartes ne peut pas être effectué de manière native dans votre compte Braze, mais vous pouvez styliser votre carte de contenu par type et le flux de la carte de contenu lors de l'intégration. Pour plus d'informations, reportez-vous à la section [Personnaliser les cartes de contenu]({{site.baseurl}}/developer_guide/content_cards/).

### Comportement en cas de licenciement

Pour qu'un utilisateur puisse fermer une carte, il peut soit la glisser sur le mobile, soit utiliser une fonction `close X`, comme le montre la capture d'écran suivante. Le site `x` apparaîtra au survol de la page uniquement pour le SDK Web.

Image montrant les comportements de fermeture de la carte de contenu.]({% image_buster /assets/img/dismissal-cc.png %})

Si un utilisateur a fermé toutes ses cartes ou si vous n'avez pas diffusé de nouvelles mises à jour, son fil d'actualité ressemblera généralement à ceci :

\![Image d'un flux de cartes de contenu vide]({% image_buster /assets/img/empty-cc.png %}){: style="max-width:45%"}

{% alert tip %}
Veillez à la pertinence des cartes de contenu en les configurant pour qu'elles soient fermées lorsque l'utilisateur effectue des actions pertinentes. Par exemple, configurez les cartes de contenu promotionnelles pour qu'elles soient fermées dès que les utilisateurs effectuent un achat, afin qu'ils ne continuent pas à voir une offre pour quelque chose qu'ils ont déjà acheté.
{% endalert %}

### Utiliser les GIF dans les cartes de contenu

| Cartes de contenu pour Android | Cartes de contenu pour iOS | Cartes de contenu pour le web |
| --- | --- |---|
| Le SDK Android ne prend pas en charge les GIF animés par défaut. Pour plus de détails sur l'activation de la prise en charge des GIF, reportez-vous à [GIFs]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs/?sdktab=android). | Par défaut, le SDK Swift ne prend pas en charge les GIF animés. Pour plus de détails sur l'activation de la prise en charge du format GIF, reportez-vous au [didacticiel sur la prise en charge du format GIF](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support). | La prise en charge du format GIF est incluse par défaut dans l'intégration SDK Web. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

<br><br>

