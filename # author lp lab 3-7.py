# author lp lab 3-7

def determine_medal(points):
    if points >= 15:
        print("The team won the Gold Medal!")
    elif points >= 13:
        print("The team won the Silver Medal!")
    elif points >= 8:
        print("The team won the Bronze Medal!")
    else:
        print("The team did not earn a medal.")