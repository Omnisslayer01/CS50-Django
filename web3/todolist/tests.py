from django.test import TestCase

# Create your tests here.
temp={"tasks":[]}
temp["tasks"].append("Nigeria")
temp["tasks"]+=["water"]
temp["tasks"]+=["China"]

print(temp["tasks"])