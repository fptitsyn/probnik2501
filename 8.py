a = "ЛОПРСТ"
c = 0
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                    for a6 in a:
                        for a7 in a:
                            for a8 in a:
                                for a9 in a:
                                    b = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9
                                    if a1 == "О":
                                        if b.count("О") == 3 and b.count("Л") == 1 and b.count("С") == 1 and b.count("П") == 1 and b.count("Р") == 1 and b.count("Т") == 2:
                                            c += 1

print(c)