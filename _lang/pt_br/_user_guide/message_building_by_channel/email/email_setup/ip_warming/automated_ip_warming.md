---
nav_title: Aquecimento de IP automatizado
article_title: Aquecimento de IP automatizado
page_order: 1
page_type: reference
description: "Este artigo de referência cobre o aquecimento de IP automatizado e como monitorar seu aquecimento de IP."
channel: email
---

# Aquecimento de IP automatizado

> Use o aquecimento de IP automatizado para aumentar gradualmente o volume de e-mails de um novo endereço IP e construir a reputação do remetente com os provedores de caixa de entrada.

{% multi_lang_include early_access_beta_alert.md feature='Automated IP warming' %}

## Como funciona?

Você pode usar o aquecimento de IP automatizado para aumentar gradualmente seu volume diário de envios, permitindo que os provedores de caixa de entrada aprendam e confiem em seus padrões de envio. Quando você adiciona um domínio ao seu espaço de trabalho, pode selecionar o tile **Aquecimento de IP Automatizado** na seção **Continue de onde parou** do seu dashboard inicial, e este tile permanece aqui por 60 dias.

A Braze envia primeiro para seus assinantes mais engajados, o que permite que o volume diário cresça em um ritmo que corresponde às melhores práticas. Em seguida, a Braze rastreia sinais de engajamento e entregabilidade. Se a Braze detectar algum problema, o sistema ajusta automaticamente sua programação.

{% alert note %}
Você pode realizar apenas um aquecimento de IP.
{% endalert %}

## Pré-requisitos

Para realizar o aquecimento de IP automatizado, você deve ter o seguinte:

- Subdomínio verificado e endereços IP ativos
- Permissões para visualizar e iniciar um aquecimento de IP
    - "Ver Dados de Uso" para visualizar a seção de aquecimento de IP
    - "Ver Modelos de E-mail" para visualizar e selecionar os modelos de e-mail para aquecimento de IP
    - "Gerenciar Configurações de E-mail" para iniciar o aquecimento de IP
- "Acessar Campanhas" 
- "Aprovar e Negar Campanhas" se o fluxo de trabalho de aprovação para campanhas estiver ativado 
    - A Braze aprova automaticamente as campanhas criadas a partir do aquecimento de IP automatizado em seu nome.

## Configure um plano de aquecimento de IP automatizado

### Etapa 1: Defina um cronograma

1. Na seção **Informações de envio**, selecione o **Endereço de remetente** para aquecer os endereços IP.
2. Insira o volume diário atual de envios e o volume de envios alvo.
3. Selecione a data de início para o aquecimento automatizado de IP. Esta data deve ser pelo menos um dia após o lançamento do plano.
4. Insira o horário de envio. Isso envia as mensagens no fuso horário da empresa.
5. Selecione **Próximo: Segmentos** para continuar a configuração.

![Detalhes do cronograma de exemplo.]({% image_buster /assets/img/automated_ip_warming_schedule.png %})

### Etapa 2: Selecione e classifique os segmentos

1. Em seguida, selecione os segmentos a serem segmentados. Durante o aquecimento de IP, a Braze começa a enviar para seus usuários mais engajados e aumenta gradualmente o volume de envios ao longo do tempo, adicionando lentamente segmentos com menos engajamento. 
2. Em seguida, arraste e solte os segmentos para classificá-los do mais alto para o mais baixo engajamento. Alto engajamento inclui destinatários que abrem e clicam consistentemente em seus e-mails. Baixo engajamento inclui destinatários que são inconsistentes em seu engajamento com seus e-mails ou não se engajaram com seus e-mails há muito tempo.
3. Selecione **Próximo: Mensagens** para continuar a configuração.

![Dois segmentos selecionados para segmentar para o aquecimento automatizado de IP.]({% image_buster /assets/img/automated_ip_warming_segment.png %})

### Etapa 3: Selecione as mensagens a serem enviadas

