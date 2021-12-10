---
nav_title: Foire aux questions
article_title: Foire aux questions sur les messages dans l'application
page_order: 19
description: "Cet article fournit des réponses aux questions fréquemment posées sur les messages In-App."
tool: messages intégrés à l'application
---

# Foire aux questions sur les messages dans l'application

> Cet article fournit des réponses à certaines questions fréquemment posées sur les messages dans l'application.

### Qu'est-ce qu'un message dans le navigateur et en quoi cela diffère-t-il d'un message dans l'application ?
Les messages dans le navigateur sont des messages dans l'application envoyés aux navigateurs Web. Créer un message dans le navigateur assurez-vous de sélectionner __Web Browser__ dans le champ __Envoyer à__ lors de la création de votre campagne de message ou de Canvas.

### Un message dans l'application s'affichera-t-il si un appareil est hors ligne ?

Cela dépend. Comme les messages intégrés sont envoyés au démarrage de la session, l'appareil est en mesure de télécharger la charge utile avant de se déconnecter, le message dans l'application peut toujours être affiché en mode hors connexion. Si la charge utile n'est pas téléchargée, le message dans l'application ne s'affichera pas.

### Si un utilisateur a déjà une charge utile de message dans l'application sur son appareil et que le message d'expiration est modifié, l'expiration sera-t-elle mise à jour sur leur appareil?

Lorsqu'un utilisateur démarre une session, Braze vérifie si des modifications ont été apportées aux messages dans l'application pour lesquels ils sont éligibles et les met à jour en conséquence. Donc, si l'expiration a changé et qu'ils enregistrent une session, alors le message dans l'application est envoyé à l'appareil avec les informations mises à jour.

### Comment puis-je configurer des heures silencieuses pour une campagne de message in-app ?

La fonction Heures silencieuses n'est pas disponible pour les campagnes de messages dans l'application. Cette fonction est utilisée pour empêcher l'envoi de messages à vos utilisateurs pendant des heures précises. Pour les campagnes de messages intégrés à l'application, vos utilisateurs ne recevront des messages dans l'application que s'ils sont actifs dans l'application.

En guise de contournement pour envoyer des messages dans l'application pendant une période spécifique, utilisez l'exemple suivant de code Liquid. Cela permet d'annuler le message si le message est affiché dans l'application après 19h59 heures ou avant 8h au fuseau horaire spécifié.

{% raw %}
```liquid
{% assigner heure = 'maintenant' | fuseau horaire : ${time_zone} %}{% assigner heure = heure | date: '%H' | plus: 0 %}
{% si heure > 19 ou heure < 8 %}
{% abort_message("Outside allowed time window") %}
{% endif %}
MESSAGE ICI
```
{% endraw %}

### Quand l'éligibilité à un message dans l'application est-elle calculée ?

L'éligibilité pour un message intégré est calculée au moment de la livraison. Si un message intégré est programmé pour être envoyé à 7 heures du matin, alors l'éligibilité est vérifiée pour ce message dans l'application à 7 heures.

Une fois que le message intégré sera affiché, l'éligibilité dépendra du moment où le message sera téléchargé et déclenché dans l'application.

### Pourquoi ma campagne de message in-app archivée donne-t-elle toujours des impressions de messages dans l'application ?

Cela peut se produire pour les utilisateurs qui remplissaient les critères de segment lorsque la campagne de message dans l'application était active.

Pour éviter cela, lors de la configuration de votre campagne, sélectionnez **Ré-évaluer l'éligibilité de la campagne avant d'afficher**.

### Comment Braze calcule-t-il une expiration de message dans l'application définie à "après 1 jour(s)"?

Braze calcule la durée d'expiration d'un jour comme 24 heures après que les utilisateurs aient droit à recevoir un message.