---
nav_title: LINE suivi des clics
article_title: LINE Suivi des clics
page_order: 2
description: "Cette page explique comment activer le suivi des clics dans vos messages LINE, tester les liens raccourcis, utiliser votre domaine personnalisé dans les liens suivis, etc."
page_type: reference
alias: /line/click_tracking/
channel:
 - LINE
---

# LINE suivi des clics

> Cette page explique comment activer le suivi des clics dans vos messages LINE, tester les liens raccourcis, utiliser votre domaine personnalisé dans les liens suivis, etc.


Lorsque le suivi des clics LINE est activé, Braze raccourcit automatiquement vos URL, ajoute des mécanismes de suivi et enregistre les clics en temps réel. Alors que LINE vous offre des données agrégées sur les clics, Braze fournit des informations granulaires sur les utilisateurs qui sont opportunes et exploitables. Ces données vous permettent de créer des stratégies de segmentation et de reciblage plus ciblées, par exemple en segmentant les utilisateurs en fonction de leur comportement au clic et en déclenchant des messages en réponse à des clics spécifiques.

Le suivi des clics de LINE peut être utilisé pour les messages textuels, les messages enrichis et les messages sous forme de cartes. Il prend en charge les liens à l'intérieur des boutons et des zones mappées qui ont une URL comme action au clic. Vous pouvez également personnaliser les URL à l'aide de Liquid et de domaines personnalisés.

## Comment cela fonctionne-t-il ?

Vous pouvez gérer les paramètres de suivi des clics de LINE dans l'onglet **Paramètres** lors de la rédaction d'un message. Lorsque cette option est activée, les URL sont raccourcis à l'aide du domaine Braze par défaut (`https://brz.ai`) ou du domaine personnalisé spécifié pour le groupe d'abonnement, et personnalisés pour l'utilisateur.

Tous les URL qui commencent par `http://` ou `https://` seront raccourcis. Un message peut contenir jusqu'à 25 URL. Les URL raccourcis qui contiennent une personnalisation liquide (comme le suivi au niveau de l'utilisateur ou les paramètres UTM) seront valables pendant deux mois.

## Mise en place du suivi des clics

### Messages texte

Pour configurer le suivi des clics pour un message texte :

1. Faites glisser un message **texte** dans le compositeur et ajoutez une URL dans le champ de texte.

\![LINE message composer avec un message texte contenant un long URL : https://braze.com/docs/user_guide/message_building_by_channel/line/create/]({% image_buster /assets/img/line/click_tracking_text_message.png %})

{: start="2"}
2\. Allez dans l'onglet **Paramètres** et confirmez que le **suivi des clics** est activé. Le suivi des clics est activé par défaut pour tous les nouveaux messages.

{% alert note %}
Vous pouvez afficher des aperçus du lien raccourci lorsque vous vous trouvez dans l'onglet **Paramètres** ou **Aperçu du test & **. Le lien complet s'affiche dans le compositeur pendant que vous créez votre message.
{% endalert %}

\![LIGNE message composer l'onglet "Paramètres" avec " avec "Click Tracking" basculé et un aperçu Message texte contenant une URL raccourcie : https://olaf.brz.ai/p/9rcfdqdD]({% image_buster /assets/img/line/click_tracking_settings.png %})

### Des messages riches

Pour configurer le suivi des clics pour un message riche :

1. Faites glisser un **message riche** dans le compositeur et sélectionnez un modèle.
2. Sélectionnez l'**URI** pour le **comportement au clic de la** zone tactile concernée.
3. Saisissez une URL dans le champ **Ouvrir l'URL.** 

!compositeur de messages LINE avec un message Rich avec deux zones à tapoter qui ont chacune une URL.]({% image_buster /assets/img/line/rich_message_click_tracking.png %})

{: start="4"}
4\. Allez dans l'onglet **Paramètres** et confirmez que le **suivi des clics** est activé. Le suivi des clics est activé par défaut pour tous les nouveaux messages.

### Envois de messages par carte

Pour configurer le suivi des clics pour un message basé sur une carte :

1. Faites glisser un **message basé sur une carte** dans le compositeur.
2. Sélectionnez l'**URI** pour le **comportement au clic** pour les zones de carte ou de bouton applicables.

\![LINE message composer avec un message sous forme de carte avec deux boutons qui ont chacun un URL.]({% image_buster /assets/img/line/card_based_message_click_tracking.png %})

{: start="3"}
3\. Allez dans l'onglet **Paramètres** et confirmez que le **suivi des clics** est activé. Le suivi des clics est activé par défaut pour tous les nouveaux messages.

{% alert note %}
Les URL figurant dans les champs **Titre** ou **Description** ne seront pas raccourcis car ces champs ne sont pas cliquables dans LINE.
{% endalert %}

## Domaines personnalisés

Le suivi des clics de LINE vous permet d'utiliser votre propre domaine pour personnaliser l'aspect et la convivialité de vos URL raccourcis, ce qui contribue à donner une image de marque cohérente. Pour plus d'informations, reportez-vous à la section [Domaines personnalisés]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains).

## La personnalisation liquide dans les URL

Vous pouvez construire dynamiquement votre URL directement dans le compositeur Braze, ce qui vous permet d'ajouter des paramètres UTM dynamiques à vos URL ou d'envoyer aux utilisateurs des liens uniques (comme diriger les utilisateurs vers leur panier abandonné ou vers un produit spécifique qui est de nouveau en stock).
Les URL peuvent être générés dynamiquement par l'utilisation de n'importe quelle étiquette Liquid de personnalisation prise en charge.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Vous pouvez également raccourcir les variables Liquid personnalisées, comme le montre l'exemple suivant :

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Raccourcir les URL rendues par les variables Liquid

Braze raccourcit les URL qui sont rendues par Liquid, même celles qui sont incluses dans les propriétés de déclenchement de l'API. Par exemple, si {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} représente un URL valide, nous raccourcirons et suivrons cet URL avant d'envoyer le message LINE.

## Essais

Avant de lancer votre campagne ou votre Canvas, la meilleure pratique consiste à prévisualiser et à tester votre message. Pour ce faire, allez dans l'onglet **Test** pour prévisualiser et envoyer un message LINE à des groupes de test de contenu ou à un utilisateur individuel.

Cet aperçu sera mis à jour avec la personnalisation pertinente et l'URL raccourcie. 

{% alert important %}
Si un brouillon est créé dans un canvas actif, l'URL raccourcie ne sera pas générée. L'URL raccourci est généré lorsque le projet Canvas est rendu actif.
{% endalert %}

## Rapports

Le tableau des performances de la LIGNE comprend la colonne **Total des clics** qui indique le nombre de clics par variante et le taux de clics associé. Pour plus de détails sur les indicateurs de LINE, reportez-vous à la section [Performances des messages de LINE.]({{site.baseurl}}/user_guide/message_building_by_channel/line/reporting)

!Performance pour une étape du canvas LINE.]({% image_buster /assets/img/line/line_step_performance.png %}){: style="max-width:30%;"}

