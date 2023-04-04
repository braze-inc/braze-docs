---
nav_title: FAQ
article_title: FAQ sur les messages In-App
page_order: 19
description: "Le présent article fournit des réponses aux questions fréquemment posées sur les messages In-App."
tool: in-app messages

---

# FAQ sur les messages In-App

> Le présent article fournit des réponses à des questions fréquemment posées sur les messages In-App.

### Qu’est-ce qu’un message dans le navigateur et en quoi diffère-t-il d’un message In-App ?
Les messages dans le navigateur sont des messages In-App envoyés à des navigateurs Web. Pour créer un message dans le navigateur, assurez-vous de sélectionner **Web Browser** (Navigateur Web) sous le champ **Send To** (Envoyer à) lors de la création de votre campagne de messages In-App ou Canvas. 

### Un message In-App s’affiche-t-il si un appareil est hors ligne ?

Tout dépend. Comme les messages In-App sont livrés au démarrage de session, l’appareil est capable de télécharger la charge utile avant de passer hors ligne et d’afficher ces messages hors ligne. Si la charge utile n’est pas téléchargée, les messages In-App ne s’affichent pas.

### Si un utilisateur possède déjà une charge utile un message In-App sur son appareil et que l’expiration du message est modifiée, l’expiration est-elle mise à jour sur son appareil ?

Lorsqu’un utilisateur commence une session, Braze vérifie en cas de modifications apportées si les messages In-App sont éligibles et les actualise en conséquence. Ainsi, si l’expiration a changé et que l’utilisateur ouvre une session, le message In-App est envoyé à l’appareil avec les informations mises à jour.

### Comment configurer les heures calmes pour une campagne de messages In-App ?

La fonctionnalité Heures calmes n’est pas disponible pour mes campagnes de messages In-App. Cette fonctionnalité permet d’empêcher l’envoi des messages à vos utilisateurs à des heures spécifiques. Pour les campagnes de messages In-App, vos utilisateurs reçoivent uniquement les messages In-App actifs dans l’application. 

En tant que solution de contournement pour envoyer des messages In-App à une heure spécifique, utilisez le code exemple suivant de Liquid. Le message In-App peut ainsi être annulé s’il s’affiche après 19 h 59 ou avant 8 h dans le fuseau horaire indiqué.

{% raw %}
```liquid
{% assign time = 'now' | time_zone: ${time_zone} %}{% assign hour = time | date: '%H' | plus: 0 %}
{% if hour > 19 or hour < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}
MESSAGE HERE
```
{% endraw %}

### Quand l’éligibilité d’un message In-App est-elle calculée ?

L’éligibilité d’un message In-App est calculée au moment de la livraison. Si un message In-App est programmé pour un envoi à 7 h, son éligibilité est vérifiée à 7 h.

Une fois un message In-App affiché, son éligibilité dépend du moment auquel il est téléchargé et déclenché.

### Pourquoi ma campagne de messages In-App archivée envoie-t-elle toujours des impressions de messages In-App ?

Ce cas peut se produire pour les utilisateurs qui répondaient aux critères du segment lorsque la campagne de messages In-App était active.

Pour éviter cela, pendant la configuration de votre campagne, sélectionnez **Re-evaluate campaign eligibility before displaying** (Réévaluer l’éligibilité de la campagne avant d’afficher). 

### Comment Braze calcule-t-il une expiration de message In-App définie à « après 1 jour(s) » ?

Braze calcule une heure d’expiration d’un jour comme 24 heures après l’éligibilité des utilisateurs à recevoir un message.