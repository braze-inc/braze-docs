---
nav_title: Heap
article_title: Heap
description: "Cet article de référence détaille l'intégration entre Braze et Heap, une plateforme d'informations numériques, qui vous permet d'importer des données Heap vers Braze, de créer des cohortes d'utilisateurs, ainsi que d'exporter des données Braze vers des statistiques des segments."
alias: /partners/heap/
page_type: partner
search_tag: Partner

---

# Heap

> [Heap](https://heap.io/), une plateforme d'informations numériques vous permet d’identifier les opportunités dans votre expérience numérique ayant le plus d'impact sur votre entreprise, en éliminant les frictions, en satisfaisant vos clients et en accélérant les revenus.

L'intégration de Braze et Heap vous permet d'[importer des données Heap vers Braze](#data-import-integration), de créer des cohortes d'utilisateurs, ainsi que d'[exporter des données Braze vers Heap]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/heap/) pour créer des segmentations.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Heap | Un compte [Heap](https://heap.io/about) est nécessaire pour bénéficier de ce partenariat. |
| Clé d'importation des données Braze | Elle peut être capturée dans le tableau de bord de Braze à partir de **Intégrations partenaires** > **Partenaires technologiques**, puis sélectionnez **Heap**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.][1] Votre endpoint dépendra de l'URL de Braze pour votre instance. |
| Braze Currents | Pour pouvoir exporter des données de Braze vers Heap, vous devez activer [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) sur votre compte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation
- Réengagez les utilisateurs qui ont abandonné un entonnoir : Déclenchez des messages de réengagement lorsque les utilisateurs abandonnent l'entonnoir d'achat ou d'abonnement.
- Personnalisez l'expérience de l’essai : Identifiez les points de friction dans votre expérience d'essai et envoyez des rappels au bon moment pour réengager les utilisateurs pendant un essai et les aider à obtenir de la valeur.
- Augmentez l'engagement sur les annonces et les offres : Ciblez les promotions, les mises à jour et les annonces de nouveaux services auprès des audiences concernées.

## Intégration de l'importation de données

Utilisez l'intégration Heap to Braze pour synchroniser automatiquement les cohortes définies dans Heap vers Braze.

### Étape 1 : Obtenez la clé d'importation des données Braze

Dans Braze, naviguez vers **Intégrations partenaires** > **Partenaires technologiques**, puis sélectionnez **Heap.** 

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), vous trouverez les **partenaires technologiques** sous la rubrique **Intégrations.**
{% endalert %}

Sur cette page, vous trouverez votre clé d'importation des données et un endpoint REST. Prenez note de ces deux valeurs et fournissez-les à votre gestionnaire de compte Heap pour terminer la configuration de l'intégration.

![][3]{: style="max-width:90%;"}

### Étape 2 : Segmentation des importations d'utilisateurs à Braze

Dans Braze, naviguez vers **Segments**, nommez votre segment de cohorte Heap et sélectionnez **Cohortes Heap** comme filtre. À partir de là, vous pouvez choisir la cohorte Heap que vous souhaitez inclure. Une fois votre segment de cohorte Heap créé, vous pouvez le sélectionner comme filtre d'audience lors de la création d'une campagne ou d'un Canvas.

![Dans le générateur de segments de Braze, le filtre des attributs de l'utilisateur "Cohorte Heap" est réglé sur "inclut" et "Cohorte d'essais Heap".][2]{: style="max-width:90%;"}

### Utilisation de cette intégration

Pour utiliser votre segment Heap, créez une campagne ou un canvas Braze et sélectionnez le segment comme votre audience cible.

![Dans le générateur de campagnes de Braze, à l'étape du ciblage, le filtre "Cibler les utilisateurs par segment" est défini sur "Cohorte Heap".][4]{: style="max-width:90%;"}

## Détails de l'intégration

La structure des données exportées est la même que celle des connecteurs HTTP personnalisés, qui peut être consultée dans le [référentiel d'exemples de connecteurs HTTP personnalisés](https://github.com/Appboy/currents-examples/tree/master/sample-data/Custom%20HTTP/users/behaviors).

## Correspondance entre les utilisateurs

Les utilisateurs identifiés peuvent être associés à leur adresse `external_id` ou `alias`. Les utilisateurs anonymes peuvent être mis en relation avec leur `device_id`. Les utilisateurs identifiés qui ont été créés à l'origine en tant qu'utilisateurs anonymes ne peuvent pas être identifiés par leur `device_id`, et doivent être identifiés par leur `external_id` ou `alias`.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/heap/heap1.png %}
[3]: {% image_buster /assets/img/heap/heap2.png %}
[4]: {% image_buster /assets/img/heap/heap3.png %} 
