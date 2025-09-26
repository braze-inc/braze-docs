---
nav_title: Création d’un message in-app
article_title: "Création d'un message in-app par glisser-déposer"
description: "Cet article de référence traite de la création d'un message in-app avec l'éditeur par glisser-déposer, des conditions préalables, des détails créatifs, et plus encore."
alias: "/create_dnd_iam/"
page_order: 1
local_redirect: #set-message-level-styles, #add-a-custom-font, #drag-and-drop-in-app-message-components, #creative-details
  set-message-level-styles: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-level-styles'
  add-a-custom-font: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#custom-fonts'
  drag-and-drop-in-app-message-components: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components'
  creative-details: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#creative-details'
---

# Créer un message in-app par glisser-déposer

> Avec l’éditeur par glisser-déposer, vous pouvez créer des messages in-app entièrement personnalisés dans les campagnes ou les canvas à l’aide de l’expérience de modification par glisser-déposer.

Si vous souhaitez utiliser vos modèles HTML personnalisés existants ou des modèles créés par un tiers, ils doivent être recréés dans l'éditeur par glisser-déposer.

Vous ne savez pas si votre message in-app doit être envoyé à l'aide d'une campagne ou d'un [canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/) ? Les campagnes sont mieux adaptées aux campagnes de communication simples et uniques, tandis que les Canvas sont mieux adaptés aux parcours client en plusieurs étapes. Une fois que vous avez choisi l'endroit où créer votre message, passons aux étapes permettant de créer un message in-app par glisser-déposer.

## Conditions préalables

### Exigences SDK

