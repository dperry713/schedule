import copy

class ShiftSchedule:
    def __init__(self):
        self.schedules = {}

    def add_week_schedule(self, week, schedule):
        self.schedules[week] = schedule

    def shallow_copy_week(self, source_week, target_week):
        if source_week in self.schedules:
            self.schedules[target_week] = self.schedules[source_week]
            print(f"Shallow copied schedule from {source_week} to {target_week}.")
        else:
            print(f"Week {source_week} not found.")

    def deep_copy_week(self, source_week, target_week):
        if source_week in self.schedules:
            self.schedules[target_week] = copy.deepcopy(self.schedules[source_week])
            print(f"Deep copied schedule from {source_week} to {target_week}.")
        else:
            print(f"Week {source_week} not found.")

    def modify_shift(self, week, employee, shift):
        if week in self.schedules and employee in self.schedules[week]:
            self.schedules[week][employee] = shift
            print(f"Modified shift for {employee} in week {week} to {shift}.")
        else:
            print(f"Week {week} or employee {employee} not found.")

    def display_schedules(self):
        for week, schedule in self.schedules.items():
            print(f"Week {week}:")
            for employee, shift in schedule.items():
                print(f"  {employee}: {shift}")

def main():
    shift_schedule = ShiftSchedule()

    # Adding initial schedules
    week1_schedule = {
        "Alice": "9am-5pm",
        "Bob": "10am-6pm",
        "Charlie": "11am-7pm"
    }
    week2_schedule = {
        "Alice": "8am-4pm",
        "Bob": "9am-5pm",
        "Charlie": "10am-6pm"
    }
    shift_schedule.add_week_schedule("Week 1", week1_schedule)
    shift_schedule.add_week_schedule("Week 2", week2_schedule)

    # Display initial schedules
    print("Initial Schedules:")
    shift_schedule.display_schedules()

    # Shallow copy Week 1 to Week 3
    shift_schedule.shallow_copy_week("Week 1", "Week 3")
    print("\nAfter Shallow Copy:")
    shift_schedule.display_schedules()

    # Modify shift in Week 3
    shift_schedule.modify_shift("Week 3", "Alice", "12pm-8pm")
    print("\nAfter Modifying Shift in Week 3:")
    shift_schedule.display_schedules()

    # Deep copy Week 2 to Week 4
    shift_schedule.deep_copy_week("Week 2", "Week 4")
    print("\nAfter Deep Copy:")
    shift_schedule.display_schedules()

    # Modify shift in Week 4
    shift_schedule.modify_shift("Week 4", "Bob", "1pm-9pm")
    print("\nAfter Modifying Shift in Week 4:")
    shift_schedule.display_schedules()

if __name__ == "__main__":
    main()
