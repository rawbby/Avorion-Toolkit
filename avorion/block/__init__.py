material_iron = 'iron'
material_titanium = 'titanium'
material_naonite = 'naonite'
material_trinium = 'trinium'
material_xanion = 'xanion'
material_ogonite = 'ogonite'
material_avorion = 'avorion'

block_armor = 'armor'
block_engine = 'engine'
block_cargo = 'cargo'
block_quarters = 'quarters'
block_thruster = 'thruster'
block_hangar = 'hangar'
block_shield = 'shield'
block_storage = 'storage'
block_generator = 'generator'
block_integrity = 'integrity'
block_computer = 'computer'
block_gyro_yaw = 'gyro_yaw'
block_gyro_pitch = 'gyro_pitch'
block_gyro_roll = 'gyro_roll'
block_dampener = 'dampener'

attribute_energy_consumption = 'energy_consumption'
attribute_yaw = 'yaw'
attribute_credits = 'credits'
attribute_energy_storage = 'energy_storage'
attribute_hp = 'hp'
attribute_shield = 'shield'
attribute_processing = 'processing'
attribute_roll = 'roll'
attribute_mass = 'mass'
attribute_pitch = 'pitch'
attribute_cost = 'cost'
attribute_crew = 'crew'
attribute_energy_generation = 'energy_generation'

material_types = {material_iron,
                  material_titanium,
                  material_naonite,
                  material_trinium,
                  material_xanion,
                  material_ogonite,
                  material_avorion}

block_types = {block_armor,
               block_engine,
               block_cargo,
               block_quarters,
               block_thruster,
               block_hangar,
               block_shield,
               block_storage,
               block_generator,
               block_integrity,
               block_computer,
               block_gyro_yaw,
               block_gyro_pitch,
               block_gyro_roll,
               block_dampener}

attributes = {attribute_energy_consumption,
              attribute_yaw,
              attribute_credits,
              attribute_energy_storage,
              attribute_hp,
              attribute_shield,
              attribute_processing,
              attribute_roll,
              attribute_mass,
              attribute_pitch,
              attribute_cost,
              attribute_crew,
              attribute_energy_generation}

block_attributes = {
    block_armor: {attribute_credits,
                  attribute_cost,
                  attribute_hp,
                  attribute_mass},

    block_engine: {attribute_credits,
                   attribute_cost,
                   attribute_hp,
                   attribute_mass,
                   attribute_energy_consumption,
                   attribute_processing},

    block_cargo: {attribute_credits,
                  attribute_cost,
                  attribute_hp,
                  attribute_mass,
                  attribute_energy_consumption,
                  attribute_processing},

    block_quarters: {attribute_credits,
                     attribute_cost,
                     attribute_hp,
                     attribute_mass,
                     attribute_processing},

    block_thruster: {attribute_credits,
                     attribute_cost,
                     attribute_hp,
                     attribute_mass,
                     attribute_crew,
                     attribute_energy_consumption,
                     attribute_processing},

    block_hangar: {attribute_credits,
                   attribute_cost,
                   attribute_hp,
                   attribute_mass,
                   attribute_processing},

    block_shield: {attribute_credits,
                   attribute_cost,
                   attribute_hp,
                   attribute_mass,
                   attribute_shield,
                   attribute_energy_consumption,
                   attribute_processing},

    block_storage: {attribute_credits,
                    attribute_cost,
                    attribute_hp,
                    attribute_mass,
                    attribute_energy_storage,
                    attribute_processing},

    block_generator: {attribute_credits,
                      attribute_cost,
                      attribute_hp,
                      attribute_mass,
                      attribute_energy_generation,
                      attribute_processing},

    block_integrity: {attribute_credits,
                      attribute_cost,
                      attribute_hp,
                      attribute_mass,
                      attribute_energy_consumption,
                      attribute_processing},

    block_computer: {attribute_credits,
                     attribute_cost,
                     attribute_hp,
                     attribute_mass,
                     attribute_energy_consumption,
                     attribute_processing},

    block_gyro_yaw: {attribute_credits,
                     attribute_cost,
                     attribute_hp,
                     attribute_mass,
                     attribute_yaw,
                     attribute_energy_consumption,
                     attribute_processing},

    block_gyro_pitch: {attribute_credits,
                       attribute_cost,
                       attribute_hp,
                       attribute_mass,
                       attribute_pitch,
                       attribute_energy_consumption,
                       attribute_processing},

    block_gyro_roll: {attribute_credits,
                      attribute_cost,
                      attribute_hp,
                      attribute_mass,
                      attribute_roll,
                      attribute_energy_consumption,
                      attribute_processing},

    block_dampener: {attribute_credits,
                     attribute_cost,
                     attribute_hp,
                     attribute_mass,
                     attribute_energy_consumption,
                     attribute_processing},
}

block_materials = {
    block_armor: {material_iron, material_titanium, material_trinium, material_ogonite},
    block_engine: material_types,
    block_thruster: material_types,
    block_cargo: material_types,
    block_quarters: material_types,
    block_hangar: {material_trinium, material_xanion, material_ogonite, material_avorion},
    block_shield: {material_naonite, material_trinium, material_xanion, material_avorion},
    block_storage: material_types,
    block_generator: material_types,
    block_integrity: {material_titanium, material_naonite, material_trinium, material_xanion, material_avorion},
    block_computer: {material_trinium, material_xanion, material_avorion},
    block_gyro_yaw: material_types,
    block_gyro_pitch: material_types,
    block_gyro_roll: material_types,
    block_dampener: {material_iron, material_avorion},
}
