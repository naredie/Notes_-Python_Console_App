Create database
if not exists console_app_python;
use console_app_python;

create table usuarios
(
    id int(255)
    auto_increment not null,
    nombre varchar
    (100),
    apellidos varchar
    (255),
    email varchar
    (255) not null,
    password varchar
    (255) not null,
    creado date not null,
    constraint pk_usuario PRIMARY key
    (id),
    constraint uq_email unique
    (email)
)engine=InnoDb;
    /*mantiene la integridad referencial entre diferentes tablas*/

    create table notas
    (
        id int(25)
        auto_increment not null,
usuario_id int
        (25) not null,
titulo varchar
        (255) not null,
descripcion text,
fecha date not null,
constraint pk_notas primary key
        (id),
constraint fk_nota_usuario foreign key
        (usuario_id) references usuarios
        (id)
)engine=InnoDb;