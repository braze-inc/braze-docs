---
nav_title: Locales dans les messages
article_title: Locales dans les messages
page_order: 4
alias: /iam_locales/
description: "Cet article explique comment utiliser les paramètres locaux dans vos messages in-app."
---

# Locales dans les messages

> Après avoir ajouté des locales à votre espace de travail, vous pouvez cibler des utilisateurs dans différentes langues au sein d'un seul message in-app.

{% multi_lang_include locales.md section="Conditions préalables" %}

## Utilisation des paramètres régionaux

Pour utiliser les lieux dans vos envois de messages, composez une campagne de messages in-app ou Canvas. Sélectionnez l'éditeur par glisser-déposer ou l'éditeur traditionnel, puis suivez les étapes en fonction de votre éditeur.

{% tabs %}
{% tab éditeur traditionnel %}

1. Ajoutez les tags de traduction {% raw %}`{% translation %}` et `{% endtranslation %}`{% endraw %} autour de tous les textes et images ou liens URL à traduire. 
2. Ajoutez un tag ID à chaque étiquette de traduction. En voici un exemple : {% raw %}`{% translation id_1 %}`{% endraw %}

![Éditeur traditionnel avec ID de traduction.]({% image_buster /assets/img/multi-language_support/html_iam_editor_translation_tags.png %}){: style="max-width:60%;"}

{: start="3"}
3\. Après avoir ajouté les tags, enregistrez votre message en tant que brouillon.
4\. Sélectionnez **Gérer les langues** et ajoutez vos langues pour le message à l'aide du menu déroulant.

![Fenêtre modale "Gérer les langues" avec une seule langue locale sélectionnée.]({% image_buster /assets/img/multi-language_support/manage_languages_modal.png %})

{: start="5"}
5\. Sélectionnez **Télécharger le** modèle pour télécharger le modèle de traduction sous forme de fichier CSV. Complétez ensuite les traductions dans le fichier CSV.

![Exemple de fichier CSV de traduction.]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})

{: start="6"}
6\. Sélectionnez **Télécharger les traductions** pour télécharger le fichier CSV contenant les traductions terminées.

{% endtab %}
{% tab Editeur par glisser-déposer %}

1. Ajoutez les tags de traduction {% raw %}`{% translation %}` et `{% endtranslation %}`{% endraw %} autour de tous les textes et images ou liens URL à traduire. 
2. Ajoutez un tag ID à chaque étiquette de traduction. En voici un exemple : {% raw %}`{% translation id_1 %}`{% endraw %} 

![Éditeur par glisser-déposer avec deux ID de traduction.]({% image_buster /assets/img/multi-language_support/dnd_iam_editor_translation_tags.png %}){: style="max-width:70%;"}

{: start="3"}
3\. Après avoir ajouté les tags, enregistrez votre message en tant que brouillon, puis ouvrez à nouveau l'éditeur.
4\. Dans le panneau **Créer**, sélectionnez **Multi-langues** et ajoutez vos langues pour le message à l'aide du menu déroulant.
5\. Sélectionnez **Télécharger le** modèle pour télécharger le modèle de traduction sous forme de fichier CSV. 

![Panneau "Multi-language" avec bouton pour télécharger le modèle.]({% image_buster /assets/img/multi-language_support/dnd_iam_download_template.png %}){: style="max-width:40%;"}

{: start="6"}
6\. Complétez les traductions dans le fichier CSV. Si vous avez copié et collé les étiquettes de traduction directement à partir de l'étape 1, vous devrez peut-être supprimer `<code>` de la colonne **Étiquettes de traduction** du fichier CSV.
7\. Sélectionnez **Télécharger les traductions** pour télécharger le fichier CSV contenant les traductions terminées.

![Panneau "Multi-langues" avec des boutons pour télécharger le modèle et les traductions.]({% image_buster /assets/img/multi-language_support/dnd_iam_upload_translations.png %}){: style="max-width:40%;"}

{% endtab %}
{% endtabs %}

Toute modification des ID ou des lieux dans le fichier CSV ne sera pas automatiquement mise à jour dans votre message. Pour mettre à jour les traductions, mettez à jour le fichier CSV et téléchargez à nouveau le fichier.

{% alert tip %}
Consultez notre [API de traduction]({{site.baseurl}}/api/endpoints/translations) pour gérer et mettre à jour les traductions dans vos campagnes et canvas.
{% endalert %}

{% multi_lang_include locales.md section="Aperçu" %}

{% multi_lang_include locales.md section="Questions fréquemment posées" %}
