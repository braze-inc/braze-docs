---
nav_title: Création de carte
article_title: Création de carte
alias: /card_creation/
description: "Cet article décrit les différences entre la création de cartes de contenu au moment du lancement de la campagne ou de l'entrée dans l'étape du canvas par rapport à la première impression."
page_order: 0
tool: Campaigns
channel:
  - content cards
---

# Création de carte

> Vous pouvez choisir le moment où Braze évalue l'éligibilité de l'audience et la personnalisation pour les nouvelles campagnes de cartes de contenu et les étapes du canvas en spécifiant le moment de la création de la carte.

## Conditions préalables

Pour profiter de cette fonctionnalité, vous devez effectuer une mise à niveau vers les versions minimales du SDK suivantes :

{% sdk_min_versions swift:5.2.0 android:23.0.0 web:4.2.0 %}

Après la mise à niveau du SDK, vos utilisateurs mobiles doivent mettre à niveau leur application. Vous pouvez filtrer l’audience de votre campagne ou de votre canvas pour [ne cibler que les utilisateurs de ces versions minimales d'application]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).

## Aperçu

{% tabs %}
{% tab Campaign %}

Vous pouvez choisir le moment où Braze crée une carte à l'étape **Livraison** lors de la création d'une nouvelle [campagne de cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/) avec une livraison planifiée.

![Section Contrôles de la carte de contenu lors de la modification de la livraison d’une carte de contenu planifiée.]({% image_buster /assets/img_archive/card_creation.png %})

Les options suivantes sont disponibles :

- **Lors du lancement de la campagne :** Le comportement par défaut précédent pour les cartes de contenu. Braze calcule l’éligibilité et la personnalisation de l’audience au lancement de la campagne, puis crée la carte et la stocke jusqu’à ce que l’utilisateur ouvre votre application. 
- **A la première impression (recommandé) :** Lorsque l'utilisateur ouvre à nouveau votre application (démarre une nouvelle [session](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), Braze détermine les cartes de contenu auxquelles l'utilisateur a droit, modélise toute personnalisation telle que Liquid ou contenu connecté, puis crée la carte. Cette option offre généralement de meilleures performances.

Quelle que soit l'option choisie, le compte à rebours de la date d'expiration de la carte de contenu commencera lorsque la campagne sera lancée.

{% endtab %}
{% tab Canvas %}

Vous pouvez choisir le moment où Braze crée une carte dans l'onglet **Canaux de communication** d'une [étape Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) de carte de contenu.

![Section Contrôles de la carte de contenu lors de la modification de la livraison d’une carte de contenu planifiée.]({% image_buster /assets/img_archive/card_creation_canvas.png %})

Les options suivantes sont disponibles :

- **À l'entrée de l'étape :** Le comportement par défaut précédent pour les cartes de contenu. Braze calcule l'éligibilité de l'audience lorsque l'utilisateur entre dans l'étape du canvas, puis crée la carte et la stocke jusqu'à ce que l'utilisateur ouvre votre appli.
- **A la première impression (recommandé) :** Braze calcule l'éligibilité de l'audience lorsque l'utilisateur entre dans l'étape du canvas. Lorsque l'utilisateur ouvre à nouveau votre application (démarre une nouvelle [session](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), Braze modélise toute personnalisation telle que Liquid ou contenu connecté, puis crée la carte. Cette option offre de meilleures performances en matière de réception/distribution de cartes et une personnalisation plus actualisée.

Quelle que soit l'option choisie, le compte à rebours de la date d'expiration de la carte de contenu commencera lorsque l'utilisateur entrera dans l'étape du canvas.

{% alert tip %}
Si vous souhaitez que les utilisateurs anonymes voient une carte de contenu lors de leur toute première session, utilisez une campagne au lieu d'un canvas. En effet, lorsqu'un utilisateur anonyme entre dans un canvas, sa session a déjà commencé. Il n'obtiendra donc pas la carte de contenu tant qu'il n'aura pas démarré une nouvelle session.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert note %}
Pour les deux options, après la création d’une carte, Braze ne recalcule pas l’éligibilité ou la personnalisation de l’audience.
{% endalert %}

### Différences entre la création de cartes au lancement ou à l'entrée et la création de cartes lors de la première impression {#differences}

Cette section décrit les principales différences entre la création de cartes au moment du lancement de la campagne ou de l'entrée en scène et la création de cartes lors de la première impression.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
.leftHeader{font-size: 12px; font-weight: bold; background-color: #f4f4f7; text-transform: uppercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">Lorsque la campagne est lancée / À l'entrée de l'étape du canvas</th>
    <th class="tg-0pky">À la première impression</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">Quand l’utiliser</td>
    <td class="tg-0pky">Si vous avez besoin que le contenu soit instantané à un moment spécifique (heure de lancement).</td>
    <td class="tg-0pky"><ul><li>Si vous devez afficher des cartes à de nouveaux utilisateurs ou à des utilisateurs anonymes susceptibles d'entrer dans le segment après le lancement<a href="#campaign_note">(campagnes uniquement*).</a></li><li>Si vous utilisez la personnalisation et souhaitez que le contenu le plus récent soit disponible sur la carte.</li></ul></td>
  </tr>
  <tr>
    <td class="leftHeader">Audience</td>
    <td class="tg-0pky">Braze évalue l’appartenance à l’audience lorsque la campagne s’envoie.<br><br>L’éligibilité des utilisateurs nouveaux ou anonymes ne sera pas évaluée s’ils essaient d’afficher la carte après l’envoi de la campagne. Pour les campagnes récurrentes, cela se fera à l’intervalle de récurrence suivant.</td>
    <td class="tg-0pky">Braze évalue l'adhésion lors de la prochaine ouverture de votre appli par l'utilisateur (démarrage d'une session, <a href="#campaign_note">campagnes uniquement*</a>).<br><br> Ce paramètre aura une portée d’audience plus large car l’éligibilité de l’utilisateur nouveau ou anonyme sera toujours évaluée lorsqu’il essaiera d’afficher la carte. <br><br>De plus, la limite de débit (limitation du nombre de personnes qui recevront la carte) ne s'applique pas lorsqu'elle est définie sur « première impression ».</td>
  </tr>
  <tr>
    <td class="leftHeader">Personnalisation</td>
    <td class="tg-0pky">Braze évalue le Liquid, le contenu connecté et les blocs de contenu au lancement de la campagne ou lorsqu'un utilisateur entre dans l'étape du canvas. Pour les campagnes récurrentes, cela se fera à l’intervalle de récurrence suivant.</td>
    <td class="tg-0pky">Braze évalue le Liquid, le contenu connecté et les blocs de contenu au moment de la première impression ou après l’intervalle de récurrence suivant.</td>
  </tr>
  <tr>
    <td class="leftHeader">Analyse</td>
  <td class="tg-0pky"><em>Les messages envoyés</em> font référence au nombre de cartes créées et mises à disposition par Braze. Cela ne tient pas compte du fait que les utilisateurs aient consulté la fiche ou non.</td>
  <td class="tg-0pky"><em>Les messages envoyés</em> font référence au nombre de cartes que Braze envoie à un utilisateur après le début d'une session. Dans Canvas, si un utilisateur accède à l'étape sans démarrer de session, Braze n'envoie pas de carte. Par conséquent, cet indicateur peut ne pas correspondre au nombre d'utilisateurs accédant à une étape.<br><br>Bien que le nombre d'utilisateurs atteints et d'impressions reste inchangé, il est probable que le volume d'envoi (<em>Messages envoyés</em>) soit plus faible lorsque vous créez une carte lors de la première impression par rapport au lancement de la campagne ou à l'entrée dans l'étape du canvas.</td>
  </tr>
  <tr>
    <td class="leftHeader">Temps de traitement</td>
  <td class="tg-0pky">Braze génère des cartes pour chaque utilisateur éligible du segment au moment du lancement. Pour les audiences importantes, veuillez sélectionner <b>« Première impression »</b> afin que les cartes soient disponibles plus rapidement après le lancement.</td>
  <td class="tg-0pky">Braze crée une carte la première fois qu'un utilisateur tente de la consulter, ce qui peut prendre 1 à 2 secondes pour s'afficher lors de la première impression.</td>
  </tr>
</tbody>
</table>

<p id="campaign_note"><sup>* Ce scénario ne s'applique qu'aux campagnes, car l'audience Canvas est évaluée à l'entrée du canvas, et non au niveau de l'étape.</sup></p>

## Considérations

### Modification de la création de la carte après le lancement

Braze recommande de ne pas modifier la façon dont les cartes sont créées après le lancement d’une campagne. En raison des différences dans la façon dont les messages envoyés sont calculés entre les deux types de création de cartes, changer la façon dont les cartes sont créées après le lancement de la campagne peut affecter la précision de votre volume d’envoi.

### Temps de traitement potentiel

Pour les audiences importantes, veuillez sélectionner l'option permettant de créer des cartes dès la première impression afin que celles-ci soient disponibles rapidement après le lancement. Les campagnes déclenchées au début de la session peuvent également bénéficier d'un déplacement vers la création d'une première impression (disponible via la réception/distribution programmée) afin d'améliorer les performances.

Lorsque les cartes sont créées lors de la première impression, leur traitement peut prendre 1 à 2 secondes. La durée de ce temps de traitement dépend de divers facteurs, tels que la taille de la carte et la complexité des options de modélisation du message. Par exemple, le temps de traitement des cartes utilisant le Contenu connecté sera au moins aussi long que le temps de réponse du Contenu connecté.

### Versions antérieures du SDK

Si l'application d'un utilisateur utilise une version antérieure du SDK, il continuera à recevoir les cartes de contenu que vous envoyez. Cependant, les cartes peuvent prendre plus de temps à apparaître et ne s'afficheront peut-être pas avant la prochaine synchronisation des cartes de contenu.

