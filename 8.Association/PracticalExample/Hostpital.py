class Room:
    def __init__(self, number: str, floor: int):
        self.number = number
        self.floor = floor

class Appointment:
    def __init__(self, doctor, patient, room: Room, time: str):
        self.doctor = doctor
        self.patient = patient
        self.room = room
        self.time = time
        doctor.add_appointment(self)
        patient.add_appointment(self)

class Doctor:
    def __init__(self, name: str, specialization: str):
        self.name = name
        self.specialization = specialization
        self.appointments = []

    def add_appointment(self, appt: Appointment):
        self.appointments.append(appt)

    def get_patients(self):
        seen = set()
        result = []
        for appt in self.appointments:
            if id(appt.patient) not in seen:
                seen.add(id(appt.patient))
                result.append(appt.patient)
        return result

class Patient:
    def __init__(self, name: str):
        self.name = name
        self.appointments = []

    def add_appointment(self, appt: Appointment):
        self.appointments.append(appt)

    def get_doctors(self):
        seen = set()
        result = []
        for appt in self.appointments:
            if id(appt.doctor) not in seen:
                seen.add(id(appt.doctor))
                result.append(appt.doctor)
        return result

if __name__ == "__main__":
    dr_smith = Doctor("Dr. Smith", "Cardiology")
    dr_jones = Doctor("Dr. Jones", "Neurology")

    patient_anna = Patient("Anna")
    patient_bob = Patient("Bob")

    room_101 = Room("101", "1st Floor")
    room_102 = Room("102", "1st Floor")

    appt1 = Appointment(dr_smith, patient_anna, room_101, "10:00 AM")
    appt2 = Appointment(dr_jones, patient_bob, room_102, "11:00 AM")
    appt3 = Appointment(dr_smith, patient_bob, room_101, "12:00 PM")

    print(f"{dr_smith.name} has patients: {[p.name for p in dr_smith.get_patients()]}")
    print(f"{dr_jones.name} has patients: {[p.name for p in dr_jones.get_patients()]}")
    print(f"{patient_anna.name} sees doctors: {[d.name for d in patient_anna.get_doctors()]}")
    print(f"{patient_bob.name} sees doctors: {[d.name for d in patient_bob.get_doctors()]}")
    print(f"Appointment 1: {appt1.doctor.name} with {appt1.patient.name} in room {appt1.room.number} at {appt1.time}")
    print(f"Appointment 2: {appt2.doctor.name} with {appt2.patient.name} in room {appt2.room.number} at {appt2.time}")
    print(f"Appointment 3: {appt3.doctor.name} with {appt3.patient.name} in room {appt3.room.number} at {appt3.time}")