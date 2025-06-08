with source as (

    select * from {{ source('public', 'claims') }}

),

renamed as (

    select
        claim_id,
        patient_id,
        procedure_code,
        amount,
        claim_date

    from source

)

select * from renamed
