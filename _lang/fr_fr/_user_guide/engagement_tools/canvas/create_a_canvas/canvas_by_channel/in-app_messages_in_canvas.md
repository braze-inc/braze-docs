---
nav_title: in-app Messages
article_title: Messages in-app de Canvas
alias: "/canvas_in-app_messages/"
page_order: 2
page_type: reference
description: "Cet article de référence décrit les fonctionnalités et les nuances propres aux messages in-app que vous pouvez ajouter à votre Canvas pour afficher des messages enrichis."
tool: Canvas
channel: in-app messages

---

# Messages in-app de Canvas

> Vous pouvez ajouter des messages in-app dans le cadre de votre parcours Canvas pour afficher des messages enrichis lorsque votre client s'engage avec votre appli.

## Fonctionnement

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

Pour les étapes du canvas dont l'entrée est déclenchée par un événement, les utilisateurs peuvent entrer dans le canvas à mi-session. Les messages in-app ne sont pas mis en ligne/en production/instantané tant qu'une session n'a pas démarré. Par conséquent, si un utilisateur est en cours de session lorsqu'il atteint l'étape Message, il ne recevra pas le message in-app tant qu'il n'aura pas démarré une autre session et effectué le déclencheur correspondant.

## Expiration de message in-app

Vous pouvez choisir la date d'expiration du message in-app. Pendant cette période, le message in-app pourra être consulté jusqu’à la date d’expiration. Après l'envoi du message in-app, celui-ci peut être consulté une seule fois.

