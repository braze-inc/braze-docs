---
nav_title: CDI pour Redshift
article_title: Ingestion de données cloud dans Braze pour Redshift
description: "Cet article de référence couvre l’Ingestion de Données Cloud dans Braze et comment synchroniser les données utilisateur pertinentes avec votre intégration Redshift."
page_order: 2
page_type: reference

---

# Ingestion de données cloud pour Redshift

{% alert important %}
L’ingestion de données cloud Braze pour Redshift est actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.
{% endalert %}

## Paramétrage du produit

Les nouvelles intégrations d’ingestion de données cloud nécessitent une configuration sur Braze ainsi que dans votre instance Redshift. Suivez ces étapes pour configurer votre intégration :
1. Assurez-vous que Braze est autorisé à accéder aux tables Redshift que vous souhaitez synchroniser. Braze se connectera à Redshift sur Internet.
2. Dans votre instance Redshift, paramétrez la ou les tables ou vues que vous voulez synchroniser avec Braze
3. Créer une nouvelle intégration dans le tableau de bord de Braze
4. Testez l’intégration et démarrez la synchronisation

### Paramétrez les tables et les vues

#### Étape 1 : Configurer le tableau 

De manière optionnelle, définissez une nouvelle base de données et un nouveau schéma pour contenir votre tableau source
```json
CREATE DATABASE BRAZE_CLOUD_PRODUCTION;
CREATE SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION;
```
Créer un tableau (ou vue) à utiliser pour votre intégration CDI
```json
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_ATTRIBUTES_SYNC (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar,
   payload varchar(max)
)
```

Vous pouvez donner le nom que vous désirez à la base de données, au schéma et au tableau, mais les noms de colonnes doivent correspondre aux définitions ci-dessus.

- `UPDATED_AT` : L’heure à laquelle la rangée a été mise à jour ou ajoutée au tableau. Nous ne synchroniserons que les rangées qui ont été ajoutées ou mises à jour depuis la dernière synchronisation.
- Colonnes d’identifiant utilisateur. Votre tableau peut contenir une ou plusieurs colonnes d’identifiants utilisateur. Chaque ligne ne doit contenir qu’un seul identifiant (soit un `external_id`, la combinaison d’un `alias_name` et d’un `alias_label`, soit un `braze_id`. Une table source peut contenir des colonnes pour un, deux ou les trois types d’identifiants. 
    - `EXTERNAL_ID` : Ceci identifie l’utilisateur que vous désirez mettre à jour.  Cela doit correspondre à la valeur `external_id` utilisée dans Braze. 
    - `ALIAS_NAME` et `ALIAS_LABEL` : Ces deux colonnes créent un objet d'alias d'utilisateur. `alias_name` doit être un identifiant unique et `alias_label` spécifie le type d'alias. Les utilisateurs peuvent avoir plusieurs alias avec différentes étiquettes, mais seulement un `alias_name` par `alias_label`.
    - `BRAZE_ID` : L’identifiant d’utilisateur Braze. Il est généré par le SDK Braze et les nouveaux utilisateurs ne peuvent pas être créés à l’aide d’un ID Braze via l’ingestion de données cloud. Pour créer de nouveaux utilisateurs, spécifiez un ID utilisateur externe ou un alias utilisateur. 
- `PAYLOAD` : Il s’agit d’une chaîne de caractères JSON des champs que vous désirez synchroniser à l’utilisateur dans Braze.
 
#### Étape 2 : Créer un utilisateur et attribuer des autorisations 

```json
CREATE USER braze_user PASSWORD '{password}';
GRANT USAGE ON SCHEMA BRAZE_CLOUD_PRODUCTION.INGESTION to braze_user;
GRANT SELECT ON TABLE USERS_ATTRIBUTES_SYNC TO braze_user;
```

Un nombre minimum d’autorisations est requis pour cet utilisateur. Si vous créez plusieurs intégrations CDI, vous devriez donner des autorisations pour un schéma ou les gérer en utilisant un groupe. 

#### Étape 3 : Autoriser l’accès aux IP de Braze (facultatif) 

Si vous avez un pare-feu ou d’autres politiques réseau actives, vous devrez donner accès au réseau de votre instance Redshift à Braze. Autorisez l’accès aux IP ci-dessous correspondant à la région de votre tableau de bord de Braze. 

| Pour les instances `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06` | Pour les instances `EU-01` et `EU-02` |
|---|---|
| `23.21.118.191`| `52.58.142.242`
| `34.206.23.173`| `52.29.193.121`
| `50.16.249.9`| `35.158.29.228`
| `52.4.160.214`| `18.157.135.97`
| `54.87.8.34`| `3.123.166.46`
| `54.156.35.251`| `3.64.27.36`
| `52.54.89.238`| `3.65.88.25`
| `18.205.178.15`| `3.68.144.188`
|   | `3.70.107.88`

### Créer une nouvelle intégration dans le tableau de bord de Braze

Rendez-vous sur la page Redshift de Braze, dans **.Technology Partners (partenaires technologiques)** et cliquez sur **Create new import sync (Créer une nouvelle synchronisation d’importation)**

1. **Ajoutez les informations de connexion et le tableau source de Redshift **<br>
Saisissez les informations de votre entrepôt de données Redshift et du tableau source et passez à l’étape suivante.<br>![][1]<br><br>
2. **Configurer les détails de la synchronisation**<br>
Choisissez ensuite un nom pour votre synchronisation et entrez les e-mails de contact. Nous utiliserons ces informations de contact pour vous signaler toute erreur d’intégration (par ex., l’accès au tableau a été supprimé inopinément).<br>![][2]<br><br> Vous choisirez également le type de données et la fréquence de synchronisation. La fréquence peut être définie une fois toutes les 15 minutes jusqu’à une fois par mois. Nous utiliserons le fuseau horaire configuré dans votre tableau de bord de Braze pour planifier la synchronisation récurrente. Les types de données supportés sont Attributs personnalisés, Événements personnalisés, et Événements d’Achat. Le type de données pour une synchronisation ne peut pas être modifié une fois créé. 

### Tester la connexion

Une fois tous les détails de configuration de votre synchronisation saisis, cliquez sur **Test connection (Tester la connexion)**. Si vous avez réussi, vous pourrez voir un aperçu des données. Si, pour une raison quelconque, nous ne pouvons pas nous connecter, nous afficherons un message d’erreur pour vous aider à résoudre le problème.

![][3]

{% alert note %}
Vous devez avoir testé une intégration avec succès pour qu’elle puisse passer du mode Draft au mode Active. Si vous avez besoin de fermer la page de création, votre intégration sera sauvegardée et vous pourrez revenir à la page Détails pour effectuer des changements et les tester.  
{% endalert %}

### Définir des intégrations ou des utilisateurs supplémentaires (optionnel)

Vous pouvez également définir plusieurs intégrations avec Braze, mais chaque intégration devra être configurée pour se synchroniser à un tableau différent. Lorsque vous créez des synchronisations supplémentaires, vous pouvez réutiliser des identifiants existants si vous vous connectez au même compte Redshift.
![][4]

Si vous réutilisez le même utilisateur dans les intégrations, vous ne pourrez pas supprimer l’utilisateur dans le tableau de bord de Braze tant qu’il n’aura pas été supprimé de toutes les synchronisations actives.

### Exécuter la synchronisation

Une fois qu’elle est activée, votre synchronisation s’exécutera selon la planification définie pendant la configuration. Si vous désirez exécuter la synchronisation en dehors des horaires de planification habituels pour tester ou récupérer les données les plus récentes, cliquez sur **Sync Now (Synchroniser maintenant)**. Cette exécution n’aura pas d’impact sur les synchronisations futures et habituelles planifiées. 
![][5]

[1]: {% image_buster /assets/img/cloud_ingestion/ingestion_6.png %}
[2]: {% image_buster /assets/img/cloud_ingestion/ingestion_7.png %}
[3]: {% image_buster /assets/img/cloud_ingestion/ingestion_8.png %}
[4]: {% image_buster /assets/img/cloud_ingestion/ingestion_9.png %}
[5]: {% image_buster /assets/img/cloud_ingestion/ingestion_10.png %}
