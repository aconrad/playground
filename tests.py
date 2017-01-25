def test_person():
    from playground.models.person import Person
    person = Person("muzzy", 1980)


def test_person_age():
    from playground.models.person import Person
    person = Person("muzzy", 1980)
    assert person.age == 37
