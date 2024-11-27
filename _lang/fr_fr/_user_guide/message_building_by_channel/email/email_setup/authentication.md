---
nav_title: Authentification par e-mail
article_title: Authentification par e-mail
page_order: 2
page_type: reference
description: "Le présent article de référence couvre l’authentification par e-mail, un ensemble de techniques visant à équiper votre e-mail d’informations vérifiables sur son origine."
channel: email

---

# Authentification par e-mail

> L’authentification par e-mail est un ensemble de techniques visant à équiper votre e-mail d’informations vérifiables sur son origine.<br><br>Une authentification correcte est primordiale pour que les fournisseurs de services Internet (ISP) reconnaissent votre qualité d’expéditeurs d’e-mails utiles et les livre immédiatement. Sans authentification, votre communication est présumée frauduleuse. 

## Méthodes d’authentification

### Cadre de politique de l’expéditeur (SPF)

Cette méthode confirme que votre adresse IP d’envoi d’e-mail Braze est autorisée à envoyer un courrier en votre nom. SPF est votre authentification de base et est réalisée en publiant les enregistrements de texte dans les paramètres DNS. Le serveur de réception vérifie les enregistrements DNS et détermine s’ils sont authentiques ou non. Cette méthode est conçue pour valider l’expéditeur de l’e-mail.

Votre enregistrement SPF sera configuré lorsque Braze configure vos IP et domaines ; au-delà de l’ajout des enregistrements DNS que nous vous fournissons, aucune autre action n’est requise.

### E-mail identifié des clés de domaine (DKIM)

Cette méthode confirme que votre domaine d’envoi d’e-mail Braze est autorisé à envoyer un courrier en votre nom. Cette méthode permet de valider l'authenticité de l'expéditeur et de s'assurer que l'intégrité du message est préservée. Elle utilise également des signatures numériques cryptographiques individuelles pour que les fournisseurs de services Internet puissent s’assurer que le courrier qu’ils délivrent est le même que celui que vous avez envoyé.

Braze signe le courrier avec votre clé privée secrète. Les fournisseurs de services Internet vérifient la signature de votre clé publique, qui est stockée dans votre dossier DNS personnalisé. Aucune signature n’est exactement identique et, seule votre clé publique peut vérifier avec succès votre signature clé privée.

Votre enregistrement DKIM sera configuré lorsque Braze configure vos adresses IP et domaines. Au-delà de l’ajout des enregistrements DNS que nous vous fournissons, aucune autre action n’est requise.

### Authentification, reporting et conformité des messages basés sur les domaines (DMARC)

Le protocole [DMARC (Domain-based Message Authentication, Reporting & Conformance)](https://dmarc.org/) est un protocole d'authentification des e-mails permettant aux expéditeurs de prouver la légitimité de leur courrier, ce qui renforce la confiance des destinataires et encourage l'acceptation des e-mails. DMARC permet aux expéditeurs d'e-mails de spécifier comment traiter les e-mails qui n'ont pas été authentifiés à l'aide de Sender Policy Framework (SPF) ou Domain Keys Identified Mail (DKIM). Pour ce faire, il faut vérifier que les contrôles SPF et DKIM sont réussis. 

Les expéditeurs peuvent indiquer aux fournisseurs de boîtes aux lettres comment traiter les courriers dont la signature ou l'authentification n'a pas été vérifiée. Les échecs peuvent indiquer que d’autres essaient de vous imiter, vous ou votre e-mail. Les expéditeurs peuvent demander aux fournisseurs de boîtes aux lettres de rejeter ou de mettre en quarantaine le courrier et même d'envoyer des rapports automatisés sur les courriers qui ne passent pas les contrôles. Ce faisant, les fournisseurs de boîtes aux lettres peuvent mieux identifier les expéditeurs de courrier indésirable et empêcher les e-mails malveillants d'envahir les boîtes de réception tout en minimisant les faux positifs et en fournissant de meilleurs rapports d'authentification pour une plus grande transparence sur le marché.

#### Fonctionnement

Pour déployer DMARC, vous devez publier un enregistrement DMARC dans votre Domain Naming System (DNS). Il s'agit d'un enregistrement TXT qui exprime publiquement la politique de votre domaine e-mail après vérification des statuts SPF et DKIM. DMARC authentifie si SPF ou DKIM, ou les deux, sont acceptés. C'est ce qu'on appelle l'alignement DMARC.

Un enregistrement DMARC indique également aux serveurs de messagerie de renvoyer des rapports XML à l'adresse e-mail de rapport indiquée dans l'enregistrement DMARC. Ces rapports fournissent des informations sur la manière dont votre e-mail circule dans l'écosystème et vous permettent d'identifier tout ce qui tente d'utiliser votre domaine d'e-mail pour envoyer des communications par e-mail.

La politique que vous avez définie dans votre enregistrement DMARC indique au serveur d'e-mail du destinataire participant ce qu'il doit faire des e-mails qui ne passent pas les tests SPF et DKIM mais qui prétendent provenir de votre domaine. Braze recommande de définir une politique DMARC sur le domaine racine, qui sera appliquée à tous les sous-domaines. Cela signifie qu'aucune configuration supplémentaire ne sera nécessaire pour les sous-domaines actuels et les nouveaux sous-domaines à l'avenir. Vous pouvez définir trois types de politiques :

| Politique | Impact |
| --- | --- |
| Aucune | Indiquer au fournisseur de boîtes aux lettres de ne rien faire pour les messages qui échouent. |
| Quarantaine | Indiquer au fournisseur de boîtes aux lettres d'envoyer les messages qui échouent dans le dossier spam. |
| Rejeter | Indiquez au fournisseur de la boîte aux lettres que les messages qui échouent iront dans le dossier spam et devront être bloqués. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Comment vérifier l'authentification DMARC de votre domaine ?

Il existe deux options pour vérifier l'authentification DMARC de votre domaine :

- **Option 1 :** Vous pouvez saisir votre domaine ou sous-domaine parent dans un vérificateur DMARC tiers, tel que [MXToolbox](https://mxtoolbox.com/dmarc.aspx), afin de vérifier si vous avez mis en place une politique DMARC et quelle est la valeur de cette politique.
    - **MXToolbox**: Si vous avez défini votre DMARC comme étant le domaine racine, saisissez-le dans MXToolbox. Si vous avez défini le DMARC au niveau du sous-domaine, saisissez le sous-domaine dans MXToolbox. Sachez que MXToolbox ne regarde pas vers le haut ou vers le bas lorsqu'il effectue des recherches. Cela signifie que si vous configurez le DMARC au niveau du domaine racine et que vous saisissez le sous-domaine, MXToolbox affichera un échec car il ne sait pas que le DMARC a été configuré au niveau du domaine racine.
- **Option 2 :** Ouvrez un e-mail provenant de votre domaine ou sous-domaine dans votre boîte aux lettres, et recherchez le message original pour vérifier si DMARC passe l'authentification sur cet e-mail.

Par exemple, si vous utilisez Gmail, procédez comme suit :

1. Cliquez sur le bouton **Plus** <i class="fa-solid fa-ellipsis"></i> dans un message e-mail.
2. Sélectionnez **Afficher l'original**.
3. Vérifiez si vous avez un statut « PASS » pour **DMARC**.

![Un e-mail dont la valeur DMARC est « PASS ».]({% image_buster /assets/img_archive/dmarc_example.png %})

