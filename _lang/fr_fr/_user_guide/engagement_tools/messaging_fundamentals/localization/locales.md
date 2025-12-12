---
nav_title: Locales dans les messages
article_title: Locales dans les messages
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "Cet article explique comment utiliser les paramètres locaux dans vos messages."
---

# Locales dans les messages

> Après avoir ajouté des locales à votre espace de travail, vous pouvez cibler des utilisateurs dans différentes langues au sein d'un seul message push, e-mail ou message in-app.

{% multi_lang_include locales.md section="Prerequisites" %}

{% alert important %}
La prise en charge du multilinguisme et des langues locales dans les messages est actuellement en phase d'accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé.
{% endalert %}

## Utilisation des langues locales

{% tabs %}
{% tab In-app message %}

Pour utiliser les lieux dans vos envois de messages, composez une campagne de messages in-app ou Canvas. Sélectionnez l'éditeur par glisser-déposer ou l'éditeur traditionnel, puis suivez les étapes en fonction de votre éditeur.

{% subtabs %}
{% subtab traditional editor %}

1. Ajoutez les tags de traduction {% raw %}`{% translation %}` et `{% endtranslation %}`{% endraw %} pour envelopper tous les textes et images ou liens URL à traduire. 
2. Ajoutez un tag ID à chaque étiquette de traduction. En voici un exemple : {% raw %}`{% translation id_1 %}`{% endraw %}

\![Editeur traditionnel avec ID de traduction.]({% image_buster /assets/img/multi-language_support/html_iam_editor_translation_tags.png %}){: style="max-width:60%;"}

{: start="3"}
3\. Après avoir ajouté les tags, enregistrez votre message en tant que brouillon.
4\. Sélectionnez **Gérer les langues** et ajoutez vos langues pour le message à l'aide du menu déroulant.

!modale "Gérer les langues" avec une locale sélectionnée.]({% image_buster /assets/img/multi-language_support/manage_languages_modal.png %})

{: start="5"}
5\. Sélectionnez **Télécharger le** modèle pour télécharger le modèle de traduction sous forme de fichier CSV. Complétez ensuite les traductions dans le fichier CSV.

\![Un exemple de fichier CSV de traduction.]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})

{: start="6"}
6\. Sélectionnez **Télécharger les traductions** pour télécharger le fichier CSV contenant les traductions terminées.

{% endsubtab %}
{% subtab Drag-and-drop editor %}

1. Ajoutez les tags de traduction {% raw %}`{% translation %}` et `{% endtranslation %}`{% endraw %} pour envelopper tous les textes et images ou liens URL à traduire. 
2. Ajoutez un tag ID à chaque étiquette de traduction. En voici un exemple : {% raw %}`{% translation id_1 %}`{% endraw %} 

\![Editeur par glisser-déposer avec deux ID de traduction.]({% image_buster /assets/img/multi-language_support/dnd_iam_editor_translation_tags.png %}){: style="max-width:70%;"}

{: start="3"}
3\. Après avoir ajouté les tags, enregistrez votre message en tant que brouillon, puis ouvrez à nouveau l'éditeur.
4\. Dans le panneau **Créer**, sélectionnez **Multi-langues** et ajoutez vos langues pour le message à l'aide du menu déroulant.
5\. Sélectionnez **Télécharger le** modèle pour télécharger le modèle de traduction sous forme de fichier CSV. 

!Panneau "Multi-langues" avec bouton pour télécharger le modèle.]({% image_buster /assets/img/multi-language_support/dnd_iam_download_template.png %}){: style="max-width:40%;"}

{: start="6"}
6\. Complétez les traductions dans le fichier CSV. Si vous avez copié et collé les étiquettes de traduction directement à partir de l'étape 1, vous devrez peut-être supprimer `<code>` de la colonne **Étiquettes de traduction** du fichier CSV.
7\. Sélectionnez **Télécharger les traductions** pour télécharger le fichier CSV contenant les traductions terminées.

!Panneau "Multi-langues" avec des boutons pour télécharger le modèle et charger les traductions.]({% image_buster /assets/img/multi-language_support/dnd_iam_upload_translations.png %}){: style="max-width:40%;"}

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Email %}

Pour utiliser les lieux dans vos messages, composez une campagne e-mail ou Canvas. Sélectionnez l'éditeur HTML ou l'éditeur par glisser-déposer, puis suivez les étapes en fonction de votre éditeur.

{% subtabs %}
{% subtab HTML editor %}

1. Mettez en surbrillance le texte à traduire. Sélectionnez **Insérer une étiquette de traduction**. Votre texte sera ainsi entouré de tags de traduction. <br>\![Editeur HTML avec une seule locale sélectionnée.]({% image_buster /assets/img/multi-language_support/html_editor_translation_tag_example.png %})
2. Enregistrez le message en tant que brouillon.
3. Sélectionnez **Multi-langues** et ajoutez vos langues pour le message à l'aide du menu déroulant.
4. Sélectionnez **Télécharger le** modèle pour télécharger le modèle de traduction sous forme de fichier CSV. Complétez ensuite les traductions dans le fichier CSV. <br>\![Un exemple de fichier CSV de traduction.]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})
5. Sélectionnez **Télécharger les traductions** pour télécharger le fichier CSV contenant les traductions terminées.

{% endsubtab %}
{% subtab Drag-and-drop editor %}

