---
nav_title: Centre de livrabilité
article_title: Centre de livrabilité
page_order: 4
description: "Cet article de référence explique comment configurer le centre de livrabilité, une fonctionnalité qui permet aux marketeurs de visualiser leurs domaines d'envoi d'e-mails et leurs réputations IP et de comprendre la livrabilité de leurs e-mails."
channel:
  - email

---

# Centre de livrabilité

> Le centre de livrabilité vous permet de mieux comprendre les performances de vos e-mails en prenant en charge l'utilisation des [outils Gmail Postmaster Tools](https://www.gmail.com/postmaster/) pour suivre les données sur les e-mails envoyés et recueillir des données sur votre domaine d'envoi.

La livrabilité des e-mails est au cœur de la réussite d'une campagne. Grâce au Centre de livrabilité du tableau de bord de Braze, vous pouvez visualiser vos domaines par **réputation IP** ou **erreurs de réception/distribution** afin de découvrir et de résoudre tout problème potentiel de livrabilité des e-mails. 

Pour accéder au Centre de livrabilité, vous devez disposer des [autorisations utilisateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) « Accéder aux campagnes, aux canvas, aux cartes, aux segments, à la bibliothèque multimédia » et « Afficher les données d’utilisation ».

## Configuration de votre compte Google Postmaster

Avant de vous connecter au Centre de livrabilité, vous devez créer un compte Google Postmaster Tools. Vous pouvez utiliser un compte Gmail professionnel ou personnel pour configurer votre Google Postmaster. 

