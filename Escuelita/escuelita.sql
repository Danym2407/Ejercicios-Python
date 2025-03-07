CREATE TABLE alumnos(
matricula INTEGER PRIMARY KEY AUTOINCREMENT
,nombre VARCHAR(100) NOT NULL
,apellido_paterno VARCHAR(100) NOT NULL
,apellido_materno VARCHAR(100)
,fecha_nacimiento DATE
,sexo CHAR);

CREATE TABLE materias(
clave CHAR(5) PRIMARY KEY
,nombre VARCHAR(100)
,creditos	 INT DEFAULT 10);

CREATE TABLE calificaciones(
alumno INT
,materia CHAR(5)
,calificacion FLOAT 
,fecha DATE  
,PRIMARY KEY (alumno, materia)
,FOREIGN KEY (alumno) REFERENCES alumnos(matricula)
,FOREIGN KEY (materia) REFERENCES materias(clave));