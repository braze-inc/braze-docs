---
nav_title: Abandon des messages
article_title: Abandon des messages Liquid
page_order: 7
description: "Les messages peuvent maintenant être abandonnés dans les instructions conditionnelles. Dans cet article de référence, nous listons quelques exemples de cas d'utilisation de cette fonctionnalité."
---

# Abandon des messages Liquid

Optionnellement, vous pouvez également annuler les messages dans les conditions. Voici quelques exemples de la façon dont cette fonctionnalité peut être utilisée dans les campagnes de marketing:

**Abandon du message si "Nombre de parties participantes" = 0:**

Par exemple, disons que vous ne vouliez pas envoyer le message ci-dessus aux clients qui n'avaient pas assisté à un jeu:

!\[Exemple de Message d'Abort Liquid\]\[15\]

Ce message ne sera envoyé qu'aux clients qui sont connus pour avoir participé à un jeu.

**Messagerie de clients anglophones uniquement :**

Vous pouvez envoyer un message aux clients anglophones uniquement en créant une déclaration "si" qui correspondra quand la langue d'un client est l'anglais et une autre déclaration qui annulera le message pour toute personne qui ne parle pas l'anglais ou qui n'a pas de langue sur son profil.

{% raw %}
```liquid

{% if ${language} == 'fr' %}
Envoyez ce message en anglais !
{% else %}
{% abort_message() %}
{% endif %}
```

Par défaut, Braze va enregistrer un message d'erreur générique dans votre journal de votre Console Développeur:

```text
{% abort_message %} appelée
```

Vous pouvez également enregistrer quelque chose dans le journal de votre console de développement en incluant une chaîne entre parenthèses :

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

!\[developer_console\]\[26\]
[15]: {% image_buster /assets/img_archive/liquid_abort.png %} [26]: {% image_buster /assets/img_archive/developer_console.png %} [34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
