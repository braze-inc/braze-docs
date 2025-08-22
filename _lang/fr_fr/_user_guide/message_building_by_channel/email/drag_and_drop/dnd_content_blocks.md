---
nav_title: Blocs de contenu
article_title: Éditeur de glisser-déposer Blocs de contenu
alias: "/dnd/content_blocks/"
channel: email
page_order: 2
description: "Cet article de référence explique comment créer et utiliser des blocs de contenu dans l'éditeur par glisser-déposer."
tool: Media

---

# Éditeur par glisser-déposer Blocs de contenu

> Les blocs de contenu utilisés exclusivement dans l'éditeur de glisser-déposer sont similaires en termes de fonctionnalité aux [blocs de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) utilisés dans différents canaux. Ils servent d’emplacement centralisé pour la conservation d’informations qui peuvent être référencées dans diverses campagnes par e-mail. Il peut s’agir de regrouper des en-têtes de courriels, des pointeurs promotionnels et plus encore, le tout sur une seule ligne réutilisable.

{% alert note %}
Les blocs de contenu par glisser-déposer sont uniquement disponibles pour les campagnes par e-mail et les e-mails dans Canvas.
{% endalert %}

## Création d’un bloc de contenu

Pour créer un bloc de contenu, procédez comme suit :

{% multi_lang_include create_content_block.md location="dnd" %}

{% alert important %}
Chaque bloc de contenu glisser-déposer est limité à une seule ligne. Cependant, vous pouvez utiliser des blocs d'éditeur par glisser-déposer pour créer et personnaliser le bloc de contenu afin de répondre à vos besoins en matière de messagerie électronique.
{% endalert %}

## Utilisation d’un bloc de contenu

Il existe deux façons d'ajouter le bloc de contenu à votre e-mail : en utilisant l'éditeur ou en utilisant Liquid.

### Utiliser l'éditeur pour ajouter un bloc de contenu

Pour ajouter un bloc de contenu dans l'éditeur, procédez comme suit :

1. Allez à l'onglet **Rows** dans l'éditeur et sélectionnez **Content Blocks**. 
2. Faites glisser et déposez votre bloc de contenu dans l'éditeur d'e-mail. 
3. (Facultatif) Ajustez la largeur de votre bloc de contenu en sélectionnant le bouton dans le menu de navigation. La largeur par défaut est de 100 %. <br><br>![Une flèche double face avec une option permettant de modifier la largeur.]({% image_buster /assets/img_archive/content_block_width.png %}){: style="max-width:30%;" }<br><br>

Après avoir ajouté le bloc de contenu à l'éditeur d'e-mails, vous pouvez y apporter des modifications qui n'affecteront pas le bloc de contenu original que vous avez créé dans **Modèles et médias.** En effet, les blocs de contenu ajoutés par glisser-déposer ne sont pas liés au bloc de contenu d'origine. Pour voir les modifications apportées au bloc de contenu original, faites-le glisser à nouveau dans l'éditeur d'e-mails. 

Un désalignement dans l'éditeur de glisser-déposer peut se produire lorsque plusieurs blocs de contenu sont ajoutés à un seul bloc de ligne. Essayez d'utiliser des blocs de lignes séparés pour maintenir l'alignement de votre contenu au niveau de la ligne.

### Utiliser Liquid pour ajouter un bloc de contenu

Pour ajouter un bloc de contenu en utilisant Liquid, procédez comme suit :

1. Accédez à votre campagne par e-mail et sélectionnez **Modifier le corps de l'e-mail**. 
2. Cliquez <i class="fas fa-plus"></i> **Personnalisation**.
3. Localisez l'onglet **Ajouter une personnalisation** et sélectionnez **Blocs de contenu** dans le menu déroulant **Type de personnalisation**.
4. Sélectionnez le nom de votre bloc de contenu dans le champ **Attribut**. Le champ d’extrait de code Liquid se remplira avec votre balise Liquid du bloc de contenu. 
5. Copiez et collez l'extrait de code Liquid dans un bloc d'éditeur de texte. <br>![L'onglet Ajouter une personnalisation avec des options.]({% image_buster /assets/img_archive/dnd_content_block_personalization.png %}){: style="max-width:30%;"}

Lorsque vous prévisualisez votre messagerie électronique, l'extrait Liquid s'affichera comme le bloc de contenu de l'éditeur par glisser-déposer. 

{% alert important %}
Lorsqu'un bloc de contenu est ajouté dans l'éditeur d'e-mails avec Liquid, ce bloc de contenu est lié au bloc de contenu original créé dans **Modèles et médias.** Ceci signifie que le bloc de contenu sera mis à jour pour afficher toutes les modifications effectuées sur le modèle de bloc de contenu d’origine.
{% endalert %}

## Mise à jour des blocs de contenu

Pour mettre à jour un bloc de contenu existant, vous pouvez soit modifier le bloc de contenu original depuis la page **Blocs de contenu**, soit copier le HTML du message original dans votre nouveau message. Les mises à jour d'un modèle de bloc de contenu seront répercutées dans tous les e-mails où le bloc de contenu est ajouté via Liquid.

Pour archiver un bloc de contenu, allez dans **Modèles** > **Blocs de contenu**, sélectionnez l'icône <i class="fas fa-ellipsis-vertical"></i> de l'ellipse verticale pour le bloc de contenu, et cliquez sur **Archiver**. Lorsque vous archivez un bloc de contenu, vos messages incluront toujours le contenu du bloc archivé. Cependant, les blocs de contenu archivés sont en lecture seule. Par conséquent, sortez le bloc de contenu des archives avant de le modifier. 

