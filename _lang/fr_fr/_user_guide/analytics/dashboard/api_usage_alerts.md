---
nav_title: "Alertes sur l'utilisation de l'API"
article_title: "Alertes sur l'utilisation de l'API"
description: "Cet article donne un aperçu des alertes d'utilisation de l'API, qui vous permettent de détecter de manière proactive un trafic inattendu."
page_order: 3.6
---

# Alertes sur l'utilisation de l'API

> Les alertes d'utilisation de l'API offrent une visibilité essentielle sur l'utilisation de votre API, ce qui vous permet de détecter de manière proactive un trafic inattendu. En configurant ces alertes pour suivre les volumes de requêtes API clés, vous pouvez recevoir des notifications en temps réel et résoudre les problèmes avant qu'ils n'aient un impact sur vos campagnes marketing.

## À propos des alertes sur l'utilisation de l'API

Vous pouvez utiliser les alertes d'utilisation de l'API pour surveiller les volumes de requêtes pour les catégories suivantes :

| Catégorie API | Détails |
|--------------|---------|
| Points d'extrémité de l'API REST | Suit l'utilisation de tous les appels d'API REST effectués vers le backend de Braze, tels que l'envoi de messages, la création de campagnes ou l'exportation d'utilisateurs. |
| Demandes d'API du SDK | Trace les demandes d'API effectuées à partir des SDK de Braze dans les apps clientes, comme le déclenchement de messages in-app ou la synchronisation des données de l'utilisateur.<br><br>_\*Seulement disponible pour les clients qui ont acheté le service Utilisateurs actifs par mois - CY 24-25._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Création d'une alerte sur l'utilisation de l'API

Pour créer une alerte sur l'utilisation de l'API :

1. Allez dans **Paramètres** > **API et identifiants** > **Alertes d'utilisation de l'API**, puis créez une nouvelle alerte.
2. Saisissez un nom pour votre alerte et choisissez les points d'extrémité de l'API REST et les clés API pour lesquels vous souhaitez être alerté.
3. Définissez vos critères d'alerte en choisissant un ou plusieurs codes de réponse et en spécifiant les [seuils d'alerte](#api-usage-alert-thresholds).
4. Lorsque vous avez terminé, basculez sur l **'activation de l'alerte.**
    Exemple d'alerte d'utilisation de l'API qui envoie des notifications lorsque le nombre d'utilisateurs augmente de 100 % en l'espace d'une heure.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

## Seuils d'alerte {#api-usage-alert-thresholds}

Lorsque vous définissez vos critères d'alerte, vous pouvez ajuster les seuils suivants :

<table>
  <thead>
    <tr>
      <th>Champ d'application</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Condition de seuil</td>
      <td>
        Définit les conditions menant au volume seuil pour lequel vous souhaitez être alerté. Les éléments suivants sont pris en charge :<br><br>
        <ul>
          <li><strong>Augmenté de</strong> ou <strong>Diminué de</strong>: Compare les demandes par rapport à la fenêtre temporelle précédente.</li>
          <li><strong>Augmenté en pourcentage</strong> ou <strong>Diminué en pourcentage :</strong> Compare le pourcentage de variation des demandes par rapport à la fenêtre temporelle précédente.</li>
          <li><strong>Supérieur ou égal</strong>, ou <strong>inférieur ou égal</strong>: Compte les demandes dans une fenêtre temporelle.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Volume seuil</td>
      <td>Utilisé en conjonction avec la condition de seuil.</td>
    </tr>
    <tr>
      <td>A l'intérieur</td>
      <td>La fenêtre temporelle pour l'évaluation de l'alerte.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Mise en place de notifications d'alerte

Vous pouvez configurer une alerte par e-mail, une alerte par webhook ou les deux. Les alertes webhook peuvent être très utiles pour des cas d'utilisation tels que l'envoi d'une alerte à des plateformes externes, comme un canal Slack. Pour un exemple, consultez notre [documentation](https://www.braze.com/docs/user_guide/administrative/app_settings/company_settings/notification_preferences#slack-incoming-webhook-integration) sur l'intégration des alertes avec Slack pour connaître nos préférences en matière de notification.

Un e-mail sera envoyé à l'adresse sélectionnée lorsque les critères de l'alerte sont atteints.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### Exemple de charge utile {#payload}

Vous trouverez ci-dessous un exemple de charge utile pour le corps d'un webhook d'alerte sur l'utilisation de l'API.

```json
{
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "alert_criteria": [
    	"response_codes": ["201", "202", "203"],
    	"threshold_condition: "Increased by %",
    	"threshold_volume": 50,
    	"within": "1 day"
    	],
    "timeframe_start": 2025-03-20T15:35:00Z,
    "timeframe_end": 2025-03-20T16:35:00Z,
    "volume": 1500,
    "previous_timeframe_start": 2025-03-20T14:35:00Z,
    "previous_timeframe_end": 2025-03-20T15:35:00Z,
    "previous_volume": 1000
  },
  "text": "Your My First API Usage Alert alert has triggered. You can view your alert and usage here: <link>. Note that this alert will reset in 1 day, as each alert will only send one notification per 8 hours."
}
```

### Exemple d'alertes

Voici quelques façons de mettre en place vos configurations d'alerte d'utilisation de l'API afin d'être notifié dans les scénarios suivants.

{% tabs local %}
{% tab api health %}
Vous pouvez mettre en place des alertes pour surveiller l'état général de votre API. Par exemple, vous pouvez configurer ces alertes lorsque les erreurs d'API augmentent de façon drastique, par exemple de 20 % par rapport à l'heure précédente.

| Endpoint | clé API | Code de réponse | Condition de seuil | Volume seuil | A l'intérieur |
| --- | --- | --- | --- | --- | --- |
| Tous les endpoints | Toutes les clés API | `4XX` et `5XX` | Augmentation de 10% | 10 | 1 heure |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab endpoint rate limit %}
Soyez alerté lorsque votre espace de travail atteint sa limite de débit pour `/users/track` endpoint. Vous pouvez également appliquer cette configuration à d'autres endpoints de Braze.

