---
nav_title: "RCS"
article_title: Sobre os Serviços de Comunicação Ricos (RCS)
alias: /about_rcs/
page_type: reference
page_order: 15
description: "Este artigo de referência cobre casos de uso gerais do canal RCS e os requisitos necessários para preparar seu canal RCS para uso."
---

# Sobre os Serviços de Comunicação Ricos (RCS)

> Os Serviços de Comunicação Ricos (RCS) aprimoram o SMS tradicional, permitindo que as marcas entreguem mensagens que são não apenas informativas, mas também muito mais envolventes. Agora suportado tanto no Android quanto no iOS, o RCS traz recursos como mídia de alta qualidade, botões interativos e perfis de remetente com marca diretamente nos aplicativos de mensagens pré-instalados dos usuários, eliminando a necessidade de baixar um aplicativo separado.

Diferente dos aplicativos de mensagens de terceiros, o RCS aproveita o ambiente de mensagens nativo (Apple Messages e Google Messages), permitindo que você alcance os usuários onde eles já passam a maior parte do tempo e vá além das experiências tradicionais de SMS e MMS, permitindo uma comunicação mais rica e interativa com os clientes. 

## Benefícios de usar o RCS

- **Experiências do cliente mais ricas:** Entregue experiências de usuário mais ricas integrando perfeitamente texto, visuais e elementos interativos—impulsionando o engajamento e abrindo caminho para campanhas personalizadas e orientadas por dados.
- **Interações confiáveis e com marca:** Alcance interações confiáveis e com marca através de um ID de remetente verificado que não apenas exibe os ativos da sua marca, mas também cumpre os principais padrões de privacidade do setor, aumentando a confiança e a fidelidade do cliente.
- **Entrega de mensagens flexível:** Facilite a entrega de mensagens flexível e confiável com um fallback de SMS sem costura que atinge todos os segmentos de público, independentemente das capacidades do dispositivo, enquanto preserva uma experiência de usuário consistente.
- **Insights práticos:** Desbloqueie insights práticos com relatórios avançados que rastreiam KPIs críticos, capacitando você a otimizar campanhas em tempo real e impulsionar o sucesso mensurável.
- **Sinergia omnicanal:** Integre perfeitamente o RCS dentro da sua estratégia de marketing abrangente para entregar experiências consistentes e intercanal para os clientes, amplificando a eficácia da campanha e o ROI geral.

## Casos de uso

| Caso de uso | Descrição |
| --- | --- |
| Promoções de produtos interativas | Dê vida às promoções de produtos combinando imagens envolventes ou vídeos curtos com documentos detalhados do produto. Aproveite as respostas sugeridas (como "Adicionar ao Carrinho" ou "Aprender") e ações openURL para impulsionar a exploração imediata do produto e a conversão—tudo dentro de uma experiência rica em mensagem. |
| Atualizações personalizadas de fidelidade e recompensas | Envie mensagens de fidelidade personalizadas enriquecidas com visuais de alta qualidade e detalhes de recompensas. Use respostas sugeridas (como "Resgatar Agora" ou "Ver Ofertas") e ações openURL para criar uma jornada interativa para o cliente, tornando cada atualização visualmente atraente e adaptada para inspirar engajamento imediato e aumentar a retenção. |
| Alertas de transação e conta seguros | Envie alertas de conta seguros e notificações de transação incluindo imagens de recibos ou documentos em PDF. Ações sugeridas (como "Reveja Agora" ou "Contate o Suporte") e links openURL ativam os clientes a acessarem rapidamente mais detalhes ou iniciar etapas de segurança, reforçando tanto a confiabilidade quanto a confiança em cada interação. |
| Melhorias na reserva do itinerário de viagem & | Melhore a experiência de viagem enviando itinerários visualmente ricos, guias de destino ou cartões de embarque. Com ações openURL, os clientes podem acessar rapidamente modificações de reserva ou atualizações em tempo real (como mudanças de horário) sem sair da janela de mensagens, facilitando uma jornada de viagem suave e envolvente do início ao fim. |
| Feedback do cliente e pesquisas interativas | Capture feedback acionável implantando pesquisas interativas que utilizam uma mistura de conteúdo de mídia rica e texto. Integre respostas sugeridas para respostas rápidas e ações openURL para acessar formulários de pesquisa mais abrangentes, facilitando para os clientes compartilharem suas opiniões, ajudando os profissionais de marketing a refinarem suas estratégias com base em feedback em tempo real de todos os setores. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Solicitações

