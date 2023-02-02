---
nav_title: Création d’un message dans l’application
article_title: "Créer un message in-app en glisser-déposer"
description: "Avec l’éditeur Drag & Drop, vous pouvez créer des messages in-app entièrement personnalisés dans les campagnes ou les Canvas à l’aide de l’expérience de modification en glisser-déposer."
alias: "/create_dnd_iam/"
---

# Créer un message in-app en glisser-déposer

Avec l’éditeur Drag & Drop, vous pouvez créer des messages in-app entièrement personnalisés dans les campagnes ou les Canvas à l’aide de l’expérience de modification en glisser-déposer.

{% alert important %}
Cette fonctionnalité est actuellement disponible en accès anticipé. Veuillez contacter notre conseiller du service de support pour obtenir l’accès.
{% endalert %}

Si vous souhaitez utiliser vos modèles HTML personnalisés existants ou les modèles créés par un tiers, ils doivent être recréés dans l’éditeur Drag & Drop.

Vous ne savez pas si votre message in-app doit être envoyé via une campagne ou un [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/) ? Les campagnes sont préférables pour des messages simples, tandis que les Canvas se prêtent davantage aux expériences utilisateur en plusieurs étapes. Une fois que vous avez choisi où créer votre message, examinons les étapes pour créer un message in-app en glisser-déposer !

## Conditions préalables

Les messages créés en utilisant l’éditeur Drag & Drop ne peuvent être envoyés qu’aux utilisateurs utilisant les versions SDK suivantes au minimum :

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

Si un utilisateur n’a pas mis à jour son application (c’est-à-dire s’il est sur une version du SDK plus ancienne), il ne recevra pas le message in-app.

**Prérequis supplémentaires du SDK Web**<br>
L’option d’initialisation [`allowUserSuppliedJavascript`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) doit être réglée sur `true`. L’option `enableHtmlInAppMessages` permettra aussi à ces messages de fonctionner, mais elle est obsolète et devrait être mise à jour vers `allowUserSuppliedJavascript`.

## Étape 1 : Créer un message in-app

Créez un nouveau message in-app ou une étape Canvas, puis sélectionnez l’**Éditeur Drag & Drop** en tant qu’expérience d’édition.Canvas Step

## Étape 2 : Créer et concevoir votre message in-app

L’expérience de modification en glisser-déposer est divisée en deux sections : **Créer** puis **Aperçu et test**.

### Définir les styles au niveau du message

Vous pouvez définir certains styles pour qu’ils soient appliqués à tous les blocs pertinents de votre message in-app à partir de l’onglet **Styles de message**. Les styles définis dans cette section sont utilisés partout dans votre message sauf aux endroits où vous les remplacez pour un bloc spécifique.

Vous pouvez à tout moment revenir à l’onglet **Styles de message** :

- Cliquez sur le bouton de fermeture « X » sur les propriétés d’un bloc individuel
- Sélectionnez le conteneur du message, le bouton de fermeture « X » du message ou l’arrière-plan de l’éditeur

#### Ajouter une police personnalisée

Pour ajouter une police personnalisée :

1. Allez dans la section **Contenu** de l’onglet **Styles de message**.
2. Cliquez sur **Ajouter une police personnalisée**.
3. Chargez votre police en utilisant la bibliothèque média. 

Nous acceptons les types de fichiers suivants pour les polices : `.ttf`, `.woff`, `.otf`, `.woff2`. Pour plus d’informations, consultez les [fichiers d’actifs]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/html_in-app_messages#asset-files).

Vous pouvez ajouter plusieurs variations d’une famille de police étant donné que les options de style peuvent ne pas être disponibles pour les polices personnalisées. Nous ne prenons pas actuellement en charge l’ajout de polices par URL.

{% alert note %}
La police au niveau du message ne s’appliquera qu’au message en cours et à tout message dupliqué, mais pas aux modèles suivants.
{% endalert %}

### Glisser-déposer des composants de messages in-app

Lorsque vous ouvrez l’éditeur Drag & Drop, vous verrez la disposition modale de base sur le Canvas édité que vous pouvez utiliser pour commencer à construire votre message. Vous pouvez conserver cette disposition ou ajouter, supprimer et bouger les lignes et les blocs. Le **bouton Fermer** restera dans la section supérieure de votre message pour que les utilisateurs aient toujours la possibilité de rejeter le modal.

![]({% image_buster /assets/img_archive/dnd_iam_create.gif %})

L’éditeur Drag & Drop utilise deux composants principaux pour faciliter et accélérer la composition des messages in-app : **lignes** et **blocs**. Tous les blocs doivent être placés dans une rangée.

#### Lignes

Les lignes sont des unités structurelles qui définissent la composition horizontale d’une section du message en utilisant des cellules. 

![]({% image_buster /assets/img_archive/dnd_iam_rows.png %}){: style="max-width:40%"}

Lorsque vous sélectionnez une ligne, vous pouvez ajouter ou supprimer autant de colonnes que nécessaire de la section de **personnalisation des colonnes** pour disposer plusieurs éléments de contenu côte à côte. 

Vous pouvez également faire glisser pour ajuster la taille des colonnes existantes.

