---
nav_title: Authentification par e-mail
article_title: Authentification par e-mail
page_order: 2
page_type: reference
description: "Cet article de référence traite de l'authentification des e-mails, un ensemble de techniques visant à doter votre e-mail d'informations vérifiables sur son origine."
channel: email

---

# Authentification par e-mail

> L'authentification des e-mails est un ensemble de techniques qui permettent de fournir à vos e-mails des informations vérifiables sur leur origine.<br><br>Une authentification correcte est essentielle pour que les fournisseurs de services Internet (ISP) vous reconnaissent comme expéditeur d'e-mails souhaités et vous délivrent votre courrier immédiatement. Sans authentification, votre communication est présumée frauduleuse. 

## Méthodes d'authentification

### Cadre de politique d'expéditeur (SPF)

Cette méthode confirme que votre adresse IP d'envoi d'e-mails de Braze est autorisée à envoyer des e-mails en votre nom. SPF est votre authentification de base et est réalisée en publiant les enregistrements de texte dans les paramètres DNS. Le serveur de réception vérifiera les enregistrements DNS et déterminera s'ils sont authentiques. Cette méthode est conçue pour valider l'expéditeur de l'e-mail.

Votre enregistrement SPF sera mis en place lorsque Braze configurera vos IP et vos domaines - en dehors de l'ajout des enregistrements DNS que nous vous donnons, aucune autre action n'est requise.

### Courrier identifié par une clé de domaine (DKIM)

Cette méthode confirme que votre domaine d'envoi d'e-mails de Braze est autorisé à envoyer des e-mails en votre nom. Cette méthode permet de valider l'authenticité de l'expéditeur et de s'assurer que l'intégrité du message est préservée. Il utilise également des signatures numériques cryptographiques individuelles pour que les FAI puissent être sûrs que le courrier qu'ils distribuent est le même que celui que vous avez envoyé.

Braze signe le courrier avec votre clé privée secrète. Les FAI vérifient la signature par rapport à votre clé publique, qui est stockée dans votre enregistrement DNS personnalisé. Il n'y a pas deux signatures identiques, et seule votre clé publique peut vérifier avec succès la signature de votre clé privée.

Votre enregistrement DKIM sera mis en place lorsque Braze configurera vos IP et vos domaines. Outre l'ajout des enregistrements DNS que nous vous fournissons, aucune autre action n'est requise.

### Authentification, notification et conformité des messages par domaine (DMARC)

[Domain-based Message Authentication, Reporting & Conformance (DMARC)](https://dmarc.org/) est un protocole d'authentification des e-mails permettant aux expéditeurs de prouver la légitimité de leur courrier, ce qui renforce la confiance des destinataires et encourage l'acceptation des e-mails. DMARC permet aux expéditeurs d'e-mails de spécifier comment traiter les e-mails qui n'ont pas été authentifiés à l'aide de Sender Policy Framework (SPF) ou Domain Keys Identified Mail (DKIM). Pour ce faire, il faut vérifier que les contrôles SPF et DKIM sont réussis. 

Les expéditeurs peuvent indiquer aux fournisseurs de boîtes aux lettres comment traiter les courriers dont la signature ou l'authentification n'a pas été vérifiée. Les échecs peuvent indiquer que d'autres tentent de vous imiter ou d'imiter votre e-mail. Les expéditeurs peuvent demander aux fournisseurs de boîtes aux lettres de rejeter ou de mettre en quarantaine le courrier et même d'envoyer des rapports automatisés sur les courriers qui ne passent pas les contrôles. Ce faisant, les fournisseurs de boîtes aux lettres peuvent mieux identifier les expéditeurs de courrier indésirable et empêcher les e-mails malveillants d'envahir les boîtes de réception tout en minimisant les faux positifs et en fournissant de meilleurs rapports d'authentification pour une plus grande transparence sur le marché.

#### Comment cela fonctionne-t-il ?

Pour déployer DMARC, vous devez publier un enregistrement DMARC dans votre Domain Naming System (DNS). Il s'agit d'un enregistrement TXT qui exprime publiquement la politique de votre domaine e-mail après vérification des statuts SPF et DKIM. DMARC authentifie si SPF ou DKIM, ou les deux, sont acceptés. C'est ce qu'on appelle l'alignement DMARC.

Un enregistrement DMARC indique également aux serveurs d'e-mail d'envoyer des rapports XML à l'adresse e-mail de rapport indiquée dans l'enregistrement DMARC. Ces rapports fournissent des informations sur la façon dont votre e-mail circule dans l'écosystème et vous permettent d'identifier tout ce qui tente d'utiliser votre domaine d'e-mail pour envoyer des communications par e-mail.

La politique que vous avez définie dans votre enregistrement DMARC indique au serveur d'e-mail du destinataire participant ce qu'il doit faire des e-mails qui ne passent pas les tests SPF et DKIM mais qui prétendent provenir de votre domaine. Braze recommande de définir une politique DMARC sur le domaine racine, qui sera appliquée à tous les sous-domaines. Cela signifie qu'aucune configuration supplémentaire ne sera nécessaire pour les sous-domaines actuels et les nouveaux sous-domaines à l'avenir. Vous pouvez définir trois types de politiques :

| Politique | Impact |
| --- | --- |
| Aucun | Indiquez au fournisseur de la boîte aux lettres de ne rien faire pour les messages qui échouent. |
| Quarantaine | Indiquez au fournisseur de la boîte aux lettres d'envoyer les messages qui échouent dans le dossier spam. |
| Rejeter | Indiquez au fournisseur de la boîte aux lettres que les messages qui échouent iront dans le dossier spam et devront être bloqués. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Comment vérifier l'authentification DMARC de votre domaine ?

Il existe deux options pour vérifier l'authentification DMARC de votre domaine :

- **Option 1 :** Vous pouvez saisir votre domaine ou sous-domaine parent dans un vérificateur DMARC tiers, tel que [MXToolbox](https://mxtoolbox.com/dmarc.aspx), afin de vérifier si vous avez mis en place une politique DMARC et quelle est la valeur de cette politique.
    - **MXToolbox**: Si vous avez défini votre DMARC comme étant le domaine racine, saisissez-le dans MXToolbox. Si vous avez défini le DMARC au niveau du sous-domaine, saisissez le sous-domaine dans MXToolbox. Sachez que MXToolbox ne regarde pas vers le haut ou vers le bas lorsqu'il effectue des recherches. Cela signifie que si vous configurez le DMARC au niveau du domaine racine et que vous saisissez le sous-domaine, MXToolbox affichera un échec car il ne sait pas que le DMARC a été configuré au niveau du domaine racine.
- **Option 2 :** Ouvrez un e-mail provenant de votre domaine ou sous-domaine dans votre boîte aux lettres, et recherchez le message original pour vérifier si DMARC passe l'authentification sur cet e-mail.

Par exemple, si vous utilisez Gmail, procédez comme suit :

1. Cliquez sur le bouton **Plus** <i class="fa-solid fa-ellipsis"></i> dans un message e-mail.
2. Sélectionnez **Afficher l'original**.
3. Vérifiez si vous avez un statut "PASS" pour **DMARC**.

\![Un e-mail dont la valeur DMARC est "PASS".]({% image_buster /assets/img_archive/dmarc_example.png %})

