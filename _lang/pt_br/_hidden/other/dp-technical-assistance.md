---
nav_title: Assistência técnica de proteção de dados
article_title: Assistência técnica de proteção de dados
page_order: 1
description: "Esta página fornece instruções técnicas para ativá-lo a gerenciar, por meio da Plataforma Braze, solicitações de indivíduos em relação a seus direitos de dados pessoais."
alias: /help/dp-technical-assistance/
permalink: /dp-technical-assistance/
hide_toc: true
---

<!--
Warning! Don't make any changes to this document without approval from the legal department.
-->

# Assistência técnica de proteção de dados

Há uma série de leis de proteção de dados que regulam o que as organizações podem fazer com os dados pessoais ("Leis de Proteção de Dados"), incluindo o Regulamento Geral de Proteção de Dados da UE e do Reino Unido ("GDPR"), a Lei de Privacidade do Consumidor da Califórnia ("CCPA") e a Lei de Portabilidade e Responsabilidade de Seguros de Saúde ("HIPAA"). Existem outras leis e normas nacionais, estaduais e específicas do setor que podem se aplicar à sua empresa.

Essas leis de proteção de dados concedem aos indivíduos "direitos de privacidade" sobre seus dados pessoais. As organizações são obrigadas a receber e responder às solicitações de indivíduos que exercem seus direitos de privacidade. A plataforma Braze pode ajudá-lo a cumprir essas Leis de Proteção de Dados, fornecendo recursos para facilitar determinadas ações exigidas por essas leis. Este documento fornece instruções técnicas para usar esses recursos para gerenciar solicitações de direitos de privacidade. Cabe a você determinar quais leis de proteção de dados se aplicam à sua empresa e agir em conformidade com elas.

## Isenção de responsabilidade legal

Nenhuma das informações a seguir tem a intenção de ser, nem deve ser considerada, uma assessoria jurídica da Braze. Recomenda-se que o usuário busque a orientação de seu próprio advogado com relação à sua situação específica e à forma como as Leis de Proteção de Dados se aplicam a ele e ao seu uso dos Serviços Braze.

## Terminologia

Para os fins deste documento, qualquer referência a dados pessoais também pode ser entendida como uma referência a informações pessoais ou informações de identificação pessoal ("Dados Pessoais"). Para simplificar, geralmente usamos a redação do GDPR ao abordar os direitos dos usuários finais. A redação do GDPR é muitas vezes intercambiável ou estreitamente alinhada com um termo ou conceito definido de outras leis de proteção de dados.

## noções básicas

A maioria das leis de privacidade define três partes interessadas principais que estão envolvidas no processamento de dados pessoais: titulares de dados, controladores de dados e processadores de dados. Cada grupo tem direitos e responsabilidades diferentes com relação ao uso de Dados Pessoais:

- Um titular de dados é um indivíduo cujos Dados Pessoais estão sendo processados pelo processador ou controlador de dados
- Um controlador de dados é uma entidade que determina as finalidades e os meios de processamento dos Dados Pessoais
- Um processador de dados é uma entidade que processa Dados Pessoais em nome e sob as instruções do controlador de dados

Em relação à plataforma Braze:

- Os titulares dos dados são, por exemplo, os usuários finais do seu aplicativo de cliente (e.g., seus clientes) ou seus colaboradores que são usuários do dashboard na sua instância da plataforma Braze.
- Você, o cliente Braze, é o controlador de dados que decide como e por que os Dados Pessoais dos titulares dos dados serão coletados e processados na plataforma Braze.
- A Braze é uma processadora de dados que processa os Dados Pessoais na plataforma Braze em seu nome e de acordo com as instruções que recebemos de você.

Os termos acima são do GDPR, mas, por exemplo, os termos comparáveis da CCPA são:

- "consumidores" para os titulares de dados.
- "empresas" para controladores de dados.
- "prestadores de serviço" para processadores de dados.

Você encontrará abaixo informações relevantes sobre as solicitações de direitos de privacidade mais comuns dos titulares dos dados, incluindo como você pode respondê-las por meio dos recursos técnicos da plataforma Braze.

## O direito de ser informado

O direito de ser informado engloba sua obrigação de fornecer "informações de processamento justo", normalmente por meio de um aviso de privacidade. Ele enfatiza a necessidade de transparência sobre como você usa os Dados Pessoais.

