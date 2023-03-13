---
nav_title: Cartes de contenu dans Canvas
article_title: Cartes de contenu dans Canvas
page_order: 7
page_type: reference
description: "Cet article de référence décrit les fonctionnalités et les nuances spécifiques à l’utilisation de cartes de contenu, comme canal de communication dans Canvas."
tool: Canvas
channel: cartes de contenu

---

# Cartes de contenu dans Canvas

Des cartes de contenu peuvent être envoyées à vos clients dans le cadre de leur parcours Canvas. Cet article décrit les fonctionnalités et les nuances spécifiques à l’utilisation de cartes de contenu, comme canal de communication dans Canvas.

Comme pour d’autres canaux de communication Canvas, les cartes de contenu seront envoyées sur l’appareil d’un utilisateur, lorsqu’elles répondent aux critères d’audience et de ciblage indiqués pour son étape. Une fois la carte de contenu envoyée, elle sera disponible dans le flux de chaque utilisateur éligible à la prochaine mise à jour du flux de cartes.

![][1]

L’[Expiration](#content-card-expiration) et le [Comportement d’avancement](#advancement-behavior-options) constituent deux options qui modifieront la façon dont l’étape de Carte de contenu interagira avec Canvas.

## Expiration de la carte de contenu {#content-card-expiration}

Lorsque vous rédigez une nouvelle carte de contenu, vous pouvez choisir la date à laquelle elle expirera dans le flux de l’utilisateur, en fonction de l’heure d’envoi. La date d’expiration commence lorsqu’un utilisateur atteint son composant de Canvas et que la carte est envoyée.

Si une carte envoyée expire avant qu’un utilisateur ne puisse la consulter dans votre application, elle sera supprimée de son flux lors de la prochaine mise à jour de ses cartes.

{% alert important %}
La carte de contenu sera disponible jusqu’à ce qu’elle expire, même si l’utilisateur est passé aux étapes suivantes. Si vous ne souhaitez pas que la carte de contenu subsiste lorsque les étapes suivantes du Canvas sont livrées, vérifiez que la vitesse d’expiration est plus courte que le délai dans les étapes suivantes.
{% endalert %}

## Options de comportement d’avancement {#advancement-behavior-options}

{% alert important %}
Depuis le 28 février 2023, vous ne pouvez plus créer ou dupliquer de Canvas à l’aide de l’éditeur Canvas d’origine. Cette section est disponible à titre de référence lorsque vous comprenez comment fonctionne le comportement d’avancement pour les étapes avec des cartes de contenu.
{% endalert %}

{% alert note %}
Dans Canvas Flow, les composants de message font automatiquement progresser tous les utilisateurs qui entrent dans l’étape. Il n’est pas nécessaire de spécifier le comportement d’avancement des messages, ce qui facilite la configuration générale de l’étape. Si vous souhaitez implémenter l’option **Avancement lors de l’envoi du message**, ajoutez un [parcours d’audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) distinct pour filtrer les utilisateurs qui n’ont pas reçu l’étape précédente.
{% endalert %}

L’option Comportement d’avancement vous permet de contrôler le moment où un utilisateur doit avancer à l’étape suivante à laquelle il est éligible. Les étapes envoyant [uniquement des cartes de contenu](#steps-with-in-content-cards-only) ont des options d’avancement différentes des [étapes avec plusieurs types de messages](#steps-with-multiple-message-channels) (notification push, e-mail, etc.). Pour les cartes de contenu dans le flux de travail Canvas Flow, cette option est définie pour faire avancer immédiatement l’audience.

### Étapes avec uniquement des cartes de contenu {#steps-with-in-content-cards-only}

Si une étape contient uniquement des cartes de contenu (et aucun autre canal de communication), vous pouvez contrôler le comportement d’avancement à l’aide des options suivantes :

| Option | Description |
|---|---|
| Avancement lors de l’envoi du message | Les utilisateurs avanceront aux étapes suivantes du Canvas lorsque la carte de contenu aura été correctement envoyée. Utilisez cette option lorsque vous souhaitez que les utilisateurs avancent uniquement si la carte est envoyée et non annulée. |
| Audience avancée immédiatement | Les utilisateurs avanceront aux étapes suivantes du Canvas en cas de tentative d’envoi de Carte de contenu. Si la carte est annulée et n’est pas envoyée, les utilisateurs avanceront quand même à l’étape suivante. Utilisez cette option lorsque vous souhaitez que les utilisateurs avancent, que la carte de contenu ait été correctement envoyée ou annulée. |
{: .reset-td-br-1 .reset-td-br-2}

![][2]

### Composants avec plusieurs canaux {#steps-with-multiple-message-channels}

Les composants Canvas avec une carte de contenu et un autre canal de communication disposent des options d’avancement suivantes :

| Option | Description |
|---|---|
| Avancement lors de l’envoi du message | Les utilisateurs avanceront jusqu’aux étapes suivantes du Canvas lorsqu’au moins un des types de messages de cette étape a été correctement envoyé.|
| Audience avancée immédiatement | Lorsque cette option est sélectionnée, toute personne qui se trouve dans l’audience du composant, avancera aux étapes suivantes une fois le délai passé, que le message indiqué ait été vu ou pas.  <br> <br> _Les utilisateurs doivent faire correspondre le segment du composant et les critères de filtre pour avancer aux étapes suivantes._ |
{: .reset-td-br-1 .reset-td-br-2}

![][3]

## Reporting et analytique

Après le lancement d’une étape Cartes de contenu dans Canvas, vous pouvez commencer à analyser plusieurs indicateurs différents pour cette étape. Ces indicateurs contiennent le nombre de messages envoyés, les destinataires uniques, les taux de conversion, le revenu total et bien plus.

![][4]

Pour en savoir plus sur les indicateurs disponibles et leurs définitions, consultez notre [Glossaire des indicateurs de rapport][6].

## Cas d’utilisation

#### Offres promotionnelles

Ajoutez des cartes au flux d’un utilisateur lorsqu’il est éligible à des promotions et des publicités spécifiques. Par exemple, si un utilisateur devient éligible pour une nouvelle offre à la suite d’une action ou d’un achat, un Canvas vous permet de lui envoyer une carte de contenu en plus d’autres canaux de communication, de sorte que l’offre soit disponible à sa prochaine connexion à l’application.

#### Boîte de réception de notification push

Il arrive parfois qu’un utilisateur soit amené à rejeter une notification push ou supprimer un e-mail et que vous souhaitiez lui envoyer un rappel ou renouveler l’offre au cas où il change d’avis.

Canvas vous permet d’ajouter un composant pour envoyer une carte de contenu et une notification push pour proposer aux utilisateurs une « boîte de réception » de cartes permanente, pour mieux correspondre aux messages promotionnels envoyés via notification push. 

#### Plusieurs flux en fonction des catégories

Vous pouvez séparer vos cartes de contenu en plusieurs flux, en fonction de catégories, par exemple les différents sujets que les utilisateurs peuvent parcourir ou les flux transactionnels et marketing. Pour plus d’informations sur la création de flux multiples à l’aide de paires clé-valeur, consultez nos guides pour [SDK Web][7] et [SDK Android][8].


[1]: {% image_buster /assets/img_archive/content-cards-in-canvas.png %}
[2]: {% image_buster /assets/img_archive/content-cards-in-canvas-single-channel.png %}
[3]: {% image_buster /assets/img_archive/content-cards-in-canvas-multiple-channels.png %}
[4]: {% image_buster /assets/img_archive/content-cards-in-canvas-analytics.png %}
[6]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/multiple_feeds/
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/multiple_feeds/
