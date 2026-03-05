---
nav_title: Calculateur de facturation
article_title: Calculateurs de facturation par SMS et RCS
page_order: 5
description: "Cet article de référence explique ce qu'est un segment de message, comment ils sont comptabilisés pour la facturation, ainsi que les éléments à garder à l'esprit lors de la création d'une copie de message SMS et RCS."
page_type: reference
alias: /sms_rcs_billing_calculators/
tool:
  - Testing Tools
channel:
  - SMS
  - MMS
  - RCS

---

# Calculateurs de facturation pour les SMS et RCS

> Chez Braze, les messages SMS sont facturés par segment de message, tandis que les messages RCS sont facturés par message. Comprendre ce qui définit un segment SMS et les différents types de facturation RCS vous permettra de mieux comprendre comment vous serez facturé et d'éviter les dépassements accidentels.

## Calculateur de copie et de segmentation des messages SMS

Les envois de messages SMS sont facturés par segment de message. Pour comprendre votre facturation, il est essentiel de savoir comment les messages SMS sont répartis.

### Qu’est-ce qu’un segment SMS ?

Le short message service (SMS) est un protocole de communication standardisé qui permet aux appareils d’envoyer et de recevoir des messages sous forme de textes brefs. Il a été conçu pour "s'intégrer entre" d'autres protocoles de signalisation, c'est pourquoi la longueur des messages SMS est limitée à 160 caractères de 7 bits, soit 1120 bits, ou 140 octets. Les segments de messages SMS sont les lots de caractères que les opérateurs de téléphonie utilisent pour mesurer les messages texte. Les messages étant facturés par segment de message, les clients tirant parti des SMS ont tout intérêt à comprendre comment les messages sont divisés.

