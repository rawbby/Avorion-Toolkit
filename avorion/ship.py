from . import *
import math
from avorion.block import *


class ShipMaterial:
    armor: str
    engine: str
    cargo: str
    quarters: str
    thruster: str
    hangar: str
    shield: str
    energy_container: str
    generator: str
    integrity: str
    computer: str
    gyro: str
    dampener: str

    def __init__(self):
        self.armor = material_trinium
        self.engine = material_xanion
        self.cargo = material_trinium
        self.quarters = material_trinium
        self.thruster = material_trinium
        self.hangar = material_trinium
        self.shield = material_trinium
        self.energy_container = material_xanion
        self.generator = material_trinium
        self.integrity = material_trinium
        self.computer = material_trinium
        self.gyro = material_trinium
        self.dampener = material_iron


class Target:
    material: ShipMaterial

    shield: float
    crew: float

    cargo: float
    hangar: float

    hp: float
    acceleration: float
    speed: float
    deceleration: float
    # yaw = 0.9
    # pitch = 0.9
    # roll = 0.9
    energy_generation_factor: float

    # how many times the required hyperspace jump energy should the energy containers hold
    energy_storage_factor: float


class Ship:
    armor_volume: int
    engine_volume: int
    cargo_volume: int
    quarters_volume: int
    thruster_volume: int
    hangar_volume: int
    shield_volume: int
    energy_container_volume: int
    generator_volume: int
    integrity_volume: int
    computer_volume: int
    gyro_volume: int
    dampener_volume: int
    material: ShipMaterial


def create_ship_from_target(target: Target):

    result_ship = Ship()
    material = target.material

    result_ship.material = material

    _shield = shield[material.shield]
    shield_factor = _shield[attribute_shield]
    shield_volume = math.ceil(target.shield / shield_factor)
    shield_energy_consumption = math.ceil(shield_volume * _shield[attribute_energy_consumption])
    shield_mass = math.ceil(shield_volume * _shield[attribute_mass])
    shield_hp = math.ceil(shield_volume * _shield[attribute_hp])

    _quarters = quarters[material.quarters]
    crew_factor = _quarters[attribute_crew]
    quarters_volume = math.ceil(target.crew / crew_factor)
    quarters_energy_consumption = math.ceil(quarters_volume * _quarters[attribute_energy_consumption])
    quarters_mass = math.ceil(quarters_volume * _quarters[attribute_mass])
    quarters_hp = math.ceil(quarters_volume * _quarters[attribute_hp])

    _cargo = cargo[material.cargo]
    cargo_edge = math.ceil(.5 + (2. * target.cargo / 7.) ** (1. / 3.))
    cargo_volume = math.floor(cargo_edge ** 3.)
    cargo_mass = math.ceil(cargo_volume * _cargo[attribute_mass])
    cargo_hp = math.ceil(cargo_volume * _cargo[attribute_hp])

    _hangar = hangar[material.hangar]
    hangar_edge = math.ceil(.5 + ((2. * target.hangar) ** (1. / 3.)))
    hangar_volume = math.floor(hangar_edge ** 3.)
    hangar_mass = math.ceil(hangar_volume * _hangar[attribute_mass])
    hangar_hp = math.ceil(hangar_volume * _hangar[attribute_hp])

    _engine = engine[material.engine]
    _armor = armor[material.armor]

    energy_consumption_sum = shield_energy_consumption + quarters_energy_consumption
    mass_sum = shield_mass + quarters_mass + cargo_mass + hangar_mass
    hp_sum = shield_hp + quarters_hp + cargo_hp + hangar_hp

    energy_consumption_extra = 0.
    mass_extra = 0.
    hp_extra = 0.

    for i in range(0, 5):
        hp_extra = target.hp - hp_sum
        hp_extra = max(hp_extra, 0)
        armor_volume = math.ceil(hp_extra / _armor[attribute_hp])
        armor_mass = math.ceil(armor_volume * _armor[attribute_mass])

        engine_volume_for_target_acceleration = target.acceleration * mass_sum / 20000.
        engine_volume_for_target_speed = math.exp((target.speed + 86) / 100) - 5
        engine_volume = max(engine_volume_for_target_speed, engine_volume_for_target_acceleration)
        engine_mass = math.ceil(engine_volume * _engine[attribute_mass])
        engine_energy_consumption = math.ceil(engine_mass * _engine[attribute_energy_consumption])

        dampener_volume = target.deceleration/(2.26583888326630189525+54314.39356138062430545688 / mass_sum)


    return result_ship
