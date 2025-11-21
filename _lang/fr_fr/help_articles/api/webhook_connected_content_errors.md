---
nav_title: Résolution des problèmes liés aux demandes de webhook et de contenu connecté
article_title: Résolution des problèmes liés aux demandes de webhook et de contenu connecté
page_order: 3
channel:
  - webhooks
description: "Cet article explique comment résoudre les codes d'erreur de webhook et de contenu connecté, notamment la nature des erreurs et les étapes à suivre pour les résoudre."
---

# Résolution des problèmes liés aux demandes de webhook et de contenu connecté

> Cet article explique comment dépanner les codes d'erreur courants pour les webhooks et le contenu connecté, et fournit des explications supplémentaires sur la façon dont ces erreurs peuvent se produire dans vos demandes.

## Erreurs 4XX

`4XX` indiquent qu'il y a un problème avec la requête envoyée à l'endpoint. Ces erreurs sont généralement causées par des requêtes erronées, notamment des paramètres mal formés, des en-têtes d'authentification manquants ou des URL incorrectes.

Reportez-vous au tableau suivant pour connaître les détails du code d'erreur et les étapes de résolution :

<style>
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>code d'erreur</th>
      <th>Ce que cela signifie</th>
      <th>Marche à suivre pour résoudre le problème</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>400 Demande erronée</b></td>
      <td>La syntaxe de la demande n'est pas correcte.</td>
      <td>
        <ul>
          <li>Vérifiez que les données utiles de la demande ne comportent pas d'erreurs de syntaxe.</li>
          <li>Confirmez que tous les champs obligatoires sont inclus et correctement formatés.</li>
          <li>Si vous envoyez une charge utile JSON, validez la structure JSON.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>401 Non autorisé</b></td>
      <td>La demande requiert l'authentification de l'utilisateur.</td>
      <td>
        <ul>
          <li>Vérifiez que les informations d'authentification correctes (telles que les clés ou jetons API) sont incluses dans les en-têtes de la demande.</li>
          <li>Confirmez que vous disposez des autorisations d'utilisateur pour accéder à l'endpoint.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>403 Interdit</b></td>
      <td>L'endpoint comprend la demande mais refuse de l'autoriser.</td>
      <td>
        <ul>
          <li>Vérifiez si la clé ou le jeton API dispose des autorisations requises.</li>
          <li>Confirmez que vous disposez des autorisations d'utilisateur pour accéder à l'endpoint.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>404 Page introuvable</b></td>
      <td>L'endpoint ne trouve pas la ressource demandée.</td>
      <td>
        <ul>
          <li>Vérifiez que l'URL de l'endpoint ne contient pas de fautes de frappe ou de chemins d'accès incorrects.</li>
          <li>Confirmez que la ressource à laquelle vous essayez d'accéder existe.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>405 Méthode non autorisée</b></td>
      <td>La méthode de demande est connue par l'endpoint mais n'est pas prise en charge par la ressource cible.</td>
      <td>
        <ul>
          <li>Vérifiez la méthode HTTP (DELETE, GET, POST, PUT) utilisée dans la requête.</li>
          <li>Confirmez que l'endpoint prend en charge la méthode que vous utilisez.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>408 Délai de requête</b></td>
      <td>L'endpoint a dépassé le délai de traitement de la demande.</td>
      <td>
        <ul>
          <li>Vérifiez la méthode HTTP (DELETE, GET, POST, PUT) utilisée dans la requête.</li>
          <li>Confirmez que l'endpoint prend en charge la méthode que vous utilisez.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>409 Conflit</b></td>
      <td>La demande est incomplète en raison d'un conflit avec l'état actuel de la ressource.</td>
      <td>
        <ul>
          <li>Vérifiez la méthode HTTP (DELETE, GET, POST, PUT) utilisée dans la requête.</li>
          <li>Confirmez que l'endpoint prend en charge la méthode que vous utilisez.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>429 Trop de demandes</b></td>
      <td>Il y a trop de demandes envoyées dans un laps de temps donné.</td>
      <td>
        <ul>
          <li>Diminuez la limite de débit de votre campagne ou de votre étape du canvas.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## Erreurs 5XX

