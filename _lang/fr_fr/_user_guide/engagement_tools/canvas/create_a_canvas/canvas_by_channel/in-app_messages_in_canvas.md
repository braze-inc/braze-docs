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

Une fois les délais écoulés et les options d'audience cochées, le message in-app sera mis en ligne/en production/instantané, et les utilisateurs le verront s'ils ouvrent l'application. Les messages in-app dans Canvas ne peuvent être déclenchés que par l'événement `start session`. Ils ne peuvent pas être déclenchés par des événements personnalisés dans un composant Canvas.

Pour les étapes du canvas dont l'entrée est déclenchée par un événement, les utilisateurs peuvent entrer dans le canvas à mi-session. Cependant, comme indiqué ci-dessus, les messages in-app ne se déclenchent pas avant le début de la session suivante, de sorte que ces utilisateurs manqueraient le message in-app initial puisqu'ils n'étaient pas éligibles pour entrer dans le Canvas avant le début de la session.

## Ajouter un message in-app à votre parcours utilisateur

Pour ajouter un message in-app à votre canvas, procédez comme suit :

1. Ajoutez une étape [Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) à votre parcours utilisateur.
2. Sélectionnez **Message in-app** pour votre **canal de communication.** 
3. Déterminez la [date d'expiration de votre message](#in-app-message-expiration) et son [comportement à l'avancement](#advancement-behavior-options).

### Expiration de message in-app

Dans l'éditeur de messages in-app, vous pouvez choisir la date d'expiration du message in-app. Pendant ce temps, le message in-app attendra d'être consulté jusqu'à ce qu'il atteigne la date d'expiration. Après l'envoi du message in-app, celui-ci peut être consulté une seule fois.

![][1]

| Option | Description | Exemple |
|---|---|---|
| Le message expire après la date indiquée | La première option vous permet de définir la date d’expiration d’un message in-app en fonction du début de disponibilité de l’étape pour l’utilisateur. | Par exemple, un message in-app avec un délai d’expiration de deux jours deviendra disponible une fois le délai de l’étape écoulé et lorsque les options d’audience seront cochées. Il sera alors disponible pendant 2 jours (48 heures) et au cours de ces deux jours, les utilisateurs pourront voir le message in-app s’ils ouvrent l’application. |
| Le message expire à une date indiquée | La seconde option vous permet de choisir une date et une heure spécifiques auxquelles le message in-app ne sera plus disponible. | Par exemple, si vous avez une vente qui s'est terminée à une date et une heure spécifiques, vous pouvez sélectionner cette option pour que les utilisateurs ne voient plus le message in-app associé lorsque la vente se termine. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Cas d’utilisation

Vous pouvez utiliser les messages in-app dans vos canevas de promotion et d'onboarding.

{% tabs %}
  {% tab Promotionnel %}

Les promotions, les coupons de réduction et les ventes ont souvent des dates d’expiration serrées. Le Canvas suivant doit alerter vos utilisateurs au moment le plus opportun qu’une promotion dont ils pourraient bénéficier est en cours, susceptible d’influencer un achat. Cette promotion expire le 28 février 2019 à 11 h 15 dans le fuseau horaire de l'entreprise.

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

Comme vous pouvez le voir, les messages in-app expirent lorsque la promotion prend fin pour éviter tout écart entre les envois de messages et l’expérience client.

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

Comme vous pouvez le voir, les messages de notification push suivent le message in-app pour garantir que l’utilisateur a bien consulté l’application et commencé son onboarding. Cela évite les courriers indésirables gênants et les envois de messages dans le désordre, pouvant dissuader les utilisateurs de consulter votre application, au lieu de favoriser un bon ressenti par rapport à leur première expérience avec votre application.

  {% endtab %}
{% endtabs %}

### Options de comportement d’avancement

Dans Canvas, les étapes de messages font automatiquement avancer tous les utilisateurs qui entrent dans l'étape. Pour utiliser l'option **Avancer lorsque le message a été envoyé**, ajoutez un [parcours d'audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) distinct pour filtrer les utilisateurs qui n'ont pas reçu l'étape précédente.

{% details Comportement original de l'éditeur de canvas %}

{% alert important %}
Vous ne pouvez plus créer ou dupliquer des toiles à l'aide de l'éditeur original. Cette section est disponible à titre de référence lorsque vous comprenez comment fonctionne le comportement d’avancement pour les étapes avec des messages in-app.
{% endalert %}

Les Canvas créez dans l’éditeur d’origine doivent spécifier le comportement d’avancement, à savoir le critère d’avancement à travers votre composant Canvas. Les [étapes comportant uniquement des messages in-app](#steps-iam-only) ont des options d'avancement différentes de celles [comportant plusieurs types de messages](#steps-multiple-channels) (notifications push, e-mail, etc.). Pour les messages in-app dans le flux de travail Canvas Flow, cette option est définie pour faire avancer immédiatement l’audience.

La livraison par événement n’est pas disponible pour des étapes de Canvas comportant des messages in-app. Les étapes Canvas avec des messages in-app doivent être programmés. À la place, les messages in-app Canvas s’afficheront la première fois que votre utilisateur ouvre l’application (déclenché par la session de démarrage), une fois que le message planifié dans le composant Canvas lui a été envoyé.

Si vous avez plusieurs messages in-app dans un Canvas, un utilisateur doit démarrer plusieurs sessions pour recevoir chacun de ces messages.

{% alert important %}
Les messages in-app ne peuvent pas être déclenchés par des événements dans Canvas.
{% endalert %}

![][2]

{% alert important %}
Lorsque l'option **Avancer lorsque le message in-app est activé** est sélectionnée, le message in-app deviendra disponible jusqu'à son expiration, même si l'utilisateur est passé aux étapes suivantes. Si vous ne souhaitez pas que le message in-app soit activé lorsque les étapes suivantes du Canvas sont livrées, vérifiez que la date d’expiration est antérieure au délai dans les étapes suivantes.
{% endalert %}

#### Étapes avec plusieurs canaux {#steps-multiple-channels}

Les étapes avec un message in-app et un autre canal de communication disposent des options d’avancement suivantes :

| Option | Description |
|---|---|---|
| Avancement lors de l’envoi du message | Les utilisateurs recevront un e-mail, un webhook ou une notification push, ou bien consulteront le message in-app pour progresser vers les étapes suivantes dans le Canvas.  <br> <br>  Si le message in-app expire et que l’utilisateur n’a pas reçu d’e-mail, de webhook ou de notification push ou n’a pas consulté le message in-app, il quittera Canvas et ne progressera pas vers les étapes suivantes. |
| Audience avancée immédiatement | Toute personne qui se trouve dans l’audience, avance aux étapes suivantes une fois le délai passé, que le message indiqué ait été vu ou pas.  <br> <br> Les utilisateurs doivent correspondre aux critères de segmentation et de filtrage de l'étape pour passer aux étapes suivantes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][3]

{% alert important %}
Lorsque l'option **Toute l'audience** est sélectionnée, le message in-app sera disponible jusqu'à son expiration, même si l'utilisateur est passé aux étapes suivantes. Si vous ne souhaitez pas que le message in-app soit activé lorsque les étapes suivantes du canvas sont livrées, vérifiez que la date d’expiration est antérieure au délai dans les étapes suivantes.
{% endalert %}

{% enddetails %}

## Priorisation des messages in-app

Un client peut déclencher simultanément deux messages in-app dans votre Canvas. Lorsque cela se produit, Braze respecte l'ordre de priorité suivant pour déterminer quel message in-app est affiché. Déplacez les différentes étapes de Canvas pour réorganiser leur priorité. Par défaut, les étapes précédentes d'une variante de canvas s’afficheront avant les étapes postérieures.

![]({% image_buster /assets/img_archive/step_priority.png %}){: style="max-width:80%"}

Accédez aux **paramètres d'envoi de** la section Canvas pour donner la priorité aux messages in-app d'un Canvas par rapport aux messages in-app d'autres Canvas et campagnes.

![]({% image_buster /assets/img_archive/canvas_send_settings.png %})

Par défaut, la priorité d’un composant Canvas est définie comme moyenne, avec les étapes les plus récentes ayant la priorité relative la plus élevée. Les priorités au niveau du Canvas et de la campagne sont également définies par défaut comme moyennes, avec la priorité relative la plus élevée définie par défaut sur les éléments les plus récents.

![]({% image_buster /assets/img_archive/canvas_priority.png %}){: style="max-width:85%"}

### Brouillons d'un Canvas actif

Lorsque vous modifiez un brouillon d'un canvas actif, les modifications apportées à la priorité des messages in-app dans les **paramètres d'envoi** ne sont pas enregistrées avec le brouillon. Ces modifications sont appliquées directement au canvas actif lorsque la fenêtre modale du trieur de priorités est fermée. Cependant, dans une étape Message, le trieur de priorités sera mis à jour lorsqu'un utilisateur lancera le brouillon, étant donné que les paramètres de l'étape s'appliquent au niveau de l'étape.

## Propriétés d’événement personnalisé dans un Canvas

La livraison par événement n'est pas disponible pour les étapes du canvas avec des messages in-app. Cela signifie que vous ne pouvez pas non plus utiliser les propriétés d'événement personnalisées pour ces étapes. 

Pour modéliser les propriétés d'événement dans Canvas, nous vous recommandons de stocker vos propriétés d'événement en tant qu'attributs personnalisés dans votre première étape de Canvas et de personnaliser votre message in-app avec les attributs personnalisés dans la deuxième étape.


[1]: {% image_buster /assets/img/expires-after.png %} "IAM Live"
[2]: {% image_buster /assets/img/iam-advancement-behavior.png %} "IAM Live"
[3]: {% image_buster /assets/img/push-advancement-behavior.png %} "IAM Live"
