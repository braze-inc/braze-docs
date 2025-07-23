---
nav_title: Paramètres généraux de style d’e-mail
article_title: Paramètres généraux de style d’e-mail
alias: "/dnd/global_style_settings/"
channel: email
page_order: 3
description: "Cet article de référence explique comment définir des paramètres globaux de style d'e-mail dans l'éditeur glisser-déposer pour vos campagnes et vos Canevas."
tool: 
  - Campaigns
  - Canvas
---

# Paramètres de style globaux des e-mails

> Avec des paramètres de style globaux, vous pouvez personnaliser l’apparence de vos campagnes par e-mail et de vos Canvas. Vous pouvez ajouter et personnaliser un thème par défaut pour votre éditeur par glisser-déposer. Cela inclut la modification de vos styles pour les titres de courrier électronique, le texte, les boutons, etc. L'utilisation d'une combinaison de ces paramètres peut contribuer à créer un aspect cohérent dans l'ensemble de vos envois de messages e-mail.

Pour modifier vos paramètres de style globaux, allez dans **Paramètres** > **Préférences e-mail** > **Préférences e-mail glisser-déposer.** Après avoir modifié les styles dans l'éditeur par glisser-déposer de l'e-mail, cliquez sur **Enregistrer.** Pour personnaliser davantage vos campagnes d'e-mail et Canvases, découvrez comment vous pouvez incorporer [des blocs d'éditeur par glisser-déposer][8].

![][1]

{% alert note %}
Les mises à jour apportées aux paramètres de style globaux s’appliqueront à toutes les campagnes par e-mail et à tous les Canvas futurs.
{% endalert %} 

## Style basique 

Pour le **style de base**, vous pouvez définir vos couleurs d'arrière-plan par défaut pour l'e-mail et le contenu de vos campagnes d'e-mail et de vos canevas. Vous pouvez également sélectionner une police par défaut, ajouter une police personnalisée et modifier les couleurs de lien.

![Options de style de base qui comprennent des options pour modifier les couleurs d’arrière-plan et de contenu de l’e-mail, le nom de police par défaut et la couleur du lien par défaut.][2] 

## Police personnalisée

Avec des polices personnalisées, vous pouvez ajouter manuellement une police Internet pour garder la cohérence de votre marque entre plusieurs plateformes d’e-mails. Vous pouvez ajouter une police personnalisée par section. 

Avant d'ajouter une police personnalisée, vérifiez que le fichier de police personnalisée répond aux exigences suivantes :

- CORS doit être activé sur le serveur qui fournit le fichier de polices personnalisé. Cette fonction est généralement gérée par votre équipe informatique. 
  - Le fichier de police personnalisé doit comporter l'en-tête : `Access-Control-Allow-Origin: *`
- L'URL du fichier doit pointer vers un fichier CSS (pas WOFF, OTF, etc.)
- Le nom de la police personnalisée doit correspondre au nom de la face de la police dans le fichier CSS

Pour ajouter une police personnalisée :

1. Cliquez sur **Ajouter une police personnalisée** sous la rubrique **Nom de la police par défaut de** la section de style.
2. Dans le champ **Nom de la police**, saisissez le même nom de police que celui qui apparaît dans votre fichier source de police personnalisée. Assurez-vous que le nom est en majuscules et correctement espacé. 
3. Saisissez l'URL correspondant dans le champ **URL de la police**.
4. Vérifiez que l’aperçu affiche votre police personnalisée avant d’enregistrer. 
5. Cliquez sur **Enregistrer** pour utiliser la police personnalisée comme police par défaut pour vos e-mails. 

{% alert important %}
Gmail ne prend pas en charge les polices personnalisées, de sorte que votre police personnalisée peut s’afficher comme une police système par défaut. Pour les autres plateformes d’e-mail, vérifiez que votre police personnalisée s’affiche correctement avant d’envoyer votre e-mail.
{% endalert %}

Sachez que le fournisseur de polices personnalisées peut collecter des données personnelles auprès de vos destinataires. Vous devez consulter les politiques de votre fournisseur de polices de caractères avant de les utiliser.

Pour utiliser des polices alternatives personnalisées dans vos campagnes d'e-mail, vous avez la possibilité de créer un [modèle d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/) ou des [blocs de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/). Assurez-vous de vérifier que votre choix de police correspond à une utilisation sur Internet et soit pris en charge par vos plateformes d’e-mails. 

### Police de secours

Les polices de secours sont utilisées pour le titre, l’en-tête et le corps du texte quand la police que vous avez choisie par défaut n’est pas prise en charge par votre fournisseur de boîte de réception ou votre système d’exploitation. Braze définit automatiquement Arial comme police de secours par défaut si les paramètres de style globaux sont conservés. Vous avez également la possibilité d’ajouter les options d’empattement typographique ou sans empattement pour votre famille de police par défaut.

