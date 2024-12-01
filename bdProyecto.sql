CREATE TABLE Propietarios (
	DNI_pr	varchar(8) PRIMARY KEY,
	Nombre_pr varchar(30),
	Apellido_pr varchar(30),
	Correo_pr varchar(50),
	Telefono_pr	varchar(15)
);

CREATE TABLE Mascotas (
	Codigo_ma INTEGER  PRIMARY KEY AUTOINCREMENT,
	DNIporietario_ma varchar(8),
	raza_ma	varchar(30),
	Genero	varchar(1),
	FechaNacimiento_ma	date,
	
	FOREIGN KEY(DNIporietario_ma) REFERENCES Propietarios(DNI_pr)
	

);

CREATE TABLE Empleados (
	

legajoEmpleado_em varchar(3),
IdPracticaMedica_em INTEGER,
DNIempleado_em	varchar(8) UNIQUE,
	Nombre_em varchar(30),
	Apellido_em varchar(30),
	Correo_em varchar(50),
	Telefono_em	varchar(15),
	
 PRIMARY KEY (legajoEmpleado_em),
 	FOREIGN KEY(IdPracticaMedica_em) REFERENCES PracticaMedica(IdPracticaMe_pra)

);
CREATE TABLE AtencionMedica (
	IdAtencion_at INTEGER   PRIMARY KEY AUTOINCREMENT,
CodigoMascota_at INTEGER,
legajoEmpleado_at varchar(3),

	FOREIGN KEY(CodigoMascota_at) REFERENCES Mascotas(Codigo_ma),
	FOREIGN KEY(legajoEmpleado_at) REFERENCES Empleados(legajoEmpleado_em)

);

CREATE TABLE PracticaMedica (
	

IdPracticaMe_pra INTEGER  PRIMARY KEY AUTOINCREMENT,
decripcion_pra varchar(50)


);
