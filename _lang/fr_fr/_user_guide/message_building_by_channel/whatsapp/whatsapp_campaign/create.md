---
nav_title: Créer un message WhatsApp
article_title: Créer un message WhatsApp
page_order: 4
description: "Cet article de référence couvre les étapes de génération et de création d’un message WhatsApp."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
search_rank: 1
---

# Créer un message WhatsApp

> Les campagnes WhatsApp sont idéales pour atteindre directement vos clients et échanger avec eux par programmation. Vous pouvez utiliser Liquid et d’autres contenus dynamiques pour non seulement proposer une expérience originale à vos utilisateurs, mais aussi générer un environnement qui favorise et optimise une expérience utilisateur discrète avec votre marque. 

## Conditions préalables

Pour créer un message WhatsApp et tirer parti du canal WhatsApp, vous devez d'abord lire la [présentation]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/) WhatsApp et effectuer les étapes suivantes :
  - Acceptez les politiques, les limites et les règles relatives au contenu
  - Paramétrez votre connexion WhatsApp
  - Construisez vos modèles initiaux dans Meta pour utiliser vos messages

## Étape 1 : Choisissez où créer votre message

{% alert note %}
WhatsApp crée des [modèles d'envoi de messages](#template-messages) différents pour chaque langue. Créez une campagne pour chaque langue avec une segmentation pour envoyer le bon modèle aux utilisateurs ou utilisez Canvas.
{% endalert %}

Vous ne savez pas si votre message doit être envoyé via une campagne ou un Canvas ? Les campagnes sont mieux adaptées aux campagnes de communication simples et uniques, tandis que les Canvas sont mieux adaptés aux parcours client en plusieurs étapes.

{% tabs %}
{% tab Campagne %}

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
Si un Canvas basé sur une action est déclenché par un message WhatsApp entrant, vous pouvez référencer les propriétés WhatsApp dans n'importe quelle étape du Canvas jusqu'au prochain parcours d'action.
{% endalert %}

{% endtab %}
{% endtabs %}

## Étape 2 : Composer votre message WhatsApp

Choisissez si vous souhaitez créer un [message type](#template-messages) WhatsApp ou un message de réponse, en fonction de votre cas d'utilisation. Toute conversation initiée par l'entreprise doit partir d'un modèle approuvé, tandis que les messages de réponse peuvent être utilisés pour répondre aux messages entrants des utilisateurs dans une fenêtre de 24 heures.

![La section Variantes de message vous permet de sélectionner un groupe d'abonnement et l'un des deux types de message : Message type et message de réponse de WhatsApp.][5]{: style="max-width:80%;"}

### Messages types

Vous pouvez utiliser des [messages types WhatsApp approuvés]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-3-create-whatsapp-templates
) pour entamer des conversations avec vos utilisateurs sur WhatsApp. Ces messages sont soumis à l'avance à WhatsApp pour approbation du contenu, ce qui peut prendre jusqu'à 24 heures. Toute modification que vous apportez à la copie doit être éditée et soumise à nouveau à WhatsApp.

Les champs de texte désactivés (surlignés en gris) ne peuvent pas être modifiés car ils font partie du modèle WhatsApp approuvé. Pour mettre à jour le texte désactivé, vous devez modifier votre modèle et le faire réapprouver.

#### Langues

Chaque modèle a une langue assignée, vous devez donc créer une campagne ou une étape du canvas pour chaque langue afin d'implémenter correctement l'appariement des utilisateurs. Par exemple, si vous créez un canvas qui utilise des modèles attribués en indonésien et en anglais, vous devez créer une étape du canvas pour le modèle indonésien et une étape du canvas pour le modèle anglais.

![Liste des modèles comprenant des aperçus de leurs messages, des langues qui leur sont attribuées et de leur statut d'approbation.][8]{: style="max-width:80%;"}

Si vous ajoutez du texte dans une langue qui s'écrit de droite à gauche, notez que l'aspect final des messages écrits de droite à gauche dépend largement de la manière dont les fournisseurs de services les restituent. Pour connaître les meilleures pratiques en matière d'élaboration de messages de droite à gauche qui s'affichent le plus précisément possible, reportez-vous à la section [Création de messages de droite à gauche.]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/localizing_a_campaign/right_to_left_messages/)

#### Variables

Si vous avez ajouté des variables en créant votre modèle WhatsApp dans le gestionnaire Meta Business, ces variables s’afficheront comme des espaces blancs dans le composeur de message. Remplacez ces espaces vides par du texte liquide ou en clair. Pour utiliser du texte brut, utilisez le format "texte ici" entre doubles accolades. Si vous avez choisi d'inclure des images lorsque vous créez votre modèle, vous pouvez télécharger ou ajouter des images à partir de la bibliothèque multimédia ou en faisant référence à l'URL d'une image.

Prenez en compte le fait que les champs texte désactivés (surlignés en gris) ne peuvent pas être édités étant donné qu’ils font partie du modèle WhatsApp approuvé. Si vous désirez effectuer des mises à jour sur le texte désactivé, vous devez modifier votre modèle et le faire approuver à nouveau.

{% alert tip %}
{% raw %}
Si vous prévoyez d’utiliser Liquid, assurez-vous d’inclure une valeur par défaut pour la personnalisation choisie. De cette façon, si le profil utilisateur de votre destinataire est incomplet, il ne recevra pas de message. Tout message comportant des variables Liquid manquantes ne sera pas envoyé via WhatsApp.
{% endraw %}
{% endalert %}

![L'outil Ajouter une personnalisation avec l'attribut "prénom_nom" et la valeur par défaut "vous".][2]{: style="max-width:80%;"}

### Liens dynamiques 

Les URL d'appel à l'action peuvent contenir des variables, bien que Meta exige qu'elles apparaissent à la fin de l'URL, comme `{% raw %}https://example.com/{{variable}}{% endraw %}`, où la variable peut alors être remplacée dans Braze avec du Liquid. Les liens peuvent également être inclus dans le corps du texte dans le cadre du modèle. Pour l'instant, aucun de ces liens ne peut être raccourci. 

### Messages de réponse

Vous pouvez utiliser les messages de réponse pour répondre aux messages entrants de vos utilisateurs. Ces messages sont créés in-app sur Braze pendant votre expérience sur la composition et peuvent être modifiés à tout moment. Vous pouvez utiliser Liquid pour faire correspondre la langue du message de réponse aux utilisateurs appropriés.

Vous pouvez utiliser trois types de messages de réponse :
- Réponse rapide
- Message texte
- Message de média

![Composeur du messages de réponse pour un message de réponse qui accueille les nouveaux utilisateurs avec un code de réduction.][6]{: style="max-width:80%;"}

## Étape 3 : Prévisualiser et tester votre message

Braze recommande toujours de prévisualiser et de tester votre message avant de l’envoyer. Passez à l'onglet **Test** pour envoyer un message WhatsApp de test à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou à des utilisateurs individuels, ou prévisualisez le message en tant qu'utilisateur directement dans Braze.

![Un message de prévisualisation pour un utilisateur existant nommé Suzanne.][3]{: style="max-width:80%;"}

{% alert note %}
Une fenêtre de conversation est nécessaire pour envoyer des messages de réponse, y compris des messages de test. Pour lancer une fenêtre de conversation, envoyez un message WhatsApp au numéro de téléphone associé au groupe d'abonnement que vous utilisez pour ce message. Le numéro de téléphone associé est répertorié dans l'alerte de l'onglet **Test.**
{% endalert %}

![Alerte indiquant : « Pour effectuer un test, commencez par ouvrir une fenêtre de conversation en envoyant un message WhatsApp au +1 631-202-0907. Ensuite, envoyez votre message de réponse à l'utilisateur test. »][7]{: style="max-width:80%;"}

## Étape 4 : Créer le reste de votre campagne ou de votre Canvas

{% tabs %}
{% tab Campagne %}

Concevez ensuite le reste de votre campagne. Consultez les sections suivantes pour plus de détails sur la meilleure façon d'utiliser nos outils pour créer des messages WhatsApp.

#### Choisir une planification ou un déclencheur pour la livraison

Les messages WhatsApp peuvent être livrés sur la base d’une heure planifiée, d’une action ou d’un déclencheur API. Pour en savoir plus, reportez-vous à la section [Planification de votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Pour une livraison basée sur l'action, vous pouvez également définir la durée de la campagne et les [Heures de silence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

C'est également à cette étape que vous pouvez spécifier les contrôles de réception/distribution, par exemple en autorisant les utilisateurs à se [réinscrire]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) pour recevoir la campagne ou en activant les règles de [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Choisir les utilisateurs à cibler

Ensuite, vous devez [cibler les utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) en choisissant des segments ou des filtres pour réduire votre audience. Vous devriez déjà avoir choisi le groupe d'abonnement, ce qui restreint les utilisateurs par le niveau ou la catégorie de communication qu'ils souhaitent avoir avec vous. Au cours de cette étape, vous allez sélectionner une audience plus importante dans vos segments et allez restreindre davantage ce segment à l’aide de nos filtres. Vous recevez automatiquement un aperçu de ce à quoi ressemble la population approximative du segment à ce moment-là. Souvenez-vous que l’appartenance à un segment exact est toujours calculée juste avant l’envoi du message.

#### Sélectionner des événements de conversion

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), après avoir reçu une campagne. Vous pouvez autoriser une fenêtre de 30 jours maximum pendant laquelle une conversion sera comptabilisée si l’utilisateur effectue l’action spécifiée.

Vous pouvez également définir des événements de conversion personnalisés propre à votre cas d’utilisation spécifique. Soyez créatif et réfléchissez à la façon dont vous voulez vraiment évaluer la réussite de cette campagne.

{% endtab %}

{% tab Canvas %}

Si vous ne l’avez pas déjà fait, complétez les sections restantes de votre composant de Canvas. Pour plus de détails sur la manière de créer le reste de votre Canvas, de mettre en œuvre les tests multivariés et la sélection intelligente, et plus encore, reportez-vous à l'étape [Créer votre Canvas]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/) de notre documentation sur le Canvas.

Comme les fenêtres de conversation ne peuvent durer que 24 heures par message entrant, Braze vérifie qu'il n'y a pas de délai supérieur à 24 heures entre un message entrant et un message de réponse. 

{% endtab %}
{% endtabs %}

## Étape 5 : Revue et déploiement

Quand vous avez fini de concevoir votre campagne ou votre Canvas, vérifiez ses détails, testez-le et envoyez-le !

Ensuite, consultez les [rapports WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign_analytics/) pour savoir comment accéder aux résultats de vos campagnes WhatsApp.

## Fonctionnalités de WhatsApp prises en charge

Braze prend en charge les fonctionnalités d'envoi de messages WhatsApp suivantes.

### Messages sortants

Vous pouvez envoyer aux utilisateurs les éléments suivants dans vos messages WhatsApp :

Fonctionnalité du message    | Détails
----------- |---------------- 
En-têtes | 
Texte | Prise en charge des paramètres variables
Images (JPEG et PNG) | Doit être de 8 bits, RVB ou RGBA, et jusqu'à 5 Mo pour tout type. 
Vidéos | Actuellement, il doit être hébergé sur une URL et contenir moins de 16 Mo. Le type de vidéo doit également être 3GPP ou MP4. <br><br>Les messages vidéo sont actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
Audio | Pris en charge uniquement pour l'envoi de messages de réponse. Il doit s'agir d'un fichier audio AAC, AMR, MP3, MP4 ou OGG, hébergé sur une URL et d'une taille inférieure à 16 Mo. <br><br>Les messages audio sont actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
Documents | Doit être hébergé sur une URL et être inférieur à 100 Mo. Le document doit également être de type texte (`.txt`), Microsoft Excel (`.xls`, `.xlsx`), Microsoft Word (`.doc`, `.docx`), Microsoft PowerPoint (`.ppt`, `pttx`) ou PDF (`.pdf`). <br><br>Les messages des documents sont actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
Texte du corps | Prise en charge des paramètres variables
Texte du pied de page | Prise en charge des paramètres variables 
CTA | Voir [Appels à l'action](#ctas).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Appels à l'action {#ctas}

Vous pouvez ajouter les appels à l'action suivants dans vos messages WhatsApp :

Type de CTA    | Détails
----------- |---------------- 
Visitez le site web | Un bouton au maximum (y compris les paramètres variables).
Appeler le numéro de téléphone | Disponible uniquement pour les modèles de messages. <br>Un bouton au maximum.
Boutons de réponse rapide personnalisés | Trois boutons au maximum. 
Bouton de désabonnement marketing | Cette option ne met pas automatiquement à jour les statuts d'abonnement. <br><br>Pour les instructions de configuration, voir la rubrique [Abonnements et désabonnements.]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/#marketing-opt-out-selection)
Modèles d'envoi de messages pour les codes de réduction | Disponible uniquement pour les modèles de messages. <br>Ils peuvent être ouverts et modifiés comme d'autres modèles d'envoi de messages et sont compatibles avec les codes de promotion Liquid et Braze. 
Messages de réponse CTA  | Créez un message de réponse comprenant un bouton d'appel à l'action.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Messages entrants

Les utilisateurs peuvent vous envoyer les éléments suivants dans leurs messages WhatsApp :

Fonctionnalité du message    | Détails
----------- |---------------- 
Texte | 
Images (JPEG et PNG)| Doit être de 8 bits, RVB ou RVBA, et jusqu'à 5 Mo pour n'importe quel type 
Audio| audio/aac<br>audio/mp4<br>audio/mpeg<br>audio/amr<br>audio/ogg (uniquement les codecs Opus, le codec de base audio/ogg n'est pas pris en charge)
Documents | texte/plain<br>application/pdf<br>application/vnd.ms-powerpoint<br>application/msword<br>application/vnd.ms-excel<br>application/vnd.openxmlformats-officedocument.wordprocessingml.document<br>application/vnd.openxmlformats-officedocument.presentationml.presentation<br>application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
CTA | Voir [Appels à l'action](#ctas).
Vidéo | vidéo/mp4, vidéo/3gp<br><br>Seuls le codec vidéo H.264 et le codec audio AAC sont pris en charge. Nous prenons en charge les vidéos avec un seul flux audio ou sans flux audio.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }



[1]: {% image_buster /assets/img/whatsapp/whatsapp6.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp7.png %}
[3]: {% image_buster /assets/img/whatsapp/whatsapp8.png %}
[4]: {% image_buster /assets/img/whatsapp/whatsapp_plain_text.png %}
[5]: {% image_buster /assets/img/whatsapp/whatsapp_message_variants.png %}
[6]: {% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}
[7]: {% image_buster /assets/img/whatsapp/whatsapp_test_phone_number.png %}
[8]: {% image_buster /assets/img/whatsapp/whatsapp_templates.png %}
