# Web Scraper con Clean Architecture en Python

Este proyecto es un **Web Scraper** desarrollado en Python siguiendo las mejores prácticas de **Clean Code** y **Clean Architecture**. Permite extraer el título de páginas web y almacenar los resultados en un archivo JSON.

## 📋 Tabla de Contenidos

-   [Características](#-características)
-   [Tecnologías](#-tecnologías)
-   [Instalación](#-instalación)
-   [Uso](#-uso)
-   [Estructura del Proyecto](#-estructura-del-proyecto)
-   [Pruebas Unitarias](#-pruebas-unitarias)
-   [Almacenamiento de Datos](#-almacenamiento-de-datos)
-   [Próximos Pasos](#-próximos-pasos)
-   [Contribuir](#-contribuir)
-   [Licencia](#-licencia)

## 🔹 Características

-   Arquitectura desacoplada (Clean Architecture)
-   Entidades, casos de uso e infraestructura claramente separados
-   Extracción de títulos de páginas web usando **requests** y **BeautifulSoup**
-   Almacenamiento en JSON mediante un repositorio genérico
-   Suite de pruebas unitarias con **pytest** para el caso de uso principal

## 🔹 Tecnologías

-   Python 3.13+
-   requests
-   beautifulsoup4
-   lxml
-   pytest

## 🔹 Instalación

1. Clona este repositorio:

    ```bash
    git clone <tu-repo-url> webscraper_clean
    cd webscraper_clean
    ```

2. Crea y activa un entorno virtual:

    - Linux/macOS:

        ```bash
        python -m venv venv
        source venv/bin/activate
        ```

    - Windows (PowerShell):

        ```powershell
        python -m venv venv
        venv\\Scripts\\activate
        ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## 🔹 Uso

Ejecuta el script principal para scrapear URLs y guardar los resultados en JSON:

```bash
python main.py
```

Por defecto, `main.py` procesa las URLs definidas en el arreglo interno y genera el archivo `scraped_pages.json`.

## 🔹 Estructura del Proyecto

```plaintext
webscraper_clean/
├── app/
│   ├── domain/                  # Entidades y contratos de repositorio
│   │   ├── page.py              # Clase Page
│   │   └── storage_repository.py# Interfaz StorageRepository
│   ├── use_cases/               # Casos de uso (logica de negocio)
│   │   ├── scrape_page.py       # PageScraper
│   │   └── scrape_and_store.py  # ScrapeAndStore
│   ├── infrastructure/          # Implementaciones concretas
│   │   ├── web/                 # Capa de scraping
│
│   │   │   └── bs_parser.py     # PageParser
│   │   └── storage/             # Persistencia
│   │       ├── __init__.py
│   │       └── json_storage.py  # JsonFileStorage
│   ├── interfaces/              # Puntos de entrada (CLI, APIs)
│   │   └── __init__.py
│   └── config.py                # Configuración global
├── tests/                       # Pruebas unitarias
│   ├── __init__.py
│   └── unit/
│       ├── __init__.py
│       └── test_scrape_page.py  # Test de PageScraper
├── main.py                      # Script de ejecución
├── requirements.txt             # Dependencias
└── README.md                    # Este archivo
```

## 🔹 Pruebas Unitarias

Ejecuta los tests con:

```bash
export PYTHONPATH=.
pytest -q
```

## 🔹 Almacenamiento de Datos

Los resultados se guardan en un archivo JSON (`scraped_pages.json`) a través de la implementación `JsonFileStorage`, que cumple la interfaz `StorageRepository`.

## 🔹 Contribuir

1. Haz un fork de este repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit de tus cambios (`git commit -m 'Añade nueva funcionalidad'`)
4. Push a tu rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 🔹 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
