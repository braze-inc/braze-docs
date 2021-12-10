---
nav_title: Authentification par e-mail
article_title: Authentification par e-mail
page_order: 1
page_type: Référence
description: "Cet article de référence couvre l'authentification par e-mail, un ensemble de techniques visant à équiper votre e-mail d'informations vérifiables sur son origine."
channel: Email
---

# Authentification par e-mail

> L'authentification par courriel est un ensemble de techniques qui équipent vos e-mails d'informations vérifiables sur son origine.

Une authentification adéquate est cruciale pour que les FSI vous reconnaissent en tant qu'expéditeur d'e-mails désirés. C'est ainsi que les FSI savent que c'est vous et comment ils savent livrer votre courrier immédiatement. Sans authentification, votre accès est présumé frauduleux.

## Méthodes d'authentification

### Cadre de politique de l'expéditeur (SPF)

Cette méthode confirme que votre adresse IP d'envoi de courriel Braze est autorisée à envoyer du courrier en votre nom. SPF est votre authentification de base et s'accomplit en publiant les enregistrements texte dans les paramètres DNS. Le serveur de réception vérifiera les enregistrements DNS et déterminera s'il est authentique ou non. Cette méthode est conçue pour valider l'expéditeur du courriel.

Votre enregistrement SPF sera configuré lorsque Braze configurera vos adresses IP et vos domaines - au-delà de l'ajout des enregistrements DNS que nous vous donnons, aucune action supplémentaire n'est requise.

### Domain Keys Identified Mail (DKIM)

Cette méthode confirme que votre domaine d'envoi de courriels Braze est autorisé à envoyer du courrier en votre nom. Cette méthode est conçue pour valider l'authenticité de l'expéditeur ET s'assurer que l'intégrité du message est préservée. Il utilise également des signatures numériques cryptographiques individuelles afin que les FAI puissent être sûrs que le courrier qu'ils délivrent est le même que le courrier que vous avez envoyé.

Braze signe le courrier avec votre clé privée secrète. Les FAI vérifient la signature par rapport à votre clé publique, qui est stockée dans votre enregistrement DNS personnalisé. Il n'y a pas deux signatures exactement identiques et seule votre clé publique peut vérifier avec succès votre signature de clé privée.

Votre enregistrement DKIM sera configuré lorsque Braze configurera vos IP et vos domaines - au-delà de l'ajout des enregistrements DNS que nous vous donnons, aucune action supplémentaire n'est requise.

### Authentification de messages par domaine, Rapports et Conformité (DMARC)

Cette méthode va plus loin dans les protocoles d'authentification SPF et DKIM.

Si vous décidez d'utiliser [DMARC](https://dmarc.org/), vous pouvez indiquer aux FAI comment ils doivent gérer le courrier qui a échoué à votre signature ou aux vérifications d'authentification. Les échecs pourraient être un signe que d'autres tentent de vous imiter, vous ou votre email. Vous pouvez dire aux FAI de rejeter ou de mettre en quarantaine le courrier et même de vous envoyer des rapports automatisés sur le mauvais courrier.
