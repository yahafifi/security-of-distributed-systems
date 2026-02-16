create table if not exists logs (
    id serial primary key,
    message text not null,
    created_at timestamp default current_timestamp
);
