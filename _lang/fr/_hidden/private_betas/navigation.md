---
nav_title: Navigation
permalink: /navigation/
hidden: true
---

# Navigation dans Braze

> Nous mettons à jour la navigation dans Braze pour vous aider à créer et à accéder à votre contenu plus rapidement et plus efficacement. En vue de faciliter cette transition pour vous et votre équipe, ce guide couvre ce qui a changé et ce à quoi vous pouvez vous attendre ensuite.

La nouvelle navigation dans Braze présente une architecture informationnelle entièrement repensée (comment les informations sont organisées, regroupées et présentées) pour rendre chaque partie de Braze plus facile à trouver et à comprendre. 

Les fonctionnalités sont désormais organisées en catégories intuitives qui sont familières et pertinentes pour le flux de travail d’un marketeur dans Braze. Les catégories de niveau supérieur sont réduites par défaut afin que vous puissiez obtenir une meilleure vue de chaque section en un coup d’œil. Certaines pages ont été renommées pour mieux représenter leur contenu.

Les participants en accès anticipé peuvent activer la nouvelle navigation à tout moment en sélectionnant **Switch to new nav (Basculer vers la nouvelle navigation)** dans l’en-tête global.

![En-tête global de Braze avec un bouton pour basculer vers la nouvelle navigation.]({% image_buster /assets/img/navigation/global_header_switch.png %}){: style="max-width:70%"}

{% alert important %}
La nouvelle navigation est actuellement en accès anticipé et est en cours de test avec un groupe sélectionné de clients. Au cours de la période d’accès anticipé, nous recueillerons régulièrement des commentaires. Vous pouvez partager des commentaires directement à partir du tableau de bord : dans la nouvelle vue de navigation, développez le bouton **Tour new navigation (Explorer la nouvelle navigation)** et sélectionnez **Send feedback (Envoyer un commentaire)**.
{% endalert %}

## À quoi s’attendre ensuite

La nouvelle navigation sera proposée à tous les clients Braze en **avril 2023** et comprendra une apparence et une convivialité mises à jour, différentes de la version à accès anticipé.

## Ce qui a changé

### Nouveau nom pour Groupe d'Apps

Dans le cadre de nos changements d’architecture informationnelle et de navigation, nous avons renommé « Groupe d'Apps » en « Espace de travail ». Nous reconnaissons que le terme « Groupe d'Apps » ne reflète pas la façon dont de nombreux utilisateurs intègrent, abordent et utilisent la plateforme Braze. Pour mieux refléter les nombreux cas d’utilisation de Braze, « Groupe d'Apps » est désormais « Espace de travail ».

Si vous utilisez notre navigation mise à jour, ce changement apparaîtra sur l’ensemble de la plateforme.

### En-tête global

{% tabs %}
{% tab Nouvelle navigation %}

![]({% image_buster /assets/img/navigation/global_header_new.png %}){: style="border:0"}

1. **Logo Braze** - Sélectionnez pour accéder à votre page d’accueil Braze.
2. **Page name (Nom de la page)** - Le nom de la page sur laquelle vous vous trouvez actuellement.
3. **Tour new navigation (Explorer la nouvelle navigation)** - Reprenez l’exploration de la navigation ou développez la liste déroulante pour accéder aux options de documentation ou pour nous envoyer des commentaires sur la nouvelle navigation.
4. **Community (Communauté)** - Accédez aux liens vers la communauté Braze Bonfire, notre blog, les études de cas et la feuille de route des produits.
5. **Support (Assistance)** - Vérifiez l’état de notre système et accédez aux liens vers la documentation Braze, Braze Learning ou demandez de l’aide.
6. **Language selector (Sélecteur de langue)** - Sélectionnez la langue que vous souhaitez utiliser pour Braze.
7. **Your profile (Votre profil)** - Affichez votre profil, les paramètres de votre entreprise, la facturation, les utilisateurs de votre entreprise ou déconnectez-vous.
8. **Icône Administrateur** - Apparaît à côté de votre profil si vous êtes administrateur pour votre entreprise.

{% endtab %}
{% tab Ancienne navigation %}

![]({% image_buster /assets/img/navigation/global_header_old.png %}){: style="border:0"}

