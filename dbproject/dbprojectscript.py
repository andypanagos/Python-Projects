          




import sqlite3

#establish a connection/cursor setup function

connection = sqlite3.connect('TextExtract.db')
with connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tbl_txt_file(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT,col_file TEXT)") #establish key with autoincrement, also with string value
    connection.commit()
connection.close()


fileList = ['information.docx','Hello.txt','myImage.png', \
            'Movie.txt','world.txt','data.pdf','myPhoto.jpg']

print(fileList)



newFileList = []

def extractFile():
    for filename in fileList:
        if '.txt' in filename:
           newFileList.append(filename)
extractFile()

print(newFileList)
#function that prints file names in a list with .txt

connection = sqlite3.connect('TextExtract.db')

with connection:
    cursor = connection.cursor()
    for file in fileList:
        if '.txt' in file:
            cursor.execute("INSERT INTO tbl_txt_file(col_file) VALUES (?)", (file,))
    connection.commit()
connection.close()
#adding auto increment primary integer to .txt files 


connection = sqlite3.connect('TextExtract.db')

with connection:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tbl_txt_file")
    varFile = cursor.fetchall()
    for item in varFile:
        message = f"File name: {item}"
    print(message)

if __name__ == '__main__':
    extractFile()
