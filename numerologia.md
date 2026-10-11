# Numerologia de sakal-y-pinatalin

Camada opcional sobre a língua. Dá a cada forma um número pela numerologia pitagórica e deixa o pedido mirar um dos significados. Não altera a gramática: `sakal-y-pinatalin.md` continua a única fonte das formas, e uma forma errada não vira certa por acertar o número. A implementação de referência está em `numero.py`.

## 1. Valor das letras

A língua usa treze letras. Pela tabela pitagórica (a=1 … i=9, j=1 … r=9, s=1 … z=8):

| letra | `a` | `i` | `u` | `y` | `h` | `p` | `t` | `k` | `m` | `n` | `l` | `r` | `s` |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| valor | 1 | 9 | 3 | 7 | 8 | 7 | 2 | 2 | 4 | 5 | 3 | 9 | 1 |

Espaço e hífen valem zero. O `y` é vogal (seção 1 da especificação), sem a ambiguidade que tem em português.

## 2. Três eixos

| eixo | soma | lê |
| --- | --- | --- |
| expressão | todas as letras | o que a forma é para fora. Eixo padrão. |
| alma | vogais `a i u y` | o que a forma quer |
| personalidade | consoantes | como a forma aparece |

## 3. Redução

Some todas as letras da forma inteira e só depois reduza. Reduzir é somar os algarismos, e repetir até sobrar um número de 1 a 9 ou um número mestre: 11, 22 ou 33. O mestre não se reduz. A cadeia se mostra inteira: `57 → 12 → 3`.

**Domínio.** Cada domínio (raiz ou nome simples, seção 1 da especificação) tem um número próprio, calculado do mesmo jeito sobre as suas letras. Palavras gramaticais e o `y` da solda entram no total, mas não são domínios. O número do domínio é leitura, no mesmo eixo pedido, e o alvo mira sempre o total. Não se somam reduções.

`sakal-y-pinatalin`: `sakal` 8, `y` 7, `pinatalin` 42 → 6. Total 57 → 12 → 3.

**Zero.** Uma forma sem vogais ou sem consoantes soma zero nesse eixo. Zero não tem número e não entra na tabela: a personalidade de `i` é zero.

**Raridade.** Vale o laço, não uma lista de somas. Como o mestre é preservado, 29, 38 e 47 param em 11 e não descem a 2. O 2 sai quando a cadeia passa por 20 ou por outro número sem mestre no caminho: 389 → 20 → 2, 992 → 20 → 2, 1199 → 20 → 2. Os mestres saem também de somas grandes: 499 → 22, 994 → 22, 6999 → 33. O 2, o 22 e o 33 falham com frequência, e isso é a regra, não um defeito.

## 4. Significados

A glosa na língua é a raiz em cuja definição o significado cabe. É alcunha: não muda o léxico, não entra na tabela canônica nem na seção 3 da especificação, e não entra na tradução. Onde nenhuma raiz serve, a glosa fica vazia. A primeira coluna de significado é a que `numero.py` imprime.

| nº | significado | sombra | glosa |
| --- | --- | --- | --- |
| 1 | início, individualidade, iniciativa | isolamento, imposição | `tamis`, início |
| 2 | acordo, cooperação, parceria | dependência, indecisão | `sumal`, acordo |
| 3 | comunicação, criatividade, alegria | dispersão, superficialidade | `lanin`, fala |
| 4 | estabilidade, trabalho, ordem, fundação | rigidez | |
| 5 | liberdade, movimento, mudança | inquietação, excesso | `til`, ir |
| 6 | cuidado, responsabilidade, lar | controle, sacrifício cobrado | `manil`, cuidar |
| 7 | introspecção, busca, análise | reclusão, desconfiança | `mulin`, pensar |
| 8 | poder, realização, posse | ganância, dureza | `tanis`, ter |
| 9 | conclusão, completude, compaixão | perda, desapego forçado | `nukal`, termo |
| 11 | iluminação, intuição, inspiração (mestre do 2) | tensão nervosa | `lis`, luz |
| 22 | grande obra, o que fica construído (mestre do 4) | peso da tarefa | `kan`, abrigo |
| 33 | serviço a muitos, ensino (mestre do 6) | martírio | `manil-malan`, cuidar, muitos |

## 5. Tradução com alvo

O pedido pode dizer um número (ou um significado da tabela, que se converte no número) e, se quiser, um eixo. Sem eixo, vale a expressão.

**A gramática vence o número.** O alvo só escolhe entre o que o pedido deixou em aberto, e nunca inventa compromisso. Compostos, a tabela canônica e o procedimento da seção 3 da especificação nunca se mexem por causa do número: o número não escolhe entre compostos. A busca segue uma ordem fixa, para que dois falantes cheguem à mesma forma. O primeiro candidato que acerta vence.

- **Nome próprio.** Uma semente dá um nome simples. Duas dão um cindido, como na seção 5 da especificação, e não são alternativas. Primeiro a semente como veio. Depois a **afinação**: a primeira semente, na ordem em que veio, seguida de `1`, `2` … `99`, com o nome gerado e, no cindido, soldado de novo (`farol` → `farol1` → `farol2` …). O número também é semente livre: os dígitos viram letras pelo passo 2 da seção 5 da especificação. O teto é 99. Declare a semente que venceu.
- **Frase, alvo.** O alvo dito pelo usuário nunca se mexe. Dito inclui inscrição (`hu`), pensamento (`su`), para muitos (`mu`) e para ti (`pu`). Se o alvo foi calado, ele sai do número, na ordem da seção 2: `pu mu hu su`. Na pergunta, `pu mu su`. Pergunta com `hu` não existe e não escorrega para `pu`. Sem número, o alvo calado fica no juízo declarado, como antes.
- **Frase, modo.** O modo não é alavanca, porque mudar o modo inventa compromisso ou fonte. `i` fica `i`. A única abertura é o endosso sem fonte: se o pedido endossa sem dizer como sabe, a fonte varia por dentro do alvo, na ordem `ka la na`. `ta`, `u`, `sa` e `ma` nunca são alavanca. Na pergunta, o modo é o alvo repetido.
- **Título e composto nu.** Não há alavanca. Calcule o número e diga se acertou.

Nenhuma palavra de conteúdo se acrescenta ou se tira por causa do número.

**Sem acerto, avise.** Entregue a forma sem afinação, ou a primeira da ordem de alvos com o modo já fechado, o número que ela dá e a frase "o alvo N não é alcançável aqui". Nunca force. Acerto com forma ilegal não vale.

## 6. Achados

Os dois autores caem em números mestre: `kaluk` (Grok) dá 11 e `kalatupin` (Claude) dá 33. O nome da língua tem expressão 3 (comunicação) e alma 11.
