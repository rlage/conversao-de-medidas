## 1 - Conversão de medidas

Você terá que criar um sistema que **formate a saída** de uma **dada entrada** para as três unidades de dados: **tempo, bytes e porcentagem**.

### Regras para formatação

#### Tempo

A entrada provida deve ser no formato `<numero> <ms>`, ex: `1340 ms`. A unidade usada para entrada será milisegundo.
* Quando a entrada for menor que 1 segundo a saída deve continuar em milisegundos `ms`.
* Quando a entrada for menor que 60 segundos a saída deve ser em segundos `s`.
* Quando a entrada for menor que 60 minutos a saída deve ser em minutos `min`.
* Quando a entrada for maior ou igual a 60 minutos a saída deve ser em horas `h`.

#### *Bytes*

A entrada provida deve ser no formato `<numero> <bytes>`, ex: `16 B`. A unidade usada para entrada será bytes (8 bits).
* Quando a entrada for menor que 1000 bytes a saída deve continuar em `B`.
* Quando a entrada for menor que 1000 elevado a 2 a saída deve ser em kilobyte `kB`.
* Quando a entrada for maior ou igual a 1000 elevado a 2 a saída deve ser em megabyte `MB`.

#### Porcentagem

A entrada provida deve ser no formato `<numero flutuante>`, ex: `0.16`. A unidade usada para entrada será um número flutuante onde, por exemplo, `0.1` significa `10%` e `0.98` significa `98%`.

### Exemplos de entradas e saídas esperadas pelo seu programa

| Entrada | Saída |
| ------ | ------ |
| 30 ms | `30 ms` |
| 5000 ms | `5 s` |
| 5400000 ms | `1.5 h` |
| 0.14 | `14%` |
| 50 B | `50 B` |
| 2000 B | `2 kB` |
