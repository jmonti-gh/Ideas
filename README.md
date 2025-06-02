# Ideas
- List and maximum possible detail of completed and pending projects

## 1.- Own Package
- Fully proprietary library (package) with modules containing interesting utilities for JM
- jm_utils with tons of modules
- More detail in particular subdir

### 1.1- Own Package - passmgrcore
- Core for managing encrypted credentials with pandas
- imports jm.passmgrcore as pmc

### 1.2.- List
jm_datetime: casos como calc ultimo día del mes, ultimo día del mes del año anterior, años bicistos, cantidad de días de un dado año... etc.
jm_pdaccessor.py: comp_df, filter_row, etc... (pd - methods extension)
jm_baseutils: 
jm_nputils: nump
jm_statistics: 
jm_datascience: acá podemos poner mucho de numpy, pandas, matplotlib, seaborn, scikit lern, tensorflow o pero NO, mejor manejarlo por separado
--> statistics, y ds me puede ayudar a maejar funciones qu utilicen varios modulos, sino ..veremos - Hay que EVITAR llamadas circulares
jm_databases: lo relacionado con inspect_db, etc... pyodbc SQLalchemy, - SQLite?

- Crear el jm_utils y prepararlo para pypi.org
https://pytutorial.com/creating-python-modules-and-packages-guide/

## 2.- Inspect DB - TO-DO
- Basically, inspect unknown DBs
- There's NOTHING to it, so the proposed approach will be restructured: known DB, known table, search field, etc.

### 2.1- Inspect DB - known table
- Inspect the structure (schema) of a table to find out what fields it has and what they represent.

### 2.2 Inspect DB - Search Field
- Search for a field knowing only the field name in a completely unknown DB.

## 3.- Queries to CSV

## 4.- Passwer Manager with pandas
- Use jm_passmgrcore module

## 5.- Programita que cambie los nombres de archivos con sufijo y/prefijo de todos los archivos de una carpeta
- podría también ser que archivos que empiecen con... no todos sino con algún filtro..
- surgió de renombrar los de fgrrica ovn sfiix _xls.CSV
- y que contemple elegir todo el árbol pá abajo (recursivo) o NO !?
