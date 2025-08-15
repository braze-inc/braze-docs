---
nav_title: "Sobre a RCS"
article_title: Sobre os serviços de comunicação avançada (RCS)
alias: /about_rcs/
page_type: reference
page_order: 0
description: "Este artigo de referência aborda os casos de uso geral do canal RCS e os requisitos necessários para deixar seu canal RCS pronto para uso."
---

# Sobre os serviços de comunicação avançada (RCS)

> Os Rich Communication Services (RCS) aprimoram o SMS tradicional, capacitando as marcas a enviar mensagens que não são apenas informativas, mas também muito mais envolventes. Agora compatível com Android e iOS, o RCS traz recursos como mídia de alta qualidade, botões interativos e perfis de remetente de marca diretamente para os aplicativos de mensagens pré-instalados dos usuários, eliminando a necessidade de baixar um app separado.

Ao contrário dos aplicativos de mensagens de terceiros, o RCS aproveita o ambiente nativo de envio de mensagens (Apple Messages e Google Messages), permitindo que você alcance os usuários onde eles já passam a maior parte do tempo e vá além das experiências tradicionais de SMS e MMS, ativando uma comunicação mais rica e interativa com os clientes. 

## Benefícios do uso do RCS

- **Experiências mais ricas para os clientes:** Proporcione experiências de usuário mais ricas, integrando perfeitamente texto, recursos visuais e elementos interativos, aumentando o engajamento e abrindo caminho para campanhas personalizadas e orientadas por dados.
- **Interações confiáveis e com a marca:** Obtenha interações confiáveis com a marca por meio de um ID de remetente verificado que não apenas mostra os ativos da sua marca, mas também está em conformidade com os principais padrões de privacidade do setor, aumentando a confiança e a fidelidade do cliente.
- **Envio flexível de mensagens:** Facilite o envio de mensagens flexíveis e confiáveis com um fallback de SMS contínuo que atinja todos os segmentos de público, independentemente dos recursos do dispositivo, preservando uma experiência de usuário consistente.
- **Insights práticos:** Desbloqueie insights práticos com relatórios avançados que rastreiam KPIs críticos, capacitando-o a otimizar campanhas em tempo real e a obter sucesso mensurável.
- **Sinergia omnicanal:** Integre perfeitamente o RCS em sua estratégia de marketing abrangente para oferecer experiências consistentes e em todos os canais aos clientes, ampliando a eficácia da campanha e o ROI geral.

## Casos de uso

| Caso de uso | Descrição |
| --- | --- |
| Promoções interativas de produtos | Dê vida às promoções de produtos combinando imagens de engajamento ou vídeos curtos com documentos detalhados do produto. Aproveite as respostas sugeridas (como "Adicionar ao carrinho" ou "Aprender") e as ações de openURL para impulsionar a exploração imediata do produto e a conversão - tudo em uma experiência rica e dentro da mensagem. |
| Atualizações personalizadas de fidelidade e recompensas | Envie mensagens de fidelidade personalizadas, enriquecidas com recursos visuais de alta qualidade e detalhes de recompensas. Use respostas sugeridas (como "Resgatar agora" ou "Exibir ofertas") e ações openURL para criar uma jornada interativa para o cliente, tornando cada atualização visualmente atraente e personalizada para inspirar engajamento imediato e maior retenção. |
| Alertas seguros sobre transações e contas | Forneça alertas de conta e notificações de transação seguros, incluindo imagens de recibos ou documentos em PDF. Ações sugeridas (como "Review Now" ou "Contact Support") e links openURL ativam os clientes para acessar rapidamente mais detalhes ou iniciar etapas de segurança, reforçando a confiabilidade e a confiança em cada interação. |
| Aprimoramentos no itinerário e na reserva de viagens | Aprimore a experiência de viagem enviando itinerários, guias de destinos ou cartões de embarque visualmente ricos. Com as ações openURL, os clientes podem acessar rapidamente as modificações de reserva ou atualizações em tempo real (como alterações de horário) sem sair da janela de envio de mensagens, facilitando uma jornada de viagem tranquila e engajada do início ao fim. |
| Feedback do cliente e pesquisas interativas | Capture feedback acionável implantando pesquisas interativas que usem uma combinação de conteúdo de mídia avançada e texto. Integre respostas sugeridas para respostas rápidas e ações openURL para acessar formulários de pesquisa mais abrangentes, simplificando o compartilhamento de opiniões dos clientes e ajudando os profissionais de marketing a refinar suas estratégias com base no feedback em tempo real de todas as verticais. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Solicitações

