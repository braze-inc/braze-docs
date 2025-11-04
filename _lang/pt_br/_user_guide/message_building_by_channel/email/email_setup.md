---
nav_title: Configuração de e-mail
article_title: Configuração do e-mail de integração
layout: dev_guide
page_order: 1
guide_top_header: "Configuração de e-mail"
guide_top_text: "O Braze pode ajudá-lo a começar a enviar campanhas de e-mail. Siga nossos guias ou confira nosso curso <a href='https://learning.braze.com/email-onboarding-for-pro-and-enterprise-achieving-high-deliverability' target='_blank'>Email Onboarding</a> Braze Learning."
page_type: landing
description: "Essa página de destino inclui recursos sobre como começar a usar campanhas de e-mail, incluindo a configuração de seus IPs e domínios, aquecimento de IP, validação de e-mail e muito mais."
channel: email

guide_featured_title: "Artigos de seção"
guide_featured_list:
- name: "Configuração de IPs e domínios"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/
  image: /assets/img/braze_icons/target-05.svg
- name: "Aquecimento IP"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/ip_warming/
  image: /assets/img/braze_icons/annotation-alert.svg
- name: "Validação de e-mail"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/email_validation/
  image: /assets/img/braze_icons/check-square-broken.svg
- name: "Autenticação de e-mail"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/authentication/
  image: /assets/img/braze_icons/user-square.svg
- name: "Importação de sua lista de e-mails"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/import_your_email_list/
  image: /assets/img/braze_icons/list.svg
- name: "Visão geral do SSL"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/ssl/
  image: /assets/img/braze_icons/navigation-pointer-01.svg
- name: "Consentimento e coleta de endereços"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/consent_and_address_collection/
  image: /assets/img/braze_icons/book-closed.svg
- name: "Armadilhas de entregabilidade e armadilhas de spam"
  link: /docs/user_guide/message_building_by_channel/email/email_setup/deliverability_pitfalls_and_spam_traps/
  image: /assets/img/braze_icons/alert-triangle.svg
---

## Requisitos

Antes de começar a enviar e-mails, você precisa de alguns itens. Consulte a tabela a seguir para saber mais sobre esses requisitos.

| Requisito | Descrição | Fonte |
|---|---|---|
| Um IP (Protocolo de Internet) dedicado| Um IP dedicado é um endereço de Internet exclusivo fornecido exclusivamente para uma única conta de hospedagem. | O Braze fornece IPs dedicados para garantir o controle da reputação do seu remetente de e-mail. O onboarding do Braze configurará isso para você.|
| Domínios com Whitelabeled | Eles consistem em um domínio e um subdomínio. Com o uso de whitelabeling, você pode passar nas verificações de autenticação de e-mail para DKIM e SPF. | A equipe de Onboarding do Braze gerará esses domínios para você, mas você deve escolher os nomes. |
| Subdomínios | Trata-se de uma subdivisão de um domínio (como "@news.company.com") em seu endereço de e-mail. Ter um subdomínio evitará erros que possam prejudicar a reputação do e-mail oficial de sua empresa. | A equipe de Onboarding gerará isso para você, mas você deve decidir o nome do subdomínio. Você não pode usar subdomínios que estejam sendo usados atualmente fora do Braze. |
| Pools de IP | Trata-se de uma configuração opcional usada para separar a reputação de diferentes tipos de e-mail (como "promocional" e "transacional") para evitar que a reputação de um afete o outro e para dar suporte a uma maior capacidade de entrega. | A equipe de Onboarding configurará as piscinas para você. Em seguida, ao redigir seu e-mail, você poderá visualizar o pool de IPs do seu e-mail na etapa **Target Audiences (Públicos-alvo** ).|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Aquecimento por IP

{% alert important %}
O aquecimento do IP é a **etapa mais importante** do processo de configuração do e-mail. Embora essa não seja sua primeira etapa (na verdade, é a última), estamos chamando a atenção aqui para que você saiba que deve aquecer seu endereço IP, caso contrário, todos os e-mails que você enviar serão enviados para spam ou estarão sujeitos a outras barreiras de envio.
{% endalert %}

[O aquecimento de IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/) é quando você envia um número relativamente pequeno de e-mails em seu primeiro lote e, com o tempo, aumenta ligeiramente o volume nos lotes seguintes até atingir seu volume diário típico. Isso é feito no final do processo de configuração do e-mail.

Ao começar com volumes menores de e-mail, você estabelece um nível de confiança com seu provedor de e-mail, mostrando que está enviando e-mails apenas para usuários relevantes. Enviar o primeiro lote de e-mails para os usuários mais engajados pode ajudá-lo a ganhar confiança mais rapidamente com seu provedor.

Quando terminar de aquecer seu IP, você poderá [começar a criar e enviar e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/)!

<br><br>
