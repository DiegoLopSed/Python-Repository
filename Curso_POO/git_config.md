## Configuración Inicial

1. **Configurar Nombre de Usuario y Correo Electrónico**
    
    ```bash
    git config --global user.name "Tu Nombre"
    git config --global user.email "tuemail@example.com"
    ```
    
    Estos datos se usarán para identificarte en los commits.
    
2. **Establecer el Editor Predeterminado**
    
    ```bash
    git config --global core.editor "nombre_del_editor"
    ```
    
    Ejemplos:
    
    - Para VS Code: `git config --global core.editor "code --wait"`
    - Para Vim: `git config --global core.editor "vim"`
3. **Configurar Colores en la Terminal**
    
    ```bash
    git config --global color.ui auto
    ```
    
    Habilita colores en la salida de comandos de Git para mejor legibilidad.
    
4. **Configurar la Rama Principal Predeterminada** Si deseas que tu rama principal se llame `main` en lugar de `master`:
    
    ```bash
    git config --global init.defaultBranch main
    ```
    
5. **Configurar el Final de Línea Automáticamente** Esto es útil si trabajas en proyectos con diferentes sistemas operativos.
    
    - En Windows:
        
        ```bash
        git config --global core.autocrlf true
        ```
        
    - En macOS/Linux:
        
        ```bash
        git config --global core.autocrlf input
        ```
        

## Verificación y Personalización

1. **Verificar Configuración** Lista todas las configuraciones actuales:
    
    ```bash
    git config --list
    ```
    
2. **Agregar Alias Ú tiles** Simplifica comandos largos con accesos rápidos:
    
    ```bash
    git config --global alias.st status
    git config --global alias.co checkout
    git config --global alias.br branch
    git config --global alias.cm commit
    ```
    
3. **Configurar el Rebase Interactivo para Pull** Si prefieres usar `rebase` en lugar de `merge` al hacer un pull:
    
    ```bash
    git config --global pull.rebase true
    ```
    

## Inicializar un Repositorio

1. **Crear un Repositorio** Cuando estés listo para trabajar en un proyecto:
    
    ```bash
    git init
    ```
    

## Trabajando con Staging

1. **Agregar Archivos al Área de Staging**
    
    - Para agregar un archivo específico:
        
        ```bash
        git add nombre_del_archivo
        ```
        
    - Para agregar todos los archivos en el directorio actual:
        
        ```bash
        git add .
        ```
        
2. **Verificar el Estado del Repositorio**
    
    - Muestra los archivos modificados, agregados y en staging:
        
        ```bash
        git status
        ```
        
3. **Confirmar los Cambios (Commit)**
    
    - Realiza un commit de los archivos en staging con un mensaje descriptivo:
        
        ```bash
        git commit -m "Mensaje del commit"
        ```

4. **Revisar el Historial de Commits**
    
    - Muestra los commits realizados:
        
        ```bash
        git log
        ```

## Corregir y Modificar Commits

1. **Modificar el Último Commit**
    
    - Si necesitas cambiar el mensaje del commit o agregar nuevos archivos:
        
        ```bash
        git commit --amend
        ```
        
    
    Esto abrirá el editor para modificar el mensaje del commit. Si ya tienes nuevos archivos en staging, estos se incluirán en el commit actualizado.
    
## Eliminar y Recuperar Archivos

1. **Eliminar un Archivo del Repositorio**
    
    - Para eliminar un archivo y registrar el cambio:
        
        ```bash
        git rm nombre_del_archivo
        ```

2. **Recuperar un Archivo Eliminado**
    
    - Si eliminaste un archivo y aún no hiciste commit:
        
        ```bash
        git restore nombre_del_archivo
        ```

## Trabajando con Ramas

1. **Crear una Nueva Rama**
    
    - Crea una nueva rama basada en la rama actual:
        
        ```
        git branch nombre_de_rama
        ```
        
2. **Cambiar a Otra Rama**
    
    - Cambia a una rama existente:
        
        ```
        git checkout nombre_de_rama
        ```
        
    - Con Git 2.23 o superior, usa:
        
        ```
        git switch nombre_de_rama
        ```
        
3. **Crear y Cambiar a una Nueva Rama**
    
    - Combina la creación y el cambio de rama:
        
        ```
        git checkout -b nombre_de_rama
        ```
        
    - Con Git 2.23 o superior, usa:
        
        ```
        git switch -c nombre_de_rama
        ```
        
4. **Listar Todas las Ramas**
    
    - Muestra todas las ramas locales:
        
        ```
        git branch
        ```
        
    - Muestra también las ramas remotas:
        
        ```
        git branch -a
        ```
        
5. **Eliminar una Rama**
    
    - Elimina una rama local:
        
        ```
        git branch -d nombre_de_rama
        ```
        
        Usa `-D` para forzar la eliminación si la rama no está completamente fusionada.
        
6. **Fusionar Ramas**
    
    - Fusiona una rama en la rama actual:
        
        ```
        git merge nombre_de_rama
        ```
