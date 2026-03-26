---
nav_title: Créer un message RCS
article_title: Créer un message RCS
page_order: 2
alias: /create_rcs_message/
description: "Cet article explique comment créer un message RCS."
page_type: reference
channel:
  - RCS
---

# Créer un message RCS

> Les campagnes RCS sont parfaites pour atteindre directement vos clients et converser de manière programmatique avec eux. Vous pouvez utiliser Liquid et d'autres contenus dynamiques pour proposer une expérience personnalisée à vos utilisateurs et créer un environnement qui favorise et optimise une expérience utilisateur discrète avec votre marque.

## Création d'un message RCS

### Étape 1 : Choisissez où créer votre message

Vous ne savez pas si votre message doit être envoyé via une campagne ou un Canvas ? Les campagnes sont plus adaptées aux campagnes de communication uniques et ciblées, tandis que les Canvas conviennent mieux aux parcours utilisateur en plusieurs étapes.

{% tabs %}
{% tab Campaign %}
1. Allez dans **Messagerie** > **Campagnes** et sélectionnez **Créer une campagne**.
2. Sélectionnez **SMS/MMS/RCS** ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Multicanal**.
3. Donnez un nom clair et significatif à votre campagne.
4. Ajoutez des [équipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) et des [étiquettes]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) si nécessaire.
   * Les étiquettes facilitent la recherche et l'identification des campagnes, et la création de rapports. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), vous pouvez filtrer les éléments en fonction de certaines étiquettes spécifiques.

