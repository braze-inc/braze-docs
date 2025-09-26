---
nav_title: Preferências de e-mail
article_title: Preferências de e-mail
page_type: reference
page_order: 14
description: "Este artigo de referência aborda as preferências de e-mail no dashboard da Braze, incluindo configurações de envio, pixels de rastreamento de abertura, página de inscrição e rodapés, e muito mais."
tool: Dashboard
channel: email

---

# Preferências de e-mail

> Preferências de e-mail é onde você pode definir configurações específicas de envio de e-mail, como rodapés personalizados, páginas personalizadas de aceitação e exclusão e muito mais. Incluir essas opções em seus e-mails de saída proporciona uma experiência fluida e coesa para seus usuários.

**As Preferências de e-mail** podem ser encontradas em **Configurações no dashboard**.

## Envio de configuração

As configurações de e-mail na seção **Configuração de envio de** e-mail determinam quais detalhes são incluídos nas suas campanhas de e-mail. Em particular, essas configurações estão relacionadas principalmente ao que o usuário vê quando recebe um e-mail do Braze.

### Configurações de envio de e-mail

Ao definir suas configurações de e-mail, suas configurações de e-mail de saída identificam qual nome e endereço de e-mail são usados quando o Braze envia e-mails para seus usuários.

{% tabs local %}
{% tab Endereço do nome de exibição %}

Nessa seção, é possível adicionar os nomes e endereços de e-mail que podem ser usados quando o Braze envia e-mails para seus usuários. Os nomes de exibição e os endereços de e-mail estarão disponíveis nas opções **Editar informações de envio** à medida que você cria sua campanha de e-mail. Observe que as atualizações feitas nas configurações de e-mail de saída não afetam retroativamente os envios existentes. 

![]({% image_buster /assets/img/email_settings/display_name_address.png %})

{% endtab %}
{% tab Endereço de resposta %}

A adição de um endereço de e-mail nessa seção permite selecioná-lo como endereço de resposta para a sua campanha de e-mail. Você também pode tornar um endereço de e-mail o padrão selecionando **Tornar padrão**. Esses endereços de e-mail estarão disponíveis nas opções **Editar informações de envio à** medida que você cria sua campanha de e-mail.

![]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

{% endtab %}
{% tab Endereço BCC %}

Essa seção permite adicionar e gerenciar endereços BCC que podem ser anexados às mensagens de e-mail enviadas pelo Braze. Endereços BCC estão disponíveis apenas para SendGrid e SparkPost. Como alternativa aos endereços BCC, recomendamos usar [envio de mensagens]({{site.baseurl}}/user_guide/data/export_braze_data/message_archiving/) para salvar uma cópia das mensagens enviadas aos usuários para fins de arquivamento ou conformidade.

Adicionar um endereço BCC a uma mensagem de e-mail enviará uma cópia idêntica da mensagem que seu usuário recebe para sua caixa de entrada BCC. Esta é uma ferramenta útil para reter cópias das mensagens que você enviou aos seus usuários para requisitos de conformidade ou questões de suporte ao cliente. Os e-mails BCC não são incluídos nos relatórios e na análise de dados de e-mail.

{% alert important %}
Adicionar um endereço BCC à sua campanha ou Canvas resultará na duplicação de seus e-mails faturáveis para a campanha ou componente Canvas, uma vez que a Braze enviará uma mensagem ao seu usuário e uma ao seu endereço BCC.
{% endalert %}

![Seção Endereço BCC da guia Configurações de e-mail.]({% image_buster /assets/img/email_settings/bcc_address.png %}){: style="max-width:75%;" }

Depois de adicionar um endereço, ele estará disponível para seleção ao compor um e-mail em campanhas ou etapas do Canvas. Selecione **Tornar padrão** ao lado de um endereço para definir que esse endereço seja selecionado por padrão ao iniciar uma nova campanha de e-mail ou componente do Canva. Para substituir isso no nível da mensagem, você pode selecionar **No BCC** ao configurar a mensagem.

Se você precisar que todas as mensagens de e-mail enviadas pelo Braze tenham um endereço BCC incluído, poderá selecionar a opção **Exigir um endereço BCC para todas as suas campanhas de e-mail**. Isso exigirá que você selecione um endereço padrão, que será selecionado automaticamente em novas campanhas de e-mail ou etapas do Canvas. O endereço padrão também será adicionado automaticamente a todas as mensagens disparadas por meio de nossa API REST. Não há necessidade de alterar a solicitação de API existente para incluir o endereço.