| Requisito | Descrição |
| --- | --- |
| Créditos de mensagens | Entre em contato com seu gerente de conta Braze para confirmar a compra de créditos de mensagens em seu contrato. Créditos de mensagens é um item de contrato flexível que permite comprar e alocar o volume de envio de mensagens em vários canais, como SMS, MMS, RCS e WhatsApp. |
| País elegível | Certifique-se de que está enviando RCS para usuários em um dos países suportados pela Braze: Estados Unidos, Reino Unido, Alemanha, México, Suécia, Espanha, Cingapura, Brasil, França, Itália, Colômbia |
| Remetente verificado RCS | O remetente que o destinatário vê em seu dispositivo para identificar de onde a mensagem está vindo. Um RCS-Verified Sender consiste em um nome de empresa, uma marca visual e um selo de verificação. <br><br> O Braze o ajudará a se candidatar e a se registrar como um remetente verificado pelo RCS nas regiões elegíveis. Você precisará fornecer ao seu representante Braze algumas informações básicas. |
| Lista de usuários com números de telefone | Antes de começar a enviar mensagens, é necessário adicionar usuários à sua conta. Além disso, você precisa saber o tamanho aproximado de seu público. Usuários e números de telefone podem ser adicionados ao Braze por meio de vários métodos diferentes. Os números de telefone devem ser formatados como um número de 10 dígitos, bem como um código de área do país. Para saber mais, consulte [Números de telefone do usuário]({{site.baseurl}}/user_phone_numbers/). |
| Palavras-chave e respostas | Todas as palavras-chave básicas devem ter respostas atribuídas a elas antes que você possa iniciar o envio de mensagens. O Braze processará automaticamente as palavras-chave de aceitação, exclusão e ajuda. Opções de personalização e configurações adicionais de resposta a palavras-chave estão disponíveis. Para saber mais, consulte [Palavras-chave de aceitação e exclusão]({{site.baseurl}}/optin_optout/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Termos importantes

| Prazo | Definição |
|----|----|
| Grupo de inscrições | Um grupo de usuários que estão inscritos em um caso de uso específico de envio de mensagens. Cada grupo de inscrições está vinculado a um ou mais "remetentes" da marca, que podem ser remetentes verificados pelo RCS, códigos SMS ou ambos. Por exemplo, se você planeja enviar mensagens RCS transacionais e promocionais, poderá optar por configurar dois grupos de inscrições com remetentes verificados RCS separados em seu dashboard do Braze. |
| Remetente verificado por RCS | A entidade de envio de uma mensagem RCS ou o que o destinatário da mensagem RCS vê em seu dispositivo para identificar de onde a mensagem está vindo. Os remetentes verificados pelo RCS contêm o nome da empresa, a legenda, a marca visual e um selo de verificação. Depois que você fornecer as informações necessárias de registro de remetente RCS ao Braze, nós cuidaremos do registro e da configuração do grupo de inscrições. |
| SMS fallback | Se uma mensagem não puder ser entregue com RCS (por exemplo, falta de suporte da operadora na região), o Braze ainda tentará entregar a mensagem por SMS quando houver um código SMS no grupo de inscrições. |
| RCS somente de texto | Essa categoria inclui mensagens RCS simples que são limitadas a texto, semelhantes ao SMS tradicional. Essas mensagens podem ter até 160 caracteres e fornecem um nível básico de comunicação sem nenhum elemento de mídia avançada.<br><br> Você pode enviar mensagens de texto com até 3.072 caracteres. No entanto, quando excederem 160 caracteres, serão cobrados da mesma forma que uma mensagem RCS rica (uma mensagem RCS única). |
| Envio de mensagens RCS ricas | As mensagens RCS avançadas aproveitam os recursos mais envolventes e avançados que o RCS oferece, como mídia, botões e muito mais. |
| "Básico" e "único" | As mensagens RCS são cobradas principalmente de duas maneiras: como mensagens básicas e únicas. "Básico" corresponde ao RCS somente de texto, enquanto "Único" corresponde ao RCS avançado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
