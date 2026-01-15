# Sistema de Gestión para Psicólogas Integrales (SGPI) 🧠

Este proyecto fue desarrollado como parte del **Proyecto de Título**.

Es una aplicación web completa basada en **Django** diseñada para optimizar la gestión administrativa y clínica de profesionales de la salud mental, permitiendo llevar un control ordenado de pacientes, sesiones, informes y cobranza.

## 🚀 Características Principales

*   **Gestión de Pacientes**: Fichas clínicas digitales con datos personales, demográficos y antecedentes.
*   **Validación Local**: Implementación de algoritmos para validación estricta de **RUT Chileno** (Rol Único Tributario).
*   **Módulo de Sesiones**: Registro histórico de cada sesión realizada.
*   **Control Financiero**: Módulo de cobranza para seguimiento de pagos y deudas.
*   **Informes**: Generación de reportes de evolución del paciente.

## 🛠️ Stack Tecnológico

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

*   **Backend**: Python 3.10 + Django 5.2
*   **Base de Datos**: SQLite (Entorno Desarrollo) / PostgreSQL (Compatible Producción)
*   **Frontend**: HTML5, CSS3, Django Templates

## 📋 Requisitos Previos

*   Python 3.8 o superior
*   pip (Gestor de paquetes de Python)

## 🔧 Instalación y Ejecución

1.  **Clonar el repositorio**:
    ```bash
    git clone https://github.com/fgmonk/sistema_psicologas.git
    cd sistema_psicologas
    ```

2.  **Crear entorno virtual** (Recomendado):
    ```bash
    python -m venv venv
    # En Windows:
    .\venv\Scripts\activate
    # En Mac/Linux:
    source venv/bin/activate
    ```

3.  **Instalar dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplicar migraciones**:
    ```bash
    python manage.py migrate
    ```

5.  **Ejecutar servidor**:
    ```bash
    python manage.py runserver
    ```
    Visita `http://127.0.0.1:8000/` en tu navegador.

## 👤 Autor

*   GitHub: [@fgmonk](https://github.com/fgmonk)


---
*Proyecto desarrollado con fines académicos y de portafolio.*
