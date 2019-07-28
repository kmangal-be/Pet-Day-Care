from app import db, Pet, PetType

## CREATE ##

pet_type = PetType('Dog','Medium',5)
db.session.add(pet_type)
db.session.commit()

## READ ##
all_pet_types = PetType.query.all()
print(all_pet_types)


## Select by ID ##
pet_type_one = PetType.query.get(1)
print(pet_type_one.name)


#FILTER#
pet_medium = PetType.query.filter_by(size='Medium')







my_pet = Pet('Rufus',7,'Grey','German Chefard',5)