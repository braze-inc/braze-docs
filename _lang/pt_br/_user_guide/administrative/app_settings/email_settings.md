---
nav_title: Preferências de e-mail
article_title: Preferências de e-mail
page_type: reference
page_order: 14
description: "Este artigo de referência aborda as preferências de e-mail no painel do Braze, incluindo configurações de envio, pixels de rastreamento de abertura, página de assinatura e rodapés, entre outros."
tool: Dashboard
channel: email

---

# Preferências de e-mail

> Email Preferences é onde você pode definir configurações específicas de e-mail de saída, como rodapés personalizados, páginas personalizadas de opt-in e opt-out e muito mais. A inclusão dessas opções em seus e-mails de saída proporciona uma experiência fluida e coesa para seus usuários.

**As preferências de e-mail** podem ser encontradas em **Configurações** no painel.

## Envio de configuração

As configurações de e-mail na seção **Configuração de envio** determinam quais detalhes são incluídos nas suas campanhas de e-mail. Em particular, essas configurações estão relacionadas principalmente ao que o usuário vê quando recebe um e-mail do Braze.

### Configurações de e-mail de saída

Ao definir suas configurações de e-mail, suas configurações de e-mail de saída identificam qual nome e endereço de e-mail são usados quando o Braze envia e-mails para seus usuários.

{% tabs local %}
{% tab Display Name Address %}

Nessa seção, você pode adicionar os nomes e endereços de e-mail que podem ser usados quando o Braze enviar e-mails para seus usuários. Os nomes de exibição e os endereços de e-mail estarão disponíveis nas opções **Editar informações de envio** à medida que você redigir sua campanha de e-mail. Observe que as atualizações feitas nas configurações de e-mail de saída não afetam retroativamente os envios existentes.

\!["Configurações de e-mail de saída" com campos para diferentes nomes de exibição e domínios.]({% image_buster /assets/img/email_settings/display_name_address.png %})

#### Personalização com Liquid

Você também pode usar [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) nos campos **From Display Name** e **Local Part** para modelar dinamicamente o e-mail de envio com base em atributos personalizados. Por exemplo, você pode usar a lógica condicional para enviar de diferentes marcas ou regiões:

{% raw %}
```liquid
{% if ${language} == 'en' %} 
English Display Name 
{% elsif ${language} == 'de' %} 
German Display Name 
{% else %} 
Default to English Display Name
{% endif %}
```
{% endraw %}

{% endtab %}
{% tab Reply-To Address %}

Adicionar um endereço de e-mail nessa seção permite selecioná-lo como endereço de resposta para a sua campanha de e-mail. Você também pode tornar um endereço de e-mail o padrão selecionando **Make Default (Tornar padrão**). Esses endereços de e-mail estarão disponíveis nas opções **Editar informações de envio** à medida que você redigir sua campanha de e-mail.

Seção "Reply-To Address" (Endereço para resposta) com campos para inserir vários endereços para resposta.]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

#### Personalização com Liquid

Você também pode usar [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) no campo **Reply-To Address** para modelar dinamicamente o endereço de resposta com base em atributos personalizados. Por exemplo, você pode usar a lógica condicional para enviar respostas a diferentes regiões ou departamentos:

{% raw %}
```liquid
{% if {{custom_attribute.${region}}} == 'US' %}
us-support@company.com
{% elsif {{custom_attribute.${region}}} == 'EU' %}
eu-support@company.com
{% else %}
global-support@company.com
{% endif %}
```
{% endraw %}

{% endtab %}
{% tab BCC Address %}

Essa seção permite adicionar e gerenciar endereços BCC que podem ser anexados a mensagens de e-mail de saída enviadas pelo Braze. Os endereços BCC estão disponíveis apenas para SendGrid e SparkPost. Como alternativa aos endereços BCC, recomendamos o uso do [arquivamento de mensagens]({{site.baseurl}}/user_guide/data/export_braze_data/message_archiving/) para salvar uma cópia das mensagens enviadas aos usuários para fins de arquivamento ou conformidade.

