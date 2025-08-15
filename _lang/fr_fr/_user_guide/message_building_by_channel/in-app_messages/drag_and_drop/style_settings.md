---
nav_title: Paramètres de style
article_title: "Paramètres du style de message in-app"
description: "Cet article de référence couvre les options de style disponibles lors de la création d'un message in-app avec l'éditeur glisser-déposer."
page_order: 3
---

# Paramètres de style des messages in-app

> L'expérience de modification par glisser-déposer est divisée en deux sections : **Créer** et **Aperçu et test**. Cet article décrit ce que vous devez savoir pour travailler dans l'onglet **Créer** de l'éditeur et suppose que vous avez déjà [créé un message in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/).

![Onglet "styles de messages".]({% image_buster /assets/img_archive/dnd_iam_message_styles.png %}){: style="float:right;max-width:25%;margin-left:15px;max-width:30%"}

## Styles au niveau des messages

Vous pouvez définir certains styles à appliquer à tous les blocs pertinents de votre message in-app à partir de l'onglet **Styles de message.**  Par exemple, vous pouvez personnaliser la police de tout le texte ou la couleur de tous les liens de votre message.

Les styles définis dans cette section sont utilisés partout dans votre message sauf aux endroits où vous les remplacez pour un bloc spécifique. Si votre message comporte [plusieurs pages]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page), vous pouvez également remplacer les styles au niveau du message pour les pages individuelles, à l'exception du type d'affichage et de la largeur maximale. Si vous essayez d'appliquer à la fois un style au niveau de la page et un style au niveau du message, le style au niveau de la page prévaudra sur le style au niveau du message.

Pour une expérience de conception plus facile, nous vous recommandons de configurer des styles au niveau des messages avant de personnaliser les styles au niveau des blocs.

Pour revenir à tout moment à l'onglet **Styles de messages**:

- Cliquez sur le bouton de fermeture « X » sur les propriétés d’un bloc individuel
- Sélectionnez le conteneur du message, le bouton de fermeture « X » du message ou l’arrière-plan de l’éditeur

### Polices personnalisées

Nous acceptons les types de fichiers suivants pour les polices : `.ttf`, `.woff`, `.otf`, et `.woff2`. Pour plus d'informations, voir [Fichiers de ressources]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/html_in-app_messages#asset-files).

Vous pouvez ajouter plusieurs variantes d'une famille de polices, car certaines options de style peuvent ne pas être disponibles pour les polices personnalisées. Nous ne prenons pas actuellement en charge l’ajout de polices par URL.

Pour ajouter une police personnalisée :

1. Accédez à la section **Contenu** de l'onglet **Styles de message**.
2. Cliquez sur **Ajouter une police personnalisée**.
3. Téléchargez votre police à l'aide de la bibliothèque multimédia. 

{% alert note %}
La police au niveau du message ne s’appliquera qu’au message en cours et à tout message dupliqué, mais pas aux modèles suivants.
{% endalert %}

## Composants du message

![GIF montrant la création d'un message in-app promotionnel.]({% image_buster /assets/img_archive/dnd_iam_create.gif %})

L'éditeur par glisser-déposer utilise deux éléments clés pour la composition des messages in-app : les **lignes** et les **blocs**. Tous les blocs doivent être placés dans une ligne.

### Lignes

Les lignes sont des unités structurelles qui définissent la composition horizontale d’une section du message en utilisant des cellules.

![Vous pouvez ajouter des rangées dans votre message in-app.]({% image_buster /assets/img_archive/dnd_iam_rows.png %}){: style="max-width:40%"}

Lorsqu'une ligne est sélectionnée, vous pouvez ajouter ou supprimer le nombre de colonnes dont vous avez besoin dans la section **Personnalisation des colonnes** pour placer différents éléments de contenu côte à côte. 

Vous pouvez également faire glisser pour ajuster la taille des colonnes existantes.

![Ajustement des colonnes à partir de la section "Personnalisation des colonnes".]({% image_buster /assets/img_archive/dnd_iam_column_customization.gif %}){: style="max-width:40%"}

En tant que bonne pratique, formatez vos propriétés de ligne et de colonne avant de formater l’un des blocs à l’intérieur des lignes. Il existe de nombreux endroits où vous pouvez ajuster l’espacement et l’alignement. Il est plus facile de le modifier au fur et à mesure en commençant à la base.

### Blocs

Les blocs représentent divers types de contenu que vous pouvez utiliser dans votre message. Faites-en glisser un à l'intérieur d'un segment de ligne existant et il s'adaptera automatiquement à la largeur de la cellule.

{% alert tip %}
Avant d'ajouter des blocs, définissez des [styles au niveau du message](#set-message-level-styles) pour le contenant du message, la police, les couleurs et tout autre élément que vous souhaitez personnaliser. Vous pouvez ensuite personnaliser les blocs individuels si nécessaire. Le **bouton de fermeture** restera dans la partie supérieure de votre message afin que les utilisateurs aient toujours la possibilité de rejeter le message.
{% endalert %}

![Glisser-déposer des cases à sélectionner.]({% image_buster /assets/img_archive/dnd_iam_editor_blocks.png %}){: style="max-width:40%"}

Chaque bloc possède ses propres paramètres, comme un contrôle granulaire sur la marge intérieure. Le panneau latéral droit passe automatiquement à un panneau de style pour l’élément de contenu sélectionné. Pour plus d'informations, voir [Propriétés du bloc éditeur]({{site.baseurl}}/editor_blocks_dnd_iam/).

Lorsque vous créez votre message in-app, vous pouvez sélectionner un affichage sur mobile, tablette ou ordinateur dans la barre d’outils pour prévisualiser l’affichage de votre message in-app pour vos groupes utilisateur. Cela garantira que votre contenu est réactif et que vous pouvez effectuer tous les ajustements nécessaires au fur et à mesure.

#### Texte de la travée

{% multi_lang_include span_text.md %}

## Détails créatifs

### Plein écran sur les écrans plus larges {#fullscreen}

Sur une tablette ou un navigateur de bureau, un message in-app en plein écran se trouve au centre de l'écran de l'application. Toute modification de la largeur maximale de l'envoi du message en plein écran ne s'appliquera qu'aux appareils de type tablette et ordinateur de bureau. 

![Exemple de message in-app en plein écran.]({% image_buster /assets/img_archive/dnd_iam_fullscreen_example.png %}){: style="border:none"}

### Ajout d'une image de fond

Vous pouvez ajouter une image à l'arrière-plan de votre message à partir de l'onglet **Styles de message.**  

1. Dans la zone du canvas, sélectionnez le conteneur d'arrière-plan. Il s'agit de la partie de votre message que l’on peut faire défiler.
2. Dans l'onglet **Styles de message**, activez l'option **Image d'arrière-plan**.
3. Ajoutez une image à partir de votre bibliothèque multimédia ou saisissez l'URL où votre image est hébergée.

{% alert tip %}
Si vous avez des difficultés à sélectionner un bloc donné, vous pouvez utiliser la flèche vers le haut dans la barre d’outils insérée du bloc pour faire passer le point central à chacun des blocs parents.
{% endalert %}

### Ajout de Liquid

![Icône pour ajouter une personnalisation Liquid.]({% image_buster /assets/img_archive/dnd_iam_liquid.png %}){: style="float:right;max-width:25%;margin-left:15px"}

Pour ajouter du [liquide]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) dans votre message in-app, sélectionnez <i class="fa-solid fa-circle-plus"></i> **Ajouter une personnalisation** dans la barre d'outils de l'éditeur. Ici, vous pouvez ajouter différents types de personnalisation tels que des attributs par défaut, des attributs d'appareil, des attributs personnalisés, etc.

