-- name: get_all_providers
select providerid, name, active, department, organization, location, address from providers
limit :limit offset :offset;

-- name: get_provider_by_id
select providerid, name, active, department, organization, location, address from providers
    where providerid = :providerid;

-- name: get_phone_by_provider_id
select phone from phone_numbers
    where providerid = :providerid;

-- name: get_speclialty_by_provider_id
select speciality from specialities
    where providerid = :providerid;

-- name: get_qualification_by_provider_id
select qualification from qualifications
    where providerid = :providerid;

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
    where providerid = :providerid;

-- name: delete_provider_by_id
delete from providers
    where providerid = :providerid
returning providerid;

-- name: delete_all_providers
delete from providers
returning *;

-- name: search_providers
select providerid, name, active, department, organization, location, address
from (
    select providerid, name, active, department, organization, location, address, tsv
    from providers, plainto_tsquery(:query) as q
    where (tsv @@ q)
) as t1 order by ts_rank_cd(tsv, plainto_tsquery(:query)) desc limit :limit offset :offset;