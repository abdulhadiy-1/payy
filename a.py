def pul_otkazish(pul, raqam, wallet):
    if float(pul) > float(wallet):
        return "Not enough money in the wallet"

    updated = False
    new_lines = []
    wallet = float(wallet) 
    with open("cards.txt", 'r') as f:
        lines = f.readlines()

    for line in lines:
        lst = line.strip().split(",")
        if lst[2] == raqam:
            lst[-1] = str(float(lst[-1]) + float(pul))  
            with open("history.txt", 'a') as file:
                file.write(f"{lst[1]} ga {pul} som o'tkazildi\n") 
            wallet -= float(pul) 
            updated = True
        new_lines.append(",".join(lst) + "\n")

    with open("cards.txt", 'w') as f:
        f.writelines(new_lines)  
    if updated:
        return "Money transferred successfully"
    else:
        return "Card not found"
