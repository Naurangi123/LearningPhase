dict={
    "Brand":"TATA",
    "Model":"Safari",
    "year":"2020",
    "year":"2022"
}
# for h in dict:
#     print(h)

# print(dict["year"])

#Insert value in the dictionary
# dict["Model"]=45

# print(dict)

#Serach in dictionary
def searchDict(dict,value):
    for key in dict:
        if dict[key]==value:
            return key,value
    return("This value does't exist")

print(searchDict(dict, "Safari"))
