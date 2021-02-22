'''
Author- Drashti Shah
Date: 02/16/2020
'''

#Importing the package

from pymongo import MongoClient

# Connect MongoDB local host to Python MongoDB

client = MongoClient('mongodb://localhost:27017/')
db = client.virtual_library

############################################################
#1.Create 'ebooks_details' collection

#Create ebooks_array for inserting data in ebooks_details collection
#All details regarding publication and pages pertain to first publication in hardcover format

books_array=[
        {"Book_ID":1, "Title": "Homeland Elegies","Primary_author":"Ayad Akhtar",
         "Secondary_author":"NA","Date_of_First_Publication":"2020-09-15",
         "No_of_Pages": 368, "Publisher":"Little, Brown and Company", "Translator":"NA", 
         "Genre_of_Book":"Fiction", "Key_Topics":"Fiction"},
         
        {"Book_ID":2, "Title":"Having and Being Had", "Primary_Author":"Eula Bliss", 
         "Secondary_Author":"NA", "Date_of_First_Publication":"2020-09-01", 
         "No_of_Pages": 336, "Publisher":"Riverhead Books", "Translator":"NA", 
         "Genre_of_Book":"Non Fiction", "Key_Topics":["Consumption","Work","Investment","Accounting"]},
        
        {"Book_ID": 3, "Title":"Tiny Pretty Things", "Primary_Author":"Sona Charaipotra", 
         "Secondary_Author":"Dhonielle Clayton", "Date_of_First_Publication":"2016-07-12", 
         "No_of_Pages": 464, "Publisher":"HarperTeen", "Translator":"NA", 
         "Genre_of_Book":"Fiction", "Key_Topics":"Fiction"},
        
        {"Book_ID": 4, "Title":"Modelling", "Primary_Author":"Nelson N", 
         "Secondary_Author":"Dean", "Date_of_First_Publication":"1998-09-05", 
         "No_of_Pages": 500, "Publisher":"McGraw Hill", "Translator":"NA", 
         "Genre_of_Book":"Non Fiction", "Key_Topics":"Machine Learning"}]

# Insert the data array into the collection
eBooks_details = db.eBooks_details.insert_many(books_array)

############################################################

#2.Create 'user_info' collection

#Create user_array for inserting data in user_info collection

users_array = [
        {"User_ID": 100, "Name":"Drashti Shah", "Phone": 7166030752, 
         "Address":"58 Windfall St", "University_Affiliation":"Columbia University"},
         
         {"User_ID": 200, "Name":"Thirth Patel", "Phone": 4567896400, 
          "Address":"688 Stillwater Avenue", "University_Affiliation":"New York University"},
         
         {"User_ID": 300, "Name":"Steven Young", "Phone": 5678767777, 
          "Address":"6 Alberta Dr", "University_Affiliation":"State University of New York at Buffalo"},
         
         {"User_ID": 400, "Name":"Karin Cho", "Phone": 7777777777, 
          "Address":"591 Grand Avenue", "University_Affiliation":"University of California"},
         
         {"User_ID": 500, "Name":"Ornwipa Taeng-aksorn", "Phone": 6740932919, 
          "Address":"5 Lafayette Lane", "University_Affiliation":"New York University"},
         
         {"User_ID": 600, "Name":"Gita Denaya Rizkianto", "Phone": 789000611, 
          "Address":"210 13th St", "University_Affiliation":"Columbia University"},
         
         {"User_ID": 700, "Name":"Sarthak Chakravarty", "Phone": 5467890000, 
          "Address":"8301 Magnolia St", "University_Affiliation":"University of Houston"},
         ]

# Insert the data array into the collection
user_info = db.user_info.insert_many(users_array)


############################################################

#3.Create 'checkout_details' collection

