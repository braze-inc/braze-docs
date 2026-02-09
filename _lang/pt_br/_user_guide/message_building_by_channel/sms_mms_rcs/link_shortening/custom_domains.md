---
nav_title: Domínios personalizados de autoatendimento
article_title: Domínios personalizados de autoatendimento
page_order: 0
description: "Esta página aborda como usar domínios personalizados com encurtamento de links para personalizar a aparência de seus URLs encurtados."
page_type: reference
alias: "/custom_domains/"
tool:
  - Campaigns
channel:
  - SMS
---

# Domínios personalizados de autoatendimento

> Esta página aborda como configurar seus próprios domínios personalizados no dashboard do Braze. Os domínios personalizados permitem usar um link encurtado de marca que reflete a identidade da sua marca em vez de um link encurtado genérico ou o domínio Braze (`brz.ai`), melhorando a confiança do usuário e o engajamento da campanha com links de SMS.

Os domínios personalizados de autoatendimento permitem que você configure e gerencie seus próprios domínios personalizados para SMS, RCS e WhatsApp, diretamente do seu dashboard do Braze. Você pode adicionar, monitorar e gerenciar facilmente até 10 domínios personalizados em um só lugar.

## Benefícios dos domínios personalizados de autoatendimento

- **Configuração simplificada:** Configure seus domínios na página **Company Settings (Configurações da empresa** ), reduzindo o tempo de configuração.
- **Transparência aprimorada:** Receba atualizações em tempo real sobre o status de configuração de seu domínio por meio de banners no dashboard.
- **Notificações proativas:** Receba alertas imediatos quando seu domínio personalizado estiver conectado ou se ocorrer algum erro de configuração.

## Requisitos de domínio

- Os domínios devem ser adquiridos, pertencentes e gerenciados por você. Isso pode ser feito por meio de um registrador de domínios, como GoDaddy, Amazon Route 53 ou Google Domains.
- O domínio usado para esse recurso deve ser:
  - Único (diferente do domínio de seu site)
  - Não pode ser usado para hospedar nenhum conteúdo da Web
    - Você também pode usar subdomínios exclusivos. Por exemplo, o domínio `braze.com` poderia ter subdomínios de `sms.braze.com` ou `whatsapp.braze.com`.

## Delegação de seu domínio personalizado

Solicitamos que você delegue seu domínio personalizado ao Braze para que possamos facilitar o roteamento adequado e a compatibilidade da infraestrutura com nossos serviços de encurtamento de links e rastreamento de cliques. Quando você delega seu domínio à Braze, nós tratamos automaticamente da renovação do certificado para evitar um lapso no serviço. 

## Adição de um domínio personalizado

1. No Braze, acesse **Configurações da empresa** > **SMS/RCS e domínios de aplicativos de envio de mensagens**.
![Página "SMS/RCS and Messaging Apps Domains" com vários domínios listados.]({% image_buster /assets/img/main_page.png %})

{: start="2"}
2\. Selecione **Add Domain (Adicionar domínio** ) para iniciar a configuração de um novo domínio personalizado.
3\. Insira o domínio personalizado que você comprou em nossa entrada no app, que usa nossa lógica de validação existente para a formatação adequada e, em seguida, selecione **Next** e **Submit**.

![Botão "Add Domain" (Adicionar domínio) na página "SMS/RCS and Messaging Apps Domains" (Domínios de SMS/RCS e de envio de mensagens).]({% image_buster /assets/img/custom_domain_button.png %}){: style="max-width:70%;"}

{: start="4"}
4\. Peça à sua equipe técnica (como engenharia ou TI) que atualize sua configuração de DNS com os detalhes do registro DNS da Cloudflare que são exibidos. Sua equipe técnica deve atualizar os registros DNS com esses detalhes em até 45 dias.
  - Se precisar de mais tempo para atualizar os registros DNS, é possível reiniciar o processo e gerar um novo conjunto de registros DNS para o seu domínio.

