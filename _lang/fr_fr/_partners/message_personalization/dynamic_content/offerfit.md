---
nav_title: "OfferFit"
article_title: OfferFit
alias: /partners/offerfit/
description: "OfferFit remplace le test A/B manuel par des tests d'intelligence artificielle. Les spécialistes du marketing de cycle de vie utilisent les tests d'intelligence artificielle d'OfferFit pour prendre la meilleure décision 1:1 pour chaque client, tester toutes les variables simultanément et détecter et s'adapter aux changements du marché."
page_type: partner
search_tag: OfferFit

---


# OfferFit

> [OfferFit](https://www.offerfit.ai/) remplace le test A/B manuel par des tests d'intelligence artificielle. Les spécialistes du marketing de cycle de vie utilisent les tests d'intelligence artificielle d'OfferFit pour prendre la meilleure décision 1:1 pour chaque client, tester toutes les variables simultanément et détecter et s'adapter aux changements du marché.

_Cette intégration est maintenue par OfferFit._

## À propos de l'intégration

L'intégration d'OfferFit et Braze vous permet de découvrir automatiquement le bon message, canal et timing pour chaque client en fonction de vos données client. Vous pouvez optimiser vos campagnes pour les clients existants identifiés avec des objectifs commerciaux tels que la vente croisée, la vente incitative, le rachat, la rétention, le renouvellement, le parrainage et la reconquête.

## Conditions préalables

| Condition | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Licence OfferFit | Une licence OfferFit active est requise pour profiter de ce partenariat.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Clé API REST de Braze | Une clé API REST Braze avec les permissions suivantes : {::nomarkdown}<ul><li><code>users.export.ids</code></li><li><code>users.export.segment</code></li><li><code>users.track</code></li><li><code>messages.send</code></li><li><code>campaigns.trigger.send</code></li> <li><code>campaigns.list</code></li><li><code>campaigns.data_series</code></li><li><code>campaigns.details</code></li><li><code>canvas.trigger.send</code></li><li><code>canvas.list</code></li><li><code>canvas.data_series</code></li><li><code>canvas.details</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>templates.email.create</code></li><li><code>templates.email.update</code></li><li><code>templates.email.info</code></li><li><code>templates.email.list</code></li></ul>{:/} Cela peut être créé dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| endpoint de l'API REST de Braze | [Votre URL d'endpoint de l'API REST][1]. Votre endpoint dépend de l'URL Braze de votre instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### endpoints de l'API REST de Braze

Votre licence OfferFit et votre cas d'utilisation détermineront les points de terminaison de l'API REST Braze que vous utilisez. Vous trouverez ci-dessous divers points de terminaison API que vous pourriez utiliser.

| endpoint de l'API REST de Braze | Utilisation d'OfferFit |
|--------------|----------------|
| [POST /users/export/ids]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)                          | Récupérer la liste des clients à cibler à l’aide d’une campagne ou d’un canvas. Comme OfferFit n'accepte aucune donnée PII, l'attribut `fields_to_export` est utilisé pour ne récupérer que les attributs de données convenus avec l'utilisateur de la plateforme. |
| [POST /users/export/segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)                         | Récupéree tous les utilisateurs qui font partie d'un segment spécifique. Comme OfferFit n'accepte aucune donnée PII, l'attribut `fields_to_export` est utilisé pour ne récupérer que les champs non-PII convenus avec l'utilisateur de la plateforme. |
| [POST /users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)                                            | OfferFit peut utiliser cet endpoint pour mettre à jour les profils utilisateur avec des attributs de données personnalisés qui peuvent être utilisés pour personnaliser l'envoi de messages.                                                                                                                                            |
| [POST /messages/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)                         | Déclencher une campagne API dans Braze. |
| [POST /campaigns/trigger/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)     | Déclencher un envoi pour une campagne configurée pour une distribution déclenchée par l'API. |
| [GET /campaigns/list]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/)                                     | Récupérer la liste de toutes les campagnes configurées dans Braze et leurs métadonnées associées. |
| [GET /campaigns/data_series]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)                     | Récupérer les données d'analyse d'une campagne spécifique de Braze. |
| [GET /campaigns/details]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/)                           | Récupérer les détails d'une campagne Braze spécifique. |
| [POST /canvas/trigger/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)         | Déclencher un envoi pour un canvas configuré pour une distribution déclenchée par l'API. |
| [GET /canvas/list]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/)                                            | Récupérer la liste de tous les canvas configurés dans Braze et leurs métadonnées associées. |
| [GET /canvas/data_series]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/)                             | Récupérer les données d'analyse d'un Canvas spécifique. |
| [GET /canvas/details]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)                                   | Récupérer les détails d'un canvas spécifique. |
| [GET /segments/list]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)                                        | Récupérer la liste de tous les segments configurés dans Braze et leurs métadonnées associées. |
| [GET /segments/data_series]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/)                        | Récupérer la taille du segment Braze. |
| [OBTENIR /segments/details]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/)                              | Récupérer les détails d'un segment Braze spécifique. |
| [POST /templates/email/create]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)      | Créer un nouveau modèle d'e-mail HTML Braze. |
| [POST /templates/email/update]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/)      | Mettre à jour un modèle d'e-mail HTML Braze existant. |
| [GET /templates/email/info]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | Récupérer les détails d'un modèle d'e-mail HTML Braze spécifique. |
| [GET /templates/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/)           | Récupérer la liste de tous les modèles d'e-mail HTML Braze configurés dans Braze et leurs paramètres `subject line` et `HTML content`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

