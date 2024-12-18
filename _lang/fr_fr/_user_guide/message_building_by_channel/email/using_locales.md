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

## Utilisation des paramètres régionaux

Pour utiliser les paramètres régionaux dans vos messages, composez une campagne e-mail ou un canvas. Sélectionnez l'éditeur HTML ou l'éditeur par glisser-déposer, puis suivez les étapes en fonction de votre éditeur.

{% tabs %}
{% tab Editeur HTML %}

1. Mettez en surbrillance le texte à traduire. Sélectionnez **Insérer une étiquette de traduction**. Votre texte sera ainsi entouré de tags de traduction. <br>![]({% image_buster /assets/img/multi-language_support/html_editor_translation_tag_example.png %})
2. Enregistrez le message en tant que brouillon.
3. Sélectionnez **Multi-langues** et ajoutez vos langues pour le message à l'aide du menu déroulant.
4. Sélectionnez **Télécharger le modèle** pour télécharger le modèle de traduction au format CSV. Complétez ensuite les traductions dans le CSV. <br>![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})
5. Sélectionnez **Télécharger les traductions** pour télécharger le fichier CSV contenant les traductions terminées.

{% endtab %}
{% tab Editeur par glisser-déposer %}

1. Ajoutez les tags de traduction {% raw %}`{% translation %}` et `{% endtranslation %}`{% endraw %} autour de tous les textes et images ou liens URL à traduire.<br>![]({% image_buster /assets/img/multi-language_support/dnd_editor_translation_example.png %})
2. Après avoir ajouté les tags, enregistrez votre message en tant que brouillon.
3. Sélectionnez **Multi-langues** et ajoutez vos langues pour le message à l'aide du menu déroulant.
4. Sélectionnez **Télécharger le modèle** pour télécharger le modèle de traduction au format CSV. Complétez ensuite les traductions dans le CSV. <br>![]({% image_buster /assets/img/multi-language_support/translation_csv_example.png %})
5. Sélectionnez **Télécharger les traductions** pour télécharger le fichier CSV contenant les traductions terminées.

{% endtab %}
{% endtabs %}

Pour mettre à jour les traductions, actualisez le fichier CSV et chargez-le à nouveau. Cela signifie que toute modification des ID ou des lieux dans le CSV ne sera pas automatiquement mise à jour dans votre message.

{% alert tip %}
Consultez notre [API de traduction]({{site.baseurl}}/api/endpoints/translations) pour gérer et mettre à jour les traductions dans vos campagnes et canvas.
{% endalert %}

## Prévisualiser vos paramètres régionaux

Dans la section **Prévisualisation et test**, sélectionnez **Utilisateur multilingue** pour prévisualiser le message afin de vérifier si la traduction de votre message est conforme aux attentes.

## Foire aux questions

#### Je souhaite apporter une modification à la version traduite dans l'un de mes pays. Comment faire ?
Modifiez le fichier CSV, puis chargez à nouveau le fichier pour apporter une modification à la copie traduite.

#### Puis-je imbriquer des tags de traduction ?
Non.

#### Puis-je ajouter un style HTML dans les étiquettes de traduction ?
Oui. Toutefois, veillez à vérifier que le style HTML n'est pas traduit avec le contenu.

#### Quelles sont les validations ou les vérifications supplémentaires effectuées par Braze ?

| Scénario                                                                                                                                                 | Validation en Braze                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Il manque, dans un fichier de traduction, les paramètres régionaux associés au message en cours.                                                                               | Ce fichier de traduction ne sera pas téléchargé.                                                                       |
| Il manque, dans un fichier de traduction, des blocs de texte, par exemple un texte à l'intérieur des tags Liquid, provenant du message e-mail en cours.                                | Ce fichier de traduction ne sera pas téléchargé.                                                                       |
| Le fichier de traduction inclut le texte par défaut qui ne correspond pas aux blocs de texte du message e-mail actuel.                                          | Ce fichier de traduction ne sera pas téléchargé. Corrigez ce problème dans votre CSV avant d'essayer de le télécharger à nouveau.               |
| Le fichier de traduction inclut des langues qui n'existent pas dans les paramètres de **prise en charge multilingue**.                                                           | Ces paramètres régionaux ne seront pas enregistrés dans Braze.                                                                      |
| Le fichier de traduction comprend des blocs de texte qui n'existent pas dans le message actuel (comme le brouillon actuel au moment où les traductions sont chargées). | Les blocs de texte qui n'existent pas dans votre message actuel ne seront pas enregistrés du fichier de traduction vers Braze. |
| Suppression d'un paramètre régional du message alors que ce paramètre régional a déjà été chargé dans le message en tant que partie du fichier de traduction.                           | En supprimant le paramètre régional, vous supprimez toutes les traductions associées à celui-ci dans votre message.                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }