---
nav_title: aquecimento de IP
article_title: aquecimento de IP
page_order: 1
page_type: reference
description: "Este artigo de referência cobre o tópico de aquecimento de IP e melhores práticas."
channel: email

---

# aquecimento de IP

> O aquecimento de IP é a prática de acostumar os provedores de caixa de entrada de e-mail a receberem envio de mensagens dos seus endereços de IP dedicados. É uma parte extremamente importante do envio de e-mails com qualquer prestador de serviço de e-mail (ESP) e prática padrão na Braze confirmar que suas mensagens alcancem as caixas de entrada de destino a uma taxa consistentemente alta.

O aquecimento de IP é projetado para ajudar você a estabelecer uma reputação positiva com os provedores de serviços de internet (ISPs). Toda vez que um novo endereço IP é usado para enviar um e-mail, os ISPs monitoram programaticamente esses e-mails para verificar se não estão sendo usados para enviar spam aos usuários.

## E se eu não tiver tempo para aquecer os IPs?

**O aquecimento de IP é necessário.** Se você não aquecer os IPs adequadamente, e o padrão do seu e-mail causar qualquer suspeita, a velocidade de entrega do seu e-mail pode ser significativamente reduzida ou desacelerada. Seu domínio ou IP também pode ser bloqueado pelos ISPs, o que pode resultar em seus e-mails indo diretamente para a pasta de spam da caixa de entrada do seu usuário. Como tal, é importante aquecer seus IPs adequadamente.

Os ISPs limitam a entrega de e-mails quando há suspeita de spam para que possam proteger seus usuários. Por exemplo, se você enviar para 100.000 usuários, o provedor de acesso à internet pode entregar o e-mail apenas para 5.000 desses usuários na primeira hora. Em seguida, o provedor de acesso à internet monitora medidas de engajamento, como taxas de abertura, taxas de cliques, cancelamentos de inscrição e relatórios de spam. Então, se um número significativo de relatórios de spam ocorrer, eles podem optar por relegar o restante desse envio para a pasta de spam em vez de entregá-lo na caixa de entrada do usuário. 

Se o engajamento for moderado, eles podem continuar a limitar seu e-mail para coletar mais dados de engajamento e determinar se o e-mail é spam com mais certeza. Se o e-mail tiver métricas de engajamento muito altas, eles podem parar de limitar esse e-mail completamente. Eles usam esses dados para criar uma reputação de e-mail que eventualmente determinará se seus e-mails serão filtrados automaticamente como spam.

Se o seu domínio ou IP for bloqueado por um provedor de acesso à internet, os registros de mensagens no [Registro de Atividade de Mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) conterão informações sobre quais sites visitar para apelar a esses provedores de acesso à internet e sair dessas listas.

## Cronograma de aquecimento de IP

Recomendamos fortemente aderir estritamente a este cronograma de aquecimento de IP para melhorar a entregabilidade. Também é importante que você não pule dias, pois a regularidade na ampliação dos esforços melhora as métricas de entrega.

Dia | \# de e-mails a serem enviados
----|--------------------------|
1 | 50
2 | 100
3 | 500
4 | 1.000
5 | 5.000
6 | 10.000
7 | 20.000
8 | 40.000
9 | 70.000
10 | 100.000
11 | 150.000
12 | 250.000
13 | 400.000
14 | 600.000
15 | 1.000.000
16 | 2.000.000
17 | 4.000.000
18+ | Dobrar diariamente até atingir o volume desejado

Sugerimos aquecer até o seu pico de envio. Ou seja, se você normalmente envia 2 milhões de e-mails por dia, mas planeja enviar 7 milhões durante um período sazonal, esse envio de "pico" é o que você deve aquecer.

Uma vez que o aquecimento esteja completo e você tenha atingido o seu volume diário desejado, você deve tentar manter esse volume diariamente. Alguma flutuação é esperada, mas atingir o volume desejado e, em seguida, fazer um envio em massa apenas uma vez por semana pode afetar negativamente suas métricas de entrega e reputação do remetente. 

{% alert important %}
A maioria dos provedores armazena dados de reputação por apenas 30 dias. Se você passar um mês sem enviar nenhuma mensagem, terá que repetir o processo de aquecimento de IP.
{% endalert %}

## Como limitar envios durante o aquecimento

Nosso recurso integrado de limitação de usuários serve como uma ferramenta útil para ajudá-lo a aquecer seu endereço IP. Depois de escolher os seus segmentos de envio de mensagens desejados durante a criação da campanha, na [etapa de Usuários Alvo]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas), selecione o menu suspenso **Opções Avançadas** para limitar seus usuários. À medida que sua programação de aquecimento continua, você pode aumentar gradualmente esse limite para aumentar o volume de e-mails que você envia.

![]({% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %})

## Segmentação de subdomínio