Anexar um endereço BCC a uma mensagem de e-mail enviará uma cópia idêntica da mensagem que o usuário receber para a sua caixa de entrada BCC. Essa é uma ferramenta útil para reter cópias de mensagens enviadas aos usuários para atender a requisitos de conformidade ou problemas de suporte ao cliente. Os e-mails BCC não são incluídos nos relatórios e análises de e-mail.

{% alert important %}
Anexar um endereço BCC à sua campanha ou Canvas resultará na duplicação de seus e-mails faturáveis para o componente de campanha ou Canvas, uma vez que o Braze enviará uma mensagem ao seu usuário e outra ao seu endereço BCC.
{% endalert %}

\![seção Endereço BCC da guia Configurações de e-mail.]({% image_buster /assets/img/email_settings/bcc_address.png %}){: style="max-width:75%;" }

Depois de adicionar um endereço, ele ficará disponível para seleção ao redigir um e-mail nas etapas de campanhas ou do Canvas. Selecione **Tornar padrão** ao lado de um endereço para definir que esse endereço seja selecionado por padrão ao iniciar uma nova campanha de e-mail ou componente do Canvas. Para substituir isso no nível da mensagem, você pode selecionar **No BCC** ao configurar sua mensagem.

Se você precisar que todas as mensagens de e-mail enviadas do Braze tenham um endereço BCC incluído, poderá selecionar a opção **Exigir um endereço BCC para todas as suas campanhas de e-mail**. Isso exigirá que você selecione um endereço padrão, que será automaticamente selecionado em novas campanhas de e-mail ou etapas do Canvas. O endereço padrão também será adicionado automaticamente a todas as mensagens acionadas por meio de nossa API REST. Não há necessidade de alterar a solicitação de API existente para incluir o endereço.

{% endtab %}
{% endtabs %}

## Pixel de rastreamento de abertura

