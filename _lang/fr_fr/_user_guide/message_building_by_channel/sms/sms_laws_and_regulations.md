---
nav_title: "Lois et réglementations SMS"
article_title: Lois et réglementations SMS
page_order: 3
description: "Le présent article de référence couvre les lois et réglementations qui encadrent SMS et MMS."
page_type: reference
channel:
  - SMS
  
---

# Lois SMS, réglementations et prévention des abus

> Comme les messages SMS sont l’une des façons les plus directes d’atteindre les clients et les utilisateurs, en allant directement au téléphone de l’utilisateur, il faut qu’il existe des réglementations pour empêcher les marques d’abuser de cette relation ou de l’utiliser de façon excessive, et les amendes en cas d’infraction pourraient coûter des milliers de dollars. 

{% alert warning %}
Le présent article n’est pas destiné à fournir, et ne peut être considéré comme fournissant des conseils juridiques. L’utilisation de SMS est soumise à des exigences légales spécifiques. Pour vous assurer que vous utilisez les services SMS conformément à toutes les lois applicables, vous devez demander conseil à votre conseiller juridique.
{% endalert %}

## Les six règles pour être en conformité

En général, nous vous encourageons à faire preuve de discernement lorsque vous envisagez l’envoi de SMS. Braze, ainsi que nos partenaires d’envoi, ont mis en place des contrôles qui empêchent la plupart des abus par SMS.

Il y a six règles que vous devez suivre :

1. **Obtenez le consentement explicite des utilisateurs avant de leur envoyer des SMS.** Chaque fois que les utilisateurs donnent leur consentement, il est de votre responsabilité de consigner, mettre à jour et conserver ces informations dans une base de données utilisateur conforme. Conformément aux directives juridiques de base, les informations les plus importantes que vous devez conserver à l’égard du consentement sont :
  - L’heure et la date auxquelles l’utilisateur a donné son consentement
  - Le type de messagerie SMS qu’il a accepté
  - Le numéro de téléphone de l’utilisateur
  - La langue dans laquelle ils se sont abonnés<br><br>

2. **Communiquez clairement les types de SMS que vous enverrez**. Les utilisateurs doivent comprendre quels messages ils peuvent attendre de votre marque dans ce canal et les types d’informations ou d’offres qu’ils recevront. Énoncez explicitement l’objectif de vos futures campagnes, la fréquence des messages et rappelez aux utilisateurs que des taux de messages/données s’appliquent.<br><br>

3. **Gardez les informations essentielles à jour et visibles**. Assurez-vous que la version la plus récente des Conditions générales de votre marque et de votre Politique de confidentialité de marketing par SMS est clairement visible et facilement accessible depuis votre page d’abonnement SMS.<br><br>

4. **Envoyez des SMS uniquement aux numéros de téléphone obtenus légalement et ayant donné leur consentement**. Dans le cadre de la planification de la migration technique, assurez-vous que votre équipe comprend le mécanisme permettant d’associer la situation d’abonnement à chaque profil utilisateur sur votre plateforme d’engagement des clients.<br><br>

5. **Assurez-vous de la conformité SHAFT aux États-Unis et dans les autres régions concernées.** L’envoi de messages SMS avec du texte concernant le sexe, la haine, l’alcool, les armes à feu et le tabac (SHAFT) est généralement considéré comme illégal aux États-Unis et dans d’autres régions.<br><br>

6. **Vérifiez tout**. Travaillez avec votre équipe juridique pour vous assurer que votre programme SMS est entièrement conforme à toutes les règles et réglementations applicables pour les régions où votre marque opère.<br><br>

## Ressources

Voici quelques liens que vous pourriez avoir besoin de consulter lorsque vous construisez votre campagne SMS :

