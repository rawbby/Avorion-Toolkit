from avorion import *


def main(argv: [str]):
    ship_material = ShipMaterial()
    target = Target()
    target.material = ship_material

    target.shield = 400000.0
    target.crew = 50.0
    target.cargo = 20000.0
    target.hangar = 400.0
    target.hp = 200000.0
    target.acceleration = 200.0
    target.speed = 1600.0
    target.deceleration = target.acceleration * (2. / 3.)
    target.energy_generation_factor = 3.0
    target.energy_storage_factor = 2.0

    result_ship = create_ship_from_target(target)
    print(result_ship)

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