![][11]

Vous pouvez ajouter jusqu’à 17 polices de secours. La première police de secours sélectionnée sera celle qui sera tentée en premier. La police de secours ne sera appliquée qu’aux modèles, aux campagnes par e-mail et aux composants Canvas nouvellement créés. La police de remplacement n'est pas automatiquement définie pour les messages qui ont été créés avant que la police de remplacement ne soit spécifiée. Nous vous recommandons fortement de sélectionner des polices de secours qui sont similaires à votre envoi de messages e-mail pour maintenir une forme de cohérence au sein de votre marque.

## Style de titre

Ici, vous pouvez ajuster les styles de vos titres d’e-mail en modifiant la taille de police, la couleur de police et l’alignement du texte. Cela s’applique à l’en-tête principal et à l’en-tête secondaire. 

![][9]

En option, vous pouvez remplacer le style par défaut du thème de votre éditeur par glisser-déposer. Cliquez sur **Remplacer le style par défaut** pour appliquer le style de titre de votre choix. Cela peut inclure la définition d’une police et d’une couleur de lien différentes.

## Style de paragraphe

Pour définir un style de paragraphe par défaut, accédez à la section **Style de paragraphe**, entrez la **taille de la police** et sélectionnez **Couleur de police** pour choisir une couleur de police. Vous pouvez également ajuster le style du bloc pour le corps du texte en modifiant les valeurs **Padding Top**, **Padding Right**, **Padding Bottom** et **Padding Left**. Cela s’appliquera à l’espacement autour des quatre zones entourant le bloc du paragraphe.

![][7]

## Style de liste

Lorsque vous ajoutez des listes à votre envoi de messages, la section **List Styling** permet de créer une cohérence dans la manière dont vos listes sont stylisées. Ceci inclut notamment : 

- Taille de police
- Couleur de police
- Poids de la police
- Hauteur de ligne
- Alignement
- Sens du texte
- Espacement des lettres
- Espacement des éléments de la liste
- Indentation des éléments de la liste
- Type de liste
- Type de style de liste

Vous pouvez définir le **type de liste** comme étant numéroté ou à puces. Le **type de style de liste** permet de personnaliser davantage le style de vos listes. Par exemple, vous pouvez définir les types de liste pour qu’ils soient toujours sous forme de listes à puces et que chaque puce soit un carré.  

![][10]

## Style de bouton

Dans la section **Style du bouton**, vous pouvez modifier les styles par défaut suivants pour le bouton :
- Couleur d’arrière-plan
- Taille de police
- Couleur de police
- Rayon de bordure
- Couleur de bordure
- Poids de bordure
- Marge intérieure du bouton

![][12]

Comme pour toutes les autres sections de style, vous pouvez ajuster le style du bloc en modifiant les valeurs **Padding Top**, **Padding Right**, **Padding Bottom** et **Padding Left**.

## Largeur du modèle d'e-mail

Grâce à la largeur du modèle d'e-mail, vous pouvez ajuster et définir une largeur pour assurer la cohérence de vos campagnes d'e-mail. 

![][13]

## Largeur du bloc de contenu

Vous pouvez également définir la largeur du bloc de contenu dans l'éditeur par glisser-déposer de l'e-mail. Nous vous recommandons de faire correspondre la largeur du bloc de contenu à celle du modèle d'e-mail.

![][14]


[1]: {% image_buster /assets/img_archive/dnd_global_style_settings.png %}
[2]: {% image_buster /assets/img_archive/dnd_basic_styling.png %}
[3]: {% image_buster /assets/img_archive/dnd_custom_font.png %}
[5]: {% image_buster /assets/img_archive/dnd_button_styling.png %}
[6]: {% image_buster /assets/img_archive/dnd_heading_styling.png %}
[7]: {% image_buster /assets/img_archive/dnd_paragraph_styling.png %}
[9]: {% image_buster /assets/img_archive/dnd_title_styling.png %}
[10]: {% image_buster /assets/img_archive/dnd_list_styling.png %}
[11]: {% image_buster /assets/img_archive/dnd_fallbacks.png %}
[12]: {% image_buster /assets/img_archive/dnd_button_styling.png %}
[13]: {% image_buster /assets/img_archive/dnd_email_template_width.png %}
[14]: {% image_buster /assets/img_archive/dnd_content_block_width.png %}
[8]: {{site.baseurl}}/user_guide/message_building_by_ (en anglais)channel/email/drag_and_drop/dnd_editor_blocks
