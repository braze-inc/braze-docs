---
nav_title: Messages In-App dans Canvas
article_title: Messages intégrés dans Canvas
page_order: 6
page_type: Référence
description: "Cet article de référence décrit les fonctionnalités et les nuances propres aux messages In-App de Canvas que vous pouvez ajouter à votre Canvas pour afficher la riche messagerie."
tool: Toile
channel: messages intégrés à l'application
---

# Messages intégrés dans Canvas

{% include video.html id="6X8E20BlblI" align="right" %}

> Les messages intégrés peuvent être ajoutés dans le cadre de votre voyage sur Canvas pour afficher une messagerie enrichie lorsque votre client s'engage avec votre application. Cet article décrit les fonctionnalités et les nuances spécifiques aux messages intégrés à Canvas dans l'application.

Avant de continuer, vous devriez avoir déjà [créé votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) et configurer les options de retard et d'audience.

Vous pouvez maintenant ajouter un message dans l'application à votre Canvas en sélectionnant un message dans l'application à partir des **canaux de messagerie**. Une fois que le délai d'une étape est passé et que les options du public ont été vérifiées, le message dans l'application sera mis en ligne et les utilisateurs le verront s'ils ouvrent l'application. Les messages intégrés dans Canvas ne peuvent être déclenchés que par l'événement de déclenchement de la `session de démarrage` - ils ne peuvent pas être déclenchés par des événements personnalisés dans une étape de Canvas !

