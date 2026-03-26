---
nav_title: Alertes
article_title: Bonnes pratiques pour les alertes
description: "Informations, directives et exemples pour les types d'alertes utilisés dans la documentation Braze."
page_order: 2
noindex: true
---

# Bonnes pratiques pour les alertes

> Ce document contient des informations, des directives générales et des exemples pour les types d'alertes utilisés dans la documentation Braze.

## Types d'alertes {#alert-types}

Les alertes permettent de catégoriser les informations dont le lecteur doit avoir connaissance. Quatre types d'alertes peuvent être utilisés dans notre documentation :

* Important  
* Note  
* Conseil  
* Avertissement

## Quand utiliser une alerte {#when-to-use-an-alert}

Utilisez les alertes pour attirer l'attention du lecteur sur des informations importantes. Le contenu doit rester court et aller droit au but. L'objectif est de s'assurer que l'information reste en mémoire.

Consultez le tableau suivant pour les définitions de chaque alerte :

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<colgroup><col style="width: 20%;"><col style="width: 80%;"></colgroup>
<thead>
<tr><th>Type d'alerte</th><th>Définition</th></tr>
</thead>
<tbody>
<tr><td>Important</td><td>Inclut des informations essentielles que le lecteur <strong>devrait</strong> prendre en compte, telles que : <ul><li>Fonctionnalités obsolètes</li><li>Impacts sur la facturation</li><li>Informations relatives aux mises à jour pertinentes</li><li>Mises en garde importantes concernant des fonctionnalités (ex. : fonctionnalités en bêta)</li><li>Autres informations importantes à retenir</li></ul></td></tr>
<tr><td>Note</td><td>Inclut des informations ponctuelles que le lecteur devrait connaître, telles que : <ul><li>Mises en garde concernant des fonctionnalités</li><li>Conseils de mise en forme</li><li>Rappels utiles</li><li>Informations rétrogradées depuis une alerte Important en raison d'une baisse de criticité du contenu (ex. : une alerte Important de longue date devenant une simple note)</li></ul></td></tr>
<tr><td>Conseil</td><td>Inclut des connaissances complémentaires et des recommandations dont le lecteur devrait avoir connaissance, telles que : <ul><li>Articles de résolution des problèmes supplémentaires</li><li>Étapes et raccourcis qui améliorent l'utilisation (ex. : personnalisation supplémentaire pour les messages in-app)</li></ul></td></tr>
<tr><td>Avertissement</td><td>Inclut des informations essentielles que le lecteur doit impérativement prendre en compte, pouvant inclure : <ul><li>Conséquences irréversibles (ex. : suppression de campagnes et de Canvas)</li><li>Comportements entraînant un dysfonctionnement de la fonctionnalité</li><li>Perte de données</li><li>Autres avertissements critiques</li></ul></td></tr>
</tbody>
</table>
{:/}

**Bonnes pratiques pour les alertes**  
Voici des directives générales et des bonnes pratiques pour les alertes.

