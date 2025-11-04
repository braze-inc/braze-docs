---
nav_title: "Paramètres de style global de l'e-mail"
article_title: "Paramètres de style global de l'e-mail"
alias: "/dnd/global_style_settings/"
channel: email
page_order: 3
description: "Cet article de référence explique comment définir des paramètres globaux de style d'e-mail dans l'éditeur glisser-déposer pour vos campagnes et vos Canevas."
tool: 
  - Campaigns
  - Canvas
---

# Paramètres de style globaux de l'e-mail

> Grâce aux paramètres de style globaux, vous pouvez personnaliser l'apparence de vos campagnes d'e-mail et de vos toiles. Vous pouvez ajouter et personnaliser un thème par défaut pour votre éditeur par glisser-déposer. Il s'agit notamment de modifier vos styles pour les titres des e-mails, le texte, les boutons, etc. L'utilisation d'une combinaison de ces paramètres peut contribuer à créer un aspect cohérent dans l'ensemble de vos envois de messages e-mail.

Pour modifier vos paramètres de style globaux, allez dans **Paramètres** > **Préférences e-mail** > **Préférences e-mail glisser-déposer**. Après avoir modifié les styles dans l'éditeur par glisser-déposer de l'e-mail, sélectionnez **Enregistrer.** Pour personnaliser davantage vos campagnes e-mail et Canvases, découvrez comment vous pouvez intégrer des [blocs d'éditeur par glisser-déposer]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks).

!section Paramètres de style global de l'e-mail dans l'onglet Paramètres de l'éditeur par glisser-déposer.]({% image_buster /assets/img_archive/dnd_global_style_settings.png %})

{% alert note %}
Les mises à jour apportées aux paramètres de style globaux s'appliqueront à toutes les futures campagnes d'e-mail et Canvas.
{% endalert %} 

## Style de base 

Pour le **style de base**, vous pouvez définir vos couleurs d'arrière-plan par défaut pour l'e-mail et le contenu de vos campagnes d'e-mail et de vos canevas. Vous pouvez également sélectionner une police par défaut, ajouter une police personnalisée et modifier les couleurs des liens.

Les options de style de base comprennent des options permettant de modifier les couleurs d'arrière-plan de l'e-mail et du contenu, le nom de la police par défaut et la couleur du lien par défaut.]({% image_buster /assets/img_archive/dnd_basic_styling.png %}) 

## Police personnalisée

Avec les polices personnalisées, vous pouvez ajouter manuellement une police web pour assurer la cohérence de la marque sur les différentes plateformes d'e-mail. Vous pouvez ajouter une police personnalisée pour chaque section de style personnalisé.

### Exigences

Avant d'ajouter une police personnalisée, vérifiez que le fichier de police personnalisée répond aux exigences suivantes :

- CORS doit être activé sur le serveur qui fournit le fichier de polices personnalisé. Cette fonction est généralement gérée par votre équipe informatique. 
  - Le fichier de police personnalisé doit comporter l'en-tête : `Access-Control-Allow-Origin: *`
- L'URL du fichier doit pointer vers un fichier CSS (pas WOFF ou OTF).
- Le nom de la police personnalisée doit correspondre au nom de la face de la police dans le fichier CSS.

Notez que le fournisseur de polices personnalisées peut collecter des données personnelles auprès de vos destinataires. Vous devez consulter les politiques de votre fournisseur de polices de caractères avant de les utiliser.

### Ajout d'une police personnalisée

Pour ajouter une police personnalisée, procédez comme suit :

1. Dans la section **Nom de la police par défaut** du **style personnalisé**, sélectionnez **Ajouter une police personnalisée**.
2. Dans le champ **Nom de la police**, saisissez le même nom de police que celui qui apparaît dans votre fichier source de polices personnalisées. Veillez à ce que ce nom soit écrit en majuscules et à ce que l'espacement soit correct.
3. Saisissez l'URL correspondant dans le champ **URL de la police**.
4. Vérifiez que l'aperçu affiche votre police personnalisée.
5. Sélectionnez **Enregistrer** pour utiliser la police personnalisée comme police par défaut pour vos e-mails. 

{% alert important %}
Gmail ne prenant pas en charge les polices personnalisées, il se peut que votre police personnalisée s'affiche en tant que police système par défaut. Pour les autres plateformes d'e-mail, vérifiez que votre police personnalisée s'affiche correctement avant d'envoyer votre message.
{% endalert %}

Pour utiliser d'autres polices personnalisées dans vos campagnes d'e-mail, vous pouvez créer un [modèle d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/) ou des [blocs de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/) qui incluent la police personnalisée. Par exemple, vous pouvez créer un modèle d'e-mail spécifique conçu avec des polices personnalisées festives adaptées à votre thème de vente. Veillez à vérifier que votre choix de police est toujours sûr pour le web et qu'il est pris en charge par vos plateformes d'e-mail.

### Police de secours