{% endtab %}
{% endtabs %}

## Pixel de rastreamento de abertura

[![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

O pixel de rastreamento de abertura de abertura de e-mail é uma imagem invisível de 1 x 1 px que é inserida automaticamente no HTML de seu e-mail. Esse pixel ajuda a Braze a detectar se os usuários finais abriram seu e-mail. As informações de abertura de e-mails podem ser muito úteis, ajudando os usuários a determinar estratégias de marketing eficazes ao compreender as taxas de abertura correspondentes.

### Colocação do pixel de rastreamento

O comportamento padrão do Braze é anexar o pixel de rastreamento à parte inferior de seu e-mail. Para a maioria dos usuários, esse é o local ideal para colocar o pixel. Embora o pixel já seja estilizado para causar o mínimo possível de alterações visuais, quaisquer alterações visuais não intencionais seriam menos visíveis na parte inferior de um e-mail. Esse também é o padrão para provedores de e-mail, como SendGrid e SparkPost.

### Alteração do local do pixel de rastreamento

Atualmente, a Braze oferece suporte para substituir o local padrão do pixel de rastreamento de abertura do ESP (a última tag em `<body>` de um e-mail) para movê-lo para a primeira tag em `<body>`.
  
!["Seção de Pixel de Rastreamento de Abertura" com as opções para mover para SendGrid, SparkPost ou Amazon SES.]({% image_buster /assets/img/open_pixel.png %}){: style="max-width:80%;" }

Para alterar o local:

1. No Braze, acesse **Configurações** > **Preferências de e-mail**.
2. Selecione uma das seguintes opções: **Mover para SendGrid**, **Mover para SparkPost**, ou **Mover para Amazon SES**
3. Selecione **Salvar**.

Uma vez salvo, o Braze enviará instruções especiais ao ESP para colocar o pixel de rastreamento de abertura na parte superior de todos os e-mails em HTML.
  
{% alert important %}
A capacitação SSL envolverá a URL do pixel de rastreamento com HTTPS em vez de HTTP. Se o seu SSL estiver mal configurado, isso pode afetar a eficácia do pixel de rastreamento.
{% endalert %}

## Cabeçalho "List-unsubscribe {#list-unsubscribe}

{% alert note %}
A partir de 15 de fevereiro de 2024, as novas empresas terão o cabeçalho list-unsubscribe (com cancelamento de inscrição com um clique) ativado por padrão.
{% endalert %}

O uso de um cabeçalho list-unsubscribe permite que os destinatários cancelem facilmente a inscrição em e-mails de marketing, exibindo um botão **Cancelar inscrição** na interface do usuário da caixa de correio, e não no corpo da mensagem.

![]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

Quando um destinatário clica em **Cancelar inscrição**, o provedor de caixa de e-mail envia a solicitação de cancelamento da inscrição para os destinos definidos no cabeçalho do e-mail.

Ativar o cancelamento da inscrição na lista é uma prática recomendada de entregabilidade e um requisito em alguns dos principais provedores de caixa de e-mail. Isso incentiva os usuários finais a se removerem com segurança de mensagens indesejadas em vez de pressionar o botão de spam em um cliente de e-mail, o que é prejudicial para a reputação de envio e entregabilidade de e-mail.

### Suporte ao provedor de caixa de e-mail

A tabela a seguir resume o suporte do provedor de caixa de e-mail para o cabeçalho "mailto:", URL de cancelamento de inscrição na lista e cancelamento de inscrição com um clique[(RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)).

| Cabeçalho "List-unsubscribe | Cabeçalho Mailto: | URL de cancelamento da inscrição na lista | Cancelamento de inscrição com um clique (RFC 8058) | 
| ----- | --- | --- | --- |
| Gmail | Com suporte* | Com suporte | Com suporte |
| Gmail Mobile | Não suportado | Não suportado | Não suportado |
| Mail da Apple | Com suporte | Não suportado | Não suportado |
| Outlook.com | Com suporte | Não suportado | Não suportado |
| Yahoo! Correio eletrônico | Com suporte* | Não suportado | Com suporte |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

_\*O Yahoo e o Gmail acabarão por preterir o cabeçalho "mailto:" e oferecerão suporte apenas a um clique._

A exibição do cabeçalho é determinada, em última análise, pelo provedor de caixa de e-mail. Para verificar se o cabeçalho list-unsubscribe está incluído no e-mail bruto (texto) do destinatário no Gmail, faça o seguinte:

1. Selecione **Mostrar Original** no e-mail. Isso abre uma nova guia com a versão bruta do e-mail e seus cabeçalhos.
2. Pesquise por "List-Unsubscribe".

Se o cabeçalho estiver na versão bruta do e-mail, mas não for exibido, o provedor de caixa de e-mail determinou não mostrar a opção de cancelar inscrição, o que significa que não temos mais insights sobre por que o provedor de caixa de e-mail não está exibindo o cabeçalho. A visualização do cabeçalho list-unsubscribe é, em última análise, baseada na reputação. Na maioria dos casos, quanto melhor for a reputação de seu remetente na caixa de entrada, menor será a probabilidade de o cabeçalho list-unsubscribe aparecer.

### Cabeçalho de cancelamento de inscrição de e-mail em espaços de trabalho

![Selecionando os "usuários que estão inscritos ou optaram por participar" para quais usuários enviar.]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Quando o recurso de cabeçalho de cancelamento de inscrição por e-mail está ativado, essa configuração se aplica a todo o espaço de trabalho, não ao nível da empresa. É adicionado a campanhas e Canvases que estão configurados para enviar a usuários que estão inscritos ou optaram por participar, ou usuários que optaram por participar na etapa **público-alvo** dos construtores de campanha e Canvas.

Ao usar o "padrão do espaço de trabalho", a Braze não adiciona o cabeçalho de cancelamento de inscrição com um clique para campanhas que são consideradas transacionais, que estão configuradas para "enviar para todos os usuários, incluindo usuários não inscritos". Para substituir isso e adicionar o cabeçalho de cancelamento de inscrição com um clique ao enviar para usuários não inscritos, você pode selecionar **Cancelar inscrição globalmente de todos os e-mails** nas configurações de cabeçalho de cancelamento de inscrição com um clique no nível da mensagem.

### Cabeçalho padrão list-unsubscribe

{% alert important %}
O Gmail pretende que os remetentes implementem o cancelamento de inscrição com um clique para todas as mensagens comerciais e promocionais enviadas a partir de 1º de junho de 2024. Para saber mais, consulte [as diretrizes de remetente do Gmail](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe) e [as Perguntas frequentes sobre as diretrizes de remetente de e-mail do Gmail](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages). O Yahoo anunciou um cronograma para o início de 2024 para os requisitos de atualização. Para saber mais, consulte [Mais Seguro, Menos Spam: Envio de e-mail com padrões para uma melhor experiência](https://blog.postmaster.yahooinc.com/).
{% endalert %}

Para usar o recurso de cancelamento de inscrição da Braze para processar cancelamentos de inscrição diretamente, selecione **Incluir um cabeçalho de cancelamento de inscrição por e-mail com um clique (mailto e HTTP) para e-mails enviados a usuários inscritos ou que optaram por participar** e selecione **Padrão da Braze** como a URL padrão da Braze e mail-to. 

![Opção para incluir automaticamente um cabeçalho de cancelar inscrição para e-mails enviados a usuários inscritos ou que optaram por receber.]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %})

O Braze oferece suporte às seguintes versões do cabeçalho list-unsubscribe:

| Versão de cancelamento de inscrição na lista | Descrição | 
| ----- | --- |
| Um clique (RFC 8058) | Oferece uma maneira simples para os destinatários cancelarem a inscrição de e-mails com um único clique. Esse é um requisito do Yahoo e do Gmail para remetentes em massa. |
| URL de cancelamento de inscrição na lista ou HTTPS | Fornece aos destinatários um link que os direciona para uma página da Web onde podem cancelar a inscrição. |
| Mailto | Especifica um endereço de e-mail como o destino para a mensagem de solicitação de cancelamento de inscrição a ser enviada do destinatário para a marca. <br><br> _Para processar solicitações de cancelamento de inscrição em listas de e-mail, essas solicitações precisam incluir o endereço de e-mail do usuário final que está cancelando a inscrição, conforme armazenado na Braze. Isso pode ser fornecido pelo "endereço de remetente" do e-mail de onde o Usuário Final está cancelando a inscrição, o assunto codificado ou o corpo codificado do e-mail recebido pelo Usuário Final do qual estão cancelando a inscrição. Em casos muito limitados, alguns provedores de caixa de entrada não seguem o [RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368) protocolo, resultando no endereço de e-mail não sendo passado corretamente. Isso pode fazer com que uma solicitação de cancelamento de inscrição não possa ser processada na Braze._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Quando o Braze recebe uma solicitação de cancelamento de inscrição em uma lista de um usuário por meio de qualquer um dos métodos acima, o estado global de inscrição de e-mail desse usuário é definido como cancelado. Se não houver uma correspondência, o Braze não processará essa solicitação.

### Cancelar inscrição com um clique

Usar o cancelamento de inscrição com um clique para o cabeçalho de cancelar inscrição ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) foca em fornecer uma maneira fácil para os destinatários cancelarem a inscrição de e-mails.

