---
nav_title: aquecimento de IP
article_title: aquecimento de IP
page_order: 1
page_type: reference
description: "Este artigo de referência cobre o tópico de aquecimento de IP e melhores práticas."
channel: email
local_redirect:
  automated-ip-warming: '/docs/user_guide/message_building_by_channel/email/email_setup/ip_warming/automated_ip_warming/'
---

# aquecimento de IP

> O aquecimento de IP é a prática de acostumar os provedores de caixa de entrada de e-mail a receberem envio de mensagens dos seus endereços de IP dedicados. É uma parte extremamente importante do envio de e-mails com qualquer prestador de serviço de e-mail (ESP) e prática padrão na Braze para confirmar que suas mensagens alcancem as caixas de entrada de destino a uma taxa consistentemente alta.

O aquecimento de IP é projetado para ajudar você a estabelecer uma reputação positiva com os provedores de serviços de internet (ISPs). Toda vez que um novo endereço IP é usado para enviar um e-mail, os ISPs monitoram programaticamente esses e-mails para verificar se não estão sendo usados para enviar spam aos usuários. Pense na reputação do seu IP e domínio como uma pontuação de crédito — os ISPs usam essa reputação para determinar se seu e-mail chega à caixa de entrada ou à pasta de spam. Assim como uma pontuação de crédito, leva tempo para construir uma reputação positiva e ainda mais tempo para reconstruir uma reputação ruim.

## E se eu não tiver tempo para aquecer os IPs?

**O aquecimento de IP é obrigatório.** Se você não aquecer os IPs adequadamente e o padrão do seu e-mail causar qualquer suspeita, a velocidade de entrega do seu e-mail pode ser significativamente reduzida ou desacelerada. Seu domínio ou IP também pode ser bloqueado pelos ISPs, o que pode resultar em seus e-mails indo diretamente para a pasta de spam da caixa de entrada do seu usuário. Por isso, é importante aquecer seus IPs adequadamente.

Os ISPs limitam a entrega de e-mails quando há suspeita de spam para proteger seus usuários. Por exemplo, se você enviar para 100.000 usuários, o provedor de acesso à internet pode entregar o e-mail apenas para 5.000 desses usuários na primeira hora. Em seguida, o provedor de acesso à internet monitora medidas de engajamento, como taxas de abertura, taxas de cliques, cancelamentos de inscrição e relatórios de spam. Então, se um número significativo de relatórios de spam ocorrer, eles podem optar por relegar o restante desse envio para a pasta de spam em vez de entregá-lo na caixa de entrada do usuário. 

Se o engajamento for moderado, eles podem continuar a limitar seu e-mail para coletar mais dados de engajamento e determinar com mais certeza se o e-mail é spam ou não. Se o e-mail tiver métricas de engajamento muito altas, eles podem parar de limitar esse e-mail completamente. Eles usam esses dados para criar uma reputação de e-mail que eventualmente determinará se seus e-mails serão filtrados automaticamente como spam.

Se o seu domínio ou IP for bloqueado por um provedor de acesso à internet, os registros de mensagens no [Registro de Atividade de Mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) conterão informações sobre quais sites visitar para apelar a esses provedores de acesso à internet e sair dessas listas.

## Cronogramas de aquecimento de IP

Recomendamos fortemente aderir estritamente a um cronograma de aquecimento de IP para melhorar a entregabilidade. Também é importante que você não pule dias, pois a escalabilidade consistente melhora as métricas de entrega. Escolha um cronograma com base no seu histórico de envio de e-mails existente e nas métricas de entregabilidade.

{% alert tip %}
Se você tiver interesse em contar com um recurso dedicado de entregabilidade como parte da sua equipe de conta, fale com o gerente de conta da Braze para mais informações.
{% endalert %}

{% tabs local %}
{% tab Conservador %}

O cronograma conservador é uma abordagem mais lenta e cautelosa que ajuda a estabelecer uma reputação de envio sólida do zero. Isso é recomendado se você é novo no envio de e-mails, está migrando de um IP compartilhado ou enfrentou problemas de entregabilidade, como limitação ou bloqueio por um provedor de caixa de entrada.

