# Desafio-Tunts.Rocks
Desafio técnico para o processo seletivo da Tunts.Rocks.

Programinha que lê a planilha no google docs e segue as seguintes regras:
Calcular a situação de cada aluno baseado na média das 3 provas (P1, P2 e P3): 

Média (m) Situação:
m<5  - Reprovado por Nota
5<=m<7  - Exame Final
m>=7  - Aprovado

Caso o número de faltas ultrapasse 25% do número total de aulas o aluno terá a situação  "Reprovado por Falta", independente da média.  Caso a situação seja "Exame Final" é necessário calcular a "Nota para Aprovação Final"(naf) de  cada aluno de acordo com seguinte fórmula: 

5 <= (m + naf)/2

Caso a situação do aluno seja diferente de "Exame Final", preencha o campo "Nota para  Aprovação Final" com 0. 
Arredondar o resultado para o próximo número inteiro (aumentar) caso necessário. Utilizar linhas de logs para acompanhamento das atividades da aplicação. 
Os textos do código fonte (atributos, classes, funções, comentários e afins) devem ser escritos  em inglês, salvo os identificadores e textos pré-definidos nesse desafio. 

Para rodar o código certifique de rodar esses comandos no terminal afim de instalar as bibliotecas necessárias:
pip install gspread
pip install oauth2client

Espero que aprovem :)
