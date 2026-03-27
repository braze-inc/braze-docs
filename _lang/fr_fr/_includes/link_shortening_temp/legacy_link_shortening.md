Le raccourcissement de liens et le suivi des clics vous permettent de raccourcir automatiquement les URL contenues dans les messages SMS ou RCS et de collecter des données analytiques sur le taux de clics, fournissant ainsi des indicateurs d'engagement supplémentaires pour mieux comprendre comment les utilisateurs interagissent avec vos campagnes.

Le raccourcissement de liens et le suivi des clics peuvent être activés au [niveau de la variante du message]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign) dans les campagnes comme dans les Canvas.

La longueur de l'URL dépend du type de suivi activé :
- **Le suivi basique** permet le suivi des clics au niveau de la campagne. Les URL statiques auront une longueur de 20 caractères, et les URL personnalisées auront une longueur de 25 caractères.
- **Le suivi avancé** permet le suivi des clics au niveau de la campagne et de l'utilisateur, et active les fonctionnalités de segmentation et de reciblage basées sur les clics. Les clics génèrent également un [événement de clic SMS]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) envoyé via Currents. Les URL statiques avec suivi avancé auront une longueur de 27 à 28 caractères, vous permettant de créer des segments d'utilisateurs ayant cliqué sur des URL. Les URL personnalisées auront une longueur de 32 à 33 caractères.

Les liens sont raccourcis à l'aide de notre domaine court partagé (`brz.ai`) ou de votre domaine de raccourcissement de liens personnalisé. Voici un exemple d'URL raccourcie : `https://brz.ai/8jshX` (basique, statique) ou `https://brz.ai/p/8jshX/2dj8d` (avancé, personnalisé). Consultez la section [Tests](#testing) pour en savoir plus.

Toutes les URL statiques commençant par `http://` ou `https://` sont raccourcies. Les URL raccourcies statiques sont valides pendant un an à compter de leur date de création. Les URL raccourcies contenant une personnalisation Liquid sont valides pendant deux mois.

{% alert note %}
Si vous prévoyez d'utiliser le [filtre de canal intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) BrazeAI<sup>TM</sup> et souhaitez que les canaux SMS et RCS soient sélectionnables, activez le raccourcissement de liens avec le suivi avancé.
{% endalert %}

## Utiliser le raccourcissement de liens

Pour utiliser le raccourcissement de liens, assurez-vous que le bouton de raccourcissement de liens dans le composeur de messages est activé. Choisissez ensuite d'utiliser le suivi basique ou avancé.

![Composeur de messages avec un bouton pour le raccourcissement de liens.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening1.png %})

Braze ne reconnaît que les URL commençant par `http://` ou `https://`. Lorsqu'une URL est reconnue, la section **Prévisualiser** se met à jour avec une URL de marque substitutive. Braze estime la longueur de l'URL après raccourcissement, mais un avertissement vous invite à sélectionner un utilisateur test et à enregistrer le message en tant que brouillon pour obtenir une estimation plus précise.

![Composeur de messages avec une longue URL dans le champ « Message » et un lien raccourci généré dans l'aperçu.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening3.png %})

### Ajouter des paramètres UTM

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## Personnalisation Liquid dans les URL

Vous pouvez construire dynamiquement votre URL directement dans le composeur Braze, ce qui vous permet d'ajouter des paramètres UTM dynamiques à vos URL ou d'envoyer aux utilisateurs des liens uniques (par exemple pour les rediriger vers leur panier abandonné ou vers un produit spécifique de nouveau en stock).

### Créer une URL avec des balises de personnalisation Liquid prises en charge

Les URL peuvent être générées dynamiquement grâce à l'utilisation de n'importe quelle [balise de personnalisation Liquid prise en charge]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Nous prenons également en charge le raccourcissement de variables Liquid personnalisées. Voici quelques exemples :

### Créer une URL à l'aide de variables Liquid

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Raccourcir les URL générées par des variables Liquid

Nous raccourcissons les URL générées par Liquid, y compris celles incluses dans les propriétés de déclenchement API. Par exemple, si {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} représente une URL valide, nous raccourcissons et suivons cette URL avant l'envoi du message.

### Raccourcir les URL dans l'endpoint `/messages/send`

Le raccourcissement de liens est également activé pour les messages API uniquement via l'[endpoint `/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Pour activer également le suivi basique ou avancé, utilisez les paramètres de requête `link_shortening_enabled` ou `user_click_tracking_enabled`.

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| Facultatif | Valeur booléenne | Définissez `link_shortening_enabled` sur `true` pour activer le raccourcissement de liens et le suivi des clics au niveau de la campagne. Pour utiliser le suivi, un `campaign_id` et un `message_variation_id` doivent être présents.|
|`user_click_tracking_enabled`| Facultatif | Valeur booléenne | Définissez `user_click_tracking_enabled` sur `true` pour activer le raccourcissement de liens, ainsi que le suivi des clics au niveau de la campagne et de l'utilisateur. Vous pouvez utiliser les données suivies pour créer des segments d'utilisateurs ayant cliqué sur des URL.<br><br> Pour utiliser ce paramètre, `link_shortening_enabled` doit être défini sur `true`, et un `campaign_id` et un `message_variation_id` doivent être présents. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Pour une liste complète des paramètres de requête, consultez les [paramètres de requête]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters).