Muitos ISPs e provedores de acesso a e-mail não filtram mais apenas pela reputação do endereço IP. Essas tecnologias de filtragem agora também levam em conta a reputação baseada em domínio. Isso significa que os filtros analisarão todos os dados associados ao domínio do remetente e não apenas isolarão o endereço IP. Por esse motivo, além de aquecer seu IP de e-mail, também recomendamos ter domínios ou subdomínios separados para e-mails de marketing, transacionais e corporativos. 

{% alert important %}
A segmentação de subdomínios é especialmente importante para remetentes de grande volume. Esses remetentes devem trabalhar com um representante da Braze ao configurar sua conta para confirmar que eles aderem a esta prática.
{% endalert %}

Recomendamos segmentar seus domínios para que o correio corporativo seja enviado através do seu domínio de nível superior, e o correio de marketing e transacional seja enviado através de diferentes domínios ou subdomínios.

## Melhores práticas

Todas as consequências de não aquecer o IP podem ser evitadas se você seguir estas melhores práticas de aquecimento de IP.

### Comece com pequenos volumes de envio de e-mail

Aumente a quantidade que você envia a cada dia de forma gradual. Campanhas de e-mail abruptas e de alto volume são vistas com o maior ceticismo pelos ISPs. Portanto, você deve começar enviando pequenas quantidades de e-mail e aumentar gradualmente o volume de e-mail que você pretende enviar. Independentemente do volume, sugerimos aquecer seu IP para estar seguro. Veja [cronograma de aquecimento de IP](#ip-warming-schedule).

### Tenha um conteúdo introdutório envolvente

Confirme que seu primeiro conteúdo é altamente envolvente e maximiza a probabilidade de que os usuários cliquem, abram e se envolvam com seu e-mail. Sempre prefira e-mails bem direcionados a disparos indiscriminados ao aquecer IPs.

### Defina uma cadência de envio consistente

Depois que o aquecimento de IP estiver completo, crie uma cadência de envio, certificando-se de também distribuir seus e-mails ao longo de um dia ou vários dias. Ao criar um cronograma o mais consistente possível, você pode evitar um resfriamento de IP, que pode ocorrer se o volume de envio parar ou diminuir significativamente por mais de alguns dias. 

Consulte nosso [cronograma de aquecimento de IP](#ip-warming-schedules) para distribuir seu envio em um período de tempo mais longo, em vez de enviar uma explosão em massa em um único momento específico.

### Limpe suas listas de e-mail

Confirme que sua lista de e-mails está limpa e não possui e-mails antigos ou não verificados. O ideal é garantir que você esteja [em conformidade com a CASL e com a CAN-SPAM]({{site.baseurl}}/user_guide/administrative/privacy/spam_regulations/).

### Monitore a reputação do remetente

Ao conduzir o processo de aquecimento de IP, monitore cuidadosamente sua reputação do remetente enquanto conduz o processo de aquecimento de IP. Essas métricas específicas são importantes de observar:
- **Taxas de bounce:** Se alguma campanha tiver mais de 3 a 5% de bounce, você deverá avaliar a limpeza de sua lista seguindo as diretrizes de nosso site [Keep It Clean: A Importância da Higiene da Lista de E-mail](https://www.braze.com/blog/email-list-hygiene/) artigo. Além disso, você deve considerar a implementação de uma [política de sunsetting]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/) para interromper o envio de e-mail para endereços de e-mail não engajados ou inativos.
- **Relatórios de Spam:** Se qualquer campanha for relatada como spam a uma taxa superior a 0,08%, você deve reavaliar o conteúdo que está enviando, verificar se está direcionado a um público interessado e garantir que seus e-mails estejam adequadamente redigidos para despertar seu interesse.
- **Taxas de Abertura:** As taxas de abertura são um proxy útil para a colocação na caixa de entrada. Se suas taxas de abertura únicas estiverem acima de 25%, você provavelmente está experimentando uma alta colocação na caixa de entrada, o que indica uma reputação positiva do remetente.

{% alert tip %}
Braze recomenda não usar [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) para aquecer seus IPs. Como as campanhas de aquecimento de IP são algumas das primeiras campanhas que você envia, a Braze não terá informações suficientes sobre seus usuários para calcular um horário de envio ideal. Neste caso, todas as mensagens com Intelligent Timing iriam para o fallback e seriam enviadas ao mesmo tempo de qualquer forma.
{% endalert %}

{% alert tip %}
É normal que os e-mails sejam enviados para a pasta de spam durante o aquecimento de IP porque seu domínio e IP ainda não estabeleceram uma reputação positiva. Se o e-mail cair na sua pasta de spam, o administrador de e-mail pode precisar adicionar seu domínio de envio Braze e IP à lista de permissões da sua empresa.
{% endalert %}

