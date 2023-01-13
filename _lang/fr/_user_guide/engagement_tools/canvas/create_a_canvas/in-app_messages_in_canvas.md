---
nav_title: Messages in-app de Canvas
article_title: Messages in-app de Canvas
page_order: 6
page_type: reference
description: "Cet article de référence décrit les fonctionnalités et les nuances spécifiques aux messages In-App de Canvas, que vous pouvez ajouter à votre Canvas pour mettre en valeur votre messagerie."
tool: Canvas
channel: messages in-app

---

# Messages in-app de Canvas

{% multi_lang_include video.html id="6X8E20BlblI" align="right" %}

> Des messages in-app peuvent être ajoutés dans le cadre de votre parcours Canvas pour mettre en valeur votre messagerie lorsque votre client accède à votre application. Cet article décrit les fonctionnalités et les nuances spécifiques aux messages in-app de Canvas.

Avant de poursuivre, vous devez avoir déjà [créé votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) et configuré des options de délai et d’audience.

À présent, vous pouvez ajouter un message in-app dans votre Canvas en sélectionnant un message in-app à partir de **canaux de messagerie**. Une fois que le délai d’une étape est passé et que les options d’audience ont été cochées, le message in-app sera activé et les utilisateurs le verront à l’ouverture de l’application. Les messages in-app dans Canvas peuvent être uniquement déclenchés par l’`start session`événement déclencheur - ils ne peuvent pas être déclenchés par des événements personnalisés dans une étape Canvas !

