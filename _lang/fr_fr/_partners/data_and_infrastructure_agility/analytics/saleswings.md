---
nav_title: SalesWings
article_title: SalesWings
description: "Cet article de référence présente le partenariat entre Braze et SalesWings, une plateforme analytique, qui vous aide à suivre le scoring et le classement, les informations et alertes commerciales, l'alignement marketing et les rapports d'attribution B2B."
alias: /partners/saleswings/
page_type: partner
search_tag: Partner

---

# SalesWings

> [SalesWings][1] est un module complémentaire SaaS de profilage de prospects B2B créé pour les équipes marketing et commerciales, qui aide à gérer la qualification des prospects et des comptes grâce au scoring et au classement des prospects, aux informations et alertes commerciales, à l'alignement marketing et aux rapports d'attribution B2B, ainsi qu'à une intégration étroite avec le CRM de Salesforce.

_Cette intégration est maintenue par SalesWings._

## À propos de l'intégration

SalesWings permet aux équipes marketing et aux gestionnaires des opérations marketing de qualifier les prospects et les comptes pour leurs équipes commerciales, ce qui est essentiel pour l'alignement et l'efficacité des ventes et du marketing. En outre, SalesWings, conjointement avec Braze, peut faire remonter à la surface le parcours client d'un lead et les données d'engagement des campagnes marketing de Braze pour les commerciaux, ce qui vous permet d'augmenter les taux de conversion des leads grâce à des conversations plus éclairées.

## Conditions préalables
 
| Condition | Description |
| ----------- | ----------- |
| Compte SalesWings | Un compte [SalesWings][1] est nécessaire pour profiter de ce partenariat. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations `users.export.ids`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.][2] Votre endpoint dépendra de l'URL de Braze pour votre instance. |
| Segment.com compte (facultatif) | Si vous êtes un utilisateur de Segment.com, vous pouvez envoyer toutes les données d'engagement et de profil des prospects et identifier les événements via Segment.com pour le profilage des prospects. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d’utilisation

{% tabs %}
{% tab Notation des prospects %}

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
Grâce à l'intégration de SalesWings avec Salesforce, vous pouvez créer des rapports automatisés avec des prospects, des contacts, des comptes et des opportunités en fonction des données d'engagement sur le web et de l'engagement dans les campagnes de Braze. Par exemple, vous pouvez établir une liste de prospects prometteurs pour une équipe commerciale, notamment en indiquant ceux qui ont cliqué sur une campagne d'e-mail spécifique ou effectué une action spécifique dans votre appli ou sur votre site Web.

![Exemple de tableau de bord lié à l'engagement des e-mails et du marketing de Braze au sein de Salesforce, examinant l'impact des campagnes Braze sur les résultats des ventes et les performances]({% image_buster /assets/img/saleswings/saleswings_email_campaign_attribution_dashboard.png %})

_Exemple de tableau de bord lié à l'engagement e-mail et marketing de Braze dans Salesforce, étudiant l'impact des campagnes de Braze sur les résultats des ventes et les résultats._
{% endtab %}
{% endtabs %}

## Intégration

### Étape 1 : Compte et configuration de SalesWings

[Planifiez une démonstration][4] avec l'équipe sympathique de SalesWings pour en savoir plus sur SalesWings.

### Étape 2 : Installer un outil de suivi des comportements dans votre site Web ou votre application

Actuellement, il existe deux façons de collecter des données comportementales dans SalesWings pour l’évaluation des prospects et l’obtention d’informations commerciales :
* [Déployez les scripts JavaScript de SalesWings][5] sur les sites Web et les applications où vous souhaitez suivre et identifier des prospects.
* Envoyez des données comportementales sur l'activité des prospects (et des données sur le profil des prospects) via l'intégration de SalesWings à Segment.com

### Étape 3 : Connecter SalesWings à Braze

Allez sur la [page**Paramètres de SalesWings**][6] et développez la section **Intégration de Braze**.

![La section Intégration Braze de la page Paramètres de SalesWings.][7]

