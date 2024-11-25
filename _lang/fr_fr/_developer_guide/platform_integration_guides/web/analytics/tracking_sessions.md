---
nav_title: Suivre des sessions
article_title: Suivre des sessions pour le Web
platform: Web
page_order: 0
description: "Cet article de référence explique comment suivre les sessions pour le Web."

---

# Suivre des sessions

> Le SDK Braze rapporte les données de session utilisées par le tableau de bord de Braze pour calculer l’engagement des utilisateurs et d’autres analyses essentielles à une meilleure connaissance de vos utilisateurs. Sur la base de la sémantique de session suivante, notre SDK génère des points de données « démarrage de la session » et « fin de la session » qui comptent pour la longueur de session et le nombre de sessions visibles dans le tableau de bord de Braze.

## Cycle de vie de la session

Par défaut, les sessions débutent lorsque `braze.openSession()` est appelé pour la première fois et restent ouvertes jusqu’à ce qu’il y ait eu au moins 30 minutes d’inactivité. Cela signifie que si l’utilisateur quitte le site et y retourne moins de 30 minutes plus tard, la même session continuera. S’ils reviennent après que les 30 minutes ont expiré, un point de données de « fermeture de session » est automatiquement généré pour le temps passé ailleurs et une nouvelle session s’ouvre.

{% alert note %}
Si vous devez forcer une nouvelle session, vous pouvez le faire en changeant d’utilisateur.
{% endalert %}

## Personnaliser la libération sur temporisation de session

Pour personnaliser le délai d'attente de la session, ajoutez l'option `sessionTimeoutInSeconds` à votre fonction [`initialize`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) à votre fonction La valeur minimale pour `sessionTimeoutInSeconds` est de 1 seconde.

```js
// Sets the session timeout to 15 minutes instead of the default 30
braze.initialize('YOUR-API-KEY-HERE', { sessionTimeoutInSeconds: 900 });
``` 

Si vous avez défini un délai de libération sur temporisation de session, les sémantiques de session s’étendent à toute cette temporisation personnalisée.

## Tester le suivi de session

Pour détecter les sessions via votre utilisateur, trouvez votre utilisateur sur le tableau de bord et accédez à **Utilisation de l'application** sur le profil de l'utilisateur. Vous pouvez confirmer que le suivi de session fonctionne en vérifiant que la métrique de session augmente lorsque vous vous y attendez.

![Un profil utilisateur indiquant le nombre de sessions, la date de la première et de la dernière utilisation de l'application.]({% image_buster /assets/img_archive/test_session.png %}){: style="max-width:50%"}

