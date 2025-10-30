---
nav_title: Cartões de conteúdo
article_title: Cartões de Conteúdo no Canvas
page_order: 1
page_type: reference
description: "Este artigo de referência descreve recursos e nuances específicas para o uso de Cartões de Conteúdo como um canal de mensagens dentro do Canvas."
tool: Canvas
channel: content cards

---

# Cartões de Conteúdo no Canvas

> Os Cartões de Conteúdo podem ser enviados aos seus clientes como parte de sua jornada no Canvas. Este artigo descreve recursos e nuances específicas para o uso de Cartões de Conteúdo como um canal de mensagens dentro do Canvas.

Assim como outros canais de mensagens do Canvas, os Cartões de Conteúdo serão enviados para o dispositivo de um usuário quando ele atender aos critérios de público e segmentação especificados para sua etapa. Após o envio do Cartão de Conteúdo, ele estará disponível no feed de cada usuário elegível na próxima vez que seu feed de cartões for atualizado.

\![Cartões de Conteúdo selecionados como o canal de mensagens para uma etapa de Mensagem.]({% image_buster /assets/img_archive/content-cards-in-canvas.png %})

Duas opções que mudarão como a etapa do Cartão de Conteúdo interagirá com o Canvas são sua [expiração](#content-card-expiration) e [remoção](#removal).

## Expiração do Cartão de Conteúdo {#content-card-expiration}

Ao compor um novo Cartão de Conteúdo, você pode escolher quando ele deve expirar do feed do usuário com base em seu horário de envio. A contagem regressiva para a expiração de um Cartão de Conteúdo começa quando o usuário chega à etapa de Mensagem no Canvas onde o cartão é enviado. O cartão estará ativo no feed do usuário a partir deste ponto até que expire. Um cartão pode existir no feed de um usuário por até 30 dias. 

\![Configurações de expiração para um Cartão de Conteúdo para uma etapa de Mensagem que será removido após três horas no feed de um usuário.]({% image_buster /assets/img_archive/content-cards-in-canvas-expiration.png %})

### Tipos de expiração

Você tem duas maneiras de definir quando um cartão deve desaparecer do feed de um usuário: uma data relativa ou uma data absoluta.

#### Datas relativas

Quando você escolhe uma data relativa, como "Remover cartões enviados após 5 dias no feed de um usuário", você pode definir uma data de expiração de até 30 dias.

#### Datas absolutas

Quando você escolhe uma data absoluta, como "Remover cartões enviados em 1º de dezembro de 2023 às 16h", há algumas nuances envolvidas.

Embora você possa especificar uma duração de expiração maior que 30 dias, o Cartão de Conteúdo existirá no feed de um usuário por no máximo 30 dias. Especificar uma duração maior que 30 dias permite que você considere quaisquer atrasos antes de acionar a etapa de Mensagem, mas não estende a vida máxima do cartão no feed do usuário.

Tenha cuidado ao definir uma data de expiração mais de 30 dias à frente do lançamento do Canvas. Se um usuário chegar à etapa de Mensagem mais de 30 dias antes da data de expiração especificada, o cartão não será enviado.

### Comportamento de expiração

O Cartão de Conteúdo permanece disponível no feed do usuário até atingir sua data de expiração, mesmo que o usuário avance para etapas subsequentes na jornada do Canvas. Se você não quiser que o Cartão de Conteúdo esteja ativo quando as próximas etapas do Canvas forem entregues, certifique-se de que a expiração seja mais curta do que o atraso nas etapas subsequentes.

Após a expiração de um Cartão de Conteúdo, ele será removido automaticamente do feed do usuário durante a próxima atualização, mesmo que eles ainda não o tenham visualizado.

## Remoção do Cartão de Conteúdo {#removal}

Os Cartões de Conteúdo podem ser removidos quando os usuários completam uma compra ou realizam um evento personalizado. Você pode selecionar um dos seguintes como o evento de remoção: **Executar Evento Personalizado** e **Fazer Compra**. Em seguida, selecione **Adicionar Evento**.

\!["Remover cartões quando os usuários completam uma compra ou realizam um evento personalizado." selecionado com o gatilho para remover cartões para usuários que fazem uma compra específica para "Pulseira".]({% image_buster /assets/img_archive/content-cards-in-canvas-removal-event.png %})

## Relatórios e análises

Após lançar uma etapa de Cartões de Conteúdo no Canvas, você pode começar a analisar várias métricas diferentes para esta etapa. Essas métricas incluem o número de mensagens enviadas, destinatários únicos, taxas de conversão, receita total e mais.

\![Análise para uma etapa de Mensagem com o desempenho da mensagem do Cartão de Conteúdo.]({% image_buster /assets/img_archive/content-cards-in-canvas-analytics.png %})

Para mais informações sobre as métricas disponíveis e suas definições, consulte nosso [Glossário de Métricas de Relatório]({{site.baseurl}}/user_guide/data/report_metrics/).

## Casos de uso

#### Ofertas promocionais

Adicione cartões ao feed de um usuário à medida que eles se qualificam para promoções e anúncios específicos. Por exemplo, se um usuário se tornar elegível para uma nova oferta após realizar uma ação ou fazer uma compra, usando o Canvas você pode enviar a eles um Cartão de Conteúdo, além de outros canais de mensagem, para que na próxima vez que eles abrirem o aplicativo, a oferta esteja disponível para eles.

#### Caixa de entrada de notificações push

Há momentos em que um usuário pode descartar uma notificação push ou excluir um e-mail, mas você quer lembrá-los ou promover a oferta caso eles mudem de ideia.

Usando o Canvas, você pode adicionar um componente que envia tanto um Cartão de Conteúdo quanto uma notificação push para dar aos usuários uma "caixa de entrada" persistente de cartões que se alinham com mensagens promocionais enviadas via push. 

#### Múltiplos feeds baseados em categorias

Você pode separar seus Cartões de Conteúdo em múltiplos feeds com base em categorias, como diferentes tópicos que os usuários podem navegar, ou feeds transacionais e de marketing. Para mais informações sobre como criar múltiplos feeds usando pares chave-valor, confira nosso guia para [Personalizando feeds de Cartões de Conteúdo]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds).


