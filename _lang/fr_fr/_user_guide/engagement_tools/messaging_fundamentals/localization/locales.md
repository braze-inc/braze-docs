---
nav_title: Locales dans les messages
article_title: Traduire les locales
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "Cet article explique comment utiliser les paramètres locaux dans vos messages."
---

# Traduire les locales

> Après avoir ajouté des locales à votre espace de travail, vous pouvez cibler des utilisateurs dans différentes langues au sein d'un même push, e-mail, bannière ou message in-app.

{% multi_lang_include locales.md section="Prerequisites" %}

## Utilisation des paramètres régionaux

### Étape 1 : Configurer les lieux dans votre espace de travail {#workspace-setup}

Avant de pouvoir utiliser les locales et les étiquettes de traduction, vous devez d'abord [ajouter les locales à votre espace de travail]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings).

### Étape 2 : Ajoutez des étiquettes Liquid à votre message. {#add-translation-tags}

Ajoutez les tags de traduction {% raw %}`{% translation your_id_here %}` et `{% endtranslation %}`{% endraw %} pour envelopper tous les textes, images ou liens URL que vous allez traduire.

Chaque traduction devrait avoir un `id` unique. Par exemple, lorsque vous traduisez un simple message d'accueil, vous pouvez nommer l'ID "message d'accueil" :

{% raw %}`{% translation greeting %}Hello!{% endtranslation}`{% endraw %}

#### Localisation des blocs HTML

Un paragraphe plus complexe peut comporter plusieurs tags de traduction : ("offer_text" et "offer_amount"):

{% raw %}
```
{% translation offer_text %}Sign up now to save{% endtranslation %}
<b>{% translation offer_amount %}50% Off{% endtranslation %}</b>
```
{% endraw %}

{% alert important %}
Le fait d'envelopper de grands blocs HTML dans des étiquettes de traduction peut entraîner des problèmes de feuille de style ou de stylisme. Enveloppez les sections de texte les plus petites possibles.
{% endalert %}

#### Localisation des liens

Pour localiser les tags des étiquettes d'ancrage, veillez à **n'** envelopper **que les parties spécifiques à la langue** et non l'ensemble de l'attribut URL de `href`. Si vous enveloppez toute l'URL, le modèle de lien risque de ne pas fonctionner correctement.

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

### Étape 3 : Choisissez les lieux d'envoi des messages {#choose-locales}

Une fois que vos tags de traduction sont dans le message, allez dans les paramètres multilingues du message et sélectionnez une ou plusieurs localités à traduire pour ce message.

![Paramètres multilingues avec un champ déroulant pour sélectionner les langues.]({% image_buster /assets/img/multi-language_support/manage_language_dropdown.png %}){: style="max-width:80%;"}

{% tabs %}
{% tab Email %}
Sélectionnez **Multi-Language** dans le menu Content lorsque vous modifiez votre message.

