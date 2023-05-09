---
nav_title: Knak
article_title: Knak
alias: /partners/knak/
description: "Cet article de référence présente le partenariat entre Braze et Knak, une plateforme de création de campagnes qui vous permet de créer des e-mails totalement réactifs en quelques minutes ou en heures au lieu de quelques jours ou semaines, et de les exporter comme modèles Braze prêts à l’emploi."
page_type: partner
search_tag: Knak

---

# Knak

> [Knak][1] est la première plateforme de création de campagnes conçue pour les équipes marketing d’entreprise à utiliser en interne. La plateforme glisser-déposer permet à quiconque de créer des e-mails et des pages de renvoi attrayantes sur la marque en quelques minutes, sans code ni aide extérieure.

L’intégration entre Braze et Knak permet de créer des e-mails totalement réactifs en quelques minutes ou en heures au lieu de quelques jours ou semaines, et de les exporter en tant que modèles Braze prêts à l’emploi. Knak est conçu pour les marketeurs qui souhaitent mettre à niveau leur création d’e-mails pour les campagnes gérées dans Braze, sans avoir besoin d’agences extérieures ou de codage manuel. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Knak | Un compte Knak est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations **Modèles** complètes. <br><br>Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze | [URL de votre endpoint REST][2]. Votre endpoint dépendra de l’URL Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Cas d’utilisation

Knak est conçu pour les marketeurs qui souhaitent mettre à niveau leur création d’e-mails sans avoir besoin d’une aide externe. Une solution idéale pour ceux qui :
- Utilisent actuellement des modèles d’e-mails simples et souhaitent les améliorer
- Comptent sur des agences externes ou des développeurs pour créer des e-mails pour Braze
- Souhaitent reprendre le contrôle sur la création d’actifs et accélérer considérablement la commercialisation

## Intégration

### Étape 1 : Configurer votre intégration

Dans Knak, accédez à **Integrations (Intégrations) > Platforms (Plateformes) > + Add New Integration (+ Ajouter une nouvelle intégration)**.

![Bouton Add integration (Ajouter une intégration)][5]

Ensuite, sélectionnez la plateforme **Braze** et saisissez la clé d’API et l’endpoint REST. Cliquez sur **Create New Integration (Créer une nouvelle intégration)** pour terminer votre intégration. 

![Créer une nouvelle intégration][6]

### Étape 2 : Synchroniser vos modèles Knak

Dans Knak, identifiez un e-mail que vous souhaitez synchroniser avec Braze et sélectionnez **Publish (Publier)** puis **Sync**.

![Intégration de Knak 1][8]

Ensuite, vérifiez le nom de l’e-mail et cliquez sur **Sync**.

![Intégration de Knak 2][9]

## Comment utiliser l’intégration

Vous pouvez trouver vos e-mails Knak téléchargés dans Braze sous **Engagement > Templates & Media (Modèles et médias)**. Ils seront attrayants, pertinents à la marque et totalement réactifs. La seule limite est votre créativité !

[1]: https://knak.com/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[5]: {% image_buster /assets/img/knak/integration-setup-step-2-add-new-integration.png %}
[6]: {% image_buster /assets/img/knak/integration-setup-step-4-add-api-key.png %}
[8]: {% image_buster /assets/img/knak/integration-post-step-1-sync.png %}
[9]: {% image_buster /assets/img/knak/integration-post-step-2-asset-name.png %}