---
nav_title: Transcend
article_title: Transcend
page_order: 1
description: "Transcend, une plate-forme d'infrastructure de confidentialité des données, aide à automatiser la réalisation des demandes de données en orchestrant les données sur des dizaines de systèmes de données, y compris le Brésil."
alias: /fr/partners/transcend/
page_type: partenaire
search_tag: Partenaire
---

# Transcend

> Transcend est une entreprise d'infrastructure de protection des données qui permet aux entreprises de donner facilement le contrôle de leurs utilisateurs sur leurs données personnelles, satisfaisant automatiquement les demandes d'objet de données au sein des entreprises à travers tous leurs systèmes de données et fournisseurs. Transcend fournit à leurs utilisateurs finaux un panneau de configuration, ou "Centre de confidentialité", hébergé à `confidentialité.<company\>.com` où les utilisateurs peuvent gérer leurs préférences de confidentialité, exporter leurs données ou les supprimer. En rendant les données sans problème pour les entreprises, Transcend met les utilisateurs partout dans le siège du conducteur de leurs données personnelles.

Le partenariat Braze et Transcend aide les utilisateurs à automatiser les demandes de confidentialité en orchestrant les données sur des dizaines de systèmes de données. En fin de compte, cela aide les équipes à se conformer à la réglementation comme le RGPD et l’ACCP et place les personnes sur le siège du conducteur en ce qui concerne leurs données.

## Pré-requis

| Pré-requis                                    | Origine   | Accès                                                                                                                                                                                                                                                                             | Libellé                                                                                                             |
| --------------------------------------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Compte transcend & Informations sur le compte | Transcend | [https://app.transcend.io/](https://app.transcend.io/)                                                                                                                                                                                                                            | Un compte Transcend actif avec les privilèges d'administrateur est nécessaire pour utiliser l'intégration de Braze. |
| Clé API Braze                                 | Brasero   | Vous devrez créer une nouvelle clé API.<br><br>Ceci peut être créé dans la __Console Développeur -> Paramètres API -> Créer une nouvelle clé API__ avec __utilisateurs. elete, users.alias.new, users.export.ids, email.unsubscribe, email.blacklist__ autorisations. | Cette clé API sera utilisée lors de la connexion du silo de données Braze à la plate-forme Transcend.               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration de Transcend et Braze

Transcend vous permet d'accéder par programme à la plateforme Braze et d'effacer et d'opter pour que les utilisateurs ne communiquent pas dans le respect des règles de confidentialité des données.

### Étape 1 : Mise en place de l’intégration Braze
Pour commencer, connectez-vous à [Transcend](https://app.transcend.io/login).

1. Dans la plate-forme Transcend, accédez à __Data Map__ > __Ajouter Data Silo__ > __Braze__ et sélectionnez le bouton __Connecter__.
2. Lorsque votre compte est provisionné, vous vous connecterez à l'une des URL correspondantes : https://dashboard-01.braze.com, https://dashboard-02.braze.com, ... https://dashboard-01.braze.eu<br> Utilisez la table [suivante]({{site.baseurl}}/api/basics/#endpoints) pour déterminer quel sous-domaine vous devez brancher en fonction de l'URL de votre tableau de bord.
3. Une fois connecté, revenez à l'onglet __Centre de confidentialité__ de Transcend. Ici, vous devrez associer les données de Braze à vos __Pratiques de Données__. Pour ce faire, créez une nouvelle catégorie et une nouvelle __collection de données__ avec la convention de nommage appropriée (par exemple, "Listes de diffusion ou profil d'utilisateur"). Lorsque vous avez terminé, appuyez sur __Publier__.
4. Retournez à votre __Data Map__ et cliquez sur le silo. Développer __Gérer les points de données__ et sélectionner l'étiquette de la collection (catégorie) que vous avez créée dans l'étape précédente à partir du menu déroulant. Vous pouvez également choisir quelles actions de données (par exemple, accès ou effacement) sont activées pour quels points de données.
5. Ensuite, tout en étant toujours dans le silo, développez __Gérer les identifiants__. Cochez les cases respectives pour lesquelles vous souhaitez activer les identifiants. Par exemple, si vous souhaitez que Transcend recherche les utilisateurs par adresse e-mail, vous cochez la case pour activer l'identifiant de l'adresse e-mail.

{% alert note %}
Si les identifiants ne sont pas activés correctement, Transcend peut ne pas être en mesure de traiter les requêtes de certains utilisateurs.
{% endalert %}

### Étape 2 : Tester les requêtes
Transcend recommande de tester les requêtes sur votre Carte de Données avant de commencer à traiter les requêtes des utilisateurs finaux. Pour faire ceci :

1. Allez au __Centre de Confidentialité__ et cliquez sur __Voir votre Centre de Confidentialité__.
2. Depuis votre __centre de confidentialité__, cliquez sur __Prenez le contrôle__, puis __Téléchargez mes données__. Vous devrez entrer votre adresse e-mail ou vous connecter pour vous authentifier avant de soumettre la demande.
3. Vérifiez votre email pour un message de Transcend. Il vous sera demandé de cliquer sur un lien de vérification pour vérifier la demande.
4. Ensuite, de retour dans le __Tableau de bord admin__, accédez à l’onglet __Requêtes entrantes__ et sélectionnez votre demande. Si vous ne voyez pas la demande ici, contactez Transcend à [support@transcend.io](mailto:support@transcend.io).
5. Une fois que vous avez cliqué sur votre demande, accédez à l'onglet __Data Silos__ et sélectionnez __Braze__. Inspectez et confirmez les données retournées.
6. Enfin, accédez à l'onglet __Rapport__ et cliquez sur __Approuver et Envoyer__. Vous devriez recevoir le rapport à l'adresse électronique que vous avez soumise avec la demande.

### Étape 3 : Suppression de l’intégration Braze

1. Pour supprimer le silo de données Braze de votre __Data Map__, accédez à votre __Carte de Données__, et cliquez dans __Braze__.
2. En bas de l'écran, développez __Supprimer Braze__et cliquez sur __Supprimer Silo__. Vous serez invité à confirmer que vous souhaitez supprimer le silo. Click __Ok__.
3. Confirmez que le silo a été supprimé en revenant vers votre __Data Map__.