![Paramètres multilingues pour l'e-mail.]({% image_buster /assets/img/multi-language_support/email_multi_language.png %}){: style="max-width:45%;"}

{% endtab %}

{% tab Push %}
Sélectionnez **Gérer les langues** lorsque vous modifiez votre message.

![Paramètres multilingues pour la poussée.]({% image_buster /assets/img/multi-language_support/push_manage_languages.png %})

{% endtab %}

{% tab In-app message %}
{% subtabs %}
{% subtab Drag-and-Drop Editor %}
Sélectionnez **Gérer les langues** en bas de la section **Créer.** 

![Paramètres multilingues pour les messages in-app à glisser-déposer.]({% image_buster /assets/img/multi-language_support/iam_dnd_manage_languages.png %}){: style="max-width:45%;"}

{% endsubtab %}
{% subtab Traditional editor %}

Sélectionnez **Gérer les langues** lorsque vous modifiez votre message.

![Paramètres multilingues pour les messages HTML in-app.]({% image_buster /assets/img/multi-language_support/iam_html_manage_languages.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Banner %}
Sélectionnez **Gérer les langues** lorsque vous modifiez votre message.

![Paramètres multilingues pour les bannières.]({% image_buster /assets/img/multi-language_support/banner_manage_languages.png %})

{% endtab %}
{% endtabs %}

### Étape 4 : Téléchargez le modèle CSV {#download-csv}

Après avoir sélectionné vos locales, sélectionnez **Télécharger le modèle** pour télécharger un modèle CSV contenant une matrice des ID de traduction et des locales que vous avez sélectionnées.

![Exemple de CSV pour les locales en, fr, et es.]({% image_buster /assets/img/multi-language_support/example_translation_csv.png %}){: style="max-width:70%;"}

### Étape 5 : Télécharger un fichier CSV complété {#upload-csv}

{% alert important %}
Toute modification des ID ou des lieux dans le fichier CSV ne sera pas automatiquement mise à jour dans votre message. Pour mettre à jour les traductions, mettez à jour le fichier CSV et téléchargez à nouveau le fichier.
{% endalert %}

Voici le format d'un exemple de CSV complété :

```
Variant1,,,,
,Translation tags,en,es,fr
title,We noticed you've left something behind,We noticed you've left something behind,Notamos que has dejado algo atrás,Nous avons remarqué que vous avez oublié quelque chose derrière vous
offer_text,Check out now and receive,Check out now and receive,Paga ahora y recibe,Payez maintenant et recevez
offer_amount,10% Off,10% Off,10% de Descuento,10 % de réduction
cta,CHECK OUT NOW,CHECK OUT NOW,VERIFICAR AHORA,VÉRIFIER MAINTENANT
```

### Étape 6 : Prévisualisation des lieux {#preview-locales}

Lors de la prévisualisation de votre message, sélectionnez l'option **Utilisateur multilingue** dans le menu déroulant **Prévisualiser en tant qu'utilisateur**. Cela vous permet de passer d'une définition de locale à l'autre pour prévisualiser toutes les traductions de votre message.

![Prévisualisation des localisations]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %})

{% alert tip %}
Consultez notre [API de traduction]({{site.baseurl}}/api/endpoints/translations) pour gérer et mettre à jour les traductions dans vos campagnes et canvas.
{% endalert %}

## Envois de messages de droite à gauche

Lorsque vous remplissez le fichier de traduction pour des langues qui s'écrivent de droite à gauche (comme l'arabe), entourez la traduction de `span` afin qu'elle soit correctement formatée :

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

Les traductions sont copiées avec une étape du canvas, une campagne ou une variation de campagne. Il en va de même pour la copie entre espaces de travail, à condition que les paramètres locaux soient définis dans l'espace de travail de destination. Veillez à revoir et à mettre à jour les traductions en conséquence lorsque vous apportez des modifications à votre Canvas ou à votre campagne.

### Utiliser l'API multilingue avec Canvases

Pour utiliser l'[API multilingue avec Canvases]({{site.baseurl}}/api/endpoints/translations/), vous devez inclure les éléments `workflow_id`, `step_id`, et `message_variation_id` dans la liste des paramètres.

#### Les étapes du canvas ont été ajoutées aux versions préliminaires après le lancement.

Lorsque vous utilisez l'API multilingue avec des étapes du canvas qui ont été créées après le lancement du canvas, le site `message_variation_id` que vous transmettez à l'API sera vide ou vierge.

## Foire aux questions

#### Puis-je apporter une modification à la version traduite dans l'un de mes pays ?
Oui. Modifiez d'abord le fichier CSV, puis téléchargez à nouveau le fichier pour apporter une modification à la copie traduite.

#### Puis-je imbriquer des tags de traduction ?
Non.

#### Les traductions prennent-elles en charge le style HTML ?
Oui, mais vérifiez que le style HTML n'est pas traduit avec le contenu.

#### Puis-je envelopper des messages HTML entiers dans une étiquette de traduction ?
Non, vos étiquettes de traduction doivent être aussi petites que possible pour éviter les limitations de performance ou de taille.

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
