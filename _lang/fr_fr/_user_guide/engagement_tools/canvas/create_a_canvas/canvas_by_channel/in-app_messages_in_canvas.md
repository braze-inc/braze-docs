---
nav_title: Messages in-app
article_title: Messages in-app dans Canvas
alias: "/canvas_in-app_messages/"
page_order: 2
page_type: reference
description: "Cet article de référence décrit les fonctionnalités et les nuances propres aux messages in-app que vous pouvez ajouter à votre Canvas pour afficher des messages enrichis."
tool: Canvas
channel: in-app messages

---

# Messages in-app dans Canvas

> Vous pouvez ajouter des messages in-app dans le cadre de votre parcours Canvas pour afficher des messages enrichis lorsque votre client s'engage avec votre appli.

## Comment cela fonctionne-t-il ?

Avant de pouvoir utiliser les messages in-app dans votre Canvas, assurez-vous d'avoir configuré un [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) avec des options de délai et d'audience.

Dans le générateur de canvas, ajoutez une étape de [Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) et sélectionnez **Message in-app** comme **canal de communication.** Vous pouvez personnaliser la [date d'expiration de votre message](#in-app-message-expiration) et son [comportement d'avancement](#advancement-behavior).

## Ajouter un message in-app à votre parcours utilisateur

Pour ajouter un message in-app à votre canvas, procédez comme suit :

1. Ajoutez une étape [Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) à votre parcours utilisateur.
2. Sélectionnez **Message in-app** pour votre **canal de communication.** 
3. Déterminez la [date d'expiration de votre message](#in-app-message-expiration) et son [comportement à l'avancement](#advancement-behavior-options).

## Messages in-app déclenchés

Vous pouvez sélectionner un déclencheur pour vos messages in-app au démarrage de la session, ou par des événements personnalisés et des achats.

Une fois les délais écoulés et les options d'audience cochées, les messages in-app sont mis en ligne/en production/instantané lorsque l'utilisateur atteint l'étape Message. Si un utilisateur démarre une session et effectue l'événement déclencheur pour le message in-app, l'utilisateur verra le message in-app. 

Pour les étapes du canvas dont l'entrée est déclenchée par une action, les utilisateurs peuvent entrer dans le canvas à mi-session. Les messages in-app ne sont pas mis en ligne/en production/instantané tant qu'une session n'a pas démarré. Par conséquent, si un utilisateur est au milieu d'une session lorsqu'il atteint l'étape Message, il ne recevra pas le message in-app tant qu'il n'aura pas démarré une autre session et effectué le déclencheur correspondant.

## Expiration des messages in-app

Vous pouvez choisir la date d'expiration du message in-app. Pendant ce temps, le message in-app attendra d'être consulté jusqu'à ce qu'il atteigne la date d'expiration. Après l'envoi du message in-app, celui-ci peut être consulté une seule fois.

!La section Contrôles du message d'une étape de message pour un message in-app. L'envoi de messages in-app expirera trois jours après la mise à disposition de l'étape.]({% image_buster /assets/img_archive/canvas_expiration2.png %}){: style="max-width:90%"}

| Option | Description | Exemple |
|---|---|---|
| **Une durée après l'étape est disponible** | Définit l'expiration du message in-app par rapport au moment où l'étape devient disponible pour l'utilisateur. | Un message in-app avec une expiration de deux jours deviendrait disponible lorsque l'utilisateur entre dans l'étape Message et que les options d'audience sont cochées. Tout retard avant d'atteindre cette étape proviendrait des étapes précédentes du canvas. Le message in-app serait alors disponible pendant deux jours (48 heures) à partir du moment où l'utilisateur entre dans l'étape, et pendant ces deux jours, les utilisateurs pourraient voir le message in-app s'ils ouvrent l'application. |
| **À une date et une heure précises** | Sélectionnez une date et une heure spécifiques auxquelles le message in-app ne sera plus disponible. | Si vous avez une vente qui se termine le 30 novembre 2024, sélectionnez cette option pour que les utilisateurs ne voient plus le message in-app associé lorsque la vente se termine. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Cas d'utilisation

Braze vous recommande d'envisager l'utilisation de cette fonctionnalité dans vos canevas de promotion et d'onboarding.

{% tabs %}
  {% tab Promotional %}

Les promotions, les coupons et les ventes ont souvent des dates d'expiration strictes. Le canvas suivant devrait alerter vos utilisateurs aux moments les plus opportuns qu'il y a une promotion qu'ils peuvent utiliser, et peut-être influencer un achat. Cette promotion expire le 28 février 2019 à 11h15 dans le fuseau horaire de votre entreprise.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table class="tg">
<thead>
  <tr>
    <th>Étape du canvas</th>
    <th>Délai</th>
    <th>L'audience</th>
    <th>Chaîne</th>
    <th>Expiration</th>
    <th>L'avancement</th>
    <th>Détails</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Jour 1 : 50% de réduction</td>
    <td>Aucun</td>
    <td>Tous à partir de l'entrée</td>
    <td>Pousser</td>
    <td>N/A</td>
    <td>L'avancement de l'audience après un délai</td>
    <td>Une poussée initiale qui avertit vos utilisateurs de la promotion. Cela a pour but d'inciter les utilisateurs à se rendre sur votre application pour profiter de la promotion.</td>
  </tr>
  <tr>
    <td>In-app : 50% de réduction</td>
    <td>Aucun</td>
    <td>Tous à partir de l'entrée</td>
    <td>Message in-app</td>
    <td><b>Expire par :</b> 2/28/2019 11:15 AM Company Time</td>
    <td>Message in-app visualisé</td>
    <td>L'utilisateur a maintenant ouvert l'application et recevra ce message, que ce soit ou non à cause du message push précédent.</td>
  </tr>
  <tr>
    <td>Rappel de 50% de réduction</td>
    <td>1 jour après que l'utilisateur a reçu l'étape précédente</td>
    <td>Tous à partir de l'entrée <br><br><b>Filtre :</b> Dernier achat effectué il y a plus d'une semaine</td>
    <td>Message in-app</td>
    <td><b>Expire par :</b> 2/28/2019 11:15 AM Company Time</td>
    <td>Aucun (dernier message dans Canvas)</td>
    <td>L'utilisateur a reçu le message in-app à l'étape précédente mais n'a pas effectué d'achat bien qu'il soit dans l'application. <br><br>Ce message a pour but d'inciter l'utilisateur à effectuer un achat en profitant de la promotion.</td>
  </tr>
</tbody>
</table>

Les messages in-app expirent à la fin de la promotion afin d'éviter tout décalage entre les messages et l'expérience client.

  {% endtab %}
  {% tab User Onboarding %}

La première impression que vous donnez à un utilisateur est sans doute la plus importante. Il peut faire ou défaire les visites futures sur votre application. Vos premières communications avec l'utilisateur doivent être judicieusement programmées et encourager les visites fréquentes de votre application afin d'en promouvoir l'utilisation.

<table class="tg">
<thead>
  <tr>
    <th>Étape du canvas</th>
    <th>Délai</th>
    <th>L'audience</th>
    <th>Chaîne</th>
    <th>Expiration</th>
    <th>L'avancement</th>
    <th>Détails</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>E-mail de bienvenue</td>
    <td>Aucun</td>
    <td>Tous à partir de l'entrée</td>
    <td>e-mail</td>
    <td>N/A</td>
    <td>Avance de l'audience après un délai</td>
    <td>L'e-mail initial qui accueille vos utilisateurs dans le cadre d'un projet, d'une adhésion ou d'un autre programme d'onboarding. <br><br>Cela a pour but de conduire les utilisateurs vers votre appli pour commencer leur onboarding.</td>
  </tr>
  <tr>
    <td>Jour 3-6 message in-app</td>
    <td>3 jours après que l'utilisateur a reçu l'étape précédente</td>
    <td>Tous à partir de l'entrée</td>
    <td>Message in-app</td>
    <td><b>Expire :</b> 3 jours après la mise à disposition de l'étape</td>
    <td>Message in-app en ligne/en production/instantané</td>
    <td>Si l'utilisateur a donné suite à l'e-mail et a été conduit à l'application, il recevra le message in-app souhaité pour poursuivre ou lui rappeler son onboarding et toutes les exigences qui y sont associées.</td>
  </tr>
  <tr>
    <td>Jour 5 pousser </td>
    <td>2 jours après que l'utilisateur a reçu l'étape précédente</td>
    <td>Tous à partir de l'entrée</td>
    <td>Pousser</td>
    <td>N/A</td>
    <td>Envoi de messages</td>
    <td>Une fois que les utilisateurs ont reçu leur message in-app, ils recevront un push de suivi pour poursuivre leur onboarding.</td>
  </tr>
</tbody>
</table>

Ces messages push sont espacés autour d'un message in-app pour s'assurer que l'utilisateur a bien visité l'application et commencé son onboarding. Cela permet d'éviter tout spam ou message in-app qui pourrait dissuader les utilisateurs de visiter votre application, et de créer au contraire un ordre fluide et raisonnable pour leurs premières expériences sur votre application.

  {% endtab %}
{% endtabs %}


## Priorité aux messages in-app

Un utilisateur peut déclencher deux messages in-app dans votre Canvas en même temps. Lorsque cela se produit, Braze respecte l'ordre de priorité suivant pour déterminer quel message in-app est affiché. 

Sélectionnez **Définir la priorité exacte** et faites glisser différentes étapes du canvas pour réorganiser leur priorité pour le canvas. Par défaut, les étapes antérieures d'une variante du canvas s'affichent avant les étapes ultérieures. Une fois que les étapes sont classées dans l'ordre de priorité que vous avez choisi, sélectionnez **Appliquer le tri**.

Le trieur de priorités avec deux étapes "Welcome IAM" et "Followup IAM".]({% image_buster /assets/img_archive/canvas_priority2.png %}){: style="max-width:85%"}

### Apporter des modifications aux projets de toiles actives

Si vous apportez des modifications à la priorité des messages in-app dans les **paramètres d'envoi d'** un brouillon d'un canvas actif, ces modifications sont appliquées directement au canvas actif lorsque la trieuse de priorité est fermée. Toutefois, dans une étape du message, le trieur de priorités sera mis à jour lorsque le projet sera lancé puisque les paramètres de l'étape Canvas s'appliquent au niveau de l'étape. 

## Comportement d'avancement

Les étapes de messages font automatiquement avancer tous les utilisateurs qui entrent dans l'étape. Notez qu'il n'attend pas que le message in-app se déclenche ou s'affiche. Il n'est pas nécessaire de spécifier le comportement d'avancement des messages, ce qui simplifie la configuration de l'ensemble de l'étape.

Lorsqu'un utilisateur entre dans une étape d'envoi de messages in-app, il en sort immédiatement au lieu d'être retenu pendant la fenêtre d'expiration. Dans ce cas, il peut être utile de prévoir une étape de temporisation dans le parcours de l'utilisateur.

Pour utiliser l'option **Avancer lorsque le message a été envoyé**, ajoutez un [parcours d'audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) distinct pour filtrer les utilisateurs qui n'ont pas reçu l'étape précédente.