- [Principes et meilleures pratiques de la CTIA en matière d'envoi de messages pour 2023](https://api.ctia.org/wp-content/uploads/2023/05/230523-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf)
- [Guide de Twilio sur la conformité des SMS aux États-Unis](https://www.twilio.com/learn/call-and-text-marketing/guide-to-us-sms-compliance)
- [Conformité et ressources d’Acoustic pour les SMS aux États-Unis](https://help.goacoustic.com/hc/en-us/articles/360043717414-United-States-SMS-compliance-and-resources)

## Considérations relatives à la conformité

### Données et vie privée

Le respect de la vie privée d’un client est essentielle à une relation significative et respectueuse. Respecter la vie privée et les informations d’un client est une autre occasion de créer un lien entre lui et votre marque. Parfois, l’utilisation d’outils marketing signifie que les données et la confidentialité ont la plus basse priorité.

Heureusement pour vous, Braze suit les directives de nombreuses [réglementations de sécurité]({{site.baseurl}}/developer_guide/disclosures/security_qualifications/#security-qualifications "qualifications de sécurité Braze"), y compris [le RGPD]({{site.baseurl}}/dp-technical-assistance/).

La [CTIA](https://www.ctia.org/) (une association commerciale représentant l'industrie des communications sans fil aux États-Unis) recommande que vous mainteniez et affichiez de manière visible une politique de confidentialité claire et facile à comprendre.

### Consentement

Les options d’abonnement, d’aide et de désabonnement sont un must absolu lors de la création de campagnes SMS.

La loi sur la protection des consommateurs par téléphone ([TCPA](https://en.wikipedia.org/wiki/Telephone_Consumer_Protection_Act_of_1991 "Wikipedia:Loi sur la protection des consommateurs par téléphone de 1991")) exige qu'une entreprise obtienne un "consentement écrit exprès" pour envoyer des messages aux clients - vous pouvez le faire de plusieurs manières, y compris via le web ou le mobile. Vous devez être clair avec le client sur la façon dont vous avez l’intention d’utiliser le SMS pour communiquer avec lui.

N'oubliez pas de respecter le [Registre national des numéros de téléphone exclus](https://www.donotcall.gov/).

Braze utilise des [Groupes d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/) pour gérer des groupes d'utilisateurs en fonction de leur niveau de consentement.

### Spam et cadence

Comme pour l’e-mail, vos utilisateurs ou clients peuvent connaître le burnout de la boîte de réception. Mais ce n’est qu’une des raisons de ne pas envoyer des messages sans cesse à vos clients. Vous devriez regarder spécifiquement la [section 5 de la loi FTC](https://www.federalreserve.gov/boarddocs/supmanual/cch/ftca.pdf "PDF : Section 5 de la loi de la Commission fédérale du commerce") pour vous assurer de la conformité (aux U.S).

Certaines considérations relatives aux spams sont intégrées aux capacités SMS en général (limites d'envoi de codes longs et courts), ainsi qu'aux limites de taux de Braze. Cependant, vous devez toujours tenir compte des lois sur la conformité lorsque vous planifiez vos campagnes.

### Contenu

Cela peut être difficile, mais en cas de doute, évitez les sujets qui impliquent la violence, le sexe, les drogues, le tabac ou autres choses du même genre. Soyez prudent lorsque vous envoyez des messages concernant ces sujets : vous pouvez tout de même être facturé pour des messages qui sont bloqués par divers transporteurs.

La [CTIA](https://www.ctia.org/) recommande de garantir la conformité à SHAFT, qui définit les sujets suivants comme étant généralement « illégaux » lors de l'envoi de messages aux États-Unis :

- Sexe
- Haine
- Alcool
- Armes à feu
- Tabac

Pour plus d'informations sur ce sujet, consultez les [Principes et bonnes pratiques de la CTIA pour l’envoi de messages pour 2019](https://api.ctia.org/wp-content/uploads/2019/07/190719-CTIA-Messaging-Principles-and-Best-Practices-FINAL.pdf).

### Planification

Assurez-vous de vous conformer à la [TCPA](https://en.wikipedia.org/wiki/telephone_consumer_protection_act_of_1991), qui dicte que vous ne devez pas envoyer de messages tard dans la nuit. Reportez-vous au contenu de la réglementation pour connaître les heures exactes. Cependant, vous ne devriez pas envoyer de messages aussi tard : ne souhaitez-vous pas un engagement fort ?

### International

La plupart de ces bonnes pratiques s’appliquent aux directives établies aux États-Unis d’Amérique. Si vous visez des clients en dehors des régions des U.S, recherchez les bonnes pratiques et les lois en vigueur dans ces régions. Il est toujours préférable d’agir de manière à respecter les réglementations les plus strictes, qui sont généralement appliquées aux États-Unis, au Canada et dans les pays de l’Union européenne.
