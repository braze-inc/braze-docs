---
nav_title: Création d’un message In-App
article_title: "Créer un message in-app en glisser-déposer"
description: "Cet article de référence explique comment créer un message in-app avec l’éditeur Drag & Drop, les conditions préalables, les informations créatives, etc."
alias: "/create_dnd_iam/"
---

# Créer un message in-app en glisser-déposer

> Avec l’éditeur Drag & Drop, vous pouvez créer des messages in-app entièrement personnalisés dans les campagnes ou les Canvas à l’aide de l’expérience de modification en glisser-déposer.

Si vous souhaitez utiliser vos modèles HTML personnalisés existants ou les modèles créés par un tiers, ils doivent être recréés dans l’éditeur Drag & Drop.

Vous ne savez pas si votre message in-app doit être envoyé via une campagne ou un [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/) ? Les campagnes sont mieux adaptées aux campagnes de communication simples et uniques, tandis que les Canvas sont mieux adaptés aux parcours client en plusieurs étapes. Une fois que vous avez choisi où créer votre message, examinons les étapes pour créer un message in-app en glisser-déposer !

## Conditions préalables

Les messages créés en utilisant l’éditeur Drag & Drop ne peuvent être envoyés qu’aux utilisateurs utilisant les versions SDK suivantes au minimum :

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

Si un utilisateur n’a pas mis à jour son application (c’est-à-dire s’il est sur une version du SDK plus ancienne), il ne recevra pas le message in-app.

**Exigences supplémentaires**<br>
- Pour le SDK Web, l’option d’initialisation [`allowUserSuppliedJavascript`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) doit être réglée sur `true`. L’option `enableHtmlInAppMessages` permettra aussi à ces messages de fonctionner, mais elle est obsolète et devrait être mise à jour vers `allowUserSuppliedJavascript`.
- Si vous utilisez Google Tag Manager, vous devez activer « Autoriser les messages in-App HTML » dans la configuration GTM.

## Étape 1 : Créer un message in-app

Créez un nouveau message in-app ou une étape Canvas, puis sélectionnez l’**Éditeur Drag & Drop** en tant qu’expérience d’édition.

## Étape 2 : Sélectionnez votre modèle

![]({% image_buster /assets/img_archive/dnd_iam_select_template.png %}){: style="float:right;max-width:25%;margin-left:15px;max-width:40%"}

Après avoir sélectionné l’éditeur Drag & Drop comme expérience de modification, vous pouvez choisir de :

- Utiliser un modèle de modal de base Braze
- Commencer par un modèle de modal vide

Cliquez sur **Build message (Créer un message)** pour commencer à concevoir votre message in-app dans l’éditeur Drag & Drop !

## Étape 3 : Créer et concevoir votre message in-app

L’expérience de modification en glisser-déposer est divisée en deux sections : **Créer** puis **Aperçu et test**.

![]({% image_buster /assets/img_archive/dnd_iam_message_styles.png %}){: style="float:right;max-width:25%;margin-left:15px;max-width:30%"}

### Définir les styles au niveau du message

Vous pouvez définir certains styles pour qu’ils soient appliqués à tous les blocs pertinents de votre message in-app à partir de l’onglet **Message Styles (Styles de message)**. Les styles définis dans cette section sont utilisés partout dans votre message sauf aux endroits où vous les remplacez pour un bloc spécifique. Pour une expérience de conception plus facile, nous vous recommandons de configurer des styles au niveau message avant de personnaliser les styles au niveau des blocs.

Vous pouvez à tout moment revenir à l’onglet **Message Styles (Styles de message)** :

- Cliquez sur le bouton de fermeture « X » sur les propriétés d’un bloc individuel
- Sélectionnez le conteneur du message, le bouton de fermeture « X » du message ou l’arrière-plan de l’éditeur

#### Ajouter une police personnalisée

Pour ajouter une police personnalisée :

1. Allez dans la section **Content (Contenu)** de l’onglet **Message Styles (Styles de message)**.
2. Cliquez sur **Add custom font (Ajouter une police personnalisée)**.
3. Chargez votre police en utilisant la bibliothèque média. 

Nous acceptons les types de fichiers suivants pour les polices : `.ttf`, `.woff`, `.otf`, `.woff2`. Pour plus d’informations, consultez les [fichiers d’actifs]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/html_in-app_messages#asset-files).

Vous pouvez ajouter plusieurs variations d’une famille de police étant donné que les options de style peuvent ne pas être disponibles pour les polices personnalisées. Nous ne prenons pas actuellement en charge l’ajout de polices par URL.

{% alert note %}
La police au niveau du message ne s’appliquera qu’au message en cours et à tout message dupliqué, mais pas aux modèles suivants.
{% endalert %}

### Glisser-déposer des composants de messages in-app

![]({% image_buster /assets/img_archive/dnd_iam_create.gif %})

