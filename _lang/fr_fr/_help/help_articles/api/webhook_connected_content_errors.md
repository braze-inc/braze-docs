---
nav_title: Résolution des problèmes liés aux demandes de webhook et de contenu connecté
article_title: Résolution des problèmes liés aux demandes de webhook et de contenu connecté
page_order: 3
channel:
  - webhooks
description: "Cet article explique comment résoudre les codes d'erreur de webhook et de contenu connecté, notamment la nature des erreurs et les étapes pour les résoudre."
---

# Résolution des problèmes liés aux demandes de webhook et de contenu connecté

> Cet article explique comment dépanner les codes d'erreur courants pour les webhooks et le contenu connecté, et fournit des explications supplémentaires sur la façon dont ces erreurs peuvent se produire dans vos demandes.

## Erreurs 4XX

`4XX` indiquent qu'il y a un problème avec la requête envoyée à l'endpoint. Ces erreurs sont généralement causées par des demandes erronées, notamment des paramètres mal formés, des en-têtes d'authentification manquants ou des URL incorrectes.

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
      <td>La demande nécessite l'authentification de l'utilisateur.</td>
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
| **599 Erreur de connexion**      | Braze a rencontré une erreur de délai de connexion au réseau en essayant d'établir une connexion à l'endpoint, ce qui signifie que l'endpoint peut être instable ou en panne. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Résolution des erreurs 5XX

Voici des conseils pour la résolution des problèmes les plus courants sur le site `5XX`:

- Consultez le message d'erreur pour obtenir des détails spécifiques disponibles dans le **journal d'activité des messages.** Pour les webhooks, rendez-vous dans la section **Performance au fil du temps** sur la page d'accueil de Braze et sélectionnez les statistiques pour les webhooks. À partir de là, vous pouvez trouver l'horodatage qui indique quand les erreurs se sont produites.
- Assurez-vous que vous n'envoyez pas trop de demandes qui surchargent l'endpoint. Vous pouvez envoyer par lots ou ajuster la limite de débit pour vérifier si cela réduit les erreurs.
