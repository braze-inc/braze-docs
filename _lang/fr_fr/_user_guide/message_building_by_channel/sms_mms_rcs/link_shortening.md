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
- Le **suivi avancé** permet de suivre les clics au niveau de la campagne et de l'utilisateur, et d'utiliser les fonctions de segmentation et de reciblage qui s'appuient sur les clics. Les clics génèrent également un [événement SMS]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) envoyé par Currents. Les URL statiques avec suivi avancé auront une longueur de 27 à 28 caractères, ce qui vous permettra de créer des segments d'utilisateurs ayant cliqué sur les URL. Les URL de personnalisation auront une longueur de 32 à 33 caractères.

Les liens sont raccourcis à l'aide de notre domaine court partagé (`brz.ai`). Un exemple d'URL peut ressembler à ceci : `https://brz.ai/8jshX` (basique, statique) ou `https://brz.ai/p/8jshX/2dj8d` (avancé, personnalisé). Pour plus d'informations, reportez-vous à la section [Test](#testing).

Toutes les URL statiques commençant par`http://`ou`https://`sont raccourcies. Les URL raccourcies statiques sont valables pendant un an à compter de leur date de création. Les URL raccourcies contenant une personnalisation Liquid sont valables pendant deux mois.

{% alert note %}
Si vous prévoyez d'utiliser le [filtre de canal intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) <sup>BrazeAITM</sup> et que vous souhaitez que les canaux SMS et RCS soient sélectionnables, activez le raccourcissement de lien avec suivi avancé.
{% endalert %}

## Utilisation du raccourcissement des liens

Pour utiliser le raccourcissement des liens, assurez-vous que la fonction de raccourcissement des liens est activée dans le compositeur de messages. Choisissez ensuite d'utiliser le suivi de base ou le suivi avancé.

![Compositeur de messages avec un bouton bascule pour le raccourcissement des liens.]({% image_buster /assets/img/link_shortening/shortening1.png %})

Braze ne reconnaît que les URL commençant par`http://`ou `https://`. Lorsqu'une URL est reconnue, la section **Aperçu** est mise à jour avec une URL marque substitutive. Braze estime la longueur de l'URL après raccourcissement, mais un avertissement vous invite à sélectionner un utilisateur test et à enregistrer le message comme brouillon pour obtenir une estimation plus précise.