[Curso de aprendizagem do Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

O pixel de rastreamento de abertura de e-mail é uma imagem invisível de 1 x 1 px que é inserida automaticamente no HTML do e-mail. Esse pixel ajuda a Braze a detectar se os usuários finais abriram seu e-mail. As informações sobre a abertura de e-mails podem ser muito úteis, ajudando os usuários a determinar estratégias de marketing eficazes por meio da compreensão das taxas de abertura correspondentes.

### Colocação do pixel de rastreamento

O comportamento padrão do Braze é anexar o pixel de rastreamento à parte inferior do e-mail. Para a maioria dos usuários, esse é o local ideal para colocar o pixel. Embora o pixel já seja estilizado para causar o mínimo possível de alterações visuais, quaisquer alterações visuais não intencionais seriam menos visíveis na parte inferior de um e-mail. Esse também é o padrão para provedores de e-mail, como SendGrid e SparkPost.

### Alteração do local do pixel de rastreamento

Atualmente, o Braze suporta a substituição do local padrão do pixel de rastreamento de abertura do ESP (a última tag em `<body>` de um e-mail) para movê-lo para a primeira tag em `<body>`.
  
\!["Abra a seção Tracking Pixel" com as opções para mover para SendGrid, SparkPost ou Amazon SES.]({% image_buster /assets/img/open_pixel.png %}){: style="max-width:80%;" }

Para alterar o local:

1. No Braze, vá para **Configurações** > **Preferências de e-mail**.
2. Selecione uma das seguintes opções: **Mudança para SendGrid**, **mudança para SparkPost** ou **mudança para Amazon SES**
3. Selecione **Salvar**.

Uma vez salvo, o Braze enviará instruções especiais ao ESP para colocar o pixel de rastreamento de abertura na parte superior de todos os e-mails em HTML.
  
{% alert important %}
A ativação do SSL envolverá o URL do pixel de rastreamento com HTTPS em vez de HTTP. Se o seu SSL estiver mal configurado, isso poderá afetar a eficácia do pixel de rastreamento.
{% endalert %}

## Cabeçalho List-unsubscribe {#list-unsubscribe}

{% alert note %}
A partir de 15 de fevereiro de 2024, as novas empresas terão o cabeçalho list-unsubscribe (com cancelamento de inscrição com um clique) ativado por padrão.
{% endalert %}

O uso de um cabeçalho list-unsubscribe permite que os destinatários cancelem facilmente a assinatura de e-mails de marketing, exibindo um botão **Unsubscribe (Cancelar assinatura)** na interface do usuário da caixa de correio, e não no corpo da mensagem.

\![]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

Quando um destinatário clica em **Cancelar assinatura**, o provedor de caixa de correio envia a solicitação de cancelamento de assinatura para o destino definido no cabeçalho do e-mail.

A ativação da opção list-unsubscribe é uma prática recomendada de capacidade de entrega e um requisito em alguns dos principais provedores de caixas de correio. Isso incentiva os usuários finais a se removerem com segurança de mensagens indesejadas em vez de pressionar o botão de spam em um cliente de e-mail, o que é prejudicial para a reputação de envio e a capacidade de entrega de e-mails.

### Suporte ao provedor de caixa de correio

A tabela a seguir resume o suporte do provedor de caixa de correio para o cabeçalho "mailto:", URL de lista de cancelamento de assinatura e cancelamento de assinatura com um clique[(RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)).

| Cabeçalho List-unsubscribe | Cabeçalho Mailto: | URL de cancelamento de inscrição na lista | Cancelamento da assinatura com um clique (RFC 8058) | 
| ----- | --- | --- | --- |
| Gmail | Com suporte* | Com suporte | Com suporte |
| Gmail Mobile | Não suportado | Não suportado | Não suportado |
| Apple Mail | Com suporte | Não suportado | Não suportado |
| Outlook.com | Com suporte | Não suportado | Não suportado |
| Yahoo! Correio eletrônico | Com suporte* | Não suportado | Com suporte |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

_\*O Yahoo e o Gmail acabarão por preterir o cabeçalho "mailto:" e oferecerão suporte apenas a um clique._

A exibição do cabeçalho é determinada, em última instância, pelo provedor da caixa de correio. Para verificar se o cabeçalho list-unsubscribe está incluído no e-mail bruto (texto) do destinatário no Gmail, faça o seguinte:

1. Selecione **Mostrar original** no e-mail. Isso abre uma nova guia com a versão bruta do e-mail e seus cabeçalhos.
2. Pesquise por "List-Unsubscribe".

Se o cabeçalho estiver na versão bruta do e-mail, mas não for exibido, o provedor de caixa de correio determinou não mostrar a opção de cancelamento de assinatura, o que significa que não temos mais informações sobre o motivo pelo qual o provedor de caixa de correio não está exibindo o cabeçalho. A visualização do cabeçalho list-unsubscribe é, em última análise, baseada na reputação. Na maioria dos casos, quanto melhor for a reputação do remetente com o provedor da caixa de correio, maior será a probabilidade de o cabeçalho list-unsubscribe aparecer.

### Cabeçalho de cancelamento de assinatura de e-mail em espaços de trabalho

\![Selecionando os "usuários que estão inscritos ou optaram por participar" para quais usuários enviar.]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Quando o recurso de cabeçalho de cancelamento de assinatura de e-mail está ativado, essa configuração se aplica a todo o espaço de trabalho, não ao nível da empresa. Ele é adicionado a campanhas e Canvases configurados para enviar a usuários inscritos ou que optaram por participar, ou a usuários que optaram por participar na etapa **Público-alvo** dos criadores de campanhas e Canvas.

Ao usar o "padrão do espaço de trabalho", o Braze não adiciona o cabeçalho de cancelamento de assinatura com um clique para campanhas consideradas transacionais, que são configuradas para "enviar a todos os usuários, inclusive os que cancelaram a assinatura". Para substituir isso e adicionar o cabeçalho de cancelamento de assinatura com um clique ao enviar para usuários que cancelaram a assinatura, é possível selecionar **Cancelar assinatura globalmente de todos os e-mails** nas configurações de cancelamento de assinatura da lista de um clique no nível da mensagem.

### Cabeçalho padrão list-unsubscribe

{% alert important %}
O Gmail pretende que os remetentes implementem o cancelamento de inscrição com um clique em todas as mensagens comerciais e promocionais enviadas a partir de 1º de junho de 2024. Para obter mais informações, consulte [as diretrizes de remetente do Gmail](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe) e as [Perguntas frequentes sobre diretrizes de remetente de e-mail do Gmail](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages). O Yahoo anunciou um cronograma para o início de 2024 para os requisitos de atualização. Para obter mais informações, consulte [More Secure, Less Spam: Aplicação de padrões de e-mail para uma melhor experiência](https://blog.postmaster.yahooinc.com/).
{% endalert %}

Para usar o recurso de cancelamento de assinatura do Braze para processar os cancelamentos diretamente, selecione **Incluir um cabeçalho de e-mail de lista de cancelamento de assinatura com um clique (mailto e HTTP) para e-mails enviados a usuários inscritos ou opt-in** e selecione **Padrão Braze** como URL e mail-to padrão do Braze. 

Opção para incluir automaticamente um cabeçalho list-unsubscribe em e-mails enviados a usuários inscritos ou opt-in.]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %})