Lorsque vous créez une campagne SMS ou un Canvas avec Braze, les messages que vous construisez dans le compositeur sont représentatifs de ce que vos utilisateurs peuvent voir lorsque le message est livré à leur téléphone, mais **ne sont pas indicatifs de la manière dont votre message sera divisé en segments et finalement de la manière dont vous serez facturé**. Il est de votre devoir de comprendre combien de segments seront envoyés et d’être conscient des dépassements potentiels, mais nous avons quelques ressources pour vous faciliter la tâche. Découvrez notre [calculateur de segment](#segment-calculator) interne.

![]({% image_buster /assets/img/sms_segment_pic.png %}){: style="border:0;"}

#### Répartition des segments

La limite de caractères pour **un segment SMS autonome** est de 160 caractères ([encodage GSM-7](https://en.wikipedia.org/wiki/GSM_03.38)) ou de 70 caractères ([encodage UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set)) en fonction du type d'encodage. Cependant, la plupart des téléphones et réseaux prennent en charge la concaténation, pour traiter des SMS plus longs pouvant atteindre 1 530 caractères (GSM-7) ou 670 caractères (UCS-2). Même si un message peut comprendre plusieurs segments, s’il ne dépasse pas ces limites de concaténation, il sera affiché comme un seul message et signalé comme tel.

Il est important de noter que **lorsque vous dépassez la limite de caractères de votre premier segment, des caractères supplémentaires entraîneront la division et la segmentation de l'ensemble de votre message en fonction de nouvelles limites de caractères**:
- **Encodage GSM-7**
    - Les messages dépassant la limite de 160 caractères sont maintenant divisés en segments de 153 caractères et envoyés séparément, puis recomposés par l’appareil du destinataire. Par exemple, un message de 161 caractères est envoyé en deux messages, dont l’un comporte 153 caractères et le second 8.
- **Encodage UCS-2**
    - Si vous incluez des caractères non-GSM tels que des émojis, caractères chinois, coréens ou japonais dans des messages SMS, ces derniers doivent être envoyés avec le codage UCS-2. Les messages dépassant la limite initiale de 70 caractères entraînent la concaténation du message en segments de 67 caractères. Par exemple, un message de 71 caractères est envoyé en deux messages, dont un comporte 67 caractères et le second 4.

Quel que soit le type de codage, chaque message SMS envoyé par Braze a une limite de 10 segments et est compatible avec [le templating Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/), [le contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), les emojis et les liens.

{% tabs %}
{% tab GSM-7 encoding %}
Nombre de caractères | Combien de segments ? |
| -------------------- | ----------------- |
| 0 - 160 caractères | 1 segment |
| 161 - 306 caractères | 2 segments |
| 307 - 459 caractères | 3 segments |
| 460 - 612 caractères | 4 segments |
| 613 - 765 caractères | 5 segments |
| 766 - 918 caractères | 6 segments |
| 919 - 1071 caractères | 7 segments |
| 1072 - 1224 caractères | 8 segments |
| 1225 - 1377 caractères | 9 segments |
| 1378 - 1530 caractères | 10 segments |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% tab UCS-2 encoding %}
Nombre de caractères | Combien de segments ? |
| -------------------- | ----------------- |
| 0 - 70 caractères | 1 segment |
| 71 - 134 caractères | 2 segments |
| 135 - 201 caractères | 3 segments |
| 202 - 268 caractères | 4 segments |
| 269 - 335 caractères | 5 segments |
| 336 - 402 caractères | 6 segments |
| 403 - 469 caractères | 7 segments |
| 470 - 536 caractères | 8 segments |
| 537 - 603 caractères | 9 segments |
| 604 - 670 caractères | 10 segments |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

### Aspects à garder à l’esprit lorsque vous créez votre texte

- **Limite de caractères par segment**
    - [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) a une limite de 160 caractères par segment SMS. Tous les messages comportant plus de 160 caractères sont segmentés avec une limite de 153 caractères.
    - [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) a une limite de 70 caractères par segment de message. Tous les messages comportant plus de 70 caractères sont segmentés avec une limite de 67 caractères.<br><br>
- **Limite de segment par message**
    - Vous pouvez envoyer un nombre maximum de segments en raison des limitations du support. Pas plus de **10 segments** de messages ne peuvent être envoyés dans un seul message SMS Braze.
    - Ces 10 segments sont limités à 1 530 caractères (codage GSM-7) ou 670 caractères (codage UCS-2).<br><br>
- **Compatible avec les modèles Liquid, le contenu connecté, les émojis et les liens**
    - Utiliser la création de modèles de Liquid et le contenu connecté dans votre message risque de vous faire dépasser la limite de caractères du type de codage choisi. Vous pouvez utiliser le [filtre de troncature des mots](https://help.shopify.com/en/themes/liquid/filters/string-filters#truncatewords) pour limiter le nombre de mots que votre Liquid pourrait apporter au message.
    - Les émojis ne partageant pas un nombre de caractères standard, testez vos messages pour être sûr qu’ils sont segmentés et affichés correctement.
    - Les liens peuvent inclure de nombreux caractères, entraînant plus de segments de messages que prévu. Bien que l’utilisation de raccourcissements de liens soit possible, mieux vaut utiliser des codes courts. Visitez notre [FAQ SMS]({{site.baseurl}}/sms_faq/) pour plus d'informations.<br><br>
- **Test**
    - Testez toujours vos messages SMS avant de les envoyer, en particulier lorsque vous utilisez Liquid et du contenu connecté, car le dépassement des limites de messages ou de texte peut entraîner des frais supplémentaires. Notez que les messages test comptent dans les limites de messages.

### Calculateur de segments SMS {#segment-calculator}
---

{% include alerts/tip_alerts.md alert='SMS segment calculator' %}

## Envoi de messages RCS

Les messages RCS sont facturés en fonction de leur contenu et du pays dans lequel le message est délivré. Pour estimer précisément les coûts, il est essentiel de comprendre les différents types de messages et la manière dont ils sont facturés.

### Types de facturation RCS

Notre plateforme prend en charge deux modèles de facturation principaux : un modèle mondial et un modèle américain.

#### Modèle mondial (marchés non américains)

Les messages sont facturés à l'unité et sont classés en deux catégories : les messages de base et les messages uniques.

{% tabs local %}
{% tab Basic %}

Les messages RCS de base sont des messages de texte uniquement, d'une longueur maximale de 160 caractères, et sont facturés comme un seul message.

{% alert note %}
L'ajout de boutons ou de tout autre élément riche modifiera le type de message en un message RCS unique.
{% endalert %}

{% endtab %}
{% tab Single %}

Les messages RCS simples sont des messages de plus de 160 caractères OU comprenant des éléments riches tels que des boutons ou des médias. Ceux-ci sont facturés comme un seul message, quelle que soit la longueur du message.

{% alert note %}
L'envoi d'un message texte et d'un fichier multimédia séparé est toujours facturé comme deux messages distincts.
{% endalert %}

{% endtab %}
{% endtabs %}

#### Modèle des États-Unis

Les messages sont classés dans les catégories Rich Media ou Rich Media.

{% tabs local %}
{% tab Rich messages %}

Les messages enrichis sont des messages en texte seul avec ou sans bouton. Ils sont facturés par segment, chaque segment étant limité à 160 octets UTF-8, ce qui signifie que **le nombre de caractères par segment n'est pas fixe**. Un message ne comportant que 160 caractères en anglais simple constitue un segment, tandis qu'un message comportant un texte plus long et des emojis peut constituer plusieurs segments.

{% endtab %}
{% tab Rich media messages %}

Les messages Rich Media comprennent un fichier média (image, vidéo) ou une Rich Card et sont facturés comme un message unique.

{% endtab %}
{% endtabs %}

### Compositeur de messages et tableau de bord de l'utilisation des messages

Lorsque vous créez votre message, le compositeur de messages affiche le type de facturation en temps réel par le biais d'un libellé (RCS de base, RCS unique, Rich ou Rich Media), ce qui vous permet de suivre les coûts avant l'envoi.

Votre [tableau de bord de l'utilisation des messages]({{site.baseurl}}/message_usage_dashboard/) reflétera ces types de facturation et indiquera le nombre de segments utilisés pour les messages américains, offrant ainsi une vue transparente de votre consommation de crédits de messages.
