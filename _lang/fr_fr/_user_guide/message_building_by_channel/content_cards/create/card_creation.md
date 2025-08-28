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
{% tab Campagne %}

Vous pouvez choisir le moment où Braze crée une carte à l'étape **Livraison** lors de la création d'une nouvelle [campagne de cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/) avec une livraison planifiée.

![Section Contrôles de la carte de contenu lors de la modification de la distribution d’une carte de contenu planifiée.]({% image_buster /assets/img_archive/card_creation.png %})

Les options suivantes sont disponibles :

- **Lors du lancement de la campagne :** Le comportement par défaut précédent pour les cartes de contenu. Braze calcule l’éligibilité et la personnalisation de l’audience au lancement de la campagne, puis crée la carte et la stocke jusqu’à ce que l’utilisateur ouvre votre application. 
- **A la première impression (recommandé) :** Lorsque l’utilisateur ouvre ensuite votre application (c’est-à-dire qu’il démarre une nouvelle [session](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), Braze détermine les cartes de contenu auxquelles l’utilisateur est éligible, modélise les personnalisations telles que le Liquid ou le contenu connecté, puis crée la carte. Cette option permet généralement d'obtenir de meilleures performances en matière de réception/distribution de cartes.

Quelle que soit l'option choisie, le compte à rebours de la date d'expiration de la carte de contenu commencera lorsque la campagne sera lancée.

{% endtab %}
{% tab Canvas %}

Vous pouvez choisir le moment où Braze crée une carte dans l'onglet **Canaux de communication** d'une [étape Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) de carte de contenu.

![Section Contrôles de la carte de contenu lors de la modification de la distribution d’une carte de contenu planifiée.]({% image_buster /assets/img_archive/card_creation_canvas.png %})

Les options suivantes sont disponibles :

- **À l'entrée de l'étape :** Le comportement par défaut précédent pour les cartes de contenu. Braze calcule l'éligibilité de l'audience lorsque l'utilisateur entre dans l'étape du canvas, puis crée la carte et la stocke jusqu'à ce que l'utilisateur ouvre votre appli.
- **A la première impression (recommandé) :** Braze calcule l'éligibilité de l'audience lorsque l'utilisateur entre dans l'étape du canvas. Lorsque l'utilisateur ouvre ensuite votre application (c'est-à-dire lorsqu'il démarre une nouvelle [session](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), Braze modélise toute personnalisation comme le Liquid ou le contenu collecté, puis crée la carte. Cette option vous permettra de bénéficier de meilleures performances dans la distribution des cartes et d'une personnalisation plus actuelle.

Quelle que soit l'option choisie, le compte à rebours de la date d'expiration de la carte de contenu commencera lorsque l'utilisateur entrera dans l'étape du canvas.

{% alert tip %}
Si vous souhaitez que les utilisateurs anonymes voient une carte de contenu lors de leur toute première session, utilisez une campagne au lieu d'un canvas. En effet, lorsqu'un utilisateur anonyme entre dans un canvas, sa session a déjà commencé. Il n'obtiendra donc pas la carte de contenu tant qu'il n'aura pas démarré une nouvelle session.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert note %}
Pour les deux options, après la création d’une carte, Braze ne recalcule pas l’éligibilité ou la personnalisation de l’audience.
{% endalert %}

### Différences entre la création de cartes au moment du lancement ou de l'entrée sur le marché et la création de cartes lors de la première impression

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
    <td class="tg-0pky">Braze évalue l'adhésion lors de la prochaine ouverture de votre appli par l'utilisateur (démarrage d'une session, <a href="#campaign_note">campagnes uniquement*</a>).<br><br> Ce paramètre aura une portée d’audience plus large car l’éligibilité de l’utilisateur nouveau ou anonyme sera toujours évaluée lorsqu’il essaiera d’afficher la carte. <br><br>En outre, la limite de débit (limitation du nombre de personnes qui recevront la campagne) n'est pas applicable lorsqu'elle est définie sur « À la première impression » (<a href="#campaign_note">campagnes uniquement*</a>).</td>
  </tr>
  <tr>
    <td class="leftHeader">Personnalisation</td>
    <td class="tg-0pky">Braze évalue le Liquid, le contenu connecté et les blocs de contenu au lancement de la campagne ou lorsqu'un utilisateur entre dans l'étape du canvas. Pour les campagnes récurrentes, cela se fera à l’intervalle de récurrence suivant.</td>
    <td class="tg-0pky">Braze évalue le Liquid, le contenu connecté et les blocs de contenu au moment de la première impression ou après l’intervalle de récurrence suivant.</td>
  </tr>
  <tr>
    <td class="leftHeader">Analyse</td>
    <td class="tg-0pky"><em>Messages envoyés</em> fait référence au nombre de cartes créées et disponibles pour être consultées. Le fait que les utilisateurs aient consulté ou non la carte n’est pas comptabilisé.</td>
    <td class="tg-0pky">Les <em>messages envoyés</em> correspondent au nombre de cartes envoyées à un utilisateur après le démarrage d'une session. Dans Canvas, les utilisateurs qui entrent dans l'étape sans démarrer de session n'auront pas de carte envoyée, c'est pourquoi cette mesure peut ne pas correspondre au nombre d'utilisateurs entrant dans une étape.<br><br>Alors que vos utilisateurs atteignables et vos impressions ne changeront pas, vous pouvez vous attendre à une diminution du volume d'envoi<em>(messages envoyés</em>) lorsqu'une carte est créée lors de la première impression par rapport à la même carte créée lors du lancement de la campagne ou de l'entrée dans l'étape du canvas.</td>
  </tr>
  <tr>
    <td class="leftHeader">Temps de traitement</td>
    <td class="tg-0pky">Les cartes sont créées pour chaque utilisateur éligible du segment au moment du lancement. Pour les audiences importantes, nous recommandons de sélectionner <b>lors de la première impression</b>, car les cartes seront disponibles plus rapidement après le lancement.</td>
    <td class="tg-0pky">Les cartes sont créées la première fois qu’un utilisateur essaie de les visualiser, de sorte qu’il peut s’écouler 1 à 2 secondes pour qu’elles s’affichent lors de la première impression.</td>
  </tr>
</tbody>
</table>

<p id="campaign_note"><sup>* Ce scénario ne s'applique qu'aux campagnes, car l'audience Canvas est évaluée à l'entrée du canvas, et non au niveau de l'étape.</sup></p>

## Considérations

### Modification de la création de la carte après le lancement

Braze recommande de ne pas modifier la façon dont les cartes sont créées après le lancement d’une campagne. En raison des différences dans la façon dont les messages envoyés sont calculés entre les deux types de création de cartes, changer la façon dont les cartes sont créées après le lancement de la campagne peut affecter la précision de votre volume d’envoi.

### Temps de traitement potentiel

Nous recommandons que les campagnes avec une audience importante utilisent l’option de créer des cartes dès la première impression, car les cartes seront disponibles beaucoup plus rapidement après le lancement de la campagne. Les campagnes qui sont déclenchées au début de la session peuvent également envisager de passer à la création de la carte à la première impression (disponible par le biais de la réception/distribution) afin d'améliorer les performances.

Lorsque les cartes sont créées à la première impression, leur traitement peut prendre 1 à 2 secondes. La durée de ce temps de traitement dépend de divers facteurs, tels que la taille de la carte et la complexité des options de modélisation du message. Par exemple, le temps de traitement des cartes utilisant le Contenu connecté sera au moins aussi long que le temps de réponse du Contenu connecté.

### Versions antérieures du SDK

Si l’application d’un utilisateur exécute une version antérieure du SDK, il recevra toujours des cartes de contenu envoyées avec une création de carte spécifiée. Cependant, les cartes prendront plus de temps à apparaître pour ces utilisateurs et peuvent ne pas apparaître avant la prochaine synchronisation de la carte de contenu.

