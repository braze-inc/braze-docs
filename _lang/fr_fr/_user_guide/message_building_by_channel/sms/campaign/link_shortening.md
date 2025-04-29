---
nav_title: Raccourcissement de lien
article_title: Raccourcissement de lien
page_order: 5
description: "Cet article de référence explique comment activer le raccourcissement des liens dans vos messages SMS et répond à quelques questions fréquemment posées."
page_type: reference
alias: "/link_shortening/"
tool:
  - Campaigns
channel:
  - SMS
---

# Raccourcissement de lien

> Le raccourcissement de lien et le suivi des clics vous permettent de raccourcir automatiquement les URL contenues dans les messages SMS et de recueillir des analyses du taux de clics, fournissant ainsi des indicateurs d’engagement supplémentaires pour comprendre le comportement des utilisateurs dans le cadre de vos campagnes SMS. <br><br> Cette page explique comment activer le raccourcissement des liens dans vos messages SMS, tester les liens raccourcis, utiliser votre domaine personnalisé dans les liens raccourcis, etc.

Le raccourcissement des liens et le suivi des clics peuvent être activés au [niveau de la variante du message]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#step-1-create-your-campaign) dans les campagnes et les toiles. 

La longueur de l'URL est déterminée par le type de suivi activé :
- Le **suivi de base** permet le suivi des clics au niveau de la campagne. Les URL statiques ont une longueur de 20 caractères et les URL dynamiques ont une longueur de 25 caractères.
- Le **suivi avancé** permet un suivi des clics au niveau de la campagne et au niveau de l'utilisateur. Les clics génèrent également un [événement SMS]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) envoyé par Currents. Les URL statiques avec suivi avancé auront une longueur de 27-28 caractères, ce qui vous permettra de créer des segmentations d'utilisateurs ayant cliqué sur les URL. Les URL dynamiques ont une longueur de 32 à 33 caractères.

