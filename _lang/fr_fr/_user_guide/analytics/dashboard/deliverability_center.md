---
nav_title: Centre de livrabilité
article_title: Centre de livrabilité
alias: "/deliverability_center/"
page_order: 4
description: "Cet article de référence explique comment configurer le centre de livrabilité, une fonctionnalité qui permet aux marketeurs de visualiser leurs domaines d'envoi d'e-mails et leurs réputations IP et de comprendre la livrabilité de leurs e-mails."
channel:
  - email

---

# Centre de livrabilité

> Le centre de livrabilité vous permet de mieux comprendre les performances de vos e-mails en prenant en charge l'utilisation des [outils Gmail Postmaster Tools](https://www.gmail.com/postmaster/) pour suivre les données sur les e-mails envoyés et recueillir des données sur votre domaine d'envoi.

La livrabilité des e-mails est au cœur de la réussite d'une campagne. Grâce au Centre de livrabilité du tableau de bord de Braze, vous pouvez visualiser vos domaines par **réputation IP** ou **erreurs de distribution** afin de découvrir et de résoudre tout problème potentiel de livrabilité des e-mails. 

Pour accéder au Centre de livrabilité, vous devez disposer des [autorisations utilisateur héritées]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=legacy%20permissions) « Accéder aux campagnes, aux Canvas, aux cartes, aux segments et à la bibliothèque multimédia » et « Afficher les données d'utilisation », ou des [autorisations granulaires]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?sdktab=granular%20permissions) dans le menu déroulant suivant pour votre espace de travail.

{% details Autorisations utilisateur pour le Centre de livrabilité %}

{% multi_lang_include deprecations/user_permissions.md %}

- Afficher les campagnes
- Modifier les campagnes
- Archiver les campagnes
- Afficher les Canvas
- Modifier les Canvas
- Archiver les Canvas
- Afficher les règles de limite de fréquence
- Modifier les règles de limite de fréquence
- Afficher l'ordre de priorité des messages
- Modifier l'ordre de priorité des messages
- Afficher les blocs de contenu
- Afficher les indicateurs de fonctionnalité
- Modifier les indicateurs de fonctionnalité
- Archiver les indicateurs de fonctionnalité
- Afficher les segments
- Modifier les segments
- Afficher les modèles IAM
- Modifier les modèles IAM
- Archiver les modèles IAM
- Afficher les modèles d'e-mail
- Modifier les modèles d'e-mail
- Archiver les modèles d'e-mail
- Afficher les modèles de webhook
- Modifier les modèles de webhook
- Archiver les modèles de webhook
- Afficher les modèles de lien d'e-mail
- Modifier les modèles de lien d'e-mail
- Afficher les ressources de la bibliothèque multimédia
- Modifier les ressources de la bibliothèque multimédia
- Supprimer les ressources de la bibliothèque multimédia
- Afficher les emplacements
- Modifier les emplacements
- Archiver les emplacements
- Consulter les codes de promotion
- Modifier les codes de promotion
- Exporter les codes de promotion
- Afficher les centres de préférences
- Modifier les centres de préférences
- Consulter les rapports
- Modifier les rapports
- Afficher les données d'utilisation

{% enddetails %}

## Configuration de votre compte Google Postmaster

Avant de vous connecter au Centre de livrabilité, vous devez créer un compte Google Postmaster Tools. Vous pouvez utiliser un compte Gmail professionnel ou personnel pour configurer votre compte Google Postmaster. 

