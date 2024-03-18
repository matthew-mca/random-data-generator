import json

import click
from faker import Faker
from faker.providers import address, date_time, person

FAKER = Faker()
FAKER.add_provider(address)
FAKER.add_provider(date_time)
FAKER.add_provider(person)


@click.command()
@click.option(
    "-c",
    "--object-count",
    type=int,
    default=50,
    help="The number of random data objects to include in the JSON output. Defaults to 50 objects.",
)
@click.option(
    "--name",
    is_flag=True,
    help="A flag to include a 'name' field in the generated data objects.",
)
@click.option(
    "--date-of-birth",
    is_flag=True,
    help="A flag to include a 'date of birth' field in the generated data objects.",
)
@click.option(
    "--building-number",
    is_flag=True,
    help="A flag to include a 'building number' field in the generated data objects.",
)
@click.option(
    "--street-name",
    is_flag=True,
    help="A flag to include a 'street name' field in the generated data objects.",
)
@click.option(
    "--city",
    is_flag=True,
    help="A flag to include a 'city' field in the generated data objects.",
)
@click.option(
    "--country",
    is_flag=True,
    help="A flag to include a 'country' field in the generated data objects.",
)
def cli(object_count, name, date_of_birth, building_number, street_name, city, country):
    click.echo("Generating random data...")

    output = {}
    output["randomObjectCount"] = object_count
    output["randomData"] = []

    for i in range(object_count):
        random_obj = {
            "objectID": i + 1,
        }

        if name:
            random_obj["name"] = FAKER.name()
        if date_of_birth:
            random_obj["dateOfBirth"] = str(FAKER.date_of_birth(minimum_age=18, maximum_age=99))
        if building_number:
            random_obj["buildingNumber"] = FAKER.building_number()
        if street_name:
            random_obj["streetName"] = FAKER.street_name()
        if city:
            random_obj["city"] = FAKER.city()
        if country:
            random_obj["country"] = FAKER.country()

        output["randomData"].append(random_obj)

    with open("./random_data.json", "w") as f:
        json.dump(output, f, indent=4)

    click.echo("Random data generated successfully.")


if __name__ == "__main__":
    cli()
