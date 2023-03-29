---
nav_title: optilyz
article_title: optilyz
page_order: 1
description: "Cet article de référence présente le partenariat entre Braze et optilyz, qui vous permet d’exécuter des campagnes de publipostage direct axées sur le client, durables et rentables."
alias: /partners/optilyz/
page_type: partner
search_tag: Partenaire

---

# optilyz

> [optilyz][1] est une plateforme d’automatisation du publipostage qui vous permet de mener des campagnes de publipostage plus axées sur le client, plus durables et plus rentables. 

Utilisez l’intégration du webhook d’optilyz et de Braze pour envoyer à vos clients des publipostages tels que des lettres, des cartes postales et des « prêts-à-poster ».

## Conditions préalables

| Condition | Description |
|---|---|
|compte optilyz | Un compte optilyz est requis pour profiter de ce partenariat. |
| Clé d’API optilyz<br><br>`<OPTILYZ_API_KEY>`| Votre gestionnaire du succès des clients optilyz vous fournira votre clé d’API optilyz.<br><br>Cette clé d’API vous permet de connecter vos comptes Braze et optilyz. |
| ID d’automatisation optilyz<br><br>`<OPTILYZ_AUTOMATION_ID>` | L’ID d’automatisation se trouve dans une case dans l’en-tête de la page.<br><br>Lorsque vous êtes connecté à optilyz, vous pouvez naviguer vers l’automatisation vers laquelle vous souhaitez envoyer des données.<br>L’automatisation doit être activée d’abord. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Cas d’utilisation

Gérer le publipostage comme un canal numérique signifie s’éloigner des envois de masse et exploiter le canal dans le cadre de vos parcours clients (numériques). Les avantages d’une approche moderne du publipostage sont les suivants :
- Augmentation des taux de conversion grâce à une pertinence accrue, des cas d’utilisation supplémentaires, des tests A/B plus faciles et des effets cross-canal
- Réduction des efforts grâce à l’automatisation et à une solution de bout en bout
- Réduction des coûts grâce à des contrats-cadres et à la transparence des coûts

## Intégration

Pour vous intégrer à optilyz, utilisez l’API [optilyz][2] pour envoyer les données du destinataire au webhook Braze.

### Étape 1 : Créer votre modèle de webhook Braze

Pour créer un modèle de webhook optilyz à utiliser dans les campagnes ou les Canvas, accédez à la section **Templates & Media (Modèles et médias)** dans la plateforme Braze. Si vous souhaitez créer une campagne de webhook optilyz unique ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d’une nouvelle campagne.

Dans votre nouveau modèle de webhook, renseignez les champs suivants :
- **URL du webhook** : `https://www.optilyz.com/api/v2/automations/<OPTILYZ_AUTOMATION_ID>/recipient`
- **Corps de la demande** : Texte brut

#### En-têtes et méthode de la requête

optilyz nécessite également un en-tête HTTP pour l’autorisation et une méthode HTTP. Les éléments suivants seront déjà inclus dans le modèle comme paire clé-valeur, mais dans l’onglet **Settings (Paramètres)**, vous devez remplacer le `<OPTILYZ_API_KEY>` avec votre clé d’API optilyz. Cette clé doit inclure le caractère « : » directement après la clé et être encodée dans la base 64. 

- **Méthode HTTP** : POST
- **En-têtes de requête** :
  - **Autorisation** : {% raw %} `{{ '<OPTILYZ_API_KEY>:' | base64_encode }}` {% endraw %}
  - **Type de contenu** : application/json

![En-têtes de demande et méthode HTTP affichés dans le générateur de webhooks de Braze.][6]{: style="max-width:50%"}

#### Corps de la demande

Dans le corps de demande suivant, vous pouvez utiliser n’importe quelle balise de personnalisation Liquid et créer un modèle de demande personnalisée. Voir la [documentation API][2] d’optilyz.

Le champ `variation` est facultatif et peut définir la conception à utiliser à l’intérieur de l’automatisation. Si une variation est omise, optilyz attribuera l’une des variations définies de manière aléatoire.

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

![Image du code du corps de la demande et URL du webhook affichés dans l’onglet de composition du constructeur de webhooks dans Braze.][5]

### Étape 2 : Prévisualiser votre demande

Ensuite, prévisualisez votre demande dans le volet **Preview (Prévisualiser)** ou accédez à l’onglet **Test** où vous pouvez sélectionner un utilisateur aléatoire, un utilisateur existant ou personnaliser votre propre test pour tester votre webhook. N’oubliez pas d’enregistrer votre modèle avant de quitter la page !

![Différents champs de test disponibles dans l’onglet test du générateur de webhooks de Braze.][7]

{% alert important %}
N’oubliez pas d’enregistrer votre modèle avant de quitter la page ! <br>Des modèles de webhook mis à jour sont disponibles dans la liste **Saved Webhook Templates (Modèles de webhooks enregistrés)** lorsque vous créez une nouvelle [campagne de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). 
{% endalert %}

[1]: https://optilyz.com
[2]: https://www.optilyz.com/doc/api/
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/webhook_template/
[5]: {% image_buster /assets/img/optilyz/optilyz_compose.png %}
[6]: {% image_buster /assets/img/optilyz/optilyz_settings.png %}
[7]: {% image_buster /assets/img/optilyz/optilyz_testing.png %}
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/