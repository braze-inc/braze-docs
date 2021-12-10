---
nav_title: Twilio
permalink: /fr/partners/twilio/
description: "Cet article décrit le partenariat entre Braze et Twilio."
page_type: partenaire
channel:
  - SMS
  - Webhook
hidden: vrai
---

# Twilio

{% alert warning %}
Veuillez noter que le soutien à l'intégration des Webhook de Twilio sera interrompu le 31 janvier 2020. Si vous souhaitez toujours accéder aux services SMS avec Braze, veuillez consulter notre [documentation SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/).
{% endalert %}

For this example, we'll configure the Braze webhook channel to send SMS and MMS to your users, via Twilio's [message sending API][20]. Pour plus de commodité, un modèle de webhook Twilio est inclus dans le tableau de bord.

## URL HTTP

L'URL du Webhook est fournie par Twilio dans votre tableau de bord. Cette URL est unique à votre compte Twilio car elle contient votre ID de compte Twilio (`TWILIO_ACCOUNT_SID`).

Dans notre exemple Twilio, l'URL du webhook est `https://api.twilio.com/2010-04-01/Accounts/TWILIO_ACCOUNT_SID/Messages.json`. Vous pouvez trouver cette URL dans la section *Pour commencer* de la console Twilio.

!\[Twilio_Console\]\[28\]

## Corps de la requête

L'API Twilio attend que le corps de la requête soit encodé par l'URL, donc nous devons commencer par changer le type de requête dans le webhook Braze en `Texte brut`. Les paramètres requis pour le corps de la requête sont *To*, *From*, et *Body*.

La capture d'écran ci-dessous est un exemple de ce à quoi votre demande pourrait ressembler si vous envoyez un SMS au numéro de téléphone de chaque utilisateur avec le corps "Bonjour de Braze!".

- Vous devrez avoir des numéros de téléphone valides sur chaque profil d'utilisateur dans votre public cible.
- Pour répondre au format de requête de Twilio, utilisez le filtre `url_param_escape` Liquid sur le contenu de votre message. Ce filtre encode une chaîne de caractères de sorte que tous les caractères sont autorisés dans une requête HTML ; par exemple, le caractère plus (`+`) dans le numéro de téléphone `+12125551212` est interdit dans les données encodées en URL et sera converti en `%2B125551212`.

!\[Corps Webhook\]\[29\]

## En-têtes et méthode de la requête

Twilio requiert deux en-têtes de requête, le type de contenu de la requête et un en-tête [HTTP Basic Authentication][32]. Ajoutez-les à votre webhook en cliquant sur l'icône d'engrenage sur le côté droit du compositeur de webhook, puis cliquez sur *Ajouter une nouvelle paire* deux fois.

| Nom de l'en-tête | Valeur de l'en-tête                                                                         |
| ---------------- | ------------------------------------------------------------------------------------------- |
| Type de contenu  | `application/x-www-form-urlencoded`                                                         |
| Autorisation     | `{% raw %}Basique {{ 'TWILIO_ACCOUNT_SID:TWILIO_AUTH_TOKEN' | base64_encode }}{% endraw %}` |

Assurez-vous de remplacer `TWILIO_ACCOUNT_SID` et `TWILIO_AUTH_TOKEN` par des valeurs de votre tableau de bord Twilio. Enfin, le point de terminaison API de Twilio attend une requête HTTP POST, alors choisissez cette option dans la liste déroulante pour la *méthode HTTP*.

!\[Méthode Webhook\]\[30\]

## Aperçu de votre demande

Utilisez le compositeur de webhook pour prévisualiser la demande pour un utilisateur aléatoire, ou pour un utilisateur ayant des identifiants particuliers, pour s'assurer que la requête est correctement rendue.

!\[Aperçu Webhook\]\[31\]
[28]: {% image_buster /assets/img_archive/Twilio_Console.png %} [29]: {% image_buster /assets/img_archive/Webhook_Body. ng %} [30]: {% image_buster /assets/img_archive/Webhook_Method.png %} [31]: {% image_buster /assets/img_archive/Webhook_Preview.png %}

[20]: https://www.twilio.com/docs/api/rest/sending-messages
[32]: https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side
