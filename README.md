# EFIAerolíneas ✈️

Proyecto web en Django que simula el sistema de gestión para una aerolínea. Permite administrar vuelos, reservas, boletos, pasajeros, aviones y usuarios. Además, incluye funcionalidades de autenticación como login, registro y logout.

## Estructura del Proyecto

Este proyecto contiene dos aplicaciones principales:

### 1. `aerolinea/`

Encargada de la lógica del negocio y manejo de datos principales de la aerolínea:

- **Modelos:**
  - `Avion`: Modelo de aeronaves con capacidad, filas y columnas.
  - `Vuelo`: Define vuelos con origen, destino, fechas y avión asignado.
  - `Asiento`: Define los asientos disponibles en cada avión.
  - `Pasajero`: Información personal del pasajero.
  - `Reserva`: Enlaza pasajero, vuelo y asiento. Maneja estados.
  - `Boleto`: Asociado a una reserva confirmada.
  - `Usuario`: (Modelo adicional para gestión interna de roles, aunque Django ya provee uno por defecto).

- **Formularios:**
  - Formularios personalizados para cada modelo con estilos e inputs HTML personalizados.

- **Vistas:**
  - CRUD completo para todas las entidades.
  - Vista de historial de reservas por pasajero.
  - Lista de pasajeros por vuelo.
  - Manejo de estado del asiento al crear o eliminar reservas (con señales).

- **Señales:**
  - Cambian automáticamente el estado del asiento al crear o eliminar una reserva (`ocupado`/`disponible`).

- **Admin:**
  - Panel de administración con filtros, búsquedas y visualización personalizada para cada modelo.

---

### 2. `home/`

Contiene la parte de autenticación de usuarios y vista principal del sitio:

- **Funcionalidades:**
  - `login` de usuarios existentes.
  - `registro` de nuevos usuarios con validación de contraseñas, usuario y email únicos.
  - `logout` para cerrar sesión.
  - Página de inicio (`index.html`).
  - Base HTML común para heredar (`base.html`).

- **Formularios:**
  - `RegisterForm` y `LoginForm`, con validaciones manuales y estilos.

- **Vistas:**
  - Manejo de sesiones (`LoginView`, `LogoutView`).
  - Registro de usuarios con envío de correo electrónico de bienvenida.
  - Vista principal con `HomeView`.

- **Internacionalización (i18n):**

    - El proyecto soporta traducciones multilenguaje utilizando los archivos .po y .mo ubicados en la carpeta locale/.

    - Las traducciones están disponibles para los idiomas Español (es) e Inglés (en).

    - Se utiliza gettext_lazy en los modelos, formularios y vistas para permitir la traducción dinámica de los textos.

    - Django selecciona automáticamente el idioma en base a la configuración del navegador o del archivo settings.py, pero también se puede modificar manualmente usando activate() y deactivate() desde django.utils.translation.

## Requisitos del Proyecto

- asgiref==3.8.1
- asttokens==3.0.0
- decorator==5.2.1
- Django==5.2.3
- django-simple-history==3.10.1
- executing==2.2.0
- ipython==9.3.0
- ipython_pygments_lexers==1.1.1
- jedi==0.19.2
- matplotlib-inline==0.1.7
- parso==0.8.4
- pexpect==4.9.0
- prompt_toolkit==3.0.51
- ptyprocess==0.7.0
- pure_eval==0.2.3
- Pygments==2.19.2
- sqlparse==0.5.3
- stack-data==0.6.3
- traitlets==5.14.3
- wcwidth==0.2.13

---

## Instalación

```bash
git clone https://github.com/tuusuario/efiaerolineas.git
cd efiaerolineas
python3 -m venv .env
source venv/bin/activate
pip install -r requirements.txt
cd efi2025
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
