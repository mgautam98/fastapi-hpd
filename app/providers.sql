-- name: get_all_providers
select * from providers
limit :limit offset :offset;

-- name: get_provider_by_id
select * from providers
    where id = :providerid;

-- name: get_phone_by_provider_id
select phone from providers
    where id = :providerid;

-- name: get_speclialty_by_provider_id
select specialty from providers
    where id = :providerid;

-- name: get_qualification_by_provider_id
select qualification from providers
    where id = :providerid;

-- name: create_provider
insert into providers(providerid, active, name, organization, address, department, location)
values (:providerid, :active, :name, :organization, :address, :department, :location)
RETURNING
    providerid, name;

-- name: add_phone_numbers
insert into phone_numbers(providerid, phone)
values (:providerid, :phone)
RETURNING
    providerid, phone;

-- name: add_qualifications
insert into qualifications(providerid, qualification)
values (:providerid, :qualification)
RETURNING
    providerid, qualification;

-- name: add_specialities
insert into specialities(providerid, speciality)
values (:providerid, :speciality)
RETURNING
    providerid, speciality;

-- name: update_provider
update providers
    set active = :active,
        name = :name,
        organization = :organization,
        address = :address,
        department = :department,
        location = :location
    where id = :providerid;

-- name: delete_all_providers
delete from providers
returning *;
