---
nav_title: Blocs de contenu
article_title: Blocs de contenu de l’éditeur Drag & Drop
alias: "/dnd/content_blocks/"
channel: E-mail
page_order: 2
description: "Le présent article de référence explique comment créer et utiliser des blocs de contenu dans l’éditeur Drag & Drop."
tool: Media

---

# Blocs de contenu de l’éditeur Drag & Drop

Les blocs de contenu utilisés exclusivement dans l’éditeur Drag & Drop ont des fonctionnalités similaires aux [blocs de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) utilisés sur différents canaux. Ils servent d’emplacement centralisé pour la conservation d’informations qui peuvent être référencées dans diverses campagnes par e-mail. Il peut s’agir de regrouper des en-têtes de courriels, des pointeurs promotionnelles et plus encore, le tout sur une seule ligne réutilisable.

{% alert important %}
Les blocs de contenu de l’éditeur Drag & Drop sont actuellement en accès anticipé et continuent à évoluer. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé. 
{% endalert %}

## Création d’un bloc de contenu

Pour créer un bloc de contenu, accédez à **Templates & Media** sous la section **Engagement** de votre tableau de bord de Braze. Sélectionnez l’onglet **Content Blocks Library (Bibliothèque de blocs de contenu)** et cliquez sur <i class="fas fa-plus"></i> **Create Content Block (Créer un bloc de contenu)**.

Saisissez un **nom de bloc de contenu** et une description facultative. 

![][1]

{% alert note %}
Les blocs de contenu de l’éditeur Drag & Drop ne peuvent être utilisés que dans les campagnes par e-mail. 
{% endalert %}

Ensuite, sélectionnez **Éditeur Drag & Drop** comme type de bloc de contenu. Cliquez sur **Edit Content Block (Modifier le bloc de contenu)** dans le **Aperçu du bloc de contenu** pour commencer à modifier votre bloc de contenu. 

Nous allons utiliser les [blocs de l’éditeur Drag & Drop]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) pour créer un bloc de contenu de l’éditeur Drag & Drop. Tout d’abord, faites glisser et déposez un bloc de format de l’onglet **Rows (Lignes)** de l’éditeur. Cela déterminera la disposition de votre bloc de contenu. 

{% alert important %}
Chaque bloc de contenu de l’éditeur Drag & Drop est limité à une ligne. Cependant, vous pouvez utiliser les blocs de l’éditeur Drag & Drop pour créer et personnaliser le bloc de contenu pour donner suite à votre e-mail.
{% endalert %}

Vous pouvez également ajouter autant de blocs de contenu de l’éditeur Drag & Drop que nécessaire pour créer vos campagnes par e-mail.

## Utilisation d’un bloc de contenu

![][2]{: style="float:right;max-width:50%;margin-left:15px;margin-top:15px;"}

Pour utiliser le bloc de contenu, accédez à votre campagne par e-mail et sélectionnez **Edit Email Body (Modifier le corps du courriel)**. Cliquez sur le bouton<i class="fas fa-plus"></i> **Personnalisation**. 

Dans l’onglet **Add Personalization (Ajouter une personnalisation)**, sélectionnez les **blocs de contenu** dans le  menu déroulant **Type de personnalisation**. Pour le champ **Attribute (Attribut)**, sélectionnez le nom de votre bloc de contenu. Le champ d’extrait de code Liquid se remplira avec votre balise Liquid du bloc de contenu. Ensuite, copiez et collez l’extrait de code Liquid dans un bloc éditeur. 

Lorsque vous prévisualisez votre e-mail, l’extrait de code Liquid s’affiche comme un bloc de contenu de l’éditeur Drag & Drop. 

## Mise à jour des blocs de contenu

Pour mettre à jour un bloc de contenu existant, vous pouvez modifier le bloc de contenu d’origine situé dans **Templates & Media**, ou copiez le HTML de votre message d’origine vers le nouveau. Notez que si vous choisissez de mettre à jour un bloc de contenu, il sera mis à jour dans tous les e-mails où le bloc de contenu est utilisé.

Pour archiver un bloc de contenu, allez sur **Templates & Media** et sélectionnez l’<i class="fas fa-cog"></i> icône d’engrenage à côté du bloc de contenu sélectionné et cliquez sur **Archive (Archiver)**. Lorsque vous archivez un bloc de contenu, vos messages incluront toujours le contenu du bloc archivé. 


[1]: {% image_buster /assets/img_archive/dnd_content_block_name.png %}
[2]: {% image_buster /assets/img_archive/dnd_content_block_personalization.png %}