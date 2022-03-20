for cock in range(0,21,1):
    for hen in range(0,33,1):
        for biddy in range(0,99,1):
            if 5*cock + 3*hen + biddy/3 == 100:
                if cock + hen + biddy == 100:
                    if biddy%3 == 0:
                        print("cock",cock,"hen",hen,"biddy",biddy)