## Tests

Avant de lancer votre campagne ou Canvas, il est recommandé de prévisualiser et de tester votre message au préalable. Pour ce faire, accédez à l'onglet **Test** pour prévisualiser et envoyer un message SMS ou RCS à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) ou à un utilisateur individuel.

Cet aperçu se met à jour avec la personnalisation pertinente et l'URL raccourcie. Le nombre de caractères et les [segments facturables]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/) sont également mis à jour pour refléter la personnalisation rendue et l'URL raccourcie.

Assurez-vous d'enregistrer la campagne ou le Canvas avant d'envoyer un message test afin d'obtenir une représentation de l'URL raccourcie telle qu'elle sera envoyée dans votre message. Si la campagne ou le Canvas n'est pas enregistré avant l'envoi test, celui-ci contiendra une URL de marque substitutive.

Pour que les Canvas apparaissent dans le filtre « A cliqué sur un lien SMS raccourci », l'étape du Canvas contenant le lien court doit également être activée avec le suivi avancé, qui permet le suivi des clics au niveau de l'utilisateur. Si le lien court est configuré avec le suivi basique, l'option de filtrage des événements de clic sur les liens courts SMS n'est pas disponible.

{% alert important %}
Si un brouillon est créé au sein d'un Canvas actif, aucune URL raccourcie ne sera générée. L'URL raccourcie réelle est générée lorsque le brouillon du Canvas est activé.
{% endalert %}

![Onglet « Test » du message avec des champs pour sélectionner les destinataires de test.]({% image_buster /assets/img/link_shortening/legacy/temp_shortening2.png %})

{% alert note %}
La personnalisation Liquid et les URL raccourcies sont générées dans l'onglet **Test** après la sélection d'un utilisateur. Assurez-vous de sélectionner un utilisateur pour obtenir un décompte de caractères précis.
{% endalert %}

## Suivi des clics

Lorsque le raccourcissement de liens est activé, le tableau **Performances SMS/MMS/RCS** inclut une colonne intitulée **Total des clics** qui affiche le nombre d'événements de clic par variante ainsi que le taux de clics associé. Pour plus de détails sur les indicateurs, consultez [Performances des messages]({{site.baseurl}}/sms_mms_rcs_reporting/).

![Tableau des indicateurs de performance SMS et MMS.]({% image_buster /assets/img/link_shortening/shortening4.png %})

Les tableaux **Performances historiques** et **Performances SMS/MMS/RCS** incluent également une option pour le **Total des clics** et affichent une série temporelle quotidienne des événements de clic. Les clics sont incrémentés lors de la redirection (par exemple lorsqu'un utilisateur visite un lien) et peuvent être incrémentés plus d'une fois par utilisateur.

## Recibler les utilisateurs

Pour des conseils sur le reciblage, consultez [Reciblage]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links).

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### Puis-je savoir quels utilisateurs individuels cliquent sur une URL ?

Oui. Lorsque le **suivi avancé** est activé, vous pouvez recibler les utilisateurs ayant cliqué sur des URL en utilisant les [filtres de reciblage SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) ou les événements de clic SMS (`users.messages.sms.ShortLinkClick`) envoyés par Currents.

### Le raccourcissement de liens fonctionne-t-il avec les liens profonds ou les liens universels ?

Le raccourcissement de liens ne fonctionne pas avec les liens profonds. En revanche, vous pouvez raccourcir les liens universels provenant de fournisseurs tiers tels que Branch ou Appsflyer, mais les utilisateurs peuvent rencontrer une brève redirection ou un effet de « scintillement ». Cela se produit parce que le lien raccourci passe d'abord par le web avant de résoudre vers le lien universel qui prend en charge l'ouverture de l'application. De plus, Braze n'est pas en mesure de résoudre les problèmes pouvant survenir lors du raccourcissement de liens universels, tels que la rupture de l'attribution ou des redirections inattendues.

{% alert note %}
Testez l'expérience utilisateur avant d'implémenter le raccourcissement de liens avec des liens universels pour vous assurer qu'il répond à vos attentes.
{% endalert %}

### Les `send_ids` sont-ils associés aux événements de clic SMS ?

Non. Cependant, si le suivi avancé est activé, vous pouvez généralement attribuer les `send_ids` aux événements de clic en utilisant le [Query Builder]({{site.baseurl}}/query_builder/) pour interroger les données Currents avec cette requête :

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id 
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL; 
```