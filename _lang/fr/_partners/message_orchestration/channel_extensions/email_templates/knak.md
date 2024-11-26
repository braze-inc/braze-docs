---
nav_title: Knak
article_title: Knak
alias: /partners/knak/
description: "Cet article de référence décrit le partenariat entre Braze et Knak, une plateforme de création de campagnes qui vous permet de créer des e-mails entièrement réactifs en quelques minutes ou heures au lieu de jours ou de semaines, et de les exporter en tant que modèles Braze prêts à l'emploi."
page_type: partner
search_tag: Knak

---

# Knak

> [Knak][1] est la première plateforme de création de campagne conçue pour les équipes marketing d'entreprise à utiliser en interne. Leur plateforme de glisser-déposer permet à n'importe qui de créer de magnifiques e-mails et pages de destination conformes à leur marque en quelques minutes, sans avoir besoin de coder ni d'aide extérieure.

L'intégration de Braze et Knak vous permet de créer des e-mails entièrement réactifs en quelques minutes ou heures au lieu de jours ou de semaines et de les exporter en tant que modèles Braze prêts à l'emploi. Knak est conçu pour les marketeurs qui veulent améliorer la création de leurs e-mails pour les campagnes gérées dans Braze, sans avoir besoin d'agences externes ou de codage manuel. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Knak | Un compte Knak est requis pour profiter de ce partenariat. |
| Clé d'API REST Braze | Une clé API Braze REST avec des autorisations complètes sur les **modèles**. <br><br>Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.][2] Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

Knak est conçu pour les marketeurs qui veulent améliorer leur création d'e-mails, sans avoir besoin de coder ou d'aide extérieure. C'est l’outil idéal pour ceux qui :
- utilisent actuellement des modèles simples pour les e-mails et souhaitent améliorer leurs performances
- comptent sur des agences externes ou des développeurs pour créer des e-mails pour Braze
- veulent reprendre le contrôle créatif de la création de ressource et arriver sur le marché beaucoup plus rapidement

## Intégration

### Étape 1 : Configurez votre intégration

Dans Knak, accédez à **Intégrations > Plateformes > + Ajouter une nouvelle intégration**.

![Bouton Ajouter l'intégration][5]

Ensuite, sélectionnez la plateforme **Braze** et fournissez la clé API Braze et l'endpoint REST. Cliquez sur **Créer une nouvelle intégration** pour compléter votre intégration. 

![Créer une nouvelle intégration][6]

### Étape 2 : Synchronisez vos modèles Knak

Dans Knak, localisez un e-mail que vous souhaitez synchroniser avec Braze et sélectionnez **Publier** puis **Synchroniser**.

![intégration Knak 1][8]

Ensuite, vérifiez le nom de l'e-mail et cliquez sur **Synchroniser**.

![intégration Knak 2][9]

## Utilisation de l'intégration

Vous pouvez trouver vos e-mails Knak téléchargés dans Braze sous **Engagement > modèles et médias**. Ils seront beaux, conformes à la marque et entièrement réactifs. La seule limite est votre propre créativité !

[1]: https://knak.com/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[5]: {% image_buster /assets/img/knak/integration-setup-step-2-add-new-integration.png %}
[6]: {% image_buster /assets/img/knak/integration-setup-step-4-add-api-key.png %}
[8]: {% image_buster /assets/img/knak/integration-post-step-1-sync.png %}
[9]: {% image_buster /assets/img/knak/integration-post-step-2-asset-name.png %}