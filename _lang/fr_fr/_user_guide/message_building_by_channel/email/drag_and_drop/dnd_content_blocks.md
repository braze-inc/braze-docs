---
nav_title: Blocs de contenu
article_title: "Blocs de contenu de l'éditeur glisser-déposer"
alias: "/dnd/content_blocks/"
channel: email
page_order: 2
description: "Cet article de référence explique comment créer et utiliser des blocs de contenu dans l'éditeur par glisser-déposer."
tool: Media

---

# Editeur glisser-déposer par blocs de contenu

> Les blocs de contenu utilisés exclusivement dans l'éditeur par glisser-déposer ont des fonctionnalités similaires à celles des [blocs de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) utilisés sur les différents canaux. Ils constituent un emplacement/localisation d'informations auxquelles il est possible de se référer dans diverses campagnes d'e-mailing. Il peut s'agir de regrouper des en-têtes d'e-mail, des appels promotionnels, et bien d'autres choses encore, le tout dans une seule ligne réutilisable.

{% alert note %}
Les blocs de contenu glissés-déposés ne peuvent être utilisés que dans les campagnes de communication par e-mail et les messages e-mail dans Canvas.
{% endalert %}

## Création d'un bloc de contenu

Pour créer un bloc de contenu, procédez comme suit :

{% multi_lang_include create_content_block.md location="dnd" %}

{% alert important %}
Chaque bloc de contenu glissé-déposé est limité à une ligne. Toutefois, vous pouvez utiliser des blocs éditeur par glisser-déposer pour créer et personnaliser le bloc de contenu en fonction de votre message e-mail.
{% endalert %}

## Utilisation d'un bloc de contenu

Il existe deux façons d'ajouter le bloc de contenu à votre e-mail : à l'aide de l'éditeur ou à l'aide de Liquid.

### Utiliser l'éditeur pour ajouter un bloc de contenu

Pour ajouter un bloc de contenu dans l'éditeur, procédez comme suit :

1. Allez dans l'onglet **Lignes de** l'éditeur et sélectionnez **Blocs de contenu**. 
2. Glissez-déposez votre bloc de contenu dans l'éditeur par e-mail. 
3. (Facultatif) Ajustez la largeur de votre bloc de contenu en sélectionnant le bouton dans le menu de navigation. La largeur par défaut est de 100 % si elle n'est pas spécifiée dans les paramètres de style globaux de votre e-mail ; dans le cas contraire, les paramètres globaux seront respectés. <br><br>\![Une flèche double face avec une option permettant de modifier la largeur.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }<br><br>

Après avoir ajouté le bloc de contenu à l'éditeur d'e-mails, vous pouvez y apporter des modifications qui n'affecteront pas le bloc de contenu original que vous avez créé dans **Modèles et médias & **. En effet, les blocs de contenu ajoutés par glisser-déposer ne sont pas liés au bloc de contenu d'origine. Pour afficher les modifications apportées au bloc de contenu d'origine, faites-le glisser à nouveau dans l'éditeur d'e-mails. 

Un désalignement dans l'éditeur par glisser-déposer peut se produire lorsque plusieurs blocs de contenu sont ajoutés à un seul bloc de rangée. Essayez d'utiliser des blocs de contenu séparés pour maintenir l'alignement de votre contenu au niveau de la ligne.

### Utiliser Liquid pour ajouter un bloc de contenu

Pour ajouter un bloc de contenu à l'aide de Liquid, procédez comme suit :

1. Accédez à votre campagne d'e-mail et sélectionnez **Modifier le corps de l'e-mail**. 
2. Cliquez sur <i class="fas fa-plus"></i> **Personnalisation**.
3. Localisez l'onglet **Ajouter une personnalisation** et sélectionnez **Blocs de contenu** dans le menu déroulant **Type de personnalisation**.
4. Sélectionnez le nom de votre bloc de contenu dans le champ **Attribut**. Le champ de l'extrait de code Liquid s'enrichit de votre étiquette Liquid du bloc de contenu. 
5. Copiez et collez l'extrait de code liquide dans un bloc éditeur de texte. <br>!L'onglet Ajouter une personnalisation avec des options.]({% image_buster /assets/img_archive/dnd_content_block_personalization.png %}){: style="max-width:30%;"}

Lorsque vous prévisualisez votre envoi de messages e-mail, l'extrait liquid s'affiche sous la forme du bloc contenu de l'éditeur glisser-déposer. 

{% alert important %}
Lorsqu'un bloc de contenu est ajouté dans l'éditeur d'e-mails avec Liquid, ce bloc de contenu est lié au bloc de contenu original créé dans **Modèles et médias & **. Cela signifie que le bloc de contenu sera mis à jour pour refléter toute modification apportée au modèle de bloc de contenu d'origine.
{% endalert %}

## Mise à jour des blocs de contenu

Pour mettre à jour un bloc de contenu existant, vous pouvez soit modifier le bloc de contenu d'origine à partir de la page **Blocs de contenu**, soit copier le code HTML du message d'origine dans votre nouveau message. Les mises à jour d'un modèle de bloc de contenu seront actualisées dans tous les messages e-mail dans lesquels le bloc de contenu est ajouté via Liquid.

Pour archiver un bloc de contenu, allez dans **Modèles** > **Blocs de contenu**, sélectionnez l'icône d'ellipse verticale <i class="fas fa-ellipsis-vertical"></i> pour le bloc de contenu et cliquez sur **Archiver**. Lorsque vous archivez un bloc de contenu, vos messages comprendront toujours le contenu du bloc archivé. Cependant, les blocs de contenu archivés sont en lecture seule, il faut donc désarchiver le bloc de contenu avant de le modifier. 