Après avoir [intégré OfferFit](#integration), vous pouvez automatiser le processus d'expérimentation en faisant ce qui suit :

1. Sélectionnez une **mesure de réussite** à maximiser, telle que le chiffre d'affaires, les conversions, l'ARPU ou tout autre
indicateur clé de performance que vous pouvez mesurer à partir de vos données client. Il s’agit de la métrique que l’intelligence artificielle d'OfferFit essaiera de maximiser.
2. Sélectionnez les **dimensions** à tester (par exemple, offre, ligne d'objet, création, canal, heure, jour, fréquence, etc.).
3. Sélectionnez les **options** disponibles pour chaque dimension. Par exemple, vous pouvez sélectionner l'e-mail, le SMS et la notification push pour la dimension du canal, puis sélectionner quotidien, deux fois par semaine et hebdomadaire pour la dimension de la fréquence.

![of_use_case_example][2]


Après l'automatisation du processus d'expérimentation, OfferFit commencera à faire des recommandations quotidiennes pour chaque client dans le but de maximiser la métrique de succès choisie. 

L'intelligence artificielle d'OfferFit apprendra de chaque interaction client et appliquera ces informations aux recommandations du jour suivant.


| Cas d'utilisation | Objectif | Approche antérieure | Approche OfferFit |
|----------|------|----------------|-------------------|
| **Vente croisée ou vente incitative** | Maximiser le chiffre d'affaires moyen par utilisateur (ARPU) provenant des abonnements internet. | Mener des campagnes annuelles offrant à chaque client le plan de niveau supérieur suivant. | Découvrez empiriquement le meilleur message, le moment d'envoi, la remise et le plan à offrir à chaque client, en apprenant quels clients sont susceptibles d'accepter des offres de saut et quels clients nécessitent des remises ou d'autres incitations pour passer à la version supérieure. |
| **Renouvellement et rétention** | Assurez le renouvellement des contrats, en maximisant à la fois la durée des contrats et la valeur actuelle nette (VAN). | Effectuez des tests A/B manuels et offrez des réductions importantes pour sécuriser les renouvellements. | Utilisez l'expérimentation automatisée pour trouver la meilleure offre de renouvellement pour chaque client, et identifiez les clients qui sont moins sensibles au prix et qui ont besoin de réductions moins importantes pour renouveler. |
| **Achat répété** | Maximiser les taux d'achat et de rachat. | Tous les clients reçoivent le même parcours après avoir créé un compte sur le site web (comme la même séquence d'e-mails avec la même cadence). | Automatisez l'expérimentation pour trouver le meilleur élément de menu à offrir à chaque client, ainsi que la ligne d'objet, l'heure d'envoi et la fréquence de communication les plus efficaces. |
| **Réconquérir** | Augmentez la réactivation en encourageant les anciens abonnés à se réabonner. | Test A/B sophistiqué et segmentation. | Tirez parti de l'expérimentation automatisée pour tester des milliers de variables à la fois afin de découvrir le meilleur contenu créatif, message, canal ou la meilleure cadence pour chaque individu. |
| **Recommandation** | Maximiser les nouveaux comptes ouverts grâce aux recommandations de cartes de crédit professionnelles de la part des clients existants. | Séquence d'e-mails fixe pour tous les clients, avec des tests A/B approfondis pour déterminer la meilleure heure d’envoi, fréquence, etc. pour la base de clients. | Automatisez l'expérimentation pour déterminer l'e-mail, la création, l'heure d'envoi et la carte de crédit idéaux à offrir à des clients spécifiques. |
| **Prospection et conversion** | Générez un chiffre d'affaires supplémentaire et payez le bon montant pour chaque client. | À mesure que les politiques de confidentialité changent chez Facebook et d'autres plateformes, les approches antérieures aux publicités payantes personnalisées deviennent moins efficaces. | Exploitez des données first-party robustes pour expérimenter automatiquement des segments de clients, la méthodologie d'enchères, les niveaux d'enchères et des contenus créatifs. |
| **Loyauté & Engagement** | Maximiser les achats des nouveaux inscrits au programme de fidélité client. | Les clients ont reçu une séquence fixe d'e-mails en réponse à leurs actions. Par exemple, tous les nouveaux inscrits au programme de fidélité reçoivent le même parcours. | Tirez parti de l’expérimentation automatisée avec divers contenus créatifs, offres d'e-mail, heures d'envoi et fréquences pour maximiser les achats et les rachats de chaque client. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }


## Intégration

### Étape 1 : Définir l'audience cible dans Braze

Définissez votre audience cible en créant au moins un segment dans Braze. Ce segment sera utilisé pour envoyer votre campagne ou canvas aux bons utilisateurs.

### Étape 2 : Configurez une campagne Braze déclenchée par une API ou un canvas et créez des éléments de campagne (par exemple, des modèles HTML, des images) {#step-2}

1. Créez une campagne ou un canvas dans Braze. OfferFit utilisera cette campagne ou ce canvas pour envoyer des événements d'activation personnalisés 1:1 aux bons utilisateurs de votre audience définie. 
2. N'incluez pas un [groupe de contrôle]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group) Braze dans votre campagne ou canvas. Cela permet au groupe de contrôle OfferFit d'être le seul actif.
3. En fonction de vos dimensions, vous pouvez configurer des tags Liquid dans votre contenu créatif pour remplir dynamiquement votre campagne ou canvas avec les recommandations d'OfferFit. OfferFit transmettra le contenu spécifique au client aux tags Liquid dans vos modèles via l'API Braze.

### Étape 3 : Mettez à jour votre configuration de cas d'utilisation OfferFit pour orchestrer les événements d'activation Braze

Vous pouvez tirer parti de l'intégration native d'activation d'OfferFit avec Braze pour orchestrer et planifier des recommandations personnalisées 1:1 pour votre audience cible.

## Personnalisation

En plus d'orchestrer des événements d'activation dans Braze, OfferFit fournit des capacités d'intégration de données qui vous permettent de récupérer des profils de clients (non-PII) et des données d'engagement depuis Braze via les points de terminaison API disponibles.

## Grâce à cette intégration

Après la configuration d'OfferFit, la plateforme d'expérimentation automatisée enverra automatiquement des événements d'activation personnalisés 1:1 à Braze pour chaque utilisateur de votre audience cible. Ces événements d'activation seront déclenchés par les campagnes Braze ou les Canvases que vous avez configurés dans [l'étape 2](#step-2).

En plus des données d'analyse disponibles dans Braze, OfferFit fournit une couche de reporting complète qui permet aux marketeurs d'explorer les informations client découvertes par OfferFit grâce à ses capacités d'intelligence artificielle auto-apprenante.


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/offerfit/of_use_case_example.png %}

