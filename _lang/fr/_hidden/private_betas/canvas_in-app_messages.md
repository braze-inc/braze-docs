---
nav_title: Messages dans l’application de Canvas
permalink: "/canvas_in-app_messages/"
hidden: true
---

# Messages dans l’application de Canvas

{% multi_lang_include video.html id="6X8E20BlblI" align="right" %}

Une fois que vous avez configuré les options de délai et d’audience, vous pouvez ajouter un message dans l’application à votre Canvas en sélectionnant **Message In-App** dans le volet **Canaux de messagerie**. Une fois que le délai d’une étape est passé et que les options d’audience ont été cochées, le message dans l’application sera activé et les utilisateurs le verront à l’ouverture de l’application.

Vous pouvez personnaliser [la date d’expiration de votre message](#in-app-message-expiration) et son [comportement d’avancement](#advancement-behavior-options).

{% alert important %}
Les messageries dans l’application de Canvas sont actuellement en bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à la bêta.
{% endalert %}

## Expiration de message dans l’application

Dans l’éditeur de messages dans l’application, vous pouvez choisir la date d’expiration du message in-app.

![La section Expiration du message dans l’application, avec le message in-app configuré pour expirer un jour après la disponibilité de l’étape.][1]

| Option | Description |
|---|---|---|
| `Message Expires ... After` | La première option vous permet de définir la date d’expiration d’un message in-app en fonction de la disponibilité de l’étape pour l’utilisateur. <br> <br> Par exemple, un message dans l’application avec un délai d’expiration de deux jours deviendra disponible une fois le délai de l’étape écoulé et lorsque les options d’audience seront cochées. Il sera alors disponible pendant 2 jours (48 heures) et au cours de ces deux jours, les utilisateurs pourront voir le message in-app s’ils ouvrent l’application. |
| `Message Expires By ...` | La deuxième option vous permet de choisir une date et une heure spécifiques auxquelles le message in-app ne sera plus disponible. <br> <br> Par exemple, si vous avez une vente qui se termine à une heure et une date spécifiques, vous pourrez sélectionner cette option de sorte qu’une fois la vente terminée, les utilisateurs ne verront plus le message in-app associé. |
{: .reset-td-br-1 .reset-td-br-2}

### Cas d’utilisation

Quand devez-vous utiliser cette fonctionnalité ? Braze recommande vivement d’utiliser cette fonctionnalité dans vos campagnes promotionnelles et onboarding.

{% tabs %}
  {% tab Promotional %}
**Canvas promotionnels**

Les promotions, les coupons de réduction et les ventes ont souvent des dates d’expiration serrées. Le Canvas suivant doit alerter vos utilisateurs au moment le plus opportun qu’une promotion dont ils pourraient bénéficier est en cours, susceptible d’influencer un achat. Cette promotion expire le 28 février 2019 à 11h15, fuseau horaire de l’entreprise

| Canvas Step | Délai | Audience | Canal | Expiration | Avancement | Détails |
|---|---|---|
| Jour 1 : 50 % de remise | Aucun | Tous à partir de l’entrée | Notification push | S/O | Intégralité de l’audience après le délai | Notification push qui alerte vos utilisateurs de la promotion. <br>  <br> Elle a pour but de diriger vos utilisateurs vers votre application pour profiter de la promotion. |
| In-App: 50 % de remise | Aucun | Tous à partir de l’entrée | Message dans l’application | Date d’expiration : <br> 28/02/2019 <br> 11h15 <br> heure de l’entreprise | Message dans l’application consulté | L’utilisateur a maintenant ouvert l’application et recevra ce message, qu’il ait préalablement reçu ou pas le message de notification push. |
| Rappel de 50 % de remise | 1 jour <br> après l’obtention de l’étape précédente par l’utilisateur. | Tous à partir de l’entrée <br> _Filtre : Achat effectué il y a plus d’une semaine._ | Message dans l’application |  Date d’expiration : <br> 28/02/2019 <br> 11h15 <br> heure de l’entreprise  | Aucun. <br> Dernier message dans Canvas. | L’utilisateur a reçu le message in-app à l’étape précédente, mais n’a pas effectué d’achat même s’il est dans l’application.  <br>  <br> Ce message est destiné à encourager l’utilisateur à effectuer un achat en utilisant la promotion. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

Comme vous pouvez le voir, les messages dans l’application expirent lorsque la promotion prend fin pour éviter tout écart entre la messagerie et l’expérience client.

  {% endtab %}
  {% tab Onboarding %}

**Canvas Onboarding utilisateur**

La première impression que vous avez d’un utilisateur est peut-être la plus critique. Elle peut encourager ou décourager l’utilisateur à/de consulter votre application. Vos premières communications avec votre utilisateur doivent être judicieusement planifiées et doivent l’encourager à consulter souvent votre application, pour promouvoir son utilisation.

| Canvas Step | Délai | Audience | Canal | Expiration | Avancement | Détails |
|---|---|---|
| E-mail de bienvenue | Aucun | Tous à partir de l’entrée | E-mail | S/O | Intégralité de l’audience après le délai | E-mail initial pour souhaiter la bienvenue à vos utilisateurs dans un projet, dans le cadre d’une adhésion ou d’un autre programme onboarding. <br>  <br> Il est conçu pour diriger les utilisateurs vers votre application pour commencer leur onboarding. |
| Message dans l’application, jour 3 à 6 | 3 jours <br> après l’obtention de l’étape précédente par l’utilisateur. | Tous à partir de l’entrée | Message dans l’application | Expire 3 jours après la disponibilité de l’étape. | Message dans l’application en direct | Si l’utilisateur a donné suite à l’e-mail et a été dirigé vers l’application, il recevra le message dans l’application souhaité pour poursuivre ou lui rappeler l’onboarding et les exigences qui y sont associées. |
| Notification push, jour 5 | 2 jours <br> après l’obtention de l’étape précédente par l’utilisateur. | Tous à partir de l’entrée | Notification push |  S/O  | Avance uniquement si message reçu | Après la réception de leur message dans l’application, les utilisateurs recevront une notification push de suivi pour poursuivre leur onboarding. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

Comme vous pouvez le voir, les messages de notification push suivent le message dans l’application pour garantir que l’utilisateur a bien consulté l’application et commencé son onboarding. Cela évite les courriers indésirables gênants et les messages hors d’usage, pouvant dissuader les utilisateurs de consulter votre application, au lieu de favoriser un bon ressenti par rapport à leur première expérience avec votre application.

  {% endtab %}
{% endtabs %}

## Options de comportement d’avancement

La fonctionnalité Comportement d’avancement vous permet de choisir les critères d’avancement de votre étape Canvas. Les [étapes disposant uniquement de messages in-app](#steps-with-in-app-messages-only) ont différentes options d’avancement par rapport aux [étapes avec plusieurs types de messages](#steps-with-multiple-message-channels) (notification push, e-mail, etc.).

La livraison par événement n’est pas disponible pour des Canvas Step avec des messages dans l’application. Les étapes Canvas avec des messages in-app doivent être programmés. À la place, les messages in-app Canvas s’afficheront la première fois que votre utilisateur ouvre l’application, une fois que le message planifié dans l’étape Canvas lui a été envoyé.

### Étapes avec messages in-app uniquement

Les étapes avec des messages in-app ont des options d’avancement spécifiques qui vous permettent d’indiquer la situation exacte pour laquelle votre message serait envoyé.

| Option | Description |
|---|---|---|
| Message in-app consulté | Lorsque l’option **Message in-app consulté** est sélectionnée, les utilisateurs avanceront aux étapes suivantes du Canvas lorsqu’ils consultent le message in-app dans votre application et qu’ils journalisent une impression du message in-app.  <br> <br> Les utilisateurs qui n’ont pas consulté le message in-app avant qu’il n’expire quitteront le Canvas et ne poursuivront pas aux étapes suivantes. |
| En direct dans l’application | Lorsque l’option **Message in-app en direct** est sélectionnée, les utilisateurs avanceront aux étapes suivantes du Canvas dès que le message in-app est activé. Les messages dans l’application sont activés une fois que le délai pour l’étape est écoulé et que les options d’audience pour l’étape ont été cochées.  <br> <br> Lorsque cette option est sélectionnée, tous les utilisateurs répondant au segment de l’étape et aux critères de filtre, avanceront aux étapes suivantes dans le Canvas. Utilisez cette option lorsque vous souhaitez que les utilisateurs avancent, que le message in-app ait été consulté ou qu’il expire. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Lorsque l’option **Message in-app en direct** est sélectionnée, le message in-app deviendra disponible jusqu’à ce qu’il expire, même si l’utilisateur est passé aux étapes suivantes. Si vous ne souhaitez pas que le message dans l’application soit activé lorsque les étapes suivantes du Canvas sont livrées, vérifiez que la date d’expiration est antérieure au délai dans les étapes suivantes.
{% endalert %}

### Étapes avec plusieurs canaux

Les étapes avec un message in-app et un autre canal de messagerie disposent des options d’avancement suivantes :

| Option | Description |
|---|---|---|
| Message reçu | Si message reçu est sélectionné, les utilisateurs recevront un(e) e-mail/webhook/notification push ou consulteront le message in-app pour progresser vers les étapes suivantes dans le Canvas. <br> <br> Si le message in-app expire et que l’utilisateur n’a pas reçu d’e-mail, de webhook ou de notification push ou n’a pas consulté le message in-app, il quittera Canvas et ne progressera pas vers les étapes suivantes. |
| Intégralité de l’audience après le délai (avancé) | Lorsque cette option est sélectionnée, tous les utilisateurs dans l’audience avanceront aux étapes suivantes une fois le délai écoulé.  <br> <br> Les utilisateurs doivent répondre au segment de l’étape et aux critères de filtre pour avancer aux étapes suivantes. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Lorsque l’option **Intégralité de l’audience ** est sélectionnée, le message in-app deviendra disponible jusqu’à ce qu’il expire, même si l’utilisateur est passé aux étapes suivantes. Si vous ne souhaitez pas que le message dans l’application soit activé lorsque les étapes suivantes du Canvas sont livrées, vérifiez que la date d’expiration est antérieure au délai dans les étapes suivantes.
{% endalert %}

[1]: {% image_buster /assets/img/expires-after.png %} "IAM Live"
