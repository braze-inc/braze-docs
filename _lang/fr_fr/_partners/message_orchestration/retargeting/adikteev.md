---
nav_title: Adikteev
article_title: "Prédiction du taux d'attrition Adikteev"
description: "Cet article de référence présente le partenariat entre Braze et Adikteev, un moteur de fidélisation des utilisateurs qui combine la prédiction du taux de désabonnement avec un service complet de reciblage applicatif"
alias: /partners/adikteev/
page_type: partner
search_tag: Partner

---

# Prédiction du taux d'attrition Adikteev

> [Adikteev](https://www.adikteev.com/churn-prediction) est un moteur de rétention des utilisateurs qui combine la prédiction du taux de désabonnement avec un service complet de reciblage d'applications.

_Cette intégration est maintenue par Adikteev._

## À propos de l'intégration

L'intégration de Braze et d'Adikteev vous permet de stimuler la rétention des utilisateurs en exploitant la technologie de prédiction du taux d'attrition d'Adikteev au sein des campagnes CRM de Braze afin de cibler en priorité les segments d'utilisateurs désabonnés.

## Conditions préalables

| Condition | Description |
| --- | --- |
| Compte Adikteev | Un compte Adikteev est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST de Braze | Une clé API REST de Braze avec la permission `users.track`. <br><br> Celui-ci peut être créé dans le tableau de bord de Braze à partir de **Paramètres** > **API et Identifiants.** |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d’utilisation

{% tabs %}
{% tab Filtrage de l'audience %}
Affinement de vos segments d'audience en fonction du risque de désabonnement.<br> Les noms et valeurs des attributs personnalisés envoyés par Adikteev sont configurables.

![Capture d'écran montrant un exemple d'utilisation d'un attribut personnalisé envoyé par Adikteev comme filtre d'un segment d'audience.]({% image_buster /assets/img/adikteev/audience.png %})
{% endtab %}
{% tab Ciblage des messages %}
Personnalisation de vos campagnes de messages Braze en fonction du risque de désabonnement des destinataires.

![Capture d'écran montrant un exemple d'utilisation d'un attribut personnalisé envoyé par Adikteev comme filtre de ciblage de campagne.]({% image_buster /assets/img/adikteev/campaign.png %})
{% endtab %}
{% endtabs %}

## Intégration

### Étape 1 : Partagez le flux d'événements de votre application

Pour commencer à exécuter la prédiction du taux d'attrition sur l'audience de votre application, Adikteev aura besoin que vous activiez les rétroactions d'événements depuis votre plateforme de mesure mobile. Suivez les instructions du [site web d'assistance d'Adikteev](https://help.adikteev.com/hc/en-us/sections/8185123408914-Data-stream-activation) pour configurer cette fonction.

### Étape 2 : Créez votre clé API REST Braze

Dans Braze, accédez à **Paramètres** > **API et identifiants.** Sélectionnez **Créer une nouvelle clé API**, saisissez le nom de la clé API de votre choix et assurez-vous que l'autorisation suivante est ajoutée :

- `users.track`

### Étape 3 : Fournir des informations à l'équipe d'Adikteev

Pour terminer l'intégration, vous devez fournir votre clé API REST et l'URL de votre endpoint REST à votre gestionnaire de compte Adikteev. Adikteev établira la connexion et vous contactera une fois la configuration terminée pour valider l'intégration.

## Mise en lots et limites de débit

L'endpoint `user.track` est utilisé pour mettre à jour les détails concernant vos utilisateurs. Consultez la [documentation de l'API]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour obtenir tous les détails concernant les limites de débit, les requêtes groupées et les détails des requêtes.

{% alert tip %}
N'oubliez pas que les appels à l'API ne doivent être effectués que pour mettre à jour des données qui ont changé, afin de réduire le nombre total d'appels à l'API. En d'autres termes, ne mettez à jour que les utilisateurs dont le segment ’attrition a changé.
{% endalert %}

## Identifiants des utilisateurs et des appareils

Les profils utilisateurs dans Braze peuvent être associés à n'importe quel type d'identifiant d'utilisateur ou d'appareil ; la liste des options disponibles dépend de la manière dont vous avez intégré la collecte de données à Braze. Pour Adikteev, vous devrez trouver un identifiant commun entre votre MMP et vos profils utilisateurs dans Braze afin d'envoyer correctement les informations relatives à la segmentation du désabonnement.

## Conservation et suppression des données

Si aucune mise à jour n'est effectuée, l'attribut et sa valeur sont conservés indéfiniment dans les profils utilisateurs de Braze.

Pour supprimer un attribut de profil, réglez-le sur `null`.

## Charges utiles des requêtes

La charge utile envoyée par Adikteev à Braze est personnalisable et peut être configurée en fonction des besoins du client. Il s'agit notamment de configurer les identifiants utilisés, le nom de l'attribut personnalisé et de déterminer si Adikteev peut créer de nouveaux utilisateurs dans Braze ou seulement mettre à jour les utilisateurs existants.


## Assistance et résolution des problèmes

Contactez votre gestionnaire de compte Adikteev pour toute question relative à l'intégration ou pour tout soutien concernant vos cas d'utilisation.