| Version minimale du SDK                                                          | Version recommandée du SDK                                                       |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}{:/} | {::nomarkdown}{% sdk_min_versions swift:6.5.0 android:26.0.0 web:4.8.1 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% details Plus d'informations sur les versions minimales de SDK %}

Les messages créés à l'aide de l'éditeur par glisser-déposer ne peuvent être envoyés qu'aux utilisateurs disposant des versions minimales du SDK (voir tableau ci-dessus). Si un utilisateur n’a pas mis à jour son application (c’est-à-dire s’il utilise une version du SDK plus ancienne), il ne recevra pas le message in-app.

Pour profiter de toutes les fonctionnalités disponibles dans l'éditeur par glisser-déposer, mettez à jour vos SDK avec les versions recommandées. Cela vous permet de bénéficier des fonctionnalités supplémentaires suivantes :

- Liens de texte qui ne renvoient pas au message
- Bouton d'action pour demander une amorce de notification push

Vous trouverez ci-dessous les exigences minimales du SDK pour ces fonctionnalités :

| Liens de texte*                                                         | Demande d'amorce de notification push                                                           |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:6.2.0 android:26.0.0 %}{:/} | {::nomarkdown}{% sdk_min_versions web:4.8.1 swift:6.5.0 android:26.0.0 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

\*Si vous incluez un lien dans votre message in-app qui redirige vers une URL et que l'utilisateur final ne dispose pas des versions minimales du SDK spécifiées, la sélection du lien fermera le message et l'utilisateur ne pourra pas revenir dans le message pour soumettre le formulaire.

{% enddetails %}

### Conditions préalables supplémentaires

- Pour le SDK Web, l'option d'initialisation [`allowUserSuppliedJavascript`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) doit être définie sur `true`. L’option `enableHtmlInAppMessages` permettra aussi à ces messages de fonctionner, mais elle est obsolète et devrait être mise à jour vers `allowUserSuppliedJavascript`.
- Si vous utilisez Google Tag Manager, vous devez activer l'option "Autoriser les messages in-app HTML" dans la configuration de GTM.

## Étape 1 : Créer un message in-app

Créez un nouveau message in-app ou une étape de canvas, puis sélectionnez l'**éditeur par glisser-déposer** comme expérience d’édition.

## Étape 2 : Sélectionnez votre modèle

Après avoir sélectionné l'éditeur par glisser-déposer comme expérience d'édition, vous pouvez choisir de :

- Commencer par un modèle de modal vide
- Utiliser un modèle de message in-app à glisser-déposer de Braze
- Sélectionner un modèle de message in-app par glisser-déposer enregistré

Sélectionnez **Créer un message** pour commencer à concevoir votre message in-app dans l'éditeur glisser-déposer.

![La section Modèles de Braze vous permet de choisir un modèle de base, une image d'arrière-plan, une capture de numéro de téléphone ou un modèle vierge.]({% image_buster /assets/img_archive/dnd_iam_select_template.png %})

Vous pouvez également accéder à tous les modèles à partir de la section **Modèles** du tableau de bord.

## Étape 3 : Ajouter des pages supplémentaires (facultatif) {#multi-page}

L'ajout de pages à votre message in-app vous permet de guider les utilisateurs à travers un flux séquentiel, comme un flux d'onboarding ou un parcours de bienvenue. Vous pouvez gérer les pages à partir de la section **Pages** de l'onglet **Créer.**

![Un message in-app pour une entreprise de soins de santé composé de trois pages.]({% image_buster /assets/img_archive/dnd_iam_mockup.png %})

{% tabs %}
{% tab Ajouter des pages %}

Les messages in-app commencent par une page par défaut. Pour ajouter une nouvelle page :

1. Sélectionnez **\+ Ajouter une page**.
2. Sélectionnez dans la liste des modèles personnalisés ou fournis par Braze.
3. Donnez à la page un nom significatif. Cela vous aidera lors de la connexion des pages entre elles.

{% alert tip %}
Vous pouvez ajouter jusqu'à 10 pages par message in-app.
{% endalert %}

Pour dupliquer une page existante :

1. Survolez la page dans la liste et sélectionnez <i class="fas fa-ellipsis-vertical"></i> pour ouvrir d'autres options.
2. Sélectionnez **Dupliquer**.
3. Donnez à la page un nom significatif. Cela vous aidera lors de la connexion des pages entre elles.

{% endtab %}
{% tab Supprimer ou renommer des pages %}

Pour supprimer ou renommer une page :

1. Survolez la page dans la liste et sélectionnez <i class="fas fa-ellipsis-vertical"></i> pour ouvrir d'autres options.
2. Sélectionnez **Renommer** ou **Supprimer**.

{% endtab %}
{% endtabs %}

### Étape 3a : Relier des pages entre elles

Les messages in-app multipages sont séquentiels, ce qui signifie que les utilisateurs interagissent avec le message en tapant ou en cliquant pour passer à la page suivante dans le flux.

Pour relier des pages entre elles :

1. Sélectionnez votre page de départ.
2. Sélectionnez un bouton ou un élément d'image dans le canvas.
3. Réglez le **comportement au clic sur** **Aller à la page**.
4. Sélectionnez la page vers laquelle vous souhaitez établir un lien à partir de la page de départ.
5. Continuez jusqu'à ce que toutes les pages soient liées.

![Un utilisateur modifie le bouton d'action principal pour aller à la page 2 du message in-app.]({% image_buster/assets/img_archive/dnd_iam_multipage.gif %})

Si une page n'est liée à aucune autre page, le message ne peut pas être lancé.

{% alert note %}
Les utilisateurs peuvent sélectionner le bouton de fermeture X pour quitter le message à tout moment. Ce bouton ne peut pas être enlevé.
{% endalert %}

## Étape 4 : Créer et concevoir votre message in-app

C'est ici que votre message doit « en jeter », en arborant le style caractéristique de votre marque. Grâce à une combinaison de blocs éditeurs et de paramètres de style, vous pouvez personnaliser et concevoir votre message in-app.

- Pour obtenir une liste des blocs éditeurs disponibles et de leurs propriétés, reportez-vous à la section [Blocs éditeurs.]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/)
- Pour vous aider à personnaliser l'aspect et la convivialité de votre message, consultez la rubrique [Paramètres de style]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/).
- Pour connaître les meilleures pratiques en matière de création d'envois de messages de droite à gauche, reportez-vous à la section [Création d'envois de droite à gauche]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

## Étape 5 : Tester votre message in-app

La section **Aperçu et test** vous permet de prévisualiser vos messages in-app sur différents appareils et d'envoyer un message test à votre appareil. Ici, vous pouvez vous assurer que les détails sont alignés sur toutes vos plateformes pour votre campagne de messages in-app à glisser-déposer. 

Il est important de toujours tester vos messages in-app avant d'envoyer vos campagnes pour vous aider à visualiser ce à quoi ressemblera votre message final du point de vue de votre utilisateur.

### Aperçu du message en tant qu’utilisateur

{% alert warning %}
Pour envoyer un test à des groupes de test de contenu ou des utilisateurs individuels, les notifications push doivent être activées sur vos appareils de test avant envoi.
{% endalert %}

Vous pouvez prévisualiser les messages à partir de l'onglet **Prévisualisation et test**, comme si vous étiez un utilisateur. Vous pouvez sélectionner un utilisateur spécifique, un utilisateur aléatoire ou créer un utilisateur personnalisé :

- **Utilisateur aléatoire :** Braze sélectionnera de manière aléatoire un utilisateur de la base de données et prévisualisera le message in-app en fonction de ses attributs ou informations sur l’événement.
- **Sélectionner un utilisateur :** Vous pouvez sélectionner un utilisateur spécifique en fonction de son adresse e-mail ou `external_id`. L’aperçu du message in-app s’affichera en fonction des attributs et des informations d’événement de cet utilisateur.
- **Utilisateur personnalisé :** Vous pouvez personnaliser un utilisateur. Braze offre des entrées pour tous les attributs et événements disponibles. Saisissez les informations que vous souhaitez voir figurer dans l'e-mail de prévisualisation.

### Liste de contrôle des tests

Réfléchissez aux questions suivantes lorsque vous testez votre message in-app :

- Avez-vous testé le message sur plusieurs appareils ?
- Les images et les données s’affichent-elles et se comportent-elles comme prévu ?
- Le Liquid fonctionne-t-il comme prévu ? Avez-vous pris en compte une valeur d’attribut par défaut si le Liquid ne renvoie aucune information ?
- Votre texte est-il clair, concis et correct ?
- Vos boutons dirigent-ils l’utilisateur à l’endroit correct ?

## Foire aux questions

#### Pourquoi les clics sur le corps n’apparaissent-ils pas sur ma page d’analytique ?

Les clics du corps ne sont pas automatiquement collectés pour les messages in-app créés avec l'éditeur par glisser-déposer. Pour plus d’informations, reportez-vous aux journaux des modifications du SDK pour [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) et [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100).

#### Puis-je segmenter en fonction des clics de bouton ?

Oui, vous pouvez segmenter en fonction des clics de bouton pour un maximum de deux boutons dans votre message. Pour ce faire, définissez l'**Identifiant pour le reporting** de vos boutons sur "0" et "1", qui correspondront respectivement aux filtres de segmentation "Clic sur le bouton 1 du message in-app" et "Clic sur le bouton 2 du message in-app".

![Le champ "Identifiant pour le rapport" avec une valeur de "0".]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}

