---
nav_title: Stylitics
article_title: Stylitics
description: "Cet article de référence décrit le partenariat entre Braze et Stylitics, une plateforme SaaS basée sur le cloud qui vous permet d'améliorer vos campagnes d'e-mail existantes avec un contenu groupé engageant et pertinent, créant une expérience client personnalisée."
alias: /partners/stylitics/
page_type: partner
search_tag: Partner

---

# Stylitics

> [Stylitics](https://stylitics.com/) est une plateforme SaaS basée sur le cloud pour les détaillants permettant d'automatiser et de distribuer du contenu visuel à grande échelle. Les offres groupées de Stylitics inspirent en contextualisant les produits, en renforçant la confiance dans les achats et en augmentant l'engagement, ce qui conduit finalement à une valeur moyenne de commande et à des taux de conversion plus élevés.

_Cette intégration est maintenue par Stylitics._

## À propos de l'intégration

Votre intégration Braze et Stylitics vous permet d'améliorer vos campagnes d'e-mail existantes avec un contenu groupé attrayant et pertinent, créant une expérience client personnalisée.

![][0]{: style="max-width:60%;"}

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Stylitics | Un compte [Stylitics](https://stylitics.com/) est requis pour profiter de ce partenariat. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

La liste suivante présente quelques exemples courants de programmes d'e-mail déclenchés :
- E-mails de panier abandonné 
- E-mails de navigation abandonnés 
- E-mails de confirmation d'expédition
- E-mails post-achat 

## Intégration

Stylitics fournit des données de bundle pour cette intégration. Votre fournisseur de services d'e-mailing peut créer ou mettre à jour le modèle d'e-mail pour inclure les bundles Stylitics. Stylitics ne peut pas modifier la mise en page ou le design des e-mails. 

1. Intégrez le lot dans l'e-mail. ESP détermine la position et la personnalisation.
2. ESP met à jour le code de l'e-mail de déclencheur pour inclure le contenu de Stylitics.
3. ESP testera, prévisualisera et lancera la série de mises à jour déclenchées. 

Stylitics ne fournira que les données du lot d’articles. Vous et votre ESP aurez accès aux données utilisateurs et pourrez intégrer les ensembles de données Stylitics pour les envoyer aux utilisateurs.

## échange de donnée

Les trois approches suivantes vous permettent d'inclure des bundles Stylitics dans vos e-mails déclenchés.

### 1\. approche API (recommandée)

Vous ou votre ESP pouvez effectuer un appel API par élément pour remplir les données du bundle dans votre e-mail. Stylitics recommande d'utiliser leur API pour effectuer des appels d’API car elle est prête à l'emploi.

{% alert note %}
Si vous exécutez un test A/B géré par Stylitics, les paramètres `styliticsCID` et `styliticsoverride` doivent être ajoutés aux URL PDP des articles Stylitics sur lesquels l'utilisateur clique dans l'e-mail.
<br><br>
Par exemple, {% raw %}`&styliticsoverride=001?styliticsCID=email[clientname]`{% endraw %}
{% endalert %}

### 2\. Approche de fichier plat
Vous ou votre ESP pouvez référencer les données du lot d'un article dans un fichier plat pour alimenter votre e-mail avec des données du lot. Stylitics peut aplatir les données du lot dans un fichier au format CSV, TXT ou XML et vous les envoyer quotidiennement. Ils peuvent également aider à ajuster le format de fichier selon les besoins de votre ESP. Notez que cela prend 2 à 3 semaines pour créer ce fichier.

#### Exigences:
- **Emplacement** : Stylitics peut déposer le fichier sur son SFTP pour que vous puissiez le récupérer quotidiennement, ou vous pouvez lui envoyer vos identifiants SFTP pour qu’il puisse déposer le fichier. 
- **Temps**: Stylitics déposera le fichier chaque matin. Faites-leur savoir à quelle heure vous avez besoin du fichier. 
- **Clé de fichier**: Vous et Stylitics devez vous mettre d'accord sur la chaîne de caractères des données de l'article à utiliser comme clé du fichier afin que votre ESP puisse référencer les données. L’unité de gestion des stocks ou les paramètres `item_group_id` et `item_number` sont couramment utilisés. 

### 3\. Approche d'extraction de données de site web
Les fournisseurs peuvent extraire le contenu Stylitics de l'interface de votre site et insérer des données de lots dans les e-mails. Aucun travail supplémentaire de Stylitics n'est requis. 

## Meilleures pratiques pour l’utilisation des modèles d’e-mails 

Vous et votre ESP créerez un modèle d'e-mail HTML pour insérer des données et des lots Stylitics. Voici quelques meilleures pratiques et recommandations. 
- Afficher 2 à 4 lots dans l'e-mail pour l'article le plus cher ou le premier article à plein tarif que l'utilisateur a acheté ou avec lequel il a interagi 
- Appeler plusieurs `item_numbers` et afficher les premières réponses du bundle 
- Ayez une option de repli s'il n'y a pas de lots disponibles pour l'article 
	- Masquer la section où les bundles Stylitics sont en ligne 
	- Afficher les lots pour le prochain article que l'utilisateur a consulté 
- Afficher les images du lot et une liste de titres de produit et de vignettes pour garantir un taux de clics clair pour l'utilisateur

{% alert note %}
Le widget JavaScript de Stylitics ne peut pas être inséré dans les e-mails car les e-mails ne supportent pas JavaScript.
{% endalert %}

## Analyses

Stylitics fournit les données du lot pour ce type de programme d'e-mails. Par conséquent, nous demandons un partage de données ouvert entre vous, votre système automatisé de communication et Stylitics. Nous vous demandons, si possible, de nous envoyer les indicateurs suivants pour nous permettre de connaître l'impact de notre programme et l’améliorer :
- Emails envoyés 
- E-mails ouverts 
- Vues et engagements 
- Taux de clics 
- Ajouts au panier 
- Achats

## Prochaines étapes 

Contactez votre gestionnaire de compte Stylitics pour coordonner les prochaines étapes et le calendrier du programme d'e-mails. Quelques prochaines étapes incluent : 
- Décidez quels e-mails vous souhaitez utiliser
- Connectez Stylitics à votre fournisseur de services de messagerie pour discuter de l'échange de données afin de choisir entre l'option API ou fichier plat 
- Créez des maquettes avec votre ESP 
- S'aligner sur l'analyse 
- S'aligner sur le calendrier de lancement 


[0]: {% image_buster /assets/img/stylitics.png %}