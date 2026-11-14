# Taller 2: Calculadora con pipeline de CI

## Integrantes

Quinnie Villarreal | Lina Ballesteros | Alejandro Rios

| Nombre completo | Usuario de GitHub | Rol |
| --- | --- | --- |
| Quinnie Villarreal | quinnie9 | Propietaria del repositorio |
| Lina Ballesteros | Pendiente | Integrante |
| Alejandro Rios | Pendiente | Integrante |

## Correcciones de seguridad

- Docker y CI instalan dependencias desde `requirements.lock` y
  `requirements-dev.lock`, con versiones transitivas fijadas, hashes SHA-256
  y distribuciones binarias. Los archivos `.txt` mantienen las dependencias
  directas del taller; los `.lock` se regeneran con `pip-compile --generate-hashes`.
- Las acciones de SonarCloud y Docker Hub están fijadas por su commit completo.
- Gunicorn corre como el usuario sin privilegios `calculadora`.
- Flask-WTF valida CSRF en los POST. Las pruebas obtienen un token real del
  formulario; también comprueban rechazo de tokens ausentes, alterados y ajenos.
- `SECRET_KEY` puede proporcionarse por variable de entorno. Si no se configura,
  se genera una clave aleatoria al arrancar; `gunicorn --preload` permite que los
  cuatro workers compartan esa clave. Reiniciar invalida las sesiones anteriores.
  Para mantener sesiones entre reinicios o varias réplicas se debe configurar
  una misma `SECRET_KEY` mediante el gestor de secretos del despliegue.

## Evidencias del trabajo en equipo

- URL del Pull Request de la sección 9: pendiente.
- URL de la ejecución fallida por el error intencional: pendiente.

## Respuestas

Pendientes de completar por el equipo en la sección 10.1 del taller.
