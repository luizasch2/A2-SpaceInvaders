O jogo Space Invaders foi criado no Japão e ficou muito famoso na década de 90. Para a A2, nos inspiramos no jogo. Vale ressaltar que o criado não é igual ao original, é uma releitura. O programa foi criado inteiramente em Python utilizando a biblioteca Pygame.

Separamos os objetos em classes. Cada classe foi separada por arquivos para facilitar o entendimento do código.

## settings.py

Onde estão definidas as configurações iniciais e essenciais do jogo, como o tamanho de tela e dois dicionários (um para cada tamnho de tela) com todas as imagens que serão usadas ao longo do jogo.

## player_config.py 

O arquivo recebe três atributos: imagem, coordenada X e Y, que definem sua posição. A imagem recebida é a skin da nave de configuração padrão, que pode ser alterada no menu opções que será falado posteriormente. Esta classe conta com seis métodos:

### Movimento

O movimento da nave é comandado pelo teclado do jogador. Para tanto, foi definida a variável ```keys = pygame.key.get_pressed()```, um objeto da biblioteca pygame. A partir disso, pode-se passar como índice a tecla que irá definir o movimento e se esta aconter, a ação que deverá ocorrer em seguida

### change_position

Muda a posição da nave quando ele se move

### change_spawn

Muda as configurações da nave quando o tamanho de tela aumenta

### change_image

Muda a skin da nave a partir da escolha do jogador

### blit

Faz a nave aparecer na tela

## enemy.py

A classe Enemy() recebe como atributos as imagens do inimigo, tanto a imagem padrão quanto sua imagem quando a dificuldade aumenta, suas coordenadas, seu estado e sua velocidade. Para ocorrer os eventos, a classe enemy tem alguns métodos:

### change_skin

Muda a skin do inimigo de acorodo com a escolha do jogador

### change_skin_hard e change_skin_to_hard

Ambos métodos servem para mudar a skin do inimigo quando a dificuldade aumenta

### change_position

Muda a posição do inimigo 

### change_vel

Muda a velocidade do inimigo, utilizada para quando há um aumento na dificuldade e o inimigo fica mais rápido

### blit

Faz o inimigo aparecer na tela

## bullet.py

Classe responsável pelo objeto bala, utilizado tanto para a nave quanto para o inimigo

Apresenta os mesmos métodos anteriores com a adição do change_state, que muda seu estado ("fire" ou "stopped"); config_enemy_image que define a imagem da bala do inimigo e, por fim, o método fire, que muda o estado da bala para "fire" e a posiciona na tela

### explosao.py

Nesse arquivo foi definida a classe Explosao() que herda da classe sprite do pygame. Sua utilidade é fazer a animação da bomba, ativada quando ocorre a colisão do inimigo com a bala atirada pelo jogador

### move.py

Esse arquivo contém a classe Move() que define algumas funções importantes e mutáveis ao longo do jogo. Tem como metodo as colisões (```isCollision``` para colisão da bala da nave com o inimigo e ```coliep``` para colisão do inimigo com a nave e da bala do inimigo com a nave). Além disso, há ainda o metodo ```restart``` que define que, quando acionado, o modo do jogo volta para o menu o score zera. Este método é acionado na main quando ocorre o game over e o jogador aperta a tecla "r". Há ainda o método ```add_score``` que adiciona um ponto ao score, chamado na main quando há colisão da bala da nave com o inimigo. Ademais, há o método ```change_mode```, o qual iremos destacar

### change_mode

Define o modo do jogo. O jogo conta com nove modos, chamados de MENU, OPT, RES, CSS, NAVE, MONSTER, BALA, GAMEOVER, GAME  iremos falar a seguir de cada um destes:

#### MENU

A tela inicial do jogo

### OPT

A tela de opções, em que se pode escolher mudar a skin dos objetos e aumentar a tela

### RES

Se o jogador escolher aumentar a tela, ocorre este modo em que o jogador pode apertar 1 para aumenta a tela ou backspace para voltar a sua última tela

### CSS

Caso o jogador queira alterar a skin dos objetos, entra nesse modo em que é possível escolher qual objeto dejesa fazer a alteração

### NAVE

Se o jogador escolher mudar a skin da nave, ocorre esse modo em que uma tela com outras opções de skin para a nave irão aparecer, para selecionar, basta apertar o número correspondente e clicar em backspace para voltar

### MONSTER

Se o jogador escolhe mudar a skin do inimigo, esse modo é ativado e ele pode selecionar a skin escolhida dentre as opções, de forma análoga ao modo NAVE

### BALA

O mesmo ocorre para a bala, em que se esse modo for escolhido, o jogdador pode selecionar uma skin para a bala dentre as 

### GAMEOVER

Quando o jogador perde, ou seja, colide com o inimigo ou é atingido por uma bala deste, nesse modo pode-se pressionar a tecla "r" para reiniciar o jogo

### GAME

Modo em que o jogo acontece. Se ocorrer esre modo, ocorre o loop principal em que todos os eventos dentro do jogo são definidos
