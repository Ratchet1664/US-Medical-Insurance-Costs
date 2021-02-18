import csv
class Obtain_file():
    def __init__(self):
        self.medical_information = []
        self.regions = ["southeast","southwest", "northeast", "northwest",]
        self.region_information = {
        "southeast":{},
        "southwest":{},
        "northeast":{},
        "northwest":{}
        }

    def Read_file(self):
        with open("C:\Matthew\Code\python\Code_Academy\Portfolio\Medical US Insurance Costs\python-portfolio-project-starter-files\insurance.csv", "r") as medical_insurance:
            reader = csv.DictReader(medical_insurance)
            data = []
            for row in reader:
                data.append(list((row["age"], row["sex"], row["bmi"], row["children"], row["smoker"], row["region"], row["charges"])))
            self.medical_information = data

    def Most_exspensive_region(self):
        info = self.medical_information
        charge = {
            "southeast": 0,
            "southwest": 0,
            "northeast": 0,
            "northwest": 0
        }
        for key in charge.keys():
            for lst in info:
                if key in lst:
                    charge[key] += float(lst[6])
            self.region_information[key].update({"Total cost": charge[key]})

        values_list = list(charge.values())
        keys_list = list(charge.keys())
        reversed_dictionary = dict(zip(values_list, keys_list))
        sorted(reversed_dictionary)
        return reversed_dictionary

    def total_individuals_per_region(self):
        info = self.medical_information
        total = {
            "southeast": 0,
            "southwest": 0,
            "northeast": 0,
            "northwest": 0
        }
        for key in total.keys():
            for lst in info:
                if key in lst:
                    total[key] += 1
            self.region_information[key].update({"Total people": total[key]})
        values_list = list(total.values())
        keys_list = list(total.keys())
        reversed_dictionary = dict(zip(values_list, keys_list))
        return reversed_dictionary

    def average_price_per_region(self):
        short = self.region_information
        total_costs = []
        total_people = []
        for key_one in short.keys():
            #total_costs.update({key_one:{}})
            for key_two, value in short[key_one].items():
                if "Total cost" == key_two:
                    #total_costs[key_one].update({key_two: value})
                    total_costs.append(value)
                if "Total people" == key_two:
                    #total_costs[key_one].update({key_two: value})
                    total_people.append(value)
        x = 0
        average_per_region = []
        for cost in total_costs:
            average_per_region.append(cost / total_people[x])
            x += 1
        cost_to_region = dict(zip(average_per_region, self.regions))
        y = 0
        for region in short.keys():
            short[region].update({"Average cost per person": average_per_region[y]})
            y += 1
        return cost_to_region

    def average_bmi(self):
        short = self.medical_information
        regions = {
            "southeast":[],
            "southwest":[],
            "northeast":[],
            "northwest":[]
        }
        total = 0
        average_bmi = []
        for lst in short:
            average_bmi.append(lst[2])
            total += float(lst[2])
            for region in regions.keys():
                if region in lst:
                    regions[region].append(lst[2])
        print(regions)



        overall_average = total / len(average_bmi)






obj = Obtain_file()
obj.Read_file()
most_exspensive = obj.Most_exspensive_region()
total_people = obj.total_individuals_per_region()
average_cost = obj.average_price_per_region()
print(obj.average_bmi())
