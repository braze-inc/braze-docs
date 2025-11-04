---
nav_title: "Création d'un message RCS"
article_title: "Création d'un message RCS"
page_order: 2
alias: /create_rcs_message/
description: "Cet article explique comment créer un message RCS."
page_type: reference
channel:
  - RCS
---

# Création d'un message RCS

> Les campagnes RCS sont parfaites pour atteindre directement vos clients et converser de manière programmatique avec eux. Vous pouvez utiliser Liquid et d'autres contenus dynamiques pour créer une expérience personnelle avec vos utilisateurs et créer un environnement qui favorise et améliore une expérience discrète de l'utilisateur avec votre marque.

## Création d'un message RCS

### Étape 1 : Choisissez où créer votre message

Vous ne savez pas si votre message doit être envoyé par le biais d'une campagne ou d'un canvas ? Les campagnes sont plus adaptées aux campagnes d'envoi de messages simples et uniques, tandis que les Canevas sont plus adaptés aux parcours utilisateurs en plusieurs étapes.

{% tabs %}
{% tab Campaign %}
1. Allez dans **Messagerie** > **Campagnes** et sélectionnez **Créer une campagne.**
2. Sélectionnez **SMS/MMS/RCS** ou, pour les campagnes ciblant plusieurs canaux, sélectionnez **Multicanal**.
3. Donnez à votre campagne un nom clair et significatif.
4. Ajoutez des [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) et des [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) si nécessaire.
   * Les étiquettes facilitent la recherche de vos campagnes et permettent de créer des rapports. Par exemple, lorsque vous utilisez le [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), vous pouvez filtrer par des étiquettes particulières.

{: start="5"}
5\. Ajoutez et nommez autant de variantes que nécessaire pour votre campagne. Vous pouvez choisir des plateformes, des types de messages et des mises en page différents pour chacune de vos variantes ajoutées. Pour en savoir plus sur ce sujet, reportez-vous aux [tests multivariés et aux tests A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
- **Essais de variantes SMS et RCS**: Braze vous permet d'inclure à la fois des variantes SMS et RCS dans une même campagne, ce qui vous permet de comparer les performances de chacune d'entre elles. Vous pouvez ajouter des variantes SMS et RCS lors de la première étape de la composition du message.

{: start="6"}
6\. Sélectionnez un [groupe d'abonnement]({{site.baseurl}}/sms_rcs_subscription_groups/) compatible avec RCS. Lors de la sélection d'un groupe d'abonnement, Braze ajoutera automatiquement un filtre de segmentation, garantissant que seuls les utilisateurs abonnés recevront la campagne. Seuls les codes longs et les codes courts appartenant à ce groupe d'abonnement seront utilisés pour envoyer des SMS aux utilisateurs ciblés.
- **Repli sur le SMS :** Braze recommande vivement que chaque groupe d'abonnement qui contient un expéditeur RCS comprenne également au moins un code SMS de repli. Ceci est important pour la livrabilité dans les cas où les messages RCS n'aboutissent pas. Cela peut s'expliquer par l'incompatibilité de l'appareil de l'utilisateur et la couverture incomplète de l'opérateur dans un pays ou une région donné(e). En activant la fonction SMS fallback, votre message sera toujours transmis à l'utilisateur et vous ne manquerez jamais l'occasion d'entrer en contact avec lui.   

{: start="7"}
7\. Choisissez entre SMS et RCS. Avant de composer des messages RCS, choisissez le canal de communication avec lequel vous les envoyez. Nous recommandons généralement d'utiliser RCS dans la mesure du possible, car il y a des avantages significatifs en termes d'engagement de l'utilisateur par rapport aux SMS ; cependant, nous offrons toujours la possibilité d'envoyer des SMS afin que vous ayez un maximum de flexibilité et de contrôle. 

!Options pour sélectionner un type de message RCS ou SMS/MMS.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% alert tip %}
Si tous les messages de votre campagne seront similaires ou auront le même contenu, composez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copier à partir de la variante** dans la liste déroulante **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}
1. [Créez votre canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) à l'aide du compositeur de canvas.
2. Après avoir configuré votre canvas, ajoutez une étape **SMS/MMS/RCS** Message dans le générateur de canvas. 
3. Donnez à votre démarche un nom clair et significatif.
4. Sélectionnez un [groupe d'abonnement]({{site.baseurl}}/sms_rcs_subscription_groups/) compatible avec RCS. Lors de la sélection d'un groupe d'abonnement, Braze ajoutera automatiquement un filtre de segmentation, garantissant que seuls les utilisateurs abonnés recevront la campagne. Seuls les codes longs et les codes courts appartenant à ce groupe d'abonnement seront utilisés pour le ciblage des utilisateurs.
- **Repli sur le SMS :** Braze recommande vivement que chaque groupe d'abonnement qui contient un expéditeur RCS comprenne également au moins un code SMS de repli. Ceci est important pour la livrabilité dans les cas où les messages RCS n'aboutissent pas. Cela peut s'expliquer par l'incompatibilité de l'appareil de l'utilisateur et la couverture incomplète de l'opérateur dans un pays ou une région donné(e). En activant la fonction SMS fallback, votre message sera toujours transmis à l'utilisateur et vous ne manquerez jamais l'occasion d'entrer en contact avec lui.

{: start="5"}
5\. Choisissez entre SMS et RCS. Avant de composer des messages RCS, choisissez le canal de communication avec lequel vous les envoyez. Nous recommandons généralement d'utiliser RCS dans la mesure du possible, car il y a des avantages significatifs en termes d'engagement de l'utilisateur par rapport aux SMS ; cependant, nous offrons toujours la possibilité d'envoyer des SMS afin que vous ayez un maximum de flexibilité et de contrôle. 

!Options pour sélectionner un type de message RCS ou SMS/MMS.]({% image_buster /assets/img/rcs/rcs_message_type.png %}){: style="max-width:65%;"}