{% details Original Canvas editor %}

Vous ne pouvez plus créer ou dupliquer des toiles à l'aide de l'éditeur original. Cette section est disponible à titre de référence pour comprendre le fonctionnement de l'avancement pour les étapes avec des messages in-app.

Les toiles créées dans l'éditeur d'origine doivent spécifier un comportement d'avancement, c'est-à-dire les critères d'avancement dans votre composant Canvas. Les [étapes comportant uniquement des messages in-app](#steps-iam-only) ont des options d'avancement différentes de celles [comportant plusieurs types de messages](#steps-multiple-channels) (tels que push ou e-mail). Pour les messages in-app dans le flux de travail actuel de Canvas, cette option est définie pour toujours faire avancer immédiatement l'audience.

La livraison par événement n'est pas disponible pour les étapes du canvas avec des messages in-app. Les étapes du canvas avec des messages in-app doivent être planifiées. Au lieu de cela, les messages in-app de Canvas apparaîtront la première fois que votre utilisateur ouvrira l'application (déclenché par la session de démarrage) après que le message planifié dans le composant Canvas lui aura été envoyé.

Si vous avez plusieurs messages in-app dans un Canvas, un utilisateur doit démarrer plusieurs sessions pour recevoir chacun de ces messages individuels.

{% alert important %}
Lorsque l'option **Avancer lorsque le message in** -app est **en direct** est sélectionnée, le message in-app sera disponible jusqu'à son expiration, même si l'utilisateur est passé aux étapes suivantes. Si vous ne souhaitez pas que le message in-app soit en ligne/en production/instantané lors de l'envoi des étapes suivantes du canvas, veillez à ce que l'expiration soit plus courte que le délai des étapes suivantes.
{% endalert %}

#### Étapes avec plusieurs canaux {#steps-multiple-channels}

Les étapes avec un message in-app et un autre canal disposent des options d'avancement suivantes :

| Option | Description |
|---|---|---|
| Avancement lors de l'envoi du message | Les utilisateurs doivent recevoir un e-mail, un webhook ou une notification push, ou consulter le message in-app pour passer aux étapes suivantes du Canvas.  <br> <br>  Si le message in-app expire et que l'utilisateur n'a pas reçu l'e-mail, le webhook ou le push, ou qu'il n'a pas consulté le message in-app, il quittera le Canvas et ne passera pas aux étapes suivantes. |
| L'avancement immédiat de l'audience | Toutes les personnes faisant partie de l'audience de l'étape passent à l'étape suivante une fois le délai écoulé, qu'elles aient vu ou non le message indiqué. <br> <br> Les utilisateurs doivent correspondre aux critères de segmentation et de filtrage de l'étape pour passer aux étapes suivantes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Lorsque l'option **Toute l'audience** est sélectionnée, le message in-app sera disponible jusqu'à son expiration, même si l'utilisateur est passé aux étapes suivantes. Si vous ne souhaitez pas que le message in-app soit en ligne/en production/instantané lors de l'envoi des étapes suivantes du canvas, vérifiez que l'expiration est plus courte que le délai des étapes suivantes.
{% endalert %}

{% enddetails %}

## Actions de déclenchement

Vous pouvez choisir parmi les actions de déclenchement suivantes pour cibler vos utilisateurs :

- **Effectuez vos achats :** Cibler les utilisateurs qui effectuent n'importe quel achat ou un achat spécifique.
- **Début de la session :** Ciblez les utilisateurs qui démarrent une session dans n'importe quelle application ou dans une application spécifique.
- **Exécuter un événement personnalisé :** Ciblez les utilisateurs qui effectuent l'événement personnalisé sélectionné (l'événement personnalisé doit être envoyé à l'aide du SDK).

Un utilisateur doit entrer dans l'étape du canvas, démarrer une session, puis effectuer le déclencheur pour recevoir un message in-app. Cela signifie que les mises à jour en cours de session ne sont pas prises en charge. Par exemple, si le déclencheur est le démarrage d'une session, il suffit à l'utilisateur d'entrer dans l'étape du canvas et de démarrer une session pour recevoir le message in-app. Si le déclencheur n'est pas de démarrer une session, l'utilisateur doit entrer dans l'étape du canvas, démarrer une session, puis effectuer le déclencheur pour recevoir le message in-app.

\!["Faire un achat spécifique" sélectionné comme action de déclenchement.]({% image_buster /assets/img_archive/canvas_trigger_actions.png %}){: style="max-width:90%"}

Les fonctionnalités Canvas suivantes ne sont pas disponibles avec les messages in-app, elles ne seront donc pas appliquées à vos messages in-app même si elles sont activées.

- Le timing intelligent
- Limite de débit
- Limitation de fréquence
- Critères de sortie
- Heures calmes

## Propriétés d'événement personnalisé dans un canvas

Les propriétés d'événement personnalisé dans les messages in-app pour Canvas sont prises en charge. Cependant, ces propriétés proviennent de l'événement personnalisé ou de l'achat déclenchant le message in-app, qui est situé dans l'étape Message, et non dans le chemin d'action précédent.

## Considérations

Voici quelques éléments à prendre en compte lors de l'envoi de messages in-app dans un canvas.

- Si l'utilisateur ne redémarre jamais l'application ou ne démarre jamais une session, l'application ne pourra pas savoir si l'utilisateur est éligible pour le message in-app, ce qui signifie qu'aucun message in-app ne sera envoyé.
- Lorsque le premier clic a lieu et qu'il existe une variable de contexte Canvas (propriétés de l'entrée Canvas), et qu'un utilisateur réintègre un Canvas cinq fois, Braze prendra la cinquième entrée et utilisera cette variable de contexte dans le message in-app.
- Un utilisateur ne peut avoir droit qu'à 10 messages in-app à la fois. Par exemple, si un utilisateur passe par différentes étapes du canvas pour 10 messages in-app, vous ne pouvez avoir que 10 de ces étapes.
