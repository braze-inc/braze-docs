---
nav_title: Aquecimento por IP
article_title: Aquecimento IP
page_order: 1
page_type: reference
description: "Este artigo de referência aborda o tópico de aquecimento de IP e práticas recomendadas."
channel: email

---

# Aquecimento por IP

> O aquecimento de IP é a prática de acostumar os provedores de caixas de entrada de e-mail a receber mensagens de seus endereços IP dedicados. É uma parte extremamente importante do envio de e-mails com qualquer provedor de serviços de e-mail (ESP) e uma prática padrão na Braze para confirmar que suas mensagens chegam às caixas de entrada de destino em uma taxa consistentemente alta.

O IP warming foi projetado para ajudá-lo a estabelecer uma reputação positiva com os provedores de serviços de Internet (ISPs). Toda vez que um novo endereço IP é usado para enviar um e-mail, os ISPs monitoram programaticamente esses e-mails para verificar se ele não está sendo usado para enviar spam aos usuários.

## E se eu não tiver tempo para aquecer os IPs?

**É necessário o aquecimento do IP.** Se você não aquecer os IPs adequadamente e o padrão do seu e-mail causar alguma suspeita, a velocidade de entrega do seu e-mail poderá ser significativamente reduzida ou diminuída. Seu domínio ou IP também pode ser bloqueado pelos ISPs, o que pode fazer com que seus e-mails sejam enviados diretamente para a pasta de spam da caixa de entrada do usuário. Por isso, é importante aquecer seus IPs adequadamente.

Os ISPs limitam a entrega de e-mails quando surge a suspeita de spam, para que possam proteger seus usuários. Por exemplo, se você enviar para 100.000 usuários, o ISP poderá entregar o e-mail apenas para 5.000 desses usuários na primeira hora. Em seguida, o ISP monitora as medidas de engajamento, como taxas de abertura, taxas de cliques, cancelamentos de assinatura e relatórios de spam. Portanto, se ocorrer um número significativo de denúncias de spam, eles poderão optar por relegar o restante do envio para a pasta de spam em vez de entregá-lo na caixa de entrada do usuário. 

Se o engajamento for moderado, eles poderão continuar a limitar seu e-mail para coletar mais dados de engajamento e determinar com mais certeza se o e-mail é ou não spam. Se o e-mail tiver métricas de engajamento muito altas, eles poderão deixar de acelerar esse e-mail completamente. Eles usam esses dados para criar uma reputação de e-mail que acabará determinando se seus e-mails serão ou não filtrados para spam automaticamente.

Se o seu domínio ou IP for bloqueado por um ISP, os registros de mensagens no [Registro de atividades de mensagens]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) conterão informações sobre quais sites visitar para apelar a esses ISPs e sair dessas listas.

## Programações de aquecimento de IP

É altamente recomendável aderir a esse cronograma de aquecimento de IP estritamente para apoiar a capacidade de entrega. Também é importante que você não pule dias, pois o escalonamento consistente melhora as métricas de entrega.

Dia | \# Número de e-mails a serem enviados
----|--------------------------|
1 | 50
2 | 100
3 | 500
4 | 1,000
5 | 5,000
6 | 10,000
7 | 20,000
8 | 40,000
9 | 70,000
10 | 100,000
11 | 150,000
12 | 250,000
13 | 400,000
14 | 600,000
15 | 1,000,000
16 | 2,000,000
17 | 4,000,000
18+ | Dupla diária até o volume desejado

Sugerimos que você se aqueça até seu pico de envio. Ou seja, se você normalmente envia 2 milhões de e-mails por dia, mas planeja enviar 7 milhões durante um período sazonal, esse "pico" de envio é o que você deve esperar.

Quando o aquecimento estiver concluído e você tiver atingido o volume diário desejado, deve procurar manter esse volume diariamente. Algumas flutuações são esperadas, mas atingir o volume desejado e depois fazer um envio em massa apenas uma vez por semana pode afetar negativamente suas métricas de entrega e a reputação do remetente. 

{% alert important %}
A maioria dos ISPs armazena dados de reputação por apenas 30 dias. Se você passar um mês sem enviar nenhuma mensagem, terá que repetir o processo de aquecimento do IP.
{% endalert %}

## Como limitar os envios durante o aquecimento

Nosso recurso integrado de limitação de usuários serve como uma ferramenta útil para ajudá-lo a aquecer seu endereço IP. Depois de escolher os segmentos de mensagens desejados durante a criação da campanha, na etapa [Target Users (Usuários-alvo]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas) ), selecione o menu suspenso **Advanced Options (Opções avançadas** ) para limitar seus usuários. À medida que seu cronograma de aquecimento continua, você pode aumentar gradualmente esse limite para aumentar o volume de e-mails que envia.

\![]({% image_buster /assets/img_archive/email_ip_warming_sends_limit_new.png %})