Les polices de secours sont utilisées pour le titre, l'en-tête et le corps du texte lorsque votre choix de police par défaut n'est pas pris en charge par le fournisseur de la boîte de réception ou le système d'exploitation. Par défaut, Braze définit automatiquement Arial comme police de secours lorsque les paramètres de style globaux sont enregistrés. Vous avez également la possibilité d'ajouter les options serif ou sans serif à votre famille de polices par défaut.

Exemple de "Arial" comme police de secours avec "Sans-serif" comme famille de police.]({% image_buster /assets/img_archive/dnd_fallbacks.png %})

Vous pouvez ajouter jusqu'à 17 polices de remplacement. La première police de secours sélectionnée sera celle qui sera essayée en premier. La police de remplacement ne sera appliquée que pour les modèles, les campagnes d'e-mail et les composants Canvas nouvellement créés. La police de remplacement n'est pas automatiquement définie pour les messages qui ont été créés avant que la police de remplacement ne soit spécifiée. Nous vous recommandons vivement de choisir des polices de remplacement similaires à votre envoi de messages e-mail afin de maintenir la cohérence de votre image de marque.

## Titre stylistique

Ici, vous pouvez ajuster les styles des titres de vos e-mails en modifiant la taille de la police, la couleur de la police et l'alignement du texte. Ceci s'applique à l'en-tête principal et à l'en-tête secondaire. 

\![Titre Paramètres de style pour un en-tête principal et un en-tête secondaire alignés au centre.]({% image_buster /assets/img_archive/dnd_title_styling.png %})

En option, vous pouvez remplacer le style par défaut du thème de votre éditeur par glisser-déposer. Sélectionnez **Remplacer le style par défaut** pour appliquer le style de titre de votre choix. Il peut s'agir d'une police de caractères et d'une couleur de lien différentes.

## Style de paragraphe

Pour définir un style de paragraphe par défaut, accédez à la section **Style de paragraphe**, entrez la **taille de la police** et sélectionnez **Couleur de police** pour choisir une couleur de police. Vous pouvez également ajuster le style du bloc pour le corps du texte en modifiant les valeurs **Padding Top**, **Padding Right**, **Padding Bottom** et **Padding Left**. Cela s'applique à l'espacement autour des quatre zones entourant le bloc de paragraphe.

\![Paragraphe Paramètres de style pour le texte avec la police 14pt.]({% image_buster /assets/img_archive/dnd_paragraph_styling.png %})

## Style de la liste

Lorsque vous ajoutez des listes à votre envoi de messages, la section **Style de liste** permet de créer une cohérence dans la manière dont vos listes sont stylisées. Il s'agit notamment de détails tels que 

- Taille de la police
- Couleur de la police
- Poids de la police
- Hauteur de la ligne
- Alignement
- Sens du texte
- Espacement des lettres
- Espacement des éléments de la liste
- Indentation des éléments de la liste
- Type de liste
- Type de style de liste

Vous pouvez définir le **type de liste** comme étant numéroté ou à puces. Le **type de style de liste** permet de personnaliser davantage le style de vos listes. Par exemple, vous pouvez faire en sorte que les listes soient toujours à puces et que chaque puce soit un carré.  

\![Paramètres de style de liste pour une liste à puces.]({% image_buster /assets/img_archive/dnd_list_styling.png %})

## Style des boutons

Dans la section **Style du bouton**, vous pouvez modifier les styles par défaut suivants pour le bouton :
- Couleur d'arrière-plan
- Taille de la police
- Couleur de la police
- Rayon de la bordure
- Couleur de la bordure
- Poids de la bordure
- Rembourrage des boutons

!Bouton Paramètres de style pour un bouton rectangulaire avec un fond bleu.]({% image_buster /assets/img_archive/dnd_button_styling.png %})

Comme pour toutes les autres sections de style, vous pouvez ajuster le style du bloc en modifiant les valeurs **Padding Top**, **Padding Right**, **Padding Bottom** et **Padding Left**.

## Largeur du modèle d'e-mail

Grâce à la largeur du modèle d'e-mail, vous pouvez ajuster et définir une largeur pour assurer la cohérence de vos campagnes d'e-mail. 

\![La largeur du modèle d'e-mail est fixée à 600px.]({% image_buster /assets/img_archive/dnd_email_template_width.png %})

## Largeur du bloc de contenu

Ce paramètre sera préconfiguré pour tous les blocs de contenu à venir. Les blocs de contenu existants ne seront pas mis à jour. Vous pouvez fixer tous les blocs de contenu à 100 %, en respectant la largeur à laquelle un bloc de contenu est inséré, ou définir une valeur spécifique en pixels.

Nous vous recommandons de faire correspondre la largeur du bloc de contenu à celle du modèle d'e-mail.

\![La largeur du bloc contenu est fixée à 600px.]({% image_buster /assets/img_archive/dnd_content_block_width_update.png %})