Dia | Número de e-mails a enviar
----|---------------------
1 | 50
2 | 50
3 | 50
4 | 100
5 | 100
6 | 100
7 | 500
8 | 500
9 | 500
10 | 1.000
11 | 1.000
12 | 1.000
13 | 2.000
14 | 2.000
15 | 2.000
16 | 4.000
17 | 4.000
18 | 4.000
19 | 8.000
20 | 8.000
21 | 8.000
22+ | Dobrar a cada 3 dias até atingir o volume desejado

{% endtab %}
{% tab Moderado %}

O cronograma moderado é uma abordagem equilibrada que aumenta o volume de envio em um ritmo constante. Isso é recomendado para a maioria dos remetentes, incluindo aqueles com algum histórico de envio de e-mails que estão fazendo a transição para um novo IP.

Dia | Número de e-mails a enviar
----|---------------------
1 | 50
2 | 100
3 | 500
4 | 1.000
5 | 2.000
6 | 4.000
7 | 8.000
8 | 16.000
9 | 25.000
10 | 35.000
11 | 50.000
12 | 75.000
13 | 100.000
14 | 150.000
15 | 200.000
16 | 275.000
17 | 375.000
18 | 500.000
19 | 650.000
20 | 825.000
21 | 1.000.000
22+ | Dobrar a cada 2 dias até atingir o volume desejado

{% endtab %}
{% tab Agressivo %}

{% alert important %}
O cronograma agressivo é a abordagem mais rápida e é recomendado apenas para remetentes com um histórico de envio estabelecido e positivo e métricas de entregabilidade alinhadas com as melhores práticas, incluindo altas taxas de abertura, altas taxas de cliques e baixas taxas de bounce. Usar este cronograma sem um histórico comprovado pode prejudicar a reputação do remetente.
{% endalert %}

Dia | Número de e-mails a enviar
----|---------------------
1 | 50
2 | 100
3 | 500
4 | 1.000
5 | 2.500
6 | 5.000
7 | 9.000
8 | 16.000
9 | 29.000
10 | 52.000
11 | 98.000
12 | 160.000
13 | 225.000
14 | 315.000
15 | 450.000
16 | 615.000
17 | 875.000
18 | 1.200.000
19 | 1.750.000
20 | 2.750.000
21+ | Dobrar diariamente até atingir o volume desejado

{% endtab %}
{% endtabs %}

Na maioria dos casos, aqueça até o seu volume médio de envio diário em vez do volume de pico. Os ISPs analisam principalmente as últimas semanas de comportamento de envio para avaliar sua reputação, então se você atinge o volume de pico apenas a cada poucos meses (por exemplo, 7 milhões durante um período sazonal), você pode aumentar gradualmente em direção a esse pico mais perto da data de envio. No entanto, se você atinge o volume de pico a cada uma ou duas semanas, aqueça até esse pico desde o início.

Após o aquecimento de IP ser concluído e você ter alcançado seu volume diário desejado, o ideal é manter esse volume diariamente. Alguma flutuação é esperada, mas alcançar o volume desejado e depois fazer um envio em massa apenas uma vez por semana pode afetar negativamente suas métricas de entrega e a reputação do remetente. 

{% alert important %}
A maioria dos provedores armazena dados de reputação por apenas 30 dias. Se você passar um mês sem enviar nenhuma mensagem, terá que repetir o processo de aquecimento de IP.
{% endalert %}

## Como limitar envios durante o aquecimento

Nosso recurso integrado de limitação de usuários serve como uma ferramenta útil para ajudar você a aquecer seu endereço IP. Depois de escolher os segmentos de envio de mensagens desejados durante a criação da campanha, na etapa [Usuários Alvo]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas), selecione o menu suspenso **Opções Avançadas** para limitar seus usuários. À medida que sua programação de aquecimento continua, você pode aumentar gradualmente esse limite para aumentar o volume de e-mails enviados.

![]({% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %})

## Segmentação de subdomínio

Muitos ISPs e provedores de acesso a e-mail não filtram mais pela reputação do endereço IP. Essas tecnologias de filtragem agora também levam em conta a reputação baseada em domínio. Isso significa que os filtros analisarão todos os dados associados ao domínio do remetente e não apenas isolarão o endereço IP. Por esse motivo, além de aquecer seu IP de e-mail, também recomendamos ter domínios ou subdomínios separados para e-mails de marketing, transacionais e corporativos. 

{% alert important %}
A segmentação de subdomínios é especialmente importante para remetentes de grande volume. Esses remetentes devem trabalhar com um representante da Braze ao configurar sua conta para confirmar que aderem a esta prática.
{% endalert %}

