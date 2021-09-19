# material_type = ['iron', 'titanium', 'naonite', 'trinium', 'xanion', 'ogonite', 'avorion']
#
# material_mass = {'iron': 51.0, 'titanium': 30.0, 'naonite': 33.0, 'trinium': 21.0,
#                  'xanion': 27.0, 'ogonite': 45.0, 'avorion': 36.0}
#
# material_hp = {'iron': 4.0, 'titanium': 6.0, 'naonite': 9.0, 'trinium': 13.5,
#                'xanion': 20.25, 'ogonite': 30.375, 'avorion': 45.5625}
#
# block_type = ['armorblock', 'engineblock', 'cargobay', 'crewquarters', 'thruster', 'hangar',
#               'shieldgenerator', 'energycontainer', 'generator', 'integrityfieldgenerator',
#               'computercore', 'gyroarrayblock', 'inertiadampener', 'assemblyblock']
#
# block_mass = {'armorblock': 5. / 3., 'thruster': .5, 'engineblock': .5, 'cargobay': 1. / 3.,
#               'crewquarters': 4. / 3., 'hangar': 2. / 3., 'shieldgenerator': 4. / 3., 'energycontainer': 1.,
#               'generator': 4. / 3., 'integrityfieldgenerator': 4. / 3., 'computercore': 4. / 3.,
#               'gyroarrayblock': .5 / 3., 'inertiadampener': .5, 'assemblyblock': 1.}
#
# block_hp = {'armorblock': 6.25, 'thruster': .125, 'engineblock': .5, 'cargobay': 1.,
#             'crewquarters': 1., 'hangar': .15, 'shieldgenerator': .125, 'energycontainer': .25,
#             'generator': .125, 'integrityfieldgenerator': .125, 'computercore': .125,
#             'gyroarrayblock': .5, 'inertiadampener': .125, 'assemblyblock': .5}
#
# shieldgenerator_material_shield = {'naonite': 900. / 8., 'trinium': 1350. / 8., 'xanion': 2025. / 8.,
#                                    'avorion': 4556.25 / 8.}
# shieldgenerator_material_cost = {'naonite': 10061. / 8., 'trinium': 11762. / 8., 'xanion': 14058. / 8.,
#                                  'avorion': 21343.25 / 8.}
# shieldgenerator_material_energy = {'naonite': 187.5 / 8., 'trinium': 217.5 / 8., 'xanion': 255. / 8.,
#                                    'avorion': 352.5 / 8.}
#
# crewquarters_material_crew = {'iron': 0.526316, 'titanium': 0.526316, 'naonite': 0.526316, 'trinium': 0.526316,
#                               'xanion': 0.526316, 'ogonite': 0.526316, 'avorion': 0.526316}
# crewquarters_material_cost = {'iron': 2.25, 'titanium': 2.25, 'naonite': 2.25, 'trinium': 2.25,
#                               'xanion': 2.25, 'ogonite': 2.25, 'avorion': 2.25}
# crewquarters_material_energy = {'iron': 500., 'titanium': 500., 'naonite': 500., 'trinium': 500.,
#                                 'xanion': 500., 'ogonite': 500., 'avorion': 500.}
#
# cargobay_material_cost = {'iron': 2.5, 'titanium': 2.5, 'naonite': 2.5, 'trinium': 2.5,
#                           'xanion': 2.5, 'ogonite': 2.5, 'avorion': 2.5}
#
# hangar_material_cost = {'trinium': 4.5, 'xanion': 4.5, 'ogonite': 4.5, 'avorion': 4.5}

# assert len(block_type) == len(block_mass)
# assert len(material_type) == len(material_mass)
# assert len(material_type) == len(material_hp)


