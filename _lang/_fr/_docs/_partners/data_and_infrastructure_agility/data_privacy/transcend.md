---
nav_title: Transcend
article_title: Transcend
page_order: 1
description: "Transcend, une plate-forme d'infrastructure de confidentialité des données, aide les utilisateurs de Braze à automatiser la gestion des demandes de données sujettes. Cela vous permet d'accéder par programme à la plateforme Braze et d'effacer et d'opter pour les utilisateurs qui ne communiquent pas, conformément à la réglementation en matière de confidentialité des données."
alias: /fr/partners/transcend/
page_type: partenaire
search_tag: Partenaire
---

# Transcend

> Transcend est une société d'infrastructure de protection des données qui permet aux entreprises de donner facilement le contrôle de leurs utilisateurs sur leurs données, satisfaisant automatiquement les demandes d'objet de données au sein des entreprises à travers tous leurs systèmes de données et fournisseurs.

Le partenariat Braze et Transcend aide les utilisateurs à automatiser les demandes de confidentialité en orchestrant les données sur des dizaines de systèmes de données. aider les équipes à se conformer à la réglementation du RGPD et de l’ACPC. Transcend fournit aux utilisateurs finaux un panneau de contrôle ou un centre de confidentialité, hébergé à `confidentialité.<company\>.com` où les utilisateurs peuvent gérer leurs préférences de confidentialité, exporter leurs données ou les supprimer.

## Pré-requis

| Exigences        | Libellé                                                                                                                                                                                                                                                                                 |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte transcend | Un compte [Transcend](https://app.transcend.io/) avec des privilèges d'administration est requis pour profiter de ce partenariat.                                                                                                                                                       |
| Clé API Braze    | Une clé API Braze REST avec les permissions `users.delete, users.alias.new, users.export.ids, email.unsubscribe,`et `email.blacklist` .<br><br>Ceci peut être créé dans le __tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API__ |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

Transcend vous permet d'accéder par programme à la plateforme Braze et d'effacer et d'opter pour que les utilisateurs ne communiquent pas dans le respect des règles de confidentialité des données.

### Étape 1 : Mettre en place l’intégration de Braze
Pour commencer, connectez-vous à [Transcend](https://app.transcend.io/login).
1. Accédez à **Data Map > Ajouter Data Silo > Braze** et sélectionnez le bouton **Connecter**.<br><br>
2. Lorsque votre compte est provisionné, vous vous connecterez à l'une des URL correspondantes : `https://dashboard-01.braze.com`, `https://dashboard-02.braze.com, . ., https://dashboard-01.braze.eu`.<br> Utilisez la [table suivante]({{site.baseurl}}/api/basics/#endpoints) pour déterminer quel sous-domaine vous devez inclure en fonction de l'URL de votre tableau de bord.<br><br>
3. Une fois connecté, accédez à l'onglet **Centre de confidentialité** de Transcend. Ici, vous devrez associer les données de Braze à vos pratiques en matière de données. Pour ce faire, créez une nouvelle catégorie et une nouvelle collection de données avec la convention de nommage appropriée (par exemple, "Listes de diffusion ou profil d'utilisateur"). Une fois terminé, appuyez sur **Publier**.<br><br>
4. Retournez à votre Carte de Données et cliquez sur le silo. Développer **Gérer les points de données** et sélectionner l'étiquette de la collection (catégorie) que vous avez créée à l'étape précédente à partir du menu déroulant. Vous pouvez également choisir quelles actions de données (par exemple, accès ou effacement) sont activées pour quels points de données. <br><br>
5. Ensuite, tout en étant toujours dans le silo, développez **Gérer les identifiants**. Cochez les cases respectives pour lesquelles vous souhaitez activer les identifiants. Par exemple, si vous souhaitez que Transcend recherche les utilisateurs par adresse e-mail, vous cochez la case pour activer l'identifiant de l'adresse e-mail.

{% alert note %}
Si les identifiants ne sont pas activés correctement, Transcend ne peut pas traiter les requêtes de certains utilisateurs.
{% endalert %}

### Étape 2 : Demandes de test
Transcend recommande de tester les requêtes sur votre Carte de Données avant de commencer à traiter les requêtes des utilisateurs finaux.
1. Allez au **Centre de confidentialité** dans Transcend et cliquez sur **Voir votre centre de confidentialité**.<br><br>
2. Depuis votre **centre de confidentialité**, cliquez sur **Prenez le contrôle**, puis **Téléchargez mes données**. Entrez votre adresse e-mail ou connectez-vous pour vous authentifier avant de soumettre la demande.<br><br>
3. Vérifiez votre email pour un message de Transcend. Il vous sera demandé de cliquer sur un lien de vérification pour vérifier la demande.<br><br>
4. Ensuite, de retour dans le tableau de bord **Admin** , accédez à l'onglet **Requêtes entrantes** et sélectionnez votre demande. Contactez Transcend à [support@transcend.io](mailto:support@transcend.io) si vous ne voyez pas la demande ici.<br><br>
5. Une fois que vous avez cliqué sur votre demande, accédez à l'onglet **Data Silos** et sélectionnez **Braze**. Inspectez et confirmez les données retournées.<br><br>
6. Enfin, accédez à l’onglet **Rapport** et cliquez sur **Approuver et Envoyer**. Vous devriez recevoir le rapport à l'adresse électronique que vous avez soumise avec la demande.

## Supprimer l’intégration de Braze
Pour supprimer le silo de données Braze de votre carte de données transcende:
1. Naviguez vers votre **Data Map**, et cliquez dans **Braze**. <br><br>
2. En bas de l'écran, développez **Supprimer Braze** et cliquez sur **Supprimer Silo**. Vous serez invité à confirmer que vous souhaitez supprimer le silo. Click **Ok**. <br><br>
3. Confirmez que le silo a été supprimé en revenant vers votre Carte des données.