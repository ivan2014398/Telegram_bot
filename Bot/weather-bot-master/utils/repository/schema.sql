create table Users (
    id integer primary key,
    tg_user_id integer unique not null,
    username text not null
);

create table Subscribes (
    id integer primary key,
    user_id integer unique not null,

    foreign key (user_id) references Users (id)
);