En règle générale, évitez d'utiliser des alertes pour du contenu essentiel à la structure de l'article (comme les introductions de fonctionnalités, les instructions de configuration et les étapes d'utilisation d'une fonctionnalité). En cas de doute, consultez l'équipe lors de la revue par les pairs.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<colgroup><col style="width: 50%;"><col style="width: 50%;"></colgroup>
<thead>
<tr><th>Directive</th><th>Exemple</th></tr>
</thead>
<tbody>
<tr><td>Expliquez l'information de l'alerte de manière claire et concise.</td><td>{% multi_lang_include alerts/note_alerts.md alert='Segment profiles first app use' %}<br><br> <a href="{{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-4-add-filters-to-your-segment">Alerte Note dans la section Étape 4 : Ajouter des filtres à votre segment</a></td></tr>
<tr><td>Pour les alertes qui s'appliquent à différentes sections d'un même article, envisagez de créer une nouvelle section regroupant ces détails afin d'éviter les répétitions.</td><td>{% multi_lang_include currents/property_details_dispatch_state_source.md %}<br><br> <a href="{{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#subscription-group-state-change-events">Détails des propriétés dans les événements d'engagement liés aux messages</a></td></tr>
<tr><td>Organisez l'information en paragraphes courts ou en listes au sein de l'alerte.</td><td>{% multi_lang_include alerts/important_alerts.md alert='Email via SMS' %}<br><br> <a href="{{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/import_your_email_list/">Alerte Important dans Importer votre liste d'e-mails</a></td></tr>
<tr><td>Tenez compte de toute mise en forme supplémentaire pouvant affecter l'affichage de l'alerte (extraits de code, étapes, images environnantes, etc.).</td><td>{% multi_lang_include alerts/tip_alerts.md alert='catalog data images' %}<br><br> <a href="{{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/#considerations">Alerte Conseil avec extrait de code dans les notifications de baisse de prix</a></td></tr>
<tr><td>Incluez un saut de ligne pour les alertes qui commencent un article.</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_5.png %}" alt="Exemple d'une alerte en début d'article."><br><br> <a href="{{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/implementation_guide/">Guide d'implémentation des cartes de contenu</a></td></tr>
<tr><td>Lorsque vous documentez des fonctionnalités en bêta, incluez une alerte Important mentionnant le statut bêta et les coordonnées de contact Braze. Placez cette alerte bêta après le texte d'aperçu et avant le premier titre principal.</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_6.png %}" alt="Exemple d'une alerte Important pour une fonctionnalité en bêta."></td></tr>
<tr><td>Évitez autant que possible d'utiliser deux alertes ou plus à la suite. Réorganisez plutôt le contenu ou intégrez l'information dans le texte.</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_7.png %}" alt="Exemple de deux alertes côte à côte, ce qui est à éviter."></td></tr>
<tr><td>Si votre alerte est longue, envisagez de créer une nouvelle section présentant l'information sous forme de liste. Par exemple, au lieu d'inclure des étapes de résolution des problèmes dans une alerte, créez une section dédiée ou fournissez un lien vers un article connexe.</td><td><img src="{% image_buster /assets/img/contributing/style_guide/alert_8.png %}" alt="Exemple d'une nouvelle section de contenu."></td></tr>
</tbody>
</table>
{:/}

## Exemples d'alertes {#alert-examples}

Consultez les exemples suivants pour comprendre comment et pourquoi chaque type d'alerte est utilisé dans notre documentation.

### Alerte Important {#important-alert}

{% multi_lang_include alerts/important_alerts.md alert='Web push private browsing' %}

* **Article :** [Push pour le Web]({{site.baseurl}}/user_guide/message_building_by_channel/push/web/)
* **Cas d'utilisation :** Inclut une mise en garde essentielle sur la fonctionnalité que le lecteur doit connaître lors de la configuration de son push web.
* **Justification de l'alerte :** L'alerte Important est préférable à une alerte Note car l'information est particulièrement importante pour le lecteur lors de la configuration de son push web.

{% multi_lang_include alerts/important_alerts.md alert='BCC address billable emails' %}

* **Article :** [Paramètres d'e-mail]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/)
* **Cas d'utilisation :**
  - Fournit une mise en garde importante sur la possibilité de doubler les e-mails facturables
  - Redirige le lecteur vers son Customer Success Manager si nécessaire
* **Justification de l'alerte :** L'alerte Important est utilisée ici pour communiquer des détails sur les adresses CCI dans les paramètres d'e-mail. Cette information est mieux présentée avec une alerte Important plutôt qu'une alerte Avertissement, car l'omission de cette information n'a pas d'impact irréversible sur la fonctionnalité (comme un dysfonctionnement ou une perte de données permanente).

{% multi_lang_include alerts/important_alerts.md alert='Android notification priority' %}

* **Article :** [Paramètres avancés de campagne]({{site.baseurl}}/user_guide/message_building_by_channel/push/android/advanced_campaign_settings/#notification-display-priority)
* **Cas d'utilisation :** Inclut une mise en garde importante sur la priorité des notifications. Redirige le lecteur vers de nouvelles informations disponibles.
* **Justification de l'alerte :** L'alerte Important est idéale ici pour rediriger le lecteur vers les informations actuelles et souligner que la section ne s'applique qu'à certains utilisateurs. Elle est également placée après le titre de section, ce qui oblige le lecteur à prendre connaissance de l'alerte avant de lire le reste de la section.

### Alerte Note {#note-alert}

{% multi_lang_include alerts/note_alerts.md alert='Content Cards frequency capping' %}

* **Article :** [Créer une carte de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/)
* **Cas d'utilisation :** Inclut des informations complémentaires dont le lecteur devrait avoir connaissance en apprenant davantage sur les cartes de contenu.
* **Justification de l'alerte :** Cette alerte Note fournit des informations de contexte sur la façon dont Braze fait tourner les anciennes cartes de contenu pour les utilisateurs. Il s'agit d'une information complémentaire utile qui ne nécessite pas l'utilisation d'une alerte Important ou Conseil.

{% multi_lang_include alerts/note_alerts.md alert='Custom Attributes time attribute' %}

* **Article :** [Attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/)
* **Cas d'utilisation :** Inclut des informations générales dont le lecteur devrait avoir connaissance. Fournit un article pour en savoir plus sur un contenu connexe (attributs temporels).
* **Justification de l'alerte :** Cette information est mieux transmise via une alerte Note plutôt qu'une alerte Important, car le contenu vise à fournir des informations générales. Ignorer cette information n'affecterait pas la facilité d'utilisation de la fonctionnalité.

{% multi_lang_include alerts/note_alerts.md alert='Manage custom data storage' %}

* **Article :** [Gérer les données personnalisées]({{site.baseurl}}/user_guide/data/activation/custom_data/managing_custom_data/#managing-properties)
* **Cas d'utilisation :** Inclut des informations générales dont le lecteur devrait avoir connaissance. Redirige vers le contact Braze pour plus d'informations.
* **Justification de l'alerte :** Cette alerte Note fournit des informations complémentaires sur le stockage des données qui seraient utiles au lecteur lors de la gestion de ses attributs personnalisés. Cependant, le contenu ne nécessite pas une indication plus forte d'importance, une alerte Note est donc appropriée ici.

### Alerte Conseil {#tip-alert}

{% multi_lang_include alerts/tip_alerts.md alert='SMS segment calculator' %}

* **Article :** [Calculateurs de facturation SMS et RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/)
* **Cas d'utilisation :** Inclut un outil permettant au lecteur de comprendre la longueur de son message et le nombre de segments SMS. Fournit des informations potentiellement utiles pour comprendre les limites de caractères.
* **Justification de l'alerte :** Cette alerte Conseil est longue car elle offre un espace pour saisir le texte et voir combien de segments un message génère. L'alerte Conseil est la meilleure option ici car il s'agit d'un générateur utile que le lecteur peut utiliser lors de la configuration de ses messages SMS.

{% multi_lang_include alerts/tip_alerts.md alert='Export troubleshooting' %}

* **Article :** [Exporter les indicateurs clés de performance pour les désinstallations quotidiennes par date]({{site.baseurl}}/api/endpoints/export/kpi/get_kpi_uninstalls_date/)
* **Cas d'utilisation :** Fournit des conseils de résolution des problèmes lors de l'utilisation de cet endpoint.
* **Justification de l'alerte :** L'alerte Conseil apporte un soutien supplémentaire au lecteur. L'alerte Conseil est préférable à une alerte Note car le contenu vise à aider le lecteur en fournissant l'article de résolution des problèmes.

### Alerte Avertissement {#warning-alert}

{% multi_lang_include alerts/warning_alerts.md alert='User profile external_id' %}

* **Article :** [Cycle de vie du profil utilisateur]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/)
* **Cas d'utilisation :** Indique ce que le lecteur ne doit pas faire lors de la création de ses profils utilisateur dans Braze.
* **Justification de l'alerte :** L'alerte Avertissement est utilisée pour mettre en garde le lecteur contre l'attribution d'un external_id avant d'avoir identifié l'utilisateur de manière unique. Cette information est mieux transmise via une alerte Avertissement plutôt qu'une alerte Important car elle implique des conséquences irréversibles pour le profil utilisateur.

{% multi_lang_include alerts/warning_alerts.md alert='Segment Currents multiple connectors' %}

* **Article :** [Segment pour Currents]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment_for_currents/)
* **Cas d'utilisation :** Met en garde le lecteur lors de la création de connecteurs Currents. Inclut les conséquences d'une création incorrecte de ces connecteurs.
* **Justification de l'alerte :** L'alerte Avertissement est idéale ici pour décrire les limitations de l'intégration Braze Segment Currents. L'alerte Avertissement est préférable à une alerte Important car la création incorrecte de plusieurs connecteurs Currents identiques peut entraîner une perte de données.

{% multi_lang_include alerts/warning_alerts.md alert='Canvas race condition audience trigger' %}

* **Article :** [Créer un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
* **Cas d'utilisation :** Liste les informations susceptibles d'empêcher le bon fonctionnement de la fonctionnalité. Détaille comment l'audience visée peut ne pas recevoir la campagne ou ne pas entrer dans le Canvas.
* **Justification de l'alerte :** L'alerte Avertissement est utilisée ici pour signaler un possible dysfonctionnement de la fonctionnalité. Cette information est mieux transmise via une alerte Avertissement plutôt qu'une alerte Important car elle est critique et peut entraîner un dysfonctionnement de la distribution du Canvas.