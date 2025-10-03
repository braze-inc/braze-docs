# Créer des agents de construction

> Découvrez comment créer un agent pour BrazeAI Decisioning Studio™, afin d'automatiser les expérimentations personnalisées et d'optimiser les résultats tels que les conversions, la fidélisation ou les chiffres d'affaires, sans tests A/B manuels.

{% multi_lang_include decisioning_studio/alert_multi_platform_support.md %}

## À propos des agents

Un agent décisionnel d'intelligence artificielle est une configuration personnalisée du moteur décisionnel BrazeAI™, conçue sur mesure pour répondre à un objectif métier spécifique.

Par exemple, vous pourriez créer un agent d'achat répété pour augmenter les conversions de suivi après une vente initiale. Vous définissez l'audience et le message dans Braze, tandis que vos agents décisionnels mènent des expériences quotidiennes et testent automatiquement différentes combinaisons d'offres de produits, de timing et de fréquence des messages pour chaque client. Au fil du temps, BrazeAI™ apprend ce qui fonctionne le mieux et orchestre des envois personnalisés via Braze pour maximiser les taux de réachat.

Pour créer un bon agent, vous allez :

- Choisissez un indicateur de réussite pour BrazeAI™ à optimiser, comme le chiffre d'affaires, les conversions ou l'ARPU.
- Définissez les dimensions à tester, telles que l'offre, la ligne d'objet, la création, le canal ou l'heure d'envoi.
- Sélectionnez les options pour chaque dimension, par exemple e-mail ou SMS, ou fréquence quotidienne ou hebdomadaire.

\![Exemple de diagramme d'un agent de studio décisionnel pour les e-mails de recommandation.]({% image_buster /assets/img/offerfit/example_use_cases_referral_email.png %})

## Exemples d'agents

Voici quelques exemples d'agents que vous pouvez créer avec BrazeAI Decisioning Studio™. Vos agents décisionnels de l'intelligence artificielle apprendront de chaque interaction avec les clients et appliqueront ces informations exploitables aux actions du lendemain.

{% multi_lang_include decisioning_studio/sample_agents.md %}

## Créer un agent

### Conditions préalables

Avant de pouvoir créer un agent, vous devrez [intégrer BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/integration).

### Étape 1 : Contactez les services experts de l'intelligence artificielle

L'équipe des services experts en intelligence artificielle travaillera en étroite collaboration avec vous pour définir le champ d'application, concevoir et créer votre agent décisionnel. Si vous ne l'avez pas encore fait, [contactez-nous](https://www.braze.com/get-started/) pour commencer.

Vous suivrez ensemble les étapes suivantes pour créer un agent personnalisé qui vous convienne.

### Étape 2 : Concevez votre agent

Aux côtés de l'équipe des services experts en intelligence artificielle, vous définirez :

- une audience ciblée, 
- les indicateurs commerciaux à optimiser, 
- les actions pour l'agent décisionnel BrazeAI™, et 
- toutes les données first-party des clients que l'agent doit exploiter pour améliorer les résultats de votre entreprise. 

Avec la conception en main, l'équipe travaillera avec vous pour identifier et compléter toutes les exigences d'intégration supplémentaires.

### Étape 3 : Mettre en place votre plateforme de réception/distribution

Ensuite, l'équipe du service expert de l'intelligence artificielle vous aidera à configurer votre plateforme d'automatisation du marketing. Bien que le studio de prise de décision fonctionne mieux avec Braze, une variété d'autres plateformes sont prises en charge - contactez votre équipe de service expert en intelligence artificielle pour obtenir des ressources supplémentaires.

{% tabs local %}
{% tab Braze %}
Pour configurer Braze :

1. Créez une [campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) ou un [canvas.]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=api-triggered%20delivery#step-2b-determine-your-canvas-entry-schedule) BrazeAI Decisioning Studio™ utilisera cette méthode de réception/distribution pour envoyer des événements d'activation personnalisés 1:1 aux utilisateurs de votre audience définie.
2. Veillez à ne pas inclure de [groupe de contrôle]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group) Braze, afin que BrazeAI™ puisse être le groupe de contrôle dédié à la place.
3. En fonction de vos dimensions, vous pouvez configurer des étiquettes Liquid dans votre contenu créatif pour alimenter dynamiquement votre envoi de messages avec des recommandations BrazeAI™. BrazeAI™ transmettra le contenu personnalisé aux étiquettes Liquid dans vos modèles à l'aide de l'API Braze.
{% endtab %}
{% endtabs %}

### Étape 4 : Lancement et suivi

Après le lancement de votre agent, votre équipe d'experts en services d'intelligence artificielle continuera à le surveiller et à l'adapter à la conception convenue. Ils vous aideront également à procéder à des ajustements, à des extensions ou à des modifications de l'agent, si nécessaire.
