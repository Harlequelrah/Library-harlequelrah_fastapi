# Description

Passioné par la programmation et le développement avec python je me lance dans la création progressive d'une bibliothèque personnalisée pour m'ameliorer , devenir plus productif et partager mon expertise avec `FASTAPI`

# Logo
![Logo](https://github.com/Harlequelrah/Library-harlequelrah_fastapi/blob/main/harlequelrah.png)

## Installation

- **Avec Github :**
   ```bash
   git clone https://github.com/Harlequelrah/Library-harlequelrah_fastapi
   ```
- **Avec pip :**
   ```bash
   pip install harlequelrah_fastapi
   ```

## Utilisation
Ce package contient plusieurs modules utiles pour accélérer et modulariser le dévéloppement avec FASTAPI. Voici un aperçu de leurs fonctionnalités.

### `Commandes`

#### 1. Commande de création du projet
Cette commande permet de générer un projet FASTAPI avec une archictecture définie

 ```bash

   harlequelrah_fastapi startproject nomduprojet
 ```
 **`architecture`:**
```
nomduprojet/
├── __init__.py
├── .gitignore
├── alembic.ini
├── env/
├── nomduprojet/
│   ├── __init__.py
│   ├── __main__.py
│   ├── alembic/
│   ├── settings/
│       ├── .gitignore
│       ├── __init__.py
│       ├── requirements.txt
│       ├── database.py
│       ├── secret.py
│       └── models_metadata.py
```

#### 2. Commande de génération d'une application
Cette commande permet de créer une application dans le projet
```bash
  harlequelrah_fastapi startapp nomappli
```
**`architecture`:**
```
sqlapp/
├── __init__.py
├── crud.py
├── model.py
├── route.py
├── schema.py
├── util.py
```
#### 3. Commande génération d'une application utilisateur
Cette commande permet de créer une application utilisateur

**`architecture`:**
```
userapp/
├── __init__.py
├── app_user.py
├── user_model.py
├── user_crud.py
```

#### 4. Commande de génération d'une application de log
Cette commande permet de créer une application de log

**`architecture`:**
```
loggerapp/
├── __init__.py
├── log_user.py
├── log_model.py
├── log_crud.py
├── log_schema.py
```
### `Modules`
####  Module `exception`
Ce module contient des exceptions personnalisées utilisés dans cette bibliothèque
##### 1. Sous module auth_exception
ce sous module dispose de quelques variables d'exceptions prédéfinies liés à l'authentification

- `AUTHENTICATION_EXCEPTION` : exception personnalisée à léver lorsqu'une erreur d'authentification se produit

##### 2. Sous module custom_http_exception
- `**CustomHttpException**` : génère une exception personnalisé qui definit une exception de type HTTPExeption.
```python
  from fastapi import HTTPException , status
  from harlequelrah_fastapi.exception.custom_http_exception import CustomHttpException
  http_exception= HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="La requête a provoquée une exception non gérée")
  raise CustomHttpException(http_exception)
```
#### Module `utility`
Ce module contient des utilitaires utilisés dans cette bibliothèque.
- `update_entity` : mets à jour les champs d'une entité objet
  - paramètres : `existing_entity` , `update_entity`
  - retourne : `existing_entity`
  - utilisation :
  ```python
  from harlequelrah_fastapi.utility.utils import update_entity
  existing_entity = {"id": 1, "name": "John"}
  update_entity = {"id":1 , "name" : "Johnson"}
  existing_entity=update_entity(existing_entity,update_entity)
  ```

#### Module `authentication`
Ce module contient des classes et des fonctions utilisées pour l'authentification.

##### 1. Sous module `token`
Ce sous module définit des classes pydantics pour la gestions des tokens :
- AccessToken : access_token : **str** , token_type : **str**
- RefreshToken : refresh_token : **str** , token_type : **str**
- Token : access_token : **str** ,refresh_token : **str** , token_type : **str**

##### 2. Sous module `authenticate`
ce sous module définit les classes et fonctions utilisées pour l'authentification

- **`Classe Authentication`**:classe principale pour gérer l'authentification
- `oauth2_scheme` : définit le schéma d'authentication
- `User` : le modèle d'utilisateur SQLAlchemy
- `UserCreateModel` : le modèle pydantic pour la création d'utilisateur
- `UserUpdateModel` : le modèle pydantic pour la mise à jour d'utilisateur
- `UserPydanticModel` : le modèle pydantic pour lire un utilisateur
- `UserLoginModel` : le modèle pydantic la connexion d'utilisateur
- `SECRET_KEY` : une clé secrète générer par défaut
- `ALGORITHM` : un algorithm par défaut `HS256`
- `REFRESH_TOKEN_EXPIRE_DAYS` : **int**
- `ACCESS_TOKEN_EXPIRE_MINUTES` : **int**
- `session_factory` : un générateur de session
- `CREDENTIALS_EXCEPTION` : une exception de type `CustomHttpException` à lever lorsque l'authentification échoue


# Contact ou Support
Pour des questions ou du support, contactez-moi à maximeatsoudegbovi@gmail.com ou au (+228) 91 36 10 29.
