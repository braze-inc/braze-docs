---
nav_title: "Alertes relatives à l'utilisation de l'API"
article_title: "Alertes d'utilisation de l'API"
description: "Cet article fournit un aperçu des alertes d'utilisation de l'API, qui vous permettent de détecter de manière proactive tout trafic inattendu."
page_order: 3.6
---

# Alertes relatives à l'utilisation de l'API

> Les alertes d'utilisation des API offrent une visibilité essentielle sur l'utilisation de vos API, vous permettant de détecter de manière proactive tout trafic inattendu. En configurant ces alertes pour suivre les volumes de requêtes API clés, vous pouvez recevoir des notifications en temps réel et résoudre les problèmes avant qu'ils n'aient un impact sur vos campagnes marketing.

## À propos des alertes relatives à l'utilisation de l'API

Vous pouvez utiliser les alertes d'utilisation de l'API pour surveiller les volumes de requêtes pour les catégories suivantes :

| Catégorie d'API | Détails |
|--------------|---------|
| Points d'endpoint de l'API REST | Suivi de l'utilisation de tous les appels API REST effectués vers le backend de Braze, tels que l'envoi de messages, la création de campagnes ou l'exportation d'utilisateurs. |
| Demandes d'API SDK | Suivez les requêtes API effectuées à partir des SDK Braze dans les applications clientes, telles que le déclenchement de messages in-app ou la synchronisation des données utilisateur.<br><br>_\*Uniquement disponible pour les clients ayant acheté des utilisateurs actifs par mois – CY 24-25._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Création d'une alerte d'utilisation de l'API

Pour créer une alerte d'utilisation de l'API :

1. Veuillez vous rendre dans **Paramètres** > **API et identifiants** > **Alertes d'utilisation des API**, puis créez une nouvelle alerte.
2. Veuillez saisir un nom pour votre alerte et sélectionner les endpoints REST API et les clés API pour lesquels vous souhaitez être alerté.
3. Veuillez définir vos critères d'alerte en sélectionnant un ou plusieurs codes de réponse et en spécifiant les [seuils d'alerte](#api-usage-alert-thresholds).
4. Une fois que vous avez terminé, basculez **l'option Alerte activée**.
    ![Exemple d'alerte d'utilisation de l'API qui envoie des notifications lorsque l'endpoint « Suivre les utilisateurs » augmente de 100 % en une heure.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts1.png %})

## Seuils d'alerte {#api-usage-alert-thresholds}

Lorsque vous définissez vos critères d'alerte, vous pouvez ajuster les seuils suivants :

<table>
  <thead>
    <tr>
      <th>Champ</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Condition de seuil</td>
      <td>
        Définit les conditions menant au volume seuil pour lequel vous souhaitez être alerté. Les éléments suivants sont pris en charge :<br><br>
        <ul>
          <li><strong>Augmentation</strong> ou <strong>diminution </strong><strong>de</strong> : Compare les demandes par rapport à la période précédente.</li>
          <li><strong>Augmentation en pourcentage</strong> ou <strong>diminution en pourcentage</strong> : Compare le pourcentage de variation des demandes par rapport à la période précédente.</li>
          <li><strong>Supérieur ou égal</strong>, <strong>inférieur ou égal</strong> : Compte les requêtes dans une fenêtre temporelle.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>Volume seuil</td>
      <td>Utilisé en conjonction avec la condition de seuil.</td>
    </tr>
    <tr>
      <td>Période</td>
      <td>La période d'évaluation des alertes.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Configuration des notifications d'alerte

Vous pouvez configurer une alerte par e-mail, webhook ou les deux. Les alertes webhook peuvent s'avérer très utiles dans certains cas, par exemple pour envoyer une alerte à des plateformes externes telles qu'un canal Slack. À titre d'exemple, veuillez consulter notre [documentation](https://www.braze.com/docs/user_guide/administrative/app_settings/company_settings/notification_preferences#slack-incoming-webhook-integration) sur l'intégration des alertes avec Slack pour connaître nos préférences en matière de notifications.

