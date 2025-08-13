---
nav_title: Locales dans les messages
article_title: Locales dans les messages
page_order: 6.3
description: "Cet article explique comment utiliser les paramètres locaux dans vos messages."
---

# Paramètres régionaux dans l’envoi de messages

> Après avoir ajouté les langues locales à votre espace de travail, vous pouvez cibler des utilisateurs dans différentes langues au sein d'un seul et même message e-mail.

## Conditions préalables

Pour modifier et gérer la [prise en charge multilingue]({{site.baseurl}}/multi_language_support/), vous devez disposer de l’autorisation « Gérer les paramètres multilingues ». Pour ajouter le paramètre régional à un message, vous devez disposer des autorisations nécessaires pour modifier les campagnes.

{% alert important %}
La prise en charge du multilinguisme et des langues locales dans les messages est actuellement en phase d'accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé.
{% endalert %}

## Utilisation des paramètres régionaux

Pour utiliser les paramètres régionaux dans vos messages, composez une campagne e-mail ou un canvas. Sélectionnez l'éditeur HTML ou l'éditeur par glisser-déposer, puis suivez les étapes en fonction de votre éditeur.

{% tabs %}
{% tab Editeur HTML %}

1. Mettez en surbrillance le texte à traduire. Sélectionnez **Insérer une étiquette de traduction**. Votre texte sera ainsi entouré de tags de traduction. <br>![Editeur HTML avec une seule locale sélectionnée.]({% image_buster /assets/img/multi-language_support/html_editor_translation_tag_example.png %})
2. Enregistrez le message en tant que brouillon.
3. Sélectionnez **Multi-langues** et ajoutez vos langues pour le message à l'aide du menu déroulant.
4. Sélectionnez **Télécharger le** modèle pour télécharger le modèle de traduction sous forme de fichier CSV. Complétez ensuite les traductions dans le fichier CSV. <br>![Exemple de fichier CSV de traduction.]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})
5. Sélectionnez **Télécharger les traductions** pour télécharger le fichier CSV contenant les traductions terminées.

{% endtab %}
{% tab Editeur par glisser-déposer %}

1. Ajoutez les tags de traduction {% raw %}`{% translation %}` et `{% endtranslation %}`{% endraw %} autour de tous les textes et images ou liens URL à traduire. 
2. Ajoutez un tag ID à chaque étiquette de traduction. En voici un exemple : {% raw %}`{% translation id_1 %}`{% endraw %} <br>![Éditeur par glisser-déposer avec deux ID de traduction.]({% image_buster /assets/img/multi-language_support/dnd_editor_translation_example.png %})
3. Après avoir ajouté les tags, enregistrez votre message en tant que brouillon.
4. Sélectionnez **Multi-langues** et ajoutez vos langues pour le message à l'aide du menu déroulant.
5. Sélectionnez **Télécharger le** modèle pour télécharger le modèle de traduction sous forme de fichier CSV. 
6. Complétez les traductions dans le fichier CSV. Si vous avez copié et collé les étiquettes de traduction directement à partir de l'étape 1, vous devrez peut-être supprimer `<code>` de la colonne **Étiquettes de traduction** du fichier CSV.
7. Sélectionnez **Télécharger les traductions** pour télécharger le fichier CSV contenant les traductions terminées.

{% endtab %}
{% endtabs %}

Toute modification des ID ou des lieux dans le fichier CSV ne sera pas automatiquement mise à jour dans votre message. Pour mettre à jour les traductions, mettez à jour le fichier CSV et téléchargez à nouveau le fichier.

## Prévisualiser vos paramètres régionaux

Dans la section **Aperçu et test**, sélectionnez **Utilisateur multilingue** pour vérifier si votre message est traduit comme prévu.

## Gestion des traductions

### Modifier les traductions pour les campagnes lancées et les canevas

Après le lancement d'une campagne ou d'un canvas, vous pouvez encore modifier les traductions lorsque vous êtes en mode brouillon. Cela s'applique que vous modifiiez les traductions directement dans le compositeur, par téléchargement CSV ou via l'API. 

Avant de procéder à des mises à jour de la traduction, la campagne ou le canvas doit d'abord être enregistré en tant que brouillon.

1. Sélectionnez **Modifier la campagne/le canevas**, puis effectuez vos modifications dans le compositeur.
2. Sélectionnez **Enregistrer comme brouillon**, puis sélectionnez **Oui** dans la fenêtre modale/boîte de dialogue, etc.
3. Accédez à l'étape du **résumé de l'examen** et sélectionnez **Mettre à jour la campagne/le canvas.**
4. Sélectionnez **Mettre à jour la campagne/le canvas** dans la fenêtre modale, etc.

Pour plus de détails sur la gestion des campagnes et des Canvas après leur lancement, reportez-vous à la section [Modification des campagnes lancées]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/) et des [brouillons de Canvas et modification après le lancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_drafts/).

### Duplication des étapes du canvas ou des campagnes, et traductions

Lors de la duplication d'une étape du canvas ou d'une campagne, que ce soit en mode brouillon après le lancement ou lors de la création initiale, les traductions associées à cette étape ne seront pas reportées. Toutes les traductions nécessaires doivent être ajoutées à la nouvelle étape ou campagne. Veillez à revoir et à mettre à jour les traductions en conséquence lorsque vous apportez des modifications à votre Canvas ou à votre campagne.

### Utiliser l'API multilingue avec Canvases

Pour utiliser l ['API multilingue avec Canvases]({{site.baseurl}}/api/endpoints/translations/), vous devez inclure les éléments `workflow_id`, `step_id`, et `message_variation_id` dans la liste des paramètres.

#### Les étapes du canvas ont été ajoutées aux versions préliminaires après le lancement.

Lorsque vous utilisez l'API multilingue avec des étapes du canvas qui ont été créées après le lancement du canvas, le site `message_variation_id` que vous transmettez à l'API sera vide ou vierge.

{% multi_lang_include locales.md section="Questions fréquemment posées" %}