from src.data.programs import Program


def add_program(agency_id, programID, name, description, modifiers, services):
    program = Program()
    program.agency_id = agency_id
    program.programID = programID
    program.name = name
    program.description = description
    program.modifiers = modifiers
    program.services = services

    program.save()
    print('New program created and saved!')
    return program


def find_program_by_ID(id_no):
    program = Program.objects(programID=id_no).first()
    if program:
        return program
    return False


def find_all_programs():
    return Program.objects()