O Braze suporta as seguintes versões do cabeçalho list-unsubscribe:

| Versão de cancelamento de inscrição na lista | Descrição | 
| ----- | --- |
| Um clique (RFC 8058) | Oferece uma maneira direta para os destinatários optarem por não receber e-mails com um único clique. Esse é um requisito do Yahoo e do Gmail para remetentes em massa. |
| URL de cancelamento de inscrição na lista ou HTTPS | Fornece aos destinatários um link que os direciona para uma página da Web onde podem cancelar a assinatura. |
| Correio eletrônico | Especifica um endereço de e-mail como o destino da mensagem de solicitação de cancelamento de assinatura a ser enviada do destinatário para a marca. <br><br> _Para processar solicitações de cancelamento de assinatura de listas de e-mail, essas solicitações precisam incluir o endereço de e-mail armazenado na Braze para o Usuário Final que está cancelando a assinatura. Isso pode ser fornecido pelo "endereço de origem" do e-mail do qual o usuário final está cancelando a assinatura, o assunto codificado ou o corpo codificado do e-mail recebido pelo usuário final do qual ele está cancelando a assinatura. Em casos muito limitados, alguns provedores de caixa de entrada não aderem ao protocolo [RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368), o que faz com que o endereço de e-mail não seja transmitido corretamente. Isso pode fazer com que uma solicitação de cancelamento de inscrição não possa ser processada no Braze._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Quando o Braze recebe uma solicitação de cancelamento de assinatura de lista de um usuário por meio de qualquer um dos métodos acima, o estado global de assinatura de e-mail desse usuário é definido como cancelado. Se não houver uma correspondência, o Braze não processará essa solicitação.

### Cancelamento da assinatura com um clique

