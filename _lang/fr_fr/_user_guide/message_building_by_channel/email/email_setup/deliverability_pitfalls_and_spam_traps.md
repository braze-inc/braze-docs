---
nav_title: Pièges de la livrabilité et pièges à spam
article_title: Pièges de la livrabilité et pièges à spam
page_order: 7
page_type: reference
description: "Cet article de référence traite des pièges potentiels en matière de livrabilité des e-mails, des pièges à spam et de la manière de les éviter."
channel: email

---

# ![cours d'apprentissage de Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability){: style="float:right;width:120px;border:0;" class="noimgborder"} Pièges de la livrabilité et pièges à spam

La livrabilité de vos e-mails peut être affectée par l'un des pièges à spam suivants :

| Type de piège | Description |
|---|---|
| Pièges immaculés | Les adresses e-mail et les domaines qui n'ont jamais été utilisés. |
| Pièges recyclés | Adresses e-mail qui étaient à l'origine des utilisateurs réels, mais qui sont maintenant dormantes. |
| Pièges à fautes de frappe | Adresses e-mail contenant des fautes de frappe courantes. |
| Plaintes contre le spam | Lorsque votre e-mail est marqué comme spam par un client. |
| Taux de rebond élevé | Lorsque votre e-mail échoue systématiquement parce que l'adresse du destinataire n'est pas valide. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Comment éviter les pièges à spam

Ces pièges peuvent être évités si vous mettez en place un processus d'abonnement confirmé. En envoyant un e-mail initial d'abonnement et en demandant aux clients de vérifier qu'ils souhaitent recevoir vos messages, vous vous assurez que vos destinataires souhaitent recevoir des informations de votre part et que vous envoyez des messages à des adresses réelles et valides. Voici d'autres moyens d'éviter les pièges à spam :

1. Envoyez un e-mail à double abonnement. Il s'agit d'un e-mail qui demandera aux utilisateurs de confirmer leurs choix d'abonnement en cliquant sur un lien.
2. La meilleure pratique consiste à mettre en œuvre une [politique de temporisation]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/).
3. **N'achetez jamais de listes d'e-mails.** 

{% alert tip %}
Les équipes Braze Customer Success et Deliverability peuvent vous aider à vous assurer que vous suivez les meilleures pratiques pour maximiser la livrabilité à travers le monde.
{% endalert %}

## Suppression d'une adresse e-mail de votre liste de rebond ou de spam

Vous pouvez supprimer les e-mails rebondis et les e-mails de votre liste de spam Braze avec les endpoints suivants :
- [`/email/bounce/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_hard_bounces)
- [`/email/spam/remove`]({{site.baseurl}}/api/endpoints/email/post_remove_spam)