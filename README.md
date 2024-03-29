# [JSON Simple Manager](https://pypi.org/project/json-simple-manager/)
- Pequena biblioteca para validação e manipulação de JSONs.
---
## Instalação
- Você pode baixar pelo pip:
```
pip install json-simple-manager
```
- Ou pelo próprio repositório:
```
git clone git@github.com:Hoyasumii/JsonSimpleManager.git
```
- ou pelos submódulos do git:
```
git submodule add git@github.com:Hoyasumii/JsonSimpleManager.git
```
- Caso queira colocar o submódulo em uma pasta específica, basta adicionar o nome da pasta após o link do repositório.
---
## Métodos disponíveis
### `checker` -> `dict`
- Retorna um dicionário com as chaves que estão: `Faltando`, `Com valor errado` e `Chaves extras`.
- Parâmetros:
    - `json`: O JSON a ser validado.
    - `schema`: O schema a ser usado na validação.
### `dropKey` -> `bool`
- Retorna `True` se a chave foi removida com sucesso, `False` caso contrário.
- Parâmetros:
    - `json`: O JSON a ser manipulado.
    - `key`: A chave a ser removida.
### `get` -> `dict`
- Retorna o `dicionário` do **JSON**.
- Parâmetros:
    - `json`: O JSON a ser manipulado.
### `update` -> `bool`
- Retorna `True` se o **JSON** foi atualizado com sucesso, `False` caso contrário.
- Parâmetros:
    - `json`: O JSON a ser manipulado.
    - `key`: A chave a ser atualizada.
    - `value`: O valor a ser atualizado.
---
- [**Link do repositório**](https://github.com/Hoyasumii/JsonSimpleManager)