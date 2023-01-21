import sys


def call_center(clients: list, participants: list, recipients: list) -> list:
    # solution 1
    return list(set(clients + participants).difference(set(recipients)))

    # solution 2
    # lst = []
    # st = set(clients + participants).difference(set(recipients))
    # for elem in set(clients + participants):
    #     if elem in st:
    #         lst.append(elem)
    #         st.discard(elem)
    # return lst

    # solution 3
    # st = set(recipients)
    # for elem in clients:
    #     if elem in st:
    #         clients.remove(elem)
    #         st.discard(elem)
    # return clients


def potential_clients(clients: list, participants: list) -> list:
    # solution 1
    return list(set(participants).difference(set(clients)))

    # solution 2
    # lst = [elem for elem in participants if elem in set(participants).difference(set(clients))]
    # return lst


def loyalty_program(clients: list, participants: list) -> list:
    # solution 1
    return list(set(clients).difference(set(participants)))

    # solution 2
    # lst = [elem for elem in clients if elem in set(clients).difference(set(participants))]
    # return lst


def marketing():
    clients = [
        'andrew@gmail.com',
        'jessica@gmail.com',
        'ted@mosby.com',
        'john@snow.is',
        'bill_gates@live.com',
        'mark@facebook.com',
        'elon@paypal.com',
        'jessica@gmail.com'
    ]
    participants = [
        'walter@heisenberg.com',
        'vasily@mail.ru',
        'pinkman@yo.org',
        'jessica@gmail.com',
        'elon@paypal.com',
        'pinkman@yo.org',
        'mr@robot.gov',
        'eleven@yahoo.com'
    ]
    recipients = [
        'andrew@gmail.com',
        'jessica@gmail.com',
        'john@snow.is'
    ]

    if len(sys.argv) == 2:
        if sys.argv[1] == 'call_center':
            print(call_center(clients, participants, recipients))
        elif sys.argv[1] == 'potential_clients':
            print(potential_clients(clients, participants))
        elif sys.argv[1] == 'loyalty_program':
            print(loyalty_program(clients, participants))
        else:
            raise ValueError("Error: Wrong argument.")


if __name__ == '__main__':
    marketing()
