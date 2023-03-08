---
nav_title: Rokt Calendar
article_title: Rokt Calendar
alias: /partners/rokt_calendar/
description: "Cet article présente le partenariat entre Braze et Rokt Calendar, une technologie de marketing dynamique qui permet aux marques de gérer les notifications push relatives aux événements individuels et communications promotionnelles, sous la forme d’événements et de notifications du calendrier."
page_type: partner
search_tag: Partenaire

---

# Rokt Calendar

> [Rokt Calendar](https://www.rokt.com/rokt-calendar/) est une technologie de marketing calendaire dynamique qui permet aux marques de lancer des événements individuels et des communications promotionnelles sous forme d’événements et de notifications calendaires.

L’intégration de Braze et de Rokt Calendar permet à vos abonnés Rokt Calendar et à leurs données d’être transférés à Braze via le webhook Braze. Vous pouvez ensuite utiliser ces données dans les Canvas Braze pour le ciblage des trajets et la segmentation de l’audience en utilisant l’un des [attributs Rokt Calendar](#audience-segmentation) personnalisés suivants. 

## Conditions préalables

| Condition  | Description |
| ------------ | ----------- |
| Compte Rokt Calendar | Un compte Rokt Calendar spécifique au client est requis pour profiter de ce partenariat. Contactez [sales-calendar@rokt.com](mailto:sales-calendar@rokt.com) pour échanger avec un gestionnaire de compte  |
| Configuration de Rokt Calendar | Votre gestionnaire de compte Rokt Calendar travaillera avec vous pour configurer le calendrier selon vos exigences spécifiques, y compris les paramètres tels que :<br>- Drapeau de fusion<br>- Drapeau de SubscriberID de rechange<br>- Capture d'e-mail, si nécessaire |
| Identifiants OAuth de Rokt Calendar | Cette clé fournie par votre gestionnaire de compte Rokt Calendar vous permettra de connecter vos comptes de Braze et Rokt Calendar.<br><br>Celle-ci peut être créée dans le Tableau de bord de Braze sous **Manage Settings (Gérer les paramètres) > Connected Content (Contenu connecté) > +Add Credential (Ajouter des identifiants)**. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. Vous devrez fournir cette clé à votre gestionnaire de compte Rokt Calendar.<br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| [Endpoint REST de Braze]({{site.baseurl}}/api/basics/#endpoints) | URL de votre endpoint REST. Votre endpoint dépendra de l’URL Braze pour votre instance. |
| ID d’abonné externe | Il s’agit de l’ID utilisé par le processus d’abonnement de Rokt Calendar pour correspondre à l’utilisateur abonné du calendrier avec l’utilisateur Braze. C’est un élément que vous transmettez à Rokt Calendar.|
{: .reset-td-br-1 .reset-td-br-2}

## Segmentation d’audience {#audience-segmentation}

Lorsque Rokt Calendar crée un nouvel utilisateur ou fait correspondre un abonné existant avec un utilisateur Braze, Rokt Calendar envoie les attributs d’abonnement personnalisés suivants que vous pouvez filtrer dans Braze :

| Attribut personnalisé  | Définition       | Exemple          |
| ----------------  | ---------------- | ---------------- |
| `rokt:account_code` | Code du compte Rokt Calendar | `brazetest/f5733866ade2` et `brazetest/ff10919f1078` |
| `rokt:account_id` |ID du compte Rokt Calendar | `d0ce4299-7d6c-4888-bfd8-c7e867a0fa6c/f5733866ade2` |
| `rokt:account_name` | Nom du compte Rokt Calendar | `Test Braze/f5733866ade2` |
| `rokt:calendar_code` | Code du calendrier Rokt Calendar | `test-calendar-1/f5733866ade2` |
| `rokt:calendar_id` | ID du calendrier Rokt Calendar | `9a9007c7-f5a4-e811-b13c-06424c4f2724/f5733866ade2` |
| `rokt:calendar_title` | Titre du calendrier Rokt Calendar | `Calendrier des tests 1/f5733866ade2` |
| `rokt:country_code` | Code pays lié à l’abonnement créé | `AU/f5733866ade2` |
| `rokt:device_name` | Type de périphérique lié à l’abonnement créé | `Desktop/f5733866ade2` |
| `rokt:geo_country` | Pays d’origine lié à l’abonnement créé | `Australia/f5733866ade2` |
| `rokt:optIn1` | Si l’utilisateur a choisi la première des deux options liées à l’abonnement créé | `True/f5733866ade2` |
| `rokt:optIn2` | Si l’utilisateur a choisi la deuxième des deux options liées à l’abonnement créé | `True/f5733866ade2` |
| `rokt:source` | La source de l’abonnement créé | `brazetest.Rokt Calendarapp.com/f5733866ade2` |
| `rokt:subscriber_email` | L’adresse e-mail saisie par l’utilisateur pendant le processus d’abonnement | `test@email.com/f5733866ade2` |
| `rokt:subscription_id` | L’ID d’abonnement, servant d’identifiant unique, lié à l’abonnement créé | `06423672-b6ba-4536-aa36-70788a7a0a36` |
| `rokt:subscription_method` | Méthode d’abonnement (webcal/Google) liée à l’abonnement créé. | `WebCal/f5733866ade2` |
| `rokt:tags` | Balises de calendrier utilisées en lien avec l’abonnement créé. | `Calendrier de test 1/Toutes les équipes/f5733866ade2 et Calendrier de test 1/TeamI//f5733866ade2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Rokt Calendar déclenchera également un événement personnalisé `subscribe` dès que l’utilisateur s’est abonné à votre calendrier Rokt. Cet événement peut être utilisé dans la segmentation Braze ou servir de déclencheur pour une campagne ou un composant Canvas.

## Intégration

### Étape 1 : Créer une audience d’utilisateurs abonnés au calendrier

Pour envoyer des événements de calendrier à partir de Canvas, vous devez d’abord avoir un calendrier Rokt configuré avec les utilisateurs déjà abonnés. Pour ce faire, vous devez informer vos utilisateurs de la localisation et de la manière d’adhérer au calendrier. Rokt Calendar vous recommande de :

#### Fournir des points d’intégration de l’abonnement
Pour créer une audience d’abonnés au calendrier, vous devrez proposer une destination vers laquelle un utilisateur peut naviguer et s’abonner. Quelques exemples de points d’intégration d’abonnement sont :
  - Ajouter un bouton calendrier à votre site web
  - Ajouter un lien calendrier dans un e-mail ou SMS 
  - Ajouter un bouton calendrier à votre application
  - Ajouter un lien calendrier sur les réseaux sociaux

#### Promouvoir le calendrier
Pour créer une audience d’utilisateurs abonnés, vous devez promouvoir le calendrier auprès de votre audience afin qu’ils sachent comment s’abonner. Voici quelques exemples de promotion du calendrier :
  - Publications sur les réseaux sociaux
  - Bulletins d’information et mises à jour par e-mail
  - Publications sur des blogs
  - Notifications dans l’application

### Étape 2 : Créer un webhook Rokt Calendar dans Braze

Dans Braze, vous pouvez configurer une campagne de webhook ou un webhook au sein d’un Canvas pour :

- Envoyer un nouvel événement personnalisé : Autorisez l’ajout de nouveaux événements à un segment des calendriers des utilisateurs abonnés.
- Mettre à jour un événement personnalisé : Autorisez les mises à jour des événements existants dans les calendriers des utilisateurs abonnés.

Pour créer un modèle de webhook Rokt Calendar à utiliser dans les campagnes ou les Canvas futurs, accédez à la section **Templates & Media (Modèles et médias)** dans la plateforme Braze. Si vous souhaitez créer une campagne de webhook Rokt Calendar unique ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d’une nouvelle campagne.

{% tabs %}
{% tab Send a new event %}
Une fois que vous avez sélectionné le modèle de webhook Rokt Calendar, vous affichez les éléments suivants :
- **URL du webhook** : {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}`{% endraw %}
- **Corps de la demande** : Texte brut
{% endtab %}
{% tab Update an existing event %}
Une fois que vous avez sélectionné le modèle de webhook Rokt Calendar, vous affichez les éléments suivants :
- **URL du webhook** : {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}/update`{% endraw %}
- **Corps de la demande** : Texte brut
{% endtab %}
{% endtabs %}

#### En-têtes et méthode de demande

Rokt Calendar exige un `Header HTTP` pour l’autorisation qui comprend votre nom d’identifiant de Contenu connecté de Rokt Calendar. Les éléments suivants seront déjà inclus dans le modèle sous forme de paires clé-valeur, mais dans l’onglet **Settings (Paramètres)**, vous devez remplacer `<Rokt-Calendar-API>` par le nom de l’identifiant trouvé dans `Manage Settings (Gérer les paramètres) > Connected Content (Contenu connecté) > Credential (Identifiants)`.

{% raw %}
- **Méthode HTTP** : POST
- **En-tête de demande** :
  - **Autorisation** : Bearer `{% connected_content https://api.roktcalendar.com/oauth2/token :method post :basic_auth <Rokt-Calendar-API> :body grant_type=client_credentials :save token :retry %}{{token.access_token}}`
  - **Corps de la demande** : application/json
{% endraw %}

#### Corps de la demande

{% tabs local %}
{% tab Send a new event %}
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  },
  "subscriptionIds": ["{{custom_attribute.${rokt:subscription_id}| join: '","'  }}"]
}
```
{% endraw %}
{% endtab %}
{% tab Update an existing event %}
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  }
}
```
{% endraw %}
{% endtab %}
{% tab Event details %}
Les champs suivants comprennent des informations pouvant être personnalisées au niveau de l’événement.

| Champ             | Définition       | Exemple          |
| ----------------  | ---------------- | ---------------- |
| `eventId` <br>***Requis** | Identifiant unique pour l’ajout ou la mise à jour de l’événement | `Event_00001`
| `eventTitle` <br>***Requis** | Le titre de l’événement tel qu’il apparaît dans le calendrier | Soldes d’été 2019
| `eventDescr` | La description de l’événement telle qu’elle apparaît dans le calendrier | La vente est activée pendant trois jours ; cliquez sur ce lien `www.mybusiness.com/sale` pour découvrir les offres. |
| `eventLocation` | L’emplacement de l’événement tel qu’il apparaît dans le calendrier, notez que cela est souvent utilisé comme deuxième appel à l’action, qui est complémentaire à l’événement eventTitle. | Profitez de ces 50 % de réduction |
| `eventStart` <br>***Requis**  | La date et l’heure de début de l’événement telles qu’elles apparaissent dans le calendrier | `2019-02-21T15:00:00` |
| `eventEnd` <br>***Requis**  | La date et l’heure de début de l’événement telles qu’elles apparaissent dans le calendrier | `2019-02-21T16:00:00` |
| `eventTz` <br>***Requis**  | Le fuseau horaire de l’événement tel qu’il apparaît dans le calendrier, notez que la liste des fuseaux horaires applicables est disponible [ici](https://roktcalendar-api.readme.io/docs/timezones). | `Heure normale de l’Est` |
| `notifyBefore` <br>***Requis**  | L’heure de rappel de l’événement telle qu’elle apparaît dans le calendrier, notez que cela est exprimé en minutes | `15` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{% endtab %}
{% endtabs %}

{% alert tip %}
Pour obtenir une liste valide des fuseaux horaires, consultez [https://roktcalendar-api.readme.io/docs/timezones](https://roktcalendar.readme.io/docs/timezones).
{% endalert %}

### Étape 3 : Prévisualiser votre demande

Prévisualisez votre demande dans le volet **Preview (Prévisualiser)** ou accédez à l’onglet **Test** où vous pouvez sélectionner un utilisateur aléatoire, un utilisateur existant ou personnaliser votre propre test pour tester votre webhook.

{% alert important %}
N’oubliez pas d’enregistrer votre modèle avant de quitter la page ! <br>Des modèles de webhook mis à jour sont disponibles dans la liste **Saved Webhook Templates (Modèles de webhooks enregistrés)** lorsque vous créez une nouvelle [campagne de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/). 
{% endalert %}
