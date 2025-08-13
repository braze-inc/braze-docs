---
nav_title: Locales dans les messages
article_title: Locales dans les messages
page_order: 9
description: "Cet article fournit des étapes sur la façon d'utiliser les locales dans vos notifications push."
---

# Locales dans les messages

> Après avoir ajouté des locales à votre espace de travail, vous pouvez cibler des utilisateurs dans différentes langues au sein d'une seule et même notification push.

{% multi_lang_include locales.md section="Conditions préalables" %}

{% alert important %}
La prise en charge du multilinguisme et des langues locales dans les messages est actuellement en phase d'accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé.
{% endalert %}

## Utilisation des paramètres régionaux

Pour utiliser les lieux dans vos messages, composez une campagne push ou un canvas, puis procédez comme suit :

1. Ajoutez les tags de traduction {% raw %}`{% translation %}` et `{% endtranslation %}`{% endraw %} autour de tous les textes et images ou liens URL à traduire.

![Compositeur de notifications push avec des étiquettes de traduction ajoutées aux champs du titre et du message.]({% image_buster /assets/img/multi-language_support/push_translation_tags.png %})

{: start="2"}
2\. Enregistrez votre message en tant que brouillon.
3\. Sélectionnez **Gérer la langue** et ajoutez vos localisations pour le message à l'aide du menu déroulant.
4\. Sélectionnez **Télécharger le modèle**, puis remplissez les traductions dans le modèle CSV.

![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})

{: start="5"}
5\. Pour télécharger le modèle CSV complété, sélectionnez **Télécharger les traductions**. 

![La fenêtre "Messages multilingues" avec deux langues sélectionnées et des boutons pour télécharger un modèle ou des traductions.]({% image_buster /assets/img/multi-language_support/upload_translation.png %})

Toute modification des ID ou des lieux dans le fichier CSV ne sera pas automatiquement mise à jour dans votre message. Pour mettre à jour les traductions, mettez à jour le fichier CSV et téléchargez à nouveau le fichier.

{% alert tip %}
Consultez notre [API de traduction]({{site.baseurl}}/api/endpoints/translations) pour gérer et mettre à jour les traductions dans vos campagnes et canvas.
{% endalert %}

{% multi_lang_include locales.md section="Aperçu" %}

{% multi_lang_include locales.md section="Questions fréquemment posées" %}