![Compositeur de messages avec une URL longue dans la case "Message" et un lien raccourci généré dans l'aperçu.]({% image_buster /assets/img/link_shortening/shortening3.png %})

### Ajout de paramètres UTM

{% multi_lang_include analytics/click_tracking.md section='UTM parameters' %}

## La personnalisation liquide dans les URL

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

Nous raccourcissons les URL qui sont générées par Liquid, même celles qui sont incluses dans les propriétés de déclencheurs API. Par exemple, si l'URL{% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} est valide, nous raccourcissons et suivons cette URL avant d'envoyer le message. 

### Raccourcir les URL dans`/messages/send`l'endpoint

Le raccourcissement des liens est également activé pour les messages API uniquement via l’[`/messages/send`endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Pour activer également le suivi de base ou avancé, utilisez les paramètres de requête `link_shortening_enabled` ou `user_click_tracking_enabled`.

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| Facultatif | Valeur booléenne | Réglez `link_shortening_enabled` sur `true` pour activer le raccourcissement des liens et le suivi des clics au niveau de la campagne. Pour utiliser le suivi, un `campaign_id` et un `message_variation_id` doivent être présents.|
|`user_click_tracking_enabled`| Facultatif | Valeur booléenne | Définissez `user_click_tracking_enabled` sur `true` pour activer le raccourcissement des liens et le suivi des clics au niveau de la campagne et de l'utilisateur. Vous pouvez utiliser les données suivies pour créer des segmentations d'utilisateurs ayant cliqué sur des URL.<br><br> Pour utiliser ce paramètre, `link_shortening_enabled` doit être `true`, et `campaign_id` et `message_variation_id` doivent être présents. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Pour obtenir une liste complète des paramètres de requête, consultez les [paramètres de requête]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters).

## Test

Avant de lancer votre campagne ou votre Canvas, la meilleure pratique consiste à prévisualiser et à tester votre message. Pour ce faire, accédez à l'onglet **Test** pour prévisualiser et envoyer un message SMS ou RCS à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) ou à un utilisateur individuel. 

Cet aperçu est mis à jour avec la personnalisation pertinente et l'URL raccourcie. Le nombre de caractères et de [segments facturables]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/) est également mis à jour afin de refléter la personnalisation appliquée et l'URL raccourcie.

Veuillez enregistrer la campagne ou le canvas avant d'envoyer un message test afin de recevoir une représentation de l'URL raccourcie qui sera envoyée dans votre message. Si la campagne ou le canvas n'est pas enregistré avant un envoi test, celui-ci inclut une URL marque substitutive.

Pour que les canevas apparaissent dans le filtre « Lien SMS raccourci cliqué », l'étape du canvas contenant le lien raccourci doit également être activée avec le suivi avancé, qui permet le suivi des clics au niveau de l'utilisateur. Si le lien court est configuré avec un suivi de base, l'option permettant de filtrer les événements de clic sur les liens courts SMS n'est pas disponible.

{% alert important %}
Si un brouillon est créé dans un Canvas actif, l'URL raccourcie ne sera pas générée. L'URL raccourci est généré lorsque le projet Canvas est rendu actif.
{% endalert %}

![Message Onglet "Test" avec des champs pour la sélection des destinataires du test.]({% image_buster /assets/img/link_shortening/shortening2.png %})

{% alert note %}
La personnalisation liquide et les URL raccourcis sont modélisés dans l'onglet **Test** après la sélection d'un utilisateur. Assurez-vous qu'un utilisateur est sélectionné pour recevoir un nombre de caractères précis.
{% endalert %}

## Suivi des clics

Lorsque le raccourcissement des liens est activé, le tableau **Performances SMS/MMS/RCS** comprend une colonne intitulée **« Total des clics** » qui affiche le nombre de clics par variante et le taux de clics associé. Pour plus de détails sur les indicateurs, reportez-vous à la section [Performances des messages.]({{site.baseurl}}/sms_mms_rcs_reporting/)

![Tableau des indicateurs de performance des SMS et MMS.]({% image_buster /assets/img/link_shortening/shortening4.png %})

Les tableaux **« Performances historiques** » et **« Performances SMS/MMS/RCS** » comprennent également une option pour **le nombre total de clics** et affichent une série chronologique quotidienne des événements de clic. Les clics sont incrémentés lors de la redirection (par exemple lorsqu'un utilisateur visite un lien) et peuvent être incrémentés plus d'une fois par utilisateur.

## Reciblage des utilisateurs

Pour obtenir des conseils sur le reciblage, consultez le site [Retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links).

{% multi_lang_include analytics/click_tracking.md section='Custom Domains' %}

{% multi_lang_include analytics/click_tracking.md section='Frequently Asked Questions' %}

### Est-il possible de savoir quels utilisateurs cliquent sur une URL ?

Oui. Lorsque le **suivi avancé** est activé, vous pouvez recibler les utilisateurs qui ont cliqué sur des URL en exploitant les [filtres de reciblage par SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) ou les événements de clics par SMS (`users.messages.sms.ShortLinkClick`) envoyés par Currents.

### Le raccourcissement des liens fonctionne-t-il avec des liens profonds ou des liens universels ?

La fonction de raccourcissement de liens ne fonctionne pas avec les liens profonds. Il est également possible de raccourcir les liens universels provenant de fournisseurs tiers tels que Branch ou Appsflyer, mais les utilisateurs peuvent alors rencontrer un bref effet de redirection ou de « scintillement ». Cela se produit parce que le lien raccourci passe d'abord par le Web avant d'être résolu en lien universel qui prend en charge l'ouverture de l'application. De plus, Braze n'est pas en mesure de résoudre les problèmes pouvant survenir lors du raccourcissement des liens universels, tels que la rupture de l'attribution ou les redirections inattendues.

{% alert note %}
Veuillez tester l'expérience utilisateur avant de mettre en œuvre le raccourcissement des liens avec des liens universels afin de vous assurer qu'elle répond à vos attentes.
{% endalert %}

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
