---
nav_title: Domínios personalizados self-service
article_title: Domínios Personalizados Self-Service
page_order: 0
description: "Esta página cobre como usar domínios personalizados com encurtamento de links para personalizar a aparência e a sensação de suas URLs encurtadas."
page_type: reference
alias: "/custom_domains/"
tool:
  - Campaigns
channel:
  - SMS
---

# Domínios personalizados self-service

> Esta página cobre como configurar seus próprios domínios personalizados no painel do Braze. Domínios personalizados permitem que você use um link encurtado com marca que reflete a identidade da sua marca em vez de um link encurtado genérico ou o domínio do Braze (`brz.ai`)—melhorando a confiança do usuário e o engajamento da campanha com links SMS.

Domínios personalizados self-service permitem que você configure e gerencie seus próprios domínios personalizados para SMS, RCS e WhatsApp—diretamente do seu painel do Braze. Você pode facilmente adicionar, monitorar e gerenciar até 10 domínios personalizados em um só lugar.

## Benefícios dos domínios personalizados self-service

- **Configuração simplificada:** Configure seus domínios na página **Configurações da Empresa**, reduzindo o tempo de configuração.
- **Transparência aprimorada:** Receba atualizações em tempo real sobre o status de configuração do seu domínio através de banners no painel.
- **Notificações proativas:** Receba alertas imediatos quando seu domínio personalizado estiver conectado ou se ocorrerem erros de configuração.

## Requisitos do domínio

- Os domínios devem ser adquiridos, possuídos e gerenciados por você. Isso pode ser feito através de um registrador de domínios, como GoDaddy, Amazon Route 53 ou Google Domains.
- O domínio usado para este recurso deve ser:
  - Único (diferente do domínio do seu site)
  - Não pode ser usado para hospedar qualquer conteúdo da web
    - Você também pode usar subdomínios exclusivos. Por exemplo, o domínio `braze.com` pode ter subdomínios de `sms.braze.com` ou `whatsapp.braze.com`.

## Delegando seu domínio personalizado

Exigimos que você delegue seu domínio personalizado ao Braze para que possamos facilitar o roteamento adequado e a compatibilidade da infraestrutura com nossos serviços de encurtamento de links e rastreamento de cliques. Quando você delega seu domínio ao Braze, nós cuidamos automaticamente da renovação do certificado para evitar uma interrupção no serviço. 

## Adicionando um domínio personalizado

1. No Braze, vá para **Configurações da Empresa** > **Domínios de SMS/RCS e Aplicativos de Mensagens**.
\!["Página de Domínios de SMS/RCS e Aplicativos de Mensagens" com vários domínios listados.]({% image_buster /assets/img/main_page.png %})

{: start="2"}
2\. Selecione **Adicionar Domínio** para iniciar uma nova configuração de domínio personalizado.
3\. Insira o domínio personalizado que você comprou em nosso campo de entrada no aplicativo, que utiliza nossa lógica de validação existente para formatação adequada, em seguida, selecione **Próximo** e **Enviar**.

\!["Botão Adicionar Domínio" na página "Domínios de SMS/RCS e Aplicativos de Mensagens".]({% image_buster /assets/img/custom_domain_button.png %}){: style="max-width:70%;"}

{: start="4"}
4\. Peça à sua equipe técnica (como engenharia ou TI) para atualizar sua configuração de DNS com os detalhes do registro DNS do Cloudflare que são exibidos. Sua equipe técnica deve atualizar seus registros DNS com esses detalhes dentro de 45 dias.
  - Se você precisar de mais tempo para atualizar seus registros DNS, pode reiniciar o processo e gerar um novo conjunto de registros DNS para seu domínio.

O Braze irá verificar sua configuração de DNS aproximadamente a cada 30 minutos para verificar atualizações.

\!["Seção de registro DNS" com 3 etapas para completar a configuração do seu domínio.]({% image_buster /assets/img/dns_record.png %})

{% alert note %}
O progresso do seu domínio é salvo automaticamente. Se você precisar sair no meio do fluxo, pode retomar mais tarde selecionando a entrada de domínio pendente na página **Domínios de SMS/RCS e Aplicativos de Mensagens**.
{% endalert %}

### Gerenciamento e uso contínuos

Após a verificação do seu domínio, seus domínios personalizados aparecerão na tabela na página **Domínios de SMS/RCS e Aplicativos de Mensagens** com indicadores de status. Você pode usar imediatamente domínios conectados em vários grupos de assinatura, espaços de trabalho e nos canais SMS, RCS e WhatsApp.

\![Lista de domínios personalizados e status.]({% image_buster /assets/img/custom_domain_statuses.png %}){: style="max-width:60%;"}

A monitorização ao vivo irá alertá-lo no painel do Braze se algum dos seus domínios ativos tiver um problema, para que seus links personalizados permaneçam utilizáveis. Se você encontrar algum problema, consulte os detalhes de erro no aplicativo ou entre em contato com o Braze [Suporte]({{site.baseurl}}/braze_support/) para assistência.

## Usando domínios personalizados

Depois de configurados, os domínios personalizados podem ser atribuídos a um ou vários grupos de assinatura de SMS, RCS e WhatsApp.

\![Configurações de grupos de assinatura que permitem selecionar um domínio de encurtamento de link.]({% image_buster /assets/img/custom_domain.png %})

Campanhas enviadas com o encurtamento de link ativado usarão o domínio atribuído associado ao seu grupo de assinatura de SMS, RCS ou WhatsApp.

\![Pré-visualização do compositor de mensagens SMS com um domínio de link encurtado que é diferente do domínio na caixa "Mensagem".]({% image_buster /assets/img/custom_domain2.png %})

## Perguntas frequentes

### Os domínios delegados podem ser compartilhados entre vários grupos de assinatura?

Sim. Um único domínio pode ser usado com vários grupos de assinatura. Para fazer isso, selecione o domínio para cada grupo de assinatura com o qual ele deve ser associado.

### Os domínios delegados podem ser compartilhados entre vários espaços de trabalho?

Sim. Os domínios podem ser associados a grupos de assinatura em vários espaços de trabalho, desde que os espaços de trabalho estejam contidos na mesma empresa.

### Quantos domínios personalizados posso adicionar?

Você pode adicionar até 10 domínios personalizados por painel.

### O que acontece se eu não atualizar meus registros DNS dentro de 45 dias?

Embora os detalhes do seu registro DNS do Cloudflare expirem após 45 dias, você pode reiniciar o processo de configuração com o mesmo domínio e a Braze gerará um novo conjunto de registros DNS para estender sua janela de configuração.

### Serei notificado se houver um erro durante o processo de atualização do DNS?

Sim. Se houver um erro, você receberá um banner no painel da Braze detalhando o problema junto com etapas para resolvê-lo. 

### Posso usar um domínio personalizado em vários canais?

Sim. Depois que um domínio personalizado for verificado, ele pode ser usado em todos os grupos de assinatura SMS, RCS e WhatsApp em todos os espaços de trabalho dentro de um painel. 

### E se eu tiver perguntas ou precisar de mais suporte?

Para orientações mais detalhadas sobre como configurar e gerenciar domínios personalizados, incluindo etapas de solução de problemas e requisitos técnicos, [entre em contato com o Suporte]({{site.baseurl}}/braze_support/).