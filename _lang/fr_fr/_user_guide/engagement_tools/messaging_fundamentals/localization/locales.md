---
nav_title: Locales dans les messages
article_title: Traduction des paramètres régionaux
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "Cet article fournit des instructions sur la manière d'utiliser les paramètres régionaux dans vos messages."
---

# Traduction des paramètres régionaux

> Après avoir ajouté des paramètres régionaux à votre espace de travail, vous pouvez effectuer le ciblage d'utilisateurs dans différentes langues à l'aide d'une seule notification push, d'un e-mail, d'une bannière, d'un message in-app ou d'un bloc de contenu.

{% multi_lang_include locales.md section="Prerequisites" %}

## Utilisation des paramètres régionaux

### Étape 1 : Configurez les paramètres régionaux dans votre espace de travail. {#workspace-setup}

Avant de pouvoir utiliser les paramètres régionaux et les étiquettes de traduction, il est nécessaire [d'ajouter les paramètres régionaux à votre espace de travail]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings).

### Étape 2 : Veuillez ajouter des étiquettes Liquid à votre message. {#add-translation-tags}

Veuillez ajouter les étiquettes de traduction{% raw %}`{% translation your_id_here %}`  et`{% endtranslation %}`{% endraw %}  pour encadrer tout le texte, les images ou les URL des liens que vous traduirez.

Chaque traduction doit disposer d'un identifiant unique`id`. Par exemple, lorsque vous traduisez une simple salutation, vous pouvez nommer l'ID « greeting » :

{% raw %}`{% translation greeting %}Hello!{% endtranslation}`{% endraw %}

#### Localisation des blocs HTML

Un paragraphe plus complexe peut comporter plusieurs étiquettes de traduction("offer_text" et "offer_amount"):

{% raw %}
```
{% translation offer_text %}Sign up now to save{% endtranslation %}
<b>{% translation offer_amount %}50% Off{% endtranslation %}</b>
```
{% endraw %}

{% alert important %}
Encadrer de grands blocs HTML dans des tags de traduction peut entraîner des problèmes de feuille de style ou de mise en forme. Veuillez veiller à ce que les sections de texte soient aussi courtes que possible.
{% endalert %}

#### Localisation des liens

Pour localiser les liens des étiquettes d'ancrage, veuillez vous assurer de n'encapsuler **que les parties spécifiques à la langue** et non l'attribut URL dans `href`son intégralité. Si vous encapsulez l'URL entière, le modèle de lien pourrait ne pas fonctionner correctement.

##### Utilisation correcte

{% raw %}
```
<a href="https://www.braze.com/{% translation link_href %}en{% endtranslation %}/page"></a>
```
{% endraw %}

##### Utilisation incorrecte

{% raw %}
```
<a href="{% translation link_href %}https://www.braze.com/en/page{% endtranslation %}"></a>
```
{% endraw %}

### Étape 3 : Veuillez sélectionner les paramètres régionaux pour les messages {#choose-locales}

Une fois que vos étiquettes de traduction sont dans le message, accédez aux paramètres multilingues du message et sélectionnez une ou plusieurs langues à traduire pour ce message.

![Paramètres multilingues avec un champ déroulant permettant de sélectionner les paramètres régionaux.]({% image_buster /assets/img/multi-language_support/manage_language_dropdown.png %}){: style="max-width:80%;"}

{% tabs %}
{% tab Email %}
Veuillez sélectionner **« Multilingue »** dans le menu « Contenu » lorsque vous modifiez votre message.

![Paramètres multilingues pour les e-mails.]({% image_buster /assets/img/multi-language_support/email_multi_language.png %}){: style="max-width:45%;"}

{% endtab %}

{% tab Push %}
Veuillez sélectionner **« Gestion des langues** » lorsque vous modifiez votre message.

![Paramètres multilingues pour les notifications push.]({% image_buster /assets/img/multi-language_support/push_manage_languages.png %})

{% endtab %}

{% tab In-app message %}
{% subtabs %}
{% subtab Drag-and-Drop Editor %}
Veuillez sélectionner **« Gestionnaire des langues** » au bas de la section **« Créer** ».

![Paramètres multilingues pour les messages glisser-déposer in-app.]({% image_buster /assets/img/multi-language_support/iam_dnd_manage_languages.png %}){: style="max-width:45%;"}

{% endsubtab %}
{% subtab Traditional editor %}

Veuillez sélectionner **« Gérer les langues** » lorsque vous modifiez votre message.

![Paramètres multilingues pour les messages in-app HTML.]({% image_buster /assets/img/multi-language_support/iam_html_manage_languages.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Banner %}
Veuillez sélectionner **« Gestion des langues** » lorsque vous modifiez votre message.

![Paramètres multilingues pour les bannières.]({% image_buster /assets/img/multi-language_support/banner_manage_languages.png %})

{% endtab %}

{% tab Content Block %}
Veuillez sélectionner **« Gestionnaire des langues** » lorsque vous modifiez votre bloc de contenu.

{% alert important %}
Les blocs de contenu associés à des traductions téléchargées ne peuvent pas être remplacés par une campagne individuelle ou un message Canvas.
{% endalert %}

![Paramètres multilingues pour les blocs de contenu.]({% image_buster /assets/img/multi-language_support/content_block_manage_languages.png %})

{% endtab %}
{% endtabs %}

### Étape 4 : Télécharger le modèle CSV {#download-csv}

Après avoir sélectionné vos paramètres régionaux, veuillez sélectionner **Télécharger le modèle** pour télécharger un modèle CSV contenant une matrice des ID de traduction et des paramètres régionaux que vous avez sélectionnés.

![Exemple de fichier CSV pour les paramètres régionaux en, fr et es.]({% image_buster /assets/img/multi-language_support/example_translation_csv.png %}){: style="max-width:70%;"}

### Étape 5 : Veuillez télécharger le fichier CSV complété. {#upload-csv}

{% alert important %}
Toute modification des ID ou des lieux dans le fichier CSV ne sera pas automatiquement mise à jour dans votre message. Pour mettre à jour les traductions, mettez à jour le fichier CSV et téléchargez à nouveau le fichier.
{% endalert %}

Voici le format d'un exemple de fichier CSV complété :

```
Variant1,,,,
,Translation tags,en,es,fr
title,We noticed you've left something behind,We noticed you've left something behind,Notamos que has dejado algo atrás,Nous avons remarqué que vous avez oublié quelque chose derrière vous
offer_text,Check out now and receive,Check out now and receive,Paga ahora y recibe,Payez maintenant et recevez
offer_amount,10% Off,10% Off,10% de Descuento,10 % de réduction
cta,CHECK OUT NOW,CHECK OUT NOW,VERIFICAR AHORA,VÉRIFIER MAINTENANT
```

### Étape 6 : Aperçu des paramètres régionaux {#preview-locales}

Lorsque vous prévisualisez votre message, veuillez sélectionner l'option **« Utilisateur multilingue** » dans le menu déroulant **« Prévisualiser en tant qu'utilisateur** ». Cela vous permet de basculer entre différentes définitions de paramètres régionaux afin de prévisualiser toutes les traductions de votre message.

![Aperçus locaux]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %})

