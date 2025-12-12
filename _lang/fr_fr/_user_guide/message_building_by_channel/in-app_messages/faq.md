---
nav_title: FAQ
article_title: FAQ sur les messages in-app
page_order: 19
description: "Cet article apporte des réponses aux questions fréquemment posées sur les messages in-app."
tool: in-app messages

---

# Questions fréquemment posées

> Cet article apporte des réponses à certaines questions fréquemment posées sur les messages in-app.

### Qu'est-ce qu'un message dans le navigateur et en quoi diffère-t-il d'un message in-app ?

Les messages dans-app sont des messages in-app envoyés aux navigateurs web. Pour créer un message in-app, veillez à sélectionner **Navigateur Web** dans le champ **Envoyer à** lorsque vous créez votre campagne de messages in-app ou Canvas. 

### Un message in-app s'affichera-t-il si un appareil est hors ligne ?

Cela dépend. Comme les messages in-app sont envoyés au début de la session, l'appareil est en mesure de télécharger la charge utile avant de se déconnecter, le message in-app peut toujours être affiché pendant la déconnexion. Si la charge utile n'est pas téléchargée, le message in-app ne s'affichera pas.

### Si un utilisateur a déjà un envoi de messages in-app sur son appareil et que l'expiration du message est modifiée, l'expiration sera-t-elle mise à jour sur son appareil ?

Lorsqu'un utilisateur démarre une session, Braze vérifie si des modifications ont été apportées aux messages in-app auxquels il a droit et les met à jour en conséquence. Ainsi, si l'expiration a changé et qu'ils enregistrent une session, le message in-app est envoyé à l'appareil avec les informations mises à jour.

### Comment mettre en place des heures calmes pour une campagne d'envoi de messages in-app ?

La fonctionnalité Heures calmes n'est pas disponible pour les campagnes de messages in-app. Cette fonctionnalité permet d'empêcher l'envoi de messages à vos utilisateurs pendant certaines heures. Pour les campagnes de messages in-app, vos utilisateurs ne recevront des messages in-app que s'ils sont actifs dans l'application. 

Comme solution de contournement pour envoyer des messages in-app à une heure précise, utilisez l'exemple de code Liquid suivant. Cela permet d'interrompre l'envoi du message si le message in-app est affiché après 19h59 ou avant 8h dans le fuseau horaire spécifié.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 19 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}
MESSAGE HERE
```
{% endraw %}

### Quand l'éligibilité à un message in-app est-elle calculée ?

L'éligibilité à un message in-app est calculée au moment de la réception/distribution. Si l'envoi d'un message in-app est planifié à 7 heures, l'éligibilité est vérifiée pour ce message in-app à 7 heures.

Une fois le message in-app affiché, l'éligibilité dépendra du moment où le message in-app est téléchargé et déclenché.

### Qu'est-ce qu'un message in-app ?

Les messages in-app seront envoyés sous forme de messages in-app modélisés lorsque l'option **Réévaluer l'éligibilité de la campagne avant l'affichage** est sélectionnée ou si l'une des étiquettes Liquid suivantes est présente dans le message :

- `canvas_entry_properties`
- `connected_content`
- Les variables du SMS telles que {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Cela signifie que lors du démarrage de la session, l'appareil recevra le déclencheur de ce message in-app au lieu de l'intégralité du message. Lorsque l'utilisateur déclenche le message in-app, l'appareil de l'utilisateur fait une demande de réseau pour récupérer le message réel.

{% alert note %}
Le message ne sera pas envoyé si l'appareil n'a pas accès à l'internet. Le message risque de ne pas être délivré si la logique du liquide prend trop de temps à se mettre en place.
{% endalert %}

### Pourquoi ma campagne de messages in-app archivée continue-t-elle d'envoyer des messages in-app ?

Cela peut se produire pour les utilisateurs qui répondaient aux critères de segmentation lorsque la campagne de messages in-app était active.

Pour éviter cela, lors de la configuration de votre campagne, sélectionnez **Réévaluer l'éligibilité de la campagne avant de l'afficher**. 

### Comment Braze calcule-t-il l'expiration d'un message in-app réglé sur "après 1 jour(s)" ?

Braze calcule un délai d'expiration d'un jour comme étant 24 heures après que les utilisateurs sont éligibles pour recevoir un message.