O uso do cancelamento de assinatura com um clique para o cabeçalho list-unsubscribe[(RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) se concentra em fornecer uma maneira fácil para os destinatários optarem por não receber e-mails.

### Cancelamento da assinatura da lista com um clique no nível da mensagem

A configuração de cancelamento de assinatura da lista com um clique no nível da mensagem substituirá o conjunto de recursos do cabeçalho de cancelamento de assinatura de e-mail para espaços de trabalho. Aplique o comportamento de cancelamento de assinatura com um clique por campanha ou etapa do Canvas para os seguintes usos:

- Adicionar um cancelamento de assinatura com um clique do Braze para um grupo de assinaturas específico para oferecer suporte a várias marcas/listas em um único espaço de trabalho
- Alternar entre o cancelamento de inscrição padrão do Braze ou o URL personalizado
- Adicione seu URL personalizado de cancelamento de assinatura com um clique
- Omitir o cancelamento de assinatura com um clique nesta mensagem

{% alert note %}
A configuração de cancelamento de assinatura da lista com um clique no nível da mensagem só está disponível ao usar o editor de arrastar e soltar e o editor HTML atualizado. Se você estiver usando o editor HTML anterior, mude para o editor HTML atualizado para usar esse recurso.
{% endalert %}

Em seu editor de e-mail, vá para **Configurações de envio** > **Informações de envio**. Selecione uma das seguintes opções:

- **Usar o padrão do espaço de trabalho**: Usa as configurações **do cabeçalho de cancelamento de assinatura de e-mail** definidas em **Preferências de e-mail**. Todas as alterações feitas nessa configuração serão aplicadas a todas as mensagens.
- **Cancelar a assinatura global de todos os e-mails**: Usa o cabeçalho padrão de cancelamento de inscrição com um clique do Braze. Os usuários que clicarem no botão de cancelamento de assinatura terão seu estado de assinatura de e-mail global definido como "Unsubscribed" (Cancelado).
- **Cancelar a assinatura de um grupo de assinatura específico**: Usa o grupo de assinatura especificado. Os usuários que clicarem no botão de cancelamento de assinatura terão a assinatura cancelada do grupo de assinatura selecionado.
    - Ao selecionar um grupo de assinaturas, adicione o filtro **Grupo de assinaturas** em **Públicos-alvo** para direcionar apenas os usuários que estão inscritos nesse grupo específico. O grupo de assinaturas selecionado para o cancelamento da assinatura com um clique deve corresponder ao grupo de assinaturas que você está segmentando. Se houver uma incompatibilidade no grupo de assinatura, você corre o risco de enviar para um usuário que está tentando cancelar a assinatura de um grupo de assinatura do qual ele já cancelou a assinatura.

{% alert important %}
A configuração **Cancelar assinatura de um grupo de assinatura específico** se aplica apenas ao cabeçalho de cancelamento de assinatura da lista de um clique. O cabeçalho mailto list-unsubscribe não é afetado ao selecionar essa opção. Isso significa que um destinatário que cancelar a assinatura usando esse método registrará um cancelamento de assinatura global, e não um cancelamento de assinatura do grupo de assinatura específico. Para excluir o cabeçalho mailto list-unsubscribe do cancelamento global da inscrição de usuários, ao selecionar essa configuração, entre em contato com [o Suporte]({{site.baseurl}}/support_contact/).
{% endalert %}

- **Personalizado:** Adiciona seu URL personalizado de cancelamento de assinatura com um clique para que você possa processar os cancelamentos diretamente.
- **Excluir cancelamento de inscrição**

{% alert important %}
A exclusão do cancelamento de assinatura com um clique ou de qualquer mecanismo de cancelamento de assinatura só deve ser feita para mensagens transacionais, como redefinições de senha, recibos e e-mails de confirmação.
{% endalert %}

O ajuste dessa configuração substituirá o comportamento padrão de cancelamento de inscrição na lista com um clique nesse e-mail.

\![]({% image_buster /assets/img/email_settings/one_click_list_unsubscribe_message_level.png %}){: style="max-width:70%;"}

#### Requisitos

Se você estiver enviando e-mails usando sua própria funcionalidade de cancelamento de assinatura personalizada, deverá atender aos seguintes requisitos para garantir que o URL de cancelamento de assinatura com um clique que você configurou esteja de acordo com a RFC 8058:

* O URL deve ser capaz de lidar com solicitações POST de cancelamento de assinatura.
* O URL deve começar com `https://`.
* O URL não deve retornar um redirecionamento HTTPS ou um corpo. Os links de cancelamento de assinatura com um clique que vão para uma página de destino ou outro tipo de página da Web não estão em conformidade com a RFC 8058.
* As solicitações POST não devem definir cookies.

Selecione **Cabeçalho personalizado de lista de** cancelamento de assinatura para adicionar seu próprio ponto final de cancelamento de assinatura configurado com um clique e um "mailto:" opcional. O Braze requer uma entrada de URL para oferecer suporte a um cabeçalho personalizado de lista de cancelamento de assinatura porque o HTTP de cancelamento de assinatura com um clique é um requisito do Yahoo e do Gmail para remetentes em massa.

\![]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}

