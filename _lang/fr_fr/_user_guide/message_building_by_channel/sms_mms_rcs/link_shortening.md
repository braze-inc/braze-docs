---
nav_title: Raccourcissement de lien
article_title: Raccourcissement de lien
page_order: 3
description: "Cet article de référence explique comment activer le raccourcissement des liens dans vos messages SMS et répond à quelques questions fréquemment posées."
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS
---

# Raccourcissement de lien

> Cette page explique comment activer le raccourcissement des liens dans vos messages SMS et RCS, tester les liens raccourcis, utiliser votre domaine personnalisé dans les liens raccourcis, et plus encore.

Le raccourcissement des liens et le suivi des clics vous permettent de raccourcir automatiquement les URL contenues dans les messages SMS ou RCS et de collecter des analyses sur le taux de clics, fournissant ainsi des indicateurs d'engagement supplémentaires pour aider à comprendre comment vos utilisateurs s'engagent dans vos campagnes.

Le raccourcissement des liens et le suivi des clics peuvent être activés au [niveau de la variante du message]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign) dans les campagnes et les toiles. 

La longueur de l'URL est déterminée par le type de suivi activé :
- Le **suivi de base** permet le suivi des clics au niveau de la campagne. Les URL statiques auront une longueur de 20 caractères, et les URL personnalisées auront une longueur de 25 caractères.
- Le **suivi avancé** permet de suivre les clics au niveau de la campagne et de l'utilisateur, et d'utiliser les fonctions de segmentation et de reciblage qui s'appuient sur les clics. Les clics génèrent également un [événement SMS]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) envoyé par Currents. Les URL statiques avec suivi avancé auront une longueur de 27-28 caractères, ce qui vous permettra de créer des segmentations d'utilisateurs ayant cliqué sur les URL. Les URL personnalisées auront une longueur de 32 à 33 caractères.

