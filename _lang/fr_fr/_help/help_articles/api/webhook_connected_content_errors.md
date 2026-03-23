---
nav_title: Résolution des problèmes liés aux demandes de webhook et de contenu connecté
article_title: Résolution des problèmes liés aux demandes de webhook et de contenu connecté
page_order: 3
channel:
  - webhooks
description: "Cet article explique comment résoudre les codes d'erreur de webhook et de contenu connecté, notamment la nature des erreurs et les étapes à suivre pour les résoudre."
---

# Résolution des problèmes liés aux demandes de webhook et de contenu connecté

> Cet article explique comment résoudre les codes d'erreur courants pour les webhooks et le contenu connecté, et fournit des explications supplémentaires sur la façon dont ces erreurs peuvent survenir dans vos requêtes.

## Erreurs 4XX

Les erreurs `4XX` indiquent un problème avec la requête envoyée à l'endpoint. Elles sont généralement causées par des requêtes erronées, notamment des paramètres mal formés, des en-têtes d'authentification manquants ou des URL incorrectes. Ces erreurs s'appliquent également au [générateur de rapports]({{site.baseurl}}/user_guide/analytics/reporting/report_builder).

Consultez le tableau suivant pour connaître les détails de chaque code d'erreur et les étapes de résolution :

<style>
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>Code d'erreur</th>
      <th>Signification</th>
      <th>Marche à suivre</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>400 Bad Request</b></td>
      <td>La syntaxe de la requête est invalide.</td>
      <td>
        <ul>
          <li>Vérifiez que le payload de la requête ne comporte pas d'erreurs de syntaxe.</li>
          <li>Confirmez que tous les champs obligatoires sont inclus et correctement formatés.</li>
          <li>Si vous envoyez un payload JSON, validez la structure JSON.</li>
          <li>Si vous utilisez Liquid pour intégrer des balises de personnalisation dans la requête webhook, vérifiez que le Liquid ne produit pas une valeur vide ou des caractères qui cassent le JSON (comme des guillemets non échappés). Prévisualisez le message pour un utilisateur test afin de confirmer que le rendu est valide.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>401 Unauthorized</b></td>
      <td>La requête nécessite une authentification de l'utilisateur.</td>
      <td>
        <ul>
          <li>Vérifiez que les informations d'authentification correctes (telles que les clés API ou les jetons) sont incluses dans les en-têtes de la requête.</li>
          <li>Confirmez que vous disposez des autorisations nécessaires pour accéder à l'endpoint.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>403 Forbidden</b></td>
      <td>L'endpoint comprend la requête mais refuse de l'autoriser.</td>
      <td>
        <ul>
          <li>Vérifiez si la clé API ou le jeton dispose des autorisations requises.</li>
          <li>Confirmez que vous disposez des autorisations nécessaires pour accéder à l'endpoint.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>404 Not Found</b></td>
      <td>L'endpoint ne trouve pas la ressource demandée.</td>
      <td>
        <ul>
          <li>Vérifiez que l'URL de l'endpoint ne contient pas de fautes de frappe ou de chemins d'accès incorrects.</li>
          <li>Confirmez que la ressource à laquelle vous essayez d'accéder existe.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>405 Method Not Allowed</b></td>
      <td>La méthode de requête est connue par l'endpoint mais n'est pas prise en charge par la ressource cible.</td>
      <td>
        <ul>
          <li>Vérifiez la méthode HTTP (DELETE, GET, POST, PUT) utilisée dans la requête.</li>
          <li>Confirmez que l'endpoint prend en charge la méthode que vous utilisez.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>408 Request Timeout</b></td>
      <td>L'endpoint a dépassé le délai de traitement de la requête.</td>
      <td>
        <ul>
          <li>Vérifiez la méthode HTTP (DELETE, GET, POST, PUT) utilisée dans la requête.</li>
          <li>Confirmez que l'endpoint prend en charge la méthode que vous utilisez.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>409 Conflict</b></td>
      <td>La requête est incomplète en raison d'un conflit avec l'état actuel de la ressource.</td>
      <td>
        <ul>
          <li>Vérifiez la méthode HTTP (DELETE, GET, POST, PUT) utilisée dans la requête.</li>
          <li>Confirmez que l'endpoint prend en charge la méthode que vous utilisez.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>429 Too Many Requests</b></td>
      <td>Trop de requêtes ont été envoyées dans un laps de temps donné.</td>
      <td>
        <ul>
          <li>Diminuez la limite de débit de votre campagne ou de votre étape du canvas.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## Erreurs 5XX