1. Accédez au [tableau de bord de Google Postmaster Tools](https://postmaster.google.com/managedomains?pli=1).
2. En bas à droite, sélectionnez l'icône <i class="fas fa-plus-circle"></i> plus.
3. Saisissez votre domaine ou sous-domaine racine pour authentifier votre e-mail. Si vous ajoutez et vérifiez le domaine racine, cela permettra d'appliquer la vérification en aval aux sous-domaines. Par exemple, en vérifiant `braze.com`, vous pouvez ensuite ajouter `demo.braze.com` et d'autres sous-domaines sans devoir les vérifier individuellement.
4. Google génère un enregistrement TXT qui peut être ajouté directement aux DNS de votre domaine. Il appartient généralement à la personne qui gère votre DNS. Pour obtenir des informations et des conseils sur la manière de mettre à jour votre DNS spécifique, consultez [Vérifier votre domaine (étapes spécifiques à l'hôte)](https://support.google.com/a/topic/1409901).
5. Sélectionnez **Suivant.** <br>![Un exemple de domaine "demo.braze.com" pour authentifier un e-mail.]({% image_buster /assets/img_archive/domain_authentication.png %})
6. Une fois l'enregistrement TXT ajouté aux DNS, retournez dans le tableau de bord de Google Postmaster Tools et sélectionnez **Vérifier.** Cette étape confirme que vous êtes propriétaire du domaine, ce qui vous permettra d'accéder aux indicateurs de livrabilité de Gmail dans votre compte Postmaster. <br> ![Demande de vérification de la propriété du domaine "demo.braze.com".]({% image_buster /assets/img_archive/domain_verification.png %})

{% alert tip %}
Assurez-vous que l'enregistrement TXT est lié au domaine parent, et non au sous-domaine que vous utilisez par l'intermédiaire de Braze.
{% endalert %}

{% alert note %}
Si vos sous-domaines ne sont pas inclus dans le centre de livrabilité de Google Postmaster, cela peut être dû au fait que vous n'avez ajouté que le domaine parent à Google Postmaster. Une fois les domaines parents vérifiés dans Google Postmaster, vous pouvez ajouter vos sous-domaines, qui seront vérifiés automatiquement. Ce processus permet à Google de fournir des indicateurs au niveau du sous-domaine, qui peuvent ensuite être intégrés dans le Centre de livrabilité de Braze.
{% endalert %}

## Intégration de Google Postmaster

Avant de configurer votre centre de livrabilité, vérifiez que vos domaines ont été [ajoutés aux outils Postmaster de Gmail](https://support.google.com/mail/answer/9981691?hl=en).

Pour intégrer Google Postmaster et configurer votre Centre de livrabilité, procédez comme suit :

1. Sélectionnez **Analyse** > **Performances des e-mails**.
2. Sélectionnez l'onglet **Centre de livrabilité**. <br>![Un centre de livrabilité avec Google Postmaster non connecté.]({% image_buster /assets/img_archive/deliverability_center1.png %})
3. Sélectionnez **Connecter avec Google Postmaster**. 
4. Sélectionnez votre compte Google, puis sélectionnez **Autoriser** pour permettre à Braze d'afficher les indicateurs de trafic e-mail pour les domaines enregistrés avec les Outils Postmaster. 

Vos domaines vérifiés s'afficheront dans le centre de livrabilité. 

![Deux domaines vérifiés pour Google Postmaster avec une réputation moyenne et faible.]({% image_buster /assets/img_archive/deliverability_center2.png %})

Vous pouvez également accéder à Google Postmaster dans le tableau de bord de Braze en allant dans **Intégrations partenaires** > **Partenaires technologiques** > **Google Postmaster**. Après l'intégration, Braze extrait les données de réputation et d'erreur des 30 derniers jours. Il se peut que les données ne soient pas immédiatement disponibles et que leur insertion prenne plusieurs minutes.

### Indicateurs et définitions

Les indicateurs et définitions suivants s'appliquent à Google Postmaster Tools.

#### Réputation de l’adresse IP 

Pour vous aider à comprendre les évaluations de la réputation des adresses IP, reportez-vous à ce tableau :

| Notation de la réputation | Définition |
| ----- | ---------- |
| Élevée | a de bons antécédents en ce qui concerne le nombre de plaintes pour spam (par exemple, les utilisateurs qui cliquent sur le bouton "spam"). |
| Moyen/faible | Connu pour générer un engagement positif, mais reçoit occasionnellement des plaintes pour spam. La plupart des e-mails provenant de ce domaine seront envoyés dans la boîte de réception, sauf en cas d'augmentation des plaintes pour spam. |
| Faible | Connu pour recevoir régulièrement des taux élevés de plaintes pour spam. Les e-mails provenant de cet expéditeur seront probablement filtrés dans le dossier spam. |
| Mauvais | a l'habitude de recevoir des taux élevés de plaintes pour spam. Les e-mails provenant de ce domaine seront presque toujours rejetés au moment de la connexion ou filtrés vers le dossier spam. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Réputation du domaine 

Utilisez le tableau suivant pour surveiller et comprendre les évaluations de la réputation de votre domaine afin d'éviter l’envoi dans un dossier spam.

| Notation de la réputation | Définition |
| ----- | ---------- |
| Élevée | Il a de bons antécédents en ce qui concerne le nombre très faible de plaintes pour spam. Conforme aux directives de Gmail relatives aux expéditeurs. Les e-mails sont rarement filtrés vers le dossier spam. A un taux de spam très bas. Conforme aux [directives de Gmail relatives aux expéditeurs.](https://developers.google.com/gmail/markup/registering-with-google) |
| Moyen/faible | Connu pour générer un engagement positif mais a occasionnellement reçu un faible volume de plaintes pour spam. La plupart des e-mails provenant de ce domaine arriveront dans la boîte de réception (sauf en cas d'augmentation notable du nombre de spams). |
| Faible | Connu pour recevoir régulièrement des plaintes pour spam. Les e-mails provenant de cet expéditeur seront probablement filtrés dans le dossier spam. |
| Mauvais | a l'habitude de recevoir des taux élevés de plaintes pour spam. Les e-mails provenant de ce domaine seront presque toujours rejetés au moment de la connexion ou filtrés vers le dossier spam. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Authentification

Utilisez le tableau de bord de l'authentification pour examiner le pourcentage d'e-mails qui ont passé les tests SPF (Sender Policy Framework), DKIM (DomainKeys Identified Mail) et DMARC (Domain-based Message Authentication, Reporting and Conformance).

| Type de graphique | Définition |
| ----- | ---------- |
| SPF | Indique le pourcentage d'e-mails qui ont passé le contrôle SPF par rapport à tous les e-mails du domaine qui ont tenté le contrôle SPF. Ceci exclut tout e-mail usurpé. |
| DKIM | Indique le pourcentage d'e-mails qui ont passé la norme DKIM par rapport à tous les e-mails du domaine qui ont tenté la norme DKIM. |
| DMARC | Indique le pourcentage d'e-mails qui ont passé l'alignement DMARC par rapport à tous les e-mails reçus du domaine qui ont passé SPF ou DKIM. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Chiffrement

Consultez ce tableau pour savoir quel pourcentage de votre trafic entrant et sortant est crypté.

| Terme | Définition |
| ----- | ---------- |
| TLS entrant | Indique le pourcentage de courrier entrant (vers Gmail) qui a passé TLS par rapport à l'ensemble du courrier reçu de ce domaine. |
| TLS sortant | Indique le pourcentage de courrier sortant (de Gmail) accepté via TLS par rapport à l'ensemble du courrier envoyé à ce domaine. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour plus d'idées sur l'amélioration de la livrabilité, lisez les [pièges de la livrabilité et les pièges à spam]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/deliverability_pitfalls_and_spam_traps/#deliverability-pitfalls-and-spam-traps). N'oubliez pas de consulter nos [meilleures pratiques en matière d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/) pour connaître les éléments à vérifier avant d'envoyer une campagne d'e-mail.

## Configuration de Microsoft Smart Network Data Services (SNDS)

Si Microsoft est votre principal fournisseur de messagerie, vous pouvez utiliser cette intégration pour accéder à vos données de réputation Microsoft et les consulter. De cette façon, vous pouvez surveiller l’intégrité de vos adresses IP pour aider à déterminer comment vos e-mails sont reçus.

{% alert important %}
Si vous ne voyez pas vos données dans le Centre de livrabilité, contactez l’[assistance]({{site.baseurl}}/user_guide/administrative/access_braze/support/) avec une liste de vos adresses IP.
{% endalert %}

![Exemple de résultats de Microsoft SNDS, y compris des exemples d'adresses IP, de destinataires, de commandes RCPT, de commandes de données, de résultats de filtrage, de taux de plaintes, de début et de fin de la période des messages piégés et d'occurrences de messages piégés.]({% image_buster /assets/img_archive/deliverability_center_msnds.png %})

### Indicateurs et définitions

Les indicateurs suivants s'appliquent à Microsoft SNDS.

#### Destinataires

Cet indicateur fait référence au nombre de destinataires des messages transmis par l'IP.

#### Commandes DATA

Cette mesure indique le nombre de commandes DATA envoyées par l'IP. Les commandes DATA font partie du protocole SMTP utilisé pour envoyer des e-mails.

#### Filtrer les résultats

Reportez-vous à ce tableau pour comprendre les résultats du filtre 

| Résultat | Définition |
| ----- | ---------- |
| Vert | Jugé comme étant du spam par le filtre anti-spam de Microsoft jusqu'à 10 % de la période donnée. |
| Jaune | Jugé comme étant du spam par le filtre anti-spam de Microsoft entre 10 % et 90 % de la période donnée. |
| Rouge | Jugé comme étant du spam par le filtre anti-spam de Microsoft jusqu'à plus de 90 % de la période donnée.| 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Taux de réclamations

Pourcentage du temps qu’un message reçu de l’adresse IP fait l’objet d’une réclamation par un utilisateur de Hotmail ou Windows Live pendant la période d’activité. Les utilisateurs ont la possibilité de signaler la quasi-totalité des messages comme étant des messages indésirables via l'interface utilisateur web. 

Pour calculer le taux de réclamation, divisez le nombre de réclamations par le nombre de destinataires du message.  

| Résultat | Définition |
| ----- | ---------- |
| Moins de 0,3 | Taux de réclamations idéal. |
| Plus de 0,3 | Passez en revue votre processus d'inscription et assurez-vous que votre lien de désabonnement fonctionne. Réfléchissez également à la possibilité de mieux personnaliser le courrier en fonction de votre audience. |
| Plus de 100 | Notez que SNDS affiche les réclamations pour le jour où elles ont été signalées, et non pas rétroactivement par rapport au jour où l’e-mail faisant l'objet de la réclamation a été livré. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Comptes piégés touchés

Le nombre d'occurrences du piège à spam correspond au nombre de messages envoyés à des "comptes pièges", c'est-à-dire des comptes gérés par Outlook.com qui ne sollicitent aucun courrier. Il est probable que les messages envoyés à ces comptes pièges soient considérés comme du spam, il est donc important de surveiller cette mesure pour s'assurer qu'elle est faible. Si le nombre d'occurrences du piège à spam est faible, cela signifie que les messages ne sont pas envoyés à ces comptes et qu'ils sont plutôt envoyés à des comptes réels.

{% alert tip %}
Si vous recherchez des enregistrements liés à l'un de vos domaines vérifiés dans Braze, notez que le Centre de livrabilité répertorie vos données à partir de Google Postmaster ou de Microsoft SNDS, ce qui signifie qu'il est probable que l'une ou l'autre plateforme n'ait pas de données à partager avec Braze. Par ailleurs, nous vous suggérons de maintenir une réception/distribution régulière des e-mails, ce qui peut vous permettre d'améliorer votre réputation.
{% endalert %}


