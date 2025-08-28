---
nav_title: Abandon des messages
article_title: Abandon des messages Liquid
page_order: 7
description: "Cet article de référence présente l’abandon des messages Liquid et quelques exemples de cas d’utilisation."

---

# Abandonner des messages

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

![Message d'erreur dans la console de développement avec un message d'abandon "language was nil".]({% image_buster /assets/img_archive/developer_console.png %})

## Demande d'envoi de messages d'annulation

Vous pouvez utiliser [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) ou votre propre entrepôt de données, s'il est connecté à Braze, pour rechercher des messages d'abandon spécifiques qui sont déclenchés lorsque la logique Liquid entraîne l'abandon d'un message.

## Considérations

L'étiquette Liquid `abort_message()` empêche l'envoi de messages aux utilisateurs, ce qui signifie que le message ne s'affichera pas sur le profil des utilisateurs et ne sera pas pris en compte dans les envois ou la limite de fréquence.
