CREATE TABLE status (
	id_status SERIAL NOT NULL,
	PRIMARY KEY(id_status),
	titulo_status VARCHAR NOT NULL
);

CREATE TABLE carregador (
	id_carregador SERIAL NOT NULL,
	PRIMARY KEY(id_carregador),
	matricula_caregador VARCHAR(5) NOT NULL,
	id_status INTEGER NOT NULL,
	FOREIGN KEY(id_status) REFERENCES status(id_status)
);

CREATE TABLE categoria (
	id_categoria SERIAL NOT NULL,
	PRIMARY KEY(id_categoria),
	titulo_categoria VARCHAR NOT NULL
);

CREATE TABLE equipamento (
	id_equipamento SERIAL NOT NULL,
	PRIMARY KEY(id_equipamento),
	numero_de_serie_equipamento VARCHAR(15) NOT NULL,
	matricula_equipamento VARCHAR(5) NOT NULL,
	id_categoria INTEGER NOT NULL,
	FOREIGN KEY(id_categoria) REFERENCES categoria(id_categoria),
	id_status INTEGER NOT NULL,
	FOREIGN KEY(id_status) REFERENCES status(id_status),
	id_carregador INTEGER NOT NULL,
	FOREIGN KEY(id_carregador) REFERENCES carregador(id_carregador)
);

CREATE TABLE aluno (
	id_aluno SERIAL NOT NULL,
	PRIMARY KEY(id_aluno),
	nome_aluno VARCHAR NOT NULL,
	serie_aluno INTEGER NOT NULL,
	turma_aluno VARCHAR(1) NOT NULL
);

CREATE TABLE materia (
	id_materia SERIAL NOT NULL,
	PRIMARY KEY(id_materia),
	titulo_materia VARCHAR NOT NULL
);

CREATE TABLE professor (
	id_professor SERIAL NOT NULL,
	PRIMARY KEY(id_professor),
	nome_professor VARCHAR NOT NULL
);

CREATE TABLE professor_materia (
	id_professor_materia SERIAL NOT NULL,
	PRIMARY KEY(id_professor_materia),
	id_professor INTEGER NOT NULL,
	FOREIGN KEY(id_professor) REFERENCES professor(id_professor),
	id_materia INTEGER NOT NULL,
	FOREIGN KEY(id_materia) REFERENCES materia(id_materia)
);

CREATE TABLE usuario (
	id_usuario SERIAL NOT NULL,
	PRIMARY KEY(id_usuario),
	id_aluno INTEGER,
	FOREIGN KEY(id_aluno) REFERENCES aluno(id_aluno),
	id_professor INTEGER,
	FOREIGN KEY(id_professor) REFERENCES professor(id_professor),
	CONSTRAINT check_usuario CHECK (((id_aluno = NULL) AND (id_professor <> NULL)) OR ((id_aluno <> NULL) AND (id_professor = NULL))) --A xor B = ( A and not B) or ( not A and B)
);

CREATE TABLE emprestimo (
	id_emprestimo SERIAL NOT NULL,
	PRIMARY KEY(id_emprestimo),
	motivo_emprestimo VARCHAR NOT NULL,
	data_inicio_emprestimo DATE NOT NULL,
	data_fim_emprestimo DATE NOT NULL,
	id_usuario INTEGER NOT NULL,
	FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario),
	id_equipamento INTEGER NOT NULL,
	FOREIGN KEY(id_equipamento) REFERENCES equipamento(id_equipamento)
);

CREATE TABLE atribuicao_permanente (
	id_atribuicao_permanente SERIAL NOT NULL,
	PRIMARY KEY(id_atribuicao_permanente),
	id_usuario INTEGER NOT NULL,
	FOREIGN KEY(id_usuario) REFERENCES usuario(id_usuario),
	id_equipamento INTEGER NOT NULL,
	FOREIGN KEY(id_equipamento) REFERENCES equipamento(id_equipamento)
);

CREATE OR REPLACE VIEW getallequipamentos AS
SELECT id_equipamento, numero_de_serie_equipamento, matricula_equipamento, titulo_categoria as categoria, sts_equi.titulo_status as status_equipamento, matricula_carregador, sts_carr.titulo_status as status_carregador
FROM equipamento equi	
INNER JOIN categoria cate ON equi.id_categoria = cate.id_categoria
INNER JOIN status sts_equi ON equi.id_status = sts_equi.id_status
INNER JOIN carregador ON equi.id_carregador = carregador.id_carregador
INNER JOIN status sts_carr ON sts_carr.id_status = carregador.id_status;

CREATE OR REPLACE VIEW getallatribuicoesfromaluno AS
SELECT id_atribuicao_permanente, aluno.id_aluno, nome_aluno, serie_aluno, turma_aluno
id_equipamento, numero_de_serie_equipamento, matricula_equipamento, titulo_categoria as categoria, 
sts_equi.titulo_status as status_equipamento, matricula_carregador, sts_carr.titulo_status as status_carregador
FROM atribuicao_permanente ap 
INNER JOIN usuario ON ap.id_usuario = usuario.id_usuario
INNER JOIN aluno ON usuario.id_aluno = aluno.id_aluno
INNER JOIN equipamento equi ON ap.id_equipamento = equi.id_equipamento
INNER JOIN categoria cate ON equi.id_categoria = cate.id_categoria
INNER JOIN status sts_equi ON equi.id_status = sts_equi.id_status
INNER JOIN carregador ON equi.id_carregador = carregador.id_carregador
INNER JOIN status sts_carr ON sts_carr.id_status = carregador.id_status;

CREATE OR REPLACE VIEW getallatribuicoesfromprofessor AS
SELECT id_atribuicao_permanente, prof.nome_professor, titulo_materia,
equi.id_equipamento, numero_de_serie_equipamento, matricula_equipamento, titulo_categoria as categoria, 
sts_equi.titulo_status as status_equipamento, matricula_carregador, sts_carr.titulo_status as status_carregador
FROM atribuicao_permanente ap 
INNER JOIN usuario ON ap.id_usuario = usuario.id_usuario
INNER JOIN professor prof ON usuario.id_professor = prof.id_professor
INNER JOIN professor_materia pm ON pm.id_professor = prof.id_professor
INNER JOIN materia ON materia.id_materia = pm.id_materia
INNER JOIN equipamento equi ON ap.id_equipamento = equi.id_equipamento
INNER JOIN categoria cate ON equi.id_categoria = cate.id_categoria
INNER JOIN status sts_equi ON equi.id_status = sts_equi.id_status
INNER JOIN carregador ON equi.id_carregador = carregador.id_carregador
INNER JOIN status sts_carr ON sts_carr.id_status = carregador.id_status;
