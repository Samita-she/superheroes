from flask import Blueprint, request, jsonify
from .models import db, Hero, Power, HeroPower

api = Blueprint("api", __name__)

@api.route("/heroes", methods=["GET"])
def get_heroes():
    return jsonify([hero.to_dict() for hero in Hero.query.all()])

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
    return jsonify([power.to_dict() for power in Power.query.all()])

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
            power.description = data.get("description", power.description)
            db.session.commit()
            return jsonify(power.to_dict())
        except Exception as e:
            return jsonify({"errors": [str(e)]}), 400

@api.route("/hero_powers", methods=["POST"])
def create_hero_power():
    try:
        data = request.get_json()
        new_hp = HeroPower(
            strength=data["strength"],
            hero_id=data["hero_id"],
            power_id=data["power_id"]
        )
        db.session.add(new_hp)
        db.session.commit()
        return jsonify(new_hp.to_dict()), 201
    except Exception as e:
        return jsonify({"errors": [str(e)]}), 400