Ensuite, prenez votre extrait de code Liquid généré et insérez-le dans votre message. Après avoir conçu et créé votre message in-app, allez dans **Prévisualisation et test** pour prévisualiser votre message.

### Utiliser le rédacteur basé sur l’IA

Lorsqu'un bloc de texte est sélectionné dans votre message in-app, cliquez sur <i class="fa-solid fa-wand-magic-sparkles" title="Rédacteur d&apos;intelligence artificielle"></i> dans la barre d'outils du bloc pour lancer l'[assistant de rédaction alimenté par l'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). L'assistant de rédaction de l'intelligence artificielle transmet un bref nom ou une brève description de produit à l'outil de génération de communication GPT3 d'OpenAI afin de générer un texte marketing semblable à celui d'un humain pour votre envoi de messages.

{% alert tip %}
Vous pouvez enregistrer quelques clics en surlignant le texte à l'intérieur du bloc avant de cliquer sur l'icône. Le texte en surbrillance sera ajouté à l'outil et une copie sera générée immédiatement.
{% endalert %}

![GIF du rédacteur d'intelligence artificielle.]({% image_buster /assets/img_archive/dnd_iam_ai_copywriter.gif %})

### Réinitialiser les styles par défaut

Les propriétés que vous avez modifiées par rapport à leur style par défaut sont marquées d’un point orange. Pour rétablir le style par défaut d'une propriété spécifique, survolez le champ et sélectionnez **Rétablir la valeur par défaut**.

![Point orange qui rétablit la taille par défaut d'un texte.]({% image_buster /assets/img_archive/dnd_iam_reset_styles.gif %}){: style="max-width:45%"}

Vous pouvez également réinitialiser tous les styles d'un élément sélectionné en sélectionnant le bouton <i class="fas fa-paintbrush" title="Bouton Copier ou coller les styles"></i> à côté du nom du panneau de propriétés et en sélectionnant **Rétablir les styles par défaut**.

### Copier et coller des styles

Après avoir modifié le style d’un élément, vous pouvez copier et coller ce style sur un autre élément. Lorsque vous collez des styles, seules les propriétés pertinentes pour cet élément sont appliquées.

![Menu déroulant avec possibilité de copier les styles.]({% image_buster /assets/img_archive/dnd_iam_copypaste_styles.png %}){: style="float:right;margin-left:15px;max-width:35%"}

1. L'élément étant sélectionné, sélectionnez <i class="fas fa-paintbrush" title="Copier ou coller des styles"></i> à côté du nom du panneau de propriétés (par exemple, si vous avez sélectionné un bouton, à côté de "Propriétés du bouton").
2. Cliquez sur **Copier les styles** et sélectionnez l'élément où vous souhaitez appliquer le style copié.
3. Sélectionnez de nouveau <i class="fas fa-paintbrush" title="Copier ou coller des styles"></i> et choisissez **Coller des styles**.

#### Raccourcis clavier

Vous pouvez également utiliser des raccourcis clavier pour copier et coller des styles :

| Action       | Mac                                            | Windows                                           |
| ------------ | ---------------------------------------------- | ------------------------------------------------- |
| Copier des styles  | <kbd>⌘</kbd> + <kbd>Maj</kbd> + <kbd>c</kbd> | <kbd>Ctrl</kbd> + <kbd>Maj</kbd> + <kbd>c</kbd> |
| Coller des styles | <kbd>⌘</kbd> + <kbd>Maj</kbd> + <kbd>v</kbd> | <kbd>Ctrl</kbd> + <kbd>Maj</kbd> + <kbd>v</kbd> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