## Anexar linhas de assunto de e-mail

Use a alternância para incluir "[TESTE]" e "[SEMENTE]" nas linhas de assunto de seus e-mails de teste e semente. Isso pode ajudar a identificar quaisquer campanhas de e-mail enviadas como testes.

\![]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## CSS embutido em novos e-mails por padrão

A incorporação de CSS é uma técnica que incorpora automaticamente estilos CSS em seus e-mails e em novos e-mails. Para alguns clientes de e-mail, isso pode melhorar a forma como seus e-mails são renderizados.

A alteração dessa configuração não afetará nenhuma de suas mensagens ou modelos de e-mail existentes. Você pode substituir esse padrão a qualquer momento durante a composição de mensagens ou modelos. Para obter mais informações, consulte [CSS inlining]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/css_inline/).

## Cadastrar novamente os usuários quando o e-mail deles mudar

Você pode reinscrever automaticamente os usuários quando eles mudarem seus endereços de e-mail. Por exemplo, se um usuário do workspace que cancelou a assinatura anteriormente alterar seu endereço de e-mail para um que não esteja na lista de cancelamento de assinatura do Braze, ele será automaticamente inscrito novamente.

\![]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## Páginas de assinatura e rodapés

{% tabs local %}
{% tab Custom Footer %}

Para e-mails comerciais, a [Lei CAN-SPAM](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003) exige que todos os e-mails comerciais incluam uma opção de cancelamento de assinatura. Com as configurações de rodapé personalizadas, você pode manter a conformidade com a CAN-SPAM e, ao mesmo tempo, personalizar o rodapé de desativação de e-mail. Para manter a conformidade, você deve adicionar seu rodapé personalizado a todos os e-mails enviados como parte das campanhas para esse espaço de trabalho.

Observe os seguintes requisitos ao criar um rodapé personalizado para suas mensagens de e-mail:
- Deve incluir um URL de cancelamento de assinatura e um endereço físico para correspondência.
- Deve ter menos de 100 KB.

\![]({% image_buster /assets/img/email_settings/custom_footer.png %})

