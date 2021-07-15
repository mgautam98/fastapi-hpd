import aiosql
from app.schemas import HealthcareProvider
from faker import Faker
from fastapi.encoders import jsonable_encoder
import json
import os
import pathlib
import pickle
import psycopg2
from random import randint, choice

Faker.seed(0)

fake = Faker()

data = []
orgs = [" Hospital", " Clinic"]
departments = [
    "Outpatient department (OPD)",
    "Inpatient Service (IP)",
    "Medical Department",
    "Nursing Department",
    "Paramedical Department",
    "Physical Medicine and Rehabilitation Department",
    "Operation Theatre Complex (OT)",
    "Pharmacy Department",
    "Radiology Department (X-ray)",
    "Dietary Department",
    "Non-professional Services (Business Management)",
    "Medical Record Department (MRD)",
    "Personnel Department",
]

specialities = [
    "Aerospace Medicine",
    "Anaesthesia",
    "Bariatric Surgery",
    "Cardiology - Interventional",
    "Cardiology - Non Interventional",
    "Cardiothoracic And Vascular Surgery",
    "Centre For Spinal Diseases",
    "Clinical Haematology And BMT",
    "Corneal Transplant",
    "Critical Care Medicine",
    "Dermatology And Cosmetology",
    "Ear Nose Throat Head And Neck Surgery",
    "Emergency Medicine",
    "Endocrinology",
    "General Surgery",
    "Infectious Diseases",
    "Internal Medicine",
    "In-Vitro Fertilisation (IVF)",
    "Laboratory Medicine",
    "Liver Transplant & Hepatic Surgery",
    "Maxillofacial Surgery",
    "Medical Gastroenterology",
    "Medical Oncology & Clinical Hematology",
    "Medical Oncology",
    "Minimally Invasive Gynecology",
    "Neonatology",
    "Nephrology",
    "Neuro Modulation",
    "Nutrition & Dietetics",
    "Neurology",
    "Neurosurgery",
    "Obstetrics And Gynecology",
    "Ophthalmology",
    "Orthopedics & Joint Replacement",
    "Pain Management",
    "Pediatric Surgery",
    "Physiotherapy",
    "Plastic Surgery",
    "Psychiatry",
    "Pulmonology",
    "Renal Transplant",
    "Reproductive Medicine & IVF",
    "Rheumatology",
    "Robotic Surgery",
    "Surgical Gastroenterology",
    "Surgical Oncology",
    "Urology",
    "Vascular and endovascular surgery",
]

qualifications = [
    "Bachelor of Medicine, Bachelor of Surgery [MBBS]",
    "Bachelor of Physiotherapy [BPT]",
    "Diploma in Medical Laboratory Technology [DMLT]",
    "Bachelor of Ayurvedic Medicine and Surgery [BAMS]",
    "Bachelor of Homeopathic Medicine & Surgery [BHMS]",
    "Bachelor of Science [B.Sc] (Operation Theatre Technology)",
    "Diploma in Physiotherapy [DPT]",
    "Bachelor of Occupational Therapy [BOT]",
    "Diploma in Medical Radio Diagnosis [DMRD]",
    "Bachelor in Audiology and Speech - Language Pathology [BASLP]",
    "Bachelor of Science [B.Sc] (Medical Imaging Technology)",
    "Diploma in Clinical Pathology [DCP]",
    "Certificate Course in Medical Laboratory Technology",
    "Bachelor of Science [B.Sc] (Dialysis)",
    "Bachelor of Science [B.Sc] (Perfusion Technology)",
    "Bachelor of Science [B.Sc] (Renal Dialysis Technology)",
    "Bachelor of Science [B.Sc] {Hons.} (Physiology)",
    "Diploma in X-Ray Technology",
    "Bachelor of Science [B.Sc] (Industrial Microbiology)",
    "Diploma in Otorhinolaryngology [DLO]",
    "Diploma in Anaesthesia [DA]",
    "Diploma in Nursing",
    "Diploma in Operation Theatre Techniques",
    "Bachelor of Science [B.Sc] (Respiratory Therapy)",
    "Diploma in Dialysis Techniques",
    "Bachelor of Unani Medicine & Surgery",
    "Bachelor of Science [B.Sc] (Radiography)",
    "Certificate Course in Physiotherapy",
    "Diploma in Radiography",
    "Diploma in Radiology Therapy [DMRT]",
    "Bachelor of Science [B.Sc] (Imaging Technology Radiography)",
    "Certificate in Laboratory Techniques [CPLT]",
    "Diploma in Occupational Therapy",
    "Bachelor of Science [B.Sc] (Pathology)",
    "Bachelor of Science [B.Sc] (Occupational Therapy)",
    "Bachelor of Science [B.Sc] (Audiology)",
]


def generate(total_recs: int = 100):
    for _ in range(total_recs):
        record = {
            "name": fake.name(),
            "address": fake.address(),
            "organization": fake.company() + choice(orgs),
            "active": True,
            "department": choice(departments) if randint(0, 1) else None,
            "location": fake.city() if randint(0, 1) else None,
            "phone": [fake.phone_number() for _ in range(2)],
            "qualification": [choice(qualifications) for _ in range(2)],
            "speciality": [choice(specialities) for _ in range(2)],
        }

        data.append(jsonable_encoder(HealthcareProvider(**record)))

    return data


def save_pickle(data, path="./database/records.pickle"):
    if not os.path.exists(path):
        open(path, "wb").close()

    with open(path, "wb") as f:
        for record in data:
            pickle.dump(record, f)


def save_json(data, path="./database/records.json"):
    if not os.path.exists(path):
        open(path, "w").close()

    json_data = json.dumps(
        data,
        indent=4,
    )
    with open(path, "w") as f:
        f.write(json_data)


def SaveToDatabase(data):
    conn = psycopg2.connect(
        host="localhost", dbname="providers", user="root", password="root"
    )

    queries = aiosql.from_path(
        pathlib.Path(__file__).parent / "app/providers.sql", "psycopg2"
    )

    queries.delete_all_providers(conn)
    conn.commit()

    for record in data:
        queries.create_provider(
            conn,
            providerid=record["providerID"],
            name=record["name"],
            active=record["active"],
            organization=record["organization"],
            address=record["address"],
            department=record["department"],
            location=record["location"],
        )

        for each in record["phone"]:
            queries.add_phone_numbers(
                conn,
                providerid=record["providerID"],
                phone=each,
            )

        for each in record["qualification"]:
            queries.add_qualifications(
                conn,
                providerid=record["providerID"],
                qualification=each,
            )

        for each in record["speciality"]:
            queries.add_specialities(
                conn,
                providerid=record["providerID"],
                speciality=each,
            )

        conn.commit()


if __name__ == "__main__":
    # save_pickle(generate(300))
    # save_json(generate(300))
    SaveToDatabase(generate(300))
