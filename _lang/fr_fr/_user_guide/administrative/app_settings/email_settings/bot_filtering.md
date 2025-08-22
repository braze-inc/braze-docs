---
nav_title: Filtrage des bots pour les e-mails
article_title: Filtrage des bots pour les e-mails
page_type: reference
page_order: 1
toc_headers: h2
alias: "/bot_filtering/"
description: "Cet article donne un aperçu du filtrage des bots pour les e-mails."
---

# Filtrage des bots pour les e-mails

> Configurez le filtrage des robots dans vos [préférences d'e-mail]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings) pour exclure tous les clics suspectés d'être des machines ou des robots. Un "bot click" dans un e-mail fait référence à un clic sur des hyperliens dans un e-mail qui est généré par un programme automatisé. En filtrant ces clics de robots, vous pouvez déclencher et envoyer intentionnellement des messages à des destinataires qui sont engagés.

{% alert important %}
À partir du 9 juillet 2025, tous les nouveaux espaces de travail créés auront le paramètre de filtrage des robots activé pour des rapports de clics plus précis dans Braze.
{% endalert %}

## À propos des clics de robots

Braze dispose d'un système de détection qui emploie plusieurs entrées pour identifier les clics suspectés de bot, également appelés interactions non humaines (INH). Les bot clics peuvent fausser les indicateurs d'engagement de vos e-mails en gonflant artificiellement les taux de clics. Cette approche nous permet de faire la différence entre les interactions humaines authentiques et les activités présumées des robots afin de préserver l'intégrité des indicateurs et des informations sur l'engagement des clics.

## Indicateurs affectés par les clics des robots

Les indicateurs suivants de Braze peuvent être affectés par les clics des robots :

- Taux de clics totaux
- Taux de clics uniques
- Taux de Click-to-Open
- Taux de conversion (si "Campagne de clics" est sélectionné comme événement de conversion)
- Carte thermique
- Certains filtres de segmentation

Les [fonctionnalités de Braze Intelligence]({{site.baseurl}}/user_guide/brazeai/intelligence) qui exploitent les données de clics en plus de nos systèmes de détection peuvent être impactées. L'activation de ce paramètre peut perturber temporairement nos systèmes de détection, ce qui peut entraîner une diminution de la métrique ou des indicateurs en raison de l'exclusion des clics suspectés d'être ceux d'un bot :

- Sélection intelligente
- Canal intelligent
- Timing intelligent
- Étape de l'expérience
    - Chemin gagnant
    - Chemin personnalisé
- Campagne arrêtée
    - Variante gagnante
    - Variante personnalisée
- Estimation du taux d'ouverture réel

Les désabonnements dus à des clics de robots présumés ne seront pas affectés. Braze continuera à traiter toutes les demandes de désinscription comme d'habitude. Si vous souhaitez que Braze bloque ces désinscriptions, soumettez vos [commentaires sur le produit]({{site.baseurl}}/user_guide/administrative/access_braze/portal).

## Filtres de segmentation affectés par le bot filtering

Les [filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) suivants peuvent être affectés par le filtrage des bots pour les messages e-mail :

- [Campagne ou Canvas avec balise cliqué(e)/ouvert(e)]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-opened-campaign-or-canvas-with-tag)
- [Étape cliquée/ouverte]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-opened-step)
- [Alias cliqué dans la campagne]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-alias-in-campaign)
- [Alias cliqué dans l'étape de Canvas]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-alias-in-canvas-step)
- [Alias cliqué dans n'importe quelle campagne ou étape de canvas]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-alias-in-any-campaign-or-canvas-step)
- [Dernier envoi de messages]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#last-engaged-with-message)
- [Canal intelligent]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#intelligent-channel)

## Activer le filtrage des robots

Allez dans **Paramètres** > **Préférences e-mail.** Sélectionnez ensuite **Supprimer les clics des robots**. Ce paramètre est appliqué au niveau de l'espace de travail.

Tout clic suspecté d'être le fait d'un robot ne sera supprimé qu'après l'activation du paramètre et ne s'appliquera pas rétroactivement aux indicateurs de votre espace de travail.

![Le paramètre de filtrage des e-mails est activé dans les préférences d'e-mail.]({% image_buster /assets/img/bot_tracking_email.png %})

{% alert important %}
Si vous activez ce paramètre et que vous le désactivez par la suite, Braze ne pourra pas rétablir dans votre analyse/analytique les activités des bots précédemment supprimées.
{% endalert %}

## Champs dans les événements de clics sur les e-mails pour Currents et Snowflake

Braze enverra les champs `is_suspected_bot_click` et `suspected_bot_click_reason` dans Currents et Snowflake pour un événement Email Click.

| Champ | Type de données | Description
| `is_suspected_bot_click` | Booléen | Indique qu'il s'agit d'un clic suspecté d'être un bot. Les valeurs envoyées seront nulles jusqu'à ce que vous activiez le paramètre **Remove bots clicks workspace** ( Supprimer les robots de l' espace de travail). Cette approche vous permet de comprendre de manière programmatique quand le filtrage des clics suspectés de bot a commencé dans votre espace de travail, de sorte que vous puissiez comparer avec précision ces données à celles de Currents et Snowflake. |
| `suspected_bot_click_reason` | Array | Indique la raison pour laquelle il s'agit d'un clic suspecté d'être effectué par un robot. Des valeurs telles que `user_agent` et `ip_address` y figureront, même si le paramètre de filtrage de l'espace de travail des robots est désactivé. Ce champ peut fournir des informations sur l'impact potentiel de l'activation de ce paramètre en comparant le nombre de clics provenant de robots présumés aux interactions humaines. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Foire aux questions

### Quel sera l'impact du filtrage des robots sur les performances de ma campagne ?

Cela n'aura pas d'incidence sur les indicateurs des campagnes déjà envoyées. Lorsque le filtrage des robots est activé dans votre espace de travail, Braze commence à filtrer les clics suspectés d'être ceux d'un robot parmi tous les clics. Vous remarquerez peut-être une baisse du taux de clics, mais celui-ci est une représentation plus précise de l'engagement de vos utilisateurs vis-à-vis de leurs messages e-mail.

### Le filtrage des robots empêchera-t-il les robots qui cliquent sur le lien de désabonnement de Braze de se désabonner ?

Non. Toutes les demandes de désabonnement continueront d'être traitées.

### Les ouvertures de machines sont-elles prises en compte dans le filtrage des clics des robots ?

Non.