![]({% image_buster /assets/img_archive/dnd_iam_column_customization.gif %}){: style="max-width:40%"}

#### Blocs

Les blocs représentent divers types de contenu que vous pouvez utiliser dans votre message. Il suffit d’en faire glisser une à l’intérieur d’un segment de ligne existant et elle s’ajustera automatiquement à la largeur de la cellule.

![]({% image_buster /assets/img_archive/dnd_iam_blocks.png %}){: style="max-width:40%"}

Chaque bloc possède ses propres paramètres, comme un contrôle granulaire sur la marge intérieure. Le panneau latéral droit passe automatiquement à un panneau de style pour l’élément de contenu sélectionné. Pour plus d’informations, voir [Propriétés du bloc éditeur]({{site.baseurl}}/editor_blocks_dnd_iam/).

Lorsque vous créez votre message in-app, vous pouvez sélectionner un affichage sur mobile, tablette ou ordinateur dans la barre d’outils pour prévisualiser l’affichage de votre message in-app pour vos groupes utilisateur. Cela garantira que votre contenu est réactif et que vous pouvez effectuer tous les ajustements nécessaires au fur et à mesure.

### Détails créatifs

#### Personnaliser l’image d’arrière-plan 

Vous pouvez ajouter une image à l’arrière-plan de votre message depuis l’onglet **Styles de message**. La section de votre message qui peut défiler doit être sélectionnée pour ajouter un arrière-plan à la totalité du message.

{% alert tip %}
Si vous avez des difficultés à sélectionner un bloc donné, vous pouvez utiliser la flèche vers le haut dans la barre d’outils insérée du bloc pour faire passer le point central à chacun des blocs parents.
{% endalert %}

#### Ajout de Liquid

![]({% image_buster /assets/img_archive/dnd_iam_liquid.png %}){: style="float:right;max-width:25%;margin-left:15px"}

Pour ajouter du [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) dans vos messages in-app, sélectionnez<i class="fa-solid fa-circle-plus"></i> **Ajouter une personnalisation** depuis la barre d’outils de l’éditeur. Ici, vous pouvez ajouter différents types de personnalisation, tels que des attributs par défaut, des attributs de périphérique, des attributs personnalisés, et bien plus encore !

Ensuite, prenez votre extrait de code Liquid généré et insérez-le dans votre message. Une fois que vous avez terminé de concevoir et de créer votre message in-app, rendez-vous dans **Aperçu et test** pour prévisualiser votre message.

## Étape 3 : Tester votre message in-app

La section **Aperçu et test** vous permet de prévisualiser vos messages in-app sur différents appareil et d’envoyer un message de test au vôtre. Ici, vous pouvez vous assurer que les détails sont alignés sur toutes vos plateformes pour votre campagne de messages in-app en glisser-déposer. Il est très important de toujours tester vos messages in-app avant d’envoyer vos campagnes pour vous aider à visualiser l’apparence de votre message final depuis la perspective de l’utilisateur.

### Aperçu du message en tant qu’utilisateur

{% alert warning %}
Pour envoyer un test à des groupes de test de contenu ou des utilisateurs individuels, les notifications push doivent être activées sur vos appareils de test avant envoi.
{% endalert %}

Vous pouvez prévisualiser les messages dans l’onglet **Aperçu et test** comme si vous étiez un utilisateur. Vous pouvez sélectionner un utilisateur spécifique, un utilisateur aléatoire ou créer un utilisateur personnalisé :

- **Utilisateur aléatoire :** Braze sélectionnera de manière aléatoire un utilisateur de la base de données et prévisualisera le message in-app en fonction de ses attributs ou informations sur l’événement.
- **Utilisateur sélectionné :** Vous pouvez sélectionner un utilisateur spécifique en fonction de son adresse e-mail ou external_id. L’aperçu du message in-app s’affichera en fonction des attributs et des informations d’événement de cet utilisateur.
- **Utilisateur personnalisé :** Vous pouvez personnaliser un utilisateur. Braze offre des entrées pour tous les attributs et événements disponibles. Vous pouvez saisir toutes les informations que vous souhaitez voir dans l’aperçu d’e-mail.

### Liste de contrôle des tests

- Avez -vous testé le message sur plusieurs appareils ?
- Les images et les données s’affichent-elles et se comportent-elles comme prévu ?
- Liquid fonctionne-t-il comme prévu ? Avez-vous pris en compte une valeur d’attribut par défaut si Liquid ne renvoie aucune information ?
- Votre texte est-il clair, concis et correct ?
- Vos boutons dirigent-ils l’utilisateur à l’endroit correct ?

## FAQ

**Puis-je personnaliser mon message in-app en utilisant de l’HTML ou du JavaScript personnalisé ou transférer des messages HTML existants dans l’éditeur ?**<br>
Non.

**Puis-je enregistrer mon message in-app comme modèle après sa création dans ma campagne ou Canvas ?**<br>
Non, vous devez recréer le message in-app dans l’éditeur Drag & Drop ou dupliquer un message existant pour le sauvegarder.

**Comment puis-je créer un message in-app plein écran ou slideup ?**<br>
L’éditeur est actuellement limité aux seuls messages modaux.
