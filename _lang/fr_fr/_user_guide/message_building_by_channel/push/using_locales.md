---
nav_title: Locales dans les messages
article_title: Locales dans les messages
page_order: 9
description: "Cet article fournit des étapes sur la façon d'utiliser les locales dans vos notifications push."
---

# Locales dans les messages

> Après avoir ajouté des locales à votre espace de travail, vous pouvez cibler des utilisateurs dans différentes langues au sein d'une seule et même notification push.

## Conditions préalables

Pour modifier et gérer la [prise en charge multilingue]({{site.baseurl}}/multi_language_support/), vous devez disposer de l’autorisation « Gérer les paramètres multilingues ». Pour ajouter le paramètre régional à un message, vous devez disposer des autorisations nécessaires pour modifier les campagnes.

## Utilisation des paramètres régionaux

Pour utiliser les lieux dans vos messages, composez une campagne push ou un canvas, puis procédez comme suit :

1. Ajoutez les tags de traduction {% raw %}`{% translation %}` et `{% endtranslation %}`{% endraw %} autour de tous les textes et images ou liens URL à traduire.<br><br>![Compositeur de notifications push avec des étiquettes de traduction ajoutées aux champs du titre et du message.]({% image_buster /assets/img/multi-language_support/push_translation_tags.png %})<br><br>
2. Enregistrez votre message en tant que brouillon.
3. Sélectionnez **Gérer la langue** et ajoutez vos localisations pour le message à l'aide du menu déroulant.
4. Sélectionnez **Télécharger le modèle**, puis remplissez les traductions dans le modèle CSV. <br><br>![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})<br><br>
5. Pour télécharger le modèle CSV complété, sélectionnez **Télécharger les traductions**. <br><br>![La fenêtre "Messages multilingues" avec deux langues sélectionnées et des boutons pour télécharger un modèle ou des traductions.]({% image_buster /assets/img/multi-language_support/upload_translation.png %})

Pour mettre à jour les traductions, actualisez le fichier CSV et chargez-le à nouveau. Cela signifie que toute modification des ID ou des lieux dans le CSV ne sera pas automatiquement mise à jour dans votre message.

{% alert tip %}
Consultez notre [API de traduction]({{site.baseurl}}/api/endpoints/translations) pour gérer et mettre à jour les traductions dans vos campagnes et canvas.
{% endalert %}

## Prévisualiser vos paramètres régionaux

Dans la liste déroulante **Prévisualiser le message en tant qu'utilisateur** de l'onglet **Test**, sélectionnez **Utilisateur personnalisé** et entrez différentes langues pour prévisualiser le message afin de vérifier si votre message se traduit comme prévu.

{% multi_lang_include locales.md section="Questions fréquemment posées" %}
