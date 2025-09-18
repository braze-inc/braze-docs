---
nav_title: optilyz
article_title: optilyz
description: "Cet article de référence décrit le partenariat entre Braze et optilyz, qui vous permet de mener des campagnes de publipostage plus orientées client, durables et rentables."
alias: /partners/optilyz/
page_type: partner
search_tag: Partner

---

# optilyz

> [optilyz][1] est une plateforme d'automatisation du publipostage qui vous permet de mener des campagnes de publipostage plus orientées client, durables et rentables. 

_Cette intégration est maintenue par Optilyz._

## À propos de l'intégration

Utilisez l'intégration du webhook optilyz et Braze pour envoyer à vos clients du publipostage, tel que des lettres, des cartes postales et des envois automatiques.

## Conditions préalables

| Condition | Description |
|---|---|
|compte optilyz | Un compte optilyz est nécessaire pour bénéficier de ce partenariat. |
| clé API optilyz<br><br>`<OPTILYZ_API_KEY>`| Le gestionnaire de la satisfaction client d'Optilyz vous fournira votre clé d’API Optilyz.<br><br>Cette clé API vous permettra de connecter vos comptes Braze et optilyz. |
| ID d'automatisation optilyz<br><br>`<OPTILYZ_AUTOMATION_ID>` | L'ID d'automatisation se trouve dans une zone de l'en-tête de la page.<br><br>Une fois connecté à optilyz, vous pouvez accéder au processus d’automatisation auquel vous souhaitez envoyer des données.<br>L'automatisme doit d'abord être activé. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Cas d'utilisation

Pour gérer le publipostage comme un canal numérique, vous devez abandonner les envois de masse et tirer parti de ce canal dans le cadre de vos parcours clients (numériques). Les avantages d'une approche moderne du publipostage sont les suivants :
- Meilleurs taux de conversion grâce à une pertinence accrue, à des cas d'utilisation supplémentaires, à des tests A/B simplifiés et à des effets cross-canal
- Effort réduit grâce à l'automatisation et à une solution de bout en bout
- Réduction des coûts grâce à des contrats-cadres et à la transparence des coûts

## Intégration

Pour intégrer optilyz, utilisez l'[API optilyz][2] pour envoyer des données du destinataire au webhook Braze.

### Étape 1 : Créez votre modèle de webhook Braze

Pour créer un modèle de webhook Optilyz à utiliser dans de futures campagnes ou Canvases, accédez à **Modèles > Modèles** de **webhook** sur la plateforme Braze. 

Si vous souhaitez créer une campagne webhook Optilyz unique ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d'une nouvelle campagne.

Dans votre nouveau modèle de Webhook, renseignez les champs suivants :
- **URL du webhook** : L'URL du webhook est unique pour chaque client et votre gestionnaire de la satisfaction client optilyz vous la fournira.
- **Corps de la requête** : Texte brut

#### En-têtes et méthode de la requête

optilyz nécessite également un en-tête HTTP pour l'autorisation et une méthode HTTP. Les éléments suivants seront déjà inclus dans le modèle en tant que paire clé-valeur, mais dans l'onglet**Paramètres**, vous devez remplacer `<OPTILYZ_API_KEY>` par votre clé d’API optilyz. Cette clé doit inclure un « : » juste après la clé et être encodée en base 64. 

- **Méthode HTTP** : POST
- **En-têtes de la requête** :
  - **Autorisation** : {% raw %} `{{ '<OPTILYZ_API_KEY>:' | base64_encode }}` {% endraw %}
  - **Type de contenu : application/json**

![Les en-têtes de requête et la méthode HTTP affichés dans le générateur de webhook Braze.][6]{: style="max-width:50%"}

#### Corps de la requête

[Dans le corps de requête suivant, vous pouvez utiliser n'importe quel tag de personnalisation Liquid et créer un modèle de requête personnalisé conformément à la documentation de l'API d'optilyz.][2]

Le champ `variation` est facultatif et permet de définir quelle conception au sein de l'automatisation doit être utilisée. Si une variation est omise, optilyz attribuera l'une des variations définies de manière aléatoire.

{% raw %}
```json
{
    "address": {
        "title": "{{custom_attribute.${salutation}}}",
        "firstName": "{{${first_name}}}",
        "lastName": "{{${last_name}}}",
        "street": "{{custom_attribute.${street}}}",
        "houseNumber": "{{custom_attribute.${houseNumber}}}",
        "address2": "{{custom_attribute.${address2}}}",
        "zipCode": "{{custom_attribute.${zipCode}}}",
        "city": "{{custom_attribute.${city}}}",
        "country": "{{custom_attribute.${country}}}"
    },
    "variation": {{custom_attribute.${designVariation}}}
}
```
{% endraw %}

![Une image du code du corps de la requête et de l'URL du webhook affichés dans l'onglet de composition du générateur de webhooks Braze.][5]

### Étape 2 : Prévisualisez votre requête

Ensuite, prévisualisez votre requête dans le panneau **Aperçu** ou accédez à l'onglet **Test**, où vous pouvez sélectionner un utilisateur aléatoire, un utilisateur existant ou personnaliser le vôtre pour tester votre webhook. N'oubliez pas d'enregistrer votre modèle avant de quitter la page !

![Différents champs de test sont disponibles dans l'onglet de test du générateur de webhooks Braze.][7]

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page ! <br>Les modèles de webhook mis à jour se trouvent dans la liste **Modèles de webhook enregistrés** lors de la création d'une nouvelle [campagne webhook.]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)
{% endalert %}


[1]: https://optilyz.com
[2]: https://www.optilyz.com/doc/api/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/
[5]: {% image_buster /assets/img/optilyz/optilyz_compose.png %}
[6]: {% image_buster /assets/img/optilyz/optilyz_settings.png %}
[7]: {% image_buster /assets/img/optilyz/optilyz_testing.png %}
[9]: {{site.baseurl}}/user_guide/message_building_by_ (en anglais)channel/webhooks/creating_a_webhook/