Vous pouvez personnaliser [la date d’expiration de votre message](#in-app-message-expiration) et son [comportement d’avancement](#advancement-behavior-options).

## Expiration de message in-app

Dans l’éditeur de messages in-app, vous pouvez choisir la date d’expiration du message in-app. Pendant cette période, le message in-app pourra être consulté jusqu’à la date d’expiration. Une fois envoyé, le message in-app peut être consulté au plus une fois.

![][1]

| Option | Description | Exemple |
|---|---|---|
| Le message expire après la date indiquée | La première option vous permet de définir la date d’expiration d’un message in-app en fonction du début de disponibilité de l’étape pour l’utilisateur. | Par exemple, un message in-app avec un délai d’expiration de deux jours deviendra disponible une fois le délai de l’étape écoulé et lorsque les options d’audience seront cochées. Il sera alors disponible pendant 2 jours (48 heures) et au cours de ces deux jours, les utilisateurs pourront voir le message in-app s’ils ouvrent l’application. |
| Le message expire à une date indiquée | La deuxième option vous permet de choisir une date et une heure spécifiques auxquelles le message in-app ne sera plus disponible. | Par exemple, si vous avez une vente qui se termine à une heure et une date spécifiques, vous pourrez sélectionner cette option de sorte qu’une fois la vente terminée, les utilisateurs ne verront plus le message in-app associé. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Cas d’utilisation

Quand devez-vous utiliser cette fonctionnalité ? Braze recommande vivement d’utiliser cette fonctionnalité dans vos campagnes promotionnelles et onboarding.

{% tabs %}
  {% tab Promotional %}
**Canvas promotionnels**

Les promotions, les coupons de réduction et les ventes ont souvent des dates d’expiration serrées. Le Canvas suivant doit alerter vos utilisateurs au moment le plus opportun qu’une promotion dont ils pourraient bénéficier est en cours, susceptible d’influencer un achat. Cette promotion expire le 28 février 2019 à 11h15, dans le fuseau horaire de la société.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table class="tg">
<thead>
  <tr>
    <th>Canvas Step</th>
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
    <td>Jour 1 : 50 % de remise</td>
    <td>Aucun</td>
    <td>Tous à partir de l’entrée</td>
    <td>Notification push</td>
    <td>S/O</td>
    <td>Audience avancée après le délai</td>
    <td>Notification push qui alerte vos utilisateurs de la promotion. Elle a pour but de diriger vos utilisateurs vers votre application pour profiter de la promotion.</td>
  </tr>
  <tr>
    <td>In-app: 50 % de remise</td>
    <td>Aucun</td>
    <td>Tous à partir de l’entrée</td>
    <td>Message in-app</td>
    <td><b>Date d’expiration :</b> 28/02/2019 11h15 heure de la société</td>
    <td>Message in-app consulté</td>
    <td>L’utilisateur a maintenant ouvert l’application et recevra ce message, qu’il ait préalablement reçu ou pas le message de notification push.</td>
  </tr>
  <tr>
    <td>Rappel de 50 % de remise</td>
    <td>1 jour après que l’utilisateur a reçu l’étape précédente</td>
    <td>Tous à partir de l’entrée <br>
<br>
<b>Filtre :</b> Achat effectué il y a plus d’une semaine</td>
    <td>Message in-app</td>
    <td><b>Date d’expiration :</b> 28/02/2019 11h15 heure de la société</td>
    <td>Aucun (dernier message dans Canvas)</td>
    <td>L’utilisateur a reçu le message in-app à l’étape précédente, mais n’a pas effectué d’achat même s’il est dans l’application. <br>
<br>
Ce message est destiné à encourager l’utilisateur à effectuer un achat en utilisant la promotion.</td>
  </tr>
</tbody>
</table>

Comme vous pouvez le voir, les messages in-app expirent lorsque la promotion expire, afin d’éviter tout écart entre la messagerie et l’expérience client.

  {% endtab %}
  {% tab Onboarding %}

**Canvas Onboarding utilisateur**

La première impression que vous avez d’un utilisateur est peut-être la plus critique. Elle peut encourager ou décourager l’utilisateur à/de consulter votre application. Vos premières communications avec votre utilisateur doivent être judicieusement planifiées et doivent l’encourager à consulter souvent votre application, pour promouvoir son utilisation.

<table class="tg">
<thead>
  <tr>
    <th>Canvas Step</th>
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
    <td>S/O</td>
    <td>Audience avancée après le délai</td>
    <td>E-mail initial pour souhaiter la bienvenue à vos utilisateurs dans un projet, dans le cadre d’une adhésion ou d’un autre programme onboarding. <br>
<br>
Il est conçu pour diriger les utilisateurs vers votre application pour commencer leur onboarding.</td>
  </tr>
  <tr>
    <td>Message in-app jour 3 à 6</td>
    <td>3 jours après que l’utilisateur a reçu l’étape précédente</td>
    <td>Tous à partir de l’entrée</td>
    <td>Message in-app</td>
    <td><b>Expire : </b> 3 jours, une fois que l’étape est disponible</td>
    <td>Message in-app en direct</td>
    <td>Si l’utilisateur a donné suite à l’e-mail et a été dirigé vers l’application, il recevra le message in-app souhaité pour poursuivre ou lui rappeler l’onboarding et les exigences qui y sont associées.</td>
  </tr>
  <tr>
    <td>Notification push jour 5 </td>
    <td>2 jours après que l’utilisateur a reçu l’étape précédente</td>
    <td>Tous à partir de l’entrée</td>
    <td>Notification push</td>
    <td>S/O</td>
    <td>Message envoyé</td>
    <td>Après la réception de leur message in-app, les utilisateurs recevront une notification push de suivi pour poursuivre leur onboarding.</td>
  </tr>
</tbody>
</table>

Comme vous pouvez le voir, les messages de notification push suivent le message in-app pour garantir que l’utilisateur a consulté l’application et commencé son onboarding. Cela évite les courriers indésirables gênants et les messages hors d’usage, pouvant dissuader les utilisateurs de consulter votre application, au lieu de favoriser un bon ressenti par rapport à leur première expérience avec votre application.

  {% endtab %}
{% endtabs %}

## Options de comportement d’avancement

La fonctionnalité Comportement d’avancement vous permet de choisir les critères d’avancement dans votre Canvas Step. Les [étapes disposant uniquement de messages in-app](#steps-iam-only) ont différentes options d’avancement par rapport aux [étapes avec plusieurs types de messages](#steps-multiple-channels) (notification push, e-mail, etc.).

La livraison par événement n’est pas disponible pour des Canvas Step avec des messages in-app. Les étapes Canvas avec des messages in-app doivent être programmés. À la place, les messages in-app Canvas s’afficheront la première fois que votre utilisateur ouvre l’application (déclenché par la session de démarrage), une fois que le message planifié dans la Canvas Step lui a été envoyé.

Si vous avez plusieurs messages in-app dans un Canvas, un utilisateur doit démarrer plusieurs sessions pour recevoir chacun de ces messages.

{% alert important %}
Les messages in-app ne peuvent pas être déclenchés par des événements dans Canvas.
{% endalert %}

### Étapes avec messages in-app uniquement {#steps-iam-only}

Les étapes avec des messages in-app ont des options d’avancement spécifiques qui vous permettent d’indiquer la situation exacte pour laquelle votre message serait envoyé.

| Option | Description |
|---|---|---|
| Avance lorsqu’un message in-app a été consulté | Les utilisateurs avanceront aux étapes suivantes du Canvas lorsqu’ils consultent le message in-app dans votre application et qu’ils journalisent une impression du message in-app.  <br>
 <br>
 Les utilisateurs qui n’ont pas consulté le message in-app avant qu’il n’expire quitteront le Canvas et ne poursuivront pas aux étapes suivantes. |
| Avance pour message in-app activé | Les utilisateurs avanceront aux étapes suivantes du Canvas dès que le message in-app est activé. Les messages in-app sont activés une fois que le délai pour l’étape s’est écoulé et que les options d’audience pour l’étape ont été cochées.  <br>
 <br>
 Lorsque cette option est sélectionnée, tous les utilisateurs répondant au segment de l’étape et aux critères de filtre, avanceront aux étapes suivantes dans le Canvas. Utilisez cette option lorsque vous souhaitez que les utilisateurs avancent, que le message in-app ait été consulté ou qu’il expire. |
{: .reset-td-br-1 .reset-td-br-2}

![][2]

{% alert important %}
  Lorsque l’option **Avancer lorsque le message in-app est activé** est sélectionnée, le message in-app deviendra disponible jusqu’à ce qu’il expire, même si l’utilisateur est passé aux étapes suivantes. Si vous ne souhaitez pas que le message in-app soit activé lorsque les étapes suivantes du Canvas sont livrées, vérifiez que la date d’expiration est antérieure au délai dans les étapes suivantes.
{% endalert %}

### Étapes avec plusieurs canaux {#steps-multiple-channels}

Les étapes avec un message in-app et un autre canal de messagerie disposent des options d’avancement suivantes :

| Option | Description |
|---|---|---|
| Avancement lors de l’envoi du message | Les utilisateurs recevront un(e) e-mail/webhook/notification push ou consulteront le message in-app pour progresser vers les étapes suivantes dans le Canvas.  <br>
 <br>
  Si le message in-app expire et que l’utilisateur n’a pas reçu d’e-mail, de webhook ou de notification push ou n’a pas consulté le message in-app, il quittera Canvas et ne progressera pas vers les étapes suivantes. |
| Audience avancée immédiatement | Toute personne qui se trouve dans l’audience, avance aux étapes suivantes une fois le délai passé, que le message indiqué ait été vu ou pas.  <br>
 <br>
 Les utilisateurs doivent répondre au segment de l’étape et aux critères de filtre pour avancer aux étapes suivantes. |
{: .reset-td-br-1 .reset-td-br-2}

![][3]

{% alert important %}
  Lorsque l’option « Intégralité de l’audience » est sélectionnée, le message in-app deviendra disponible jusqu’à ce qu’il expire, même si l’utilisateur est passé aux étapes suivantes. Si vous ne souhaitez pas que le message in-app soit activé lorsque les étapes suivantes du Canvas sont livrées, vérifiez que la date d’expiration est antérieure au délai dans les étapes suivantes.
{% endalert %}

## Priorisation des messages in-app

Un client peut déclencher simultanément deux messages in-app dans votre Canvas. Dans ce cas, Braze respectera l’ordre de priorité suivant pour déterminer quel message in-app est affiché. Déplacez les différentes Canvas Steps pour réorganiser leur priorité. Par défaut, les étapes précédentes dans une Canvas Variant s’afficheront avant les étapes postérieures.

![]({% image_buster /assets/img_archive/step_priority.png %}){: style="max-width:80%"}

Naviguez jusqu’à **Paramètres d’envoi** de la section Canvas pour prioriser les messages in-app d’un Canvas, par rapport aux messages in-app d’autres Canvas et campagnes.

Par défaut, la priorité d’une étape Canvas est définie comme moyenne, avec les étapes les plus récentes ayant la priorité relative la plus élevée. Les priorités au niveau du Canvas et de la campagne sont également définies par défaut comme moyennes, avec la priorité relative la plus élevée définie par défaut sur les éléments les plus récents.

![]({% image_buster /assets/img_archive/canvas_priority.png %}){: style="max-width:70%"}

## Propriétés d’événement personnalisé dans un Canvas

La livraison par événement n’étant pas disponible pour les Canvas Steps avec messages in-app, vous ne pouvez pas non plus utiliser des propriétés de l’événement personnalisées pour ces étapes. Si vous voulez modifier des propriétés de l’événement dans Canvas, nous recommandons d’archiver vos propriétés d’événement comme attributs personnalisés dans votre première étape Canvas puis de personnaliser votre message in-app avec les attributs personnalisés dans la deuxième étape.


[1]: {% image_buster /assets/img/expires-after.png %} "IAM Live"
[2]: {% image_buster /assets/img/iam-advancement-behavior.png %} "IAM Live"
[3]: {% image_buster /assets/img/push-advancement-behavior.png %} "IAM Live"