## Segmentação de subdomínio

Muitos ISPs e provedores de acesso a e-mail não filtram mais apenas pela reputação do endereço IP. Essas tecnologias de filtragem agora também levam em conta a reputação baseada em domínio. Isso significa que os filtros examinarão todos os dados associados ao domínio do remetente e não apenas o endereço IP. Por esse motivo, além de aquecer seu IP de e-mail, também recomendamos ter domínios ou subdomínios separados para marketing, transações e correio corporativo. 

{% alert important %}
A segmentação de subdomínios é especialmente importante para remetentes de grande volume. Esses remetentes devem trabalhar com um representante da Braze ao configurar sua conta para confirmar que estão aderindo a essa prática.
{% endalert %}

Recomendamos segmentar seus domínios de modo que o e-mail corporativo seja enviado por meio de seu domínio de nível superior e o e-mail de marketing e transacional seja enviado por meio de domínios ou subdomínios diferentes.

## Práticas recomendadas

Todas as consequências de não aquecer o IP podem ser evitadas se você seguir estas práticas recomendadas de aquecimento do IP.

### Comece com pequenos volumes de envio de e-mail

Aumente a quantidade que você envia todos os dias da forma mais gradual possível. As campanhas de e-mail abruptas e de grande volume são vistas com mais ceticismo pelos ISPs. Portanto, você deve começar enviando pequenas quantidades de e-mail e aumentar gradualmente o volume de e-mail que pretende enviar. Independentemente do volume, sugerimos que você aqueça seu IP por segurança. Consulte a [programação de aquecimento do IP](#ip-warming-schedule).

### Ter conteúdo introdutório envolvente

Confirme se o seu primeiro conteúdo é altamente envolvente e maximiza a probabilidade de os usuários clicarem, abrirem e se envolverem com seu e-mail. Sempre prefira e-mails bem direcionados a explosões indiscriminadas ao aquecer IPs.

### Defina uma cadência de envio consistente

Quando o aquecimento do IP estiver concluído, crie uma cadência de envio, certificando-se de distribuir seus e-mails em um dia ou vários dias. Ao criar uma programação o mais consistente possível, você pode evitar um resfriamento do IP, que pode ocorrer se o volume de envio parar ou diminuir significativamente por mais de alguns dias. 

Consulte nosso [cronograma de aquecimento de IP](#ip-warming-schedules) para distribuir seu envio em um período de tempo mais longo, em vez de enviar uma explosão em massa em um único momento específico.

### Limpe suas listas de e-mail

Confirme se sua lista de e-mails está limpa e não tem e-mails antigos ou não verificados. O ideal é garantir que você esteja [em conformidade com a CASL e com a CAN-SPAM]({{site.baseurl}}/user_guide/administrative/privacy/spam_regulations/).

### Monitore sua reputação de remetente

Ao conduzir o processo de aquecimento de IP, certifique-se de monitorar cuidadosamente a reputação do remetente enquanto conduz o processo de aquecimento de IP. É importante observar essas métricas específicas:
- **Taxas de rejeição:** Se alguma campanha tiver mais de 3 a 5% de devoluções, você deverá avaliar a limpeza de sua lista seguindo as diretrizes de nosso site [Keep It Clean: A importância da higiene da lista de e-mails](https://www.braze.com/blog/email-list-hygiene/) article. Além disso, você deve considerar a implementação de uma [política de suspensão]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sunset_policies/) para interromper o envio de e-mails para endereços de e-mail não engajados ou inativos.
- **Relatórios de spam:** Se alguma campanha for relatada como spam a uma taxa superior a 0,08%, você deverá reavaliar o conteúdo que está enviando, verificar se ele é direcionado a um público interessado e certificar-se de que seus e-mails sejam redigidos de forma adequada para despertar o interesse dele.
- **Taxas de abertura:** As taxas de abertura são um indicador útil do posicionamento na caixa de entrada. Se suas taxas de abertura exclusivas forem superiores a 25%, é provável que você esteja tendo um posicionamento alto na caixa de entrada, o que indica uma reputação positiva do remetente.

{% alert tip %}
A Braze recomenda não usar o [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) para aquecer seus IPs. Como as campanhas de aquecimento de IP são algumas das primeiras campanhas que você envia, o Braze não terá informações suficientes sobre seus usuários para calcular o tempo ideal de envio. Nesse caso, todas as mensagens com Intelligent Timing teriam como padrão o horário de fallback e seriam enviadas ao mesmo tempo de qualquer forma.
{% endalert %}

{% alert tip %}
É normal que os e-mails sejam enviados para a pasta de spam durante o aquecimento do IP porque seu domínio e IP ainda não estabeleceram uma reputação positiva. Se o e-mail for parar na sua pasta de spam, o administrador de e-mail talvez precise adicionar o domínio e o IP de envio do Braze à lista de permissões da sua empresa.
{% endalert %}