![La section Contrôles du message d'une étape de message pour un message in-app. L'envoi de messages in-app expirera trois jours après la mise à disposition de l'étape.]({% image_buster /assets/img_archive/canvas_expiration2.png %}){: style="max-width:90%"}

| Option | Description | Exemple |
|---|---|---|
| **Une durée après l'étape est disponible** | Définit l'expiration du message in-app par rapport au moment où l'étape devient disponible pour l'utilisateur. | Un message in-app avec une expiration de deux jours deviendrait disponible une fois le délai de l'étape écoulé et les options d'audience cochées. Il sera alors disponible pendant 2 jours (48 heures) et au cours de ces deux jours, les utilisateurs pourront voir le message in-app s’ils ouvrent l’application. |
| **À une date et une heure spécifiques** | Sélectionnez une date et une heure spécifiques auxquelles le message in-app ne sera plus disponible. | Si vous avez une vente qui se termine le 30 novembre 2024, sélectionnez cette option pour que les utilisateurs ne voient plus le message in-app associé lorsque la vente se termine. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Cas d’utilisation

Braze vous recommande d'envisager l'utilisation de cette fonctionnalité dans vos canevas de promotion et d'onboarding.

{% tabs %}
  {% tab Promotionnel %}

Les promotions, les coupons de réduction et les ventes ont souvent des dates d’expiration serrées. Le Canvas suivant doit alerter vos utilisateurs au moment le plus opportun qu’une promotion dont ils pourraient bénéficier est en cours, susceptible d’influencer un achat. Cette promotion expire le 28 février 2019 à 11h15 dans le fuseau horaire de votre entreprise.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table class="tg">
<thead>
  <tr>
    <th>Étape de canvas</th>
    <th>Délai</th>
    <th>Audience</th>
    <th>Canal</th>
    <th>Expiration</th>
    <th>Avancement</th>
    <th>Détails</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Jour 1 : 50 % de remise</td>
    <td>Aucun</td>
    <td>Tous à partir de l’entrée</td>
    <td>Notification push</td>
    <td>S.O.</td>
    <td>Audience avancée après le délai</td>
    <td>Notification push qui alerte vos utilisateurs de la promotion. Cela a pour but d'inciter les utilisateurs à se rendre sur votre application pour profiter de la promotion.</td>
  </tr>
  <tr>
    <td>In-app : 50 % de remise</td>
    <td>Aucun</td>
    <td>Tous à partir de l’entrée</td>
    <td>Message in-app</td>
    <td><b>Date d’expiration :</b> 28/02/2019 11 h 15 heure de la société</td>
    <td>Message in-app consulté</td>
    <td>L’utilisateur a maintenant ouvert l’application et recevra ce message, qu’il ait préalablement reçu ou pas le message de notification push.</td>
  </tr>
  <tr>
    <td>Rappel de 50 % de remise</td>
    <td>1 jour après que l’utilisateur a reçu l’étape précédente</td>
    <td>Tous à partir de l’entrée <br><br><b>Filtre :</b> Achat effectué il y a plus d’une semaine</td>
    <td>Message in-app</td>
    <td><b>Date d’expiration :</b> 28/02/2019 11 h 15 heure de la société</td>
    <td>Aucun (dernier message dans Canvas)</td>
    <td>L’utilisateur a reçu le message in-app à l’étape précédente, mais n’a pas effectué d’achat même s’il est dans l’application. <br><br>Ce message est destiné à encourager l’utilisateur à effectuer un achat en utilisant la promotion.</td>
  </tr>
</tbody>
</table>

Les messages in-app expirent à la fin de la promotion afin d'éviter tout décalage entre les messages et l'expérience client.

  {% endtab %}
  {% tab Onboarding des utilisateurs %}

La première impression que vous avez d’un utilisateur est peut-être la plus critique. Elle peut encourager ou décourager l’utilisateur à/de consulter votre application. Vos premières communications avec votre utilisateur doivent être judicieusement planifiées et doivent l’encourager à consulter souvent votre application, pour promouvoir son utilisation.

<table class="tg">
<thead>
  <tr>
    <th>Étape de canvas</th>
    <th>Délai</th>
    <th>Audience</th>
    <th>Canal</th>
    <th>Expiration</th>
    <th>Avancement</th>
    <th>Détails</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>E-mail de bienvenue</td>
    <td>Aucun</td>
    <td>Tous à partir de l’entrée</td>
    <td>E-mail</td>
    <td>S.O.</td>
    <td>Audience avancée après le délai</td>
    <td>E-mail initial pour souhaiter la bienvenue à vos utilisateurs dans un projet, dans le cadre d’une adhésion ou d’un autre programme onboarding. <br><br>Il est conçu pour diriger les utilisateurs vers votre application pour commencer leur onboarding.</td>
  </tr>
  <tr>
    <td>Message in-app jour 3 à 6</td>
    <td>3 jours après que l’utilisateur a reçu l’étape précédente</td>
    <td>Tous à partir de l’entrée</td>
    <td>Message in-app</td>
    <td><b>Expire :</b> 3 jours après la mise à disposition de l'étape</td>
    <td>Message in-app en direct</td>
    <td>Si l’utilisateur a donné suite à l’e-mail et a été dirigé vers l’application, il recevra le message in-app souhaité pour poursuivre ou lui rappeler l’onboarding et les exigences qui y sont associées.</td>
  </tr>
  <tr>
    <td>Notification push jour 5 </td>
    <td>2 jours après que l’utilisateur a reçu l’étape précédente</td>
    <td>Tous à partir de l’entrée</td>
    <td>Notification push</td>
    <td>S.O.</td>
    <td>Message envoyé</td>
    <td>Après la réception de leur message in-app, les utilisateurs recevront une notification push de suivi pour poursuivre leur onboarding.</td>
  </tr>
</tbody>
</table>

Ces messages push sont espacés autour d'un message in-app pour s'assurer que l'utilisateur a bien visité l'application et commencé son onboarding. Cela permet d'éviter tout spam ou message in-app qui pourrait dissuader les utilisateurs de visiter votre application, et de créer au contraire un ordre fluide et raisonnable pour leurs premières expériences sur votre application.

  {% endtab %}
{% endtabs %}


## Priorisation des messages in-app

Un utilisateur peut déclencher deux messages in-app dans votre Canvas en même temps. Lorsque cela se produit, Braze respecte l'ordre de priorité suivant pour déterminer quel message in-app est affiché. 

Sélectionnez **Définir la priorité exacte** et faites glisser différentes étapes du canvas pour réorganiser leur priorité pour le canvas. Par défaut, les étapes précédentes d'une variante de canvas s’afficheront avant les étapes postérieures. Une fois que les étapes sont classées dans l'ordre de priorité que vous avez choisi, sélectionnez **Appliquer le tri**.

![Le trieur de priorités avec deux étapes "Welcome IAM" et "Followup IAM".]({% image_buster /assets/img_archive/canvas_priority2.png %}){: style="max-width:85%"}

### Apporter des modifications aux projets de toiles actives

Si vous apportez des modifications à la priorité des messages in-app dans les **paramètres d'envoi d'** un brouillon d'un canvas actif, ces modifications sont appliquées directement au canvas actif lorsque la trieuse de priorité est fermée. Toutefois, dans une étape du message, le trieur de priorités sera mis à jour lorsque le projet sera lancé puisque les paramètres de l'étape Canvas s'appliquent au niveau de l'étape. 

## Comportement d’avancement

Les étapes de messages font automatiquement avancer tous les utilisateurs qui entrent dans l'étape. Notez qu'il n'attend pas que le message in-app se déclenche ou s'affiche. Il n’est pas nécessaire de spécifier le comportement d’avancement des messages, ce qui facilite la configuration générale de l’étape.

Lorsqu'un utilisateur entre dans une étape d'envoi de messages in-app, il en sort immédiatement au lieu d'être retenu pendant la fenêtre d'expiration. Dans ce cas, il peut être utile de prévoir une étape de temporisation dans le parcours de l'utilisateur.

Pour utiliser l'option **Avancer lorsque le message a été envoyé**, ajoutez un [parcours d'audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) distinct pour filtrer les utilisateurs qui n'ont pas reçu l'étape précédente.

