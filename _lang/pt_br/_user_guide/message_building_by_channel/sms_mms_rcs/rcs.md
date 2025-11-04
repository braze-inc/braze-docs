---
nav_title: "RCS"
article_title: Sobre os serviços de comunicação avançada (RCS)
alias: /about_rcs/
page_type: reference
page_order: 14
description: "Este artigo de referência aborda os casos de uso geral do canal RCS e os requisitos necessários para deixar seu canal RCS pronto para uso."
---

# Sobre os serviços de comunicação avançada (RCS)

> Os Rich Communication Services (RCS) aprimoram o SMS tradicional, permitindo que as marcas enviem mensagens não apenas informativas, mas também muito mais envolventes. Agora com suporte para Android e iOS, o RCS traz recursos como mídia de alta qualidade, botões interativos e perfis de remetente com marca diretamente para os aplicativos de mensagens pré-instalados dos usuários, eliminando a necessidade de baixar um aplicativo separado.

Ao contrário dos aplicativos de mensagens de terceiros, o RCS aproveita o ambiente nativo de mensagens (Apple Messages e Google Messages), permitindo que você alcance os usuários onde eles já passam a maior parte do tempo e vá além das experiências tradicionais de SMS e MMS, permitindo uma comunicação mais rica e interativa com os clientes. 

## Benefícios do uso do RCS

- **Experiências mais ricas para os clientes:** Proporcione experiências de usuário mais ricas, integrando perfeitamente texto, recursos visuais e elementos interativos, aumentando o envolvimento e abrindo caminho para campanhas personalizadas e orientadas por dados.
- **Interações confiáveis e com a marca:** Obtenha interações confiáveis com a marca por meio de um ID de remetente verificado que não apenas exibe os ativos da sua marca, mas também está em conformidade com os principais padrões de privacidade do setor, aumentando a confiança e a fidelidade do cliente.
- **Entrega flexível de mensagens:** Facilite a entrega de mensagens flexíveis e confiáveis com um fallback de SMS contínuo que alcance todos os segmentos do público, independentemente dos recursos do dispositivo, preservando uma experiência de usuário consistente.
- **Insights práticos:** Desbloqueie insights acionáveis com relatórios avançados que rastreiam KPIs essenciais, permitindo que você otimize campanhas em tempo real e obtenha sucesso mensurável.
- **Sinergia omnichannel:** Integre perfeitamente o RCS em sua estratégia de marketing abrangente para proporcionar experiências consistentes e multicanal aos clientes, ampliando a eficácia da campanha e o ROI geral.

## Casos de uso

| Caso de uso | Descrição |
| --- | --- |
| Promoções interativas de produtos | Dê vida às promoções de produtos combinando imagens envolventes ou vídeos curtos com documentos detalhados do produto. Aproveite as respostas sugeridas (como "Adicionar ao carrinho" ou "Aprender") e as ações de openURL para impulsionar a exploração imediata do produto e a conversão - tudo em uma experiência rica e dentro da mensagem. |
| Atualizações personalizadas de fidelidade e recompensas | Envie mensagens personalizadas de fidelidade enriquecidas com recursos visuais de alta qualidade e detalhes de prêmios. Use respostas sugeridas (como "Resgatar agora" ou "Exibir ofertas") e ações openURL para criar uma jornada interativa para o cliente, tornando cada atualização visualmente atraente e personalizada para inspirar o envolvimento imediato e aumentar a retenção. |
| Alertas seguros sobre transações e contas | Forneça alertas de conta e notificações de transação seguros, incluindo imagens de recibos ou documentos em PDF. Ações sugeridas (como "Review Now" ou "Contact Support") e links openURL permitem que os clientes acessem rapidamente mais detalhes ou iniciem etapas de segurança, reforçando a confiabilidade e a confiança em cada interação. |
| Itinerário de viagem & aprimoramentos na reserva | Aprimore a experiência de viagem enviando itinerários, guias de destino ou cartões de embarque visualmente ricos. Com as ações openURL, os clientes podem acessar rapidamente modificações na reserva ou atualizações em tempo real (como alterações de horários) sem sair da janela de mensagens, facilitando uma jornada de viagem tranquila e envolvente do início ao fim. |
| Feedback do cliente e pesquisas interativas | Capture feedback acionável implantando pesquisas interativas que usem uma combinação de conteúdo de mídia avançada e texto. Integre respostas sugeridas para respostas rápidas e ações openURL para acessar formulários de pesquisa mais abrangentes, simplificando o compartilhamento de opiniões dos clientes e ajudando os profissionais de marketing a refinar suas estratégias com base no feedback em tempo real de todas as verticais. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Requisitos