Les erreurs `5XX` indiquent un problème au niveau de l'endpoint. Elles sont généralement dues à des problèmes côté serveur.

| Code d'erreur                    | Signification                                                                                                                                         |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **500 Internal Server Error** | L'endpoint a rencontré une condition inattendue qui l'a empêché de traiter la requête.                                                       |
| **502 Bad Gateway**           | L'endpoint a reçu une réponse non valide du serveur en amont.                                                                                   |
| **503 Service Unavailable**   | L'endpoint est temporairement incapable de traiter la requête en raison d'une surcharge ou d'une maintenance.                                                    |
| **504 Gateway Timeout**       | L'endpoint n'a pas reçu de réponse en temps voulu de la part du serveur en amont.                                                                               |
| **529 Host Overloaded**       | L'hôte de l'endpoint est surchargé et n'a pas pu répondre. |
| **598 Host Unhealthy**        | Braze a simulé la réponse parce que l'hôte de l'endpoint est temporairement marqué comme défaillant. Pour en savoir plus, consultez la section [Détection d'un hôte défaillant](#unhealthy-host-detection). |
| **599 Connection Error**      | Braze a rencontré une erreur de délai de connexion réseau en essayant d'établir une connexion à l'endpoint, ce qui signifie que l'endpoint peut être instable ou hors service. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Résolution des erreurs 5XX

Voici quelques conseils pour résoudre les erreurs `5XX` les plus courantes :

- Consultez le message d'erreur pour obtenir des détails spécifiques dans le **journal d'activité des messages**. Pour les webhooks, rendez-vous dans la section **Performance au fil du temps** sur la page d'accueil de Braze et sélectionnez les statistiques des webhooks. Vous pourrez y trouver l'horodatage indiquant quand les erreurs se sont produites.
- Assurez-vous de ne pas envoyer trop de requêtes qui surchargent l'endpoint. Vous pouvez envoyer par lots ou ajuster la limite de débit pour vérifier si cela réduit les erreurs.

## Détection d'un hôte défaillant

Les webhooks et le contenu connecté de Braze utilisent un mécanisme de détection d'hôte défaillant pour identifier les situations où l'hôte cible connaît un taux élevé de lenteur significative ou de surcharge entraînant des dépassements de délai, un trop grand nombre de requêtes ou d'autres problèmes empêchant Braze de communiquer correctement avec l'endpoint cible. Ce mécanisme agit comme un garde-fou pour réduire la charge inutile qui pourrait être à l'origine des difficultés de l'hôte cible. Il sert également à stabiliser l'infrastructure de Braze et à maintenir des vitesses d'envoi de messages rapides.

Les seuils de détection diffèrent entre les webhooks et le contenu connecté :
- **Pour les webhooks** : Si le nombre d'**échecs dépasse 3 000 dans une fenêtre de temps glissante d'une minute** (par combinaison unique de nom d'hôte et de groupe d'applications&#8212;et **non** par chemin d'accès à l'endpoint), Braze interrompt temporairement les requêtes vers l'hôte cible pendant une minute.
- **Pour le contenu connecté** : Si le nombre d'**échecs dépasse 3 000 ET que le taux d'erreur dépasse 90 % dans une fenêtre de temps glissante d'une minute** (par combinaison unique de nom d'hôte et de groupe d'applications&#8212;et **non** par chemin d'accès à l'endpoint), Braze interrompt temporairement les requêtes vers l'hôte cible pendant une minute.

Lorsque les requêtes sont interrompues, Braze simule des réponses avec un code d'erreur `598` pour signaler le mauvais état de santé de l'hôte. Au bout d'une minute, Braze reprend les requêtes à pleine vitesse si l'hôte est jugé sain. Si l'hôte est toujours défaillant, Braze attend une minute supplémentaire avant de réessayer.

Les codes d'erreur suivants contribuent au compteur d'échecs du détecteur d'hôte défaillant : `408`, `429`, `502`, `503`, `504`, `529`.

Pour les webhooks, Braze relance automatiquement les requêtes HTTP qui ont été interrompues par le détecteur d'hôte défaillant. Cette relance automatique utilise des délais exponentiels et n'effectue que quelques tentatives avant d'échouer définitivement. Pour plus d'informations sur les erreurs de webhook, consultez la section [Erreurs, logique de réessai et délais d'attente]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook#errors-retry-logic-and-timeouts).

Pour le contenu connecté, si les requêtes vers l'hôte cible sont interrompues par le détecteur d'hôte défaillant, Braze continue de rendre les messages et de suivre votre logique Liquid comme s'il avait reçu un code de réponse d'erreur. Si vous souhaitez que ces requêtes de contenu connecté soient relancées lorsqu'elles sont interrompues par le détecteur d'hôte défaillant, utilisez l'option `:retry`. Pour plus d'informations sur l'option `:retry`, consultez la section [Nouvelles tentatives de contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries).

Si vous pensez que la détection d'hôte défaillant est à l'origine de problèmes, contactez l'[assistance Braze]({{site.baseurl}}/support_contact/).

## E-mails automatisés et entrées dans le journal d'activité des messages

### Mise en place des e-mails automatisés

Si vous rencontrez plus de 100 000 erreurs d'endpoint de webhook ou de contenu connecté (tentatives incluses) dans un espace de travail sur une période de 24 heures, vous recevrez un e-mail contenant les informations suivantes pour vous aider à résoudre les erreurs :

- Nom de l'espace de travail
- Un lien vers le canvas ou la campagne
- URL de l'endpoint
- Code d'erreur
- Heure de la dernière occurrence de l'erreur
- Liens vers le journal d'activité des messages et la documentation associée

{% alert note %}
Vous pouvez configurer le seuil d'erreur par espace de travail. Pour ajuster ce seuil, contactez l'[assistance Braze]({{site.baseurl}}/support_contact/).
{% endalert %}

Les erreurs d'endpoint concernées sont les suivantes :

- **`4XX` :** `400`, `401`, `403`, `404`, `405`, `408`, `409`, `429`
- **`5XX` :** `500`, `502`, `503`, `504`, `598`, `599`

Ces e-mails ne sont envoyés qu'une fois par jour au niveau de l'espace de travail. Si aucun utilisateur ne s'est inscrit pour recevoir ces e-mails, tous les administrateurs de la société en seront informés.

Pour vous inscrire à la réception de ces e-mails, procédez comme suit :

1. Allez dans **Paramètres** > **Paramètres d'administration** > **Préférences de notification**.
2. Sélectionnez **Erreurs de contenu connecté** et **Erreurs de webhook** dans la section **Canvas et Campagnes**.

### Entrées du journal d'activité des messages

En cas d'échec, il y aura au moins une entrée dans le [journal d'activité des messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab) liée à cet échec. Si la requête est relancée et finit par aboutir, ces détails seront disponibles dans Currents et Snowflake Data Share. Notez que même si une requête finit par aboutir après une relance, les erreurs peuvent tout de même déclencher l'e-mail automatisé.

### Informations supplémentaires sur les échecs dans Braze Currents

Pour améliorer la transparence sur les problèmes liés aux webhooks, Braze transmet les événements détaillés d'échec des webhooks à Currents et à Snowflake Data Sharing. Ces événements incluent les requêtes de webhook ayant échoué (telles que les réponses HTTP `4xx` ou `5xx`), offrant ainsi une meilleure visibilité sur l'impact des problèmes de webhook sur la distribution des messages. Les événements d'échec comprennent aussi bien les erreurs terminales que les erreurs en cours de relance.

{% alert note %}
Les requêtes de contenu connecté ne sont pas incluses dans ces événements d'échec de webhook.
{% endalert %}

Pour plus d'informations, consultez le [glossaire des événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).