Copiez la valeur de la colonne **Identifiant** de la clé nouvellement créée et collez-la dans le champ **Clé API Braze** de la section **Intégration Braze** de SalesWings.

Ajoutez votre endpoint de l’API Braze comme décrit dans [l'article sur les endpoints d’API et de SDK][8], et saisissez-le dans le champ **Endpoint de l’API Braze.**  Copiez la valeur de la colonne **Endpoint REST** et saisissez-la dans le champ **Endpoint API Braze** dans la section **Intégration Braze de** SalesWings.

Cliquez ensuite sur **Enregistrer les modifications** dans les paramètres de SalesWings.

### Étape 4 : Configuration de la fonction d’évaluation des prospects de SalesWings pour Braze, intégration d’un CRM, etc.

Consultez l'équipe SalesWings pour une assistance complète à l'onboarding via le [site web][1].

## Grâce à cette intégration 

Pour déclencher l’évaluation des prospects et la création d'informations commerciales, SalesWings doit identifier un utilisateur sur votre site web ou votre appli. Cela peut se produire de la manière suivante :

- **Soumission de formulaires :** Lorsqu'un utilisateur soumet un formulaire web, SalesWings identifie automatiquement le type de formulaire web dont il s’agit (formulaire de connexion, de téléchargement, de contact, etc.) et détermine l'identité de l’utilisateur. 
- **Cliquez sur l'URL avec un ID Braze ou un ID externe :** Un utilisateur clique sur une action marketeur de Braze, typiquement des clics d'e-mail, des clics de bannière ou similaires, menant à une page que vous suivez avec SalesWings.
- **Suivi des e-mails commerciaux via les modules complémentaires Gmail et Outlook (facultatif) :** Si vous décidez de doter vos conseillers commerciaux de plugins de suivi par e-mail, ils peuvent déclencher le suivi complet des utilisateurs sur le site Web en envoyant des liens de suivi.
- **Segment.com identifier l'événement (facultatif) :** Si vous êtes un utilisateur de Segment.com, vous pouvez également résoudre l'identité d'un utilisateur avec l'intégration de Segment.com.

### Identifier les utilisateurs à partir des clics sur les URL

Vous pouvez identifier automatiquement les utilisateurs lorsqu'ils cliquent sur une URL traçable (par exemple, les envois d'e-mails, les bannières avec URL). Pour rendre une URL traçable, il y a deux façons de modifier les URL de votre site web dans vos e-mails, bannières ou SMS en ajoutant le paramètre et l'ID à la fin de vos liens.

1. L'ajout de `?braze_id=` suivi de {% raw %}`{{${braze_id}}}`{% endraw %} 
  - **Exemple de lien :** {% raw %}`https://www.your-website.com?braze_id={{${braze_id}}}`{% endraw %}<br><br>

2. L'ajout de `?br_user_id=` suivi de {% raw %}`{{${user_id}}}`{% endraw %}
  - **Exemple de lien :** {% raw %}`https://www.client-website.com?br_user_id={{${user_id}}}`{% endraw %}

La variable `braze_id` est définie sur un identifiant de l'utilisateur généré par Braze et est toujours disponible. La variable `br_user_id` est définie sur l'identifiant de l'utilisateur dans votre système et peut être manquante dans certains scénarios (par exemple, pour les utilisateurs anonymes créés par le SDK). Si `braze_id` et `br_user_id` sont utilisés dans un lien, SalesWings ne prendra en compte que le paramètre `braze_id`.

Pour la configuration et d'autres résolutions des problèmes, contactez l'[équipe des services de SalesWings][1] pour une assistance à l'onboarding.


[1]: https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs
[4]: https://www.saleswingsapp.com/schedule-a-demo?utm_source=braze&utm_campaign=technicaldocs
[5]: https://support.saleswingsapp.com/en/collections/3285135-1-implementing-saleswings-tracking-script
[6]: https://helium.saleswings.pro/settings
[7]: {% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_integration_settings.png %}
[8]: {{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints
