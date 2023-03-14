---
nav_title: Abandon des messages
article_title: Abandon des messages Liquid
page_order: 7
description: "Cet article de référence présente l’abandon des messages Liquid et quelques exemples de cas d’utilisation."

---

# Abandon des messages Liquid

Vous pouvez, de manière facultative, abandonner également des messages au sein de conditionnelles. Voici quelques exemples de la manière dont cette fonctionnalité peut être utilisée dans les campagnes marketing :

## Abandon du message si « Nombre de jeux assisté » = 0

Supposons par exemple que vous ne souhaitiez pas envoyer un message aux clients qui n’ont pas participé à un jeu :

{% raw %}
```liquid
{% if customer_attribute.${Number_Game_Attended} == 1 %}
Loved the game? Get 10% off your second one with code SAVE10.
{% elsif customer_attribute.${Number_Game Attended} > 1 %}
Love the games? Get 10% off your next one with code SAVE10.
{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

Ce message ne sera envoyé qu’aux clients connus pour avoir assisté à un match.

## Communiquer uniquement avec les clients anglophones

Vous pouvez envoyer des messages uniquement à des clients anglophones en créant une déclaration « si » qui correspondra à la langue du client en anglais et une déclaration « sinon » qui annulera le message pour toute personne qui ne parle pas anglais ou qui n’a pas de langue sur son profil.

{% raw %}
```liquid

{% if ${language} == 'en' %}
Send this message in English!
{% else %}
{% abort_message() %}
{% endif %}
```

Par défaut, Braze enregistre un message d’erreur générique sur votre journal dans la Developer Console :

```text
{% abort_message %} called
```

Vous pouvez également envoyer le journal des messages d’abandon à votre journal dans la Developer Console en incluant une chaîne de caractères à l’intérieur des parenthèses :

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

![Le journal des erreurs de message dans la Developer Console avec un message d’abandon de « langue était nulle ».][26]

[15]: {% image_buster /assets/img_archive/liquid_abort.png %}
[26]: {% image_buster /assets/img_archive/developer_console.png %}
[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[37]:#accounting-for-null-attribute-values
