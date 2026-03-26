---
nav_title: Abandonner des messages
article_title: Interrompre les messages liquides
page_order: 7
description: "Cet article de référence présente l’abandon des messages Liquid et quelques exemples de cas d’utilisation."

---

# Messages d'interruption

> En option, vous pouvez utiliser l'étiquette Liquid message `abort_message("optional reason for aborting")` dans les conditionnels pour empêcher l'envoi d'un message à un utilisateur. Cet article de référence répertorie quelques exemples de la manière dont cette fonctionnalité peut être utilisée dans les campagnes marketing.

{% alert note %}
Si une étape du message est annulée dans un canvas, l'utilisateur **ne quitte pas** le canvas et **passe** à l’étape suivante.
{% endalert %}

## Abandon du message si « Nombre de jeux assisté » = 0

Supposons par exemple que vous ne souhaitiez pas envoyer un message aux clients qui n’ont pas participé à un jeu :

{% raw %}
```liquid
{% if custom_attribute.${Number_Game_Attended} == 1 %}
Loved the game? Get 10% off your second one with code SAVE10.
{% elsif custom_attribute.${Number_Game Attended} > 1 %}
Love the games? Get 10% off your next one with code SAVE10.
{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

Ce message ne sera envoyé qu’aux clients connus pour avoir assisté à un match.

## Communiquer uniquement avec les clients anglophones

Vous pouvez envoyer des messages à des clients anglophones uniquement en créant une instruction "if" qui correspondra lorsque la langue du client est l'anglais et une instruction "else" qui annulera le message pour toute personne qui ne parle pas anglais ou qui n'a pas de langue dans son profil.

{% raw %}
```liquid

{% if ${language} == 'en' %}
Send this message in English!
{% else %}
{% abort_message() %}
{% endif %}
```

Par défaut, Braze enregistre un message d'erreur générique dans votre journal d'activité des messages :

```text
{% abort_message %} called
```

Vous pouvez également faire en sorte que le message d'abandon enregistre quelque chose dans votre journal d'activité des messages en incluant une chaîne de caractères entre les parenthèses :

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

![Le journal des erreurs de message dans la console de développement avec un message d’abandon de « langue était nulle ».]({% image_buster /assets/img_archive/developer_console.png %})

## Requête pour les messages d'interruption

Vous pouvez utiliser [le générateur de requêtes]({{site.baseurl}}/user_guide/analytics/query_builder/) ou votre propre entrepôt de données, s'il est connecté à Braze, pour rechercher des messages d'interruption spécifiques qui sont déclenchés lorsque la logique Liquid provoque l'interruption d'un message.

## Lorsque la logique d'interruption est évaluée

Le moment choisi pour l'évaluation de la logique d'interruption dépend du canal de communication.

### Push, e-mail, SMS, webhook et cartes de contenu

La logique d'interruption est évaluée au moment de l'envoi, lorsque Braze traite le message en vue de sa réception/distribution.

### in-app Messages

La logique d'interruption est évaluée au moment où le message in-app est déclenché (par exemple, lorsque l'utilisateur effectue l'événement déclencheur ou démarre une session), et non lorsque le message est initialement envoyé à l'appareil. Les messages in-app sont transmis au SDK au début de la session et mis en cache localement ; le Liquid, y compris les`abort_message()`appels éventuels, est exécuté lorsque le déclencheur est rempli.

## Considérations

L'étiquette Liquid `abort_message()` empêche l'envoi de messages aux utilisateurs, ce qui signifie que le message ne s'affichera pas sur le profil des utilisateurs et ne sera pas pris en compte dans les envois ou la limite de fréquence.