### Cancelamento da inscrição com um clique na lista no nível da mensagem

A configuração de cancelamento de inscrição na lista de um clique no nível da mensagem substituirá o conjunto de recursos do cabeçalho de cancelamento de inscrição de e-mail para espaços de trabalho. Aplique o comportamento de cancelamento de inscrição com um clique por campanha ou etapa do Canva para os seguintes usos:

- Adicionar um cancelamento de inscrição com um clique do Braze para um grupo de inscrições específico para oferecer suporte a várias marcas/listas em um espaço de trabalho
- Alternar entre o cancelamento de inscrição padrão do Braze ou o URL personalizado
- Adicione seu URL personalizado de cancelamento de inscrição com um clique
- Omitir o cancelamento de inscrição com um clique nesta mensagem

{% alert note %}
A configuração de cancelamento de inscrição com um clique no nível da mensagem está disponível apenas ao usar o editor de arrastar e soltar e o editor de HTML atualizado. Se estiver usando o editor de HTML anterior, mude para o editor de HTML atualizado para usar esse recurso.
{% endalert %}

Em seu editor de e-mail, acesse **Configurações de envio** > **Informações de envio**. Selecione uma das seguintes opções:

- **Usar o espaço de trabalho padrão**: Usa as configurações **do cabeçalho de cancelamento de inscrição de e-mail** definidas em **Preferências de e-mail**. As alterações feitas nesta configuração serão aplicadas a todas as mensagens.
- **Cancelar inscrição globalmente de todos os e-mails**: Usa o cabeçalho de cancelamento de inscrição com um clique padrão da Braze. Os usuários que clicarem no botão de cancelamento da inscrição terão seu estado de inscrição global de e-mail definido como "Cancelado".
- **Cancelar inscrição em um grupo de inscrições específico**: Usa o grupo de inscrições especificado. Os usuários que clicarem no botão cancelar inscrição terão a inscrição cancelada no grupo de inscrições selecionado.
    - Ao selecionar um grupo de inscrições, adicione o filtro **Grupo de inscrições** em **Públicos-alvo** para direcionar apenas os usuários que estão inscritos nesse grupo específico. O grupo de inscrições selecionado para cancelar inscrição com um clique deve corresponder ao grupo de inscrições que está sendo direcionado. Se houver uma incompatibilidade no grupo de inscrições, você pode correr o risco de enviar para um usuário que está tentando cancelar a inscrição de um grupo de inscrições do qual já está cancelado.