1. **Logo Braze** - Sélectionnez pour accéder à votre page d’accueil Braze.
2. **Page name (Nom de la page)** - Le nom de la page sur laquelle vous vous trouvez actuellement.
3. **Switch to new nav (Basculer vers la nouvelle navigation)** - Basculez votre vue vers la nouvelle expérience de navigation ou développez la liste déroulante pour accéder à la documentation.
3. **Resources (Ressources)** - Accédez aux liens vers Braze Learning, la documentation, la communauté Braze Bonfire, notre blog, des études de cas et la feuille de route des produits.
4. **Get Help (Obtenir de l’aide)** - Vérifiez l’état de notre système, consultez les articles d’aide ou demandez de l’aide au service d’assistance.
5. **Language selector (Sélecteur de langue)** - Sélectionnez la langue que vous souhaitez utiliser pour Braze.
6. **Your profile (Votre profil)** - Affichez votre profil, les paramètres de votre entreprise, les abonnements et l’utilisation, les utilisateurs de votre entreprise ou déconnectez-vous.
7. **Icône Administrateur** - Apparaît à côté de votre profil si vous êtes administrateur pour votre entreprise.

{% endtab %}
{% tab Changements %}

![]({% image_buster /assets/img/navigation/global_header_compare.png %}){: style="border:0"}

- Communauté
   -**Resources (Ressources)** est désormais **Community (Communauté)**
- Assistance
   -**Get Help (Obtenir de l’aide)** est maintenant **Support (Assistance)** 
   -**Braze Learning** et **Documentation** sont maintenant disponibles ici
   -**Braze Support (Assistance Braze)** est maintenant **Get Help (Obtenir de l’aide)** 
- Votre profil
   - **Account Settings (Paramètres du compte)** est maintenant **Manage Your Profile (Gérer votre profil)**
   -**Subscriptions and Usage (Abonnements et utilisation)** est maintenant **Billing (Facturation)**
   -**Manage Users (Gérer les utilisateurs)** est désormais **Company Users (Utilisateurs de l’entreprise)**

{% endtab %}
{% endtabs %}

### Barre latérale

<style>
#navigation td {
    word-break: break-word;
    width: 50%;
    font-size: 16px;
}
</style>

{% tabs %}
{% tab Nouvelle navigation %}

<table id="navigation">
<tbody>
  <tr>
    <td><img src="{% image_buster /assets/img/navigation/sidebar_new.png %}"></td>
    <td><b>1. Workspace selector (Sélecteur d’espace de travail)</b> - Vous permet de voir dans quel espace de travail vous vous trouvez actuellement ou de basculer entre les espaces de travail.<br><br><b>2. Home (Accueil)</b> - Page d’accueil Braze. Après votre configuration initiale, il s’agit de votre tableau de bord <b>Overview (Aperçu)</b>.<br><br><b>3. Messaging (Envoi de messages)</b> - Créez et gérez vos campagnes et vos Canvas, et accédez à une vue calendrier de vos prochains messages planifiés.<br><br><b>4. Audience</b> - Contient tout ce qui est lié à vos utilisateurs, tel que : recherche ou importation d’utilisateurs, gestion de vos segments, Groupe de contrôle global, groupes d’abonnement, etc.<br><br><b>5. Templates (Modèles)</b> - Contient vos modèles de message, blocs de contenu et votre bibliothèque multimédia.<br><br><b>6. Analytics (Analyses)</b> - Contient vos rapports, votre tableau de bord analytique et vos prédictions.<br><br><b>7. Partner Integrations (Intégrations de partenaires)</b> - Contient nos intégrations de partenaires technologiques, nos partenaires de solutions et exportations de données (Currents).<br><br><b>8. Data Settings (Paramètres de données)</b> - Contient les paramètres associés aux données utilisateur, tels que attributs utilisateur personnalisés, événements utilisateur personnalisés, catalogues, produits, etc.<br><br><b>9. Settings (Paramètres)</b> - Gérez votre intégration d’espace de travail, les paramètres d’espace de travail, les paramètres de l’entreprise, la facturation, etc.<br></td>
  </tr>
</tbody>
</table>

{% endtab %}
{% tab Ancienne navigation %}

