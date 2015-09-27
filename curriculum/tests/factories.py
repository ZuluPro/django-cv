import factory
from curriculum import models


class ResumeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Resume

    firstname = factory.Faker('first_name')
    lastname = factory.Faker('last_name')
    title = factory.Faker('job')
    resume = factory.Faker('paragraph')

    phone = factory.Faker('phone_number')
    website = factory.Faker('url')
    email = factory.Faker('email')
    city = factory.Faker('city')
    country = factory.Faker('country')
    address = factory.Faker('address')

    driving_license = factory.Faker('text', max_nb_chars=15)

    hobbies = factory.Faker('text', max_nb_chars=50)
    tags = factory.Faker('word')

    skype = factory.Faker('word')
    twitter = factory.Faker('word')
    stackoverflow = factory.Faker('random_int')
    github = factory.Faker('word')
