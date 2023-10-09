from db.handlers import session
from db.tables import Athlete


def add_athlete(athlete):
    session.add(athlete)
    session.commit()


def delete_athlete(athlete):
    session.delete(athlete)
    session.commit()


def edit_athlete(athlete, athlete_id):
    athlete_list = list_athlete()
    athlete_list[athlete_id].name = athlete.name
    athlete_list[athlete_id].cpf = athlete.cpf
    athlete_list[athlete_id].age = athlete.age
    athlete_list[athlete_id].birthdate = athlete.birthdate
    athlete_list[athlete_id].height = athlete.height
    athlete_list[athlete_id].weight = athlete.weight
    athlete_list[athlete_id].sex = athlete.sex
    athlete_list[athlete_id].sport = athlete.sport

def list_athlete():
    athlete_list = session.query(Athlete).order_by(Athlete.id_athlete)
    return athlete_list


def delete_athlete_by_id(athlete_id):
    athlete = recover_test_case(athlete_id)
    session.delete(athlete)
    session.commit()


def recover_test_case(athlete_id):
    athlete_list_query = list_athlete()
    athlete_list = athlete_list_query.all()
    last_index = (athlete_list.__len__() - 1)
    if last_index > -1:
        return athlete_list[athlete_id]
    else:
        return None
