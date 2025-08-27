---
nav_title: Partenariat Twilio
alias: /partners/twilio/

description: "Cet article présente le partenariat entre Braze et Twilio."
page_type: update
channel: 
  - SMS
  - Webhook
---

# Twilio

{% alert warning %}
Notez que le support pour l’intégration du Webhook Twilio sera interrompu le 31 janvier 2020. Si vous souhaitez continuer à accéder aux services SMS avec Braze, consultez notre [documentation sur les SMS.]({{site.baseurl}}/user_guide/message_building_by_channel/sms/)
{% endalert %}

Pour cet exemple, nous allons configurer le canal webhook Braze pour envoyer des SMS et des MMS à vos utilisateurs, via [l'API d'envoi de messages](https://www.twilio.com/docs/api/rest/sending-messages) de Twilio. Un modèle de webhook Twilio est inclus sur le tableau de bord.

## URL HTTP

L’URL du webhook est fournie par Twilio dans votre tableau de bord. Cette URL est spécifique à votre compte Twilio car elle contient votre ID de compte Twilio (`TWILIO_ACCOUNT_SID`).

Dans notre Twilio, l’URL du webhook Twilio est `https://api.twilio.com/2010-04-01/Accounts/TWILIO_ACCOUNT_SID/Messages.json`. Vous trouverez cette URL dans la section *Mise en route de* la console Twilio.

![Twilio_Console]({% image_buster /assets/img_archive/Twilio_Console.png %})

## Corps de la demande

L’API Twilio s’attend à ce que le corps de la requête soit dans une chaîne URL encodée, donc nous devons commencer en changeant le type de demande du compositeur de webhook de Braze à `Raw Text`. Les paramètres requis pour le corps de la demande sont *To*, *From* et *Body*.

La capture d’écran suivante illustre l’aspect de votre requête si vous envoyez un SMS au numéro de téléphone de chaque utilisateur, avec dans le corps du message « Bonjour de Braze ! ».

- Vous devez avoir des numéros de téléphone valides pour chaque profil utilisateur de votre audience cible.
- Pour répondre au format de requête Twilio, utilisez le filtre Liquid `url_param_escape` sur le contenu de votre message. Ce filtre encode une chaîne pour que tous les caractères soient autorisés dans une demande HTML ; par exemple, le caractère plus (`+`) dans le numéro de téléphone `+12125551212` est interdit dans les données encodées dans l’URL et sera converti en `%2B12125551212`.

![Corps du webhook]({% image_buster /assets/img_archive/Webhook_Body.png %})

## En-têtes et méthode de requête

Twilio a besoin de deux en-têtes de requête, le Content-Type de la requête et un en-tête [HTTP Basic Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side). Ajoutez-les à votre webhook en cliquant sur l'icône d'engrenage à côté du compositeur du webhook, puis en cliquant deux fois sur *Ajouter une nouvelle paire.*

Nom d’en-tête | Valeur de l’en-tête
--- | ---
Type de contenu | `application/x-www-form-urlencoded`
Autorisation | `{% raw %}Basic {{ 'TWILIO_ACCOUNT_SID:TWILIO_AUTH_TOKEN' | base64_encode }}{% endraw %}`

Assurez-vous de remplacer `TWILIO_ACCOUNT_SID` et `TWILIO_AUTH_TOKEN` avec les valeurs de votre tableau de bord Twilio. Enfin, l'endpoint de l'API de Twilio attend une requête HTTP POST, choisissez donc cette option dans le menu déroulant de la *méthode HTTP.*

![Méthode webhook]({% image_buster /assets/img_archive/Webhook_Method.png %})

## Prévisualiser votre requête

Utilisez le compositeur de webhook pour prévisualiser la demande d’un utilisateur aléatoire, ou pour un utilisateur avec des identifiants particuliers, pour vous assurer que la demande est correctement exécutée.

![Aperçu du webhook]({% image_buster /assets/img_archive/Webhook_Preview.png %})

