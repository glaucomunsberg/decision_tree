
#### Dataset
 
 Our hint is that the information does not result in a good decision tree. By the way
   we will assemble eighteen fields and change to boolean two fields 
   (has PhD course and is academic modality).Only the area and level (pure field) of each course be used directly. See the fields generate bellow 
   
   years_open      | FLOAT = 2016 - Inicio Mestrado # used by the fields bellow
   diss_doce_year  | FLOAT = (Dissertacoes/Docentes)/years_open
   tese_doce_year  | FLOAT = (Teses/Docentes)/years_open
   peri_doce_year  | FLOAT = (TotalPeriodos/Docentes)/years_open
   weight_a1       | FLOAT = TotalA1*weight(A1)
   weight_a2       | FLOAT = TotalA2*weight(A2)
   weight_b1       | FLOAT = TotalB1*weight(B1)
   weight_b2       | FLOAT = TotalB2*weight(B2)
   weight_b3       | FLOAT = TotalB3*weight(B3)
   weight_b4       | FLOAT = TotalB4*weight(B4)
   weight_b5       | FLOAT = TotalB5*weight(B5)
   weight_c        | FLOAT = TotalC *weight(C)
   weight_nc       | FLOAT = TotalNC*weight(NC)
   qual_doce_year  | FLOAT = (TotalQualificados/Docentes)/years_open
   conf_doce_year  | FLOAT = (Conferencias/Docentes)/years_open
   livr_doce_year  | FLOAT = (Livros/Docentes)/years_open
   capi_doce_year  | FLOAT = (Capitulos/Docentes)/years_open
   arti_doce_year  | FLOAT = (Prod.Artistica/Docentes)/years_open
   has_phd         | BOOL  = Exist PhD courses?
   is_academic     | BOOL  = academica?
   
   
#### Results 

 Area CAPES              | Level expected  | ID3 labeled  | C45 labeled  | C45 (pruning) labeled  
------------------------ | --------------- | ------------ | ------------ | ----------------------
artes_musica             |      tres       |     tres     |     tres     |     tres
admin_ciencontabeis_tur  |      cinco      |     seis     |     cinco    |     cinco
antropologia_arqueologia |      sete       |     cinco    |       -      |       -
arquitetura_urbanismo    |      quatro     |     tres     |     tres     |     tres
biologicas_i             |      cinco      |     cinco    |     quatro   |     quatro
biologicas_ii            |      quatro     |       -      |       -      |       -
biologicas_iii           |      quatro     |     tres     |     quatro   |     quatro
biotecnologia            |      quatro     |     quatro   |     quatro   |     quatro
cienagrarias_i           |      seis       |       -      |     cinco    |     cinco
ciencia_alimentos        |      tres       |     tres     |     tres     |     tres
computacao               |      quatro     |       -      |     quatro   |     quatro
ecologia                 |      cinco      |       -      |     cinco    |     cinco
educacao_fisica          |      quatro     |       -      |     sete     |     sete
engenharias_i            |      cinco      |       -      |     cinco    |     cinco
engenharias_ii           |      seis       |     cinco    |     sete     |     sete
engenharias_iii          |      tres       |     tres     |     tres     |     tres
engenharias_iv           |      sete       |     sete     |     seis     |     seis
geociencias              |      seis       |       -      |     seis     |     seis
geografia                |      tres       |     quatro   |     quatro   |     quatro
mat_prob_estatistica     |      tres       |     tres     |       -      |       -
letras_linguistica       |      quatro     |       -      |       -      |       -
medicina_veterinaria     |      seis       |     seis     |       -      |       -
odontologia              |      quatro     |     cinco    |     cinco    |     cinco
sociologia               |      quatro     |     tres     |     quatro   |     quatro



## Weight of each Qualis

 The weight of each qualis and publication qualified has.
 
 A1 -> 0.9
 A2 -> 0.75
 B1 -> 0.6
 B2 -> 0.45
 B3 -> 0.3
 B4 -> 0.25
 B5 -> 0.1
 C  -> 0.07
 NC -> 0.01
 
## Course birthday

 The Brazilian's academic productions were an increase after the year 1996, for this reason we decide to put the ceiling 20 year of any course with more that this.
 
 
#### Fields on original file

Area - Área de avaliação
Instituicao	- Instuição do Programa
Modalidade - Se trata-se de Mestrado Acadêmico ou Mestrado Profissional
Inicio Doutorado - Ano de início do doutorado (se houver)
Inicio Mestrado - Ano de início do mestrado
Docentes - Número de docentes no Programa
Dissertacoes - Número de dissertações defendidas
Teses - Número de teses defendidas
Di/Te - Razão entre número de dissertações e teses defendidas
TotalPeriodicos - Número total de artigos publicados em periódicos
TotalQualificados - Número total de artigos publicados em periódicos qualificados (com Qualis)
A1	- Número de artigos publicados em periódicos com Qualis A1
A2	- Número de artigos publicados em periódicos com Qualis A2
B1	- Número de artigos publicados em periódicos com Qualis B1
B2	- Número de artigos publicados em periódicos com Qualis B2
B3	- Número de artigos publicados em periódicos com Qualis B3
B4	- Número de artigos publicados em periódicos com Qualis B4
B5	- Número de artigos publicados em periódicos com Qualis B5
C 	- Número de artigos publicados em periódicos com Qualis C
NC	- Número de artigos publicados em periódicos sem Qualis
Capitulos - Número de capítulos de livros publicados
Coletaneas - Número de coletâneas publicadas
Conferencias - Número de artigos publicados em conferências
Livros - Número de livros publicados
Outros - Número de outras publicações
Prod.Artistica - Número de produções artísticas
Conceito - Conceito da CAPES para o Programa

#### Examples.csv
The file contains a subset (not included at training.csv) to verify the decision tree. The examples.csv contain one course (capes program) by area