Recomendamos segmentar seus domínios para que o e-mail corporativo seja enviado pelo seu domínio de nível superior, e o e-mail de marketing e transacional seja enviado por diferentes domínios ou subdomínios.

## Melhores práticas

Você pode evitar todas as consequências de não aquecer o IP seguindo estas melhores práticas:

### Comece com pequenos volumes de envio de e-mail

Aumente a quantidade que você envia a cada dia da forma mais gradual possível. Campanhas de e-mail abruptas e de alto volume são vistas com o maior ceticismo pelos ISPs. Portanto, você deve começar enviando pequenas quantidades de e-mail e aumentar gradualmente até o volume que pretende enviar. Tenha em mente que você está aquecendo seu IP em cada ISP individualmente — os ISPs não compartilham dados de reputação entre si. Ao planejar seus volumes de aquecimento, certifique-se de que não está aumentando o volume muito rapidamente em nenhum ISP específico. Independentemente do volume, sugerimos aquecer seu IP por segurança. Veja [cronogramas de aquecimento de IP](#ip-warming-schedules).

### Tenha um conteúdo introdutório envolvente

Confirme que seu primeiro conteúdo é altamente envolvente e maximiza a probabilidade de que os usuários cliquem, abram e interajam com seu e-mail. Sempre prefira e-mails bem direcionados a disparos indiscriminados ao aquecer IPs.

### Defina uma cadência de envio consistente

Depois que o aquecimento de IP estiver completo, crie uma cadência de envio, certificando-se de também distribuir seus e-mails ao longo de um dia ou vários dias. Ao criar um cronograma o mais consistente possível, você pode evitar um resfriamento de IP, que pode ocorrer se o volume de envio parar ou diminuir significativamente por mais de alguns dias. 

Consulte nosso [cronograma de aquecimento de IP](#ip-warming-schedules) para distribuir seu envio em um período de tempo mais longo, em vez de enviar um disparo em massa em um único momento específico.

### Limpe suas listas de e-mail

Confirme que sua lista de e-mails está limpa e não possui e-mails antigos ou não verificados. Garantir que você esteja em conformidade com [CASL e CAN-SPAM]({{site.baseurl}}/user_guide/administrative/privacy/spam_regulations/) é o ideal.

### Monitore a reputação do remetente

Ao conduzir o processo de aquecimento de IP, monitore cuidadosamente a reputação do remetente. Essas métricas específicas são importantes de observar:
- **Taxas de bounce:** Se qualquer campanha tiver uma taxa de bounce superior a 3-5%, você deve avaliar a limpeza da sua lista seguindo as diretrizes em nosso artigo [Mantenha Limpo: A Importância da Higiene da Lista de E-mail](https://www.braze.com/blog/email-list-hygiene/). Além disso, você deve considerar implementar uma [política de descontinuação]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/) para parar de enviar e-mails para endereços de e-mail não engajados ou inativos.
- **Relatórios de spam:** Se qualquer campanha for relatada como spam a uma taxa superior a 0,08%, você deve reavaliar o conteúdo que está enviando, verificar se está direcionado a um público interessado e garantir que seus e-mails estejam adequadamente redigidos para despertar o interesse.
- **Taxas de abertura:** As taxas de abertura são um indicador útil para a colocação na caixa de entrada. Se suas taxas de abertura únicas estiverem acima de 25%, você provavelmente está tendo uma alta colocação na caixa de entrada, o que indica uma reputação positiva do remetente.

{% alert tip %}
A Braze recomenda não usar [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) para aquecer seus IPs. Como as campanhas de aquecimento de IP são algumas das primeiras campanhas que você envia, a Braze não terá informações suficientes sobre seus usuários para calcular um horário de envio ideal. Nesse caso, todas as mensagens com Intelligent Timing usariam o horário de fallback e seriam enviadas ao mesmo tempo de qualquer forma.
{% endalert %}

{% alert tip %}
É normal que os e-mails sejam enviados para a pasta de spam durante o aquecimento de IP, porque seu domínio e IP ainda não estabeleceram uma reputação positiva. Se o e-mail cair na sua pasta de spam, o administrador de e-mail pode precisar adicionar o domínio de envio da Braze e o IP à lista de permissões da sua empresa.
{% endalert %}