def main(argv: [str]):
    #    block_material = {
    #        'armorblock': 'trinium',
    #        'engineblock': 'xanion',
    #        'cargobay': 'trinium',
    #        'crewquarters': 'trinium',
    #        'thruster': 'trinium',
    #        'hangar': 'trinium',
    #        'shieldgenerator': 'trinium',
    #        'energycontainer': 'xanion',
    #        'generator': 'trinium',
    #        'integrityfieldgenerator': 'trinium',
    #        'computercore': 'trinium',
    #        'gyroarrayblock': 'trinium',
    #        'inertiadampener': 'iron',
    #        'assemblyblock': 'xanion'}
    #
    #    target_shield = 400000.0
    #    target_crew = 50.0
    #
    #    target_cargo = 20000.0
    #    target_hangar = 400.0
    #
    #    target_hp = 200000.0
    #    target_acceleration = 200.0
    #    target_speed = 1600.0
    #    target_deceleration = target_acceleration * (2. / 3.)
    #    target_yaw = 0.9
    #    target_pitch = 0.9
    #    target_roll = 0.9
    #    target_energy_generation_factor = 3.0
    #    target_energy_storage_factor = 2.0
    #
    #    shield_material = block_material['shieldgenerator']
    #    shield_factor = shieldgenerator_material_shield[shield_material]
    #    shield_volume = math.ceil(target_shield / shield_factor)
    #    shield = math.floor(shield_volume * shield_factor)
    #    shield_mass = math.ceil(block_mass['shieldgenerator'] * material_mass[shield_material] * shield_volume)
    #    shield_hp = math.ceil(block_hp['shieldgenerator'] * material_hp[shield_material] * shield_volume)
    #    shield_cost = math.ceil(shieldgenerator_material_cost[shield_material] * shield_volume)
    #    shield_energy = math.ceil(shieldgenerator_material_energy[shield_material] * shield_volume)
    #
    #    print(f"shield_material: {shield_material}")
    #    print(f"shield_volume:   {shield_volume}")
    #    print(f"shield:          {shield}")
    #    print(f"shield_mass:     {shield_mass}")
    #    print(f"shield_hp:       {shield_hp}")
    #    print(f"shield_cost:     {shield_cost}")
    #    print(f"shield_energy:   {shield_energy}")
    #    print()
    #
    #    crew_material = block_material['crewquarters']
    #    crew_factor = crewquarters_material_crew[crew_material]
    #    crew_volume = math.ceil(target_crew / crew_factor)
    #    crew = math.floor(crew_volume * crew_factor)
    #    crew_mass = math.ceil(block_mass['crewquarters'] * material_mass[crew_material] * crew_volume)
    #    crew_hp = math.ceil(block_hp['crewquarters'] * material_hp[crew_material] * crew_volume)
    #    crew_cost = math.ceil(crewquarters_material_cost[crew_material] * crew_volume)
    #    crew_energy = math.ceil(crewquarters_material_energy[crew_material] * crew_volume)
    #
    #    print(f"crew_material: {crew_material}")
    #    print(f"crew_volume:   {crew_volume}")
    #    print(f"crew:          {crew}")
    #    print(f"crew_mass:     {crew_mass}")
    #    print(f"crew_hp:       {crew_hp}")
    #    print(f"crew_cost:     {crew_cost}")
    #    print(f"crew_energy:   {crew_energy}")
    #    print()
    #
    #    cargo_material = block_material['cargobay']
    #    cargo_edge = math.ceil(.5 + (((2. / 7.) ** (1. / 3.)) * (target_cargo ** (1. / 3.))))
    #    cargo = math.floor(3.5 * (cargo_edge - 0.5) ** 3.)
    #    cargo_volume = math.floor(cargo_edge ** 3.)
    #    cargo_mass = math.ceil(block_mass['cargobay'] * material_mass[cargo_material] * cargo_volume)
    #    cargo_hp = math.ceil(block_hp['cargobay'] * material_hp[cargo_material] * cargo_volume)
    #    cargo_cost = math.ceil(cargobay_material_cost[cargo_material] * cargo_volume)
    #
    #    print(f"cargo_material: {cargo_material}")
    #    print(f"cargo_edge:     {cargo_edge}")
    #    print(f"cargo:          {cargo}")
    #    print(f"cargo_volume:   {cargo_volume}")
    #    print(f"cargo_mass:     {cargo_mass}")
    #    print(f"cargo_hp:       {cargo_hp}")
    #    print(f"cargo_cost:     {cargo_cost}")
    #    print()
    #
    #    hangar_material = block_material['hangar']
    #    hangar_edge = math.ceil(.5 + ((2. ** (1. / 3.)) * (target_hangar ** (1. / 3.))))
    #    hangar = math.floor(.5 * (hangar_edge - 0.5) ** 3.)
    #    hangar_volume = math.floor(hangar_edge ** 3.)
    #    hangar_mass = math.ceil(block_mass['hangar'] * material_mass[hangar_material] * hangar_volume)
    #    hangar_hp = math.ceil(block_hp['hangar'] * material_hp[hangar_material] * hangar_volume)
    #    hangar_cost = math.ceil(hangar_material_cost[hangar_material] * hangar_volume)
    #
    #    print(f"hangar_material: {hangar_material}")
    #    print(f"hangar_edge:     {hangar_edge}")
    #    print(f"hangar:          {hangar}")
    #    print(f"hangar_volume:   {hangar_volume}")
    #    print(f"hangar_mass:     {hangar_mass}")
    #    print(f"hangar_hp:       {hangar_hp}")
    #    print(f"hangar_cost:     {hangar_cost}")
    #    print()

    import json
    import avorion

    print(json.dumps(3220065408 / 856000000))

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
