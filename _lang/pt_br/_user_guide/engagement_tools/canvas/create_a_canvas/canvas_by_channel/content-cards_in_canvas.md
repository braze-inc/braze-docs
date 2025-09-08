---
nav_title: Cartões de conteúdo
article_title: Cartões de conteúdo no Canvas
page_order: 1
page_type: reference
description: "Este artigo de referência descreve os recursos e as nuances específicas do uso dos cartões de conteúdo como um canal de envio de mensagens no Canva."
tool: Canvas
channel: content cards

---

# Cartões de conteúdo no Canvas

> Os cartões de conteúdo podem ser enviados a seus clientes como parte de sua jornada no canva. Este artigo descreve os recursos e as nuances específicas do uso dos cartões de conteúdo como um canal de envio de mensagens no Canva.

Assim como em outros canais de envio de mensagens do Canva, os cartões de conteúdo serão enviados para o dispositivo do usuário quando ele atender ao público e aos critérios de direcionamento especificados para a etapa do canva. Depois que o cartão de conteúdo for enviado, ele estará disponível no feed de cada usuário elegível na próxima vez que o feed de cartões for atualizado.

![Cartões de conteúdo selecionados como o canal de envio de mensagens para uma etapa de Mensagem.]({% image_buster /assets/img_archive/content-cards-in-canvas.png %})

Duas opções que mudarão a forma como a etapa do cartão de conteúdo interagirá com o Canva são a [expiração](#content-card-expiration) e a [remoção](#removal).

## Expiração do cartão de conteúdo {#content-card-expiration}

Ao criar um novo cartão de conteúdo, você pode escolher quando ele deve expirar do feed do usuário com base no tempo de envio. A contagem regressiva para a expiração de um cartão de conteúdo começa quando o usuário chega à etapa de mensagens no Canva em que o cartão é enviado. O cartão estará ativo no feed do usuário a partir desse momento até expirar. Um cartão pode existir no feed de um usuário por até 30 dias. 

![Configurações de expiração de um cartão de conteúdo para uma etapa de mensagem que será removida após três horas no feed de um usuário.]({% image_buster /assets/img_archive/content-cards-in-canvas-expiration.png %})

### Tipos de expiração

Você tem duas maneiras de definir quando um cartão deve desaparecer do feed de um usuário: uma data relativa ou uma data absoluta.

#### Datas relativas

Ao escolher uma data relativa, como "Remover cartões enviados após 5 dias no feed de um usuário", é possível definir uma data de expiração de até 30 dias.

#### Datas absolutas

Quando você escolhe uma data absoluta, como "Remove sent cards on December 1, 2023 at 4 pm" (Remover cartões enviados em 1º de dezembro de 2023 às 16h), há algumas nuances envolvidas.

Embora seja possível especificar uma duração de expiração maior que 30 dias, o cartão de conteúdo existirá no feed de um usuário por no máximo 30 dias. Especificar uma duração superior a 30 dias permite levar em conta qualquer postergação antes de disparar a etapa Mensagem, mas não estende a vida útil máxima do cartão no feed do usuário.

Tenha cuidado ao definir uma data de expiração com mais antecedência do que 30 dias após o lançamento do Canva. Se um usuário chegar à etapa Mensagem mais de 30 dias antes da data de expiração especificada, o cartão não será enviado.

### Comportamento de expiração

O cartão de conteúdo permanece disponível no feed do usuário até atingir sua data de expiração, mesmo que o usuário avance para etapas subsequentes na jornada do Canva. Se você não quiser que o cartão de conteúdo esteja ativo quando as próximas etapas do canva forem entregues, certifique-se de que a expiração seja mais curta do que a postergação nas etapas subsequentes.

Após a expiração de um cartão de conteúdo, ele será automaticamente removido do feed do usuário durante a próxima atualização, mesmo que ele ainda não o tenha visualizado.

## Remoção do cartão de conteúdo {#removal}

Os cartões de conteúdo podem ser removidos quando os usuários concluem uma compra ou realizam um evento personalizado. Você pode selecionar uma das seguintes opções como o evento de remoção: **Execute o evento personalizado** e **faça a compra**. Em seguida, selecione **Add Event (Adicionar evento**).

!["Remove cards when users complete a purchase or perform a custom event." selecionado com o disparo para remover cartões para usuários que fazem uma compra específica para "Bracelet".]({% image_buster /assets/img_archive/content-cards-in-canvas-removal-event.png %})

## Relatórios e análise de dados

Depois de iniciar uma etapa dos cartões de conteúdo no Canva, você pode começar a analisar várias métricas diferentes para essa etapa. Essas métricas incluem o número de mensagens enviadas, destinatários únicos, taxas de conversão, receita total e muito mais.

![Análise de dados para uma etapa de mensagem com a performance de mensagem do cartão de conteúdo.]({% image_buster /assets/img_archive/content-cards-in-canvas-analytics.png %})

Para saber mais sobre as métricas disponíveis e suas definições, consulte nosso [Glossário de métricas do relatório]({{site.baseurl}}/user_guide/data/report_metrics/).

## Casos de uso

#### Ofertas promocionais

Adicione cartões ao feed de um usuário à medida que ele se qualifica para promoções e anúncios específicos. Por exemplo, se um usuário se tornar elegível para uma nova oferta depois de executar uma ação ou fazer uma compra, usando o Canva, você poderá enviar a ele um cartão de conteúdo, além de outros canais de envio de mensagens, para que, na próxima vez que ele abrir o app, a oferta esteja disponível para ele.

#### Caixa de entrada de notificações por push

Há ocasiões em que um usuário pode descartar uma notificação por push ou excluir um e-mail, mas você quer lembrá-lo ou promover a oferta caso ele mude de ideia.

Usando o Canva, é possível adicionar um componente que envia um Content Card e uma notificação por push para oferecer aos usuários uma "caixa de entrada" persistente de cartões que se alinham às mensagens promocionais enviadas via push. 

#### Vários feeds com base em categorias

É possível separar seus cartões de conteúdo em vários feeds com base em categorias, como diferentes tópicos que os usuários podem navegar, ou feeds transacionais e de marketing. Para saber mais sobre como criar vários feeds usando pares de valores-chave, consulte nosso guia para [personalizar os feeds do cartão de conteúdo]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds).