1. Ajoutez les tags de traduction {% raw %}`{% translation %}` et `{% endtranslation %}`{% endraw %} pour envelopper tous les textes et images ou liens URL à traduire. 
2. Ajoutez un tag ID à chaque étiquette de traduction. En voici un exemple : {% raw %}`{% translation id_1 %}`{% endraw %} <br>\![Editeur par glisser-déposer avec deux ID de traduction.]({% image_buster /assets/img/multi-language_support/dnd_editor_translation_example.png %})
3. Après avoir ajouté les tags, enregistrez votre message en tant que brouillon.
4. Sélectionnez **Multi-langues** et ajoutez vos langues pour le message à l'aide du menu déroulant.
5. Sélectionnez **Télécharger le** modèle pour télécharger le modèle de traduction sous forme de fichier CSV. 
6. Complétez les traductions dans le fichier CSV. Si vous avez copié et collé les étiquettes de traduction directement à partir de l'étape 1, vous devrez peut-être supprimer `<code>` de la colonne **Étiquettes de traduction** du fichier CSV.
7. Sélectionnez **Télécharger les traductions** pour télécharger le fichier CSV contenant les traductions terminées.

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Push %}

Pour utiliser les lieux dans vos messages, composez une campagne push ou un canvas, puis procédez comme suit :

1. Ajoutez les tags de traduction {% raw %}`{% translation id1%}` et `{% endtranslation %}`{% endraw %} pour envelopper tous les textes, images ou liens URL à traduire. Chaque ID de traduction (`id1`) doit être unique.

Compositeur de notifications push avec des étiquettes de traduction ajoutées aux champs du titre et du message.]({% image_buster /assets/img/multi-language_support/push_translation_tags.png %})

{: start="2"}
2\. Enregistrez votre message en tant que brouillon.
3\. Sélectionnez **Gérer la langue** et ajoutez vos localisations pour le message à l'aide du menu déroulant.
4\. Sélectionnez **Télécharger le modèle**, puis remplissez les traductions dans le modèle CSV.

\![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})

{: start="5"}
5\. Pour télécharger le modèle CSV complété, sélectionnez **Télécharger les traductions**. 

La fenêtre "Messages multilingues" avec deux langues sélectionnées et des boutons pour télécharger un modèle ou des traductions.]({% image_buster /assets/img/multi-language_support/upload_translation.png %})

{% endtab %}
{% endtabs %}

Toute modification des ID ou des lieux dans le fichier CSV ne sera pas automatiquement mise à jour dans votre message. Pour mettre à jour les traductions, mettez à jour le fichier CSV et téléchargez à nouveau le fichier.

{% alert tip %}
Consultez notre [API de traduction]({{site.baseurl}}/api/endpoints/translations) pour gérer et mettre à jour les traductions dans vos campagnes et Canvases.
{% endalert %}

## Prévisualisez vos lieux

{% tabs %}
{% tab In-app message %}

Dans la liste déroulante **Prévisualiser le message en tant qu'utilisateur** de l'onglet **Test**, sélectionnez **Utilisateur personnalisé** et entrez différentes langues pour prévisualiser le message afin de vérifier si votre message se traduit comme prévu.


{% endtab %}
{% tab Email %}

Dans la section **Aperçu & Test**, sélectionnez **Utilisateur multilingue** pour vérifier si votre message est traduit comme prévu.

{% endtab %}
{% tab Push %}

Dans la liste déroulante **Prévisualiser le message en tant qu'utilisateur** de l'onglet **Test**, sélectionnez **Utilisateur personnalisé** et entrez différentes langues pour prévisualiser le message afin de vérifier si votre message se traduit comme prévu.

{% endtab %}
{% endtabs %}

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

## Questions fréquemment posées

#### Puis-je apporter une modification à la version traduite dans l'un de mes pays ?
Oui. Modifiez d'abord le fichier CSV, puis téléchargez à nouveau le fichier pour apporter une modification à la copie traduite.

#### Puis-je imbriquer des étiquettes de traduction ?
Non.

#### Puis-je ajouter un style HTML dans les étiquettes de traduction ?
Oui, mais vérifiez que le style HTML n'est pas traduit avec le contenu.

#### Quelles sont les validations ou les vérifications supplémentaires effectuées par Braze ?

| Scénario                                                                                                                                                 | Validation en Braze                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Il manque dans un fichier de traduction les locales associées au message en cours.                                                                               | Ce fichier de traduction ne sera pas téléchargé.                                                                       |
| Il manque des blocs de texte dans un fichier de traduction, par exemple un texte à l'intérieur des étiquettes Liquid, dans le message e-mail en cours.                                | Ce fichier de traduction ne sera pas téléchargé.                                                                       |
| Le fichier de traduction inclut le texte par défaut qui ne correspond pas aux blocs de texte du message e-mail actuel.                                          | Ce fichier de traduction ne sera pas téléchargé. Corrigez ce problème dans votre CSV avant d'essayer de le télécharger à nouveau.               |
| Le fichier de traduction inclut des langues qui n'existent pas dans les paramètres de **prise en charge multilingue**.                                                           | Ces lieux ne seront pas enregistrés dans Braze.                                                                      |
| Le fichier de traduction comprend des blocs de texte qui n'existent pas dans l'envoi actuel (comme le brouillon actuel au moment où les traductions sont téléchargées). | Les blocs de texte qui n'existent pas dans votre message actuel ne seront pas enregistrés du fichier de traduction vers Braze. |
| Suppression d'une locale du message alors que cette locale a déjà été téléchargée dans le message en tant que partie du fichier de traduction.                           | En supprimant la locale, vous supprimez toutes les traductions associées à la locale dans votre message.                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }