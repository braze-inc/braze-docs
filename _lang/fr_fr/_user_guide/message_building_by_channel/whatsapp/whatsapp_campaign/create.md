---
nav_title: Veuillez créer un message WhatsApp.
article_title: Créer un message WhatsApp
page_order: 0
description: "Cet article de référence couvre les étapes de génération et de création d’un message WhatsApp."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
search_rank: 1
---

# Veuillez créer un message WhatsApp.

> Les campagnes WhatsApp sont idéales pour atteindre directement vos clients et échanger avec eux par programmation. Vous pouvez utiliser Liquid et d’autres contenus dynamiques pour non seulement proposer une expérience originale à vos utilisateurs, mais aussi générer un environnement qui favorise et optimise une expérience utilisateur discrète avec votre marque. 

## Conditions préalables

Avant de pouvoir créer des messages WhatsApp, vous devez passer en revue et compléter les éléments suivants de l'[aperçu de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/):
  - Acceptez les politiques, les limites et les règles relatives au contenu
  - Paramétrez votre connexion WhatsApp
  - Construisez vos modèles initiaux dans Meta pour utiliser vos messages

## Création d'un message

### Étape 1 : Choisissez où créer votre message

{% alert note %}
WhatsApp crée des [modèles d'envoi de messages](#template-messages) différents pour chaque langue. Créez une campagne pour chaque langue avec une segmentation pour envoyer le bon modèle aux utilisateurs ou utilisez Canvas.
{% endalert %}

Vous ne savez pas si votre message doit être envoyé via une campagne ou un Canvas ? Les campagnes sont plus adaptées aux campagnes de communication uniques et avec ciblage, tandis que les canevas conviennent mieux aux parcours utilisateur en plusieurs étapes.

{% tabs %}
{% tab Campaign %}

**Étapes :**

1. Accédez à la page **Campagnes** et cliquez sur <i class="fas fa-plus"></i> **Créer une campagne**.
2. Sélectionnez **WhatsApp** ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Campagne multicanal.**
3. Donnez un nom clair et significatif à votre campagne.
4. Ajoutez [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) et [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) au besoin.
   * Les balises facilitent la recherche et l’identification des campagnes, et la création de rapports. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), vous pouvez filtrer les éléments en fonction de certaines étiquettes spécifiques.
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez choisir différentes plates-formes, types de messages et mises en page pour chacune de vos variantes ajoutées. Pour plus d'informations sur ce sujet, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si tous les messages de votre campagne sont similaires ou ont le même contenu, composez votre message avant d’ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copier à partir de la variante** dans le menu déroulant **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Étapes :**

1. [Créez votre canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l'aide du compositeur de canvas.
2. Après avoir configuré votre Canvas, ajoutez une étape dans le Créateur de Canvas. Donnez un nom clair et significatif à votre étape.
3. Choisissez un [calendrier par étapes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) et spécifiez un délai si nécessaire.
4. Filtrez votre audience pour cette étape si nécessaire. Vous pouvez affiner davantage les destinataires de cette étape en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options d’audience seront vérifiées après le délai au moment de l’envoi des messages.
5. Choisissez votre [comportement d'avancement]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Choisissez les autres canaux de communication que vous souhaitez associer à votre message.

{% alert tip %}
Si un canvas basé sur une action est déclenché par un message WhatsApp entrant, vous pouvez faire référence aux propriétés WhatsApp dans n'importe quelle étape du canvas jusqu'au prochain parcours d’action.
{% endalert %}

{% endtab %}
{% endtabs %}

### Étape 2 : Composer votre message WhatsApp

Choisissez si vous souhaitez créer un [message type](#template-messages) WhatsApp ou un message de réponse, en fonction de votre cas d'utilisation. Toute conversation initiée par l'entreprise doit partir d'un modèle approuvé, tandis que les messages de réponse peuvent être utilisés pour répondre aux messages entrants des utilisateurs dans une fenêtre de 24 heures.

![La section Variantes de message vous permet de sélectionner un groupe d'abonnement et l'un des deux types de message : Message type et message de réponse de WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp_message_variants.png %}){: style="max-width:80%;"}

{% tabs %}
{% tab Template messages %}

Vous pouvez utiliser des [messages types WhatsApp approuvés]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-3-create-whatsapp-templates
) pour entamer des conversations avec vos utilisateurs sur WhatsApp. Ces messages sont soumis à l'avance à WhatsApp pour approbation du contenu, ce qui peut prendre jusqu'à 24 heures. Toute modification que vous apportez à la copie doit être éditée et soumise à nouveau à WhatsApp.

Les champs de texte désactivés (surlignés en gris) ne peuvent pas être modifiés car ils font partie du modèle WhatsApp approuvé. Pour mettre à jour le texte désactivé, vous devez modifier votre modèle et le faire réapprouver.

#### Langues

Chaque modèle a une langue assignée, vous devez donc créer une campagne ou une étape du canvas pour chaque langue afin d'implémenter correctement l'appariement des utilisateurs. Par exemple, si vous créez un canvas qui utilise des modèles attribués en indonésien et en anglais, vous devez créer une étape du canvas pour le modèle indonésien et une étape du canvas pour le modèle anglais.

![Liste des modèles comprenant des aperçus de leurs messages, des langues qui leur sont attribuées et de leur statut d'approbation.]({% image_buster /assets/img/whatsapp/whatsapp_templates.png %}){: style="max-width:80%;"}

Si vous ajoutez du texte dans une langue qui s'écrit de droite à gauche, notez que l'aspect final des messages écrits de droite à gauche dépend largement de la manière dont les fournisseurs de services les restituent. Pour connaître les meilleures pratiques en matière d'élaboration de messages de droite à gauche qui s'affichent le plus précisément possible, reportez-vous à la section [Création de messages de droite à gauche.]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/)

#### Variables

Si vous avez ajouté des variables en créant votre modèle WhatsApp dans le gestionnaire Meta Business, ces variables s’afficheront comme des espaces blancs dans le composeur de message. Remplacez ces espaces vides par du texte liquide ou en clair. Pour utiliser du texte brut, utilisez le format "texte ici" entre doubles accolades. Si vous avez choisi d'inclure des images lors de la création de votre modèle, vous pouvez télécharger ou ajouter des images à partir de la bibliothèque multimédia ou en référençant l'URL d'une image. Dans la mesure du possible, nous vous recommandons de télécharger les images directement dans votre bibliothèque multimédia afin d'en garantir la cohérence et la fiabilité.

Prenez en compte le fait que les champs texte désactivés (surlignés en gris) ne peuvent pas être édités étant donné qu’ils font partie du modèle WhatsApp approuvé. Si vous désirez effectuer des mises à jour sur le texte désactivé, vous devez modifier votre modèle et le faire approuver à nouveau.

{% alert tip %}
{% raw %}
Si vous prévoyez d’utiliser Liquid, assurez-vous d’inclure une valeur par défaut pour la personnalisation choisie. De cette façon, si le profil utilisateur de votre destinataire est incomplet, il ne recevra pas de message. Tout message dont les variables Liquid sont manquantes ne sera pas envoyé par WhatsApp.
{% endraw %}
{% endalert %}

![L'outil Ajouter une personnalisation avec l'attribut"first_name"et la valeur par défaut « vous ».]({% image_buster /assets/img/whatsapp/whatsapp7.png %}){: style="max-width:80%;"}

### Liens dynamiques 

Les URL d'appel à l'action peuvent contenir des variables, bien que Meta exige qu'elles apparaissent à la fin de l'URL, comme `{% raw %}https://example.com/{{variable}}{% endraw %}`, où la variable peut alors être remplacée dans Braze avec du Liquid. Les liens peuvent également être inclus dans le corps du texte dans le cadre du modèle. Ces deux liens peuvent être raccourcis et suivis à l'aide [du suivi des clics]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking/).

### Images dynamiques

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% tab Response messages %}

Vous pouvez utiliser les messages de réponse pour répondre aux messages entrants de vos utilisateurs. Ces messages sont créés in-app sur Braze pendant votre expérience sur la composition et peuvent être modifiés à tout moment. Vous pouvez utiliser Liquid pour faire correspondre la langue du message de réponse aux utilisateurs appropriés.

Vous pouvez utiliser cinq modèles de messages de réponse :
- Réponse rapide
- Message texte
- Message de média
- Bouton d'action
- Message de la liste

![Composeur du messages de réponse pour un message de réponse qui accueille les nouveaux utilisateurs avec un code de réduction.]({% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Étape 3 : Prévisualiser et tester votre message

Braze recommande toujours de prévisualiser et de tester votre message avant de l’envoyer. Passez à l'onglet **Test** pour envoyer un message WhatsApp de test à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou à des utilisateurs individuels, ou prévisualisez le message en tant qu'utilisateur directement dans Braze.

![Un message d'aperçu pour un utilisateur personnalisé nommé Max.]({% image_buster /assets/img/whatsapp/whatsapp8.png %}){: style="max-width:80%;"}

{% alert note %}
Une fenêtre de conversation est nécessaire pour envoyer des messages de réponse, y compris des messages de test. Pour lancer une fenêtre de conversation, envoyez un message WhatsApp au numéro de téléphone associé au groupe d'abonnement que vous utilisez pour ce message. Le numéro de téléphone associé est répertorié dans l'alerte de l'onglet **Test.**
{% endalert %}

![Une alerte qui dit : " Pour tester, ouvrez d'abord une fenêtre de conversation en envoyant un message WhatsApp au +1 217-582-9414. Ensuite, envoyez votre message de réponse à l'utilisateur test. »]({% image_buster /assets/img/whatsapp/whatsapp_test_phone_number.png %}){: style="max-width:70%;"}

### Étape 4 : Créer le reste de votre campagne ou de votre Canvas

{% tabs %}
{% tab Campaign %}

Concevez ensuite le reste de votre campagne. Consultez les sections suivantes pour plus de détails sur la meilleure façon d'utiliser nos outils pour créer des messages WhatsApp.

#### Choisir une planification ou un déclencheur pour la livraison

Les messages WhatsApp peuvent être livrés sur la base d’une heure planifiée, d’une action ou d’un déclencheur API. Pour en savoir plus, reportez-vous à la section [Planification de votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Pour une livraison basée sur l'action, vous pouvez également définir la durée de la campagne et les [Heures de silence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

C'est également à cette étape que vous pouvez spécifier les contrôles de réception/distribution, par exemple en autorisant les utilisateurs à se [réinscrire]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) pour recevoir la campagne ou en activant les règles de [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Choisir les utilisateurs à cibler

Ensuite, il est nécessaire de [réaliser le ciblage des utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) en sélectionnant des segments ou des filtres afin de restreindre votre audience. Vous devriez déjà avoir sélectionné le groupe d'abonnement, qui restreint les utilisateurs en fonction du niveau ou de la catégorie de communication qu'ils souhaitent avoir avec vous. Au cours de cette étape, vous sélectionnez l'audience la plus large parmi vos segments et affinez ce segment à l'aide de nos filtres. Vous recevez automatiquement un aperçu de la population approximative de ce segment. Veuillez noter que l'appartenance exacte à un segment est toujours calculée avant l'envoi du message.

{% multi_lang_include target_audiences.md %}

#### Sélectionner des événements de conversion

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), après avoir reçu une campagne. Vous pouvez autoriser une fenêtre de 30 jours maximum pendant laquelle une conversion sera comptabilisée si l’utilisateur effectue l’action spécifiée.

Vous pouvez également définir des événements de conversion personnalisés propre à votre cas d’utilisation spécifique. Soyez créatif et réfléchissez à la façon dont vous voulez vraiment évaluer la réussite de cette campagne.

{% endtab %}

{% tab Canvas %}

Si vous ne l’avez pas déjà fait, complétez les sections restantes de votre composant de Canvas. Pour plus de détails sur la manière de créer le reste de votre Canvas, de mettre en œuvre les tests multivariés et la sélection intelligente, et plus encore, reportez-vous à l'étape [Créer votre Canvas]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/) de notre documentation sur le Canvas.

Comme les fenêtres de conversation ne peuvent durer que 24 heures par message entrant, Braze vérifie qu'il n'y a pas de délai supérieur à 24 heures entre un message entrant et un message de réponse. 

{% endtab %}
{% endtabs %}

### Étape 5 : Revue et déploiement

Quand vous avez fini de concevoir votre campagne ou votre Canvas, vérifiez ses détails, testez-le et envoyez-le !

Ensuite, consultez les [rapports WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign_analytics/) pour savoir comment accéder aux résultats de vos campagnes WhatsApp.

## Fonctionnalités de WhatsApp prises en charge

### Messages sortants

Les fonctionnalités suivantes sont prises en charge pour les messages WhatsApp sortants que vous envoyez par l'intermédiaire de Braze :

| Fonctionnalité | Détails | Taille maximale | Formats pris en charge |
| ------- | ------- | ------------- | ---------------------- |
| Texte de l'en-tête | Les chaînes de caractères et les paramètres variables sont pris en charge. | - | -
| Texte du corps | Les chaînes de caractères et les paramètres variables sont pris en charge. | - | - |
| Texte du pied de page | Les chaînes de caractères et les paramètres variables sont pris en charge. | - | - |
| Liens CTA | Différents types d'appels à l'action (CTA) sont pris en charge. Pour plus de détails, voir les [types d'appel à l'action.](#ctas) | - | - |
| Images | Les images peuvent être intégrées dans le corps du texte. Ils doivent être de 8 bits et utiliser un modèle de couleur RVB ou RGBA. | < 5 MO | `.png`, `.jpg`, `.jpeg` |
| Documents | Les documents peuvent être intégrés dans le corps du texte. Les fichiers doivent être hébergés par l'intermédiaire d'une URL. | < 100 MO | `.txt`, `.xls`, `.xlsx`, `.doc`, `.docx`, `.ppt`, `.pttx`, `.pdf` |
| Vidéos | Les vidéos peuvent être intégrées dans le corps du texte. Les fichiers doivent être hébergés par URL ou dans la [bibliothèque multimédia de Braze]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library). | < 16 MO | `.3gp`, `.mp4` |
| Audio | L'audio n'est pris en charge que par l'envoi de messages. Les fichiers doivent être hébergés par l'intermédiaire d'une URL. | < 16 MO | `.aac`, `.amr`, `.mp3`, `.mp4`, `.ogg` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert important %}
Meta présente un problème connu qui peut empêcher la lecture de certaines vidéos MP4 sur les appareils Android en raison de paramètres d'encodage ou de conteneur spécifiques. En attendant qu'une solution définitive soit disponible, le reformatage du fichier MP4 permet de résoudre le problème pour la plupart des expéditeurs. Veuillez tester toutes les vidéos sur des appareils Android afin de confirmer leur bonne livrabilité. <br><br>Vous pouvez reformater le fichier MP4 à l'aide d'un outil en ligne, tel que [CloudConvert](https://cloudconvert.com/mp4-converter). Veuillez télécharger votre fichier MP4 dans l'outil, le convertir à nouveau en MP4, puis télécharger le fichier converti.
{% endalert %}

### Messages entrants

Les fonctionnalités suivantes sont prises en charge pour les messages WhatsApp entrants que vous recevez par l'intermédiaire de Braze :

| Fonctionnalité | Détails | Formats pris en charge |
| ------- | ------- | ------------------ |
| Texte du corps | Seules les chaînes de caractères standard sont prises en charge. | - |
| Images | Les images doivent être de 8 bits et utiliser un modèle de couleurs RVB ou RGBA. Les fichiers doivent être inférieurs à 5 Mo. | `.jpg`, `.png` |
| Audio | Seuls les fichiers Ogg encodés avec le codec Opus sont pris en charge. Les autres formats Ogg ne le sont pas. | `.aac`, `.mp4`, `.mpeg`, `.amr`, `.ogg (Opus only)` |
| Documents | Les documents sont pris en charge par l'envoi de messages en pièce jointe. | `.txt`, `.pdf`, `.ppt`, `.doc`, `.xls`, `.docx`, `.pptx`, `.xlsx` |
| Vidéo | Seuls le codec vidéo H.264 et le codec audio AAC sont pris en charge. Les vidéos doivent avoir un seul flux audio ou ne pas en avoir. | `.mp4`, `.3gp` |
| Liens CTA | Différents types d'appels à l'action (CTA) sont pris en charge. Pour plus de détails, voir les [types d'appel à l'action.](#ctas) | - |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Types d'appels à l'action {#ctas}

Les types d'appel à l'action suivants sont pris en charge pour les messages WhatsApp que vous envoyez par l'intermédiaire de Braze :

| Type de CTA    | Détails |
| ----------- |---------------- | 
| Visitez le site web | Un bouton au maximum (y compris les paramètres variables). |
| Appeler le numéro de téléphone | Disponible uniquement pour les modèles de messages. <br>Un bouton au maximum. |
| Boutons de réponse rapide personnalisés | Trois boutons au maximum. |
| Bouton de désabonnement marketing | Par défaut, les statuts d'abonnement ne sont pas mis à jour automatiquement. Pour obtenir des instructions détaillées, veuillez consulter [la section Abonnements et& désabonnements]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/#marketing-opt-out-selection). |
| Modèles de messages pour codes promotionnels | Disponible uniquement pour les modèles de messages. <br>Ces modèles peuvent être ouverts et modifiés comme les autres modèles de message, et sont compatibles avec les codes de promotion Liquid et Braze. |
| Messages de réponse CTA  | Veuillez créer un message de réponse incluant un bouton d'action. |
| [Liste des messages de réponse]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/#list-messages) | Créez un message de réponse comprenant une liste de 10 options au maximum parmi lesquelles les utilisateurs peuvent choisir. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