{% endtab %}
{% endtabs %}

### Étape 2 : Sélectionnez votre type d'envoi de messages RCS

Pour votre type de message RCS, choisissez entre **Texte** ou **Média**.

!Options pour sélectionner un type de message Texte ou Média.]({% image_buster /assets/img/rcs/rcs_text_media.png %}){: style="max-width:65%;"}

{% tabs %}
{% tab Text %}
Comme leur nom l'indique, les messages texte RCS se concentrent sur le texte en tant que support. Si vous tapez jusqu'à 160 caractères, le message RCS est facturé comme un message de texte seul (ou "de base"). Si vous dépassez 160 caractères ou utilisez un élément riche, le message est facturé comme un message RCS riche (ou "simple") (et la limite de caractères passe à 3072 caractères). 

#### Fonctionnalités

- Les types de messages comprennent toutes les fonctionnalités des SMS. Seul le suivi avancé est possible pour le suivi des clics sur les URL afin de vous donner une granularité de rapport au niveau de l'utilisateur. 
- En outre, vous avez désormais la possibilité d'inclure des boutons de **réponses** et d'**actions suggérées** attrayants qui incitent les utilisateurs à effectuer des actions à fort taux d'engagement, comme visiter une page d'atterrissage ou passer une commande. 
    - Les **réponses suggérées** sont des boutons contenant des suggestions de réponses sur lesquelles les utilisateurs peuvent cliquer et qui sont pré-remplies dans leur saisie de texte, ce qui leur évite d'avoir à réfléchir à une réponse en leur proposant un ensemble limité de choix. 
    - Les **actions suggérées** sont des boutons qui déclenchent une action sur l'appareil de l'utilisateur. Ils se composent généralement d'un ou deux mots descriptifs et d'une icône visuelle pour aider l'utilisateur à comprendre ce que fait le bouton. Braze prend actuellement en charge les actions suggérées OpenURL. Le fonctionnement est similaire à celui d'une URL : les utilisateurs qui sélectionnent le bouton sont redirigés vers une page web ou un autre emplacement/localisation identifié par une URL. 

Un GIF de trois actions suggérées pour un message RCS promouvant les styles de mode en vogue : "La royauté des contes de fées", "L'université à la mode" et "Montrez-moi vos autres styles".]({% image_buster /assets/img/rcs/rcs_suggested_actions.gif %}){: style="max-width:70%;"}

#### Considérations