- **Personalizado:** Adiciona seu URL personalizado de cancelamento de inscrição com um clique para que você processe diretamente cancelamentos de inscrição.
- **Excluir opção de cancelamento de inscrição**

{% alert important %}
A exclusão do cancelamento de inscrição com um clique ou de qualquer mecanismo de cancelamento de inscrição só deve ser feita para envios de mensagens transacionais, como redefinições de senha, recibos e e-mails de confirmação.
{% endalert %}

O ajuste dessa configuração substituirá o comportamento padrão de cancelamento de inscrição na lista com um clique nesse e-mail.

![]({% image_buster /assets/img/email_settings/one_click_list_unsubscribe_message_level.png %}){: style="max-width:70%;"}

#### Solicitações

Se estiver enviando e-mails usando sua própria funcionalidade personalizada de cancelamento de inscrição, é necessário atender aos seguintes requisitos para garantir que o URL de cancelamento de inscrição com um clique que você configurou esteja de acordo com a RFC 8058:

* O URL deve ser capaz de lidar com solicitações POST de cancelamento de inscrição.
* O URL deve começar com `https://`.
* O URL não deve retornar um redirecionamento HTTPS ou um corpo. Os links de cancelamento de inscrição com um clique que acessam uma landing page ou outro tipo de página da Web não estão em conformidade com a RFC 8058.
* As solicitações POST não devem definir cookies.

