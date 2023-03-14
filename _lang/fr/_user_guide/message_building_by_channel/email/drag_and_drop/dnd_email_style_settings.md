---
nav_title: Paramètres de style globaux des e-mails
article_title: Paramètres de style globaux des e-mails
alias: "/dnd/global_style_settings/"
channel: email
page_order: 3
description: "Le présent article de référence explique comment définir des paramètres de style globaux des e-mails pour vos campagnes et Canvas."
tool: 
  - Campagnes
  - Canvas
---

# Paramètres de l’éditeur d’e-mail Drag & Drop

Avec des paramètres de style globaux, vous pouvez personnaliser l’apparence de vos campagnes par e-mail et de vos Canvas. Vous pouvez ajouter et personnaliser un thème par défaut pour votre éditeur Drag & Drop. Cela inclut la modification de vos styles pour les titres de courrier électronique, le texte, les boutons, etc.

Pour modifier vos paramètres de style globaux, allez sur **Manage Settings (Gérer les paramètres)** et sélectionnez l’onglet **Email Settings (Paramètres d’e-mail)**. Sélectionnez les **paramètres de l’éditeur d’e-mail Drag & Drop**.

![][1]

{% alert note %}
Les mises à jour apportées aux paramètres de style globaux s’appliqueront à toutes les campagnes par e-mail et à tous les Canvas futurs. 
{% endalert %} 

## Style basique 

Pour le **style basique**, vous pouvez définir vos couleurs par défaut d'arrière-plan des e-mails et du contenu pour vos campagnes par e-mail et vos Canvas. Vous pouvez également sélectionner une police par défaut, ajouter une police personnalisée et modifier les couleurs de lien.

![Options de style de base qui comprennent des options pour modifier les couleurs d’arrière-plan et de contenu de l’e-mail, le nom de police par défaut et la couleur du lien par défaut.][2] 

## Police personnalisée

Avec des polices personnalisées, vous pouvez ajouter manuellement une police Internet pour garder la cohérence de votre marque entre plusieurs plateformes d’e-mails. Vous pouvez ajouter une police personnalisée par section. 

Pour ajouter une police personnalisée :

1. Cliquez sur **Add a custom font (Ajouter une police personnalisée)** sous le **Default Font Name (Nom de police par défaut)** de la section de style.
2. Saisissez le nom de la police et l’URL du fichier source. Cette URL de fichier source doit pointer vers une feuille de style telle qu’un fichier CSS. Dans le champ **Font Name (Nom de police)**, saisissez le même nom de police que celui dans votre fichier source de polices personnalisées. Assurez-vous que le nom est en majuscules et correctement espacé. Saisissez l’**URL de police** correspondante. 
3. Vérifiez que l’aperçu affiche votre police personnalisée avant d’enregistrer. 
4. Cliquez sur **Save (Enregistrer)** pour utiliser la police personnalisée comme police d’e-mail par défaut. 

{% alert important %}
Gmail ne prend pas en charge les polices personnalisées, de sorte que votre police personnalisée peut s’afficher comme une police système par défaut. Pour les autres plateformes d’e-mail, vérifiez que votre police personnalisée s’affiche correctement avant d’envoyer votre e-mail.
{% endalert %}

Pour utiliser des polices personnalisées alternatives dans vos campagnes par e-mail, vous avez la possibilité de créer un [modèle d’e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/) ou des [blocs de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/). Assurez-vous de vérifier que votre choix de police correspond à une utilisation sur Internet et soit pris en charge par vos plateformes d’e-mails. 

### Police de secours

Les polices de secours sont utilisées pour le titre, l’en-tête et le corps du texte quand la police que vous avez choisie par défaut n’est pas prise en charge par votre fournisseur de boîte de réception ou votre système d’exploitation. Braze définit automatiquement Arial comme police de secours par défaut si les paramètres de style globaux sont conservés. Vous avez également la possibilité d’ajouter les options d’empattement typographique ou sans empattement pour votre famille de police par défaut.

![][11]

Vous pouvez ajouter jusqu’à 17 polices de secours. La première police de secours sélectionnée sera celle qui sera tentée en premier. La police de secours ne sera appliquée qu’aux modèles, aux campagnes par e-mail et aux composants Canvas nouvellement créés. La police de secours n’est pas automatiquement définie pour les messages qui ont été créés avant qu’elle ne soit spécifiée. Nous vous recommandons fortement de sélectionner des polices de secours qui sont similaires à votre envoi de messages e-mail pour maintenir une forme de cohérence au sein de votre marque.

## Style de titre

Ici, vous pouvez ajuster les styles de vos titres d’e-mail en modifiant la taille de police, la couleur de police et l’alignement du texte. Cela s’applique à l’en-tête principal et à l’en-tête secondaire. 

![][9]

Vous pouvez également remplacer le style par défaut du thème de votre éditeur Drag & Drop. Cliquez sur **Override default style (Remplacer le style par défaut)** pour appliquer votre style de titre. Cela peut inclure la définition d’une police et d’une couleur de lien différentes.

## Style de paragraphe

Pour définir un style de paragraphe par défaut, accédez au **Paragraph Styling (Style de paragraphe)**, entrez dans **Font Size (Taille de la police)** et sélectionnez **Font Color (Couleur de la police)** pour choisir une couleur de police. Vous pouvez également ajuster le style de bloc pour le texte du corps en modifiant les valeurs **Padding Top (Marge intérieure supérieure)**, **Padding Right (Marge intérieure droite)**, **Padding Bottom (Marge intérieure inférieure)** et **Padding Left (Marge intérieure gauche)**. Cela s’appliquera à l’espacement autour des quatre zones entourant le bloc du paragraphe.

![][7]

## Style de liste

Lorsque vous ajoutez des listes à vos communications, la section **List Styling (Style de liste)** crée une cohérence dans la façon dont vos listes sont mises en page. Cela inclut des détails tels que la taille de la police, la couleur de la police, l’épaisseur de la ligne, l’alignement, la direction du texte, l’espacement des éléments de liste et leur indentation.

Ici, vous pouvez également définir le **List Type (Type de liste)** comme étant des listes numérotées ou à puces. Le **List Style Type (Type de style de liste)** offre une personnalisation supplémentaire concernant le style de vos listes. Par exemple, vous pouvez définir les types de liste pour qu’ils soient toujours sous forme de listes à puces et que chaque puce soit un carré.  

![][10]

## Style de bouton

Dans la section **Button Styling (Style de bouton)** vous pouvez modifier les styles de bouton par défaut suivants :
- Couleur d’arrière-plan
- Taille de police
- Couleur de police
- Rayon de bordure
- Couleur de bordure
- Poids de bordure
- Marge intérieure du bouton

![][12]

Comme pour toutes les autres sections de style, vous pouvez ajuster le style de bloc pour le texte du corps en modifiant les valeurs **Padding Top (Marge intérieure supérieure)**, **Padding Right (Marge intérieure droite)**, **Padding Bottom (Marge intérieure inférieure)** et **Padding Left (Marge intérieure gauche)**.

Après avoir modifié les styles dans l’éditeur d’e-mail Drag & Drop, cliquez sur **Save (Enregistrer)**. Pour personnaliser davantage vos campagnes par e-mail et vos Canvas, consultez les [blocs de l’éditeur Drag & Drop][8].

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
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks