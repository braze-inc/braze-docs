---
nav_title: Transcend
article_title: Transcend
description: "Cet article de référence décrit le partenariat entre Braze et Transcend, une plateforme d’infrastructure de confidentialité des données qui aide les utilisateurs de Braze à automatiser l’exécution des demandes des personnes concernées."
alias: /partners/transcend/
page_type: partner
search_tag: Partenaire

---

# Transcend

> Transcend est une entreprise d’infrastructure de confidentialité des données qui permet aux entreprises de contrôler leurs données de façon simple et automatique, en remplissant automatiquement les demandes des personnes concernées à travers tous leurs fournisseurs et systèmes de données. 

Le partenariat entre Braze et Transcend permet aux utilisateurs d’automatiser les demandes de confidentialité en organisant les données issues de dizaines de systèmes de données, aidant ainsi les équipes à se conformer aux réglementations telles que le RGPD et le CCPA. Transcend fournit aux utilisateurs finaux un panneau de contrôle, également appelé centre de confidentialité, hébergé par `privacy.\<company\>.com` et où les utilisateurs peuvent gérer leurs préférences de confidentialité et exporter ou supprimer leurs données. 

## Conditions préalables

| Conditions | Description |
|---|---|
| Compte Transcend | Un compte [Transcend](https://app.transcend.io/) avec privilèges administrateur est nécessaire pour profiter de ce partenariat. |
| Clé API Braze | Une clé API REST Braze avec des autorisations `users.delete, users.alias.new, users.export.ids, email.unsubscribe,` et `email.blacklist`.<br><br>Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

Transcend vous permet d’accéder à des utilisateurs, de les supprimer et de les désinscrire des communications depuis la plateforme Braze via un programme, conformément aux réglementations de confidentialité des données.

### Étape 1 : Configurer l’intégration Braze
Pour commencer, connectez-vous à [Transcend](https://app.transcend.io/login).
1. Accédez à **Data Map (Carte de données) > Add Data Silo (Ajouter un silo de données) > Braze** et cliquez sur le bouton **Connect (Connexion)**.<br><br>
2. Une fois votre compte provisionné, vous vous connecterez à l’une des URL suivantes : `https://dashboard-01.braze.com`, `https://dashboard-02.braze.com, ..., https://dashboard-01.braze.eu`.<br> Utilisez le [tableau]({{site.baseurl}}/api/basics/#endpoints) suivant pour déterminer quel sous-domaine vous devez inclure en fonction de l’URL de votre tableau de bord.<br><br>
3. Une fois connecté, accédez à l’onglet **Privacy Center (Centre de confidentialité)** de Transcend. Vous devrez ensuite mapper les données de Braze à vos pratiques en matière de données. Pour ce faire, créez une nouvelle catégorie et une nouvelle collecte de données avec la convention d’affectation de nom appropriée (par ex., « Listes de distribution ou Profil d’utilisateur »). Une fois terminé, cliquez sur **Publish (Publier)**.<br><br>
4. Revenez à votre carte de données et cliquez sur le silo de données Braze. Développez le menu **Manage Endpoints (Gérer les points de données)** et sélectionnez le libellé de la collection (catégorie) que vous avez créée à l’étape précédente à partir de la liste déroulante. Vous pouvez également choisir quelles actions (par ex., accès ou suppression) sont activées pour chaque point de données. <br><br>
5. Ensuite, tout en restant dans le silo de données Braze, développez le menu **Manager Identifiers (Gérer les identifiants)**. Cochez les cases correspondant aux identifiants que vous souhaitez activer. Par exemple, si vous souhaitez que Transcend recherche des utilisateurs par adresse e-mail, vous devez cocher la case Identifiant d’adresse e-mail.

{% alert note %}
Si les identifiants ne sont pas activés correctement, il se peut que Transcend ne puisse pas traiter les demandes de certains utilisateurs.
{% endalert %}

### Étape 2 : Requêtes de test
Transcend recommande des requêtes de test sur votre carte de données avant de commencer à traiter des requêtes provenant des utilisateurs finaux.
1. Accédez au **Privacy Center (Centre de confidentialité)** de Transcend et cliquez sur **View your Privacy Center (Consulter votre centre de confidentialité)**.<br><br>
2. Depuis votre **Privacy Center (Centre de confidentialité)**, cliquez sur **Take Control (Prendre le contrôle)**, puis **Download my data (Télécharger mes données)**. Saisissez votre adresse e-mail ou connectez-vous pour vous authentifier avant de soumettre la requête.<br><br>
3. Ouvrez vos e-mails pour consulter le message de Transcend. Vous devez cliquer sur le lien de vérification pour valider la requête.<br><br>
4. Ensuite, dans le tableau de bord **Admin**, accédez aux **Incoming Requests (Requêtes entrantes)** et sélectionnez votre requête. Si la requête n’apparait pas ici, veuillez contacter Transcend à l’adresse [support@transcend.io](mailto:support@transcend.io).<br><br>
5. Après avoir cliqué sur votre requête, accédez à l’onglet **Data Silos (Silos de données)** et sélectionnez **Braze**. Vérifiez et confirmez les données renvoyées.<br><br>
6. Enfin, accédez à l’onglet **Report (Rapport)** et cliquez sur **Approve and Send (Approuver et envoyer)**. Vous devriez recevoir le rapport à l’adresse e-mail que vous avez renseignée avec la requête.

## Supprimer l’intégration Braze
Pour supprimer le silo de données Braze de votre carte de données Transcend :
1. Accédez à votre **Data Map (Carte de données)**, puis cliquez sur **Braze**. <br><br>
2. Au bas de l’écran, développez le menu **Remove Braze (Supprimer Braze)**, puis cliquez sur **Remove Silo (Supprimer le silo)**. Un message vous demandera de confirmer que vous souhaitez bien supprimer le silo. Cliquez sur **OK**. <br><br>
3. Vérifiez que le silo a bien été supprimé en revenant à votre carte de données.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)