`5XX` indiquent qu'il y a un problème avec l'endpoint. Ces erreurs sont généralement dues à des problèmes au niveau du serveur.

| code d'erreur                    | Ce que cela signifie                                                                                                                                         |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **500 Erreur interne du serveur** | L'endpoint a rencontré une condition inattendue qui l'a empêché de terminer la demande.                                                       |
| **502 Mauvaise passerelle**           | L'endpoint a reçu une réponse non valide du serveur en amont.                                                                                   |
| **503 Service indisponible**   | L'endpoint est actuellement incapable de traiter la demande en raison d'une surcharge temporaire ou d'une maintenance.                                                    |
| **504 Délai d'attente de la passerelle**       | L'endpoint n'a pas reçu de réponse en temps voulu de la part du serveur en amont.                                                                               |
| **529 Hôte surchargé**       | L'hôte de l'endpoint est surchargé et n'a pas pu répondre. |
| **598 Hôte en mauvaise santé**        | Braze a simulé la réponse parce que l'hôte de l'endpoint est temporairement marqué comme malsain. Pour en savoir plus, consultez la section [Détection d'un hôte malsain](#unhealthy-host-detection). |
| **599 Erreur de connexion**      | Braze a rencontré une erreur de délai de connexion au réseau en essayant d'établir une connexion à l'endpoint, ce qui signifie que l'endpoint peut être instable ou en panne. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Résolution des erreurs 5XX

Vous trouverez ci-dessous des conseils pour la résolution des problèmes les plus courants sur le site `5XX`:

- Consultez le message d'erreur pour obtenir des détails spécifiques disponibles dans le **journal d'activité des messages.** Pour les webhooks, rendez-vous dans la section **Performance au fil du temps** sur la page d'accueil de Braze et sélectionnez les statistiques pour les webhooks. À partir de là, vous pouvez trouver l'horodatage qui indique quand les erreurs se sont produites.
- Assurez-vous que vous n'envoyez pas trop de demandes qui surchargent l'endpoint. Vous pouvez envoyer par lots ou ajuster la limite de débit pour vérifier si cela réduit les erreurs.

## Détection d'un hôte malsain

Les webhooks et le contenu connecté de Braze utilisent un mécanisme de détection d'hôte malsain pour détecter lorsque l'hôte cible connaît un taux élevé de lenteur significative ou de surcharge entraînant des dépassements de délai, un trop grand nombre de demandes ou d'autres résultats qui empêchent Braze de communiquer avec succès avec l'endpoint cible. Il agit comme un garde-fou pour réduire la charge inutile qui pourrait être à l'origine des difficultés de l'hôte cible. Il sert également à stabiliser l'infrastructure de Braze et à maintenir des vitesses d'envoi de messages rapides.

Les seuils de détection diffèrent entre les webhooks et le contenu connecté :
- **Pour les webhooks**: Si le nombre d'**échecs dépasse 3 000 dans une fenêtre de temps mobile d'une minute** (par combinaison unique de nom d'hôte et de groupe d'applications, et **non** par chemin d'accès à l'endpoint), Braze interrompt temporairement les requêtes vers l'hôte cible pendant une minute.
- **Pour le contenu connecté**: Si le nombre d'**échecs dépasse 3 000 ET que le taux d'erreur dépasse 90 % dans une fenêtre de temps mobile d'une minute** (par combinaison unique de nom d'hôte et de groupe d'applications - et **non** par chemin d'accès à l'endpoint), Braze interrompt temporairement les requêtes vers l'hôte cible pendant une minute.

Lorsque les requêtes sont interrompues, Braze simule des réponses avec un code d'erreur `598` pour indiquer le mauvais état de santé. Au bout d'une minute, Braze reprend les requêtes à pleine vitesse si l'hôte est jugé sain. Si l'hôte est toujours en mauvaise santé, Braze attendra encore une minute avant de réessayer.

Les codes d'erreur suivants contribuent au nombre d'échecs du détecteur d'hôte malsain : `408`, `429`, `502`, `503`, `504`, `529`.

Pour les webhooks, Braze relance automatiquement les requêtes HTTP qui ont été interrompues par le détecteur d'hôte malsain. Cette relance automatique utilise des délais exponentiels et n'effectuera que quelques tentatives avant d'échouer. Pour plus d'informations sur les erreurs de webhook, reportez-vous à la section [Erreurs, logique de réessai et délais d'attente.]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook#errors-retry-logic-and-timeouts)

Pour le contenu connecté, si les requêtes vers l'hôte cible sont interrompues par le détecteur d'hôte malsain, Braze continuera à rendre les messages et à suivre votre logique Liquid comme s'il avait reçu un code de réponse d'erreur. Si vous voulez vous assurer que ces demandes de contenu connecté sont relancées lorsqu'elles sont interrompues par le détecteur d'hôte malsain, utilisez l'option `:retry`. Pour plus d'informations sur l'option `:retry`, reportez-vous à la section [Tentatives de contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries).

Si vous pensez que la détection des hôtes malsains peut être à l'origine de problèmes, contactez l'[assistance de Braze]({{site.baseurl}}/support_contact/).

## E-mails automatisés et entrées dans le journal d'activité des messages

### Mise en place d'e-mails automatisés

Si vous rencontrez plus de 100 000 erreurs de webhook ou d'endpoint de contenu connecté (y compris les tentatives) dans un espace de travail au cours d'une période de 24 heures, vous recevrez un e-mail contenant les informations suivantes sur la manière de résoudre les erreurs. 

- Nom de l'espace de travail
- Un lien vers le canvas ou la campagne
- URL de l'endpoint
- code d'erreur
- Heure à laquelle l'erreur a été observée pour la dernière fois
- Liens vers le journal d'activité des messages et la documentation connexe

{% alert note %}
Vous pouvez configurer le seuil d'erreur par espace de travail. Pour ajuster ce seuil, contactez le [service d'assistance de Braze]({{site.baseurl}}/support_contact/).
{% endalert %}

Les erreurs d'endpoint sont les suivantes :

- **`4XX`:** `400`, `401`, `403`, `404`, `405`, `408`, `409`, `429`
- **`5XX`:** `500`, `502`, `503`, `504`, `598`, `599`

Ces e-mails ne sont envoyés qu'une fois par jour au niveau de l'espace de travail. Si aucun utilisateur ne s'inscrit pour recevoir ces e-mails, tous les administrateurs de l'entreprise en seront informés.

Pour vous inscrire à la réception de ces e-mails, procédez comme suit :

1. Allez dans **Réglages** > **Réglages administratifs** > **Préférences de notification.**
2. Sélectionnez les **erreurs de contenu connecté** et les **erreurs de webhook** dans la **section Canvas et campagnes.**

### Entrées du journal d'activité des messages

Il y aura au moins une entrée dans le [journal d'activité des messages]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab) liée à l'erreur qui a déclenché l'e-mail automatisé.

### Informations supplémentaires sur les défaillances dans Braze Currents

Pour améliorer la transparence des problèmes liés aux webhooks, Braze transmet les événements détaillés de défaillance des webhooks à Currents et à Snowflake Data Sharing. Ces événements comprennent les demandes de webhook qui ont échoué (telles que les réponses HTTP `4xx` ou `5xx` ), ce qui permet de mieux observer la manière dont les problèmes de webhook peuvent influer sur la réception/distribution des messages. Notez que les événements d'échec comprennent les erreurs de terminal ainsi que les erreurs qui sont retentées.

{% alert note %}
Les demandes de contenu connecté ne sont pas incluses dans ces événements d'échec du webhook.
{% endalert %}

Pour plus d'informations, consultez le [glossaire des événements d'engagement aux messages.]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/)
