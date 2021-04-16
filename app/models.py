from . import db


class Concept(db.Model):
    __tablename__ = 'concept'

    concept_id = db.Column(db.Integer, primary_key=True, nullable=False)
    concept_name = db.Column(db.String(255))
    domain_id = db.Column(db.String(20), )
    vocabulary_id = db.Column(db.String(20))
    concept_class_id = db.Column(db.String(20))
    standard_concept = db.Column(db.String(1))
    concept_code = db.Column(db.String(50))
    valid_start_date = db.Column(db.Date)
    valid_end_date = db.Column(db.Date)
    invalid_reason = db.Column(db.String(50))


class ConditionOccurrence(db.Model):
    __tablename__ = 'condition_occurrence'

    condition_occurrence_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    person_id = db.Column(db.BigInteger, db.ForeignKey('person.person_id'))
    condition_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id'))
    condition_start_date = db.Column(db.Date)
    condition_start_datetime = db.Column(db.TIMESTAMP)
    condition_end_date = db.Column(db.Date)
    condition_end_datetime = db.Column(db.TIMESTAMP)
    condition_type_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id'))
    condition_status_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id'))
    stop_reason = db.Column(db.String(20))
    provider_id = db.Column(db.BigInteger)
    visit_occurrence_id = db.Column(db.BigInteger, db.ForeignKey('visit_occurrence.visit_occurrence_id'))
    visit_detail_id = db.Column(db.BigInteger)
    condition_source_value = db.Column(db.String(50))
    condition_source_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id'))
    condition_status_source_value = db.Column(db.String(50))


class Death(db.Model):
    __tablename__ = 'death'

    person_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    death_date = db.Column(db.Date)
    death_datetime = db.Column(db.TIMESTAMP)
    death_type_concept_id = db.Column(db.Integer)
    cause_concept_id = db.Column(db.BigInteger, db.ForeignKey('concept.concept_id'))
    cause_source_value = db.Column(db.Integer)
    cause_source_concept_id = db.Column(db.BigInteger, db.ForeignKey('concept.concept_id'))


class DrugExposure(db.Model):
    __tablename__ = 'drug_exposure'

    drug_exposure_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    person_id = db.Column(db.BigInteger, db.ForeignKey('person.person_id'))
    drug_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id'))
    drug_exposure_start_date = db.Column(db.Date)
    drug_exposure_start_datetime = db.Column(db.TIMESTAMP)
    drug_exposure_end_date = db.Column(db.Date)
    drug_exposure_end_datetime = db.Column(db.TIMESTAMP)
    verbatim_end_date = db.Column(db.Date)
    drug_type_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id'))
    stop_reason = db.Column(db.String(20))
    refills = db.Column(db.Integer)
    quantity = db.Column(db.Numeric)
    days_supply = db.Column(db.Integer)
    sig = db.Column(db.Text)
    route_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id'))
    lot_number = db.Column(db.String(50))
    provider_id = db.Column(db.BigInteger)
    visit_occurrence_id = db.Column(db.BigInteger, db.ForeignKey('visit_occurrence.visit_occurrence_id'))
    visit_detail_id = db.Column(db.BigInteger)
    drug_source_value = db.Column(db.String(50))
    drug_source_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id'))
    route_source_value = db.Column(db.String(50))
    dose_unit_source_value = db.Column(db.String(50))


class Person(db.Model):
    __tablename__ = 'person'

    person_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    gender_concept_id = db.Column(db.Integer)
    year_of_birth = db.Column(db.Integer)
    month_of_birth = db.Column(db.Integer)
    day_of_birth = db.Column(db.Integer)
    birth_datetime = db.Column(db.TIMESTAMP)
    race_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id'))  # 인종
    ethnicity_concept_id = db.Column(db.Integer)
    location_id = db.Column(db.BigInteger)
    provider_id = db.Column(db.BigInteger)
    care_site_id = db.Column(db.BigInteger)
    person_source_value = db.Column(db.String(50))
    gender_source_value = db.Column(db.String(50))  # 성별
    gender_source_concept_id = db.Column(db.BigInteger, db.ForeignKey('concept.concept_id'))
    race_source_value = db.Column(db.String(50))
    race_source_concept_id = db.Column(db.Integer)
    ethnicity_source_value = db.Column(db.String(50))
    ethnicity_source_concept_id = db.Column(db.Integer)


class VisitOccurrence(db.Model):
    __tablename__ = 'visit_occurrence'

    visit_occurrence_id = db.Column(db.BigInteger, primary_key=True, nullable=False)
    person_id = db.Column(db.BigInteger, db.ForeignKey('person.person_id'))
    visit_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id'))
    visit_start_date = db.Column(db.Date)
    visit_start_datetime = db.Column(db.TIMESTAMP)
    visit_end_date = db.Column(db.Date)
    visit_end_datetime = db.Column(db.TIMESTAMP)
    visit_type_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id'))
    provider_id = db.Column(db.BigInteger)
    care_site_id = db.Column(db.BigInteger)
    visit_source_value = db.Column(db.String(50))
    visit_source_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id'))
    admitted_from_concept_id = db.Column(db.Integer)
    admitted_from_source_value = db.Column(db.String(50))
    discharge_to_source_value = db.Column(db.String(50))
    discharge_to_concept_id = db.Column(db.Integer, db.ForeignKey('concept.concept_id'))
    preceding_visit_occurrence_id = db.Column(db.BigInteger, db.ForeignKey('visit_occurrence.visit_occurrence_id'))