Selecione **Cabeçalho personalizado de lista de** cancelamento de inscrição para adicionar seu próprio ponto final configurado de cancelamento de inscrição com um clique e um "mailto:" opcional. O Braze requer uma entrada de URL para suportar um cabeçalho personalizado de lista de cancelamento de inscrição porque o HTTP de cancelamento de inscrição com um clique é um requisito do Yahoo e do Gmail para remetentes em massa.

![]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}

## Anexar linhas de assunto de e-mail

Use o botão de alternância para incluir "[TEST]" e "[SEED]" nas linhas de assunto de seus e-mails de teste e de propagação. Isso pode ajudar a identificar quaisquer campanhas de e-mail enviadas como testes.

![]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## CSS embutido em novos e-mails por padrão

O inlining de CSS é uma técnica que inlining automaticamente estilos CSS para seus e-mails e novos e-mails. Em alguns clientes de e-mail, isso pode melhorar a visualização dele para o usuário.

Essa configuração não afeta mensagens ou modelos de e-mail existentes. É possível substituir esse padrão a qualquer momento durante a composição de mensagens ou modelos. Para saber mais, consulte [CSS inlining]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/css_inline/).

## Cadastrar novamente os usuários quando o e-mail deles mudar

É possível reinscrever automaticamente os usuários quando eles mudarem seus endereços de e-mail. Por exemplo, se um usuário do espaço de trabalho que cancelou a inscrição anteriormente alterar seu endereço de e-mail para um que não esteja na lista de cancelamento de inscrição do Braze, ele será automaticamente inscrito novamente.

![]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## Páginas de inscrição e rodapés

{% tabs local %}
{% tab Rodapé personalizado %}

Para e-mails comerciais, a [Lei CAN-SPAM](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003) exige que todos os e-mails comerciais incluam uma opção de cancelamento de inscrição. Com as configurações de rodapé personalizadas, é possível manter a conformidade com a CAN-SPAM e, ao mesmo tempo, personalizar o rodapé de envio de e-mail para aceitação. Para manter a conformidade, você deve adicionar seu rodapé personalizado a todos os e-mails enviados como parte das campanhas para esse espaço de trabalho.

Observe os seguintes requisitos ao criar um rodapé personalizado para o envio de mensagens por e-mail:
- Deve incluir um URL para cancelar inscrição e um endereço físico para correspondência.
- Deve ter menos de 100 KB.

![]({% image_buster /assets/img/email_settings/custom_footer.png %})

