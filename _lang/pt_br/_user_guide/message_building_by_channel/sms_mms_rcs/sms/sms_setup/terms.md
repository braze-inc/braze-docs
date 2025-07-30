---
page_order: 1
nav_title: Termos importantes
article_title: Termos importantes de SMS
alias: /sms_terms_to_know/

layout: glossary_page
glossary_top_header: "Terms to Know"
glossary_top_text: "SMS–everyone has it and knows what it is. What they don't know is the nuance. Check out the following terms to learn more about SMS ecosystems, technologies, and processes."
page_type: glossary
description: "Este glossário define vários termos de SMS que você deve conhecer."
channel: SMS 

glossaries:
  - name: SMS (Serviço de Mensagens Curtas)
    description: "Um canal de envio de mensagens criado em 1980 e uma das mais antigas tecnologias de mensagens de texto. Ele também é um dos canais de mensagens de texto mais difundidos e usados com mais frequência. Esse canal é uma maneira mais direta de alcançar seus usuários e clientes do que a maioria dos outros canais de envio de mensagens, pois utiliza o número de telefone pessoal deles para entrar em contato. Por isso, o SMS tem mais regras e regulamentos do que outros canais de envio de mensagens."
  - name: Código curto
    description: Essa é uma sequência curta e memorável de 5 a 6 dígitos que permite que os remetentes enviem mais mensagens a taxas mais consistentes do que números longos (uma mensagem por segundo).<br><br>É necessário um código curto ou longo.
  - name: Código longo
    description: Esse é o número telefônico padrão de 10 dígitos (na maioria dos países) que permite que os remetentes enviem mais mensagens à taxa de uma mensagem por segundo.<br><br>É necessário um código curto ou longo.
  - name: Codificação
    description: A conversão de qualquer coisa em um formato codificado. O conteúdo do SMS pode ser codificado em GSM-7 ou UCS-2.
  - name: Codificação GSM-7 (Sistema Global de Comunicações Móveis)
    description: "O GSM-7 é o padrão de codificação mais visto para a maioria dos envios de mensagens SMS. Ele usa a maioria dos alfabetos grego e inglês, além de alguns caracteres adicionais. Você pode saber mais sobre a codificação GSM-7 e quais conjuntos de caracteres podem ser usados na <a href='https://en.wikipedia.org/wiki/GSM_03.38#GSM_7-bit_default_alphabet_and_extension_table_of_3GPP_TS_23.038_.2F_GSM_03.38' title=\"tabela de alfabeto padrão e extensão de 7 bits do GSMWikipedia\"></a>. Idiomas como chinês, coreano ou japonês devem ser transferidos usando a codificação de caracteres UCS-2 de 16 bits. <br> <br> Você pode estimar que o limite de caracteres por segmento para esse tipo de codificação é de 128 caracteres."
  - name: Codificação UCS-2 (Conjunto de caracteres codificados universais)
    description: "A codificação UCS-2 é um padrão de codificação fallback, especialmente quando uma mensagem não pode ser codificada usando o GSM-7 ou quando um idioma precisa de mais de 128 caracteres para ser renderizado. O USC-2 é melhor medido por <a href='https://en.wikipedia.org/wiki/Code_point'>pontos de código</a>, em vez de \"caracteres\". Independentemente disso, você poderia estimar que o limite de caracteres por segmento para esse tipo de codificação é de 67 caracteres."
  - name: Grupos de inscrições para SMS
    description: Os grupos de inscrições são uma ferramenta do Braze que permite direcionar níveis de inscrição específicos de usuários ou clientes. Os grupos de inscrições para SMS são construídos internamente com base no seu serviço de mensagens e não podem ser compartilhados entre espaços de trabalho.
  - name: Segmentos de mensagem
    description: "Um segmento de mensagem é um agrupamento de até um número definido de caracteres (160 para codificação GSM-7; 67 para codificação UCS-2) que será enviado em um único envio de SMS. Se você enviar um SMS com 161 caracteres usando a codificação GSM-7, verá que há dois (2) segmentos de mensagens que foram enviados. O envio de vários segmentos de mensagens pode resultar em cobranças adicionais."
  - name: Serviço de mensagens
    description: "Uma coleção de códigos longos, códigos curtos e IDs alfanuméricos usados para enviar sua mensagem SMS com o Braze."
  - name: Palavra-chave
    description: "Uma palavra curta que é enviada a um código curto ou longo para interagir com um programa SMS predefinido ou para solicitar a aceitação de um programa específico ou de todos os programas em um código. Por exemplo, <code>STOP</code>. Palavras-chave devem <br> - ser alfanumérico <br> - não têm espaços <br> - ter menos de 10 caracteres. <br> <br> Uma combinação específica de palavra-chave e código curto só pode ser usada em um programa ativo de cada vez. Se for inserida uma palavra-chave que já esteja sendo usada por outro programa, será exibido um erro de validação. <br> <br> Há duas categorias de palavras-chave obrigatórias que todos os provedores de conteúdo de SMS devem cumprir: <code>STOP</code> e <code>HELP</code>."
  - name: Palavra-chave obrigatória HELP
    description: "Para cada programa criado na plataforma do SMS Campaign Manager, o conteúdo para essa palavra-chave deve ser fornecido e precisa atender às práticas recomendadas e à conformidade da operadora por país ou região em que o tráfego de SMS está sendo enviado e recebido. Na maioria dos casos, esse conteúdo deve conter uma breve explicação sobre o programa de SMS e como fazer a aceitação."
  - name: Palavras-chave STOP globais
    description: "As variações incluem <code>STOP</code>, <code>END</code>, <code>QUIT</code>, <code>UNSUBSCRIBE</code>, <code>CANCEL</code>, <code>STOPALL</code>. Eles são chamados de <code>Global-Stop-Keywords</code>. Se qualquer uma dessas palavras-chave for digitada em um código curto ou longo, o número do celular (o número do celular originado) será excluído de todos os programas de SMS ativos no código ao qual está associado."
  - name: Código de vaidade
    description: Um código curto personalizado é um número telefônico de 5 a 6 dígitos selecionado especificamente por uma marca. Os códigos curtos Vanity são de marca e mais fáceis de serem lembrados pelos consumidores.
  - name: Código curto compartilhado
    description: "Ao usar um código curto compartilhado, todas as mensagens de texto, independentemente da empresa ou organização que as envia, chegam ao dispositivo móvel do consumidor a partir do mesmo número de telefone 5-6. Embora os códigos curtos compartilhados tenham um custo relativamente baixo e estejam imediatamente disponíveis, isso significa que sua empresa não terá um código curto dedicado e estará sujeita a que outras empresas sigam o protocolo correto com seu código curto compartilhado." 
  - name: ID alfanumérica do remetente
    description: A ID alfanumérica do remetente permite que você defina o nome ou a marca da sua empresa como ID do remetente usando caracteres alfanuméricos ao enviar mensagens unidirecionais para países compatíveis.
  - name: Número gratuito
    description: "Um número de telefone gratuito ou freephone é um número de telefone que é cobrado por todas as chamadas recebidas em vez de incorrer em cobranças ao assinante do telefone de origem. Os números gratuitos nos EUA e no Canadá são habilitados para SMS, em que os assinantes são cobrados pelos textos recebidos e enviados.<br><br>O envio de mensagens Toll-Free funciona melhor quando o caso de uso é de pessoa para pessoa, como suporte ao cliente ou vendas, com o remetente e o destinatário conversando por texto."
  - name: Envio de mensagens unidirecional
    description: O envio de mensagens unidirecionais permite que você se comunique com seus clientes enviando mensagens de texto. O envio de mensagens unidirecionais é útil se você estiver implementando uma ID de remetente alfanumérica em mercados em que códigos longos e curtos não estão disponíveis. 
  - name: Envio de mensagens bidirecionais
    description: O envio de mensagens bidirecionais permite que você mantenha uma conversa enviando e recebendo mensagens de texto. 
---
