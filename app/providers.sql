-- name: get_all_providers
select * from providers;

-- name: delete_all_providers
delete from providers
returning *;

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
