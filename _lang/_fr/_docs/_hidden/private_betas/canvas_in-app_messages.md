---
nav_title: Messages intégrés dans Canvas
permalink: "/fr/canvas_in-app_messages/"
hidden: vrai
---

# Messages In-App dans Canvas

{% include video.html id="6X8E20BlblI" align="right" %}

Une fois que vous avez configuré les options de délai et d'audience, vous pouvez ajouter un message dans l'application à votre Canvas en sélectionnant le message dans l'application "Canaux de messagerie".  Une fois que le délai d'une étape est passé et que les options du public ont été vérifiées, le message dans l'application sera mis en ligne et les utilisateurs le verront s'ils ouvrent l'application.

Vous pouvez personnaliser [quand votre message expirera](#in-app-message-expiration) et quel [comportement d'avancement](#advancement-behavior-options) il aura.

{% alert important %}
Messsages intégrés pour Canvas est actuellement en bêta. Veuillez contacter votre responsable de compte Braze si vous êtes intéressé à participer à la bêta.
{% endalert %}

## Expiration du message In-App

Dans le composeur de message intégré à l'application, vous avez la possibilité de choisir quand le message dans l'application expirera.

!\[Expire après \]\[1\]

| Option                       | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Expire le message... Après` | La première option vous permet d'expirer le message dans l'application par rapport au moment où l'étape devient disponible pour l'utilisateur. <br> <br> _Par exemple, un message dans l'application avec une expiration de deux jours serait disponible après que le délai de l'étape s'écoule et que les options d'audience soient vérifiées. Il serait alors disponible pendant 2 jours (48 heures) et pendant ces deux jours, les utilisateurs peuvent voir le message dans l'application s'ils ouvrent l'application._ |
| `Le message expire par...`   | La deuxième option vous permet de choisir une date et une heure spécifiques lorsque le message dans l'application sera plus long. <br> <br> _Par exemple, si vous avez une vente qui s'est terminée à une date et heure précises, vous pouvez sélectionner cette option afin qu'une fois la vente terminée, les utilisateurs ne voient plus le message associé dans l'application._                                                                                                                                         |
{: .reset-td-br-1 .reset-td-br-2}

### Cas d'utilisation

Quand devriez-vous utiliser cette fonctionnalité ? Braze recommande vivement que vous envisagiez d'utiliser cette fonctionnalité dans vos campagnes promotionnelles et d'intégration.

{% tabs %}
  {% tab Promotional %}
__Canevas promotionnels__

Les promotions, les coupons et les ventes ont souvent des dates d'expiration difficiles. Le Canvas décrit ci-dessous devrait alerter vos utilisateurs au moment le plus opportun où il y a une promotion qu'ils peuvent utiliser, et peut-être influencer un achat. Cette promotion expire par 2/28/2019 à 11h15 dans le fuseau horaire de la société.

| Étape de la toile              | Délai                                                                 | Audience                                                                                | Chaîne         | Expiration                                                                          | Avancée                                        | Détails du produit                                                                                                                                                                                                                                                                |
| ------------------------------ | --------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | -------------- | ----------------------------------------------------------------------------------- | ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Jour 1 : 50% de réduction      | Aucun                                                                 | Tout depuis l'entrée                                                                    | Pousser        | N/A                                                                                 | Toute l'audience après un délai                | Push initial qui avertit vos utilisateurs de la promotion. <br>  <br> Ceci est destiné à conduire les utilisateurs vers votre application pour profiter de la promotion.                                                                                              |
| In-App : 50% de réduction      | Aucun                                                                 | Tout depuis l'entrée                                                                    | Message In-App | Expire par: <br> 2/28/2019 <br> 11:15 AM <br> Heure de la société | Message In-App consulté                        | L'utilisateur a maintenant ouvert l'application et recevra ce message si oui ou non c'était à cause du message push avant.                                                                                                                                                        |
| 50% de réduction sur le rappel | 1 jour <br> Après que l'utilisateur reçoive l'étape précédente. | Tout depuis l'entrée <br> _Filtre : Dernière commande il y a plus d'une semaine._ | Message In-App | Expire par: <br> 2/28/2019 <br> 11:15 AM <br> Heure de la société | Aucun <br> _Dernier message sur Canvas._ | L'utilisateur a reçu le message dans l'application lors de l'étape précédente, mais n'a pas fait d'achat, bien qu'il soit dans l'application.  <br>  <br> Ce message est destiné à attirer davantage l'utilisateur pour effectuer un achat en utilisant la promotion. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

Comme vous pouvez le voir, les messages dans l'application expirent lorsque la promotion expire pour éviter toute divergence entre la messagerie et l'expérience du client.

  {% endtab %}
  {% tab Onboarding %}

__Canevas d’intégration des utilisateurs__

Votre première impression avec un utilisateur est peut-être la plus critique. Il peut faire ou casser des visites futures sur votre application. Vos communications initiales avec votre utilisateur devraient être raisonnablement chronométrées et encourager les visites fréquentes sur votre application pour promouvoir l'utilisation.

| Étape de la toile          | Délai                                                                   | Audience             | Chaîne         | Expiration                                            | Avancée                                  | Détails du produit                                                                                                                                                                                                                             |
| -------------------------- | ----------------------------------------------------------------------- | -------------------- | -------------- | ----------------------------------------------------- | ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| E-mail de bienvenue        | Aucun                                                                   | Tout depuis l'entrée | Courriel       | N/A                                                   | Toute l'audience après un délai          | Courriel initial qui accueille vos utilisateurs à un projet, à une adhésion ou à un autre programme d'intégration. <br>  <br> Ceci est destiné à conduire les utilisateurs vers votre application pour commencer leur intégration. |
| Message In-App du jour 3-6 | 3 jours <br> Après que l'utilisateur ait reçu l'étape précédente. | Tout depuis l'entrée | Message In-App | Expire trois jours après que l'étape soit disponible. | Message en direct dans l'application     | Si l'utilisateur a agi sur l'e-mail et a été poussé vers l'application, ils recevront le message souhaité dans l'application pour continuer ou leur rappeler leur intégration et toutes les conditions qui y sont associées.                   |
| Push du jour 5             | 2 jours <br> Après que l'utilisateur reçoive l'étape précédente.  | Tout depuis l'entrée | Pousser        | N/A                                                   | Avancer seulement si le message est reçu | Une fois que les utilisateurs auront reçu leur message dans l'application, ils recevront un push de suivi pour continuer leur intégration.                                                                                                     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

Comme vous pouvez le voir, les messages push sont espacés autour d'un message intégré pour s'assurer que l'utilisateur a visité l'application et commencé son intégration. Cela empêchera tout spam ennuyeux ou message hors de l'ordre qui pourrait dissuader les utilisateurs de visiter votre application, et au lieu de créer un ordre fluide et raisonnable à leurs expériences initiales avec votre application.

  {% endtab %}
{% endtabs %}

## Options de comportement d'avancement

La fonction de comportement avancement de Braze vous permet de choisir les critères de progression à travers votre pas de Canvas . [Les étapes avec seulement les messages dans l'application](#steps-with-in-app-messages-only) ont des options d'avancement différentes que [étapes avec plusieurs types de messages](#steps-with-multiple-message-channels) (push, email, etc.).

La distribution basée sur l'action n'est __pas disponible pour les étapes de Canvas avec les messages dans l'application__. Les étapes de Canvas avec les messages dans l'application __doivent être planifiées__. Au lieu de cela, Les messages de Canvas dans l'application apparaîtront la première fois que votre utilisateur ouvrira l'application après que le message programmé à l'étape Canvas leur ait été envoyé.

### Étapes avec les messages intégrés uniquement

Les étapes avec les messages dans l'application ont des options d'avancement spécifiques qui vous permettent de spécifier la situation exacte de l'envoi de votre message.

!\[iamlive.png\]\[2\]

| Option                       | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| In-App consultée             | Quand "In-App Viewed" est sélectionné, les utilisateurs passeront aux prochaines étapes du Canvas lorsqu'ils verront le message dans l'application dans votre application et connecteront une impression de message dans l'application.  <br> <br> _Les utilisateurs qui ne voient pas le message dans l'application avant qu'il n'expire quitteront le Canvas et ne passeront pas aux étapes suivantes._                                                                                                                                                                                                                               |
| En direct dans l'application | Lorsque "In-App Live" est sélectionné, les utilisateurs passeront aux étapes suivantes dans le Canvas dès que le message dans l'application sera en ligne. Les messages dans l'application sont en direct une fois que le délai pour l'étape est écoulé et que les options du public pour l'étape ont été vérifiées.  <br> <br> _Lorsque cette option est sélectionnée, tous les utilisateurs qui correspondent au segment de l'étape et aux critères de filtrage seront avancés aux étapes suivantes dans le Canvas. Utilisez cette option lorsque vous voulez que les utilisateurs avancent, que le message soit consulté ou expiré._ |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
  Lorsque "In-App Live" est sélectionné, le message dans l'application sera disponible jusqu'à ce qu'il expire, même si l'utilisateur est passé aux étapes suivantes. Si vous ne voulez pas que le message dans l'application soit en direct lorsque les prochaines étapes du Canvas sont livrées, s'assurer que l'expiration est plus courte que le délai lors des étapes suivantes.
{% endalert %}


### Étapes avec plusieurs canaux

!\[iampush.png\]\[3\]

Les étapes avec un message intégré et un autre canal ont les options d'avancement suivantes :

| Option                                  | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Message reçu                            | Lorsque le message reçu est sélectionné, les utilisateurs doivent recevoir un email/webhook/push ou voir le message dans l'application afin de passer aux étapes suivantes dans le Canvas.  <br> <br>  _Si le message dans l'application expire et que l'utilisateur n'a pas reçu le courriel/webhook/push ou n'a pas consulté le message dans l'application. ils quitteront le Canvas et ne passeront pas aux étapes suivantes._ |
| Avancer toute l'audience après un délai | Lorsque cette option est sélectionnée, tous les participants de l'étape passeront à l'étape suivante après le délai.  <br> <br> _Les utilisateurs doivent correspondre au segment de l'étape et filtrer les critères afin de passer aux étapes suivantes._                                                                                                                                                                        |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
  Lorsque "Toute l'audience" est sélectionnée, le message dans l'application sera disponible jusqu'à ce qu'il expire, même si l'utilisateur est passé aux étapes suivantes. Si vous ne voulez pas que le message dans l'application soit en direct lorsque les prochaines étapes du Canvas sont livrées, s'assurer que l'expiration est plus courte que le délai lors des étapes suivantes.
{% endalert %}
[1]: {% image_buster /assets/img/expires-after.png %} "IAM Live"
