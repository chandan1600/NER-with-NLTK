import nltk

#inital global variables
fileIteration = 1
numIncrement = 1
orgCount = 0
personCount = 0
gpeCount = 0
orgList = ""
personList = ""
gpeList = ""

#all 28 files are being traversed
while fileIteration <= 28:
    print("****** File number: " + str(fileIteration) + " ******" + "\n")

    #all txt and dat files within larger files are traversed
    while numIncrement <= 5:

        #dat file is opened for reading
        datFile = open(
            "/Users/chandanaulakh/Desktop/TVTextExtract/" + str(fileIteration) + "/" + str(fileIteration) + "_" +
            str(numIncrement) + ".dat.txt", "r", encoding="mac_roman")
        datData = datFile.read()
        #count is taken for labels in dat files
        orgCount += datData.split().count("(ORGANISATION)")
        personCount += datData.split().count("(PERSON)")
        gpeCount += datData.split().count("(GPE)")
        datFile.close()

        #txt file is opened for reading
        txtFile = open("/Users/chandanaulakh/Desktop/TVTextExtract/" + str(fileIteration) + "/" + str(fileIteration) + "_" +
                       str(numIncrement) + ".txt", "r", encoding="mac_roman")
        txtData = txtFile.read()
        #txt file is chunked
        for chunk in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(txtData))):
            #labels are counted from chunking
            if hasattr(chunk, 'label'):
                if chunk.label() == "ORGANIZATION":
                    orgList += chunk.label() + " " + ' '.join(c[0] for c in chunk) + "\n"
                if chunk.label() == "PERSON":
                    personList += chunk.label() + " " + ' '.join(c[0] for c in chunk) + "\n"
                if chunk.label() == "GPE":
                    gpeList += chunk.label() + " " + ' '.join(c[0] for c in chunk) + "\n"
        txtFile.close()

        numIncrement += 1

    #count for DAT file values is shown
    print("-- DAT file extract values (actual) --")
    print("Organisation: "+ str(orgCount))
    print("Person: " + str(personCount))
    print("GPE: "+str(gpeCount) + "\n")
    #count for txt file values is shown
    print("-- TXT file extract values (predicted) --")
    print("Organisation: " + str(orgList.split().count("ORGANIZATION")))
    print("Person: " + str(personList.split().count("PERSON")))
    print("GPE: " + str(gpeList.split().count("GPE")) + "\n")

    #count values are reset for next file
    fileIteration += 1
    numIncrement = 1
    orgCount = 0
    personCount= 0
    gpeCount = 0
    orgList = ""
    personList = ""
    gpeList = ""