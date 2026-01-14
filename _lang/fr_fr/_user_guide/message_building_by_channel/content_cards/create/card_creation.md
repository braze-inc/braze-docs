---
nav_title: Création de cartes
article_title: Création de cartes
alias: /card_creation/
description: "Cet article décrit les différences entre la création de cartes de contenu au moment du lancement de la campagne ou de l'entrée dans l'étape du canvas par rapport à la première impression."
page_order: 0
tool: Campaigns
channel:
  - content cards
---

# Création de cartes

> Vous pouvez choisir le moment où Braze évalue l'éligibilité de l'audience et la personnalisation pour les nouvelles campagnes de cartes de contenu et les étapes du canvas en spécifiant le moment de la création de la carte.

## Conditions préalables

Pour bénéficier de cette fonctionnalité, vous devez passer aux versions minimales suivantes du SDK :

{% sdk_min_versions swift:5.2.0 android:23.0.0 web:4.2.0 %}

Après avoir mis à jour le SDK, vos utilisateurs mobiles doivent mettre à jour leur application. Vous pouvez filtrer votre campagne ou votre audience Canvas pour ne [cibler]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions) que [les utilisateurs de ces versions minimales d'apps]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).

## Aperçu

{% tabs %}
{% tab Campaign %}

Vous pouvez choisir le moment où Braze crée une carte à l'étape **Réception/distribution** lors de la création d'une nouvelle [campagne de cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/) avec une réception/distribution planifiée.

!section Contrôles des cartes de contenu lorsque vous modifiez la réception/distribution d'une carte de contenu planifiée.]({% image_buster /assets/img_archive/card_creation.png %})

Les options suivantes sont disponibles :

- **Lors du lancement de la campagne :** L'ancien comportement par défaut pour les cartes de contenu. Braze calcule l'éligibilité de l'audience et la personnalisation lors du lancement de la campagne, puis crée la carte et la stocke jusqu'à ce que l'utilisateur ouvre votre appli. 
- **A la première impression (recommandé) :** Lorsque l'utilisateur ouvre votre application (c'est-à-dire lorsqu'il démarre une nouvelle [session](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), Braze détermine les cartes de contenu auxquelles l'utilisateur est éligible, les modèles de personnalisation tels que Liquid ou Connected Content, puis crée la carte. Cette option permet généralement d'obtenir de meilleures performances en matière de réception/distribution de cartes.

Quelle que soit l'option choisie, le compte à rebours de la date d'expiration de la carte de contenu commencera lorsque la campagne sera lancée.

{% endtab %}
{% tab Canvas %}

Vous pouvez choisir le moment où Braze crée une carte dans l'onglet **Canaux de communication** d'une [étape Message de]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) carte de contenu.

!section Contrôles des cartes de contenu lorsque vous modifiez la réception/distribution d'une carte de contenu planifiée.]({% image_buster /assets/img_archive/card_creation_canvas.png %})

Les options suivantes sont disponibles :

- **A l'entrée de l'étape :** L'ancien comportement par défaut pour les cartes de contenu. Braze calcule l'éligibilité de l'audience lorsque l'utilisateur entre dans l'étape du canvas, puis crée la carte et la stocke jusqu'à ce que l'utilisateur ouvre votre appli.
- **A la première impression (recommandé) :** Braze calcule l'éligibilité de l'audience lorsque l'utilisateur entre dans l'étape du canvas. Lorsque l'utilisateur ouvre votre application (c'est-à-dire lorsqu'il démarre une nouvelle [session](https://www.braze.com/resources/articles/whats-an-app-session-anyway)), Braze modélise toute personnalisation, comme Liquid ou Connected Content, puis crée la carte. Cette option vous permettra de bénéficier d'une meilleure performance dans la réception/distribution des cartes et d'une personnalisation plus actuelle.

Quelle que soit l'option choisie, le compte à rebours de la date d'expiration de la carte de contenu commencera lorsque l'utilisateur entrera dans l'étape du canvas.

