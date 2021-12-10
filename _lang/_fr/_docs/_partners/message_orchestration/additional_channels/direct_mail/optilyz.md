---
nav_title: optilyz
article_title: optilyz
page_order: 1
description: "Cet article décrit le partenariat entre Braze et optilyz, qui vous permet de mener des campagnes de publipostage plus axées sur la clientèle, durables et rentables."
alias: /fr/partners/optilyz/
page_type: partenaire
search_tag: Partenaire
---

# optilyz

> [optilyz][1] est une plate-forme d'automatisation de messagerie directe qui vous permet d'exécuter des campagnes de messagerie directe plus axées sur le client, durables et rentables.

Utilisez l'intégration optilyz et Braze webhook pour envoyer à vos clients du courrier direct comme des lettres, des cartes postales et des auto-mailers.

## Pré-requis

| Exigences                                                                | Libellé                                                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| compte optilyz                                                           | Un compte optilyz est requis pour profiter de ce partenariat.                                                                                                                                                                                                                                           |
| clé API optilyz<br><br>`<OPTILYZ_API_KEY>`             | Votre gestionnaire client optilyz vous fournira votre clé API optilyz.<br><br>Cette clé API vous permettra de connecter vos comptes Braze et optilyz.                                                                                                                                       |
| optilyz automation ID<br><br>`<OPTILYZ_AUTOMATION_ID>` | L'identifiant d'automatisation peut être trouvé dans une boîte dans l'en-tête de la page.<br><br>Lorsque vous êtes connecté à optilyz, vous pouvez naviguer jusqu'à l'automatisation dans laquelle vous voulez envoyer des données.<br>L'automatisation doit être activée en premier. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Cas d'utilisation

Exécuter le courrier direct comme un canal numérique signifie s'éloigner des mailings de masse et tirer parti du canal dans le cadre de vos voyages (numériques). Les avantages d'une approche moderne du publipostage sont :
- Augmentation des taux de conversion grâce à une pertinence accrue, des cas d'utilisation supplémentaires, un test A/B plus facile et des effets transversaux
- Réduction de l'effort par l'automatisation et une solution de bout en bout
- Réduction des coûts par le biais des contrats encadrés et de la transparence des coûts

## Intégration

Pour intégrer avec optilyz, utilisez l'API [optilyz][2] pour envoyer les données du destinataire au webhook de Braze.

### Étape 1 : Créez votre modèle de webhook Braze

Créer un modèle de webhook optilyz à utiliser dans les futures campagnes ou Canvases, accédez à la section **Modèles & Médias** de la plateforme Braze. Si vous souhaitez créer une campagne d'optilyz unique ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d'une nouvelle campagne.

Dans votre nouveau modèle Webhook, remplissez les champs suivants :
- **URL du Webhook**: `https://www.optilyz.com/api/v2/automations/<OPTILYZ_AUTOMATION_ID>/recipient`
- **Corps de la requête**: Texte brut

#### En-têtes de requête et méthode

optilyz a également besoin d'un en-tête HTTP pour être autorisé et d'une méthode HTTP. Les éléments suivants seront déjà inclus dans le modèle en tant que paire clé-valeur, mais dans l'onglet **Paramètres** , vous devez remplacer la `<OPTILYZ_API_KEY>` par votre clé API optilyz. Cette clé doit inclure un ":" directement après la clé et être encodée en base 64.

- **Méthode HTTP**: POST
- **En-têtes de la requête**:
  - **Autorisation**: {% raw %} `{{ '<OPTILYZ_API_KEY>:' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

!\[optilyz_settings\]\[6\]{: style="max-width:50%"}

#### Corps de la requête

Dans le corps de la requête suivante, vous pouvez utiliser n'importe quelle étiquette de personnalisation Liquid et construire un modèle de requête personnalisé selon la [documentation API][2] d'optilyz.

Le champ `variation` est facultatif et peut définir la conception à l'intérieur de l'automatisation à utiliser. Si une variation est omise, optilyz attribuera aléatoirement une des variations définies.

{% raw %}
```json
{
    "address": {
        "title": "{{custom_attribute.${salutation}}}",
        "firstName": "{{${first_name}}}",
        "lastName": "{{${last_name}}}",
        "street": "{{custom_attribute.${street}}}",
        "houseNumber": "{{custom_attribute.${houseNumber}}}",
        "adresse2": "{{custom_attribute.${address2}}}",
        "zipCode": "{{custom_attribute.${zipCode}}}",
        "city": "{{custom_attribute.${city}}}",
        "pays": "{{custom_attribute.${country}}}"
    },
    "variation": {{custom_attribute.${designVariation}}}
}
```
{% endraw %}

!\[optilyz_compose\]\[5\]

### Étape 2 : Aperçu de votre demande

Ensuite, prévisualisez votre requête dans le panneau de gauche ou accédez à l’onglet __Test__ où vous pouvez sélectionner un utilisateur aléatoire, un utilisateur existant, ou personnaliser le vôtre pour tester votre webhook. N'oubliez pas d'enregistrer votre modèle avant de quitter la page!

!\[optilyz_testing\]\[7\]

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page! <br>Les modèles de webhook mis à jour peuvent être trouvés dans la liste **Modèles de Webhook enregistrés** lors de la création d'une nouvelle [campagne webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}
[5]: {% image_buster /assets/img/optilyz/optilyz_compose.png %} [6]: {% image_buster /assets/img/optilyz/optilyz_settings.png %} [7]: {% image_buster /assets/img/optilyz/optilyz_testing.png %}

[1]: https://optilyz.com
[2]: https://www.optilyz.com/doc/api/
[2]: https://www.optilyz.com/doc/api/