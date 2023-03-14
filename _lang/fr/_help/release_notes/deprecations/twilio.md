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
Notez que le support pour l’intégration du Webhook Twilio sera interrompu le 31 janvier 2020. Si vous souhaitez toujours accéder aux services SMS avec Braze, consultez notre [Documentation SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/). 
{% endalert %}

Dans cet exemple, nous allons configurer le canal webhook Braze pour envoyer des SMS et MMS à vos utilisateurs via [l’API d’envoi de messages de Twilio][20]. Un modèle de webhook Twilio est inclus sur le tableau de bord.

## URL HTTP

L’URL du webhook est fournie par Twilio dans votre tableau de bord. Cette URL est spécifique à votre compte Twilio car elle contient votre ID de compte Twilio (`TWILIO_ACCOUNT_SID`).

Dans notre Twilio, l’URL du webhook Twilio est `https://api.twilio.com/2010-04-01/Accounts/TWILIO_ACCOUNT_SID/Messages.json`. Vous pouvez trouver cette URL dans la section *Getting Started* (Démarrage) de la console Twilio.

![Twilio_Console][28]

## Corps de la demande

L’API Twilio s’attend à ce que le corps de la requête soit dans une chaîne URL encodée, donc nous devons commencer en changeant le type de demande du compositeur de webhook de Braze à `Texte brut`. Les paramètres requis pour le corps de la demande sont *À*, *De* et *Corps*.

La capture d’écran suivante illustre l’aspect de votre requête si vous envoyez un SMS au numéro de téléphone de chaque utilisateur, avec dans le corps du message « Bonjour de Braze ! ».

- Vous devez avoir des numéros de téléphone valides pour chaque profil utilisateur de votre audience cible.
- Pour répondre au format de requête Twilio, utilisez le filtre Liquid `url_param_escape` sur le contenu de votre message. Ce filtre encode une chaîne pour que tous les caractères soient autorisés dans une demande HTML ; par exemple, le caractère plus (`+`) dans le numéro de téléphone `+12125551212` est interdit dans les données encodées dans l’URL et sera converti en `%2B12125551212`.

![Corps du webhook][29]

## En-têtes et méthode de requête

Twilio exige deux en-têtes de requête, le type de contenu de requête et un en-tête d’[Authentification HTTP][32]. Ajoutez-les à votre webhook en cliquant sur l’icône d’engrenage située à côté du compositeur de webhook, puis cliquez deux fois sur *Ajouter une nouvelle paire*.

Nom d’en-tête | Valeur de l’en-tête
--- | ---
Type de contenu | `application/x-www-form-urlencoded`
Autorisation | `{% raw %}Basic {{ 'TWILIO_ACCOUNT_SID:TWILIO_AUTH_TOKEN' | base64_encode }}{% endraw %}`

Assurez-vous de remplacer `TWILIO_ACCOUNT_SID` et `TWILIO_AUTH_TOKEN` avec les valeurs de votre tableau de bord Twilio. Enfin, l’endpoint d’API Twilio attend une requête HTTP POST, alors choisissez cette option dans la liste déroulante pour la *Méthode HTTP*.

![Méthode du webhook][30]

## Prévisualiser votre requête

Utilisez le compositeur de webhook pour prévisualiser la demande d’un utilisateur aléatoire, ou pour un utilisateur avec des identifiants particuliers, pour vous assurer que la demande est correctement exécutée.

![Prévisualisation dans le Webhook][31]

[20]: https://www.twilio.com/docs/api/rest/sending-messages
[28]: {% image_buster /assets/img_archive/Twilio_Console.png %}
[29]: {% image_buster /assets/img_archive/Webhook_Body.png %}
[30]: {% image_buster /assets/img_archive/Webhook_Method.png %}
[31]: {% image_buster /assets/img_archive/Webhook_Preview.png %}
[32]: https://en.wikipedia.org/wiki/Basic_access_authentication#Client_side