{% alert tip %}
Si vous souhaitez que les utilisateurs anonymes voient une carte de contenu lors de leur toute première session, utilisez une campagne au lieu d'un canvas. En effet, lorsqu'un utilisateur anonyme entre dans un canvas, sa session a déjà commencé. Il n'obtiendra donc pas la carte de contenu tant qu'il n'aura pas démarré une nouvelle session.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert note %}
Pour les deux options, après la création d'une carte, Braze ne recalcule pas l'éligibilité de l'audience ou la personnalisation.
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
    <th class="tg-0pky">À première vue</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">Quand l'utiliser ?</td>
    <td class="tg-0pky">Si vous avez besoin que le contenu soit diffusé à un moment précis (le moment du lancement).</td>
    <td class="tg-0pky"><ul><li>Si vous devez afficher des cartes à de nouveaux utilisateurs ou à des utilisateurs anonymes susceptibles d'entrer dans le segment après le lancement<a href="#campaign_note">(campagnes uniquement*).</a></li><li>Si vous utilisez la personnalisation et souhaitez que le contenu le plus récent soit disponible sur la carte.</li></ul></td>
  </tr>
  <tr>
    <td class="leftHeader">L'audience</td>
    <td class="tg-0pky">Braze évalue l'adhésion de l'audience au moment de l'envoi de la campagne.<br><br>L'éligibilité des utilisateurs nouveaux ou anonymes ne sera pas évaluée s'ils tentent de consulter la carte après l'envoi de la campagne. Pour les campagnes récurrentes, ce sera au prochain intervalle de récurrence.</td>
    <td class="tg-0pky">Braze évalue l'adhésion lors de la prochaine ouverture de votre appli par l'utilisateur (démarrage d'une session, <a href="#campaign_note">campagnes uniquement*</a>).<br><br> Ce paramètre permettra d'atteindre une audience plus large, car les utilisateurs anonymes ou nouveaux seront toujours évalués pour déterminer leur éligibilité lorsqu'ils tenteront de consulter la carte. <br><br>En outre, la limite de débit (limitation du nombre de personnes qui recevront la carte) n'est pas applicable lorsqu'elle est réglée sur à la première impression.</td>
  </tr>
  <tr>
    <td class="leftHeader">Personnalisation</td>
    <td class="tg-0pky">Braze évalue le Liquid, le contenu connecté et les blocs de contenu au moment où la campagne est lancée ou lorsqu'un utilisateur entre dans l'étape du canvas. Pour les campagnes récurrentes, ce sera au prochain intervalle de récurrence.</td>
    <td class="tg-0pky">Braze évalue le liquide, le contenu connecté et les blocs de contenu au moment de la première impression ou après le prochain intervalle de récurrence.</td>
  </tr>
  <tr>
    <td class="leftHeader">Analyse/analytique (si utilisé comme adjectif)</td>
    <td class="tg-0pky">Les <em>messages envoyés</em> font référence au nombre de cartes créées et disponibles pour être vues. Cela ne tient pas compte du fait que les utilisateurs ont ou non consulté la carte.</td>
    <td class="tg-0pky">Les <em>messages envoyés</em> correspondent au nombre de cartes envoyées à un utilisateur après le démarrage d'une session. Dans Canvas, les utilisateurs qui entrent dans l'étape sans démarrer de session n'auront pas de carte envoyée, c'est pourquoi cette mesure peut ne pas correspondre au nombre d'utilisateurs entrant dans une étape.<br><br>Alors que vos utilisateurs atteignables et vos impressions ne changeront pas, vous pouvez vous attendre à une diminution du volume d'envoi<em>(messages envoyés</em>) lorsqu'une carte est créée lors de la première impression par rapport à la même carte créée lors du lancement de la campagne ou de l'entrée dans l'étape du canvas.</td>
  </tr>
  <tr>
    <td class="leftHeader">Délai de traitement</td>
    <td class="tg-0pky">Des cartes sont créées pour chaque utilisateur éligible dans le segment au moment du lancement. Pour les audiences importantes, nous vous recommandons de sélectionner <b>À la première impression</b>, car les cartes seront disponibles plus rapidement après le lancement.</td>
    <td class="tg-0pky">Les cartes sont créées la première fois qu'un utilisateur essaie de les visualiser, ce qui peut prendre 1 à 2 secondes pour qu'elles s'affichent lors de la première impression.</td>
  </tr>
</tbody>
</table>

<p id="campaign_note"><sup>* Ce scénario ne s'applique qu'aux campagnes, car l'audience de Canvas est évaluée à l'entrée dans Canvas, et non au niveau de l'étape.</sup></p>

## Considérations

### Modification de la création des cartes après le lancement

Braze recommande de ne pas modifier la façon dont les cartes sont créées après le lancement d'une campagne. En raison des différences de calcul des messages envoyés entre les deux types de création de cartes, le fait de modifier le mode de création des cartes après le lancement de la campagne peut avoir une incidence sur la précision de votre volume d'envoi.

### Temps de traitement potentiel

Nous recommandons aux campagnes ayant une audience importante de choisir l'option de création de cartes dès la première impression, car les cartes seront disponibles beaucoup plus rapidement après le lancement de la campagne. Les campagnes qui sont déclenchées au début de la session peuvent également envisager de passer à la création de la carte à la première impression (disponible par le biais de la réception/distribution) afin d'améliorer les performances.

Lorsque les cartes sont créées lors de la première impression, le traitement des cartes peut prendre 1 à 2 secondes. La durée de ce traitement dépend de divers facteurs, tels que la taille de la carte et la complexité des options d'envoi de messages. Par exemple, le temps de traitement des cartes utilisant le contenu connecté sera au moins aussi long que le temps de réponse du contenu connecté.

### Versions précédentes du SDK

Si l'application d'un utilisateur exécute une version antérieure du SDK, il recevra toujours les cartes de contenu envoyées avec une création de carte spécifiée. Cependant, les cartes prendront plus de temps à apparaître pour ces utilisateurs, et peuvent ne pas apparaître avant la prochaine synchronisation des cartes de contenu.

