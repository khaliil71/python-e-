class WorkoutLogic:
    def get_beginner_plan(self):
        """Returns a fixed 3-day beginner workout plan"""
        return [
            {  
                "day": "Day 1 - Full Body",
                "exercises": [
                    {"name": "Bodyweight Squats", "sets": 3, "reps": "10-12"},
                    {"name": "Knee Push-ups", "sets": 3, "reps": "8-10"},
                    {"name": "Plank", "sets": 3, "duration": "20-30 sec"},
                    {"name": "Brisk Walking", "duration": "10 min"}
                ]
            },
            {   
                "day": "Day 2 - Rest/Recovery",
                "exercises": [
                    {"name": "Walking or Stretching", "duration": "20-30 min"},
                    {"name": "Focus on hydration and nutrition", "note": ""}
                ]
            },
            {   
                "day": "Day 3 - Full Body",
                "exercises": [
                    {"name": "Assisted Lunges", "sets": 3, "reps": "8 each leg"},
                    {"name": "Wall Push-ups", "sets": 3, "reps": "10-12"},
                    {"name": "Seated Knee Lifts", "sets": 3, "reps": "12"},
                    {"name": "Light Cycling", "duration": "10 min"}
                ]
            }
        ]