Vous pouvez personnaliser [quand votre message expirera](#in-app-message-expiration) et quel [comportement d'avancement](#advancement-behavior-options) il aura.

## Expiration du message dans l'application

Dans le composeur de message intégré à l'application, vous avez la possibilité de choisir quand le message dans l'application expirera. Pendant cette période, le message dans l'application s'assied et attend d'être consulté jusqu'à ce qu'il ait atteint la date d'expiration. Une fois envoyé, le message dans l'application peut être visualisé au plus une fois. !\[Expire après \]\[1\]

| Option                                       | Libellé                                                                                                                                        | Exemple                                                                                                                                                                                                                                                                                                                                                                  |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Le message expire après la période spécifiée | La première option vous permet d'expirer le message dans l'application par rapport au moment où l'étape devient disponible pour l'utilisateur. | Par exemple, un message dans l'application avec une expiration de deux jours deviendrait disponible après que le délai de l'étape soit écoulé et que les options d'audience soient vérifiées. Il serait alors disponible pendant 2 jours (48 heures) et pendant ces deux jours, les utilisateurs peuvent voir le message dans l'application s'ils ouvrent l'application. |
| Le message expire à la date spécifiée        | La deuxième option vous permet de choisir une date et une heure spécifiques lorsque le message dans l'application sera plus long.              | Par exemple, si vous avez une vente qui s'est terminée à une date et heure précises, vous pouvez sélectionner cette option afin qu'une fois la vente terminée, les utilisateurs ne voient plus le message associé dans l'application.                                                                                                                                    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Cas d'utilisation

Quand devriez-vous utiliser cette fonctionnalité ? Braze recommande vivement que vous envisagiez d'utiliser cette fonctionnalité dans vos campagnes promotionnelles et d'intégration.

{% tabs %}
  {% tab Promotional %}
__Canevas promotionnels__

Les promotions, les coupons et les ventes ont souvent des dates d'expiration difficiles. Le Canvas décrit ci-dessous devrait alerter vos utilisateurs au moment le plus opportun où il y a une promotion qu'ils peuvent utiliser, et peut-être influencer un achat. Cette promotion expire par 2/28/2019 à 11h15 dans le fuseau horaire de la société.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table class="tg">
<thead>
  <tr>
    <th>Étape de la toile</th>
    <th>Délai</th>
    <th>Audience</th>
    <th>Chaîne</th>
    <th>Expiration</th>
    <th>Avancée</th>
    <th>Détails du produit</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Jour 1: 50% de réduction</td>
    <td>Aucun</td>
    <td>Tout depuis l'entrée</td>
    <td>Pousser</td>
    <td>N/A</td>
    <td>Audience Avancée après délai</td>
    <td>Push initial qui avertit vos utilisateurs de la promotion. Ceci est destiné à conduire les utilisateurs vers votre application pour profiter de la promotion.</td>
  </tr>
  <tr>
    <td>In-app : 50% de réduction</td>
    <td>Aucun</td>
    <td>Tout depuis l'entrée</td>
    <td>Message dans l'application</td>
    <td><b>Expire par:</b> 2/28/2019 11:15 AM Company Time</td>
    <td>Message In-App consulté</td>
    <td>L'utilisateur a maintenant ouvert l'application et recevra ce message si oui ou non c'était à cause du message push avant.</td>
  </tr>
  <tr>
    <td>50% de réduction sur le rappel</td>
    <td>1 jour après que l'utilisateur ait reçu l'étape précédente</td>
    <td>Tout depuis l'entrée <br><br><b>Filtre:</b> Dernière commande il y a plus d'une semaine</td>
    <td>Message dans l'application</td>
    <td><b>Expire par:</b> 2/28/2019 11:15 AM Company Time</td>
    <td>Aucun (dernier message dans Canvas)</td>
    <td>L'utilisateur a reçu le message dans l'application lors de l'étape précédente, mais n'a pas fait d'achat, bien qu'il soit dans l'application. <br><br>Ce message est destiné à attirer davantage l'utilisateur pour effectuer un achat en utilisant la promotion.</td>
  </tr>
</tbody>
</table>

Comme vous pouvez le voir, les messages dans l'application expirent lorsque la promotion expire pour éviter toute divergence entre la messagerie et l'expérience du client.

  {% endtab %}
  {% tab Onboarding %}

__Canevas d’intégration des utilisateurs__

Votre première impression avec un utilisateur est peut-être la plus critique. Il peut faire ou casser des visites futures sur votre application. Vos communications initiales avec votre utilisateur devraient être raisonnablement chronométrées et encourager les visites fréquentes sur votre application pour promouvoir l'utilisation.

<table class="tg">
<thead>
  <tr>
    <th>Étape de la toile</th>
    <th>Délai</th>
    <th>Audience</th>
    <th>Chaîne</th>
    <th>Expiration</th>
    <th>Avancée</th>
    <th>Détails du produit</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>E-mail de bienvenue</td>
    <td>Aucun</td>
    <td>Tout depuis l'entrée</td>
    <td>Courriel</td>
    <td>N/A</td>
    <td>Audience Avancée après délai</td>
    <td>Courriel initial qui accueille vos utilisateurs à un projet, à une adhésion ou à un autre programme d'intégration. <br><br>Ceci est destiné à conduire les utilisateurs vers votre application pour commencer leur intégration.</td>
  </tr>
  <tr>
    <td>Message du jour 3–6 dans l'application</td>
    <td>3 jours après que l'utilisateur ait reçu l'étape précédente</td>
    <td>Tout depuis l'entrée</td>
    <td>Message dans l'application</td>
    <td><b>Expire :</b> 3 jours après que l'étape soit disponible</td>
    <td>Message en direct dans l'application</td>
    <td>Si l'utilisateur a agi sur l'e-mail et a été poussé vers l'application, ils recevront le message souhaité dans l'application pour continuer ou leur rappeler leur intégration et toutes les conditions qui y sont associées.</td>
  </tr>
  <tr>
    <td>Poussée du jour 5 </td>
    <td>2 jours après que l'utilisateur ait reçu l'étape précédente</td>
    <td>Tout depuis l'entrée</td>
    <td>Pousser</td>
    <td>N/A</td>
    <td>Message envoyé</td>
    <td>Une fois que les utilisateurs auront reçu leur message dans l'application, ils recevront un push de suivi pour continuer leur intégration.</td>
  </tr>
</tbody>
</table>

Comme vous pouvez le voir, les messages push sont espacés autour d'un message intégré pour s'assurer que l'utilisateur a visité l'application et commencé son intégration. Cela empêchera tout spam ennuyeux ou message hors de l'ordre qui pourrait dissuader les utilisateurs de visiter votre application, et au lieu de créer un ordre fluide et raisonnable à leurs expériences initiales avec votre application.

  {% endtab %}
{% endtabs %}

## Options de comportement d'avancement

La fonction de comportement avancement de Braze vous permet de choisir les critères de progression à travers votre pas de Canvas . [Les étapes avec seulement les messages dans l'application](#steps-iam-only) ont des options d'avancement différentes que [étapes avec plusieurs types de messages](#steps-multiple-channels) (push, email, etc.).

La livraison par action n'est pas disponible pour les étapes de Canvas avec les messages dans l'application. Les étapes de la toile avec les messages intégrés à l'application doivent être planifiées. Au lieu de cela, Les messages intégrés à Canvas apparaîtront la première fois que votre utilisateur ouvrira l'application (déclenchée par la session de démarrage) après que le message programmé à l'étape Canvas leur ait été envoyé.

Si vous avez plusieurs messages dans l'application dans un Canvas, un utilisateur doit démarrer plusieurs sessions pour recevoir chacun de ces messages.

{% alert important %}
Les messages intégrés ne peuvent pas être déclenchés par des événements dans Canvas.
{% endalert %}

### Étapes uniquement avec les messages dans l'application {#steps-iam-only}

Les étapes avec les messages dans l'application ont des options d'avancement spécifiques qui vous permettent de spécifier la situation exacte de l'envoi de votre message.

!\[iamlive.png\]\[2\]

| Option                                                      | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Avancer lorsque le message intégré est visualisé            | Les utilisateurs passeront aux prochaines étapes du Canvas lorsqu'ils verront le message dans l'application dans votre application et connecteront une impression de message dans l'application.  <br> <br> Les utilisateurs qui ne voient pas le message dans l'application avant qu'il n'expire quitteront le Canvas et ne passeront pas aux étapes suivantes.                                                                                                                                                                                                                                   |
| Avancer lorsque le message est en direct dans l'application | Les utilisateurs passeront aux étapes suivantes dans le Canvas dès que le message dans l'application sera mis en ligne. Les messages dans l'application sont en direct une fois que le délai pour l'étape est écoulé et que les options du public pour l'étape ont été vérifiées.  <br> <br> Lorsque cette option est sélectionnée, tous les utilisateurs qui correspondent au segment de l'étape et aux critères de filtrage seront avancés aux étapes suivantes dans le Canvas. Utilisez cette option lorsque vous voulez que les utilisateurs avancent, que le message soit consulté ou expiré. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
  Lorsque **Advance When In-App Message Live** est sélectionné, le message dans l'application sera disponible jusqu'à ce qu'il expire, même si l'utilisateur est passé aux étapes suivantes. Si vous ne voulez pas que le message dans l'application soit en direct lorsque les prochaines étapes du Canvas sont livrées, s'assurer que l'expiration est plus courte que le délai lors des étapes suivantes.
{% endalert %}

### Étapes avec plusieurs canaux {#steps-multiple-channels}

!\[Comportement de l'avancement des pousss\]\[3\]

Les étapes avec un message intégré et un autre canal ont les options d'avancement suivantes :

| Option                                  | Libellé                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Avancer lorsque le message a été envoyé | Les utilisateurs doivent recevoir un email/webhook/push ou voir le message dans l'application pour passer aux étapes suivantes dans le Canvas.  <br> <br>  Si le message dans l'application expire et que l'utilisateur n'a pas été envoyé le courriel/webhook/push ou a consulté le message dans l'application. ils quitteront le Canvas et ne passeront pas aux étapes suivantes. |
| Audience immédiatement Avancée          | Tous les auditeurs de l'étape passent à l'étape suivante après le délai écoulé, qu'ils aient vu ou non le message noté.  <br> <br> Les utilisateurs doivent correspondre au segment de l'étape et filtrer les critères pour passer aux étapes suivantes.                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
  Lorsque "Toute l'audience" est sélectionnée, le message dans l'application sera disponible jusqu'à ce qu'il expire, même si l'utilisateur est passé aux étapes suivantes. Si vous ne voulez pas que le message dans l'application soit en direct lorsque les prochaines étapes du Canvas sont livrées, s'assurer que l'expiration est plus courte que le délai lors des étapes suivantes.
{% endalert %}

## Propriétés personnalisées de l'événement dans une toile

En raison du fait que la distribution basée sur l'action n'est pas disponible pour les étapes de Canvas avec des messages dans l'application, vous ne pouvez pas non plus utiliser de propriétés d'événement personnalisées pour ces étapes. Si vous souhaitez modéliser les propriétés d'événements sur Canvas, nous vous recommandons de stocker vos propriétés d'événements en tant qu'attributs personnalisés dans votre première étape de Canvas puis la personnalisation de votre message dans l'application avec les attributs personnalisés dans la deuxième étape.
[1]: {% image_buster /assets/img/expires-after.png %} "IAM Live" [2]: {% image_buster /assets/img/iam-advancement-behavior. ng %} "IAM Live" [3]: {% image_buster /assets/img/push-advancement-behavior.png %} "IAM Live"
