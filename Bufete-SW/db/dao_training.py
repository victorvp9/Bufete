from db.handlers import session
from db.tables import Training


def add_training(training):
    session.add(training)
    session.commit()


def delete_training(training):
    session.delete(training)
    session.commit()


def edit_training(training, training_id):
    training_list = list_training()
    training_list[training_id].name = training.name
    training_list[training_id].number_of_hits = training.number_of_hits
    training_list[training_id].sequence = training.sequence
    training_list[training_id].is_random = training.is_random


def list_training():
    training_list = session.query(Training).order_by(Training.id_training)
    return training_list


def delete_training_by_id(training_id):
    training = recover_test_case(training_id)
    session.delete(training)
    session.commit()


def recover_test_case(training_id):
    training_list_query = list_training()
    training_list = training_list_query.all()
    last_index = (training_list.__len__() - 1)
    if last_index > -1:
        return training_list[training_id]
    else:
        return None