Para saber mais sobre o modelo Liquid de rodapé personalizado, consulte nossa documentação sobre [rodapés personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

{% endtab %}
{% tab Custom Unsubscribe Page %}

O Braze permite que você defina uma **página de cancelamento de inscrição personalizada** com seu próprio HTML. Essa página aparecerá depois que um usuário tiver selecionado cancelar a assinatura na parte inferior de um e-mail. Observe que essa página deve ter menos de 750 KB. 

\![]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

Saiba mais sobre as práticas recomendadas para o gerenciamento de listas de e-mail em [Gerenciamento de assinaturas de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% tab Custom Opt-In Page %}

Você pode criar uma página de opt-in personalizada usando seu próprio HTML. Incluir isso em seu e-mail pode ser especialmente benéfico se você quiser que sua marca e sua mensagem permaneçam consistentes durante todo o ciclo de vida do usuário. Observe que essa página deve ter menos de 750 KB. 

\![]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

Saiba mais sobre as práticas recomendadas para o gerenciamento de listas de e-mail em [Gerenciamento de assinaturas de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% endtabs %}

## Perguntas frequentes

### Cancelamento da assinatura com um clique

{% details Can the one-click unsubscribe URL (via list-unsubscribe header) link to a preference center? %}
Não, isso não está de acordo com a RFC 8058, o que significa que você não estará em conformidade com o requisito de cancelamento de assinatura com um clique do Yahoo e do Gmail.
{% enddetails %}

{% details Why do I receive the error message "Your email body does not include an unsubscribe link" when composing my preference center? %}
Um centro de preferências não é considerado um link de cancelamento de assinatura. Seus destinatários de e-mail devem ter a opção de cancelar a assinatura de qualquer e-mail comercial para manter a conformidade com a CAN-SPAM.
{% enddetails %}

{% details Will I need to edit past email campaigns and Canvases to apply the one-click unsubscribe setting after enabling it? %}
Se você não tiver nenhum dos casos de uso para a configuração de cancelamento de assinatura da lista com um clique no nível da mensagem, não será necessário realizar nenhuma ação, desde que a configuração esteja ativada em **Preferências de e-mail**. O Braze adicionará automaticamente os cabeçalhos de cancelamento de inscrição com um clique a todas as mensagens de marketing e promocionais enviadas. No entanto, se você precisar configurar o comportamento de cancelamento de assinatura com um clique em nível de mensagem, será necessário atualizar as campanhas anteriores e as etapas do Canvas com o e-mail de acordo.
{% enddetails %}

{% details I can see the list-unsubscribe and one-click unsubscribe header in the original message or raw data, but why don't I see the Unsubscribe button in Gmail or Yahoo? %}
O Gmail e o Yahoo decidem, em última instância, se exibem ou não o cabeçalho de lista de cancelamento de inscrição ou de cancelamento de inscrição com um clique. Para novos remetentes ou remetentes com baixa reputação de remetente, isso pode ocasionalmente fazer com que o botão de cancelamento de assinatura não seja exibido.
{% enddetails %}

{% details Does the custom one-click unsubscribe header support Liquid? %}
Sim, há suporte para a lógica líquida e condicional para permitir URLs dinâmicos de cancelamento de assinatura com um clique para o cabeçalho.
{% enddetails %}

{% alert tip %}
Se estiver adicionando lógica condicional, evite ter valores de saída que adicionem espaços em branco ao seu URL, pois o Braze não remove esses espaços em branco.
{% endalert %}

### Cancelamento da assinatura da lista com um clique no nível da mensagem

{% details If I add the email headers for one-click manually, and I have the email unsubscribe header turned on, what is the expected behavior? %}
Os cabeçalhos de e-mail adicionados para a lista de cancelamento de inscrição com um clique serão aplicados a todos os envios futuros dessa campanha.
{% enddetails %}

{% details Why do subscription groups have to match across message variants in order to launch? %}
Para uma campanha com teste A/B, o Braze enviará aleatoriamente a um usuário uma das variantes. Se você tiver dois grupos de assinatura diferentes definidos na mesma campanha (a Variante A está definida para o Grupo de Assinatura A e a Variante B está definida para o Grupo de Assinatura B), não podemos garantir que os usuários que estiverem inscritos apenas no Grupo de Assinatura B receberão a Variante B. Pode haver um cenário em que os usuários estejam cancelando a assinatura de um grupo de assinatura do qual já tenham optado por sair.
{% enddetails %}

{% details The email unsubscribe header setting is turned off in Email Preferences, but in my campaign's sending info, the one-click list-unsubscribe setting is set to "Use workspace default". Is this a bug? %}
Não. Se a configuração do espaço de trabalho estiver desativada e a configuração da mensagem estiver definida como **Usar padrão do espaço de trabalho**, o Braze seguirá o que está configurado em **Preferências de e-mail**. Isso significa que não adicionaremos o cabeçalho de cancelamento de inscrição com um clique para a campanha.
{% enddetails %}

{% details What happens if a subscription group is archived? Will this break the one-click unsubscribe on emails sent? %}
Se um grupo de assinaturas referenciado em **Informações de envio** para um clique for arquivado, o Braze ainda processará os cancelamentos de assinatura de um clique. O grupo de assinatura não será mais exibido no painel (filtro de segmento, perfil de usuário e áreas semelhantes).
{% enddetails %}

{% details Is the one-click unsubscribe setting available for email templates? %}
Não, no momento não temos planos de adicionar isso aos modelos de e-mail, pois esses modelos não são atribuídos a um domínio de envio. Se você estiver interessado nesse recurso para modelos de e-mail, envie [comentários sobre o produto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% enddetails %}

{% details Does this feature check that the one-click unsubscribe URL added to the custom option is valid? %}
Não, não verificamos nem validamos nenhum link no painel de controle do Braze. Certifique-se de testar adequadamente seu URL antes do lançamento.
{% enddetails %}


