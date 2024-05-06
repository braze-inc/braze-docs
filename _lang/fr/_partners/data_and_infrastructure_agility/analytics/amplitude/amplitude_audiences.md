---
nav_title: Audiences Amplitude
article_title: Audiences Amplitude
page_order: 0
alias: /partners/amplitude_recommend/
description: "Cet article présente le partenariat entre currents Braze et Amplitude, une plateforme d’aide à la décision et d’analyse de produits."
page_type: partner
tool: Currents
search_tag: Partenaire

---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Audiences Amplitude

> [Amplitude](https://amplitude.com/) est une plateforme d’aide à la décision et d’analyse de produits.

L’intégration bidirectionnelle de Braze et Amplitude vous permet d’importer vos cohortes Amplitude, caractéristiques d'utilisateur et événements dans Braze et de créer des segments qui peuvent être utilisés afin de cibler des utilisateurs dans de futures campagnes ou de futurs Canvas. Vous pouvez également tirer parti de currents Braze pour [exporter vos événements Braze vers Amplitude]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/#data-export-integration) afin d’effectuer des analyses approfondies de vos produits et des données marketing.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Amplitude | Un [compte Amplitude](https://amplitude.com/) est requis pour profiter de ce partenariat. |
| Currents | Pour réexporter des données dans Amplitude, vous devez avoir configuré [currents Braze]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2} 

## Choisir une intégration 

Amplitude et Braze proposent deux méthodes d'intégration différentes. Lisez la documentation suivante pour déterminer quelles méthodes répondront à vos besoins :

- Braze Event Streaming (bêta) : Une intégration qui vous permet de transférer les données brutes d'événement Amplitude directement dans Braze.
- Importation de la cohorte : Une intégration qui vous permet de transférer les cohortes Amplitude directement dans Braze.

## Braze Event Streaming

### Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Clé d’API REST Braze | Une clé d’API REST Braze avec toutes les autorisations.<br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze | [URL de votre endpoint REST][1]. Votre endpoint dépendra de l’URL Braze pour votre instance. |
| Identifiant de l'application Braze | L'identifiant de l'application qui recevra les événements Amplitude. Cela se trouve dans **Braze Dashboard > Developer Console > Settings (Tableau de bord de Braze > Console du développeur > Paramètres)**.  |

### Configuration d’Amplitude

1. Dans Amplitude, accédez aux **Data Destinations (Destinations de données)**, puis recherchez « Braze - Event Stream » (Braze - Flux d’événements).
2. Saisissez un nom de synchronisation, puis cliquez sur **Create Sync (Créer une synchronisation)**.
3. Cliquez sur **Edit (Éditer)** et fournissez votre endpoint d'API REST Braze, votre clé d'API REST et votre identifiant d'application Braze.
4. Utilisez le filtre d'envoi d'événements pour sélectionner les événements à envoyer. Vous pouvez envoyer tous les événements, mais Amplitude recommande de choisir les plus importants. 
5. Lorsque vous avez terminé, activez la destination et enregistrez. 

Reportez-vous à [Braze Event Streaming](https://www.docs.developers.amplitude.com/data/destinations/braze/) pour plus d'informations sur cette intégration.

## Intégration de l’importation de données

Utilisez le partenariat entre Braze et Amplitude pour importer des cohortes Amplitude directement dans Braze afin de segmenter des audiences. Cela vous permet d’effectuer des analyses plus approfondies à l’aide d’Amplitude et d’exécuter vos stratégies de manière harmonieuse avec Braze.

{% multi_lang_include video.html id="8a57e44be7da423e9699cedd6c241eae" source="loom"%}

Toutes les intégrations que vous avez configurées seront prises en compte dans le volume de points de données de votre compte.

### Étape 1 : Obtenir la clé d’importation des données Braze

Dans Braze, accédez à **Technology Partners (Partenaires technologiques)** et sélectionnez **Amplitude**. Ici, vous trouverez l’endpoint REST pour générer votre clé d’importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d’importation des données et l’endpoint REST sont utilisés à l’étape suivante lors de la configuration d’un postback dans le tableau de bord d’Amplitude.<br><br>![]({% image_buster /assets/img/amplitude3.png %})

### Étape 2 : Configurer l’intégration Braze dans Amplitude

Dans Amplitude, accédez à **Sources & Destinations (Sources et destinations) > [Project name (Nom du projet)] > Destinations > Braze**. Dans l’invite qui apparaît, renseignez la clé d’importation des données de Braze et l’endpoint REST, puis cliquez sur **Save (Enregistrer)**.

![]({% image_buster /assets/img/amplitude.png %})

### Étape 3 : Exporter une cohorte Amplitude vers Braze

Pour exporter des utilisateurs d’Amplitude vers Braze, créez d’abord une [cohorte](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts) avec les utilisateurs que vous souhaitez exporter. Amplitude peut synchroniser les cohortes avec Braze en utilisant les identifiants suivants :
- Alias d’utilisateur
- ID de l’appareil
- ID utilisateur (ID externe)

Après avoir créé votre cohorte, cliquez sur **Sync to… (Synchroniser avec…)** pour exporter ces utilisateurs vers Braze.

#### Définition de la cadence de synchronisation

Les synchronisations de cohorte peuvent être définies comme synchronisation unique, planifiée quotidiennement, toutes les heures ou même en temps réel qui met à jour toutes les minutes. Assurez-vous de sélectionner une option adaptée aux besoins de votre entreprise tout en tenant compte de la consommation de [points de données]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/).