L’éditeur Drag & Drop utilise deux composants principaux pour faciliter et accélérer la composition des messages in-app : **lignes** et **blocs**. Tous les blocs doivent être placés dans une ligne.

#### Lignes

Les lignes sont des unités structurelles qui définissent la composition horizontale d’une section du message en utilisant des cellules.

![]({% image_buster /assets/img_archive/dnd_iam_rows.png %}){: style="max-width:40%"}

Lorsque vous sélectionnez une ligne, vous pouvez ajouter ou supprimer autant de colonnes que nécessaire de la section de **personnalisation des colonnes** pour disposer plusieurs éléments de contenu côte à côte. 

Vous pouvez également faire glisser pour ajuster la taille des colonnes existantes.

![]({% image_buster /assets/img_archive/dnd_iam_column_customization.gif %}){: style="max-width:40%"}

En tant que bonne pratique, formatez vos propriétés de ligne et de colonne avant de formater l’un des blocs à l’intérieur des lignes. Il existe de nombreux endroits où vous pouvez ajuster l’espacement et l’alignement. Il est plus facile de le modifier au fur et à mesure en commençant à la base.

#### Blocs

Les blocs représentent divers types de contenu que vous pouvez utiliser dans votre message. Il suffit d’en faire glisser une à l’intérieur d’un segment de ligne existant et elle s’ajustera automatiquement à la largeur de la cellule.

