---
nav_title: SalesWings
article_title: SalesWings
description: "Cet article de référence présente le partenariat entre Braze et SalesWings, une solution d'opérations de vente et de marketing pour Braze, qui vous aide à qualifier les prospects et les comptes, fournit des informations et des alertes commerciales au sein d'un CRM comme Salesforce ainsi que des rapports d'attribution B2B."
alias: /partners/saleswings/
page_type: partner
search_tag: Partner

---

# SalesWings

> [SalesWings](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs) est une solution SaaS B2B pour les opérations de vente et de marketing, qui permet de gérer la qualification des prospects et des comptes grâce à un système holistique de notation et de classement des prospects, fournit des informations et des alertes sur les ventes, des rapports d'attribution B2B, ainsi qu'une intégration étroite avec le CRM de Salesforce.

_Cette intégration est maintenue par SalesWings._

## À propos de l'intégration

SalesWings permet aux équipes marketing et aux gestionnaires des opérations marketing de qualifier les prospects et les comptes pour leurs équipes commerciales, ce qui est essentiel pour l'alignement des ventes et du marketing et l'efficacité opérationnelle. En outre, SalesWings, conjointement avec Braze, peut faire remonter aux commerciaux le parcours client complet d'un lead et d'un compte, ainsi que les données d'engagement des campagnes marketing de Braze, ce qui vous permet d'augmenter les taux de qualification des leads grâce à des conversations plus éclairées. SalesWings identifie les besoins et les intérêts ainsi que d'autres signaux, ce qui permet de transmettre de manière automatisée les acheteurs qualifiés aux équipes de vente au sein de votre CRM.

## Conditions préalables
 
| Condition | Description |
| ----------- | ----------- |
| Compte SalesWings | Un compte [SalesWings](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs) est nécessaire pour profiter de ce partenariat. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations `users.export.ids`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Votre endpoint dépendra de l'URL de Braze pour votre instance. |
| Segment.com compte (facultatif) | Si vous êtes un utilisateur de Segment.com, vous pouvez envoyer toutes les données d'engagement et de profil des prospects et identifier les événements via Segment.com pour le profilage des prospects. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d’utilisation

{% tabs %}
{% tab Évaluation des prospects et des comptes %}

SalesWings offre aux clients de Braze [un moyen flexible de qualifier les prospects, les contacts et les comptes grâce à des fonctionnalités évoluées d’évaluation](https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs) et de classement des prospects. Toutes vos données de qualification des leads sont nativement poussées vers Salesforce CRM et d'autres systèmes où vous souhaitez gérer et créer des rapports sur les leads, les contacts, les comptes et les opportunités.

