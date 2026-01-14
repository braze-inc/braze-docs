---
nav_title: Amplitude
article_title: "Importation de cohortes d'Amplitude"
description: "Cet article de référence décrit la fonctionnalité d'importation de la cohorte d'Amplitude, une plateforme d'analyse de produits et d'aide à la décision."
page_type: partner
search_tag: Partner
---

# Amplitude : importation de la cohorte

> Cet article explique comment importer des cohortes d'utilisateurs d'[Amplitude](https://amplitude.com/) vers Braze. Pour plus d'informations sur l'intégration d'Amplitude et de ses autres fonctionnalités, consultez l'[article principal sur Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences/).

## Intégration de l'importation de données

Toute intégration que vous configurez sera prise en compte dans le volume de points de données de votre compte.

### Étape 1 : Obtenir la clé d'importation des données de Braze

Dans Braze, accédez à **Intégrations de partenaires** > **Partenaires technologiques** et sélectionnez **Amplitude**. Ici, vous trouverez l’endpoint REST et générerez votre clé d'importation des données Braze. 

Une fois générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d'importation des données et l’endpoint REST sont utilisés à l'étape suivante lors de la configuration d'un postback dans le tableau de bord d'Amplitude.<br><br>![]({% image_buster /assets/img/amplitude3.png %})

### Étape 2 : Configurer l'intégration de Braze dans Amplitude

Dans Amplitude, accédez à **Sources et destinations** > **[nom du projet] ]** > **Destinations** > **Braze**. **Dans l'invite qui s'affiche, indiquez la clé d'importation des données Braze et l’endpoint REST, puis cliquez sur Enregistrer.**

![]({% image_buster /assets/img/amplitude.png %})

### Étape 3 : Exporter une cohorte Amplitude vers Braze

Tout d'abord, pour exporter des utilisateurs d'Amplitude vers Braze, créez une [cohorte](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts) d'utilisateurs que vous souhaitez exporter. Amplitude peut synchroniser les cohortes avec Braze à l'aide des identifiants suivants :
- Alias d'utilisateur
- ID de l'appareil
- ID utilisateur (ID externe)

Vous pouvez configurer plusieurs connexions Braze dans votre compte Amplitude. Cela vous permet de configurer une connexion pour synchroniser les ID des utilisateurs connus et une autre pour synchroniser les ID des appareils des utilisateurs anonymes.

Une fois que vous avez créé une cohorte, cliquez sur **Synchroniser avec...** pour exporter ces utilisateurs vers Braze.

{% alert important %}
Seuls les utilisateurs qui existent déjà dans Braze pourront être ajoutés ou supprimés d'une cohorte. L'importation d'une cohorte ne créera pas de nouveaux utilisateurs dans Braze.
{% endalert %}

#### Définition de la cadence de synchronisation

Les synchronisations des cohortes peuvent être configurées pour être une synchronisation unique, planifiée quotidiennement ou toutes les heures, ou même en temps réel avec des mises à jour toutes les minutes. Assurez-vous de sélectionner une option adaptée aux besoins de votre entreprise tout en tenant compte de la consommation de [données]({{site.baseurl}}/user_guide/data/data_points/).

### Étape 4 : Segmentez les utilisateurs dans Braze

Dans Braze, pour créer un segment de ces utilisateurs, accédez à **Segments** sous **Engagement**, nommez votre segment et sélectionnez **Amplitude Cohortes comme filtre**. Ensuite, utilisez l'option « inclut » et choisissez la cohorte que vous avez créée dans Amplitude. 

![Dans le générateur de segments Braze, le filtre « amplitude_cohorts » est défini sur « includes_value » et « Amplitude cohort test ». ]({% image_buster /assets/img/amplitude2.png %})

Après l'avoir enregistré, vous pouvez faire référence à ce segment lors de la création d'un canvas ou d'une campagne à l'étape du ciblage des utilisateurs.

## Correspondance entre les utilisateurs

Les utilisateurs identifiés peuvent être associés à leur adresse `external_id` ou `alias`. Les utilisateurs anonymes peuvent être mis en relation avec leur `device_id`. Les utilisateurs identifiés qui ont été créés à l'origine en tant qu'utilisateurs anonymes ne peuvent pas être identifiés par leur `device_id`, et doivent être identifiés par leur `external_id` ou `alias`.