| Requisito | Descrição |
| --- | --- |
| Créditos de mensagem | Entre em contato com seu gerente de conta Braze para confirmar que você comprou Créditos de Mensagem em seu contrato. Créditos de Mensagem é um item de contrato flexível que permite que você compre e aloque volume de mensagens em vários canais, como SMS, MMS, RCS e WhatsApp. |
| País elegível | Certifique-se de que você está enviando RCS para usuários em um dos países suportados pela Braze: Estados Unidos, Reino Unido, Alemanha, México, Suécia, Espanha, Cingapura, Brasil, França, Itália, Colômbia |
| Remetente verificado de RCS | O remetente que o destinatário vê em seu dispositivo para identificar de onde a mensagem está vindo. Um Remetente Verificado de RCS consiste em um nome de empresa, branding visual e um selo verificado. <br><br> Braze ajudará você a se inscrever e registrar um remetente verificado por RCS em regiões elegíveis. Você precisará fornecer ao seu representante da Braze algumas informações básicas. |
| Lista de usuários com números de telefone | Antes de começar a enviar mensagens, é necessário adicionar usuários à sua conta. Além disso, você precisa saber o tamanho aproximado de seu público. Usuários e números de telefone podem ser adicionados à Braze através de vários métodos diferentes. Os números de telefone devem ser formatados como um número de 10 dígitos, bem como um código de área do país. Para saber mais, consulte [Números de telefone dos usuários]({{site.baseurl}}/user_phone_numbers/). |
| Palavras-chave e respostas | Todas as palavras-chave básicas devem ter respostas atribuídas a elas antes que você possa começar a enviar mensagens. A Braze processará automaticamente palavras-chave de aceitação, recusa e ajuda. Opções de personalização e configurações adicionais de palavras-chave e respostas estão disponíveis. Para saber mais, consulte [Palavras-chave de aceitação e recusa]({{site.baseurl}}/optin_optout/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Termos importantes

| Prazo | Definição |
|----|----|
| Grupo de inscrições | Um grupo de usuários que estão inscritos em um caso de uso específico de envio de mensagens. Cada grupo de inscrições está vinculado a um ou mais "remetentes" de marca, que podem ser remetentes verificados por RCS, códigos SMS ou ambos. Por exemplo, se você planeja enviar mensagens RCS transacionais e promocionais, pode optar por configurar dois grupos de inscrições com remetentes verificados por RCS separados no seu dashboard da Braze. |
| Remetente verificado por RCS | A entidade que envia uma mensagem RCS, ou o que o destinatário da mensagem RCS vê em seu dispositivo para identificar de onde a mensagem está vindo. Remetentes verificados por RCS contêm um nome de empresa, legenda, branding visual e um selo verificado. Depois de fornecer as informações necessárias para o registro do remetente RCS à Braze, cuidamos do registro e da configuração do grupo de inscrições. |
| Fallback de SMS | Se uma mensagem não puder ser entregue com RCS (por exemplo, falta de suporte da operadora na região), a Braze ainda tentará entregar a mensagem via SMS quando um código SMS existir dentro do grupo de inscrições. |
| RCS básico | Mensagens apenas de texto de até 160 caracteres. Cobrado como uma única mensagem. <br><br> Esta categoria é usada apenas no modelo global. |
| RCS único | Mensagens apenas de texto que têm mais de 160 caracteres **ou** incluem quaisquer elementos ricos, como botões ou mídia. <br><br>Esta categoria é usada apenas no modelo global. |
| Rico | Mensagens apenas de texto, com ou sem sugestões limitadas ou botões. Cobrado por segmento (160 bytes UTF-8). Por exemplo, uma mensagem com 161 caracteres de texto simples é dois segmentos. <br><br> Esta categoria é usada apenas no modelo dos Estados Unidos. |
| Mídia Rica | Mensagens que incluem um arquivo de mídia (imagem, vídeo) ou um Cartão Rico. Cobrado como uma única mensagem, independentemente do comprimento da mensagem. <br><br> Esta categoria é usada apenas no modelo dos Estados Unidos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
