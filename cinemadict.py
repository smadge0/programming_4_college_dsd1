cinema = {"Unfrosted": {"Times":["10:40", "12:00", "13:00", "14:20", "15:20", "17:00", "18:00", "19:40", "20:40", "22:00"], "Seats": 38 },
          "Cats (2019)": {"Times": ["8:30", "11:20", "12:30", "14:20", "16:20", "18:00", "19:00", "21:30", "23:00"], "Seats": 27},
          "Texas Chainsaw Massacre (2022)":{"Times": ["9:00", "11:30", "12:40", "14:20", "16:20", "18:00", "19:00", "21:30", "23:00"], "Seats": 15},
          "Disaster Movie": {"Times": ["8:40", "11:30", "13:00", "14:00", "16:30", "17:30", "19:20", "21:40", "23:30"], "Seats": 31}
          }

def viewmoviesplustimes(cinema):
    for key in cinema.keys():
        print(f"{key} is showing at {cinema[key]["Times"]}")

viewmoviesplustimes(cinema)


