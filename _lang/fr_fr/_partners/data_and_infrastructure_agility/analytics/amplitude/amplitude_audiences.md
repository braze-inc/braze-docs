---
nav_title: Amplitude
article_title: Amplitude
page_order: 0
alias: /partners/amplitude_recommend/
description: "Cet article de référence présente le partenariat entre Braze et Amplitude, une plateforme d'analyse des produits et d'aide à la décision."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Cours Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude

> [Amplitude](https://amplitude.com/) est une plateforme d'analyse des produits et d'aide à la décision.

L'intégration bidirectionnelle entre Braze et Amplitude vous permet d'[importer vos cohortes]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/amplitude/), traits de caractère d'utilisateurs et événements d'Amplitude dans Braze, ainsi que de créer des segments qui peuvent cibler les utilisateurs dans de futures campagnes ou Canvases. Vous pouvez également tirer parti de Braze Currents pour [exporter vos événements Braze vers Amplitude]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/#data-export-integration) afin d’analyser plus en profondeur vos données produits et marketing.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte d'Amplitude | Un [compte Amplitude](https://amplitude.com/) est nécessaire pour bénéficier de ce partenariat. |
| Currents | Pour pouvoir exporter des données dans Amplitude, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Choisissez une intégration 

Amplitude et Braze proposent deux méthodes d'intégration différentes. Lisez la documentation suivante pour déterminer quelles méthodes répondent à vos besoins :

- Flux d'événements de Braze : Une intégration qui vous permet de transmettre les données brutes des événements d'Amplitude directement à Braze.
- [Importation de la cohorte]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/amplitude/): Une intégration qui vous permet de transmettre les cohortes d'Amplitude à Braze.

## Flux d'événements Braze

### Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Clé API REST de Braze | Une clé API REST de Braze avec toutes les autorisations.<br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Endpoint REST Braze | [Votre URL de l’endpoint REST][1].] Votre endpoint dépendra de l'URL de Braze pour votre instance. |
| Identifiant de l'application Braze | L'identifiant de l'application qui recevra les événements Amplitude. Vous trouverez cette information dans le **tableau de bord de Braze > Console de développement > Paramètres**. |

### Configuration de l'Amplitude

1. Dans Amplitude, naviguez vers **Destinations des données** puis recherchez "Braze - Flux d'événements".
2. Saisissez un nom de synchronisation, puis cliquez sur **Créer une synchronisation**.
3. Cliquez sur **Modifier** et indiquez votre endpoint de l'API REST de Braze, votre clé API REST et l'identifiant de l'application Braze.
4. Utilisez le filtre d'envoi d'événements pour sélectionner les événements à envoyer. Vous pouvez envoyer tous les événements, mais Amplitude recommande de choisir les plus importants. 
5. Lorsque vous avez terminé, activez la destination et enregistrez. 

Reportez-vous à la section [Flux d'événements de Braze](https://www.docs.developers.amplitude.com/data/destinations/braze/) pour plus d'informations sur cette intégration.

## Synchronisation des traits d'utilisateur et des calculs

Utilisez les audiences pour envoyer les propriétés et les calculs des utilisateurs à Braze en tant qu'attributs personnalisés. Vous pourrez synchroniser les propriétés des utilisateurs ou les propriétés calculées pour les utilisateurs qui ont été actifs au cours des 90 derniers jours.

Lorsque la propriété d'un utilisateur ou un calcul est mis à jour, Amplitude met à jour un attribut personnalisé dans Braze portant le même nom que la propriété de l'utilisateur ou le calcul.

Les synchronisations des traits d'utilisateur et des calculs créeront de nouveaux utilisateurs pour les identifiants d'utilisateur qui n'existent pas encore dans Braze. Les calculs et les traits d'utilisateur ne peuvent être synchronisés qu'à l'aide d'identifiants d'utilisateur. Un identifiant d'utilisateur peut être l'un des éléments suivants :
- ID externe
- ID Braze
- Alias utilisateur
- Adresse e-mail

Reportez-vous à la documentation d'Amplitude pour en savoir plus sur la [synchronisation des propriétés, des recommandations et des cohortes vers des destinations tierces](https://help.amplitude.com/hc/en-us/articles/360060055531).

#### Comment synchroniser les propriétés et les calculs des utilisateurs ?

Dans Amplitude Audiences, sélectionnez **Synchronisations > Créer une synchronisation.**

![]({% image_buster /assets/img/amplitude11.png %})

Ensuite, choisissez de synchroniser une propriété de l'utilisateur, un calcul, une cohorte ou une recommandation. 

{% tabs %}
{% tab Synchronisation des propriétés des utilisateurs %}

Sélectionnez **Propriété de l'utilisateur**, puis la propriété de l'utilisateur à synchroniser.

![]({% image_buster /assets/img/amplitude7.png %})

Ensuite, sélectionnez une destination vers laquelle synchroniser votre propriété d'utilisateur.

![]({% image_buster /assets/img/amplitude8.png %})

Enfin, définissez la fréquence de votre synchronisation.

![Définissez votre cadence comme une synchronisation unique ou une synchronisation planifiée.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% tab Calcul de synchronisation %}

Sélectionnez le **calcul**, puis le calcul souhaité à synchroniser.

![]({% image_buster /assets/img/amplitude10.png %})

Ensuite, sélectionnez une destination pour synchroniser votre calcul.

![]({% image_buster /assets/img/amplitude8.png %})

Enfin, définissez la fréquence de votre synchronisation.

![Définissez votre cadence comme une synchronisation unique ou une synchronisation planifiée.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% endtabs %}

## Points d'extrémité de l'API du profil utilisateur d'Amplitude

Pour vérifier certains des endpoints communs de l'API Amplitude qui peuvent être utilisés avec le contenu connecté, consultez notre documentation dédiée à [l'API Amplitude]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_user_profile_api/).