![Un e-mail sera envoyé à l'adresse sélectionnée lorsque les critères de l'alerte seront remplis.]({% image_buster /assets/img/api_usage_alerts/api_usage_alerts2.png %})

### Exemple de charge utile {#payload}

Voici un exemple de charge utile pour le corps d'un webhook d'alerte d'utilisation d'API.

```json
{
  "data": {
    "alert_name": "My First API Usage Alert",
    "alert_type": "API Usage Alert",
    "alert_criteria": {
    	"response_codes": ["201", "202", "203"],
    	"threshold_condition": "Increased by %",
    	"threshold_volume": 50,
    	"within": "1 day"
    },
    "timeframe_start": "2025-03-20T15:35:00Z",
    "timeframe_end": "2025-03-20T16:35:00Z",
    "volume": 1500,
    "previous_timeframe_start": "2025-03-20T14:35:00Z",
    "previous_timeframe_end": "2025-03-20T15:35:00Z",
    "previous_volume": 1000
  },
  "text": "Your My First API Usage Alert alert has triggered. You can view your alert and usage here: <link>. Note that this alert will reset in 1 day, as each alert will only send one notification per 8 hours."
}
```

### Exemples d'alertes

Voici quelques méthodes pour configurer vos alertes d'utilisation de l'API afin d'être averti dans les scénarios suivants.

{% tabs local %}
{% tab api health %}
Vous pouvez configurer des alertes pour surveiller l'état général de votre API. Par exemple, vous pouvez configurer ces alertes lorsque les erreurs API augmentent considérablement, par exemple de 20 % par rapport à l'heure précédente.

| Endpoint | Clé API | Code de réponse | Condition de seuil | Volume seuil | Période |
| --- | --- | --- | --- | --- | --- |
| Tous les endpoints | Toutes les clés API | `4XX` et `5XX` | Augmentation de 10 % | 10 | 1 heure |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab endpoint rate limit %}
Soyez averti lorsque votre espace de travail atteint sa limite de débit pour`/users/track`l'endpoint. Vous pouvez également appliquer cette configuration à d'autres endpoints Braze.

| Endpoint | Clé API | Code de réponse | Condition de seuil | Volume seuil | Période |
| --- | --- | --- | --- | --- | --- |
| `/users/track` | Toutes les clés API | `429` | Supérieur ou égal à | 100 | 1 heure |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab API-triggered campaigns %}
Cette configuration d'alerte vous informe lorsque des erreurs surviennent pour les campagnes et les canevas déclenchés par l'API, dont certaines peuvent être hautement prioritaires.

| Endpoint | Clé API | Code de réponse | Condition de seuil | Volume seuil | Période |
| --- | --- | --- | --- | --- | --- |
| {::nomarkdown}<ul><li><code>/campaigns/trigger/send</code></li><li><code>/canvas/trigger/send</code></li><li><code>/messages/send</code></li></ul>{:/} | Toutes les clés API | `4XX` et `5XX` | Supérieur ou égal à | 1 | 1 heure |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}

{% tab partner integrations %}
Veuillez utiliser la configuration d'alerte suivante pour être averti lorsqu'une intégration de partenaire cesse d'envoyer des données à Braze.

| Endpoint | Clé API | Code de réponse | Condition de seuil | Volume seuil | Période |
| --- | --- | --- | --- | --- | --- |
| Tous les endpoints | La clé API utilisée pour l'intégration de votre partenaire | Tous les codes de réponse | Inférieur ou égal à | 0 | 1 jour |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 .reset-td-br-6 role="presentation" }
{% endtab %}
{% endtabs %}

## Considérations

- Chaque alerte active n'enverra qu'une seule notification par e-mail ou webhook toutes les 8 heures. Ceci vise à éviter un nombre excessif de notifications provenant d'une seule alerte. Si votre alerte vous avertit prématurément, envisagez de modifier les critères d'alerte afin qu'ils correspondent mieux à votre cas d'utilisation.
- Vous pouvez disposer de jusqu'à 10 alertes par espace de travail.