{% alert tip %}
Consultez notre [API de traduction]({{site.baseurl}}/api/endpoints/translations) pour gérer et mettre à jour les traductions dans vos campagnes et canvas.
{% endalert %}

## Envois de messages de droite à gauche

Lorsque vous remplissez le fichier de traduction pour les langues qui s'écrivent de droite à gauche (comme l'arabe), veuillez encadrer la traduction avec`span`  afin qu'elle soit correctement formatée :

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

## Gestion des traductions

### Modifier les traductions pour les campagnes lancées et les canevas

Après le lancement d'une campagne ou d'un canvas, vous pouvez encore modifier les traductions lorsque vous êtes en mode brouillon. Cela s'applique que vous modifiiez les traductions directement dans le compositeur, par téléchargement CSV ou via l'API. 

Pour plus de détails sur la gestion des campagnes et des Canvas après leur lancement, reportez-vous à la section [Modification des campagnes lancées]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/) et des [brouillons de Canvas et modification après le lancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_drafts/).

### Duplication des étapes du canvas ou des campagnes, et traductions

Les traductions sont copiées avec une étape du canvas, une campagne ou une variante de campagne. Cela s'applique également lors de la copie entre espaces de travail, à condition que les paramètres régionaux soient définis dans l'espace de travail de destination. Veillez à revoir et à mettre à jour les traductions en conséquence lorsque vous apportez des modifications à votre Canvas ou à votre campagne.

### Utilisation de l'API multilingue avec les canevas

Pour utiliser l'[API]({{site.baseurl}}/api/endpoints/translations/) [multilingue avec les canevas]({{site.baseurl}}/api/endpoints/translations/), il est nécessaire d'inclure les paramètres `workflow_id`,`step_id` et`message_variation_id`  dans la liste des paramètres.

#### Les étapes du canvas ont été ajoutées aux versions préliminaires après le lancement.

Lorsque vous utilisez l'API multilingue avec des étapes du canvas créées après le lancement de Canvas, les`message_variation_id`données que vous transmettez à l'API seront vides ou vierges.

## Foire aux questions

#### Puis-je apporter une modification à la version traduite dans l'un de mes pays ?
Oui. Modifiez d'abord le fichier CSV, puis téléchargez à nouveau le fichier pour apporter une modification à la copie traduite.

#### Puis-je imbriquer des tags de traduction ?
Non.

#### Les traductions prennent-elles en charge le langage HTML pour la mise en forme ?
Oui, mais vérifiez que le style HTML n'est pas traduit avec le contenu.

#### Puis-je inclure des messages HTML complets dans une étiquette de traduction ?
Non, vos tags de traduction doivent être aussi petits que possible afin d'éviter toute limitation en termes de performances ou de taille.

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
