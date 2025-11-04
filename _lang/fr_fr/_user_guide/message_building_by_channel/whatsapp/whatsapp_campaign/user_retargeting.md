---
nav_title: Reciblage des utilisateurs
article_title: Reciblage des utilisateurs
page_order: 4
description: "Cet article de référence traite de la manière dont les utilisateurs peuvent recibler leurs messages en fonction des interactions WhatsApp des utilisateurs."
page_type: reference
channel:
  - WhatsApp
---

# Reciblage des utilisateurs 

> En plus de modifier l'état de l'abonnement de l'utilisateur, Braze enregistrera également les interactions avec le profil utilisateur pour filtrer et déclencher des messages.<br><br>Ces filtres et déclencheurs vous permettent de filtrer les utilisateurs qui ont reçu des messages WhatsApp ou qui ont reçu des messages WhatsApp à partir d'une campagne WhatsApp ou d'une étape du canvas spécifique.

## Options de reciblage

{% alert note %}
Lorsque vous créez des audiences avec le reciblage utilisateur, vous pouvez souhaiter inclure ou exclure certains utilisateurs en fonction de leurs préférences, et afin de respecter les lois sur la protection de la vie privée, telles que le droit "Ne pas vendre ou partager" en vertu de la CCPA. Les marketeurs doivent mettre en œuvre les filtres pertinents pour l'éligibilité des utilisateurs au sein de leurs critères d'entrée dans le canvas et/ou la campagne.
{% endalert %}

### Filtrer les utilisateurs par WhatsApp

Les utilisateurs peuvent être filtrés en fonction de la date à laquelle ils ont reçu un message WhatsApp pour la dernière fois ou s'ils ont reçu un message WhatsApp provenant d'une campagne WhatsApp spécifique. Les filtres peuvent être définis dans l'étape Utilisateurs ciblés du générateur de campagne.

**Filtre sur le dernier message WhatsApp reçu**<br>
\![Filtre pour la dernière réception d'un message WhatsApp le 22 avril 2025.]({% image_buster /assets/img/whatsapp/whatsapp23.png %}){: style="max-width:75%"}

**Filtre sur les messages reçus dans le cadre d'une campagne WhatsApp**<br>
Filtre les utilisateurs qui ont reçu un message d'une campagne WhatsApp spécifique. Avec ce filtre, vous avez également la possibilité de filtrer les personnes qui n'ont pas reçu de messages d'une campagne WhatsApp.<br>
\![Filtre pour la réception d'une campagne WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp22.png %}){: style="max-width:75%"}

### Filtrer par engagement
Recibler les utilisateurs qui ont, ou non, lu une campagne WhatsApp ou une étape du canvas. 

**Recibler les utilisateurs qui ont ouvert/lu une campagne WhatsApp spécifique.**
1. Créez un segment à l'aide du filtre **Campagne cliquée/ouverte.** 
2. Sélectionnez **lire un message WhatsApp.**
3. Choisissez la campagne souhaitée.<br>

!Filtre pour avoir lu un message WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp21.png %}){: style="max-width:75%"}

**Recibler les utilisateurs qui ont ouvert/lu une étape du canvas spécifique**
1. Créez une segmentation à l'aide du filtre **Étape cliquée/ouverte**.
2. Sélectionnez **lire un message WhatsApp.**
3. Choisissez la toile et les étapes du canvas souhaitées.<br>

Filtre pour la lecture d'une étape de WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp20.png %}){: style="max-width:75%"}

**Filtrer par attribution de campagne ou de canvas.**<br>
Filtre pour les utilisateurs qui ont ouvert/lu une campagne WhatsApp spécifique ou un composant ou une étiquette Canvas.

Filtre permettant d'ouvrir un message WhatsApp spécifique.]({% image_buster /assets/img/whatsapp/whatsapp19.png %}){: style="max-width:75%"}

