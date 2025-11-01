---
nav_title: "Filtrage des clics des robots"
article_title: "Filtrage des clics des robots SMS et RCS"
description: "Cet article de référence couvre le filtrage des clics des robots SMS et RCS."
alias: /sms_rcs_bot_click_filtering/
page_type: reference
page_order: 11
channel:
  - SMS
  - RCS
---

# Filtrage des clics des robots SMS et RCS

> Le filtrage des clics de robots par SMS et RCS améliore l'analyse/analytique des campagnes et les flux de travail en excluant les clics de robots présumés. Un "bot click" désigne les clics automatisés sur des liens raccourcis dans les messages SMS et RCS, tels que ceux provenant de robots d'exploration du web, d'aperçus de liens Android et iOS, ou de logiciels de sécurité CPaaS. Cette fonctionnalité facilite l'établissement de rapports précis, la segmentation et l'orchestration pour engager les utilisateurs réels. <br><br> Pour le filtrage des clics des robots dans les campagnes d'e-mail, reportez-vous à la section [Filtrage des robots pour les e-mails]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/bot_filtering/).

## Comment cela fonctionne-t-il ?

Braze dispose d'un système de détection exclusif qui utilise plusieurs entrées pour identifier les clics suspectés de bot, également connus sous le nom d'interactions non humaines (INH). Les bot clics peuvent gonfler les taux d'engagement, ce qui fausse les indicateurs d'engagement. En les filtrant, Braze facilite la saisie de données fiables pour la prise de décision.

Notre système analyse les agents utilisateurs associés aux robots d'indexation, aux aperçus de liens Android et iOS ou aux logiciels de sécurité CPaaS. Quelques exemples d'agents utilisateurs filtrés : `GoogleBot`, `python-requests/2.32.3`, et `Barracuda Sentinel (EE)`.

## Indicateurs et flux de travail affectés

Les indicateurs et flux de travail suivants de Braze sont impactés par les clics des robots :

- **_Nombre total de clics_:** Les analyses de campagne et les analyses Canvas excluront les clics des robots, ne reflétant que les interactions humaines.
- **Filtres de segmentation :** Les filtres de segmentation faisant référence aux interactions avec les liens SMS excluront les clics de robots pour un reciblage plus précis dans les campagnes et les Canvases.
- **Orchestration :** Les clics des robots sont déclenchés par des déclencheurs basés sur l'action et des parcours d'action Canvas qui font référence à des interactions de liens SMS, ce qui permet aux déclencheurs de refléter le comportement humain.
- **Braze Intelligence :**
    - **Sélection intelligente :** Exclut les clics des robots lors de l'optimisation de la sélection des variantes.
    - **Canal intelligent :** Exclut les clics des robots lorsque le SMS ou le RCS est sélectionné pour une sélection précise du canal.
    - **Étapes de l'expérience :** Exclut les clics des robots pour garantir la fiabilité des résultats de l'expérience.
    - **Exportation des données actuelles :** Inclut les champs `is_suspected_bot_click` et `suspected_bot_click_reason` pour faciliter l'analyse des clics humains par rapport aux clics de robots. Ces champs sont disponibles dans [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/), [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) et [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/).

Les désabonnements dus à des clics de robots présumés ne sont pas affectés. Braze traite toutes les demandes de désinscription comme d'habitude. Pour bloquer ces désabonnements, [soumettez vos commentaires sur le produit]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

## Champs actuels dans les événements de clics par SMS

Braze inclut les champs Currents suivants pour les événements de clic SMS :

| Champ d'application | Type de données | Description |
| --- | --- | --- |
| `is_suspected_bot_click` | Booléen | Indique si le clic est suspecté d'être un clic de robot. Renvoie `null` pour tous les utilisateurs jusqu'à ce que le filtrage des clics des robots soit activé pour votre entreprise. Lorsque cette option est activée, elle est alimentée par `true` ou `false` pour tous les nouveaux clics à venir. |
| `suspected_bot_click_reason` | Chaîne de caractères, tableau | Indique la raison d'un clic suspecté d'être le fait d'un robot (par exemple `user_agent`). Se remplit même si le filtrage est désactivé, ce qui permet d'obtenir des informations sur les activités potentielles des robots. Ce champ est disponible globalement et indique une raison pour tous les utilisateurs, même si le filtrage des clics de robots n'est pas encore activé. Cela permet d'avoir des informations sur l'activité potentielle des robots avant d'activer le filtrage des clics des robots. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Modèle de générateur de requêtes

Pour vous aider à analyser vos données, vous pouvez utiliser le modèle mobile préconstruit **Événements de clics SMS par des bots** dans [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/).

## Questions fréquemment posées

### Quel est l'impact du filtrage des clics des robots sur les performances de la campagne ?

Le filtrage n'affecte pas les campagnes déjà envoyées. Lorsqu'il est activé, il réduit les taux de clics à partir de ce moment en excluant les clics des robots.

### Le filtrage des robots empêche-t-il les robots de cliquer sur les liens de désinscription ?

Non. Toutes les demandes de désabonnement sont traitées comme d'habitude.

### Les aperçus de liens sont-ils inclus dans le filtrage des clics des robots ?

Oui. Les aperçus de liens (tels que les aperçus de liens Android et iOS) sont signalés comme des clics de robots et filtrés.

### Comment activer le filtrage des clics des robots ?

Vous devez contacter l'équipe de votre compte Braze pour activer le filtrage des clics des robots pendant l'accès anticipé. Lorsque le filtrage des clics des robots sera disponible, la fonctionnalité sera activée par défaut pour tous les utilisateurs de SMS et de RCS.

Assurez-vous également que vous avez activé le suivi avancé des clics pour le [raccourcissement des liens]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/). Cela vous permet de recevoir l'analyse/analytique des clics du bot, car nous suivons ces données au niveau de l'utilisateur individuel. 

{% alert note %}
Pour plus d'informations, [contactez le service d'assistance]({{site.baseurl}}/braze_support/).
{% endalert %}