<table id="navigation">
<tbody>
  <tr>
    <td><img src="{% image_buster /assets/img/navigation/sidebar_old.png %}"></td>
    <td><b>1. App Group selector (Sélecteur de groupe d’apps)</b> - Vous permet de voir dans quel groupe d’apps vous êtes actuellement ou de basculer entre les groupes d’apps.<br><br><b>2. Data (Données)</b> - Contient divers rapports, tableaux de bord et paramètres associés aux données utilisateur dans Braze.<br><br><b>3. Engagement</b> - Contient des pages liées à l’envoi de messages, telles que vos campagnes de segments, Canvas, modèles de messages, etc.<br><br><b>4. Users (Utilisateurs)</b> - Recherchez ou importez des utilisateurs, ou gérez vos groupes d’abonnement.<br><br><b>5. Integrations (Intégrations)</b> - Contient des intégrations comprenant nos partenaires technologiques, Currents et codes de promotion.<br><br><b>6. Settings (Paramètres)</b> - Contient les paramètres de groupe d’apps, divers paramètres de données, journaux, etc.</td>
  </tr>
</tbody>
</table>

{% endtab %}
{% tab Changements %}

Les catégories de niveau supérieur sont maintenant réduites par défaut afin que vous puissiez obtenir une meilleure vue de chaque section en un coup d’œil.

Le tableau suivant indique où se trouve chaque page dans la nouvelle navigation. Certaines pages ont été renommées et le nouveau nom est référencé dans la colonne « New location » (Nouvel emplacement).