{: start="5"} 
5. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez choisir différentes plateformes, types de messages et dispositions pour chacune de vos variantes. Pour en savoir plus, consultez [Tests multivariés et A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
- **Tests des variantes SMS et RCS** : Braze vous permet d'inclure à la fois des variantes SMS et RCS dans une même campagne, ce qui vous permet de comparer les performances de chacune. Vous pouvez ajouter des variantes SMS et RCS lors de la première étape de la composition du message.

{: start="6"} 
6. Sélectionnez un [groupe d'abonnement]({{site.baseurl}}/sms_rcs_subscription_groups/) compatible RCS. Lors de la sélection d'un groupe d'abonnement, Braze ajoute automatiquement un filtre de segmentation, garantissant que seuls les utilisateurs abonnés recevront la campagne. Seuls les codes longs et les codes courts appartenant à ce groupe d'abonnement seront utilisés pour envoyer des SMS aux utilisateurs cibles.
- **Repli sur le SMS :** Braze recommande vivement que chaque groupe d'abonnement contenant un expéditeur RCS comprenne également au moins un code SMS de repli. Ceci est important pour la livrabilité dans les cas où les messages RCS n'aboutissent pas. Parmi les raisons possibles : l'incompatibilité de l'appareil de l'utilisateur ou une couverture incomplète de l'opérateur dans un pays ou une région donné(e). En activant le repli SMS, votre message RCS pourra tout de même être transmis par SMS lorsque le RCS n'est pas disponible, et vous ne manquerez jamais l'occasion d'entrer en contact avec vos utilisateurs.

{% alert note %}
Le repli MMS n'est pas pris en charge.
{% endalert %}

{: start="7"}
7. Choisissez entre SMS et RCS. Avant de composer des messages RCS, choisissez le canal d'envoi. Nous recommandons généralement d'utiliser RCS dans la mesure du possible, car il offre des avantages significatifs en termes d'engagement utilisateur par rapport aux SMS ; cependant, nous offrons toujours la possibilité d'envoyer des SMS afin que vous ayez un maximum de flexibilité et de contrôle. 

![Options permettant de choisir entre un message RCS ou SMS/MMS.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% alert tip %}
Si tous les messages de votre campagne sont similaires ou ont le même contenu, composez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copier à partir de la variante** dans la liste déroulante **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Créez votre Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l'aide du compositeur de Canvas.
2. Une fois votre Canvas configuré, ajoutez une étape de message **SMS/MMS/RCS** dans le générateur de Canvas. 
3. Donnez un nom clair et significatif à votre étape.
4. Sélectionnez un [groupe d'abonnement]({{site.baseurl}}/sms_rcs_subscription_groups/) compatible RCS. Lors de la sélection d'un groupe d'abonnement, Braze ajoute automatiquement un filtre de segmentation, garantissant que seuls les utilisateurs abonnés recevront la campagne. Seuls les codes longs et les codes courts appartenant à ce groupe d'abonnement seront utilisés pour le ciblage des utilisateurs.
- **Repli sur le SMS :** Braze recommande vivement que chaque groupe d'abonnement contenant un expéditeur RCS comprenne également au moins un code SMS de repli. Ceci est important pour la livrabilité dans les cas où les messages RCS n'aboutissent pas. Parmi les raisons possibles : l'incompatibilité de l'appareil de l'utilisateur ou une couverture incomplète de l'opérateur dans un pays ou une région donné(e). En activant le repli SMS, votre message sera toujours transmis à l'utilisateur et vous ne manquerez jamais l'occasion d'entrer en contact avec lui.

{: start="5"}
5. Choisissez entre SMS et RCS. Avant de composer des messages RCS, choisissez le canal d'envoi. Nous recommandons généralement d'utiliser RCS dans la mesure du possible, car il offre des avantages significatifs en termes d'engagement utilisateur par rapport aux SMS ; cependant, nous offrons toujours la possibilité d'envoyer des SMS afin que vous ayez un maximum de flexibilité et de contrôle. 

![Options permettant de choisir entre un message RCS ou SMS/MMS.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### Étape 2 : Sélectionnez votre type de message RCS

Pour votre type de message RCS, choisissez entre **Texte** ou **Média**.

![Options permettant de choisir entre un message texte ou multimédia.]({% image_buster /assets/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% tabs %}
{% tab Text %}
Comme leur nom l'indique, les messages texte RCS se concentrent sur le texte comme support. Si vous saisissez jusqu'à 160 caractères, le message RCS est facturé comme un message texte seul (ou « de base »). Si vous dépassez 160 caractères ou utilisez un élément riche, le message est facturé comme un message RCS riche (ou « simple ») et la limite de caractères passe à 3 072 caractères. 

#### Fonctionnalités

- Les types de messages texte incluent toutes les fonctionnalités des SMS. Seul le suivi avancé est disponible pour le suivi des clics sur les URL, afin de vous offrir une granularité de rapport au niveau de l'utilisateur. 
- Vous avez également la possibilité d'inclure des boutons de **réponses suggérées** et d'**actions suggérées** attrayants qui incitent les utilisateurs à effectuer des actions à fort taux d'engagement, comme visiter une page d'accueil ou passer une commande. 
    - Les **réponses suggérées** sont des boutons contenant des suggestions de réponses sur lesquelles les utilisateurs peuvent cliquer. Le texte est alors pré-rempli dans leur champ de saisie, ce qui leur évite d'avoir à réfléchir à une réponse en leur proposant un ensemble limité de choix. 
    - Les **actions suggérées** sont des boutons qui déclenchent une action sur l'appareil de l'utilisateur. Ils se composent généralement d'un ou deux mots descriptifs et d'une icône visuelle pour aider l'utilisateur à comprendre ce que fait le bouton. Braze prend actuellement en charge les actions suggérées OpenURL. Le fonctionnement est similaire à celui d'une URL : les utilisateurs qui sélectionnent le bouton sont redirigés vers une page web ou un autre emplacement identifié par une URL. 

![Un GIF de trois actions suggérées pour un message RCS promouvant les styles de mode en vogue : « La royauté des contes de fées », « Le monde universitaire avant-gardiste » et « Montrez-moi vos autres styles ».]({% image_buster /assets/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

#### Considérations

- En ce qui concerne les limites de caractères, vous pouvez écrire jusqu'à 160 caractères pour un message RCS texte seul (de base) ou jusqu'à 3 072 pour un message RCS riche (simple). 
- Pour les limites de boutons, vous pouvez ajouter jusqu'à cinq boutons par message. Ces boutons peuvent être des actions suggérées ou des réponses suggérées.
- Les blocs de texte trop longs et les boutons trop nombreux peuvent frustrer les utilisateurs. Dans la mesure du possible, nous vous recommandons de miser sur la simplicité. 
- Dans certains cas, il peut être plus rentable d'envoyer des messages texte plus longs par RCS que par SMS. En effet, les messages SMS plus longs sont décomposés en plusieurs segments, chacun étant facturable, alors que les messages RCS sont facturés par message. Contactez votre Account Manager Braze pour plus de détails et de conseils. 
{% endtab %}

{% tab Media %}
Les messages média RCS vous permettent d'utiliser des formats média attrayants qui ne sont pas possibles avec les SMS, notamment des fichiers d'images, de vidéos et de documents. Ces options multimédias vous aident à engager votre audience encore plus profondément et ouvrent la voie à des cas d'utilisation entièrement nouveaux. Pour l'instant, seul le téléchargement d'images est pris en charge via la [bibliothèque multimédia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). 

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

#### Fonctionnalités

- Les types de messages multimédias prennent en charge tout ce qui est disponible dans les types de messages texte, à savoir le texte, les réponses suggérées et les actions suggérées.
- Prise en charge des fichiers d'images, y compris les formats JPEG et PNG. Les fichiers images sont disponibles par téléchargement depuis la bibliothèque multimédia. 
- Prise en charge des fichiers vidéo, y compris les formats MP4, MPEG et MV4. Les fichiers vidéo peuvent être ajoutés par URL directement dans le compositeur de messages. 
- Prise en charge des fichiers de documents au format PDF. Les fichiers de documents peuvent être ajoutés par URL directement dans le compositeur de messages. 

![Compositeur RCS avec une option permettant de télécharger un fichier multimédia.]({% image_buster /assets/img/rcs/rcs_media_type.png %})

#### Spécifications des fichiers

| Type de fichier | Spécifications |
| --- | --- |
| Tous | - La taille des fichiers est limitée à 100 Mo <br><br>- L'URL du fichier peut comporter jusqu'à 2 048 caractères |
| Fichiers images | Les formats pris en charge sont JPG, JPEG et GIF |
| Fichiers vidéo | Les formats pris en charge sont H263, M4V, MP4, MPEG-4, MPEG et WEBM |
| Fichiers de documents | Format pris en charge : PDF |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Considérations

L'expérience utilisateur lors de la réception de messages RCS peut varier légèrement en fonction de plusieurs facteurs, notamment la couverture de l'opérateur dans le pays de destination, le matériel de l'appareil mobile et son système d'exploitation. 

D'une manière générale, RCS s'intègre plus naturellement aux appareils Android (cette technologie a été largement mise en œuvre par Google, et la messagerie RCS pair-à-pair est largement adoptée par la communauté Android). Les différents appareils peuvent restituer l'expérience à des vitesses et avec des qualités variables.  
{% endtab %}
{% endtabs %}

### Étape 3 : Composez votre message RCS

Rédigez votre message en utilisant les langues et la personnalisation ([Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) et emojis) selon vos besoins. Veillez à respecter nos limites de texte pour réduire vos risques de frais de dépassement.

{% alert important %}
Avant de poursuivre, lisez nos [lignes directrices concernant les limites des messages RCS](#step-2-select-your-rcs-message-type). Les messages RCS sont [facturés par message]({{site.baseurl}}/sms_rcs_billing_calculators/), il est donc important de bien comprendre ce qui peut être inclus dans chaque type de message RCS.
{% endalert %}

### Étape 4 : Prévisualisez et testez votre message

Le rendu RCS étant contrôlé par le système d'exploitation de l'utilisateur, le fabricant de l'appareil, l'opérateur et l'application de messagerie (par exemple, Google Messages ou Apple Messages), l'apparence des messages peut varier. Par conséquent, l'aperçu RCS affiché dans Braze peut ne pas correspondre exactement à ce que l'utilisateur final recevra. Les différences peuvent concerner la mise en page, la taille des médias, les boutons, les éléments de marque ou les fonctionnalités prises en charge. Braze recommande toujours de prévisualiser et de tester votre message avant de l'envoyer. Utilisez l'onglet **Test** pour envoyer un RCS test à des groupes de test de contenu ou à des utilisateurs individuels, et prévisualisez le message en tant qu'utilisateur directement dans Braze. Cependant, le rendu final doit toujours être validé sur des appareils réels dans la mesure du possible, car Braze ne peut garantir une parfaite parité entre toutes les combinaisons de systèmes d'exploitation, d'appareils et d'opérateurs.


### Étape 5 : Créez le reste de votre campagne ou Canvas

Ensuite, créez le reste de votre campagne ou Canvas. Reportez-vous aux sections suivantes pour plus de détails sur la meilleure façon d'utiliser nos outils pour créer des messages RCS.

#### Étape 5.1 : Choisir une planification ou un déclencheur de réception/distribution

Les messages RCS peuvent être envoyés en fonction d'une heure planifiée, d'une action ou d'un déclencheur API. Pour en savoir plus, reportez-vous à la section [Planification de votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Pour la livraison par événement, vous pouvez également définir la durée de la campagne et les heures calmes.

Spécifiez vos contrôles de réception/distribution, par exemple en autorisant les utilisateurs à redevenir éligibles pour recevoir la campagne ou en activant des règles de limite de fréquence.

#### Étape 5.2 : Choisir les utilisateurs à cibler

Ciblez les utilisateurs en choisissant des segments ou des filtres pour affiner votre audience. Vous devriez avoir déjà sélectionné le groupe d'abonnement, qui restreint les utilisateurs en fonction du niveau ou de la catégorie de communication qu'ils souhaitent avoir avec vous.

{% multi_lang_include target_audiences.md %}

Ensuite, sélectionnez l'audience la plus large parmi vos segments et affinez-la à l'aide de [filtres]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) facultatifs. Vous recevez automatiquement un aperçu de la taille approximative de ce segment. Gardez à l'esprit que l'appartenance exacte à un segment est toujours calculée avant l'envoi du message.

{% alert tip %}
Vous souhaitez utiliser le reciblage RCS pour cibler les utilisateurs en fonction de leurs interactions SMS et RCS ? Reportez-vous à la rubrique [Reciblage]({{site.baseurl}}/sms_mms_rcs_user_retargeting/).
{% endalert %}

#### Étape 5.3 : Sélectionner des événements de conversion

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, ou événements de conversion, après avoir reçu une campagne. Vous pouvez définir une fenêtre de 30 jours maximum pendant laquelle une conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée.

Les événements de conversion vous aident à évaluer le succès de votre campagne. Par exemple :
- Si vous utilisez le géociblage pour déclencher un message RCS dont l'objectif final est que l'utilisateur effectue un achat, définissez l'événement de conversion sur **Achat**.
- Si vous essayez de diriger l'utilisateur vers votre application, définissez l'événement de conversion sur **Démarrage de la session**.

Vous pouvez également définir des événements de conversion personnalisés propres à votre cas d'utilisation. Faites preuve de créativité dans la manière dont vous souhaitez mesurer le succès de votre campagne.

### Étape 6 : Vérifiez et déployez

Une fois que vous avez fini de créer votre campagne ou votre Canvas, vérifiez-en les détails, testez-le, puis envoyez-le !

Ensuite, reportez-vous à la section [Rapports pour les SMS, MMS et RCS]({{site.baseurl}}/sms_mms_rcs_reporting/) pour savoir comment accéder aux résultats de vos campagnes RCS.

## Conseils

### Utiliser Liquid pour la personnalisation des messages

Si vous envisagez d'utiliser Liquid, veillez à inclure une valeur par défaut pour la personnalisation choisie. Ainsi, si le profil utilisateur du destinataire est incomplet, il ne recevra pas une marque substitutive vierge `Hi, !` au lieu de son nom ou d'une phrase cohérente.

### Générer du texte avec l'intelligence artificielle

Vous avez besoin d'aide pour créer un texte attrayant ? Essayez l'[assistant de rédaction IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Saisissez le nom ou la description d'un produit, et l'intelligence artificielle générera un texte marketing au ton naturel, que vous pourrez utiliser dans vos messages.

![Éditeur de messages avec une icône permettant d'accéder à l'assistant de rédaction IA.]({% image_buster /assets/img/rcs/rcs_ai_copywriter.png %}){: style="max-width:70%;"}

### Créer des workflows de messages conversationnels

Les workflows de messages conversationnels vous permettent de répondre dynamiquement aux utilisateurs, créant ainsi une expérience de messagerie interactive. Pour créer un workflow, créez un Canvas puis combinez les réponses suggérées avec des [parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) pour orienter votre workflow en fonction de la réponse sélectionnée par l'utilisateur.

1. Dans le générateur de Canvas, créez une étape de message RCS avec plusieurs réponses suggérées.

![Compositeur de messages RCS avec des réponses suggérées.]({% image_buster /assets/img/rcs/suggested_replies.png %})

{: start="2"}
2. Connectez ce message à un parcours d'action avec un groupe d'actions pour chaque réponse suggérée.
3. Pour chaque groupe d'actions :
  - Sélectionnez le déclencheur **Envoyer un message SMS entrant**.
  - Définissez le corps du message pour qu'il soit identique à la réponse suggérée correspondante. 

![Étape de parcours d'action configurée avec trois groupes d'actions, un pour chaque réponse suggérée.]({% image_buster /assets/img/rcs/quick_reply.png %})

{: start="4"}
4. Connectez chaque groupe d'actions à une étape de message RCS, puis ajoutez du contenu en fonction de la réponse suggérée associée.
5. Poursuivez le workflow conversationnel en ajoutant des réponses suggérées à tous les messages de suivi.
6. Répétez les étapes 2 à 4 jusqu'à ce que le workflow soit terminé.

![Canvas montrant un workflow conversationnel avec deux parcours d'action.]({% image_buster /assets/img/rcs/full_conversational_workflow.png %})

## Foire aux questions

### Puis-je envoyer des messages vocaux pré-enregistrés avec RCS ?

Oui, vous pouvez utiliser les messages multimédias pour prendre en charge les fichiers audio.