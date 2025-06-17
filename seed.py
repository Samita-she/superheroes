# seed.py

from app import create_app
from app.models import db, Hero, Power, HeroPower

# Create the app context
app = create_app()

with app.app_context():
    # Drop and recreate all tables
    db.drop_all()
    db.create_all()

    # Create hero instances
    heroes = [
        Hero(name="Kamala Khan", super_name="Ms. Marvel"),
        Hero(name="Doreen Green", super_name="Squirrel Girl"),
        Hero(name="Gwen Stacy", super_name="Spider-Gwen"),
        Hero(name="Janet Van Dyne", super_name="The Wasp"),
        Hero(name="Wanda Maximoff", super_name="Scarlet Witch"),
        Hero(name="Carol Danvers", super_name="Captain Marvel"),
        Hero(name="Jean Grey", super_name="Dark Phoenix"),
        Hero(name="Ororo Munroe", super_name="Storm"),
        Hero(name="Kitty Pryde", super_name="Shadowcat"),
        Hero(name="Elektra Natchios", super_name="Elektra"),
    ]

    # Create power instances with valid descriptions
    powers = [
        Power(name="super strength", description="Gives the wielder incredible strength, enough to lift cars and smash walls."),
        Power(name="flight", description="Gives the wielder the ability to fly through the skies at supersonic speed."),
        Power(name="super human senses", description="Allows the wielder to perceive things beyond normal human capability."),
        Power(name="elasticity", description="Can stretch the human body to extreme lengths and shapes."),
    ]

    # Add and commit
    db.session.add_all(heroes + powers)
    db.session.commit()

    print("✅ Database seeded successfully.")