1. Selecione **Selecionar modelos de e-mail**.
2. Escolha os modelos de e-mail para as mensagens a serem enviadas. O conteúdo que você envia durante o aquecimento de IP deve incentivar aberturas e cliques. Recomendamos escolher conteúdos que tiveram boa recepção no passado. Por exemplo, você pode usar ofertas promocionais para incentivar o engajamento imediato e compras.
3. Selecione **Selecionar modelos**. A Braze calcula o número de modelos necessários antes que você possa lançar. Recomendamos fornecer mais modelos do que o mínimo necessário para permitir que o sistema se ajuste a problemas de entregabilidade sem parar.
4. Após adicionar o número necessário de modelos, selecione **Próximo: Resumo**.

{% alert important %}
Mudanças feitas nas campanhas criadas a partir da ferramenta de aquecimento de IP (como mudar a data programada, segmento, volume) não serão refletidas na página de **Resumo** do aquecimento de IP.
{% endalert %}

### Etapa 4: Revisão e lançamento

Revise os detalhes do seu plano de aquecimento de IP. Em seguida, selecione **Lançar**.

## Durante o aquecimento de IP ativo

As campanhas de aquecimento de IP são criadas de 1 a 2 dias de antecedência, a menos que você esteja lançando um aquecimento de IP no dia seguinte. Essas campanhas são automaticamente nomeadas com o seguinte formato: `IP Warming Day [X] - [Date] - [Template Name]`.

Quando a meta diária de envio é atingida, o sistema para de enviar por aquele dia para proteger sua reputação. 

O sistema monitora sua integridade com base nos seguintes benchmarks da indústria: 

- Taxa de entrega cai para menos ou igual a 90%
- Taxa de abertura menor que 10%
- Taxas de rejeição maiores que 5%
- Taxas de reclamação de spam maiores que 0,1%

Se as estatísticas estiverem abaixo de nossos benchmarks, o sistema retém o volume no dia seguinte em vez de aumentar o volume para mitigar o risco à sua reputação de remetente.

## Pare um plano de aquecimento de IP

A Braze permite que você pare o aquecimento de IP e a criação de futuras campanhas, mas se uma campanha já estiver ativa ou agendada para as próximas 24 a 48 horas, você pode precisar parar a campanha específica manualmente. Parar um plano de aquecimento de IP também interrompe todas as campanhas associadas.

No entanto, quando parado, o aquecimento de IP não pode ser retomado. Em vez disso, você deve configurar um novo plano para retomar de onde parou, fazendo:

- Baixando os dados existentes do seu plano parado para manter em seu registro, pois uma vez que você inicie um novo aquecimento de IP, o rastreador anterior será removido
- Atualizando o **Volume diário atual de envio** para o volume mais recente
- Adicionando um filtro a um segmento se você planeja usar o mesmo segmento do último aquecimento de IP, excluindo usuários que já receberam campanhas anteriores

## Quando um aquecimento de IP é concluído

O aquecimento de IP é marcado como concluído quando o último dia de aquecimento de IP termina à meia-noite no fuso horário da sua empresa. Por exemplo, se a última campanha enviada no plano de aquecimento de IP for enviada às 20h, então o plano é marcado como concluído após quatro horas.

O rastreador permanece na página inicial por 90 dias após o término do plano. Após 90 dias, o rastreador é removido. Baixar os dados inclui essas métricas padrão de e-mail:

- _Envios_	
- _Entregue_	
- _Bounces_	
- _Relatórios de spam_	
- _Total de aberturas_	
- _Aberturas exclusivas_	
- _Clicado_	
- _Cancelou inscrição_

Se um dia incluir várias campanhas usadas para atender aos requisitos de volume, estas são agregadas na visualização diária.

![Rastreador de aquecimento de IP com volume de envio para a semana de 16 de janeiro.]({% image_buster /assets/img/automated_ip_warming_example.png %})