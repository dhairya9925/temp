# import json
# from models import sellerRegister


# # def update_json():
# #     # Open and update_json the JSON file
# #     with open('/workspaces/temp/ecom/sellerRegistration/countryCode.json', "r+") as file:
# #         data = json.load(file)
# #         names = []
# #         # sReg = sellerRegister(dialCode = code)
# #         # sReg.save()
# #         # for key in data:
# #         #     # count+=1
# #         #     if len(key) == 6:
# #         #         names.append((key["name"], key["dialCodes"]))
# #         #     else:
# #         #         names.append((key["name"], "Not Found"))
# #         #         print(f"country: {key["name"]}")
# #         #         data.remove(key)

# #         #         # Updating file
# #         #         with open("/workspaces/temp/ecom/sellerRegistration/countryCode.json", "w") as fp:
# #         #             fp.truncate()
# #         #             json.dump(data, fp, indent=6) # indent is for formating
                
# #     return data

# def insert():

#     with open('/workspaces/temp/ecom/sellerRegistration/countryCode.json', "r+") as file:
#         data = json.load(file)
#         # country = ""
#         # dialCode = ""
#         # image = ""
#         for val in data:
#             country = val["country"]
#             dialCodes = val["dialCode"]
#             image = val["image"]
#             if len(dialCode) > 1:
#                 for dialCode in dialCode:
#                     sReg = sellerRegister(country = country, dialCode = dialCode,image = image)
#                 print("--- More than 1 dialCode ---")
#             else:
#                 sReg = sellerRegister(country = country, dialCode = dialCodes[0],image = image)
#                 # sReg.save()
                

    
#     return 0

# insert()