1. Accédez au [tableau de bord de Google Postmaster Tools](https://postmaster.google.com/managedomains?pli=1).
2. En bas à droite, sélectionnez l'icône <i class="fas fa-plus-circle"></i> plus.
3. Saisissez votre domaine racine (parent) pour authentifier votre e-mail. Assurez-vous que l'enregistrement TXT est associé à ce domaine racine (parent), et **non** au sous-domaine que vous utilisez via Braze. La vérification du domaine racine (parent) vous permet d'ajouter ultérieurement des sous-domaines dans Postmaster Tools sans créer d'enregistrements TXT supplémentaires. Par exemple, en vérifiant `braze.com`, vous pourrez ensuite ajouter `demo.braze.com` comme sous-domaine distinct dans Postmaster Tools pour consulter les indicateurs au niveau du sous-domaine.
4. Google génère un enregistrement TXT qui peut être ajouté directement au DNS de votre domaine. Il appartient généralement à la personne qui gère votre DNS. Pour obtenir des informations et des conseils sur la manière de mettre à jour votre DNS spécifique, consultez [Vérifier votre domaine (étapes spécifiques à l'hôte)](https://support.google.com/a/topic/1409901).
5. Sélectionnez **Suivant**. <br>![Un exemple de domaine « demo.braze.com » pour authentifier un e-mail.]({% image_buster /assets/img_archive/domain_authentication.png %})
6. Une fois l'enregistrement TXT ajouté au DNS, retournez dans le tableau de bord de Google Postmaster Tools et sélectionnez **Vérifier**. Cette étape permet de confirmer que vous êtes bien le propriétaire du domaine, afin que vous puissiez accéder aux indicateurs de livrabilité Gmail dans votre compte Postmaster. <br> ![Une invite vous demandant de vérifier que vous êtes bien le propriétaire du domaine « demo.braze.com ».]({% image_buster /assets/img_archive/domain_verification.png %})

{% alert note %}
Si vos sous-domaines ne sont pas inclus dans le Centre de livrabilité pour Google Postmaster, cela peut être dû au fait que vous n'avez ajouté que le domaine racine (parent) à Google Postmaster. Une fois les domaines racines vérifiés dans Google Postmaster, vous pouvez ajouter vos sous-domaines, qui seront vérifiés automatiquement. Ce processus permet à Google de fournir des indicateurs au niveau du sous-domaine, qui peuvent ensuite être intégrés dans le Centre de livrabilité de Braze.
{% endalert %}

## Intégration de Google Postmaster

Avant de configurer votre Centre de livrabilité, vérifiez que vos domaines ont été [ajoutés aux outils Postmaster de Gmail](https://support.google.com/mail/answer/9981691?hl=en).

Pour intégrer Google Postmaster et configurer votre Centre de livrabilité, procédez comme suit :

1. Accédez à **Analyse** > **Performances des e-mails**.
2. Sélectionnez l'onglet **Centre de livrabilité**. <br>![Un Centre de livrabilité non connecté à Google Postmaster.]({% image_buster /assets/img_archive/deliverability_center1.png %})
3. Sélectionnez **Connecter avec Google Postmaster**. 
4. Sélectionnez votre compte Google, puis sélectionnez **Autoriser** pour permettre à Braze d'afficher les indicateurs de trafic e-mail pour les domaines enregistrés avec les outils Postmaster. 

Vos domaines vérifiés apparaissent dans le Centre de livrabilité. 

![Deux domaines vérifiés pour Google Postmaster avec une réputation moyenne et faible.]({% image_buster /assets/img_archive/deliverability_center2.png %})

Vous pouvez également accéder à Google Postmaster dans le tableau de bord de Braze en allant dans **Intégrations partenaires** > **Partenaires technologiques** > **Google Postmaster**. Après l'intégration, Braze extrait les données de réputation et d'erreur des 30 derniers jours. Il se peut que les données ne soient pas immédiatement disponibles et que leur chargement prenne plusieurs minutes.

### Indicateurs et définitions

Les indicateurs et définitions suivants s'appliquent à Google Postmaster Tools.

#### Réputation de l'adresse IP 

Pour vous aider à comprendre les évaluations de la réputation des adresses IP, reportez-vous à ce tableau :

| Notation de la réputation | Définition |
| ----- | ---------- |
| Élevée | A de bons antécédents en matière de faible taux de plaintes pour spam (par exemple, les utilisateurs qui cliquent sur le bouton « spam »). |
| Moyenne/Correcte | Connu pour générer un engagement positif, mais reçoit occasionnellement des plaintes pour spam. La plupart des e-mails provenant de ce domaine sont acheminés vers la boîte de réception, sauf lorsque les signalements de spam augmentent. |
| Faible | Connu pour recevoir régulièrement des taux élevés de plaintes pour spam. Les e-mails provenant de cet expéditeur sont susceptibles d'être filtrés vers le dossier spam. |
| Mauvaise | A l'habitude de recevoir des taux élevés de plaintes pour spam. Les e-mails provenant de ce domaine sont généralement rejetés lors de la connexion ou redirigés vers le dossier spam. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Réputation du domaine 

Utilisez le tableau suivant pour surveiller et comprendre les évaluations de la réputation de votre domaine afin d'éviter d'être filtré dans un dossier spam.

| Notation de la réputation | Définition |
| ----- | ---------- |
| Élevée | A de bons antécédents en matière de très faible taux de plaintes pour spam. Conforme aux directives de Gmail relatives aux expéditeurs. Les e-mails sont rarement filtrés dans le dossier spam. A un taux de spam très bas. Conforme aux [directives de Gmail relatives aux expéditeurs](https://developers.google.com/gmail/markup/registering-with-google). |
| Moyenne/Correcte | Connu pour générer un engagement positif, mais a parfois fait l'objet d'un faible nombre de plaintes pour spam. La plupart des e-mails provenant de ce domaine parviennent dans la boîte de réception (sauf en cas d'augmentation significative du niveau de spam). |
| Faible | Connu pour recevoir régulièrement des plaintes pour spam. Les e-mails provenant de cet expéditeur sont susceptibles d'être filtrés vers le dossier spam. |
| Mauvaise | A l'habitude de recevoir des taux élevés de plaintes pour spam. Les e-mails provenant de ce domaine sont généralement rejetés lors de la connexion ou redirigés vers le dossier spam. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Authentification

Utilisez le tableau de bord de l'authentification pour examiner le pourcentage d'e-mails ayant passé avec succès les contrôles SPF (Sender Policy Framework), DKIM (DomainKeys Identified Mail) et DMARC (Domain-based Message Authentication, Reporting and Conformance).

| Type de graphique | Définition |
| ----- | ---------- |
| SPF | Indique le pourcentage d'e-mails ayant passé le contrôle SPF par rapport à tous les e-mails du domaine ayant tenté le contrôle SPF. Les e-mails usurpés sont exclus. |
| DKIM | Indique le pourcentage d'e-mails ayant passé le contrôle DKIM par rapport à tous les e-mails du domaine ayant tenté le contrôle DKIM. |
| DMARC | Indique le pourcentage d'e-mails ayant passé l'alignement DMARC par rapport à tous les e-mails reçus du domaine ayant passé SPF ou DKIM. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Chiffrement

Consultez ce tableau pour savoir quel pourcentage de votre trafic entrant et sortant est chiffré.

| Terme | Définition |
| ----- | ---------- |
| TLS entrant | Indique le pourcentage de courrier entrant (vers Gmail) ayant passé le contrôle TLS par rapport à l'ensemble du courrier reçu de ce domaine. |
| TLS sortant | Indique le pourcentage de courrier sortant (de Gmail) accepté via TLS par rapport à l'ensemble du courrier envoyé à ce domaine. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour plus d'idées sur l'amélioration de la livrabilité, lisez [Pièges de la livrabilité et pièges à spam]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/deliverability_pitfalls_and_spam_traps/#deliverability-pitfalls-and-spam-traps). N'oubliez pas de consulter nos [bonnes pratiques en matière d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/) pour connaître les éléments à vérifier avant d'envoyer une campagne d'e-mail.

## Configuration de Microsoft Smart Network Data Services (SNDS)

Si Microsoft est votre principal fournisseur de messagerie, vous pouvez utiliser cette intégration pour accéder à vos données de réputation Microsoft et les consulter. Vous pourrez ainsi surveiller l'état de vos adresses IP pour mieux comprendre comment vos e-mails sont reçus.

{% alert important %}
Si vous ne voyez pas vos données dans le Centre de livrabilité, contactez l'[assistance]({{site.baseurl}}/user_guide/administrative/access_braze/support/) en fournissant la liste de vos adresses IP.
{% endalert %}

![Exemple de résultats fournis par Microsoft SNDS, comprenant des exemples d'adresses IP, de destinataires, de commandes RCPT, de commandes DATA, de résultats de filtrage, de taux de plaintes, de début et de fin de période de messages pièges et de résultats de pièges à spam.]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### Indicateurs et définitions

Les indicateurs suivants s'appliquent à Microsoft SNDS.

#### Destinataires

Cet indicateur correspond au nombre de destinataires des messages transmis par l'adresse IP.

#### Commandes DATA

Cet indicateur suit le nombre de commandes DATA envoyées par l'adresse IP. Les commandes DATA font partie du protocole SMTP utilisé pour envoyer des e-mails.

#### Résultats du filtrage

Reportez-vous à ce tableau pour comprendre les résultats du filtrage.

| Résultat | Définition |
| ----- | ---------- |
| Vert | Jugé comme spam par le filtre anti-spam de Microsoft pour moins de 10 % de la période donnée. |
| Jaune | Jugé comme spam par le filtre anti-spam de Microsoft entre 10 % et 90 % de la période donnée. |
| Rouge | Jugé comme spam par le filtre anti-spam de Microsoft pour plus de 90 % de la période donnée.| 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Taux de réclamations

Il s'agit de la proportion de messages reçus depuis l'adresse IP qui font l'objet d'une réclamation par un utilisateur Hotmail ou Windows Live pendant la période d'activité. Les utilisateurs ont la possibilité de signaler la quasi-totalité des messages comme indésirables via l'interface web. 

Pour calculer le taux de réclamations, divisez le nombre de réclamations par le nombre de destinataires du message.  

| Résultat | Définition |
| ----- | ---------- |
| Moins de 0,3 % | Taux de réclamations idéal. |
| Plus de 0,3 % | Passez en revue votre processus d'inscription et assurez-vous que votre lien de désabonnement fonctionne. Vérifiez également si vos e-mails pourraient être davantage personnalisés pour votre audience. |
| Plus de 100 % | Notez que SNDS affiche les réclamations pour le jour où elles ont été signalées, et non rétroactivement par rapport au jour où l'e-mail faisant l'objet de la réclamation a été livré. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Comptes pièges touchés

Le nombre de comptes pièges touchés correspond au nombre de messages envoyés à des « comptes pièges », c'est-à-dire des comptes gérés par Outlook.com qui ne sollicitent aucun courrier. Les messages envoyés à ces comptes pièges sont très probablement considérés comme du spam. Il est donc important de surveiller cet indicateur pour s'assurer qu'il reste faible. Un faible nombre de comptes pièges touchés signifie que les messages ne sont pas envoyés à ces comptes et qu'ils sont bien acheminés vers des comptes réels.

{% alert tip %}
Si vous recherchez des enregistrements liés à l'un de vos domaines vérifiés dans Braze, notez que le Centre de livrabilité répertorie vos données provenant de Google Postmaster ou de Microsoft SNDS, ce qui signifie qu'il est possible que l'une ou l'autre de ces plateformes ne dispose d'aucune donnée à partager avec Braze. Par ailleurs, nous vous recommandons de maintenir une distribution régulière des e-mails, ce qui peut contribuer à améliorer votre réputation. 
{% endalert %}