- En ce qui concerne les limites de caractères du texte, vous pouvez écrire jusqu'à 160 caractères pour un message RCS en texte seul (de base) ou jusqu'à 3072 pour un message RCS riche (unique). 
- Pour les limites de boutons, vous pouvez ajouter jusqu'à cinq boutons par message. Ces boutons peuvent être des suggestions d'actions ou de réponses.
- Les blocs de texte trop longs et les boutons trop nombreux peuvent frustrer les utilisateurs. Dans la mesure du possible, nous vous recommandons donc de miser sur la simplicité. 
- Dans certains cas, il peut être plus rentable d'envoyer des messages texte plus longs par RCS que par SMS. En effet, les messages SMS plus longs sont décomposés en plusieurs segments, chacun d'entre eux étant facturable, alors que les messages RCS sont plutôt facturés par message. Contactez votre gestionnaire de compte Braze pour plus de détails et de conseils.
{% endtab %}

{% tab Media %}
Les messages média RCS vous permettent d'utiliser des formats média attrayants qui ne sont pas possibles avec les SMS. Il s'agit notamment de fichiers d'images, de vidéos et de documents. Ces options médiatiques existent pour vous aider à engager votre audience encore plus profondément et permettre des cas d'utilisation entièrement nouveaux. Pour l'instant, seul le téléchargement d'images est pris en charge par la [bibliothèque multimédia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). 

#### Fonctionnalités

- Les types de messages multimédias prennent en charge tout ce qui est disponible dans les types de messages textuels, à savoir le texte, les réponses suggérées et les actions suggérées.
- Prend en charge les fichiers d'images, y compris les formats de fichiers JPEG et PNG. Les fichiers images sont disponibles par téléchargement à partir de la bibliothèque multimédia. 
- Prend en charge les fichiers vidéo, y compris les formats MP4, MPEG et MV4. Les fichiers vidéo peuvent être ajoutés par URL directement dans le compositeur de messages. 
- Prend en charge les fichiers de documents au format PDF. Les fichiers de documents peuvent être ajoutés par l'intermédiaire de l'URL directement dans le compositeur de messages. 

\![RCS compositeur avec une option pour télécharger un fichier média.]({% image_buster /assets/img/rcs/rcs_media_type.png %})

#### Spécifications des fichiers

| Type de fichier | Spécifications |
| --- | --- |
| Tous | \- La taille des fichiers est limitée à 100 Mo <br><br>\- L'URL du fichier peut comporter jusqu'à 2048 caractères |
| Fichiers images | Les formats de fichiers pris en charge sont JPG, JPEG et GIF.
| Fichiers vidéo | Les formats de fichiers pris en charge sont les suivants : H263, M4V, MP4, MPEG-4, MPEG, WEBM. |
| Dossiers de documents | Formats de fichiers pris en charge : PDF (EN ANGLAIS) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Considérations

L'expérience de l'utilisateur lors de la réception de messages RCS peut varier légèrement en fonction d'un certain nombre de facteurs, notamment la couverture de l'opérateur dans le pays de destination, le matériel de l'appareil mobile et le système d'exploitation de l'appareil mobile. 

D'une manière générale, RCS s'intègre plus naturellement aux appareils Android (cette méthode a été largement mise en œuvre par Google, et l'envoi de messages RCS d'égal à égal est largement adopté par la communauté Android). Des appareils différents peuvent restituer l'expérience à des vitesses et avec des qualités différentes.  
{% endtab %}
{% endtabs %}

### Étape 3 : Composez votre message RCS

Rédigez votre message en utilisant les langues et la personnalisation[(Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) et emojis) selon vos besoins. Veillez à respecter les limites fixées pour les messages afin de réduire les risques de frais supplémentaires.

