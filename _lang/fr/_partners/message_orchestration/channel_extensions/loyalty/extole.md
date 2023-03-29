---
nav_title: Extole
article_title: Extole
description: "Cet article de référence présente le partenariat entre Braze et Extole, une société de marketing de recommandation qui vous permet d’extraire des événements et attributs clients de programmes de parrainage et de croissance dans Braze"
alias: /partners/extole/
page_type: partner
search_tag: Partenaire

---

# Extole

> [Extole][1], une société Saas, est un leader du secteur du marketing de recommandation, aidant à créer et à optimiser des programmes de marketing de recommandation efficaces pour augmenter l’acquisition des clients.

Avec l’intégration entre Braze et Extole, vous pouvez transférer dans Braze les événements et attributs client provenant des programmes Extole de parrainage et de croissance, ce qui vous permet de créer des campagnes de marketing plus personnalisées qui stimulent l’acquisition, l’engagement et la fidélité des clients. Vous pouvez également extraire dynamiquement des attributs de contenu Extole, tels que des codes de partage et des liens personnalisés, dans les communications de Braze.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Extole | Un compte Extole est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Clé API REST test de Braze (facultatif) | Une clé d’API qui peut être utilisée à des fins de test si vous souhaitez que ces demandes soient envoyées à une instance test de Braze séparée. |
| Instance de Braze | Votre instance Braze peut être obtenue auprès de votre gestionnaire d’onboarding Braze ou est disponible sur la [page API overview]({{site.baseurl}}/api/basics/#endpoints). |
| Identité de l’utilisateur | Identifiant unique d’un utilisateur dans Braze et Extole. C’est généralement l’`external_id`. |
{: .reset-td-br-1 .reset-td-br-2}

## Cas d’utilisation

Les exemples d’utilisation suivants présentent quelques façons de tirer parti de l’intégration d’Extole à Braze. Travaillez avec vos gestionnaires Extole de la mise en œuvre et de la réussite des clients pour développer une option qui répond aux besoins spécifiques de votre entreprise.
- Transformez chaque client en un partisan en y incluant son lien de partage unique dans les communications de Braze.
- Poursuivez la conversation avec les visiteurs du site en déclenchant une campagne de bienvenue personnalisée lorsqu’ils s’abonnent pour recevoir des communications marketing dans les programmes optimisés par Extole.
- Favorisez un engagement supplémentaire en déclenchant une campagne de recommandations produit lorsqu’un partisan partage un produit spécifique avec un ami.
- Remerciez les partisans de vous apporter de nouveaux clients de qualité en déclenchant une campagne de « surprise et de ravissement » lorsqu’ils sont à l’origine de cinq recommandations ou plus.
- Déclenchez une campagne de parrainage par e-mail, notification push ou SMS à n’importe quel moment de la journée où le client est ravi, comme un achat ou une expérience positive avec votre marque.

## Intégration

Effectuez les étapes suivantes pour que votre intégration soit rapidement opérationnelle. Vos gestionnaires de l’implémentation et du succès client d’Extole vous soutiendront tout au long de ce processus.

### Étape 1 : Définir les noms et les attributs des événements 

Tout événement suivi par Extole peut être envoyé à Braze. Travaillez avec votre gestionnaire de l’implémentation ou de la réussite client Extole pour identifier les noms d’événements et les attributs utilisateur que vous souhaitez envoyer dans Braze ou sélectionnez parmi les options par défaut dans les tableaux ci-dessous. Votre gestionnaire de la mise en œuvre ou de la réussite des clients Extole mappera et configurera ensuite les noms des événements dans le tableau de bord d’Extole.

#### Noms des événements

| Nom de l’événement | Description |
| ----------- | ----------- |
| Lien de partage créé | Un lien de partage est créé pour un client. |
| Partagé | Un client envoie un lien à son ou ses amis par e-mail, SMS ou canal social. |
| Parrainé inscrit | Un client parrainé s’inscrit par e-mail ou par SMS dans le cadre du programme. |
| Parrainé converti | Un client parrainé effectue un achat. Notez que les événements liés aux résultats peuvent être personnalisés pour votre entreprise.|
| Abonné | Un client s’abonne par e-mail ou SMS. |
| Non inscrit | Un client se désabonne par e-mail ou SMS. |
| Récompense gagnée | Un client gagne une récompense. |
{: .reset-td-br-1 .reset-td-br-2}

#### Noms des attributs

| Nom de l’attribut | Description | Exemple | 
| -------------- | ----- | ------- |
| `external_id` (obligatoire) | L’identifiant unique du client, tel qu’un ID utilisateur. | ID utilisateur |
| `email` | L’adresse e-mail du client. | jsmith@votreentreprise.com |
| `phone_number` | Le numéro de téléphone du client, y compris l’indicatif du pays. | +15555555555 |
| `share_link` | Le lien de partage personnel du client. | refer.yourcompany.com/jsmith |
| `first_name` | Le prénom du client. | John |
| `last_name` | Le nom du client. | Smith |
| `city` | La ville du client, en toutes lettres. | Boston |
| `state` | L’état du client, en abrégé. | MA |
| `country` | Le pays du client, en abrégé. | US |
| `funnel` | Le bon type d’entonnoir pour le client. | ami ou partisan |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Étape 2 : Connexion à votre compte Braze 

Pour commencer à envoyer les données de vos programmes Extole vers Braze, créez une nouvelle intégration de webhook dans le centre de webhooks sortants d’Extole.


1. Accédez à **Tech Center > Outbound Webhooks (Centre tech > Wehooks sortants)** dans votre compte My Extole et cliquez sur le bouton **+ New Integration (+ Nouvelle intégration)**.
2. Entrez un nom de clé (c'est-à-dire la façon dont vous souhaitez faire référence à la clé dans Extole) et sélectionnez **Webhook** comme type de clé. 
3. Dans le champ ID de clé de partenaire, ajoutez une valeur que vous reconnaîtrez pour cet identifiant (par exemple, votre ID de compte, votre adresse e-mail ou votre ID utilisateur).
4. Sélectionnez `PASSWORD` dans le menu déroulant de l'algorithme.
5. Ajoutez votre clé API REST Braze au champ clé et cliquez sur **Create Key (Créer une clé)**.<br><br>![][4]{: style="max-width:80%;"}

Ensuite, travaillez avec votre gestionnaire du succès ou de la mise en œuvre d’Extole pour créer un nouveau webhook. Ils configureront le webhook pour vous en utilisant votre clé nouvellement générée et l’URL de votre instance Braze.<br><br>![][5]{: style="max-width:80%;"}

## Personnalisation

### Configurer une clé d’API pour les tests

Si vous ne fournissez qu’une seule clé d’API REST Braze à Extole, seuls les événements de production seront envoyés à Braze. Si vous souhaitez également envoyer des événements de mise à disposition ou de test, créez une autre clé d’API REST Braze et configurez une intégration webhook supplémentaire dans le tableau de bord d’Extole.

### Création d’un nouvel alias d’utilisateur

Pour certains cas d’utilisation, tels qu’un nouvel abonnement par e-mail ou SMS pour lequel Extole ne dispose pas d’un ID externe (ID utilisateur), Extole peut vérifier l’identifiant utilisateur en utilisant [l’endpoint d’exportation utilisateur par identifiant ][2] de Braze. Si l’utilisateur existe dans Braze, Extole ajoutera et mettra à jour tous les attributs du profil. Si la demande ne renvoie pas de profil d’utilisateur, Extole utilisera [l’endpoint de suivi utilisateur][3] pour créer un alias d’utilisateur avec l’adresse e-mail de l’utilisateur comme nom d’alias.

## Comment utiliser cette intégration

Après avoir connecté votre compte Braze au tableau de bord Extole, les événements commenceront automatiquement à circuler d’Extole vers Braze. Une vue en direct des événements envoyés à Braze peut être trouvée dans le centre des webhooks sortants d’Extole pour la résolution des problèmes. 

![][6]

Une fois que les événements et les attributs que vous avez configurés arrivent dans Braze, vous pouvez utiliser les données pour générer des audiences Braze et la segmentation des campagnes.

[1]: https://www.extole.com
[2]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[3]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/#request-body
[4]: {% image_buster /assets/img/extole/extole-outbound-webhooks.png %}
[5]: {% image_buster /assets/img/extole/extole-add-new-webhook.png %}
[6]: {% image_buster /assets/img/extole/extole-webhook-live-events.png %}