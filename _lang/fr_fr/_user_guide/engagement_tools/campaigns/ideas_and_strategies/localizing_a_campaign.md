---
nav_title: Localisation
page_order: 3
page_type: reference
description: "L’article décrit les avantages des différentes approches d’orchestration dans les campagnes et les Canvas et répertorie les différentes façons dont les utilisateurs peuvent gérer la personnalisation dans leurs envois de message."
tool:
  - Campaigns
  - Canvas

---

# Localisation

> Braze recueille automatiquement les informations d’emplacement des appareils de l’utilisateur après l’intégration du SDK. L’emplacement contient l’identifiant de langue et de région. Cette information est disponible dans l'outil de segmentation de Braze sous **Pays** et **langue**.

Consultez les ressources [iOS](https://developer.apple.com/library/ios/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html) et [Android/FireOS](http://developer.android.com/reference/java/util/Locale.html) suivantes pour obtenir des détails techniques sur la façon dont les paramètres régionaux sont reçus en fonction de votre plateforme.

Pour les entreprises avec des clients dans de nombreux pays, gérer la localisation tôt dans votre parcours Braze peut faire gagner du temps et des ressources à votre entreprise. L’article suivant répertorie les avantages des différentes approches d’orchestration dans les campagnes et les Canvas ainsi que les différentes façons dont les utilisateurs peuvent gérer la personnalisation dans leurs envois de message.

- **Options d'orchestration**
  - [Campagne](#campaign) (un modèle pour tous contre un modèle par pays)
  - [Canevas](#canvas) (un voyage pour tous contre un voyage par pays)<br><br>
- **Options de personnalisation**
  - [Saisie manuelle](#option-1-manual-entry)
  - [Blocs de contenu](#option-2-content-blocks)
  - [Catalogues](#option-3-catalogs)
  - [Partenaires de localisation](#option-4-localization-partners)
  - [Traductions dans une Google Sheet publique](#option-5-translations-in-a-public-google-sheet)
  - [Transformer une feuille de calcul Google en API JSON via SheetDB](#option-6-google-spreadsheet-into-a-json-api-via-sheetdb)

## Orchestration

### Campagne arrêtée

{% tabs local %}
{% tab Un modèle unique pour tous %}

Dans l’approche « un modèle pour tous », la localisation est appliquée à un modèle unique dans Braze à l’aide de [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid). Après l'envoi, le tableau de bord fournit des analyses de campagne agrégées. L'engagement au niveau de l'utilisateur peut être mesuré à l'aide d'entonnoirs de segmentation personnalisés, par exemple en combinant les filtres **Pays** et **Campagne reçue.**

| Avantages | Considérations |
| --- | --- |
| \- Approche centralisée<br>\- Temps de création des e-mails réduit, pas besoin de créer un e-mail plusieurs fois | \- Création manuelle de rapports<br>\- Le rapport de campagne affiche les indicateurs agrégés plutôt que les indicateurs par pays<br>\- Nécessité de tester soigneusement le Liquid pour s’assurer qu’il se remplit comme prévu<br>\- Selon la façon dont vous saisissez la valeur du pays ou le nombre de pays que vous avez paramétrés, il peut être difficile de tester chaque pays<br>\- Envois plus difficiles à planifier pour des heures spécifiques sur plusieurs fuseaux horaires<br>\- Difficile à utiliser si vous souhaitez envoyer un contenu distinct par pays. |
| \--- | \--- | \--- |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Un modèle par pays %}

L’approche « un modèle par pays » sépare les modèles en différents paramètres régionaux d’envoi. Après l'envoi, le tableau de bord présente des analyses d'envoi basées sur chaque pays séparément, et tout événement [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) au niveau de l'utilisateur en aval sera également lié à une campagne spécifique.

- Les modèles bénéficient de la mise en place de [tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags#tags) à des fins de maintenance et de suivi.
- Les campagnes peuvent hériter des configurations du même [modèle Braze]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media#about-templates-and-media) et des [blocs de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) (tels que les [modèles d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template) qui contiennent Liquid).
- Les campagnes et les modèles préexistants peuvent être [dupliqués]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns/) pour permettre un délai de rentabilité plus rapide.

| Avantages | Considérations |
| --- | --- |
| \- Évolutif vers plusieurs emplacements<br>\- Génération de rapports sur les revenus par pays au sein de Braze (par exemple, par campagne)<br>\- Flexibilité en cas de contenu radicalement différent par pays | \- Nécessite une structuration stratégique<br>\- Plus d’efforts de création requis (par exemple, campagnes distinctes pour chaque pays) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### Canvas

{% tabs local %}
{% tab Un voyage pour tous %}

Dans l’approche « Un parcours pour tous », la localisation est gérée dans les [parcours Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/the_basics/#building-the-customer-journey) et Liquid pour définir les envois de message pour chaque utilisateur. 

Après l'envoi d'un canvas, le tableau de bord fournit une [analyse agrégée du canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/), tandis que l'engagement au niveau de l'utilisateur peut être mesuré via des [entonnoirs de segments]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_funnels/) personnalisés, tels que la combinaison des filtres [**Pays**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#country) et [**Étape du canvas reçu**.

| Avantages | Considérations |
| --- | --- |
| \- Approche centralisée<br>\- Temps de création des e-mails réduit : pas besoin de créer un e-mail plusieurs fois. | \- Création manuelle de rapports<br>\- Le rapport de Canvas affiche les indicateurs agrégés plutôt que les indicateurs par pays<br>\- Nécessité de tester soigneusement le Liquid pour s’assurer qu’il se remplit comme prévu<br>\- Selon la façon dont vous saisissez la valeur du pays ou le nombre de pays que vous avez paramétrés, il peut être difficile de tester chaque pays<br>\- Envois plus difficiles à planifier pour des heures spécifiques sur plusieurs fuseaux horaires<br>\- Difficile à utiliser si vous souhaitez envoyer un contenu distinct par pays. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Un voyage par pays %}

Dans l’approche « un parcours par pays », le générateur de parcours [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) offre la flexibilité de créer des parcours utilisateur à l’aide de plusieurs [composants Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/). Ces composants peuvent être [dupliqués]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/duplicating_segments_and_campaigns/#duplicating-canvases) au niveau des composants et de l'ensemble du parcours.

La localisation peut être obtenue par les méthodes suivantes :
- Des Canvas séparés par pays, ce qui garantit que les parcours utilisateur complexes sont définis en haut de l’entonnoir à l’aide de filtres d’audience
- Des parcours utilisateurs sur mesure par pays, la mise en œuvre de [parcours d'audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) pour segmenter intuitivement les utilisateurs à grande échelle pour chaque parcours en créant des fils de messages distincts pour chaque pays dans un seul Canvas.

Une fois envoyé, le tableau de bord fournit des analyses/analytiques dynamiques par pays et au sein des événements [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) au niveau de l'utilisateur, en fonction de l'emplacement/localisation actuel du client.

| Avantages | Considérations |
| --- | --- |
| \- Génération de rapports sur les revenus par pays au sein de Braze (par exemple, par canvas, variante ou étape)<br>\- Flexibilité en cas de contenu radicalement différent par pays<br>\- Peut ajouter d’autres canaux dans le cadre du parcours à l’avenir | \- Nécessite une structuration stratégique<br>\- Plus d'efforts de création requis (par exemple, des étapes de messages distinctes pour chaque pays)<br>\- Le Canvas peut devenir volumineux et difficile à lire si vous avez des parcours personnalisés et complexes pour chaque pays dans un même Canvas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Personnalisation

### Option 1 : Saisie manuelle

La saisie manuelle vous oblige à coller manuellement votre contenu dans le corps de votre message et à utiliser [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) pour afficher [de manière conditionnelle]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) la langue correcte au destinataire.

{% raw %}
```liquid
{% if ${language} == 'en' %}
This is a message in English from Braze!
{% elsif ${language} == 'es' %}
Este es un mensaje en español de Braze !
{% elsif ${language} == 'zh' %}
这是一条来自Braze的中文消息。
{% else %}
This is a message from Braze! This will go to anyone who does not match the other specified languages!
{% endif %}
```
{% endraw %}

Pour ce faire, utilisez le format ci-dessus ou le tableau de bord de Braze : 
1. Lorsque vous composez votre message, sélectionnez le bouton **Langue** pour générer une logique conditionnelle liquide pour chaque langue sélectionnée.
2. Après avoir inséré votre texte modélisé dans votre message, saisissez différentes variantes pour chaque langue. Pour chaque champ ayant une modélisation, vous devez saisir les variations après le segment entre crochets de modélisation. La variation doit correspondre au code de langue référencé entre crochets avant lui.
3. Testez votre message avant de l’envoyer en saisissant l’ID d’un utilisateur ou un e-mail pour vérifier comment un message apparaîtrait à une personne en fonction de sa langue. 

{% alert tip %}
Nous recommandons toujours d'inclure une déclaration {% raw %}`{% else %}`{% endraw %} dans votre message. Alors que la plupart des utilisateurs verront des envois de messages pour leur langue spécifique, le texte sera visible pour ceux qui :
- Aucune langue sélectionnée
- Ont une langue qui n’est pas prise en charge par Braze
- Disposent d’un appareil pour lequel la langue est indétectable
{% endalert %}

### Option 2 : Blocs de contenu

Les [blocs de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks) Braze sont des blocs de contenu réutilisables. Lorsqu'un bloc est modifié, toutes les références à ce bloc sont modifiées. Par exemple, les mises à jour de l'en-tête ou du pied de page d'un e-mail seront répercutées dans tous les e-mails ou dans les traductions en interne. Ces blocs peuvent également être [créés]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/#create-content-block) et [mis à jour]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) à l'aide de l'API REST, et les utilisateurs peuvent charger des traductions par programmation. 

Lors de la création d’une campagne dans le tableau de bord, les blocs de contenu peuvent être référencés à l’aide d’une balise {% raw %}`{{content_blocks.${name_of_content_block}}}`{% endraw %} Ces blocs peuvent contenir toutes les traductions logées dans une logique conditionnelle pour chaque langue, comme indiqué dans l'option 1, ou un bloc séparé pour chaque langue peut être utilisé.

Les blocs de contenu peuvent également être utilisés comme processus de gestion de la traduction où le contenu qui nécessite une traduction est hébergé dans un bloc de contenu, récupéré, traduit, puis mis à jour :
1. Créez manuellement un bloc de contenu dans le tableau de bord avec la balise « Nécessite une traduction ».
2. Votre service effectue une extraction nocturne de tous les blocs de contenu à l'aide de l'[endpoint `/content_blocks/list`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/).
3. Votre service récupère les détails de chaque bloc de contenu via l'[endpoint `/content_blocks/info`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) afin d’identifier les blocs tagués pour traduction.
4. Votre service de traduction traduit le corps de tous les blocs de contenu indiquant « Nécessite une traduction ».
5. Votre service utilise l'[endpoint `/content_block/update`]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) pour mettre à jour le contenu traduit et l'étiquette avec la mention « Traduction terminée ».

### Option 3 : Catalogues

[Les catalogues]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/) vous permettent d'accéder aux données des objets JSON importés via l'API et les fichiers CSV afin d'enrichir vos messages, de manière similaire aux attributs personnalisés ou aux propriétés d'événements personnalisés via Liquid. Par exemple :

{% tabs local %}
{% tab API %}

Créez un catalogue à l’aide de l’appel API suivant :
```json
curl --location --request POST 'https://your_api_endpoint/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "catalogs": [
   {
     "name": "translations",
     "description": "My localization samples",
     "fields": [
       {
         "name": "id",
         "type": "string"
       },
       {
         "name": "context",
         "type": "string"
       },
       {
         "name": "language",
         "type": "string"
       },
       {
         "name": "body",
         "type": "string"
       }
     ]
   }
 ]
}'
```
Ajoutez des éléments à l’aide de l’appel API suivant :
```json
curl --location --request POST 'https://your_api_endpoint/catalogs/translations/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "items": [
   {
     "id": "1",
     "context": "1",
     "language": "en",
     "body": "Hey"
   },
   {
     "id": "2",
     "context": "1",
     "language": "es",
     "body": "Hola"
   },
   {
     "id": "3",
     "context": "1",
     "language": "pt",
     "body": "Oi"
   },
   {
     "id": "4",
     "context": "1",
     "language": "de",
     "body": "Hallo"
   }
 ]
}'
```
{% endtab%}
{% tab CSV %}
Créez un fichier CSV au format suivant :

| id | contexte | langue | body |
| --- | --- | --- |
| 1 | 1 | en | Hé |
| 2 | 1 | es | Hola |
| 3 | 1 | pt | Oi |
| 4 | 1 | de | Hallo |
| 5 | 2 | en | Hé |
| 6 | 2 | es | Hola |
| 7 | 2 | pt | Oi |
| 8 | 2 | de | Hallo |
| 9 | 3 | en | Hé |
| 10 | 3 | es | Hola |
| 11 | 3 | pt | Oi |
| 12 | 3 | de | Hallo |

{% endtab %}
{% endtabs %}

Ces éléments du catalogue peuvent ensuite être référencés à l'aide de la [personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#using-catalogs-in-a-message), illustrée ci-dessous, ou de [sélections]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections) qui vous permettent de créer des groupes de données. 

{% raw %}
```liquid
{% catalog_items translations 1 %}
{{items[0].body}} 

//returns “Hey”
```
{% endraw %}

### Option 4 : Ajouter un paramètre régional

Ajoutez et utilisez les [paramètres locaux dans vos messages]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales) pour cibler les utilisateurs dans différentes langues au sein d'une même campagne e-mail ou d'un même Canvas. 

{% alert important %}
Cette fonctionnalité est actuellement disponible en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}


### Option 5 : Partenaires de localisation

De nombreux partenaires de Braze proposent des solutions de localisation, notamment [Transifex]({{site.baseurl}}/partners/message_personalization/localization/transifex/#about-transifex) et [Crowdin](https://crowdin.com/). Généralement, les utilisateurs se servent de la plateforme aux côtés d’une équipe interne et d’une agence de traduction. Ces traductions y sont ensuite téléchargées et deviennent accessibles via l’API REST. Ces services s'appuient également souvent sur le [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), ce qui permet aux utilisateurs de récupérer les traductions via l'API.

Par exemple, les appels de contenu connecté suivants font appel à Transifex et Crowdin pour récupérer une traduction, en s'appuyant sur {% raw %}`{{${language}}}`{% endraw %} afin d’identifier la bonne traduction pour un utilisateur donné. Cette traduction est ensuite enregistrée dans le bloc JSON « chaînes » et référencée.

{% tabs local %}
{% tab Exemple de Transifex %}
{% raw %}
```liquid
{% connected_content https://www.transifex.com/api/2/project/example/resource/example/translation/{{${language}}}/strings :basic_auth semc :save strings %}
{{strings[0].translation}}
```
{% endraw %}
{% endtab %}
{% tab Exemple de Crowdin %}
{% raw %}
```liquid
{% connected_content https://api.crowdin.com/api/project/braze-test/export-file?key=you_api_key&language={{${language}}}&file=test.json&export_translated_only=1 :save response %}
{{response.value_1}}
```
{% endraw %}
{% endtab %}
{% endtabs %}

### Option 6 : Traductions dans une Google Sheet publique 

Une autre option de traduction comprend le fait de les héberger dans Google Sheets. Souvent, cela peut être géré en partenariat avec une agence de traduction. Les traductions hébergées ici peuvent être interrogées à l’aide du Contenu connecté. La traduction pertinente pour un utilisateur en fonction de sa langue sera ensuite insérée dans le corps de la campagne au moment de l’envoi. 

{% alert note %}
L’API Google Sheets a une limite de 500 requêtes par 100 secondes par projet. Les appels de contenu connecté peuvent être mis en cache, mais cette solution ne peut pas être mise à l’échelle d’une campagne à fort trafic.
{% endalert %}

### Option 7 : Transformer une feuille de calcul Google en API JSON via SheetDB  

Cette option offre une méthode alternative pour transformer Google Sheets en objets JSON interrogés à l’aide du Contenu connecté. En transformant une feuille de calcul en API JSON via SheetDB, vous pouvez choisir parmi [plusieurs niveaux d'abonnement](https://sheetdb.io/pricing) en fonction de la cadence des appels à l'API.

La structure de la feuille de calcul suit les étapes de l'option 4, mais SheetDB fournit également des [filtres supplémentaires](https://docs.sheetdb.io/#sheetdb-api) pour interroger les objets.

Certains utilisateurs préféreront peut-être mettre en œuvre SheetDB avec moins de dépendances Liquid et Connected Block en implémentant la [méthode de recherche de](https://docs.sheetdb.io/#get-search-in-document) SheetDB dans les appels de requête GET pour filtrer les objets JSON sur la base de l'étiquette Liquid {% raw %}`{{${language}}}`{% endraw %} afin de renvoyer automatiquement les résultats pour une seule langue plutôt que de créer de grands blocs conditionnels.

#### Étape 1 : Formater la Google Sheet

Tout d’abord, créez la Google Sheet de sorte que les langues soient des objets différents :

| langue | titre1 | corps1 | titre2 | corps2 |
| en | Hey | 1 | Hey2 | 5 |
| es | Hola | 2 | Hola2 | 6 |
| pt | Oi | 3 | Oi2 | 7 |
| de | Hallo | 4 | Hallo2 | 8 |

#### Étape 2 : Utiliser la balise Liquid de langue dans un appel de Contenu Connecté

Ensuite, implémentez l'étiquette Liquid {% raw %}`{{${language}}}`{% endraw %} dans un appel de contenu connecté. Notez que SheetDB génère automatiquement le site `sheet_id` lors de la création de la feuille de calcul.

{% raw %}
```liquid
{% connected_content https://sheetdb.io/api/v1/[sheet_id]/search?language={{${language}}} :save result%}
```
{% endraw %}

#### Étape 3 : Modélisez vos messages

Enfin, utilisez le Liquid pour modéliser vos messages :

{% raw %}
```liquid
{{result[0].title1}} //returns “Hey”
{{result[0].title2}} //returns “Hey2”
```
{% endraw %}

##### Considérations

- Le champ {% raw %}`{{${language}}}`{% endraw %} doit être défini pour tous les utilisateurs ; dans le cas contraire, un bloc conditionnel Liquid doit être fonctionnalité en tant que traitement de repli pour les utilisateurs ne disposant pas d'une langue.
- La modélisation des données dans Google Sheets doit suivre un autre segment vertical axé sur la langue plutôt que d’avoir des objets Message.
- SheetDB propose un compte gratuit limité et plusieurs options payantes qu'il convient d'envisager en fonction de votre stratégie de campagne. 
- Les appels de contenu connecté peuvent être mis en cache. Nous vous recommandons de mesurer la cadence prévue des appels à l'API et d'étudier une autre approche consistant à appeler l'endpoint principal de SheetDB au lieu d'utiliser la méthode de recherche.