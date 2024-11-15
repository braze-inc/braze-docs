---
nav_title: "Campanhas sem atividades e canvas"
permalink: "/idle_campaigns_canvases/"
hidden: true
---

# Campanhas sem atividades e canvas

> Este artigo de referência explica o status sem atividades para campanhas e telas e responde a perguntas frequentes.

{% alert note %}
Em 2024, canvas serão marcados **sem atividades** e parados, similar a campanhas. Quando os canvas estiverem sem atividades ou parados, eles seguirão a lógica deste documento.
{% endalert %}

Campanhas e canvas recebem um status sem atividades quando não enviam mensagens ou não inserem usuários há algum tempo. Essas campanhas e canvas serão automaticamente interrompidas nas datas de parada associadas. Você pode filtrar por campanhas sem atividades e canvas para ajudar a classificar e gerenciar sua lista de campanhas e canvas.

## Campanhas sem atividades

De forma contínua, as campanhas sem atividades que atendem aos seguintes critérios serão interrompidas:
 
- Um envio único agendado está sete dias após a data de envio
- Uma campanha programada ou baseada em ações com uma data de término está sete dias após a data de término
- Uma campanha sem data de término que não enviou mensagens em um ano

Para campanhas sem datas de término, se uma mensagem for enviada ou a campanha for atualizada, a contagem regressiva de um ano para parar a campanha será reiniciada. Quando as campanhas forem interrompidas, o Braze notificará os clientes em seu dashboard e por e-mail.

As campanhas serão interrompidas na data de término padrão ou um dia após o prazo final da última conversão ocorrida, o que for mais tarde. Os envios que são resultado de uma Variante Vencedora ou Personalizada são tratados como envios agendados e serão interrompidos sete dias após o envio da Variante Vencedora ou Personalizada. Todas as campanhas serão interrompidas às 4h UTC todos os dias para todos os usuários do Braze.

Os cartões de conteúdo não serão interrompidos até o prazo de expiração e também obedecerão aos critérios mencionados, bem como à regra do prazo de conversão.

Consulte esta tabela para saber como manter uma campanha sem atividades ativa:

| Razão para o status de sem atividades                                                                              | Etapas para ativar a campanha                     |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------|
| Campanhas que são envios agendados uma vez, e já se passaram sete dias da data de envio                 | Agendar um envio futuro                            |
| Campanhas que são agendadas ou baseadas em ações, têm datas de término, e já se passaram sete dias após a data de término | Estender a data final                               |
| Campanhas sem data de ponta a ponta que não enviaram mensagens em um ano                                | Envie uma mensagem ou faça qualquer edição na campanha |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Canvas sem atividades

De forma contínua, canvas sem atividades que atendam aos seguintes critérios serão interrompidos:

- Um envio único agendado está atrasado em relação à sua data de envio e duração máxima em mais de 7 dias
- Uma canva programada ou baseada em ações com uma data de término está além de sua data de término e duração máxima por mais de 7 dias
- Uma canva sem data de término não foi acessada por usuários ou editada em mais de 12 meses e sua duração máxima

Para canvas sem datas de término, se um usuário for inserido ou a canva for atualizada, a contagem regressiva de um ano para parar a canva será reiniciada. Quando os canvas são interrompidos, a Braze notificará os clientes em seu dashboard e por e-mail.

A [duração máxima]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) de uma canva é o maior tempo possível que um usuário pode levar para concluir uma determinada canva. Essa duração inclui as expirações dos cartões de conteúdo e das mensagens no app.

Consulte esta tabela para saber como manter um canva sem atividades ativo:

| Razão para o status de sem atividades                                                                                                  | Passos para ativar a canva                     |
|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| Canvas que são envios agendados únicos, e são sete dias e duração máxima após a data de envio                 | Agendar um envio futuro                          |
| Canvas que são programados ou baseados em ações, têm datas de término, e são sete dias e duração máxima após a data de término | Estender a data final                             |
| canvas sem datas de término que não enviaram mensagens em um ano                                                      | Envie uma mensagem ou faça qualquer edição na canva |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Perguntas frequentes

#### A quais campanhas ou canvas isso se aplica?

Isso se aplicará a campanhas e canvas que já atendem aos critérios listados anteriormente, e campanhas e canvas que atenderão aos critérios daqui para frente.

#### Como sei se uma campanha ou canva está sem atividades?

Campanhas e Canvas sem atividades serão exibidos nas páginas de listagem de campanhas e Canvas na categoria **Ocioso**. A data em que a campanha ou canva será interrompida está listada como uma coluna na lista.

#### O que acontece se uma campanha sem atividades ou canva for atualizada?

Se uma campanha que não enviou uma mensagem ou um canva em que não entrou usuários for atualizada, a contagem regressiva será reiniciada.

#### O que acontece com campanhas que não enviaram uma mensagem em um ano (ou canvas que não inseriram usuários em um ano), mas têm uma data de término no futuro?

Interromperemos essas campanhas e telas sete dias após a data de término.

#### Quem receberá notificações por e-mail sobre campanhas interrompidas e canvas?

Por padrão, todos os usuários com permissões de administrador são inscritos para receber notificações por e-mail sobre campanhas de parada automática e canvas. O criador da campanha ou canva sempre será notificado quando for interrompido. Os usuários podem gerenciar as preferências de notificação por e-mail indo para **Configurações da Empresa** > **Preferências de Notificação**, depois adicionando ou removendo destinatários da notificação **Campanha Parada Automaticamente** e da notificação **Canva Parado Automaticamente**.

#### Como funciona a interrupção dos cartões de conteúdo?

Os Cartões de Conteúdo em campanhas não serão interrompidos até o prazo de expiração e o período de buffer apropriado. Eles serão interrompidos no final do período de buffer (correspondente a se a campanha é um envio único, tem uma data de término ou não tem uma data de término) e o prazo de expiração. 

Por exemplo, se um cartão de conteúdo expirar em 1º de abril, for um envio único e tiver um prazo de conversão de 10 dias, ele será interrompido em 12 de abril (10 dias após o prazo de conversão, mais um dia). Se um cartão de conteúdo expirar em 1º de abril, for acionado por API e não tiver enviado mensagens desde 15 de março, ele expirará em 15 de março do próximo ano.

canvas são interrompidos apenas depois que os Cartões de Conteúdo são interrompidos, o que significa que sua duração máxima foi atingida.

#### Tenho um experimento do tipo "feature flag" em meu Canvas. Depois que meu sinalizador de recurso for definido, o Canva permanecerá ativo?

As telas com etapas do Feature Flag não são interrompidas automaticamente e não ficam sem atividades.

#### Por que estou vendo campanhas sem atividades exibidas na minha lista de campanhas quando apliquei um filtro para mostrar apenas campanhas ativas?

As campanhas sem atividades são consideradas ativas até que sejam interrompidas.

#### Uma campanha seria listada como sem atividades quando ainda está enviando notificações por push?

Não. Uma campanha será listada como sem atividades quando não estiver mais enviando mensagens ativamente. 