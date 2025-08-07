# 📄 CHANGELOG – Sistema de Gestión de Consultas Psicológicas Infantiles

## [Sprint 0] - Inicio del proyecto  
**Fecha de cierre:** 15 de julio de 2025

### Añadido
- Configuración inicial del proyecto Django.
- Creación del repositorio en GitHub: [https://github.com/fgmonk/sistema_psicologas](https://github.com/fgmonk/sistema_psicologas).
- Definición de estructura base del proyecto (apps, entorno virtual, configuración inicial).
- Diseño de arquitectura del sistema: modelo de vistas 4+1, patrón MTV.
- Definición de usuarios clave del sistema: `felipegonzalezmat@gmail.com` y `mane.rosati@gmail.com`.

### Documentación
- Entrega de planificación inicial, backlog del producto y cronograma de iteraciones.
- Primer borrador de diagrama de clases y modelo de datos MVP.

---

## [Sprint 1] - Módulo Ficha de Pacientes  
**Fecha de cierre:** 29 de julio de 2025

### Añadido
- Módulo **Pacientes**:
  - Registro de pacientes con datos personales y datos del apoderado.
  - Edición y eliminación de registros de pacientes.
  - Búsqueda por RUT o nombre desde el listado.

- Estructura de la ficha clínica:
  - Visualización del historial del paciente.
  - Acceso desde la ficha a sesiones, informes y datos personales.

### Mejoras
- Asignación del RUT como identificador único de cada paciente.
- Integración con las vistas administrativas de Django Admin para gestión básica.

### Documentación
- Diseño final del modelo Paciente y su implementación en `models.py`.
- Capturas de interfaz para la ficha y listado de pacientes.
- Evidencia de pruebas unitarias en la creación y edición de pacientes.
- Actualización del diagrama de clases.

---

## [Sprint 2] - Módulo de Informes  
**Fecha de cierre:** 5 de agosto de 2025

### Añadido
- Módulo **Informes**:
  - Creación de informe tipo 1 (para colegio), tipo 2 (para familia) y tipo 3 (en blanco).
  - Asociación de informe a paciente mediante FK.
  - Campo de contenido editable para escribir el informe directamente desde el sistema.

- Exportación de informes:
  - Descarga en formato PDF y Word (.docx).
  - Vista previa del informe generado.

### Mejoras
- Integración de informes con la ficha del paciente.
- Validación automática del tipo de informe seleccionado.
- Agregado de fecha automática de generación.

### Documentación
- Diagrama de clases actualizado incluyendo la relación Paciente–Informe.
- Capturas del flujo de creación de informe y su visualización.
- Evidencia de trazabilidad entre requerimientos funcionales e implementación en `models.py` y `views.py`.
- Release note consolidado para documentación formal.
