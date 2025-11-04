---
nav_title: Intégrer des GIF
article_title: Intégrer des GIF dans les cartes de contenu
page_order: 5
description: "Découvrez comment intégrer des GIF dans les cartes de contenu à l'aide du SDK de Braze."
channel:
  - content cards
platform:
  - Android
  - Swift
  - Web
  - FireOS
---

# Intégrer des GIF dans les cartes de contenu

> Découvrez comment intégrer des GIF dans les cartes de contenu à l'aide du SDK de Braze.

{% alert note %}
Pour les SDK wrapper non répertoriés, utilisez plutôt la méthode native Android ou Swift correspondante. Gardez à l'esprit que les SDK Android et Swift Braze ne prennent pas en charge les GIF animés de manière native, vous mettrez donc en œuvre les GIF de la carte de contenu à l'aide d'outils tiers à la place.
{% endalert %}

{% sdktabs %}
{% sdktab android %}
{% multi_lang_include developer_guide/android/_global/gifs.md %}
{% endsdktab %}

{% sdktab swift %}
{% multi_lang_include developer_guide/swift/gifs.md %}
{% endsdktab %}

{% sdktab web %}
Pour l'instant, les cartes de contenu GIF ne sont pas prises en charge par le SDK de Braze.
{% endsdktab %}
{% endsdktabs %}