Les liens seront raccourcis en utilisant notre domaine court partagé (`brz.ai`). Un exemple d'URL peut ressembler à ceci : `https://brz.ai/8jshX` (basique, statique) ou `https://brz.ai/8jshX/2dj8d` (avancé, dynamique). Pour plus d'informations, reportez-vous à la section [Test](#testing).

Tous les URL statiques commençant par `http://` ou `https://` seront raccourcis. Les URL statiques raccourcis seront valables pendant un an à compter de la date de leur création. Les URL raccourcis qui contiennent la personnalisation Liquid seront valables pendant deux mois.

{% alert note %}
Si vous prévoyez d'utiliser le [filtre de canal intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) BrazeAI<sup>TM</sup> et que vous souhaitez que le canal SMS puisse être sélectionné, activez le raccourcissement des liens SMS avec le suivi avancé et le [suivi des clics]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#click-tracking).
{% endalert %}

## Utilisation du raccourcissement des liens

Pour utiliser le raccourcissement de lien, assurez-vous que la fonction de raccourcissement de lien du compositeur de message est activée. Choisissez ensuite d'utiliser le suivi de base ou le suivi avancé.

![Compositeur de messages avec un bouton bascule pour le raccourcissement des liens.][1]

Braze ne reconnaîtra que les URL qui commencent par `http://` ou `https://`. Lorsqu'une URL est reconnue, la section **Aperçu** est mise à jour avec une URL marque substitutive. Braze estimera la longueur de l’URL après le raccourcissement, mais un message d’avertissement vous demandera de sélectionner un utilisateur test et de sauvegarder le message comme brouillon pour une estimation plus précise.

![Compositeur de messages avec une URL longue dans la case "Message" et un lien raccourci généré dans l'aperçu.][3]

### Ajout de paramètres UTM

Si le raccourcissement des liens vous permet de suivre vos URL automatiquement, vous pouvez également ajouter des paramètres UTM à vos URL pour suivre les performances des campagnes dans des outils d'analyse/analytique tiers, tels que Google Analytics.

Pour ajouter des paramètres UTM à votre URL, procédez comme suit :

1. Commencez par votre URL de base. Il s'agit de l'URL de la page que vous souhaitez suivre (par exemple `https://www.example.com`).
2. Ajoutez un point d'interrogation ( ?) après votre URL de base.
3. Ajoutez chaque paramètre UTM séparé par une esperluette (&).

Un exemple est `https://www.example.com?utm_source=newsletter&utm_medium=sms`.

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

Nous raccourcissons les URL qui sont générées par Liquid, même celles qui sont incluses dans les propriétés de déclencheurs API. Par exemple, si {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} représente une URL valide, nous raccourcissons et suivons cette URL avant d'envoyer le SMS. 

### Raccourcir les URL dans l'endpoint /messages/send

Le raccourcissement des liens est également activé pour les messages API uniquement via l’[`/messages/send`endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Pour activer également le suivi de base ou avancé, utilisez les paramètres de requête `link_shortening_enabled` ou `user_click_tracking_enabled`.

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`link_shortening_enabled`| Facultatif | Valeur booléenne | Réglez `link_shortening_enabled` sur `true` pour activer le raccourcissement des liens et le suivi des clics au niveau de la campagne. Pour utiliser le suivi, un `campaign_id` et un `message_variation_id` doivent être présents.|
|`user_click_tracking_enabled`| Facultatif | Valeur booléenne | Définissez `user_click_tracking_enabled` sur `true` pour activer le raccourcissement des liens et le suivi des clics au niveau de la campagne et de l'utilisateur. Vous pouvez utiliser les données suivies pour créer des segmentations d'utilisateurs ayant cliqué sur des URL.<br><br> Pour utiliser ce paramètre, `link_shortening_enabled` doit être `true`, et `campaign_id` et `message_variation_id` doivent être présents. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

Pour obtenir une liste complète des paramètres de requête, consultez les [paramètres de requête]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#request-parameters).

## Test

Avant de lancer votre campagne ou votre Canvas, la meilleure pratique consiste à prévisualiser et à tester votre message. Pour ce faire, allez dans l'onglet **Test** pour prévisualiser et envoyer un SMS à des [groupes de test de contenu]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab#content-test-groups) ou à un utilisateur individuel. 

Cet aperçu sera mis à jour avec la personnalisation pertinente et l'URL raccourcie. Le nombre de caractères et les [segments facturables]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/) seront également mis à jour pour refléter la personnalisation rendue et l'URL raccourcie. 

Veillez à enregistrer la campagne ou le canvas avant d'envoyer un message test afin de recevoir une représentation de l'URL raccourcie qui sera expédiée dans votre message. Si la campagne ou le Canvas n'est pas enregistré avant un envoi de test, l'envoi de test inclura une URL marque substitutive.

{% alert important %}
Si un brouillon est créé dans un Canvas actif, l'URL raccourcie ne sera pas générée. L'URL raccourci est généré lorsque l'ébauche de canvas est activée.
{% endalert %}

![Message Onglet "Test" avec des champs pour la sélection des destinataires du test.][2]

{% alert note %}
La personnalisation liquide et les URL raccourcis sont modélisés dans l'onglet **Test** après la sélection d'un utilisateur. Assurez-vous qu'un utilisateur est sélectionné pour recevoir un nombre de caractères précis.
{% endalert %}

## Suivi des clics

Lorsque le raccourcissement des liens est activé, le tableau des performances SMS et MMS comprend une colonne intitulée **Nombre total de clics** qui indique le nombre de clics par variante et le taux de clics associé. Pour plus de détails sur les indicateurs relatifs aux SMS, consultez la section [Performances des messages SMS.]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/#message-performance)

![Tableau des indicateurs de performance des SMS et MMS.][4]

Les graphiques des **performances historiques** et des **performances des SMS/MMS** comprennent également une option pour le **nombre total de clics** et affichent une série chronologique quotidienne d'événements de clics. Les clics sont incrémentés lors de la redirection (par exemple lorsqu'un utilisateur visite un lien) et peuvent être incrémentés plus d'une fois par utilisateur.

## Reciblage des utilisateurs

Pour obtenir des conseils sur le reciblage, consultez la page sur [le reciblage par SMS.]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/#filter-by-advanced-tracking-links)

## Domaines personnalisés

Le raccourcissement de lien vous permet également d’utiliser votre propre domaine pour personnaliser l’apparence de vos URL raccourcies et présenter une image de marque cohérente. Pour plus d'informations, reportez-vous à la section [Domaines personnalisés]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/custom_domains/).

## Foire aux questions

### Raccourcissement de lien

#### Les liens que je reçois lors des tests sont-ils de vraies URL ?

Si la campagne a été enregistrée en tant que brouillon avant l'envoi du test, oui. Sinon, il s’agit d’une marque substitutive d’URL. Notez que l'URL exacte envoyée lors d'une campagne lancée peut différer de celle envoyée lors d'un envoi test.

#### Le SDK Braze doit-il être installé pour raccourcir des liens ?

Non. Le raccourcissement des liens fonctionne sans aucune intégration SDK.

#### Est-il possible de savoir quels utilisateurs cliquent sur une URL ?

Oui. Lorsque le **suivi avancé** est activé, vous pouvez recibler les utilisateurs qui ont cliqué sur des URL en exploitant les [filtres de reciblage par SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) ou les événements de clics par SMS (`users.messages.sms.ShortLinkClick`) envoyés par Currents.

#### Est-il possible d’ajouter des paramètres UTM à une URL avant qu’elle ne devienne courte ?

Oui. Des paramètres statiques et dynamiques peuvent être ajoutés. 

#### Combien de temps les URL raccourcies restent-elles valides ?

Les URL statiques sont valables un an à compter de la date d'enregistrement de l'URL, par exemple lors du premier envoi. Les URL dynamiques sont valables deux mois à compter de la date d'enregistrement de l'URL.

#### Le raccourcissement des liens fonctionne-t-il avec des liens profonds ou des liens universels ?

La fonction de raccourcissement de liens ne fonctionne pas avec les liens profonds. Vous pouvez raccourcir les liens universels à partir de fournisseurs tels que Branch ou Appsflyer, mais Braze n'est pas en mesure de résoudre les problèmes qui peuvent survenir lors de cette opération (comme la rupture de l'attribution ou la cause d'une redirection).

[1]: {% image_buster /assets/img/link_shortening/shortening1.png %}
[2]: {% image_buster /assets/img/link_shortening/shortening2.png %}
[3]: {% image_buster /assets/img/link_shortening/shortening3.png %}
[4]: {% image_buster /assets/img/link_shortening/shortening4.png %}
[5]: {% image_buster /assets/img/sms/retargeting5.png %}
[6]: {% image_buster /assets/img/sms/retargeting4.png %}
[7]: {% image_buster /assets/img/custom_domain.png %}
[8]: {% image_buster /assets/img/custom_domain2.png %}
[11]: {% image_buster /assets/img/sms/link_shortening10.png %}
[13]: {% image_buster /assets/img/link_shortening/shortening3.png %}   

