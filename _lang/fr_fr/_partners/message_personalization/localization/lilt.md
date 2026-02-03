---
nav_title: LILT
article_title: LILT
description: "Cet article de référence présente le partenariat entre Braze et LILT."
alias: /partners/lilt/
page_type: partner
search_tag: Partner
---

# LILT

> [LILT](https://lilt.com/) est la solution complète d'intelligence artificielle pour la traduction et la création de contenu en entreprise. LILT permet aux organisations mondiales de mettre à l'échelle et d'optimiser leurs opérations de contenu, de produit, de communication et de support, avec des agents d'intelligence artificielle et des flux de travail entièrement automatisés.

_Cette intégration est maintenue par la LILT._

## À propos de cette intégration

Le connecteur LILT Braze permet de traduire des modèles d'e-mails en HTML avec une vitesse d'intelligence artificielle et une qualité digne d'une entreprise. Demandez une traduction instantanée conforme à la marque ou une traduction vérifiée dont la qualité est garantie et recevez le contenu multilingue des e-mails de la LILT directement dans Braze. 

## Cas d’utilisation

L'intégration de LILT Braze automatise et accélère le processus de traduction, ce qui permet aux équipes de marketing mondial de lancer leurs campagnes multilingues rapidement et en respectant la cohérence de la marque.

### Rationalisation du lancement de la campagne mondiale

Lancez des campagnes marketing dans plusieurs régions simultanément, sans retards dus à des traductions manuelles.

- **Scénario :** Votre entreprise lance un nouveau produit dans 10 pays.
- **Solution :** Votre équipe marketing finalise le modèle d'e-mail en anglais dans Braze, l'étiquette avec `LILT: Ready`, et le connecteur LILT extrait automatiquement le contenu. Des linguistes spécialisés par domaine révisent les invites de traduction de l'intelligence artificielle dans la plateforme LILT à des fins d'assurance qualité, et le connecteur repousse les versions traduites dans Braze.
- **Bénéfice :** Réduit le délai de mise sur le marché de vos campagnes mondiales de quelques jours à quelques heures, afin que tous les clients puissent recevoir l'annonce d'un nouveau produit au moment optimal.

### Localisation instantanée en fonction de la marque

Utilisez l'intelligence artificielle de LILT pour des traductions immédiates et conformes à la marque pour les communications sensibles au temps.

- **Scénario :** Vous devez déployer immédiatement des e-mails pour une vente flash, une offre à durée limitée ou une interruption de service urgente dans cinq marchés géographiques.
- **Solution :** Vous avez tagué le modèle d'e-mail avec `LILT: Instant`. LILT utilise son intelligence artificielle et les ressources linguistiques propres à votre entreprise (telles que la terminologie et les guides de style) pour générer une traduction de haute qualité et conforme à la marque en quelques minutes.
- **Bénéfice :** Permet des communications hyper-réactives et en temps réel sans sacrifier la voix ou la qualité de la marque, ce qui est essentiel pour le marketing sensible au temps.

## Conditions préalables

| Prérequis       | Description |                        
|-----------------------|-----------------|
| Un compte LILT   | Un compte LILT est nécessaire pour bénéficier de ce partenariat.  |
| Une clé de l'API REST de Braze  | Une clé API REST de Braze avec les autorisations suivantes :<br>- `templates.email.create`<br>- `templates.email.update`<br>- `templates.email.info`<br>- `templates.email.list`<br>- `templates.translations.source.get`<br>- `templates.translations.update`<br>- `templates.translations.get`<br>- `templates.translations.all.get`. <br><br> Créez cette clé dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API.** |
| Un endpoint REST Braze | [L'URL de votre endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Votre endpoint dépend de l'URL Braze de votre instance.  |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}


## Intégration

### Étape 1 : Configurer le connecteur de la LILT Braze

1. Connectez-vous à LILT, puis allez dans **Connexion** > **Nouveau connecteur** > **Braze**.
	
![Brazez le connecteur en LILT.]({% image_buster /assets/img/lilt/image_1_select_connector.png %})

{: start="2"}
2\. Sélectionnez le flux de travail de localisation souhaité pour votre contenu Braze.

![Braze workflow in LILT.]({% image_buster /assets/img/lilt/image_2_select_workflow.png %})	

{: start="3"}
3\. Entrez et vérifiez les détails de configuration nécessaires :
- Votre clé API Braze
- Endpoint REST Braze

![Complétez les informations d'identification de l'API.]({% image_buster /assets/img/lilt/image_3_api_creds.png %})	

{: start="4"}
4\. Sélectionnez **Vérifier** pour tester la configuration. Une fois la connexion confirmée, enregistrez la configuration.

### Étape 2 : Préparez votre espace de travail Braze

1. Activez les fonctionnalités multilingues dans les paramètres de votre espace de travail Braze.

![Configurer les lieux dans Braze.]({% image_buster /assets/img/lilt/image_4_lilt_locales.png %})	

{: start="2"}
2\. Créez les étiquettes suivantes dans Braze pour votre flux de travail LILT : 
- `LILT: Ready`
- `LILT: In progress`
- `LILT: Sent to LILT`
- `LILT: Delivered`
- `LILT: Needs Attention`
- `LILT: Instant`

![Configurez les étiquettes LILT dans Braze.]({% image_buster /assets/img/lilt/image_5_lilt_tags.png %})	

{: start="3"}
### Étape 3 : Envoyer le contenu à la LILT pour traduction 

1. Après avoir configuré le connecteur LILT Braze, utilisez les tags de traduction Liquid dans vos modèles d'e-mail Braze pour identifier le contenu à traduire. 
- Exemple :  {% raw %}`{% translation id_0 %}`Bonjour, `{{first_name}}!{% endtranslation %}`{% endraw %}
2. Lancez la traduction en mettant à jour l'étiquette du modèle pour indiquer le flux de travail souhaité : 
- Choisissez `LILT: Ready` pour une traduction vérifiée
- Choisissez `LILT: Instant` pour une traduction instantanée adaptée à votre marque
3. Le connecteur de la LILT Braze s'exécute à la fréquence que vous avez prédéfinie pour transférer le contenu étiqueté dans la LILT. Suivez l'avancement de la traduction, car les étiquettes de contenu se mettent automatiquement à jour dans Braze pour refléter l'état d'avancement de votre projet. 
	
![Modèle d'e-mail de Braze avec étiquettes de traduction.]({% image_buster /assets/img/lilt/image_6_braze_template.png %})	