| Requisito | Descrição |
| --- | --- |
| Créditos de mensagens | Entre em contato com o gerente da sua conta Braze para confirmar a compra de créditos de mensagens no seu contrato. Créditos de mensagens é um item de contrato flexível que permite que você compre e aloque o volume de mensagens em vários canais, como SMS, MMS, RCS e WhatsApp. |
| País elegível | Certifique-se de que está enviando RCS para usuários em um dos países suportados pelo Braze: Estados Unidos, Reino Unido, Alemanha, México, Suécia, Espanha, Cingapura, Brasil, França, Itália, Colômbia |
| Remetente verificado RCS | O remetente que o destinatário vê em seu dispositivo para identificar de onde a mensagem está vindo. Um RCS-Verified Sender consiste em um nome de empresa, uma marca visual e um selo de verificação. <br><br> O Braze o ajudará a se candidatar e se registrar como um remetente verificado pelo RCS em regiões qualificadas. Você precisará fornecer ao seu representante Braze algumas informações básicas. |
| Lista de usuários com números de telefone | Antes de começar a enviar mensagens, é necessário adicionar usuários à sua conta. Além disso, você deve saber o tamanho aproximado do seu público. Usuários e números de telefone podem ser adicionados ao Braze por meio de vários métodos diferentes. Os números de telefone devem ser formatados como um número de 10 dígitos, bem como um código de área do país. Para saber mais, consulte [Números de telefone do usuário]({{site.baseurl}}/user_phone_numbers/). |
| Palavras-chave e respostas | Todas as palavras-chave básicas devem ter respostas atribuídas a elas antes que você possa começar a enviar mensagens. O Braze processará automaticamente as palavras-chave opt-in, opt-out e help. Opções de personalização e configurações adicionais de resposta a palavras-chave estão disponíveis. Para saber mais, consulte [Palavras-chave de opt-in e opt-out]({{site.baseurl}}/optin_optout/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Termos a serem conhecidos

| Prazo | Definição |
|----|----|
| Grupo de assinaturas | Um grupo de usuários que estão inscritos em um caso de uso específico de mensagens. Cada grupo de assinatura está vinculado a um ou mais "remetentes" da marca, que podem ser remetentes verificados pelo RCS, códigos SMS ou ambos. Por exemplo, se você planeja enviar mensagens RCS transacionais e promocionais, poderá optar por configurar dois grupos de assinatura com remetentes verificados RCS separados no painel do Braze. |
| Remetente verificado por RCS | A entidade de envio de uma mensagem RCS ou o que o destinatário da mensagem RCS vê em seu dispositivo para identificar de onde a mensagem está vindo. Os remetentes verificados pelo RCS contêm o nome da empresa, a legenda, a marca visual e um selo de verificação. Depois que você fornecer as informações necessárias de registro de remetente RCS à Braze, nós cuidaremos do registro e da configuração do grupo de assinatura. |
| SMS fallback | Se uma mensagem não puder ser entregue com RCS (por exemplo, falta de suporte da operadora na região), o Braze ainda tentará entregar a mensagem por SMS quando houver um código SMS no grupo de assinatura. |
| RCS básico | Mensagens somente de texto com até 160 caracteres. Cobrado como uma única mensagem. <br><br> Essa categoria é usada apenas no modelo global. |
| RCS único | Mensagens somente de texto com mais de 160 caracteres **ou** que incluam elementos ricos, como botões ou mídia. <br><br>Essa categoria é usada apenas no modelo global. |
| Rico | Mensagens somente de texto, com ou sem sugestões ou botões limitados. Cobrado por segmento (160 bytes UTF-8). Por exemplo, uma mensagem com 161 caracteres de texto simples tem dois segmentos. <br><br> Essa categoria é usada apenas no modelo dos Estados Unidos. |
| Mídia avançada | Mensagens que incluem um arquivo de mídia (imagem, vídeo) ou um Rich Card. Cobrado como uma única mensagem, independentemente do tamanho da mensagem. <br><br> Essa categoria é usada apenas no modelo dos Estados Unidos. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
