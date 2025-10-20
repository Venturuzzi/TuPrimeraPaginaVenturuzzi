# Blog MVT (Django)

Proyecto de ejemplo para la consigna: **Django + patrón MVT**, **herencia de plantillas**, **3 modelos**, **formularios de alta** y **búsqueda**.

## Estructura
- App: `blog`
- Modelos: `Category`, `Author`, `Post` (relaciones: `Post` -> `Category` y `Author`)
- Formularios: ModelForm para cada modelo + `SearchForm` (GET)
- Vistas: home, listado de posts, crear autor/categoría/post, búsqueda
- Plantillas: heredan de `base.html`


## Cómo correr el proyecto
```bash
# 1) Crear y activar venv (opcional pero recomendado)
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/Mac: source .venv/bin/activate

# 2) Instalar dependencias
pip install -r requirements.txt

# 3) Migraciones
python manage.py migrate

# 4) (Opcional) Crear superusuario para admin
python manage.py createsuperuser

# 5) Levantar servidor
python manage.py runserver