| Endpoint | clé API | Code de réponse | Condition de seuil | Volume seuil | A l'intérieur |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | Toutes les clés API | `429` | Supérieur ou égal à | 100 | 1 heure |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab API-triggered campaigns %}
Cette configuration d'alerte vous informe lorsque des erreurs se produisent pour les campagnes et les Canvases déclenchées par l'API, dont certaines peuvent être hautement prioritaires.

| Endpoint | clé API | Code de réponse | Condition de seuil | Volume seuil | A l'intérieur |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/campagnes/déclencheurs/envoi</code></li><li><code>/canvas/trigger/send</code></li><li><code>/messages/envoi</code></li></ul>{:/} | Toutes les clés API | `4XX` et `5XX` | Supérieur ou égal à | 1 | 1 heure |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab partner integrations %}
Utilisez la configuration d'alerte suivante pour être alerté lorsqu'une intégration partenaire cesse d'envoyer des données à Braze.

| Endpoint | clé API | Code de réponse | Condition de seuil | Volume seuil | A l'intérieur |
| --- | --- | --- | --- | --- | --- |
| Tous les endpoints | La clé API utilisée pour l'intégration de votre partenaire | Tous les codes de réponse | Inférieur ou égal à | 0 | 1 jour |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}
{% endtabs %}

## Considérations

- Chaque alerte active n'enverra un e-mail ou une notification webhook qu'une fois toutes les 8 heures. Cela permet d'éviter un trop grand nombre de notifications à partir d'une seule alerte. Si votre alerte vous avertit prématurément, envisagez de modifier les critères d'alerte pour qu'ils correspondent mieux à votre cas d'utilisation.
- Vous pouvez avoir jusqu'à 10 alertes par espace de travail.
