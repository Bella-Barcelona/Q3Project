from pyscript import document, display



def getclub(e):

    get_Info = document.getElementById("Clubs").value

    info = clubs[get_Info] 
    information = f"""
    Club: {get_Info}
    Moderator: {info['Moderator']}
    Meeting Time: {info['Time']}
    Location: {info['Location']}
    Members: {info['Members']}
    """

    document.getElementById("infoclub").innerText = information

clubs = {
    
    "Math Club": {
        "Moderator": "Mr. Nicole Gabuya",
        "Time": "Monday 02:30 - 03:00 PM",
        "Location": "Room 404",
        "Members": 25
    },
    "Science Club": {
        "Moderator": "Ms. Jameelyn Maramag",
        "Time": "Tuesday 03:00 - 04:00 PM",
        "Location": "Room 404",
        "Members": 28
    },
    "Communications Arts Club": {
        "Moderator": "Ms. Yannis Fernandez",
        "Time": "Wed & Fri 03:00 - 04:00 PM",
        "Location": "Room 406",
        "Members": 20
    },
    "Social Science Club": {
        "Moderator": "Mr. Roberto Lim",
        "Time": "Tuesday 03:00 - 04:00 PM",
        "Location": "Room 409",
        "Members": 22
    },
    "CAT club": {
        "Moderator": "SSgt. Jemima David PA (Res)",
        "Time": "Wednesday 02:30 - 04:30 PM",
        "Location": "Quadrangle / Teatro Preciosa",
        "Members": 50
    },
    "Volleyball Varsity": {
        "Moderator": "Mr. Adrian Ruiz",
        "Time": "Wednesday 03:00 - 04:00 PM",
        "Location": "Quadrangle",
        "Members": 18
    },
    "Basketball Varsity": {
        "Moderator": "Mr. Adrian Ruiz",
        "Time": "Monday 03:00 - 04:00 PM",
        "Location": "Quadrangle",
        "Members": 20
    },
    "Marching Band": {
        "Moderator": "Mr. Emilio Alumno",
        "Time": "Tuesday & Wednesday 03:00 - 4:30 PM",
        "Location": "Band Room",
        "Members": 40
    },
    "Glee Club": {
        "Moderator": "Mr. Denver Martin",
        "Time": "Monday 03:00 - 05:00 PM",
        "Location": "High School Music Room",
        "Members": 30
    },
    "Dance Club": {
        "Moderator": "Mr. Alfred Cases",
        "Time": "Tuesday 03:00 - 05:00 PM",
        "Location": "Teatro Preciosa",
        "Members": 35
    },
}