---
nav_title: Extole
article_title: Extole
description: "Cet article décrit le partenariat entre Braze et Extole, une entreprise de marketing de recommandation, qui vous permet de récupérer des événements et attributs client à partir des programmes de parrainage et de croissance dans Braze"
alias: /partners/extole/
page_type: partner
search_tag: Partner

---

# Extole

> [Extole](https://www.extole.com/), une entreprise SaaS leader de l'industrie du marketing de parrainage permet de créer et d’optimiser des programmes de marketing de recommandation efficaces pour augmenter l'acquisition de clients.

_Cette intégration est maintenue par Extole._

## À propos de l'intégration

Avec l'intégration de Braze et Extole, vous pouvez extraire des événements et attributs client des programmes de parrainage et de croissance d'Extole vers Braze, vous permettant ainsi de créer des campagnes marketing plus personnalisées qui augmentent l'acquisition, l'engagement et la fidélité des clients. Vous pouvez également extraire dynamiquement les attributs de contenu Extole, tels que les liens et codes de partage personnalisés dans les communications Braze.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Extole | Un compte Extole est requis pour profiter de ce partenariat. |
| Clé d'API REST Braze | Une clé API REST Braze avec la permission `users.track`. Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| URL de l'API Braze | Votre URL API Braze est spécifique à votre [instance Braze]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

Les cas d'utilisation suivants montrent quelques façons de tirer parti de l'intégration d'Extole avec Braze. Travaillez avec votre implémentation Extole et vos responsables de la satisfaction client pour développer une option qui répond aux besoins spécifiques de votre entreprise.

- Tirez parti des custom events de vos programmes de recommandation et d'engagement pour déclencher une campagne Braze ou un canvas
- Créez des segments personnalisés, des tableaux de bord et des rapports en utilisant les données de vos programmes alimentés par Extole
- Désabonnez ou abonnez automatiquement les utilisateurs à votre liste de marketing dans Braze

## Intégration

Complétez les étapes suivantes pour que votre intégration soit rapidement opérationnelle. L’équipe de la mise en œuvre d’Extole et les gestionnaires de la satisfaction client vous accompagneront tout au long de ce processus et répondront à toutes vos questions.

### Connectez-vous à votre compte Braze

1. Sélectionnez l'intégration Braze sur la page [Partenaires](https://my.extole.com/partners) de votre compte My Extole.
2. Dans l'intégration Braze, sélectionnez **Installer** pour établir une connexion entre Extole et Braze.
3. Remplissez les champs obligatoires, en commençant par votre clé API REST Braze. 
4. Entrez votre URL d'API Braze. Cette URL dépend de l'instance à laquelle votre compte Braze est provisionné.
5. Ajoutez tous les événements Extole que vous souhaitez envoyer à Braze. Les événements par défaut, les propriétés d'événement et les attributs utilisateur sont décrits dans le [tableau des événements Extole](https://dev.extole.com/docs/braze#extole-program-events).
6. Ajoutez tous les états de récompense que vous souhaitez envoyer à Braze autre que l'état `FULFILLED`. Reportez-vous au [tableau des récompenses Extole](https://dev.extole.com/docs/braze#extole-rewards) pour obtenir des descriptions des états de récompense disponibles.
7. Sélectionnez votre clé de mappage d'ID externe Braze. C'est ainsi qu'Extole met à jour les profils utilisateurs dans Braze. Vous pouvez mapper la clé d’ID externe de Braze à `email_address` ou à `partner_user_id` pour l'utilisateur. Nous recommandons d'utiliser le paramètre`external_id` plutôt que le paramètre `email_address` car il est plus sûr.
8. Enregistrer vos paramètres pour terminer la connexion. Désormais, les événements Extole peuvent être transférés vers votre compte Braze.

### Événements du programme Extole

Vous trouverez ci-dessous les événements par défaut, les propriétés d'événement et les attributs utilisateur qu'Extole enverra à Braze. Contactez l’équipe de la mise en œuvre d'Extole ou de la satisfaction client pour identifier et ajouter d’autres événements Extole à votre intégration.

| Événement | Description | propriétés d'événement | Attributs de l'utilisateur |
| ----------- | ----------- | ----------- | ----------- |
| `extole_created_share_link` | Un participant crée son lien de partage en entrant son e-mail dans l'Expérience de partage Extole. | Nom de l'événement  <br>Heure de l'événement  <br>partenaire (Extole)  <br>Entonnoir (référent ou ami)  <br>Programme | <br>ID externe <br>e-mail  <br>Partager le lien |
| `extole_shared` | Un participant partage son lien de recommandation avec un ami. | Nom de l'événement  <br>Heure de l'événement  <br>partenaire (Extole)  <br>ID externe  <br>Entonnoir (référent ou ami)  <br>Programme  <br>Partager la chaîne | e-mail <br>Prénom <br>Nom de famille |
| `outcome` - Le résultat est dynamique en fonction de la configuration de votre programme (comme `extole_shipped`, `extole_converted`)| Un participant a converti ou complété l'événement de résultat souhaité configuré pour le programme. | Dynamique par programme | e-mail <br>Prénom <br>Nom de famille |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### États d'abonnement Extole

| État de l'abonnement | Description | propriétés d'événement | Attributs de l'utilisateur |
| ----------- | ----------- | ----------- | ----------- |
| `subscribed` | Un participant a choisi de recevoir des messages marketing. | N/A | e-mail  <br>Type de liste  <br>ID externe  <br>Abonné aux e-mails |
| `unsubscribed` | Un participant a choisi de ne plus recevoir de communications par e-mail d'Extole.| e-mail  <br>ID externe  <br>État de l'abonnement (désabonné)  <br>ID de groupe d'abonnement  | Type de liste |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Récompenses Extole

Par défaut, Extole enverra des événements de récompense dans l'état `FULFILLED` à Braze afin que vous puissiez déclencher des notifications de récompense via une campagne Braze ou Canvas. Reportez-vous au tableau suivant pour les états de récompense supplémentaires.

| État de récompense | Description | propriétés d'événement | Attributs de l'utilisateur |
| ----------- | ----------- | ----------- | ----------- |
| `FULFILLED` | L'état par défaut. Une valeur a été attribuée à la récompense (comme un bon de réduction ou une carte-cadeau) par un fournisseur de récompenses Extole. | e-mail <br>Valeur nominale  <br>Code de coupon  <br>Type de valeur nominale  | e-mail <br>Prénom  <br>Nom de famille |
| `EARNED` | Une récompense a été créée et associée à une personne. | e-mail <br>Valeur nominale  <br>Code de coupon  <br>Type de valeur nominale  | e-mail <br>Prénom  <br>Nom de famille |
| `SENT` | La récompense a été remplie et a été envoyée au destinataire par e-mail ou directement à un appareil. | e-mail <br>Valeur nominale  <br>Code de coupon  <br>Type de valeur nominale  | e-mail <br>Prénom  <br>Nom de famille |
| `REDEEMED` | La récompense a été utilisée par le destinataire, comme en témoigne un événement de conversion ou de rachat envoyé à Extole.| e-mail <br>Valeur nominale  <br>Code de coupon  <br>Type de valeur nominale  | e-mail <br>Prénom  <br>Nom de famille |
| `FAILED` | Un problème a empêché la récompense d'être émise ou envoyée, nécessitant une attention. | e-mail <br>Valeur nominale  <br>Code de coupon  <br>Type de valeur nominale  | e-mail <br>Prénom  <br>Nom de famille |
| `CANCELED` | La récompense a été désactivée et retournera dans l'inventaire. | e-mail <br>Valeur nominale  <br>Type de valeur nominale  | e-mail <br>Prénom  <br>Nom de famille |
| `REVOKED` | La récompense remplie a été invalidée. Par exemple, Extole a demandé une carte-cadeau fournisseur, puis a déterminé que la carte avait été envoyée par erreur. Si le fournisseur prend en charge la révocation de la récompense, Extole demandera le remboursement des fonds, et la récompense ne sera plus valide. | e-mail <br>Valeur nominale   <br>Type de valeur nominale  | e-mail <br>Prénom  <br>Nom de famille |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }


## Personnalisation

### Rechercher et créer des utilisateurs dans Braze

Pour certains cas d'utilisation, tels qu'un nouvel e-mail ou abonnement SMS où Extole n'a pas d'ID externe (ID d’utilisateur), Extole peut vérifier l'identifiant de l'utilisateur à l’aide de l’[endpoint Exporter le profil utilisateur par l’identifiant de Braze]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/). Extole ajoutera et mettra à jour tous les attributs de profil si l'utilisateur existe dans Braze. Si la requête ne renvoie pas de profil utilisateur, Extole utilisera l'endpoint `/users/track` pour créer un alias d'utilisateur avec l'adresse e-mail de l'utilisateur comme nom d'alias.

## Grâce à cette intégration

Après avoir connecté vos comptes, les événements commenceront automatiquement à circuler d'Extole à Braze sans aucune action de votre part. Une vue en temps réel des événements envoyés à Braze est disponible dans le Centre des webhooks sortants d'Extole pour la résolution des problèmes. 

