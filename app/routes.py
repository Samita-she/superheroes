from flask import Blueprint, request, jsonify
from .models import db, Hero, Power, HeroPower

api = Blueprint("api", __name__)

@api.route("/heroes", methods=["GET"])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.to_dict() for hero in heroes])

@api.route("/heroes/<int:id>", methods=["GET"])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    data = hero.to_dict()
    data["hero_powers"] = [hp.to_dict() for hp in hero.hero_powers]
    return jsonify(data)

@api.route("/powers", methods=["GET"])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict() for power in powers])

@api.route("/powers/<int:id>", methods=["GET", "PATCH"])
def handle_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    if request.method == "GET":
        return jsonify(power.to_dict())

    elif request.method == "PATCH":
        try:
            data = request.get_json()
            description = data.get("description")

            if not description or len(description) < 20:
                return jsonify({"errors": ["Description must be at least 20 characters long."]}), 400

            power.description = description
            db.session.commit()
            return jsonify(power.to_dict())
        except Exception as e:
            db.session.rollback()
            return jsonify({"errors": [str(e)]}), 400

@api.route("/hero_powers", methods=["POST"])
def create_hero_power():
    try:
        data = request.get_json()
        strength = data.get("strength")
        hero_id = data.get("hero_id")
        power_id = data.get("power_id")

        if not all([strength, hero_id, power_id]):
            return jsonify({"errors": ["Missing required fields."]}), 400

        new_hp = HeroPower(
            strength=strength,
            hero_id=hero_id,
            power_id=power_id
        )
        db.session.add(new_hp)
        db.session.commit()
        return jsonify(new_hp.hero.to_dict()), 201  # Returns updated hero info per spec
    except Exception as e:
        db.session.rollback()
        return jsonify({"errors": [str(e)]}), 400
@api.route("/")
def index():
    return jsonify({
        "message": "Welcome to the Superheroes API 🚀",
        "endpoints": ["/heroes", "/heroes/<id>", "/powers", "/powers/<id>", "/hero_powers"]
    })
