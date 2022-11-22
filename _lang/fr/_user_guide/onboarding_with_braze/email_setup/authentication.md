---
nav_title: Authentification par e-mail
article_title: Authentification par e-mail
page_order: 1
page_type: reference
description: "Le présent article de référence couvre l’authentification par e-mail, un ensemble de techniques visant à équiper votre e-mail d’informations vérifiables sur son origine."
channel: (e-mail)

---

# Authentification par e-mail

> L’authentification par e-mail est un ensemble de techniques visant à équiper votre e-mail d’informations vérifiables sur son origine.

Une authentification appropriée est cruciale pour que les AI vous reconnaissent en tant qu’expéditeur d’e-mails désirables. C’est la façon dont les AI savent que c’est vous et savent comment livrer votre courrier immédiatement. Sans authentification, votre communication est présumée frauduleuse.

## Méthodes d’authentification

### Cadre de politique de l’expéditeur (SPF)

Cette méthode confirme que votre adresse IP d’envoi d’e-mail Braze est autorisée à envoyer un courrier en votre nom. SPF est votre authentification de base et est réalisée en publiant les enregistrements de texte dans les paramètres DNS. Le serveur de réception vérifie les enregistrements DNS et détermine s’il est authentique ou non. Cette méthode est conçue pour valider l’expéditeur de l’e-mail.

Votre enregistrement SPF sera configuré lorsque Braze configure vos IP et domaines -au-delà de l’ajout des enregistrements DNS que nous vous fournissons, aucune autre action n’est requise.

### Courriel identifié des clés de domaine (DKIM)

Cette méthode confirme que votre adresse IP d’envoi d’e-mail Braze est autorisée à envoyer un courrier en votre nom. Cette méthode est conçue pour valider l’authenticité de l’expéditeur ET s’assurer que l’intégrité du message est préservée. Elle utilise également des signatures numériques cryptographiques individuelles pour que les FAI puissent s’assurer que le courrier qu’ils délivrent est le même que celui que vous avez envoyé.

Braze signe le courrier avec votre clé privée secrète. Les ISP vérifient la signature de votre clé publique, qui est stockée dans votre dossier DNS personnalisé. Aucune signature n’est exactement identique et, seule votre clé publique peut vérifier avec succès votre signature clé privée.

Votre enregistrement SPF sera configuré lorsque Braze configure vos IP et domaines -au-delà de l’ajout des enregistrements DNS que nous vous fournissons, aucune autre action n’est requise.

### Authentification, reporting et conformité des messages basés sur les domaines (DMARC)

Cette méthode prend en outre les protocoles d’authentification SPF et DKIM.

Si vous décidez d’utiliser [DMARC](https://dmarc.org/), vous pouvez indiquer aux ISP comment ils doivent gérer les courriels ayant échoués à vos vérifications de signature ou d’authentification. Les échecs peuvent être un signe que d’autres essaient de vous imiter ou votre e-mail. Vous pouvez informer les ISP de rejeter ou de mettre en quarantaine le courriel et même de vous envoyer des rapports automatisés sur les courriels frauduleux.
