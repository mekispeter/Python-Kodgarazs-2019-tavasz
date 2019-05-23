with open("tesztadatok.csv", "w", encoding = "utf-8") as outfile:
    for i in range(1, 12):
        with open("tesztadatok_"+str(i)+".txt", encoding = "utf-8") as infile:
            text = infile.read()

        for c in "nfkhp":
            text = text.replace (c, ","+c)

        text = text.replace("\n", ",tesztalany"+str(i)+"\n")

        outfile.write(text)
