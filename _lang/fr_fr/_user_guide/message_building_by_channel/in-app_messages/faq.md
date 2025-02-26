---
nav_title: FAQ
article_title: FAQ sur les messages in-app
page_order: 19
description: "Le présent article fournit des réponses aux questions fréquemment posées sur les messages in-app."
tool: in-app messages

---

# Foire aux questions

> Le présent article fournit des réponses à des questions fréquemment posées sur les messages in-app.

### Qu’est-ce qu’un message intégré au navigateur et en quoi diffère-t-il d’un message in-app ?

Les messages intégrés au navigateur sont des messages in-app envoyés à des navigateurs Web. Pour créer un message dans le navigateur, assurez-vous de sélectionner **Navigateur Web** dans le champ **Envoyer à** lors de la création de votre campagne de message intégré ou de Canvas. 

### Un message in-app s’affiche-t-il si un appareil est hors ligne ?

Tout dépend. Comme les messages in-app sont livrés au démarrage de session, l’appareil est capable de télécharger la charge utile avant de passer hors ligne et d’afficher ces messages hors ligne. Si la charge utile n’est pas téléchargée, les messages in-app ne s’affichent pas.

### Si un utilisateur possède déjà une charge utile un message in-app sur son appareil et que l’expiration du message est modifiée, l’expiration est-elle mise à jour sur son appareil ?

Lorsqu’un utilisateur commence une session, Braze vérifie en cas de modifications apportées si les messages in-app sont éligibles et les actualise en conséquence. Ainsi, si l’expiration a changé et que l’utilisateur ouvre une session, le message in-app est envoyé à l’appareil avec les informations mises à jour.

### Comment configurer les heures calmes pour une campagne de messages in-app ?

La fonctionnalité Heures calmes n’est pas disponible pour mes campagnes de messages in-app. Cette fonctionnalité permet d’empêcher l’envoi des messages à vos utilisateurs à des heures spécifiques. Pour les campagnes de messages in-app, vos utilisateurs reçoivent uniquement les messages in-app actifs dans l’application. 

En tant que solution de contournement pour envoyer des messages in-app à une heure spécifique, utilisez le code exemple suivant de Liquid. Ceci permet d'annuler le message si le message in-app est affiché après 19 h 59 ou avant 8 h 00 dans le fuseau horaire spécifié.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 19 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}
MESSAGE HERE
```
{% endraw %}

### Quand l’éligibilité d’un message in-app est-elle calculée ?

L’éligibilité d’un message in-app est calculée au moment de la livraison. Si un message in-app est programmé pour un envoi à 7 h, son éligibilité est vérifiée à 7 h.

Une fois un message in-app affiché, son éligibilité dépend du moment auquel il est téléchargé et déclenché.

### Qu'est-ce que les messages intégrés dans l'application modélisés ?

Les messages intégrés à l'application seront livrés sous forme de messages intégrés à l'application modélisés lorsque **Réévaluer l'éligibilité de la campagne avant l'affichage** est sélectionné ou si l'un des tags Liquid suivants existe dans le message :

- `canvas_entry_properties`
- `connected_content`
- Les variables SMS telles que {% raw %}`{sms.${*}}`{% endraw %}
- `catalog_items`
- `catalog_selection_items`
- `event_properties`

Cela signifie qu'au début de la session, l'appareil recevra le déclencheur de ce message intégré plutôt que le message entier. Lorsque l'utilisateur déclenche le message intégré à l'application, l'appareil de l'utilisateur effectuera une demande réseau pour récupérer le message réel.

{% alert note %}
Le message ne sera pas livré si l'appareil n'a pas accès à Internet. Le message pourrait ne pas être livré si la logique Liquid prend trop de temps à se résoudre.
{% endalert %}

### Pourquoi ma campagne de messages in-app archivée envoie-t-elle toujours des impressions de messages in-app ?

Ce cas peut se produire pour les utilisateurs qui répondaient aux critères du segment lorsque la campagne de messages in-app était active.

Pour éviter cela, lors de la configuration de votre campagne, sélectionnez **Réévaluer l'éligibilité de la campagne avant l'affichage**. 

### Comment Braze calcule-t-il une expiration de message in-app définie à « après 1 jour(s) » ?

Braze calcule une heure d’expiration d’un jour comme 24 heures après l’éligibilité des utilisateurs à recevoir un message.