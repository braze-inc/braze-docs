---
nav_title: Descontinuação do TLS 1.0 e 1.1
page_order: 2

page_type: update
description: "Este artigo descreve a descontinuação do TLS 1.0 e TLS 1.1 pela Braze, concluída em maio de 2018."
---
# Descontinuação do TLS 1.0 e 1.1

{% alert update %}
A Braze removeu o suporte para cifras de Segurança da Camada de Transporte (TLS) tanto no TLS 1.0 quanto no 1.1, de acordo com as recomendações feitas pelo Conselho de Padrões de Segurança PCI. Realizamos essa descontinuação de suporte em duas fases, concluídas em maio de 2018.
{% endalert %} 

## Fundo

A Braze está descontinuando cifras de Segurança da Camada de Transporte (TLS) conhecidas como fracas tanto no TLS 1.0 quanto no 1.1, de acordo com as recomendações feitas pelo Conselho de Padrões de Segurança PCI em duas fases que concluem em maio de 2018.

Esta mudança não está sendo feita em resposta a qualquer violação ou problema relacionado à plataforma da Braze, mas como uma medida de precaução para manter nossos padrões de segurança e dados de classe mundial, e para proteger proativamente nossos clientes e seus clientes.

Nos últimos anos, uma série de problemas de segurança sistemáticos associados tanto ao TLS quanto ao seu predecessor, Secure Sockets Layer (SSL), incluindo [POODLE](https://www.us-cert.gov/ncas/alerts/TA14-290A), [Heartbleed](https://en.wikipedia.org/wiki/Heartbleed), [LOGJAM](https://en.wikipedia.org/wiki/Logjam_(computer_security)) e outros, ameaçaram o tráfego web criptografado e expuseram partes da internet a violações de segurança. Juntamente com outras empresas de tecnologia, a Braze já tomou medidas para desativar protocolos e cifras de criptografia fracos à medida que os ataques são descobertos—por exemplo, removendo o suporte para SSLv3 em 2014.

Mais recentemente, o PCI Security Standards Council lançou orientações relacionadas à criptografia em abril de 2015 para o [Payment Card Industry Data Security Standard](https://en.wikipedia.org/wiki/Payment_Card_Industry_Data_Security_Standard) (PCI-DSS). A orientação exclui SSL 3.0, TLS 1.0 e alguns dos pacotes de cifras compatíveis com TLS 1.1 da sua lista de protocolos de cifras criptográficas fortes, e incentiva as empresas a descontinuarem o suporte para esses protocolos ou cifras para garantir a segurança dos usuários da internet.

Um conjunto de cifras é uma combinação de algoritmos que fornecem criptografia, autenticação e integridade das comunicações ao negociar uma conexão SSL ou TLS segura. Quando é descoberto que é possível quebrar uma cifra específica—independentemente de haver ou não ataques conhecidos atualmente—a cifra é considerada como tendo "fraquezas" que poderiam ativar ataques futuros. Ao excluir essas cifras TLS dos requisitos de conformidade PCI DSS, o Conselho PCI DSS está exigindo que os provedores de serviços aceitem apenas os melhores padrões de criptografia. O Conselho PCI DSS estabeleceu um prazo até 30 de junho de 2018 para conformidade com o requisito de criptografia para interromper o suporte ao TLS 1.0 e TLS 1.1.

## Plano de descontinuação da Braze
Para cumprir as recomendações do Conselho PCI DSS, a Braze aumentará as versões mínimas de TLS que são aceitas em nossos Serviços. Para lhe dar uma melhor ideia sobre nosso plano de conformidade e seu impacto potencial em sua marca e seus usuários, há duas fases principais em nosso plano para estar ciente:

### Fase 1: 1 de outubro de 2017

A Braze removerá a capacidade de usar as seguintes cifras do dashboard Web e APIs REST da Braze:

- `TLS_RSA_WITH_AES_256_CBC_SHA`
- `TLS_RSA_WITH_AES_128_CBC_SHA`
- `TLS_RSA_WITH_AES_256_CBC_SHA256`
- `TLS_RSA_WITH_AES_256_GCM_SHA384`
- `TLS_RSA_WITH_AES_128_CBC_SHA256`
- `TLS_RSA_WITH_AES_128_GCM_SHA256`
- `TLS_RSA_WITH_3DES_EDE_CBC_SHA`

Esta mudança não deve impactar os clientes que acessam o dashboard da Braze, pois todos os navegadores modernos aceitam cifras mais seguras. No entanto, se você encontrar um erro de criptografia SSL ao acessar o dashboard da web após 1º de outubro, poderá resolver o problema simplesmente atualizando para a versão mais recente do seu navegador da web.

Sua equipe de engenharia deve garantir que não esteja usando nenhum desses cifradores para comunicação de servidor para servidor com as APIs REST da Braze. Se estiverem, precisarão atualizar seu código para usar cifras de criptografia mais seguras antes de 1º de outubro para continuar usando as APIs da Braze. No entanto, para manter o suporte a dispositivos móveis antigos e desatualizados que podem estar usando cifras fracas, a Braze continuará a suportar essas cifras nas APIs que recebem dados de nossos SDKs.

### Fase 2: 31 de maio de 2018

A Braze estará desativando o suporte para TLS 1.0 e TLS 1.1 em todos os serviços da plataforma em 31 de maio de 2018 — incluindo o dashboard da Braze, APIs REST e APIs que se comunicam com nossos SDKs. Também removeremos o suporte para as cifras listadas na seção anterior em conexão com as APIs que recebem dados do SDK. Isso significa que nenhuma comunicação TLS 1.0 e 1.1 de e para Braze será mais pela nossa rede a partir desta data.

Como resultado dessa mudança, alguns dispositivos móveis antigos ou desatualizados—provavelmente aqueles que executam versões antigas do Android—podem perder a capacidade de se comunicar com a Braze, impedindo-os de enviar dados para a Braze ou receber mensagens no app da Braze. No entanto, prevemos que a mudança afetará apenas um pequeno número de dispositivos. Qualquer dispositivo afetado também perderá a capacidade de se comunicar com qualquer site ou serviço compatível com PCI um mês depois, em 30 de junho de 2018, data definida pelo Conselho PCI DSS para a remoção das cifras TLS 1.0 e TLS 1.1.

## Plano de ação
Se a sua marca estiver utilizando as APIs REST da Braze, fale com sua equipe de engenharia para garantir que todas as chamadas de servidor para servidor para a Braze estejam usando TLS 1.2 conforme listado acima, a fim de evitar uma interrupção do serviço. Saiba que algumas linguagens de programação—como o Java 7—usam versões mais antigas do TLS por padrão, então sua equipe de engenharia pode precisar fazer algumas alterações no código para ser compatível com os requisitos de criptografia atualizados.

Dispositivos Apple não serão afetados pela descontinuação planejada da Braze porque a Apple exige TLS 1.2 desde o final de 2016. O mesmo vale para os navegadores web modernos, então não prevemos que essas mudanças terão qualquer impacto no uso do SDK para Web. No entanto, dispositivos Android executando Android 4.4 (KitKat) ou inferior podem não usar TLS 1.2 por padrão, então tome medidas para fazer upgrade de qualquer uma de suas integrações Android para pelo menos a versão 2.0.3 do SDK da Braze (que usa TLS 1.2 por padrão, se um determinado dispositivo puder suportá-lo) até 31 de maio de 2018.

Por fim, devido às conhecidas fraquezas no TLS 1.0 e no conjunto de cifras TLS 1.1, é possível que ataques possam surgir no futuro, o que exigiria que a Braze acelerasse nosso plano de descontinuação, a fim de proteger a segurança de todos os nossos clientes. A Braze monitorará o estado da segurança e quaisquer ataques relevantes associados aos protocolos TLS 1.0 e 1.1, e divulgará se souber de quaisquer ataques que alterem o cronograma estabelecido nas seções anteriores. Mas, por causa desse impacto potencial, recomendamos fortemente que você trabalhe com sua equipe de engenharia para garantir que suas chamadas de API para a Braze estejam protegidas com TLS 1.2 e que você planeje fazer upgrade para o SDK mais recente do Android nos próximos meses.