{% alert tip %}
Avant d’ajouter des blocs, configurez les [styles de message](#set-message-level-styles) pour le conteneur de messages, la police, les couleurs et tout autre élément que vous souhaitez personnaliser. Vous pouvez ensuite personnaliser les blocs individuels si nécessaire. Le **bouton Fermer** restera dans la section supérieure de votre message pour que les utilisateurs aient toujours la possibilité de rejeter le modal.
{% endalert %}

![]({% image_buster /assets/img_archive/dnd_iam_editor_blocks.png %}){: style="max-width:40%"}

Chaque bloc possède ses propres paramètres, comme un contrôle granulaire sur la marge intérieure. Le panneau latéral droit passe automatiquement à un panneau de style pour l’élément de contenu sélectionné. Pour plus d’informations, voir [Propriétés du bloc éditeur]({{site.baseurl}}/editor_blocks_dnd_iam/).

Lorsque vous créez votre message in-app, vous pouvez sélectionner un affichage sur mobile, tablette ou ordinateur dans la barre d’outils pour prévisualiser l’affichage de votre message in-app pour vos groupes utilisateur. Cela garantira que votre contenu est réactif et que vous pouvez effectuer tous les ajustements nécessaires au fur et à mesure.

### Détails créatifs

#### Personnaliser l’image d’arrière-plan

Vous pouvez ajouter une image à l’arrière-plan de votre message depuis l’onglet **Message Styles (Styles de message)**. La section de votre message qui peut défiler doit être sélectionnée pour ajouter un arrière-plan à la totalité du message.

{% alert tip %}
Si vous avez des difficultés à sélectionner un bloc donné, vous pouvez utiliser la flèche vers le haut dans la barre d’outils insérée du bloc pour faire passer le point central à chacun des blocs parents.
{% endalert %}

#### Ajout de Liquid

![]({% image_buster /assets/img_archive/dnd_iam_liquid.png %}){: style="float:right;max-width:25%;margin-left:15px"}

Pour ajouter du [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) dans vos messages in-app, sélectionnez<i class="fa-solid fa-circle-plus"></i> **Add Personalization (Ajouter une personnalisation)** depuis la barre d’outils de l’éditeur. Ici, vous pouvez ajouter différents types de personnalisation, tels que des attributs par défaut, des attributs d’appareil, des attributs personnalisés, et bien plus encore !

Ensuite, prenez votre extrait de code Liquid généré et insérez-le dans votre message. Une fois que vous avez terminé de concevoir et de créer votre message in-app, rendez-vous dans **Preview & Test (Aperçu et test)** pour prévisualiser votre message.

#### Réinitialiser les styles par défaut

Les propriétés que vous avez modifiées par rapport à leur style par défaut sont marquées d’un point orange. Pour réinitialiser rapidement une propriété spécifique vers son style par défaut, survolez le champ et sélectionnez **Reset to default (Réinitialiser à la valeur par défaut)**.

![]({% image_buster /assets/img_archive/dnd_iam_reset_styles.gif %}){: style="max-width:45%"}

Vous pouvez également réinitialiser tous les styles pour un élément sélectionné en choisissant le <i class="fas fa-paintbrush" title="Copier ou coller des styles de bouton"></i> à côté du nom du panneau de propriétés et en sélectionnant **Reset to default styles (Réinitialiser les styles par défaut)**.

#### Copier et coller des styles

Après avoir modifié le style d’un élément, vous pouvez copier et coller ce style sur un autre élément. Lorsque vous collez des styles, seules les propriétés pertinentes pour cet élément sont appliquées.

![]({% image_buster /assets/img_archive/dnd_iam_copypaste_styles.png %}){: style="float:right;margin-left:15px;max-width:45%"}

1. Lorsque l’élément est sélectionné, choisissez <i class="fas fa-paintbrush" title="Copier ou coller des styles"></i> à côté du nom du panneau de propriétés (par exemple, si vous avez sélectionné un bouton, à côté de « Propriétés du bouton »).
2. Cliquez sur **Copy Styles (Copier les styles)** et sélectionnez l’élément dans lequel vous souhaitez appliquer le style copié.
3. Sélectionnez <i class="fas fa-paintbrush" title="Copier ou coller des styles"></i> à nouveau et choisissez **Paste styles (Coller les styles)**.

##### Raccourcis clavier

Vous pouvez également utiliser des raccourcis clavier pour copier et coller des styles :

| Action | Mac | Windows |
| --- | --- | --- |
| Copier des styles | <kbd>⌘</kbd> + <kbd>Maj</kbd> + <kbd>c</kbd> | <kbd>Ctrl</kbd> + <kbd>Maj</kbd> + <kbd>c</kbd> |
| Coller des styles | <kbd>⌘</kbd> + <kbd>Maj</kbd> + <kbd>v</kbd> | <kbd>Ctrl</kbd> + <kbd>Maj</kbd> + <kbd>v</kbd> 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Étape 4 : Tester votre message in-app

La section **Preview & Test (Aperçu et test)** vous permet de prévisualiser vos messages in-app sur différents appareils et d’envoyer un message de test au vôtre. Ici, vous pouvez vous assurer que les détails sont alignés sur toutes vos plateformes pour votre campagne de messages in-app en glisser-déposer. Il est très important de toujours tester vos messages in-app avant d’envoyer vos campagnes pour vous aider à visualiser l’apparence de votre message final depuis la perspective de l’utilisateur.

### Aperçu du message en tant qu’utilisateur

{% alert warning %}
Pour envoyer un test à des groupes de test de contenu ou des utilisateurs individuels, les notifications push doivent être activées sur vos appareils de test avant envoi.
{% endalert %}

Vous pouvez prévisualiser les messages dans l’onglet **Preview & Test (Aperçu et test)** comme si vous étiez un utilisateur. Vous pouvez sélectionner un utilisateur spécifique, un utilisateur aléatoire ou créer un utilisateur personnalisé :

- **Utilisateur aléatoire :** Braze sélectionnera de manière aléatoire un utilisateur de la base de données et prévisualisera le message in-app en fonction de ses attributs ou informations sur l’événement.
- **Utilisateur sélectionné :** Vous pouvez sélectionner un utilisateur spécifique en fonction de son adresse e-mail ou external_id. L’aperçu du message in-app s’affichera en fonction des attributs et des informations d’événement de cet utilisateur.
- **Utilisateur personnalisé :** Vous pouvez personnaliser un utilisateur. Braze offre des entrées pour tous les attributs et événements disponibles. Vous pouvez saisir toutes les informations que vous souhaitez voir dans l’aperçu d’e-mail.

### Liste de contrôle des tests

- Avez-vous testé le message sur plusieurs appareils ?
- Les images et les données s’affichent-elles et se comportent-elles comme prévu ?
- Le Liquid fonctionne-t-il comme prévu ? Avez-vous pris en compte une valeur d’attribut par défaut si le Liquid ne renvoie aucune information ?
- Votre texte est-il clair, concis et correct ?
- Vos boutons dirigent-ils l’utilisateur à l’endroit correct ?

## Foire aux questions

#### Pourquoi les clics sur le corps n’apparaissent-ils pas sur ma page d’analytique ?

Les clics sur le corps ne sont pas automatiquement recueillis pour les messages in-app créés avec l’éditeur Drag & Drop. Pour plus de détails, reportez-vous aux journaux de modifications SDK pour [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) et [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100).

#### Puis-je segmenter en fonction des clics de bouton ?

Oui, vous pouvez segmenter en fonction des clics de bouton pour un maximum de deux boutons dans votre message. Pour ce faire, définissez l'**Identifier for Reporting (Identifiant pour les rapports)** pour vos boutons sur « 0 » et « 1 », qui correspondront aux filtres de segmentation « A cliqué sur le bouton 1 du message in-app » et « A cliqué sur le bouton 2 du message in-app ».

#### Puis-je personnaliser mon message in-app en utilisant de l’HTML ou du JavaScript personnalisé ou transférer des messages HTML existants dans l’éditeur ?

Non.

#### Puis-je enregistrer mon message in-app comme modèle après sa création dans ma campagne ou mon Canvas ? **

Non, vous devez recréer le message in-app dans l’éditeur Drag & Drop ou dupliquer un message existant pour le sauvegarder.

#### Comment puis-je créer un message in-app plein écran ou slideup ?

L’éditeur est actuellement limité aux seuls messages modaux.
