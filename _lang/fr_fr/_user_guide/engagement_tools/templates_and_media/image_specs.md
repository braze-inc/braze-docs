---
nav_title: "Spécifications de l'image"
article_title: "Spécifications de l'image"
page_order: 4.1

page_type: reference
description: "Cet article de référence décrit les tailles d'image et les spécifications recommandées pour chaque type de canal."
tool:
  - Templates
  - Media

---

# Spécifications de l'image

> En général, les images de petite taille et de haute qualité se chargent plus rapidement. Nous vous recommandons donc d'utiliser la ressource la plus petite possible pour obtenir le résultat souhaité. Pour maximiser l'utilisation de votre image dans des canaux spécifiques, reportez-vous aux détails de cet article.

Vous devriez toujours [prévisualiser et tester vos messages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) sur une variété d'appareils pour confirmer que les zones les plus importantes de votre image et de votre message apparaissent comme prévu.

{% alert tip %} Créez des ressources en toute confiance ! Nos modèles d'images de messages in-app et nos superpositions de zones de sécurité sont conçus pour s'adapter aux appareils de toutes tailles. [Téléchargez les modèles de conception ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}). {% endalert %}

{% multi_lang_include image_specs.md variable_name='payload size' %}

## Messages in-app

{% multi_lang_include image_specs.md variable_name='in-app messages' %}

### Font Awesome

Braze prend en charge l'utilisation de [Font Awesome v4.3.0](https://fontawesome.com/v4.7.0/cheatsheet/) pour les icônes des messages modaux in-app.

## Notifications push

{% multi_lang_include image_specs.md variable_name='push notifications' %}

## e-mail

{% multi_lang_include image_specs.md variable_name='email' %}

## Comportement de l'image

{% multi_lang_include image_specs.md variable_name='image behavior' %}