Para saber mais sobre modelos Liquid de rodapés personalizados, consulte nossa documentação sobre [rodapés personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

{% endtab %}
{% tab Página personalizada de cancelamento de inscrição %}

O Braze permite que você defina uma **página de cancelamento de inscrição personalizada** com seu próprio HTML. Essa página aparecerá depois que um usuário tiver selecionado cancelar inscrição na parte inferior de um e-mail. Note que essa página deve ter menos de 750 KB. 

![]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

Saiba mais sobre as práticas recomendadas para o gerenciamento de listas de e-mail em [Gerenciamento de inscrições de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% tab Página de aceitação personalizada %}

Você pode criar uma página de aceitação personalizada usando seu próprio HTML. Incluir isso no seu envio de e-mail pode ser especialmente benéfico se quiser que a marca e a mensagem permaneçam consistentes durante todo o ciclo de vida do usuário. Note que essa página deve ter menos de 750 KB. 

![]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

Saiba mais sobre as práticas recomendadas para o gerenciamento de listas de e-mail em [Gerenciamento de inscrições de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% endtabs %}

## Perguntas frequentes

### Cancelar inscrição com um clique

{% details O URL de cancelamento de inscrição com um clique (via cabeçalho list-unsubscribe) pode ser vinculado a uma central de preferências? %}
Não, isso não está de acordo com a RFC 8058, o que significa que você não estará em conformidade com o requisito de cancelamento de inscrição com um clique do Yahoo e do Gmail.
{% enddetails %}

{% details Por que recebo a mensagem de erro "O corpo do seu e-mail não inclui um link de cancelamento de inscrição" ao criar minha central de preferências? %}
Uma Central de Preferências não é considerada um link de cancelamento de inscrição. Seus destinatários de e-mail devem ter a opção de cancelar inscrição de qualquer e-mail comercial para permanecer em conformidade com a CAN-SPAM.
{% enddetails %}

{% details Precisarei editar campanhas de e-mail e Canvas anteriores para aplicar a configuração de cancelamento de inscrição com um clique depois de ativá-la? %}
Se você não tiver nenhum dos casos de uso para a configuração de cancelamento de inscrição na lista de um clique no nível da mensagem, não há nenhuma ação necessária, desde que a configuração esteja ativada em **Preferências de e-mail**. O Braze adicionará automaticamente os cabeçalhos de cancelamento de inscrição com um clique a todas as mensagens de marketing e promocionais enviadas. No entanto, se você precisar configurar o comportamento de cancelamento de inscrição com um clique em nível de mensagem, precisará atualizar campanhas anteriores e etapas do Canvas com o e-mail de acordo.
{% enddetails %}

{% details Posso ver o cabeçalho list-unsubscribe e one-click unsubscribe na mensagem original ou nos dados brutos, mas por que não vejo o botão Unsubscribe no Gmail ou no Yahoo? %}
O Gmail e o Yahoo decidem, em última instância, se exibem ou não o cabeçalho de cancelamento de inscrição em lista ou de cancelamento de inscrição com um clique. Para novos remetentes ou remetentes com baixa reputação de remetente, isso pode ocasionalmente fazer com que o botão de cancelar inscrição não seja exibido.
{% enddetails %}

{% details O cabeçalho personalizado de cancelamento de inscrição com um clique é compatível com o Liquid? %}
Sim, o Liquid e a lógica condicional são compatíveis para permitir URLs dinâmicos de cancelamento de inscrição com um clique para o cabeçalho.
{% enddetails %}

{% alert tip %}
Se você estiver adicionando lógica condicional, evite ter valores de saída que adicionem espaços em branco à sua URL, pois o Braze não remove esses espaços em branco.
{% endalert %}

### Cancelamento da inscrição com um clique na lista no nível da mensagem

{% details Se eu adicionar os cabeçalhos de e-mail para um clique manualmente, e eu tiver o cabeçalho de cancelar inscrição de e-mail ativado, qual é o comportamento esperado? %}
Os cabeçalhos de e-mail adicionados para a lista de cancelamento de inscrição com um clique serão aplicados a todos os envios futuros dessa campanha.
{% enddetails %}

{% details Por que os grupos de inscrições precisam corresponder às variantes de mensagens para serem lançados? %}
Para uma campanha com Testes A/B, o Braze enviará aleatoriamente a um usuário uma das variantes. Se você tiver dois grupos de inscrições diferentes configurados na mesma campanha (Variante A está configurada para o Grupo de Inscrições A, e Variante B está configurada para o Grupo de Inscrições B), não podemos garantir que os usuários que estão apenas inscritos no Grupo de Inscrições B receberão a Variante B. Pode haver um cenário em que os usuários estão cancelando a inscrição de um grupo de inscrições do qual já optaram por sair.
{% enddetails %}

{% details A configuração do cabeçalho de cancelamento de inscrição de e-mail está desativada nas Preferências de e-mail, mas nas informações de envio da minha campanha, a configuração de cancelamento de inscrição na lista de um clique está definida como "Usar padrão do espaço de trabalho". Isso é um bug? %}
Se a configuração de espaço de trabalho estiver desativada e a configuração de mensagem estiver definida como **Usar espaço de trabalho padrão**, a Braze seguirá o que está configurado em **Preferências de e-mail**. Isso significa que não adicionaremos o cabeçalho de cancelar inscrição com um clique para a campanha.
{% enddetails %}

{% details O que acontece se um grupo de inscrições for arquivado? Isso interromperá o cancelamento de inscrição com um clique nos e-mails enviados? %}
Se um grupo de inscrições referenciado em **Informações de envio** para um clique for arquivado, o Braze ainda processará os cancelamentos de inscrição de um clique. O grupo de inscrições não será mais exibido no dashboard (filtro de segmento, perfil de usuário e áreas semelhantes).
{% enddetails %}

{% details A configuração de cancelar inscrição com um clique está disponível para modelos de e-mail? %}
Não, atualmente não temos planos de adicionar isso para modelos de e-mail, pois esses modelos não estão atribuídos a um domínio de envio. Se você tiver interesse nesse recurso para modelos de e-mail, envie [um feedback sobre o produto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% enddetails %}

{% details Esse recurso verifica se o URL de cancelamento de inscrição com um clique adicionado à opção personalizada é válido? %}
Não, não verificamos nem validamos nenhum link no dashboard do Braze. Certifique-se de testar adequadamente seu URL antes do lançamento.
{% enddetails %}


