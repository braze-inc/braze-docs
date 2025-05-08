---
nav_title: Lytics
article_title: Lytics
description: "Cet article de référence traite de l'intégration de Braze et Lytics. Lytics est une plateforme de données clients d'entreprise pour les marketeurs, les analystes et les technologues. Cette intégration permet aux marques de synchroniser et de mapper leurs données Lytics directement sur Braze."
alias: /partners/lytics/
page_type: partner
search_tag: Partner
---

# Lytics

> [Lytics][1] est la plateforme de données client (CDP) de choix pour la prochaine génération d'entreprises centrées sur le client. Les solutions Lytics Decision Engine, Conductor et Cloud Connect offrent aux marketeurs et aux équipes chargées des données des possibilités de résolution d'identité, d'orchestration et d'optimisation des campagnes en temps réel et dans le respect de la confidentialité.

_Cette intégration est maintenue par Lytics._

## À propos de l'intégration

L'intégration de Braze et Lytics offre une vue unifiée de vos clients pour permettre une personnalisation puissante et mener des campagnes optimisées à l'aide de l'orchestration et des décisions de la prochaine meilleure action.

L'intégration permet aux marques de :

- Exporter des audiences vers Braze directement à partir de Lytics
- Envoyez les événements des campagnes Braze ou Canvases à Lytics en temps réel pour des campagnes personnalisées et pour créer des profils utilisateurs riches.

## Cas d'utilisation

Connectez Braze à Lytics pour [importer](#importing-data-from-braze-to-lytics) des e-mails, des SMS et l’activité des notifications push afin d'enrichir les profils utilisateurs Lytics. En utilisant conjointement Braze et Lytics, vous pouvez également [exporter](#integration) les audiences cross-canal et basées sur le comportement de Lytics pour créer des parcours clients Braze hautement personnalisés à l'aide de données first-party.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Lytics | Un compte Lytics est nécessaire pour profiter de cette intégration. |
| Numéro de compte Lytics | Un numéro de compte Lytics est nécessaire pour configurer l'URL de l'endpoint webhook. |
| Jeton API Lytics | Un jeton API REST Lytics avec des autorisations de gestionnaire de données. <br><br> Celui-ci peut être créé dans le tableau de bord Lytics à partir de la **console Paramètres du compte** > **Jetons d'accès** > **Créer un nouveau jeton.** |
| Clé API REST de Braze | Une clé API REST Braze avec l'autorisation `users.track`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Instance de Braze | Votre [instance Braze]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). En cas de doute, contactez votre gestionnaire onboarding de Braze pour obtenir ces informations. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

Cette section décrit comment exporter des données Lytics dans Braze.

### Étape 1 : Créer une autorisation

Dans Lytics, accédez au tableau de bord **Autorisation** au sein de la console **Données** dans la barre de navigation. Sélectionnez **Créer une nouvelle autorisation**, puis recherchez et sélectionnez **Braze**.

Dans l'invite **Configurer l'autorisation** qui s'affiche, fournissez un libellé et une description, puis saisissez votre clé API REST et votre instance Braze. Sélectionnez **Terminer** lorsque vous avez terminé.

![][2]{: style="max-width:80%;"}

### Étape 2 : Créer un nouvel emploi

Dans Lytics, accédez au tableau de bord **Emplois** dans la console **Données** de la barre de navigation. Sélectionnez **Créer un nouvel emploi**, recherchez et sélectionnez **Braze**.  Dans l'invite **Select Job Type** qui s'affiche, sélectionnez **Export Audience.**

![][3]{: style="max-width:80%;"}

Ensuite, choisissez une autorisation dans les options de **sélection de l'autorisation.** 

![][4]{: style="max-width:80%;"}

### Étape 3 : Configurer le travail

Dans l'invite **Configure Job**, indiquez un libellé et une description facultative. Ensuite, dans le champ **ID externe de Braze**, sélectionnez le champ de Lytics qui contient l'ID externe de Braze (`braze_id`). L'étape suivante est la plus importante : sélectionnez les audiences à exporter vers Braze.

![][5]{: style="max-width:80%;"}

Enfin, choisissez l'option préférée pour la case à cocher **Utilisateurs existants**. En laissant cette case cochée, vous ajouterez les utilisateurs qui existent déjà dans l'audience Lytics sélectionnée. Si la case n'est pas cochée, les utilisateurs ne seront exportés vers Braze que lorsqu'ils entreront ou sortiront de l'audience après le début du flux de travail.

{% alert note %}
En cochant cette case, tous les utilisateurs existants dans l'audience sélectionnée seront poussés vers Braze. Il en résultera un point de données par utilisateur et par audience pour la synchronisation initiale.
{% endalert %}

Cliquez sur **Terminer** lorsque vous avez terminé pour lancer l'exportation et enregistrer.

![][6]{: style="max-width:80%;"}

Une fois la tâche d'exportation configurée, Lytics enverra les audiences sélectionnées à Braze via l'intégration native. Vous trouverez ci-dessous un exemple d'audience montrant la structure JSON de l'audience envoyée à Braze.

```json
{
    "lytics_to_braze_audience": [{
            "external_id": "ABC124ID",
            "lytics_segments": {
                "add": [
                    "lytics_all",
                    "lytics_new"
                ]
            }
        },
        {
            "external_id": "XYZ234ID",
            "lytics_segments": {
                "add": [
                    "lytics_known"
                ],
                "remove": [
                    "lytics_new"
                ]
            }
        }
    ]
}
```

Un nouvel utilisateur sera créé dans Braze pour tout `external_id` inclus dans l'exportation d'audience qui n'existe pas encore dans Braze. 

## Importation de données de Braze vers Lytics

Vous pouvez importer des données d'audience de Braze vers Lytics à l'aide des méthodes suivantes :

- [Utilisation de webhooks](#using-webhooks)
- [À partir d'un fichier CSV](#from-a-csv-file)

### Utilisation de webhooks

#### Étape 1 : Créer un jeton API Lytics

Naviguez vers le menu du compte Lytics dans le coin inférieur gauche en sélectionnant votre nom de compte, et sélectionnez **Jetons d'accès** dans le menu déroulant. Ensuite, sélectionnez **Créer un jeton d’API.**

![][7]{: style="max-width:80%;"}

Saisissez un nom, une description facultative et une période d'expiration du jeton. Ensuite, activez le **gestionnaire de données** pour les autorisations API et cliquez sur **Générer un jeton**. Copiez le jeton et conservez-le en lieu sûr.

![][8]{: style="max-width:80%;"}

#### Étape 2 : Configurez l'URL du webhook de Lytics

L'URL du webhook Lytics est utilisée par Braze pour envoyer un message à l'API Lytics depuis Braze. Ce message peut être utilisé pour personnaliser vos campagnes dans Lytics ou peut être utilisé pour enrichir votre profil client Lytics. Les deux paramètres suivants doivent être ajoutés à l'URL du webhook de Lytics :

- Numéro de compte Lytics
- Jeton API Lytics

Configurez l'URL de votre webhook comme suit :

```
https://api.lytics.io/c/<ACCOUNT-NUMBER>/braze_users?key=<LYTICS-API-TOKEN>
```

Remplacez `<ACCOUNT-NUMBER>` par votre numéro de compte et `<LYTICS-API-TOKEN>` par votre jeton API Lytics.

#### Étape 3 : Créer un webhook à Braze 

Dans Braze, créez une nouvelle [campagne webhook.]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) Ajoutez l'URL du webhook de Lytics dans le champ **URL du webhook.**

Après avoir défini le type de requête (méthode HTTP `POST`) et configuré le reste des détails du webhook, votre webhook est prêt à être testé et déployé. Voici un exemple de corps de la requête POST après avoir configuré le webhook à Braze :

```json
{
  "city": "AnyTown",
  "country": "United States",
  "first_name": "John",
  "gender": "male",
  "language": "English",
  "last_name": "Smith",
  "date_of_birth": "19820101",
  "phone_number": "5551231234",
  "time_zone": "GMT+7",
  "twitter_handle": "johnsmith",
  "email": "john.smith@email.com",
  "braze_id": "xxxxxx" 
}
```

### À partir d'un fichier CSV

Cette section décrit comment importer les données des utilisateurs de Braze d'un segment dans Lytics.

#### Étape 1 : Créer une autorisation

Dans Lytics, accédez au tableau de bord **Autorisation** au sein de la console **Données** dans la barre de navigation. Sélectionnez **Créer une nouvelle autorisation**, puis recherchez et sélectionnez **Intégrations personnalisées**.

Sélectionnez le type d'autorisation SFTP qui vous convient le mieux en fonction de vos besoins en termes de sécurité et d'activité. Les types d'autorisation suivants sont pris en charge pour l'importation de fichiers dans Lytics via SFTP :

- Autorisation du serveur SFTP du client
- Autorisation du serveur SFTP du client avec la clé privée PGP
- Autorisation du serveur SFTP géré par Lytics

Les autorisations SFTP à clé publique sont destinées à être utilisées uniquement pour l'exportation SFTP.

![][9]{: style="max-width:80%;"}

Dans l'invite **Configurer l'autorisation** qui s'affiche, fournissez un libellé et une description et complétez le reste des exigences de configuration. Cliquez sur **Terminer** lorsque vous avez terminé.

#### Étape 2 : Exporter vos données de segmentation au format CSV

Dans Braze, naviguez vers **Audience** > **Segments**. Localisez le segment que vous souhaitez exporter, puis sélectionnez <i class="fas fa-gear" aria-label="Paramètres"></i> puis **Exporter les données utilisateur au format CSV**. Vous pouvez exporter jusqu'à 500 000 utilisateurs dans une segmentation. Pour plus d'informations, reportez-vous à la section [Exportation des données de segmentation au format CSV]({{site.baseurl}}/user_guide/data/export_braze_data/segment_data_to_csv/).

#### Étape 3 : Configurer une tâche d'importation CSV

Dans Lytics, accédez au tableau de bord **Emplois** dans la console **Données** de la barre de navigation. Sélectionnez **Créer un nouveau travail**, puis recherchez et sélectionnez **Intégrations personnalisées**.

Sélectionnez ensuite le type de travail. Pour importer des fichiers CSV de Braze dans Lytics, sélectionnez **Importer CSV** comme type de travail.

![][10]{: style="max-width:80%;"}

Enfin, saisissez un libellé et une description facultative pour la tâche et configurez tout autre détail nécessaire. Cliquez sur **Terminer** pour lancer et enregistrer le travail.


[1]: https://www.lytics.com/
[2]: {% image_buster /assets/img/lytics/braze_authorization.png %}
[3]: {% image_buster /assets/img/lytics/braze_jobtype.png %}
[4]: {% image_buster /assets/img/lytics/braze_jobauth.png %}
[5]: {% image_buster /assets/img/lytics/braze_job.png %}
[6]: {% image_buster /assets/img/lytics/braze_backfill.png %}
[7]: {% image_buster /assets/img/lytics/create_token.png %}
[8]: {% image_buster /assets/img/lytics/data_manager.png %}
[9]: {% image_buster /assets/img/lytics/authorization_method.png %}
[10]: {% image_buster /assets/img/lytics/configure_job.png %}