{% details Editeur de canevas original %}

Vous ne pouvez plus créer ou dupliquer des toiles à l'aide de l'éditeur original. Cette section est disponible à titre de référence lorsque vous comprenez comment fonctionne le comportement d’avancement pour les étapes avec des messages in-app.

Les Canvas créez dans l’éditeur d’origine doivent spécifier le comportement d’avancement, à savoir le critère d’avancement à travers votre composant Canvas. Les [étapes comportant uniquement des messages in-app](#steps-iam-only) ont des options d'avancement différentes de celles [comportant plusieurs types de messages](#steps-multiple-channels) (tels que push ou e-mail). Pour les messages in-app dans le flux de travail Canvas Flow, cette option est définie pour faire avancer immédiatement l’audience.

La livraison par événement n’est pas disponible pour des étapes de Canvas comportant des messages in-app. Les étapes Canvas avec des messages in-app doivent être programmés. À la place, les messages in-app Canvas s’afficheront la première fois que votre utilisateur ouvre l’application (déclenché par la session de démarrage), une fois que le message planifié dans le composant Canvas lui a été envoyé.

Si vous avez plusieurs messages in-app dans un Canvas, un utilisateur doit démarrer plusieurs sessions pour recevoir chacun de ces messages.

{% alert important %}
Lorsque l'option **Avancer lorsque le message in-app est activé** est sélectionnée, le message in-app deviendra disponible jusqu'à son expiration, même si l'utilisateur est passé aux étapes suivantes. Si vous ne souhaitez pas que le message in-app soit activé lorsque les étapes suivantes du Canvas sont livrées, vérifiez que la date d’expiration est antérieure au délai dans les étapes suivantes.
{% endalert %}

#### Étapes avec plusieurs canaux {#steps-multiple-channels}

Les étapes avec un message in-app et un autre canal de communication disposent des options d’avancement suivantes :

| Option | Description |
|---|---|---|
| Avancement lors de l’envoi du message | Les utilisateurs recevront un e-mail, un webhook ou une notification push, ou bien consulteront le message in-app pour progresser vers les étapes suivantes dans le Canvas.  <br> <br>  Si le message in-app expire et que l’utilisateur n’a pas reçu d’e-mail, de webhook ou de notification push ou n’a pas consulté le message in-app, il quittera Canvas et ne progressera pas vers les étapes suivantes. |
| Audience avancée immédiatement | Toute personne qui se trouve dans l’audience, avance aux étapes suivantes une fois le délai passé, que le message indiqué ait été vu ou pas. <br> <br> Les utilisateurs doivent correspondre aux critères de segmentation et de filtrage de l'étape pour passer aux étapes suivantes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Lorsque l'option **Toute l'audience** est sélectionnée, le message in-app sera disponible jusqu'à son expiration, même si l'utilisateur est passé aux étapes suivantes. Si vous ne souhaitez pas que le message in-app soit activé lorsque les étapes suivantes du canvas sont livrées, vérifiez que la date d’expiration est antérieure au délai dans les étapes suivantes.
{% endalert %}

{% enddetails %}

## Actions de déclenchement

Vous pouvez choisir parmi les actions de déclenchement suivantes pour cibler vos utilisateurs :

- **Effectuer un achat :** Cibler les utilisateurs qui effectuent n'importe quel achat ou un achat spécifique.
- **Lancer la session :** Ciblez les utilisateurs qui démarrent une session dans n'importe quelle application ou dans une application spécifique.
- **Effectuer un événement personnalisé :** Ciblez les utilisateurs qui effectuent l'événement personnalisé sélectionné.

Un utilisateur doit entrer dans l'étape du canvas, démarrer une session, puis effectuer le déclencheur pour recevoir un message in-app. Cela signifie que les mises à jour en cours de session ne sont pas prises en charge. Par exemple, si le déclencheur est le démarrage d'une session, il suffit à l'utilisateur d'entrer dans l'étape du canvas et de démarrer une session pour recevoir le message in-app. Si le déclencheur n'est pas de démarrer une session, l'utilisateur doit entrer dans l'étape du canvas, démarrer une session, puis effectuer le déclencheur pour recevoir le message in-app.

!["Faire un achat spécifique" sélectionné comme action de déclenchement.]({% image_buster /assets/img_archive/canvas_trigger_actions.png %}){: style="max-width:90%"}

Les fonctionnalités Canvas suivantes ne sont pas disponibles avec les messages in-app, elles ne seront donc pas appliquées à vos messages in-app même si elles sont activées.

- Timing intelligent
- Limitation du taux
- Limite de fréquence
- Critère de sortie
- Heures calmes

## Propriétés d’événement personnalisé dans un Canvas

Les propriétés d'événement personnalisé dans les messages in-app pour Canvas sont prises en charge. Cependant, ces propriétés proviennent de l'événement personnalisé ou de l'achat déclenchant le message in-app, qui est situé dans l'étape Message, et non dans le chemin d'action précédent.

## Considérations

Voici quelques éléments à prendre en compte lors de l'envoi de messages in-app dans un canvas.

- Si l'utilisateur ne redémarre jamais l'application ou ne démarre jamais une session, l'application ne sera pas en mesure de déterminer si l'utilisateur peut recevoir un message in-app, ce qui signifie qu'aucun message in-app ne sera envoyé.
- Lorsque le premier clic a lieu et qu'il existe une variable de contexte Canvas (propriétés de l'entrée Canvas), et qu'un utilisateur réintègre un Canvas cinq fois, Braze prendra la cinquième entrée et utilisera cette variable de contexte dans le message in-app.
- Un utilisateur ne peut avoir droit qu'à 10 messages in-app à la fois. Par exemple, si un utilisateur passe par différentes étapes du canvas pour 10 messages in-app, vous ne pouvez avoir que 10 de ces étapes.