Les liens seront raccourcis en utilisant notre domaine court partagé (`brz.ai`). Un exemple d'URL peut ressembler à ceci : `https://brz.ai/8jshX` (basique, statique) ou `https://brz.ai/p/8jshX/2dj8d` (avancé, personnalisé). Pour plus d'informations, reportez-vous à la section [Test](#testing).

Tous les URL statiques commençant par `http://` ou `https://` seront raccourcis. Les URL statiques raccourcis seront valables pendant un an à compter de la date de leur création. Les URL raccourcis qui contiennent la personnalisation Liquid seront valables pendant deux mois.

{% alert note %}
Si vous prévoyez d'utiliser le [filtre de canal intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) <sup>BrazeAITM</sup> et que vous souhaitez que les canaux SMS et RCS soient sélectionnables, activez le raccourcissement de lien avec suivi avancé.
{% endalert %}

## Utilisation du raccourcissement des liens

Pour utiliser le raccourcissement des liens, assurez-vous que la fonction de raccourcissement des liens est activée dans le compositeur de messages. Choisissez ensuite d'utiliser le suivi de base ou le suivi avancé.

![Compositeur de messages avec possibilité de basculer vers un raccourcissement des liens.]({% image_buster /assets/img/link_shortening/shortening1.png %})

Braze ne reconnaîtra que les URL qui commencent par `http://` ou `https://`. Lorsqu'une URL est reconnue, la section **Aperçu** est mise à jour avec une URL marque substitutive. Braze estimera la longueur de l’URL après le raccourcissement, mais un message d’avertissement vous demandera de sélectionner un utilisateur test et de sauvegarder le message comme brouillon pour une estimation plus précise.

![Compositeur de messages avec un URL long dans la case "Message" et un lien raccourci généré dans l'aperçu.]({% image_buster /assets/img/link_shortening/shortening3.png %})

### Ajout de paramètres UTM

{% multi_lang_include click_tracking.md section='UTM parameters' %}

## La personnalisation Liquid dans les URL

Vous pouvez construire dynamiquement votre URL directement dans le compositeur Braze, ce qui vous permet d'ajouter des paramètres UTM dynamiques à vos URL ou d'envoyer aux utilisateurs des liens uniques (comme diriger les utilisateurs vers leur panier abandonné ou vers un produit spécifique qui est de nouveau en stock).

### Créez une URL avec les étiquettes de personnalisation Liquid prises en charge.

Les URL peuvent être générés dynamiquement par l'utilisation de n'importe quelle [étiquette Liquid de personnalisation prise en charge]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

{% raw %}
```liquid
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Nous sommes également favorables au raccourcissement des variables Liquid personnalisées. Plusieurs exemples sont présentés ci-dessous :

### Créer une URL à l'aide des variables Liquid

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

### Raccourcir les URL rendues par les variables Liquid

Nous raccourcissons les URL qui sont générées par Liquid, même celles qui sont incluses dans les propriétés de déclencheurs API. Par exemple, si {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} représente un URL valide, nous raccourcirons et suivrons cet URL avant d'envoyer le message. 

### Raccourcir les URL dans l'endpoint /messages/send

Le raccourcissement des liens est également activé pour les messages API uniquement via l’[`/messages/send`endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Pour activer également le suivi de base ou avancé, utilisez les paramètres de requête `link_shortening_enabled` ou `user_click_tracking_enabled`.

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| Facultatif | Valeur booléenne | Réglez `link_shortening_enabled` sur `true` pour activer le raccourcissement des liens et le suivi des clics au niveau de la campagne. Pour utiliser le suivi, un `campaign_id` et un `message_variation_id` doivent être présents.|
|`user_click_tracking_enabled`| Facultatif | Valeur booléenne | Définissez `user_click_tracking_enabled` sur `true` pour activer le raccourcissement des liens et le suivi des clics au niveau de la campagne et de l'utilisateur. Vous pouvez utiliser les données suivies pour créer des segmentations d'utilisateurs ayant cliqué sur des URL.<br><br> Pour utiliser ce paramètre, `link_shortening_enabled` doit être `true`, et `campaign_id` et `message_variation_id` doivent être présents. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Pour obtenir une liste complète des paramètres de requête, consultez les [paramètres de requête]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters).

## Test

Avant de lancer votre campagne ou votre Canvas, la meilleure pratique consiste à prévisualiser et à tester votre message. Pour ce faire, accédez à l'onglet **Test** pour prévisualiser et envoyer un message SMS ou RCS à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) ou à un utilisateur individuel. 

Cet aperçu sera mis à jour avec la personnalisation pertinente et l'URL raccourcie. Le nombre de caractères et les [segments facturables]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/) seront également mis à jour pour refléter la personnalisation rendue et l'URL raccourcie. 

Veillez à enregistrer la campagne ou le canvas avant d'envoyer un message test afin de recevoir une représentation de l'URL raccourcie qui sera expédiée dans votre message. Si la campagne ou le Canvas n'est pas enregistré avant un envoi de test, l'envoi de test inclura une URL marque substitutive.

{% alert important %}
Si un brouillon est créé dans un Canvas actif, l'URL raccourcie ne sera pas générée. L'URL raccourci est généré lorsque l'ébauche de canvas est activée.
{% endalert %}

![Envoi de messages onglet "Test" avec des champs pour la sélection des destinataires du test.]({% image_buster /assets/img/link_shortening/shortening2.png %})

{% alert note %}
La personnalisation liquide et les URL raccourcis sont modélisés dans l'onglet **Test** après la sélection d'un utilisateur. Assurez-vous qu'un utilisateur est sélectionné pour recevoir un nombre de caractères précis.
{% endalert %}

## Suivi des clics

Lorsque le raccourcissement des liens est activé, le tableau des **performances deSMS/MMS/RCS ** comprend une colonne intitulée **Nombre total de clics** qui indique le nombre de clics par variante et le taux de clics associé. Pour plus de détails sur les indicateurs, reportez-vous à la section [Performances des messages.]({{site.baseurl}}/sms_mms_rcs_reporting/)

![Tableau des indicateurs de performance des SMS et MMS.]({% image_buster /assets/img/link_shortening/shortening4.png %})

Les tableaux " **Performances historiques"** et " **PerformancesSMS/MMS/RCS ** " comprennent également une option " **Nombre total de clics** " et affichent une série chronologique quotidienne d'événements liés aux clics. Les clics sont incrémentés lors de la redirection (par exemple lorsqu'un utilisateur visite un lien) et peuvent être incrémentés plus d'une fois par utilisateur.

## Reciblage des utilisateurs

Pour obtenir des conseils sur le reciblage, consultez le site [Retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links).

{% multi_lang_include click_tracking.md section='Domaines personnalisés' %}

{% multi_lang_include click_tracking.md section='Foire aux questions' %}

### Est-il possible de savoir quels utilisateurs cliquent sur une URL ?

Oui. Lorsque le **suivi avancé** est activé, vous pouvez recibler les utilisateurs qui ont cliqué sur des URL en exploitant les [filtres de reciblage par SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) ou les événements de clics par SMS (`users.messages.sms.ShortLinkClick`) envoyés par Currents.

{% alert note %}
Pour l'instant, les événements RCS Click ne sont pas disponibles sur Currents.
{% endalert %}

### Le raccourcissement des liens fonctionne-t-il avec des liens profonds ou des liens universels ?

La fonction de raccourcissement de liens ne fonctionne pas avec les liens profonds. Vous pouvez raccourcir les liens universels à partir de fournisseurs tels que Branch ou Appsflyer, mais Braze n'est pas en mesure de résoudre les problèmes qui peuvent survenir lors de cette opération (comme la rupture de l'attribution ou la cause d'une redirection).

### Le site `send_ids` est-il associé aux clics sur les SMS ?

Non. Toutefois, si vous avez activé le suivi avancé, vous pouvez généralement attribuer `send_ids` aux événements de clic en utilisant [Query Builder]({{site.baseurl}}/query_builder/) pour interroger les données Currents avec cette requête :

```sql
SELECT c.*, s.send_id
FROM USERS_MESSAGES_SMS_SHORTLINKCLICK_SHARED AS c
  INNER JOIN USERS_MESSAGES_SMS_SEND_SHARED AS s
    ON s.user_id = c.user_id 
      AND (s.message_variation_id = c.message_variation_id OR s.canvas_step_message_variation_id = c.canvas_step_message_variation_id)
WHERE s.send_id IS NOT NULL; 
```