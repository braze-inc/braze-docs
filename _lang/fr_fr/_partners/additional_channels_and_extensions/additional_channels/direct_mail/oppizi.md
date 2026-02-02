---
nav_title: Oppizi
article_title: Oppizi 
alias: /partners/oppizi/
description: "Cet article de référence présente le partenariat entre Braze et Oppizi."
page_type: partner
search_tag: Partner
---

# Oppizi

> [Oppizi](https://www.oppizi.com/) est le leader mondial du marketing hors ligne, offrant aux entreprises une solution unique pour mener des campagnes de publipostage et de ciblage mesurables.

_Cette intégration est maintenue par Oppizi._

## Conditions préalables

| Condition                    | Description                                                                   |
| ------------------------------ | ----------------------------------------------------------------------------- |
| Compte Oppizi                 | Un compte Oppizi actif est nécessaire pour utiliser cette intégration.                 |
| Clé API d'Oppizi                 | Vous le trouverez dans votre compte Oppizi dans **Intégrations** > **Braze**.                |
| Oppizi Direct Mail workflow ID | Créez un flux de travail dans Oppizi sur la page de **flux de travail de publipostage** pour obtenir un ID. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d’utilisation

Avec l'intégration d'Oppizi, vous pouvez :

* **Envoyez des cartes postales automatisées** de publipostage à l'aide de déclencheurs Braze connectés au webhook et aux flux de travail de publipostage d'Oppizi.
* **Configurez des seuils, des vagues et des limites** dans les flux de publipostage d'Oppizi pour contrôler l'envoi de vos campagnes.
* **Créez des cartes postales professionnelles** avec l'outil de conception intégré d'Oppizi - aucune expérience en conception n'est requise.
* **Suivez les performances de votre campagne** en temps réel grâce au tableau de bord d'Oppizi.

## Intégration

### Étape 1 : Générez votre clé API Oppizi 

Pour utiliser votre modèle de webhook à Braze, vous devrez d'abord générer votre clé API Oppizi.

1. Connectez-vous à Oppizi.
2. Allez dans **Intégrations** > **Braze**.
3. Générez votre clé API.

Vous pouvez gérer, révoquer et créer vos clés à partir de cette page si nécessaire.

### Étape 2 : Créez un modèle de webhook Braze à Braze

Ensuite, créez un modèle de webhook pour Oppizi à Braze afin de l'utiliser dans vos futures campagnes ou Canvases.

1. Dans Braze, allez dans **Modèles** > **Modèles de webhook**.

Dans votre modèle de webhook, remplissez les champs suivants :

- **URL du webhook :** ```https://webhooks.oppizi.com/events```
- **Corps de la demande :** **Texte brut**

Pour la méthode de requête et les en-têtes, Oppizi exige qu'une méthode HTTP et les en-têtes HTTP suivants soient inclus dans le modèle. Remplissez les champs suivants :

- **Méthode HTTP :** POST
- **En-têtes de la requête :**
  - **Autorisation :** `Bearer <oppiziAPIKey>`
  - **Content-Type :** `application/json`

![Un exemple de l'en-tête du webhook Oppizi à Braze.]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_headers.png %})

Pour le **corps de la demande**, vous devez inclure le champ **oppiziWorkflowID**. Cet ID est généré lors de la création d'un flux de travail dans Oppiz et est nécessaire pour spécifier à quel flux de travail de publipostage vos destinataires doivent être ajoutés. Chaque flux de publipostage dans Oppizi a un ID unique, donc si vous créez un modèle de webhook Oppizi dans Braze, veillez à toujours mettre à jour l'ID du flux de travail pour qu'il soit correct.

{% alert note %}
Vérifiez que les attributs personnalisés requis sont configurés dans votre compte Braze pour les adresses postales de vos destinataires, car ils sont nécessaires pour l'envoi de publipostage.
{% endalert %}

![Un exemple de modèle de webhook Oppizi dans Braze.]({% image_buster /assets/img/oppizi/oppizi_braze_webhook_example.png %})

Voici un exemple de corps de requête :

{% raw %}
```json
{
    "event" : "workflow.addRecipient",
    "oppiziWorkflowID" : "<oppiziWorkflowID>",
    "requestType" : "live",
    "recipient" : {
        "recipientID" : "{{${braze_id}}}",
        "firstName" : "{{${first_name}}}",
        "lastName" : "{{${last_name}}}",
        "address1" : "{{custom_attribute.${address1}}}",
        "address2" : "{{custom_attribute.${address2}}}",
        "city" : "{{custom_attribute.${city}}}",
        "country" : "{{${country}}}",
        "zipCode" : "{{custom_attribute.${zipCode}}}",
        "state" : "{{custom_attribute.${state}}}"
    }
}
```
{% endraw %}

### Étape 3 : Créez un flux de travail pour le publipostage dans Oppizi

1. Dans Oppizi, allez dans **Direct Mail Workflow** > **Créer un workflow**
2. Configurez les détails du flux de travail, y compris les seuils, les vagues, le format des cartes postales et les illustrations.
3. Dans la section Détails du webhook, vous trouverez un corps de requête prêt à l'emploi, comprenant votre ID de flux de travail, que vous pouvez coller directement dans Braze.

### Étape 4 : Prévisualisez et testez votre demande dans Braze

Après avoir ajouté le corps de votre demande avec l'ID du flux de travail d'Oppizi, exécutez un test pour confirmer que votre configuration fonctionne comme prévu.

Pour exécuter le test, mettez à jour `requestType` de `live` à `test` dans le corps de la requête. Notez que cette étape est cruciale pour éviter d'ajouter des destinataires de test à votre audience de publipostage.

Une fois les tests terminés, remettez à jour `requestType` en `live` et enregistrez votre Canvas. Vous êtes maintenant prêt à lancer vos campagnes de publipostage automatisées.
