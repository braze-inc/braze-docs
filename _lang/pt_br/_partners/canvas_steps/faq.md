---
nav_title: Perguntas frequentes
article_title: Perguntas frequentes sobre o Audience Sync
description: "Este artigo fornece respostas a perguntas frequentes sobre o Audience Sync."
page_order: 80
Tool:
  - Canvas

---

# Perguntas frequentes

> Este artigo fornece respostas a algumas perguntas frequentes sobre o Audience Sync.

### Quanto tempo leva para que meus públicos sejam preenchidos no meu dashboard de parceiro do Audience Sync?

O tempo necessário para preencher um público depende do parceiro específico. Todas as redes processarão as solicitações do Braze e tentarão combinar os usuários. Em geral, esse processo pode levar de 6 a 48 horas.

É possível verificar o intervalo de tempo específico na seção Solução de problemas da documentação de cada parceiro do Audience Sync.

### Que tipo de dados primários posso usar no meu Audience Sync?

Os campos específicos usados para cada parceiro podem variar de acordo com os requisitos do parceiro. 

Por exemplo, ao configurar uma sincronização de público do Facebook, você poderá usar uma ampla variedade de campos primários, como e-mail, telefone, nome e sobrenome, ao passo que, com o Snapchat, você só poderá selecionar e-mail, telefone ou ID do anunciante móvel. 

É importante notar que os campos de usuário que podem ser selecionados para sincronização estão correlacionados com os atributos padrão do Braze e os IDs de publicidade móvel. Você deve garantir a transmissão adequada desses dados por meio de nossos SDKs ou APIs. 

### O que acontece quando meus dados estão sendo processados para serem enviados a cada parceiro do Audience Sync?

Os dados que você selecionar para enviar ao destino do Audience Sync serão normalizados. Cada parceiro pode ter especificações diferentes para a normalização de dados com base em seus requisitos de API, portanto, consulte o endpoint específico de cada parceiro para obter mais detalhes.

Além disso, o Braze criará hashes para todos os dados antes de sincronizar os usuários com nossos parceiros do Audience Sync, garantindo que todos os IPI sejam criptografados usando SHA256.

### Por que posso selecionar vários identificadores em uma etapa para alguns parceiros, mas só posso selecionar um identificador para outros?

Isso é determinado pelos métodos de integração com parceiros e não é controlado pelo Braze. Alguns parceiros (como o Meta) permitem a sincronização de vários identificadores e outros parceiros (como o Google) permitem que apenas um único identificador seja sincronizado com um usuário em um determinado momento.

### Como faço para reconectar minha integração?

Se o usuário anterior que conectou a integração não estiver mais na sua empresa, será necessário atualizar a integração com o novo usuário. Você pode fazer isso selecionando **Confirm (Confirmar**). Note que isso pode interromper as telas ativas.

O usuário que está se reconectando deve ter acesso de leitura e gravação a todos os públicos para que os usuários possam ser sincronizados com sucesso com os parceiros. Verifique se o usuário que está reconectando a integração tem acesso às mesmas contas de anúncios e públicos. Não deve haver necessidade de editar nenhuma etapa do Canva existente. 

### Quais são os erros mais comuns que podem ocorrer ao criar e gerenciar minhas sincronizações do público?

- **Token inválido**<br>
  - As causas típicas incluem a alteração da senha para registro em uma rede de anúncios específica ou a expiração das credenciais.
  - Para resolver esse problema, basta acessar a página específica do parceiro em questão para desconectar e reconectar sua conta.
- **Tamanho do público muito baixo**<br>
  - Esse erro normalmente ocorre quando você cria uma etapa do Audience Sync que remove usuários do seu público. Se o tamanho de seu público se aproximar de zero, a rede poderá sinalizar que ele é muito baixo para ser atendido. 
  - Para resolver esse problema, certifique-se de considerar uma estratégia de sincronização de público que adicione e remova usuários regularmente, de modo a não esgotar totalmente o tamanho do público.
- **O público não existe**<br>
  - Esse erro ocorre porque a etapa do Audience Sync usa um público que não existe. Isso também pode ser disparado se você não tiver a permissão necessária para acessar o público. 
  - Para resolver esse problema, adicione um público ativo na sua configuração do Audience Sync ou crie um novo público.
- **Tentativa de acesso à conta de anúncios**<br>
  - Esse erro ocorre se você não tiver permissões para a conta de anúncios e/ou público que selecionou.
  - Para resolver esse problema, trabalhe com os administradores de sua conta de anúncios para obter o acesso e as permissões adequados. 
- **Configurações inválidas**<br>
  - Esse erro será disparado se você não tiver configurado um destino específico do Audience Sync no canva, incluindo os campos de conta de anúncio, público ou usuário a serem correspondidos. 
  - Para resolver esse problema, conclua a configuração de cada parceiro antes de iniciar.
- **Termos de Serviço**<br>
  - Para alguns destinos do Audience Sync, como o Facebook, a rede de anúncios exige que você aceite termos de serviços específicos para usar o recurso do Audience Sync. Esse erro será disparado se você não tiver aceitado os termos apropriados. 
  - Para resolver esse problema, verifique se você aceitou os termos exigidos de cada parceiro. Especificamente para o Facebook, consulte a [solução de problemas do Facebook]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync/#troubleshooting). 