### Recomendação de Braze

A maioria das leis de proteção de dados enfatiza a necessidade de transparência em relação à forma como você usa os dados pessoais. Essa é a responsabilidade dos controladores de dados, que normalmente manterão um aviso de privacidade facilmente acessível aos usuários de seus produtos e serviços e que abranja o processamento feito pelo Braze.

## O direito de acesso

De acordo com as Leis de Proteção de Dados, os titulares de dados podem ter o direito de obter:

- Confirmação de que seus dados pessoais estão sendo processados,
- Acesso a seus dados pessoais, e
- Outras informações complementares, conforme determinado pela Lei de Proteção de Dados aplicável.

### Recomendação de Braze

Para fornecer dados pessoais da Braze em um formato legível por máquina em resposta a uma solicitação de acesso do titular dos dados, você poderá exportar o perfil do usuário final fazendo uma chamada de API para as [APIs REST](https://www.braze.com/docs/api/endpoints/export/#user-export) da Braze com o identificador de usuário (definido por você como `external_id` fornecido à Braze) e/ou o identificador do dispositivo.

## O direito de retificação

Os indivíduos têm o direito de ter seus dados pessoais corrigidos se estiverem imprecisos ou incompletos. Se o usuário tiver divulgado os dados pessoais em questão a terceiros, poderá considerar a necessidade de informá-los sobre a retificação, quando possível.

### Recomendação de Braze

Caso um Titular dos Dados solicite a retificação de imprecisões nos Dados Pessoais que estão sendo processados por você ou pela Braze em seu nome, você poderá usar os SDKs da Braze ou as [APIs REST](https://www.braze.com/docs/api/endpoints/user_data/#user-track-endpoint) da Braze para corrigir esses Dados Pessoais.

## O direito à exclusão

O direito de exclusão também é conhecido como "direito de ser esquecido" ou "direito de ser excluído".

### Recomendação de Braze

#### Eliminação padrão 

Depois de interromper a coleta de dados, você poderá usar [o endpoint da API REST de Exclusão de Usuário do Braze](https://www.braze.com/docs/api/endpoints/user_data/post_user_delete/) para excluir um usuário final, o que removerá todos os registros desse usuário final dos Serviços do Braze:

- Para usuários finais que têm um external_id nos Serviços, é possível usar esse ID para excluir os dados desse usuário final.
- Para usuários finais anônimos que não têm um external_id nos Serviços, você pode recuperar o identificador do dispositivo desse usuário final usando o Braze SDK e pode usar o identificador do dispositivo para encontrar o perfil do usuário final associado a esse dispositivo. Em seguida, é possível usar a API de exclusão de usuário para excluir o perfil associado a esse usuário final.

A exclusão de um usuário final dos Serviços Braze excluirá permanentemente o Perfil de Usuário centralizado da Braze para esse usuário final, conforme definido pelo `external_id` fornecido. Isso inclui informações de perfil estruturadas que o Braze coletou por padrão ou que você configurou os Serviços Braze para coletar, como informações do dispositivo, país, idioma e endereço de e-mail.

Observe que o endereço de e-mail ou o número de telefone associado ao perfil do usuário final ainda poderá ser armazenado pelo Braze, pois poderá estar associado ao perfil de outro usuário final. Os envios de e-mail e números de telefone não são exclusivos dos Serviços Braze. Isso significa que sua equipe poderia ter configurado o Braze para armazenar o mesmo endereço de e-mail ou número de telefone em vários perfis de usuário. Se a sua equipe tiver configurado o Braze dessa forma, esteja ciente de que talvez seja necessário excluir todos os perfis de usuários que representam um determinado titular de dados para atender a uma solicitação de exclusão de um titular de dados, e sua equipe precisaria fazer várias chamadas de API para excluir todos os perfis de usuários que se referem a um determinado titular de dados.

#### Considerações adicionais sobre a exclusão

<style>
#considerations td {
    word-break: break-word;
    width: 100%;
    font-size: 16px;
}
</style>

<table id="considerations">
<tbody>
  <tr>
    <td>
        <p>Os clientes podem criar campos personalizados para propriedades de eventos e extras de mensagens. Esses campos não se destinam a dados pessoais e, portanto, não estão incluídos no processo de exclusão padrão descrito acima. Se, no entanto, você usar o Braze para inserir ou coletar dados pessoais por meio de propriedades de eventos e extras de mensagens, poderá configurar o processo de exclusão disparado pelo endpoint da API REST de exclusão de usuários para incluir também esses campos, de modo que os dados contidos nesses campos também sejam excluídos.</p>
        <p>As configurações padrão são aplicadas no nível da empresa, mas você pode optar por excluir os seguintes campos quando o processo de exclusão for executado, no nível do grupo de app/espaço de trabalho:</p>
    <ul>
        <li>PROPRIEDADES para USERS_BEHAVIORS_CUSTOMEVENT</li>
        <li>PROPERTIES for USERS_BEHAVIORS_PURCHASE</li>
        <li>MESSAGE_EXTRAS para:</li>
            <ul>
            <li>USERS_MESSAGES_CONTENTCARD</li>
            <li>USERS_MESSAGES_EMAIL_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_SEND</li>
            <li>USERS_MESSAGES_PUSHNOTIFICATION_RETRYSEND_SHARED</li>
            <li>USERS_MESSAGES_WEBHOOK_SEND</li>
            <li>USERS_MESSAGES_SMS_SEND</li>
            <li>Eventos futuros de envio de mensagens</li>
            </ul>
    </ul>
    <p>As configurações para isso podem ser acessadas em <b>Configurações da empresa</b> > <b>Configurações administrativas</b> > <b>Configurações de segurança</b>. As preferências de exclusão de dados são definidas por tipo ou categoria de evento. Somente um usuário com preferências de administrador pode fazer alterações nessas configurações. Como alternativa, um administrador pode delegar essas permissões a outro usuário.</p>
    <p>Se um tipo de evento ou mensagem extra for definido para ser incluído no processo de exclusão, os dados desse campo serão excluídos no futuro para os usuários para os quais você estiver executando um User Delete REST API Endpoint. Além disso, quando você selecionar essa preferência de exclusão, no próximo trabalho de exclusão programado, os dados desses campos serão excluídos de quaisquer conjuntos de dados anônimos existentes que contenham esses campos. Não será possível restaurar os campos de dados excluídos.</p>
    </td>
  </tr>
</tbody>
</table>

#### Análise de dados

Para manter a integridade da análise de uso de campanhas e aplicativos, os dados agregados anônimos não serão modificados quando um usuário final for excluído. Por exemplo, o Braze não diminuirá o número total de sessões de um app quando um usuário final for excluído. A(s) sessão(ões) em que esse usuário final visitou o aplicativo ainda será(ão) incluída(s) no número total de visitas a esse aplicativo, mas esses dados não serão conectados de forma alguma ao perfil do usuário final esquecido, garantindo que esses dados anônimos e agregados não possam ser vinculados a um usuário final individual.

As análises de dados nos Serviços Braze estão vinculadas ao Identificador de usuário final Braze. Depois que o perfil do usuário final for excluído, o Identificador de Usuário Braze se tornará efetivamente um identificador completamente anônimo, pois a Braze não poderá vinculá-lo a nenhum usuário final individual.

#### Uma vez que a exclusão tenha ocorrido

Em geral, espera-se que você envide esforços razoáveis para notificar os titulares dos dados quando tiver atendido à solicitação deles para apagar seus Dados Pessoais. Um usuário final excluído poderá se registrar novamente ou se engajar novamente com seu app ou serviço em uma data posterior, e o Braze não poderá identificá-lo como o usuário excluído ou esquecido. Os Serviços Braze não são capazes de criar listas de identificadores de usuários ou endereços de e-mail excluídos em seu nome.

## O direito à restrição de processamento

Os titulares dos dados podem ter o direito de "bloquear" ou suprimir o processamento de seus Dados Pessoais em determinadas circunstâncias. Restringir o processamento significa não realizar qualquer processamento ao qual o titular dos dados tenha se oposto.

### Recomendação de Braze

Os Serviços da Braze não suportam a restrição do processamento de categorias individuais de Dados Pessoais. Caso tenha sido solicitado por um titular de dados a restringir o processamento de determinados subconjuntos de Dados Pessoais desse titular de dados, você deverá usar as [APIs do Braze](https://www.braze.com/docs/api/home/) para exportar todo(s) o(s) perfil(is) desse usuário final e, em seguida, [excluí-lo](https://www.braze.com/docs/api/endpoints/user_data/#user-delete-endpoint) (s) do Braze. As APIs da Braze podem ser usadas para reimportar esses dados no caso de o usuário final permitir posteriormente que você processe esses subconjuntos específicos de seus Dados Pessoais. Além disso, recomenda-se que o usuário final desinstale ou saia de todo e qualquer aplicativo que use o SDK do Braze para interromper a coleta de dados adicionais sobre o titular dos dados.

## O direito à portabilidade de dados

O direito à portabilidade de dados permite que os titulares de dados obtenham e reutilizem seus dados pessoais para seus próprios fins em diferentes serviços. Os dados pessoais devem ser fornecidos em um formato estruturado, legível por máquina e comumente usado.

### Recomendação de Braze

Semelhante ao Direito de Acesso, você pode usar a Braze [REST API](https://www.braze.com/docs/api/endpoints/export/#user-export) para exportar os Dados Pessoais de um usuário final e fornecê-los ao Titular dos Dados de acordo com sua solicitação.

## O direito de contestar

Os indivíduos podem ter o direito de se opor a:

- processamento baseado em interesses legítimos ou na performance de uma tarefa de interesse público/exercício de autoridade oficial (incluindo criação de perfis);
- marketing direto (incluindo criação de perfis); e
- processamento para fins de pesquisa científica/histórica e estatística.

### Recomendação de Braze

O Braze oferece a capacidade de marcar um perfil de usuário como tendo cancelado a inscrição de SMS, e-mails ou notificações por push por meio de nossas [APIs REST](https://www.braze.com/docs/api/home/) de e-mail e dos SDKs [para iOS](https://www.braze.com/docs/developer_guide/platform_integration_guides/ios/analytics/setting_custom_attributes/), [Android](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) e [Web](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/analytics/setting_custom_attributes/). Se receber objeções dos Titulares dos Dados quanto ao recebimento de tais mensagens, poderá usar as APIs do Braze para cancelar a inscrição desses usuários finais.

Se isso não for suficiente, para evitar o processamento de dados pessoais de usuários finais pela Braze, o perfil do usuário final deverá ser excluído da mesma forma que a especificada no "Direito de Exclusão".

## Direitos relacionados à tomada de decisões automatizadas e à criação de perfis

Algumas leis de proteção de dados impedem ou permitem que os titulares dos dados aceitem a tomada de decisões automatizadas ou a criação de perfis em determinadas circunstâncias, em particular para decisões que "produzam um efeito legal ou um efeito similarmente significativo sobre o indivíduo".

### Recomendação de Braze

A Braze não realiza nenhuma ação automatizada de criação de perfil ou tomada de decisão com ramificações legais ou equivalentes para os titulares dos dados. Se o usuário acreditar que seu próprio uso da Plataforma Braze terá impactos legais ou equivalentes e tiver recebido uma objeção a isso, poderá optar por excluir o Perfil de Usuário da mesma forma que no "Direito de Exclusão".

## Direcionamento da publicidade

De acordo com algumas leis de privacidade do estado dos EUA, os titulares dos dados podem se opor ao uso de seus Dados Pessoais para fins de direcionamento de publicidade.

### Recomendação de Braze

Ao criar públicos para fins de direcionamento de anúncios para seus titulares de dados, você deve garantir que excluiu todos os titulares de dados que se opuseram à publicidade direcionada, por exemplo, os consumidores da Califórnia que exerceram seu direito de "Não vender ou compartilhar" nos termos da CCPA.

Para saber mais sobre como criar públicos para sincronizar com plataformas de terceiros, consulte [Sincronização de públicos](https://www.braze.com/docs/partners/canvas_steps).

## O direito à não discriminação 

Os titulares de dados têm o direito de exercer seus direitos de privacidade sem discriminação.

### Recomendação de Braze

Em seu uso dos Serviços Braze, os clientes devem garantir que não discriminem os dados de clientes que tenham exercido seus direitos de privacidade. Por exemplo, recomendamos que os titulares de dados que tenham exercido seus direitos de privacidade não sejam segmentados em públicos ou direcionados de outra forma que possa discriminá-los.