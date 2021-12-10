---
nav_title: Cartes de contenu dans la toile
article_title: Cartes de contenu dans Canvas
page_order: 7
page_type: Référence
description: "Cet article de référence décrit les caractéristiques et les nuances propres à l'utilisation des Cartes de Contenu comme canal de messagerie dans Canvas."
tool: Toile
channel: cartes de contenu
---

# Cartes de contenu dans Canvas

Les cartes de contenu peuvent être envoyées à vos clients dans le cadre de leur voyage sur Canvas . Cet article décrit les fonctionnalités et les nuances propres à l'utilisation des Cartes de Contenu comme canal de messagerie dans Canvas.

Comme les autres canaux de messagerie Canvas Les cartes de contenu seront envoyées à l'appareil d'un utilisateur lorsqu'il répond aux critères d'audience et de ciblage spécifiés pour cette étape. Une fois la carte de contenu envoyée, elle sera disponible dans le fil de chaque utilisateur éligible la prochaine fois que le flux de sa carte sera actualisé.

!\[cartes de contenu in canvas\]\[1\]

Deux options qui vont changer la façon dont l'étape de la carte de contenu interagira avec Canvas sont son [Expiration](#content-card-expiration) et [Comportement d'avancement](#advancement-behavior-options).

## Expiration de la carte de contenu {#content-card-expiration}

Lorsque vous composez une nouvelle carte de contenu, vous avez la possibilité de choisir quand elle doit expirer du flux de l'utilisateur, en fonction de son heure d'envoi. La durée d'expiration commence quand un utilisateur atteint l'étape Canvas et que la carte est envoyée.

Si une carte envoyée expire avant qu'un utilisateur ne la consulte dans votre application, il sera retiré de leur flux la prochaine fois que leurs cartes seront actualisées.

{% alert important %}
 La carte de contenu sera disponible jusqu'à ce qu'elle expire, même si l'utilisateur est passé à l'étape suivante. Si vous ne voulez pas que la carte de contenu soit en direct lorsque les prochaines étapes du Canvas sont livrées, s'assurer que l'expiration est plus courte que le délai lors des étapes suivantes.
{% endalert %}

## Options de comportement d'avancement {#advancement-behavior-options}

L'option de comportement d'avancement vous permet de contrôler quand un utilisateur doit passer à sa prochaine étape admissible. [Les étapes qui n'envoient que des cartes de contenu](#steps-with-in-content-cards-only) ont des options d'avancement différentes que [étapes avec plusieurs types de messages](#steps-with-multiple-message-channels) (push, email, etc.).

### Étapes uniquement avec des cartes de contenu {#steps-with-in-content-cards-only}

Si une étape ne contient que des cartes de contenu (et aucun autre canal de messagerie), vous pouvez contrôler le comportement d'avancement avec les options suivantes :

!\[content-card-in-canvas-single-channel.png\]\[2\]

| Option                                  | Libellé                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Avancer lorsque le message a été envoyé | Les utilisateurs passeront aux étapes suivantes de la toile lorsque la carte de contenu aura été envoyée avec succès. Utilisez cette option lorsque vous voulez que les utilisateurs avancent seulement si la carte sera envoyée et non abandonnée.                                                                                             |
| Audience immédiatement Avancée          | Les utilisateurs passeront aux étapes suivantes de Canvas lorsque la carte de contenu sera envoyée. Si la carte est abandonnée et non envoyée, les utilisateurs passeront toujours à l'étape suivante. Utilisez cette option lorsque vous voulez que les utilisateurs avancent, que la carte de contenu soit envoyée avec succès ou abandonnée. |
{: .reset-td-br-1 .reset-td-br-2}

### Étapes avec plusieurs canaux {#steps-with-multiple-message-channels}

!\[content-cards-in-canvas-multiple-channels.png\]\[3\]

Les étapes de Canvas avec une carte de contenu et un autre canal de messagerie ont les options d'avancement suivantes :

| Option                                  | Libellé                                                                                                                                                                                                                                                                                                    |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Avancer lorsque le message a été envoyé | Les utilisateurs passeront aux étapes suivantes du Canvas quand au moins un des types de messages de cette étape a été envoyé avec succès.                                                                                                                                                                 |
| Audience immédiatement Avancée          | Lorsque cette option est sélectionnée, tous les participants de l'étape passeront aux étapes suivantes après le délai, s'ils ont vu ou non le message noté.  <br> <br> _Les utilisateurs doivent correspondre au segment de l'étape et filtrer les critères pour passer aux étapes suivantes._ |
{: .reset-td-br-1 .reset-td-br-2}

## Rapports et analyses

Après avoir lancé une étape sur Canvas d'une carte de contenu, vous pouvez commencer à analyser plusieurs métriques différentes pour cette étape. Ces paramètres comprennent le nombre de messages envoyés, les destinataires uniques, les taux de conversion, les revenus totaux et plus encore.

Pour plus d'informations sur les métriques disponibles et leurs définitions, consultez notre [Glossaire des métriques de rapport][6].

!\[content-card-in-canvas-analytics.png\]\[4\]

## Cas d'utilisation

#### Offres promotionnelles

Ajoutez des cartes au flux d'un utilisateur qui se qualifie pour des promotions et des publicités spécifiques. Par exemple, si un utilisateur devient éligible à une nouvelle offre après avoir effectué une action ou effectué un achat, en utilisant Canvas vous pouvez leur envoyer une Carte de Contenu, en plus des autres salons de messagerie, de sorte que la prochaine fois qu'ils ouvriront l'application, l'offre est disponible pour eux.

#### Boîte de réception des notifications push

Il y a des moments où un utilisateur peut rejeter une notification push ou supprimer un e-mail, mais vous voulez leur rappeler ou promouvoir l'offre au cas où ils changeraient d'avis.

Utilisation de Canvas, vous pouvez ajouter une étape qui envoie à la fois une fiche de contenu et une notification Push pour donner aux utilisateurs une boîte de réception persistante de cartes qui s'alignent avec les messages promotionnels envoyés via Push.

#### Flux multiples basés sur des catégories

Vous pouvez séparer vos cartes de contenu en plusieurs flux en fonction de catégories. Par exemple, différents sujets que les utilisateurs peuvent consulter, ou transactionnels vs flux marketing. Pour plus d'informations, consultez ces guides pour créer différents flux en utilisant des paires clé-valeur :

* [Flux multiples pour SDK Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/multiple_feeds/)
* [Flux multiples pour le SDK Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/multiple_feeds/)
[1]: {% image_buster /assets/img_archive/content-cards-in-canvas.png %} [2]: {% image_buster /assets/img_archive/content-cards-in-canvas-single-channel. ng %} [3]: {% image_buster /assets/img_archive/content-cards-in-canvas-multiple-channels.png %} [4]: {% image_buster /assets/img_archive/content-cards-in-canvas-analytics.png %}

[6]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
