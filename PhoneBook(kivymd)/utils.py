from models import User, Phone


def phone_save(name: str, pthones: str) -> bool:
    if name and pthones:
        user = User.add(name)
        for phone in pthones.split('\n'):
            Phone.add(phone, user)
        return True
    return False

def show_all_for_name(query: str):
    return [tuple([user.name, ' '.join([phone.phone for phone in user.phones]), user.id]) for user in User.find_by_name(query)]

def show_all_for_phone(query: str):
    return [tuple([user.name, ' '.join([phone.phone for phone in user.phones]), user.id]) for user in User.find_by_phone(query)]

def show_all_phones():
    return [tuple([user.name, ' '.join([phone.phone for phone in user.phones]), user.id]) for user in User.find_all()]

def delete_by_id(user_id):
    return User.delete_by_id(user_id)