![Exemple d'un modèle d’évaluation de prospect simple et sans code dans SalesWings]({% image_buster /assets/img/saleswings/example_lead_scoring_builder_braze_lead_scoring.png %})

_Exemple d'un modèle d’évaluation de prospects simple et sans code dans SalesWings_
{% endtab %}
{% tab Alignement des ventes et du marketing %}
SalesWings permet aux équipes marketing de suivre, de qualifier et de transmettre à vos équipes commerciales les leads qualifiés par le marketing. Toutes les données de SalesWings sont nativement poussées vers Salesforce, et peuvent être exploitées pour affiner n'importe quel processus existant, ou créer de nouveaux processus via des listes, des rapports, des flux, et plus encore.

![Exemple de hiérarchisation d'une liste de prospects ou de contacts par la fonction d’évaluation des prospects de SalesWings directement dans Salesforce]({% image_buster /assets/img/saleswings/prioritized_lead_or_contact_list_braze_lead_scoring.png %})

_Exemple de hiérarchisation d'une liste de prospects ou de contacts par la fonction d’évaluation des prospects de SalesWings en mode natif dans Salesforce_

![Exemple de la façon dont la fonction d’évaluation des prospects de SalesWings a classé une liste de comptes nativement dans Salesforce]({% image_buster /assets/img/saleswings/prioritized_account_list_braze_lead_scoring.png %})

_Exemple de hiérarchisation d'une liste de comptes par la fonction d’évaluation de SalesWings en mode natif dans Salesforce_
{% endtab %}
{% tab Classement des prospects et des comptes %}
SalesWings permet aux clients de Braze de qualifier les prospects et les comptes sur la base de données de profil (généralement des données CRM). On parle également de "classement des prospects", de "notation de l'adéquation" ou de "notation firmographique". Les clients de Braze peuvent envoyer des données d'attribut directement à SalesWings, et SalesWings peut lire les données et les enregistrements des objets standards ou personnalisés de Salesforce CRM pour un scoring holistique du profil.
{% endtab %}
{% tab Informations sur les ventes pour les commerciaux %}
SalesWings vous permet de fournir à vos commerciaux des informations commerciales sur leurs prospects, leurs contacts et leurs comptes (solution alternative à Marketo Sales Insights). Essentiellement, vous pouvez faire remonter en surface toutes les données relatives à l'engagement sur Braze et sur le web à votre équipe de vente. Les informations sont intégrées de manière native dans le CRM Salesforce et peuvent être poussées vers d'autres CRM ou systèmes ou via un e-mail de Braze en tant qu'"alerte commerciale".

![Exemple de vue des informations sur les ventes pour les commerciaux dans Salesforce (également disponible pour d'autres systèmes CRM)]({% image_buster /assets/img/saleswings/marketo_sales_insights_alternative_for_braze.png %}).

_Exemple de vue des informations sur les ventes pour les commerciaux dans Salesforce (également disponible pour d'autres systèmes CRM)._
{% endtab %}
{% tab Alertes commerciales %}
SalesWings propose des alertes natives par e-mail et Slack, et vous pouvez configurer des abonnements aux rapports dans Salesforce auxquels votre équipe commerciale peut accéder pour obtenir des rapports quotidiens, hebdomadaires et mensuels par e-mail. De plus, grâce à une intégration Zapier, vous pouvez créer des workflows supplémentaires basés sur les données de qualification des leads de SalesWings.

![Exemple d'alerte commerciale via le canal Slack]({% image_buster /assets/img/saleswings/smart_watch_alerts.png %})

_Exemple d'alerte commerciale via le canal Slack_
{% endtab %}
{% tab Création de rapports dans Salesforce CRM %}
Grâce à l'intégration native de SalesWings avec Salesforce, vous pouvez créer des rapports automatisés avec des prospects, des contacts, des comptes et des opportunités sur la base des données d'engagement web et de tout engagement de campagne Braze avec une intégration currents Braze native. Par exemple, vous pouvez surfacer une liste de prospects chauds à une équipe de vente, avec tous ceux qui ont cliqué sur une campagne d'e-mail spécifique ou effectué une action spécifique dans votre appli ou votre site web.

![Exemple de tableau de bord lié à l'engagement des e-mails et du marketing de Braze au sein de Salesforce, examinant l'impact des campagnes Braze sur les résultats des ventes et les performances]({% image_buster /assets/img/saleswings/saleswings_email_campaign_attribution_dashboard.png %})

_Exemple de tableau de bord lié à l'engagement e-mail et marketing de Braze dans Salesforce, étudiant l'impact des campagnes de Braze sur les résultats des ventes et les résultats._
{% endtab %}
{% endtabs %}

## Intégration

### Étape 1 : Compte et configuration de SalesWings

[Planifiez une démonstration](https://www.saleswingsapp.com/schedule-a-demo?utm_source=braze&utm_campaign=technicaldocs) avec l'équipe sympathique de SalesWings pour en savoir plus sur SalesWings.

### Étape 2 : Installer un outil de suivi des comportements dans votre site Web ou votre application

Il existe plusieurs façons de collecter des données comportementales dans SalesWings pour le scoring des leads et des comptes, l'identification de l'intention de l'acheteur et les informations commerciales :
* [Déployez les scripts JavaScript de SalesWings](https://support.saleswingsapp.com/en/collections/3285135-1-implementing-saleswings-tracking-script) sur les sites Web et les applications où vous souhaitez suivre et identifier des prospects.
* Intégrez les événements de Braze ainsi que les propriétés d'événement dans SalesWings via Braze Currents.
* Envoyez des données comportementales sur l'activité des prospects (et des données sur le profil des prospects) via l'[intégration de SalesWings avec Segment.](https://support.saleswingsapp.com/en/articles/9258905-segment-com-integration)
* Envoyez des données directement à l'[API de](https://support.saleswingsapp.com/en/articles/6930889-using-saleswings-open-api-to-send-events-to-saleswings) SalesWings à partir d'une solution tierce.

### Étape 3 : Connecter SalesWings à Braze

Allez sur la [page**Intégrations de SalesWings**](https://helium.saleswings.pro/integrations) et développez la section **Intégration de Braze**.

![La section Intégration de Braze de la page Paramètres de SalesWings.]({% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_integration_settings.png %})

Copiez la valeur de la colonne **Identifiant** de la clé nouvellement créée et collez-la dans le champ **Clé API Braze** de la section **Intégration Braze** de SalesWings.

Ajoutez votre endpoint API Braze comme décrit dans l'[article sur les endpoints API et SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints), et saisissez-le dans le champ **Endpoint API Braze**. Copiez la valeur de la colonne **Endpoint REST** et saisissez-la dans le champ **Endpoint API Braze** dans la section **Intégration Braze de** SalesWings.

Sélectionnez ensuite **Enregistrer**.

### Étape 4 : Configurer une exportation personnalisée de Currents vers SalesWings (facultatif)

Si vous souhaitez utiliser le [comportement de l'utilisateur]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events) et les événements d'[engagement des messages]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events) pour l'intelligence comportementale, le scoring des prospects et des comptes, produire des informations sur les ventes ou générer des rapports dans votre CRM, allez sur la page [**Intégrations de SalesWings**](https://helium.saleswings.pro/integrations) et développez la section **Intégration Braze**.

Sélectionnez **Générer** sous **Générer un jeton API pour configurer une exportation de courants personnalisée**.

Ensuite, [créez un nouveau courant]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents) et sélectionnez **Exportation de courants personnalisés** comme type de courant.

Dans la section **Credentials** du formulaire Current creation, entrez le jeton API que vous avez généré sur la [page**SalesWings Integrations**](https://helium.saleswings.pro/integrations) pour **Bearer Token**, et `https://helium.saleswings.pro/api/braze/currents/events` pour **Endpoint**.

### Étape 5 : Configuration du scoring des prospects et des comptes de SalesWings pour Braze, intégration CRM, etc.

Consultez l'équipe SalesWings pour une assistance complète à l'onboarding via le [site web](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs).

## Utilisation de cette intégration 

Pour déclencher le rattachement des données comportementales et d'autres données aux leads et aux comptes, SalesWings doit identifier un utilisateur sur votre site web ou votre appli, ou par le biais d'une intégration third-party. Cela peut se produire de la manière suivante :

- **Soumission de formulaires :** Lorsqu'un utilisateur soumet un formulaire web, SalesWings identifie automatiquement le type de formulaire web dont il s’agit (formulaire de connexion, de téléchargement, de contact, etc.) et détermine l'identité de l’utilisateur. 
- **Cliquez sur l'URL avec un ID Braze ou un ID externe :** Un utilisateur clique sur une action marketeur de Braze, typiquement des clics d'e-mail, des clics de bannière ou similaires, menant à une page que vous suivez avec SalesWings.
- **Événements de Braze Currents (facultatif) :** Si l'exportation des Custom Currents vers SalesWings est personnalisée, SalesWings créera un profil identifié pour chaque utilisateur de Braze dont l'e-mail contient des événements envoyés au Current.
- **Suivi des e-mails commerciaux via les modules complémentaires Gmail et Outlook (facultatif) :** Si vous décidez de doter vos conseillers commerciaux de plugins de suivi par e-mail, ils peuvent déclencher le suivi complet des utilisateurs sur le site Web en envoyant des liens de suivi.
- **Segment.com identifier l'événement (facultatif) :** Si vous êtes un utilisateur de Segment.com, vous pouvez également résoudre l'identité d'un utilisateur avec l'intégration de Segment.com.

### Identifier les utilisateurs à partir des clics sur les URL

Vous pouvez identifier automatiquement les utilisateurs lorsqu'ils cliquent sur une URL traçable (par exemple, les envois d'e-mails, les bannières avec URL). Pour rendre une URL traçable, il y a deux façons de modifier les URL de votre site web dans vos e-mails, bannières ou SMS en ajoutant le paramètre et l'ID à la fin de vos liens.

1. L'ajout de `?braze_id=` suivi de {% raw %}`{{${braze_id}}}`{% endraw %} 
  - **Exemple de lien :** {% raw %}`https://www.your-website.com?braze_id={{${braze_id}}}`{% endraw %}<br><br>

2. L'ajout de `?br_user_id=` suivi de {% raw %}`{{${user_id}}}`{% endraw %}
  - **Exemple de lien :** {% raw %}`https://www.client-website.com?br_user_id={{${user_id}}}`{% endraw %}

La variable `braze_id` est définie sur un identifiant de l'utilisateur généré par Braze et est toujours disponible. La variable `br_user_id` est définie sur l'identifiant de l'utilisateur dans votre système et peut être manquante dans certains scénarios (par exemple, pour les utilisateurs anonymes créés par le SDK). Si `braze_id` et `br_user_id` sont utilisés dans un lien, SalesWings ne prendra en compte que le paramètre `braze_id`.

### Utiliser les événements de Braze Currents dans votre CRM

Si vous connectez un Braze Currents à SalesWings, SalesWings créera des profils de prospects identifiés pour chaque utilisateur de Braze disposant d'un e-mail et enregistrera les événements de Braze pris en charge en tant qu'activité de prospects. Dans votre CRM, toutes les données peuvent être automatiquement agrégées au niveau du compte du lead. L'activité et les données enregistrées pourraient ensuite être combinées avec les données comportementales collectées avec le script de suivi de SalesWings ou Segment.com, ou en envoyant d'autres données à l'API de SalesWings, et ensuite utilisées pour identifier les besoins et la préparation à la vente de vos prospects pour vos processus de gestion des prospects et des comptes.

Le tableau suivant présente les types d'événements de Braze pris en charge par SalesWings et leur représentation dans l'historique des activités des prospects et le moteur de règles de SalesWings :

| Catégorie d'événement | Type d’événement | Nom de l'événement dans SalesWings |
| ----------- | ----------- | ----------- |
| Événements du canvas | Entrées | `[Nurturing] Added by marketing team onto the journey $canvas_name` |
| Événements de comportement client | Événements personnalisés | `[Custom Event tracked] $name` |
| Événements de comportement client | Première session | `[User Action] Today marks the user's first session` |
| Événements de comportement client | Attribution d’installation | `[User Action] User installed app from $source` |
| Événements de comportement client | Événements d’achat | `[Purchase] Customer purchased $product_id for $price $currency` |
| Événements liés aux messages | Carte de contenu cliquée | `[Content Card engagement] Clicked on $campaign_name content card` |
| Événements liés aux messages | Rebond d’e-mail | `[Alerting or negative] Email hard-bounced. This person's email appears to be no longer valid` |
| Événements liés aux messages | Clics sur e-mails | `[Email campaign engagement] Clicked in email $campaign_name on $url` |
| Événements liés aux messages | Réception des e-mails | `[Nurturing] Received email $campaign_name` |
| Événements liés aux messages | Ouverture d'e-mails | `[Email campaign engagement] Opened email $campaign_name` |
| Événements liés aux messages | Désabonnement des e-mails | `[Subscription status change] Unsubscribed from $campaign_name` |
| Événements liés aux messages | Clic sur le in-app Message | `[In-app campaign engagement] Clicked on message $campaign_name` |
| Événements liés aux messages | Ouverture de notification push | `[Push notification engagement] Clicked on notification $campaign_name` |
| Événements liés aux messages | SMS/MMS entrants reçus | `[SMS/mobile campaign engagement] We received a message from this person to our internal number $inbound_phone_number: $message_body` |
| Événements liés aux messages | Clic de lien court SMS/MMS | `[SMS/mobile campaign engagement] Clicked on $short_url` |
| Événements liés aux messages | WhatsApp Inbound Received | `[WhatsApp engagement] We received a message from this person to our WhatsApp number $inbound_phone_number: $message_body` |
| Événements liés aux messages | Lecture WhatsApp | `[WhatsApp engagement] Lead read our message from the $campaign_name campaign` |
| Abonnements | Changement de statut global d’abonnement | `[Subscription status change] Global marketing subscription setting set to $subscription_status` |
| Abonnements | Changement de statut du groupe d’abonnement | `[Subscription status change] $subscription_status to/from $campaign_name` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Vous pouvez ensuite configurer les conditions **Événement personnalisé** > **Nom de l'événement** et **Événement personnalisé** > **Propriété de l'événement** pour les étiquettes et les scores SalesWings par rapport aux noms d'événements SalesWings figurant dans le tableau ci-dessus. La liste des propriétés d'événement disponibles pour les conditions est pré-remplie avec certaines des entrées les plus couramment utilisées, et vous pouvez toujours en ajouter de nouvelles dans la section **Propriété d'événement** de la [page de configuration du moteur de règles](https://helium.saleswings.pro/falcon).

![Exemple de condition de nom d'événement.]({% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_custom_event_condition.png %})

Pour la configuration et d'autres résolutions des problèmes, contactez l'[équipe des services de SalesWings](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs) pour une assistance à l'onboarding.