{% alert important %}
Avant de poursuivre, lisez nos [lignes directrices concernant les limites des messages RCS.](#step-2-select-your-rcs-message-type) Les messages RCS sont [facturés par message]({{site.baseurl}}/sms_rcs_billing_calculators/), il est donc utile de comprendre les nuances de ce qui peut être inclus dans chaque type de message RCS.
{% endalert %}

### Étape 4 : Prévisualisez et testez votre message

Braze recommande toujours de prévisualiser et de tester votre message avant de l'envoyer. Accédez à l'onglet **Test** pour envoyer un RCS de test à des groupes de test de contenu ou à des utilisateurs individuels, ou prévisualiser le message en tant qu'utilisateur directement dans Braze.

### Étape 5 : Créez le reste de votre campagne ou Canvas

Ensuite, créez le reste de votre campagne ou Canvas. Reportez-vous aux sections suivantes pour plus de détails sur la meilleure façon d'utiliser nos outils pour créer des messages RCS.

#### Étape 5.1 : Choisissez la planification ou le déclencheur de la réception/distribution

Les messages RCS peuvent être envoyés en fonction d'une heure planifiée, d'une action ou d'un déclencheur API. Pour en savoir plus, reportez-vous à la section [Planification de votre campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Pour la réception/distribution par événement, vous pouvez également définir la durée de la campagne et les heures calmes.

Spécifiez vos contrôles de réception/distribution, par exemple en autorisant les utilisateurs à se réinscrire pour recevoir la campagne ou en activant des règles de limitation de fréquence.

#### Étape 5.2 : Choisissez les utilisateurs à cibler

Ciblez les utilisateurs en choisissant des segments ou des filtres pour réduire votre audience. Vous devriez avoir déjà sélectionné le groupe d'abonnement, qui restreint les utilisateurs en fonction du niveau ou de la catégorie de communication qu'ils souhaitent avoir avec vous.

{% multi_lang_include target_audiences.md %}

Ensuite, vous sélectionnerez l'audience la plus large à partir de vos segments et vous restreindrez davantage cette segmentation à l'aide de [filtres]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) facultatifs. Vous obtiendrez automatiquement un aperçu de ce à quoi ressemble actuellement cette segmentation approximative de la population. N'oubliez pas que l'appartenance exacte à un segment est toujours calculée juste avant l'envoi du message.

{% alert tip %}
Vous souhaitez utiliser le reciblage RCS pour cibler les utilisateurs en fonction de leurs interactions par SMS et RCS ? Reportez-vous à la rubrique " [reciblage"]({{site.baseurl}}/sms_mms_rcs_user_retargeting/).
{% endalert %}

#### Étape 5.3 : Choisissez des événements de conversion

Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques, ou événements de conversion, après avoir reçu une campagne. Vous pouvez autoriser une fenêtre de 30 jours maximum pendant laquelle une conversion sera comptabilisée si l'utilisateur effectue l'action spécifiée.

Les événements de conversion vous aident à mesurer le succès de votre campagne. Par exemple :
- Si vous utilisez le géociblage pour déclencher un message RCS dont l'objectif final est que l'utilisateur effectue un achat, définissez l'événement de conversion sur **Achat**.
- Si vous essayez de conduire l'utilisateur vers votre application, définissez l'événement de conversion sur **Démarrage de la session.**

Vous pouvez également définir des événements de conversion personnalisés en fonction de votre cas d'utilisation spécifique. Faites preuve de créativité dans la manière dont vous souhaitez réellement mesurer le succès de votre campagne.

### Étape 6 : Examiner et déployer

Une fois que vous avez fini de créer votre campagne ou votre canvas, vérifiez-en les détails, testez-le, puis envoyez-le !

Ensuite, reportez-vous à la section [Rapports pour les SMS, MMS et RCS]({{site.baseurl}}/sms_mms_rcs_reporting/) pour savoir comment accéder aux résultats de vos campagnes RCS.

## Conseils

### Utilisation de Liquid pour la personnalisation des messages

Si vous envisagez d'utiliser Liquid, veillez à inclure une valeur par défaut pour la personnalisation choisie. Ainsi, si le profil utilisateur du destinataire est incomplet, il ne recevra pas un marque substitutive vierge `Hi, !` au lieu de son nom ou d'une phrase cohérente.

### Générer des copies d'intelligence artificielle

Vous avez besoin d'aide pour créer un texte attrayant ? Essayez d'utiliser l'[assistant de rédaction de l'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Saisissez le nom ou la description d'un produit, et l'intelligence artificielle générera un texte marketing semblable à celui d'un humain, que vous pourrez utiliser dans vos messages.

!Compositeur de messages avec une icône pour ouvrir l'assistant de rédaction de l'intelligence artificielle.]({% image_buster /assets/img/rcs/rcs_ai_copywriter.png %}){: style="max-width:70%;"}

## Questions fréquemment posées

### Puis-je envoyer des messages vocaux pré-enregistrés avec RCS ?

Oui, vous pouvez utiliser les messages multimédia pour prendre en charge les fichiers audio.