Les données relatives aux clics seront automatiquement reportées dans le tableau de bord analytique. 

\![Tableau de bord de l'analyse/analytique de la performance de la LIGNE (si utilisé comme adjectif anjectif).]({% image_buster /assets/img/line/line_performance.png %})

## Reciblage des utilisateurs

Vous pouvez recibler les utilisateurs qui ont cliqué sur une URL dans un message LINE en utilisant les filtres de segmentation et les déclencheurs suivants :

- Déclencheurs basés sur l'action
    - Interagir avec la campagne
    - Interagir avec Step

!LIGNE de déclenchement de la réception/distribution par événement.]({% image_buster /assets/img/line/line_action_based.png %})

- Filtres de segmentation
    - Campagne cliquée/ouverte
    - Campagne ou canvas cliqué/ouvert avec étiquette 
    - Étape cliquée/ouverte

!Groupe de filtres affichant les trois filtres de segmentation : "Campagne cliquée/ouverte", "Campagne cliquée/ouverte ou canvas avec étiquette" et "Étape cliquée/ouverte".]({% image_buster /assets/img/line/line_segmentation_filters.png %})

## Questions fréquemment posées

### Les liens que je reçois lors de l'envoi de tests sont-ils de véritables URL ?

Oui, de véritables URL seront générées lors de l'envoi de tests. Cependant, l'URL exacte envoyée lors d'une campagne lancée peut différer de celle envoyée lors d'un envoi test.

### Puis-je ajouter des paramètres UTM à une URL avant qu'elle ne soit raccourcie ?

Oui, des paramètres statiques et dynamiques peuvent être ajoutés.

### Combien de temps les URL raccourcis restent-ils valides ?

Les URL personnalisées sont valables deux mois à compter de la date d'enregistrement de l'URL.

### Faut-il installer le SDK de Braze pour raccourcir les URL ?

Non, le suivi des clics fonctionne sans intégration SDK.

### Puis-je savoir quels utilisateurs individuels cliquent sur une URL ?

Oui. Lorsque le suivi des clics est activé, vous pouvez recibler les utilisateurs qui ont cliqué sur des URL en utilisant les [filtres de reciblage LINE.](#retargeting-users)

### Le suivi des clics fonctionne-t-il avec les liens profonds ou les liens universels ?

Le suivi des clics ne fonctionne pas avec les liens profonds. Vous pouvez raccourcir les liens universels à partir de fournisseurs tels que Branch ou Appsflyer, mais Braze n'est pas en mesure de résoudre les problèmes qui peuvent survenir lors de cette opération (comme la rupture de l'attribution ou l'échec de la redirection).

### Les prévisualisations sur l'application LINE comptent-elles comme des clics ?

Non, ils ne contribuent pas au taux de clics des messages LINE.