# Create array for inserting data into the collection 'checkout_details'
checkout_array = [
        {"Checkout_ID": 11111, "Book_ID": 1, "Title":"Homeland Elegies", 
         "Key_Topics":"Fiction", "User_ID": 100, "Name":"Drashti Shah", 
         "University_Affiliation":"Columbia University", "Checkout_Date":"2020-09-06",
         },
        
        {"Checkout_ID": 22222, "Book_ID": 2, "Title":"Having and Being Had", 
         "Key_Topics":["Consumption","Work","Investment","Accounting"], "User_ID": 200, "User_Name":"Thirth Patel", 
         "University_Affiliation":"New York University", "Checkout_Date":"2020-10-01",
         },
        
        {"Checkout_ID": 33333, "Book_ID": 3, "Title":"Tiny Pretty Things", 
         "Key_Topics":"Fiction", "User_ID": 300, "User_Name":"Steven Young", 
         "University_Affiliation":"State University of New York at Buffalo", "Checkout_Date":"2020-11-30",
         },
        
        {"Checkout_ID": 44444, "Book_ID": 4, "Title":"Modelling", 
         "Key_Topics":"Machine Learning", "User_ID": 400, "User_Name":"Karin Cho", 
         "University_Affiliation":"University of California", "Checkout_Date":"2020-12-10",
         },
        
        {"Checkout_ID": 55555, "Book_ID": 1, "Title":"Homeland Elegies", 
         "Key_Topics":"Fiction", "User_ID": 500, "User_Name":"Ornwipa Taeng-aksorn", 
         "University_Affiliation":"New York University", "Checkout_Date":"2021-01-02",
         },
        
        {"Checkout_ID": 66666, "Book_ID": 2, "Title":"Having and Being Had", 
         "Key_Topics":["Consumption","Work","Investment","Accounting"], "User_ID": 600, 
         "User_Name":"Gita Denaya Rizkianto","University_Affiliation":"Columbia University",
         "Checkout_Date":"2021-02-11",
          },
        
        {"Checkout_ID": 77777, "Book_ID": 3, "Title":"Tiny Pretty Things", 
         "Key_Topics":"Fiction", "User_ID": 700, "User_Name":"Sarthak Chakravarty", 
         "University_Affiliation":"University of Houston", "Checkout_Date":"2021-02-15",
         },
        
        {"Checkout_ID": 88888, "Book_ID": 4, "Title":"Modelling", 
         "Key_Topics":"Machine Learning", "User_ID": 100, "User_Name":"Drashti Shah", 
         "University_Affiliation":"Columbia University", "Checkout_Date":"2021-02-15",
         }
        ]

# Insert the data array into the collection
checkout_details = db.checkout_details.insert_many(checkout_array)


############################################################

# Question 1:Which books have been checked out since such and such date

#I have selected the date 15th Feb, 2021

checkout_details = db.checkout_details

#$gte wil give greater than or equal to the Checkout-Date 

for book in checkout_details.distinct("Title", {"$and": [{"Checkout_Date":{
        "$gte":"2021-02-15"}}]}):
    print(book)
    
############################################################

# Question 2:Which users have checked out such and such book

#I selected book title- Having and Being Had
for names in checkout_details.distinct("User_Name",
                                       {"$and": [{"Title":"Having and Being Had"}]}):
    print(names)

############################################################
    
# Question 3:How many books does the library have on such and such topic
   
#Genre-wise-I selected Genre-Fiction
eBooks_details=db.eBooks_details

print(db.eBooks_details.count_documents({"Genre_of_Book":"Fiction"}))


#Key Topics wise
#It works with selecting all key_topics in a document
print(db.eBooks_details.count_documents({"Key_Topics":["Consumption",
                                                       "Work","Investment","Accounting"]}))

#It also works with selecting one out of many topics in the document
print(db.eBooks_details.count_documents({"Key_Topics":"Consumption"}))

# Question 4:Which users from Columbia University have checked out books on 
# Machine Learning between this date and that date

#I have selected dates between Aug, 2020 and Feb, 2021

for users in checkout_details.distinct("User_Name",
                                    {"$and":[{"Key_Topics":"Machine Learning"},
                                    {"Checkout_Date":{"$gte":"2020-08-01"}},
                                    {"Checkout_Date":{"$lte":"2021-02-28"}},
                                    {"University_Affiliation":"Columbia University"}]}):
    print(users)
    
