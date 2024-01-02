# JSON Checker
- Pequena biblioteca para validação de JSONs.
- O método principal e único vai compar o JSON com um schema e retornar um booleano indicando se o JSON é válido ou não.
---
## Como usar
1. Para usar a biblioteca, basta importar o único método que ela possui, que é o `jsonChecker`. Seus únicos parâmetros são:
    - `json`: O JSON a ser validado.
    - `schema`: O schema a ser usado na validação.
    - `exact`: `opcional`: Se `True`, o JSON deve conter apenas as chaves do schema. Se `False`, o JSON pode conter chaves que não estão no schema.
---