O Braze pesquisará sua configuração de DNS aproximadamente a cada 30 minutos para verificar se há atualizações.

![Seção "Registro DNS" com 3 etapas a serem concluídas para finalizar a configuração do seu domínio.]({% image_buster /assets/img/dns_record.png %})

{% alert note %}
O progresso de seu domínio é salvo automaticamente. Se precisar sair no meio do fluxo, você poderá retomá-lo mais tarde selecionando a entrada de domínio pendente na página **Domínios de SMS/RCS e de aplicativos de envio de mensagens**.
{% endalert %}

### Gerenciamento e uso contínuos

Depois que seu domínio for verificado, seus domínios personalizados aparecerão na tabela da página **SMS/RCS and Messaging Apps Domains** com indicadores de status. Você pode usar imediatamente os domínios conectados em vários grupos de inscrições, espaços de trabalho e canais de SMS, RCS e WhatsApp.

![Lista de domínios e status personalizados.]({% image_buster /assets/img/custom_domain_statuses.png %}){: style="max-width:60%;"}

O monitoramento ao vivo o alertará no dashboard do Braze se algum dos seus domínios ativos tiver um problema, para que seus links personalizados permaneçam utilizáveis. Se encontrar algum problema, consulte os detalhes de erro no app ou entre em contato com [o suporte]({{site.baseurl}}/braze_support/) da Braze para obter assistência.

## Atribuir domínios personalizados a grupos de inscrições

Depois de configurados, os domínios personalizados podem ser atribuídos a um ou vários grupos de inscrições de SMS, RCS e WhatsApp.

1. Acesse **Público** > **Gerenciamento de grupos de inscrições**.
2. Encontre e selecione seu grupo de inscrições na lista.
3. Em **Detalhes do grupo de inscrições**, selecione seu domínio personalizado como o **domínio de encurtamento de links**.

![Configurações de grupos de inscrições que permitem selecionar um domínio de encurtamento de links.]({% image_buster /assets/img/custom_domain.png %})

As campanhas enviadas com o encurtamento de links ativado usarão o domínio atribuído associado ao seu grupo de inscrições de SMS, RCS ou WhatsApp.

![Pré-visualização do criador de mensagens SMS com um domínio de link encurtado que é diferente do domínio na caixa "Mensagem".]({% image_buster /assets/img/custom_domain2.png %})

## Perguntas frequentes

### Os domínios delegados podem ser compartilhados entre vários grupos de inscrições?

Sim. Um único domínio pode ser usado com vários grupos de inscrições. Para fazer isso, selecione o domínio para cada grupo de inscrições ao qual ele deve ser associado.

### Os domínios delegados podem ser compartilhados em vários espaços de trabalho?

Sim. Os domínios podem ser associados a grupos de inscrições em vários espaços de trabalho, desde que os espaços de trabalho estejam contidos na mesma empresa.

### Quantos domínios personalizados posso adicionar?

Você pode adicionar até 10 domínios personalizados por dashboard.

### O que acontecerá se eu não atualizar meus registros DNS dentro de 45 dias?

Embora os detalhes do registro DNS do Cloudflare expirem após 45 dias, é possível reiniciar o processo de configuração com o mesmo domínio e o Braze gerará um conjunto de novos registros DNS para estender a janela de configuração.

### Serei notificado se houver um erro durante o processo de atualização do DNS?

Sim. Se houver um erro, você receberá um banner no dashboard do Braze detalhando o problema e as etapas para resolvê-lo. 

### Posso usar um domínio personalizado em vários canais?

Sim. Depois que um domínio personalizado é verificado, ele pode ser usado em todos os grupos de inscrições de SMS, RCS e WhatsApp em todos os espaços de trabalho em um dashboard. 

### E se eu tiver dúvidas ou precisar de mais suporte?

Para obter orientações mais detalhadas sobre a configuração e o gerenciamento de domínios personalizados, incluindo etapas de solução de problemas e requisitos técnicos, [entre em contato com o Suporte]({{site.baseurl}}/braze_support/).
