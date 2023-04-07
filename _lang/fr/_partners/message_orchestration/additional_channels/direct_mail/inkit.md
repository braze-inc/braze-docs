---
nav_title: Inkit
article_title: Inkit
alias: /partners/inkit/
description: "Cet article de référence présente le partenariat entre Braze et Inkit, qui vous permet d’économiser du temps et de l’effort en automatisant vos campagnes de publipostage et en remettant les clients hors ligne en ligne."
page_type: partner
search_tag: Partenaire

---

# Inkit

> [Inkit][1] vous permet d’atteindre et de communiquer avec vos clients en fournissant des campagnes de publipostage direct automatisées et personnalisées, en rendant des documents électroniques à grande échelle et en validant les adresses e-mail des clients. 

L’intégration de Braze et Inkit vous permet d’envoyer des messages Inkit à des utilisateurs Braze via des webhooks Braze. 

## Conditions préalables

|Condition| Description|
| ---| ---|
|Compte Inkit | Un [compte Inkit](https://console.liftigniter.com/login) est nécessaire pour tirer parti de ce partenariat. |
| Clé d’API Inkit<br><br>`<INKIT_API_TOKEN>` | Cette clé, disponible sur votre [Tableau de bord Inkit](https://app.inkit.io/#/account/integrations), vous permettra de connecter vos comptes Braze et Inkit.|
| ID du modèle Inkit<br><br>`<INKIT_TEMPLATE_ID>` | Cette clé est disponible dans l’URL de chaque modèle, ce qui vous permet d’envoyer votre modèle à Braze. <br><br>Par exemple, dans l’URL `https://app.inkit.io/#/templates/design/bd9b0b8c-c47b-40ae-8787-80dd76f6d2bb`, l’ID de modèle est `bd9b0b8c-c47b-40ae-8787-80dd76f6d2bb`. |
| En-tête HTTP  | Sur votre compte Inkit, vous associerez cette option avec votre clé d’API Inkit pour autoriser la connexion comme une paire clé-valeur dans votre modèle Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

### Étape 1 : Créer un modèle Inkit

Sur la plateforme Inkit, créez un modèle à utiliser dans votre campagne Braze. 
Reportez-vous à la [documentation Inkit](https://help.inkit.com/hc/en-us/articles/360036546873-Braze-Inkit-Integration) au sujet de ce partenariat pour en savoir plus.

### Étape 2 : Créer votre modèle de webhook Braze

Pour créer un modèle de webhook Inkit à utiliser dans les campagnes ou les Canvas, accédez à la section **Templates & Media** dans la plateforme Braze. Si vous souhaitez créer une campagne de webhook Inkit unique ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d’une nouvelle campagne.

![Une sélection de modèles de webhooks prêts à l’emploi disponibles dans l’onglet Webhook Templates de la section Templates & Media.][7]

Une fois que vous avez sélectionné le modèle de webhook Inkit, vous affichez les éléments suivants :
- **URL du webhook** : `https://internal.inkit.io/integrations/webhook`
- **Corps de la demande** : Texte brut

![Code du corps de la demande et URL du webhook affichés dans l’onglet de composition du constructeur de webhooks dans Braze.][5]

#### En-têtes et méthode de la requête

Inkit nécessite un `HTTP Header` pour obtenir une autorisation qui inclut la clé d’API Inkit encodée dans la base 64. Les éléments suivants seront déjà inclus dans le modèle comme paire clé-valeur, mais dans l’onglet **Settings** (Paramètres), vous devez remplacer le `<INKIT_API_TOKEN>` avec votre clé d’API Inkit.

{% raw %}
- **Méthode HTTP** : POST
- **En-tête de requête** :
  - **Autorisation** : Basiques `{{ '<INKIT_API_TOKEN>' | base64_encode }}`
  - **Corps de la demande** : application/json
{% endraw %}

#### Corps de la demande

Assurez-vous que cette valeur dans Liquid correspond aux attributs personnalisés appropriés associés aux champs obligatoires et facultatifs suivants. Vous pouvez également ajouter des champs de données personnalisés à n’importe quelle demande.

```json
{% raw %}{
  "api_token": "<INKIT_API_TOKEN>",
  "template_id": "<INKIT_TEMPLATE_ID>",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "company": "{{custom_attribute.${company_name}}}",
  "phone" : "{{${phone_number}}}",
  "address_line_1": "{{custom_attribute.${address}}}",
  "address_line_2": "{{custom_attribute.${address2}}}",
  "address_city": "{{${city}}}",
  "address_state": "{{custom_attribute.${state}}}",
  "address_zip": "{{custom_attribute.${zip}}}",
  "address_country": "{{${country}}}",
  "source" : "Braze"
}{% endraw %}
```

### Étape 3 : Prévisualiser votre demande

Votre texte brut indiquera automatiquement s’il s’agit d’une balise Braze applicable. `street`, `unit`, `state` et `zip` doivent être configurés comme [attributs personnalisés][3] pour envoyer ce webhook.

Prévisualisez votre demande dans le volet **Preview (Prévisualiser)** ou accédez à l’onglet **Test** où vous pouvez sélectionner un utilisateur aléatoire, un utilisateur existant ou personnaliser votre propre test pour tester votre webhook.

{% alert important %}
N’oubliez pas d’enregistrer votre modèle avant de quitter la page ! <br>Des modèles de webhook mis à jour sont disponibles dans la liste **Saved Webhook Templates (Modèles de webhooks enregistrés)** lorsque vous créez une nouvelle [campagne de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). 
{% endalert %}

[1]: https://www.inkit.com
[2]: https://help.inkit.com/hc/en-us/articles/360036546873-Braze-Inkit-Integration
[3]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes
[5]: {% image_buster /assets/img/inkit-integration.png %}
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
[7]: {% image_buster /assets/img/inkit-webhook-template.png %}