### Étape 4 : Segmenter des utilisateurs dans Braze

Dans Braze, pour créer un segment avec ces utilisateurs, accédez à **Segments** sous **Engagement**, nommez votre segment et sélectionnez **Amplitude Cohorts (Cohortes Amplitude)** en tant que filtre. Ensuite, utilisez l’option « includes (inclut) » et sélectionnez la cohorte que vous avez créée dans Amplitude. 

![Dans le générateur de segments de Braze, le filtre « amplitude_cohorts » est défini sur « includes_value » et « Amplitude cohort test » (Test de cohorte Amplitude).]({% image_buster /assets/img/amplitude2.png %})

Une fois enregistré, vous pouvez référencer ce segment pendant la création d’un Canvas ou d’une campagne dans l’étape de ciblage des utilisateurs.

## Synchroniser les caractéristiques et les calculs des utilisateurs

Utilisez Audiences pour envoyer des propriétés utilisateur et des calculs à Braze en tant qu'attributs personnalisés. Vous pourrez synchroniser les propriétés utilisateur ou les propriétés calculées pour les utilisateurs ayant été actifs au cours des 90 derniers jours.

Lorsqu'une propriété d'utilisateur ou un calcul est mis à jour, Amplitude met à jour un attribut personnalisé dans Braze avec le même nom que cette propriété d'utilisateur ou ce calcul.

Les synchronisations de caractéristiques et de calculs des utilisateurs créeront de nouveaux utilisateurs pour les identifiants d'utilisateurs qui n'existent pas encore dans Braze. Les calculs et les caractéristiques des utilisateurs ne peuvent être synchronisés uniquement à l'aide de l'ID utilisateur.

Consultez la documentation d'Amplitude pour en savoir plus sur [la synchronisation des propriétés, des recommandations et des cohortes vers des destinations tierces](https://help.amplitude.com/hc/en-us/articles/360060055531).

#### Comment synchroniser les propriétés et les calculs utilisateur

Dans Amplitude Audiences, sélectionnez **New > Sync (Nouveau > Synchroniser)**.

![]({% image_buster /assets/img/amplitude5.png %})

Ensuite, choisissez de synchroniser une propriété utilisateur, un calcul, une cohorte ou une recommandation. 

{% tabs %}
{% tab Syncing user property %}

Sélectionnez **User Property (Propriété utilisateur)**, puis la propriété utilisateur que vous souhaitez synchroniser.

![]({% image_buster /assets/img/amplitude7.png %})

Ensuite, sélectionnez une destination avec laquelle synchroniser votre propriété utilisateur.

![]({% image_buster /assets/img/amplitude8.png %})

Enfin, définissez la fréquence de votre synchronisation.

![Définissez votre cadence comme une synchronisation unique ou une synchronisation planifiée.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% tab Syncing computation %}

Sélectionnez **Computation (Calcul)** puis le calcul à synchroniser

![]({% image_buster /assets/img/amplitude10.png %})

Ensuite, sélectionnez une destination pour synchroniser votre calcul.

![]({% image_buster /assets/img/amplitude8.png %})

Enfin, définissez la fréquence de votre synchronisation.

![Définissez votre cadence comme une synchronisation unique ou une synchronisation planifiée.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% endtabs %}

## Endpoints de l’API des profils utilisateur d’Amplitude

Pour découvrir certains endpoints d’API Amplitude communs qui peuvent être utilisés avec le Contenu connecté, consultez notre [documentation sur l’API d’Amplitude]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_user_profile_api/).