#### Puis-je personnaliser mon message in-app à l'aide de HTML ou de JavaScript personnalisés ou transférer des messages HTML existants dans l'éditeur ?

Vous ne pouvez pas transférer directement des messages HTML existants dans l'éditeur, mais vous pouvez insérer du HTML brut, du CSS et du JavaScript dans un bloc de code personnalisé. Vous pouvez utiliser les blocs de code personnalisé pour intégrer des vidéos de tiers et des liquides avancés, tels que le contenu connecté ou les instructions conditionnelles.

#### Comment créer un message in-app contextuel ?

Actuellement, l'éditeur est limité aux messages modaux et plein écran. Vous pouvez passer d'un type d'affichage à l'autre dans la section **Conteneur de messages** du panneau **Styles de messages.** 

#### Puis-je enregistrer mon message in-app comme modèle après l'avoir créé dans ma campagne ou mon Canvas ?

Oui. Pour tout message in-app que vous souhaitez réutiliser dans une prochaine campagne ou étape du canvas, vous pouvez l'enregistrer en tant que modèle personnalisé à l'aide du bouton **Enregistrer en tant que modèle**, disponible après avoir quitté l'éditeur. Avant de pouvoir l'enregistrer en tant que modèle, vous devez d'abord lancer la campagne OU l'enregistrer en tant que brouillon.

![Aperçu d'un message in-app pour une visite de produit.]({% image_buster /assets/img_archive/dnd_iam_save_as_template.png %})

Vous pouvez également créer et enregistrer des modèles de messages in-app en naviguant vers **Modèles** > **Modèles de messages in-app.**