| Nom de la page                     | Nouvel emplacement                                                          |
| ----------------------------- | --------------------------------------------------------------------- |
| Paramètres API                  | **Settings** > **Workspace Setup and Testing** > **API Keys** (Paramètres > Configuration d’espace de travail et Tests > Clés API)         |
| Flux de travail d’approbation             | **Settings** > **Workspace Settings** > **Approval Workflow** (Paramètres > Paramètres d’espace de travail > Flux de travail d’approbation)         |
| Campagnes                     | **Messaging** > **Campaigns** (Envoi de messages > Campagnes)                                         |
| Calendrier                      | **Messaging** > **Content Calendar** (Envoi de messages > Calendrier de contenu)                                  |
| Canvas                        | **Messaging** > **Canvas** (Envoi de messages > Canvas)                                            |
| Catalogues                      | **Data Settings** > **Catalogs** (Paramètres de données > Catalogues)                                      |
| Contenu connecté             | **Settings** > **Workspace Settings** > **Connected Content** (Paramètres > Paramètres d’espace de travail > Contenu connecté)         |
| Bibliothèque de blocs de contenu        | **Templates** > **Content Blocks** (Modèles > Modèles de bloc de contenu)                                    |
| Conversions                   | **Analytics** > **Analytics Dashboards** > **Conversions** (Analyses > Tableaux de bord analytiques > Conversions)            |
| Currents                      | **Partner Integrations** > **Data Export (Currents)** (Intégrations de partenaires > Exportation de données (Currents))                 |
| Attributs personnalisés             | **Data Settings** > **Custom User Attributes** (Paramètres de données > Attributs utilisateur personnalisés)                        |
| Évènements personnalisés (rapport)        | **Analytics** > **Reports** > **Custom Events Reports** (Analyses > Rapports > Rapports d’événements personnalisés)               |
| Événements personnalisés                 | **Data Settings** > **Custom User Events** (Paramètres de données > Événements utilisateur personnalisés)                            |
| Data Feeds                    | **Data Settings** > **Data Feeds** (Paramètres de données > Data Feeds)                                    |
| Developer Console             | **Settings** > **Workspace Setup and Testing** (Paramètres > Configuration d’espace de travail et Tests)                        |
| Appareils et Opérateurs            | **Analytics** > **Reports** > **Devices and Carriers** (Analyses > Rapports > Appareils et opérateurs)                |
| Performances e-mail             | **Analytics** > **Analytics Dashboards** > **Email Performance** (Analyses > Tableaux de bord analytiques > Performances e-mail)      |
| Paramètres d’e-mail                | **Settings** > **Workspace Settings** > **Email Preferences** (Paramètres > Paramètres d’espace de travail > Préférences e-mail)         |
| Modèles d’e-mail               | **Templates** > **Email Templates** (Modèles > Modèles d’e-mail)                                   |
| Engagement Reports            | **Analytics** > **Reports** > **Engagement** (Analytises > Rapports > Engagement)                          |
| Journal d’événements utilisateurs                | **Settings** > **Workspace Setup and Testing** > **Event User Log** (Paramètres > Configuration d’espace de travail et Tests > Journal d'événements utilisateurs)   |
| Indicateurs de fonctionnalité                 | **Audience** > **Feature Flags** (Audience > Indicateurs de fonctionnalité)                                      |
| Global Control (rapport)       | **Analytics** > **Reports** > **Global Control** (Analyses > Rapports > Global Control)                      |
| Paramètres Groupe de contrôle global | **Audience** > **Global Control Group** (Audience > Groupe de contrôle global)                               |
| Modèles de message In-App      | **Templates** > **In-App Message Templates** (Modèles > Modèles de messages in-app)                            |
| Groupes internes               | **Settings** > **Workspace Setup and Testing** > **Internal Groups** (Paramètres > Configuration d’espace de travail et Tests > Groupes internes)  |
| Modèles de liens                | **Templates** > **Email Link Templates** (Modèles > Modèles de lien d’e-mail)                              |
| Locations                     | **Audience** > **Locations**                                          |
| Gérer les paramètres               | **Settings** > **Workspace Settings** (Paramètres > Paramètres d’espace de travail)                                 |
| Gérer les Teams                  | **Settings** > **Workspace Settings** > **Internal Teams** (Paramètres > Paramètres d’espace de travail > Équipes internes)            |
| Bibliothèque multimédia                 | **Templates** > **Media Library** (Modèles > Bibliothèque multimédia)                                     |
| Journal des activités de message          | **Settings** > **Workspace Setup and Testing** > **Message Activity** (Paramètres > Configuration d’espace de travail et Tests > Activité de message) |
| Fil d’actualité                     | **Messaging** > **News Feed** (Envoi de messages > Fil d'actualité)                                         |
| Aperçu                      | **Accueil**                                                              |
| Prédictions                   | **Analytics** > **Predictions** (Analyses > Prédictions)                                       |
| Produits                      | **Data Settings** > **Products** (Paramètres de données > Produits)                                      |
| Promotion Codes               | **Data Settings** > **Promotion Codes** (Paramètres de données > Codes  de promotion)                               |
| Paramètres TTL (Durée de vie) de notification push             | **Settings** > **Workspace Settings** > **Push Time-To-Live (TTL)** (Paramètres > Paramètres d’espace de travail > TTL (Durée de vie) notification push)   |
| Créateur de rapports                | **Analytics** > **Reports** > **Report Builder** (Analyses > Rapports > Créateur de rapports)                      |
| Revenue                       | **Analytics** > **Reports** > **Revenue** (Analyses > Rapports > Chiffre d'affaires)                             |
| Segments                      | **Audience** > **Segments** (Audience > Segments)                                           |
| Segment Extensions            | **Audience** > **Segment Extensions**                                 |
| Segment Insights              | **Analytics** > **Reports** > **Segment Insights** (Analyses > Rapports > Segment Insights)                    |
| Global Message Settings       | **Settings** > **Workspace Settings** > **Message Frequency** (Paramètres > Paramètres d’espace de travail > Fréquence des messages)         |
| Performances SMS               | **Analytics** > **Analytics Dashboards** > **Email Performance** (Analyses > Tableaux de bord analytiques > Performances SMS)        |
| Gestion de groupe d’abonnement | **Audience** > **Subscription** > **Subscription Groups** (Audience > Abonnement > Groupes d'abonnement)             |
| Groupes d’abonnement           | **Audience** > **Subscription** > **Subscription Groups** (Audience > Abonnement > Groupes d'abonnement)             |
| Balises                          | **Settings** > **Workspace Settings** > **Tag Management** (Paramètres > Paramètres d’espace de travail > Gestion des balises)            |
| Technology Partners           | **Partner Integrations** > **Technology Partner Integrations** (Intégrations de partenaires > Intégrations de partenaires technologiques)        |
| User Import                   | **Audience** > **Import Users** (Audience > Importer des utilisateurs)                                       |
| User Search                   | **Audience** > **Search Users** (Audience > Rechercher des utilisateurs)                                       |
| Modèles de webhook             | **Templates** > **Webhook Templates** (Modèles > Modèles de webhook)                                 |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}